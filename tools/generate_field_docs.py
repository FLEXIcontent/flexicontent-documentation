#!/usr/bin/env python3
"""Generate the FLEXIcontent field types documentation.

Sources (official FLEXIcontent 5.x):
  tools/sources/fields/*.xml                       -> plugins/flexicontent_fields/*/<type>.xml
  tools/sources/fields/lang/en-GB/*.ini            -> plugin English language files
  tools/sources/fields/lang/fr-FR/*.ini            -> plugin French language files (Crowdin)
  tools/sources/en-GB.com_flexicontent.ini         -> component English language file
  tools/sources/fr-FR.com_flexicontent.ini         -> component French language file

One page is generated per field type, plus an overview page. English sources live in
docs/fields/, French translations in i18n/fr/docusaurus-plugin-content-docs/current/fields/.
"""
import html
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import fr_translations

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / 'tools' / 'sources'
PLUGIN_DIR = SOURCES / 'fields'
DOC_EN = ROOT / 'docs' / 'fields'
DOC_FR = ROOT / 'i18n' / 'fr' / 'docusaurus-plugin-content-docs' / 'current' / 'fields'

# type -> (English name, French name, category)
FIELDS = {
    'account_via_submit': ('User account via submit', 'Compte utilisateur via le formulaire', 'Relations & users'),
    'addressint': ('International address / Google Maps', 'Adresse internationale / Google Maps', 'Text & basic'),
    'authoritems': ('Author items', 'Contenus de l’auteur', 'Relations & users'),
    'checkbox': ('Checkbox', 'Case à cocher', 'Choices & tags'),
    'checkboximage': ('Checkbox image', 'Case à cocher avec image', 'Choices & tags'),
    'color': ('Color', 'Couleur', 'Text & basic'),
    'comments': ('Comments', 'Commentaires', 'Layout & structure'),
    'core': ('Core fields (Joomla)', 'Champs cœur (Joomla)', 'Layout & structure'),
    'coreprops': ('Core property', 'Propriété cœur', 'Layout & structure'),
    'custom_form_html': ('Custom HTML / form tab', 'HTML personnalisé / onglet de formulaire', 'Layout & structure'),
    'date': ('Date / timestamp', 'Date / horodatage', 'Text & basic'),
    'email': ('Email', 'E-mail', 'Text & basic'),
    'fcloadmodule': ('Load module', 'Charger un module', 'Layout & structure'),
    'fcpagenav': ('Page navigation', 'Navigation entre contenus', 'Layout & structure'),
    'fieldgroup': ('Field group (repeatable)', 'Groupe de champs (répétable)', 'Layout & structure'),
    'file': ('File', 'Fichier', 'Files & media'),
    'image': ('Image / gallery', 'Image / galerie', 'Files & media'),
    'jprofile': ('User profile', 'Profil utilisateur', 'Relations & users'),
    'linkslist': ('Links list', 'Liste de liens', 'Text & basic'),
    'mediafile': ('Media file', 'Fichier multimédia', 'Files & media'),
    'phonenumbers': ('International phone numbers', 'Numéros de téléphone internationaux', 'Text & basic'),
    'radio': ('Radio', 'Bouton radio', 'Choices & tags'),
    'radioimage': ('Radio image', 'Bouton radio avec image', 'Choices & tags'),
    'relation': ('Relation', 'Relation', 'Relations & users'),
    'relation_reverse': ('Reverse relation', 'Relation inverse', 'Relations & users'),
    'select': ('Select', 'Liste déroulante', 'Choices & tags'),
    'selectmultiple': ('Select multiple', 'Liste à choix multiples', 'Choices & tags'),
    'sharedmedia': ('Shared video / audio', 'Vidéo / audio partagé', 'Files & media'),
    'subform': ('Subform', 'Sous-formulaire', 'Layout & structure'),
    'termlist': ('Term list', 'Liste de termes', 'Choices & tags'),
    'text': ('Text', 'Texte', 'Text & basic'),
    'textarea': ('Textarea', 'Zone de texte', 'Text & basic'),
    'textselect': ('Text select', 'Texte avec liste', 'Text & basic'),
    'toolbar': ('Toolbar', 'Barre d’outils', 'Layout & structure'),
    'weblink': ('Web link', 'Lien web', 'Text & basic'),
}

CATEGORY_FR = {
    'Text & basic': 'Texte et basique',
    'Choices & tags': 'Choix et étiquettes',
    'Files & media': 'Fichiers et médias',
    'Relations & users': 'Relations et utilisateurs',
    'Layout & structure': 'Mise en page et structure',
}

HEADERS = {
    'en': ['Option', 'Description', 'Type', 'Values', 'Default'],
    'fr': ['Option', 'Description', 'Type', 'Valeurs', 'Défaut'],
}


def load_ini(path):
    data = {}
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith(';') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def build_lang(lang):
    prefix = 'en-GB' if lang == 'en' else 'fr-FR'
    table = {}
    main = SOURCES / f'{prefix}.com_flexicontent.ini'
    table.update(load_ini(main))
    for path in sorted((PLUGIN_DIR / 'lang' / prefix).glob('*.ini')):
        table.update(load_ini(path))
    return table


LANG = {'en': build_lang('en'), 'fr': build_lang('fr')}

KEY_RE = re.compile(r'\b((?:FLEXI|PLG|J)[A-Z0-9_]{3,})\b')


def tr(value, lang, depth=0):
    """Resolve a language key, recursively resolving nested keys inside its value."""
    if not value:
        return ''
    table = LANG[lang]
    resolved = table.get(value, value)
    if depth < 2 and resolved != value:
        return tr(resolved, lang, depth + 1)
    if depth == 0:
        # Resolve embedded keys in literal strings (e.g. "Use FLEXI_YES to ...")
        resolved = KEY_RE.sub(lambda m: table.get(m.group(1), m.group(1)), resolved)
    return resolved


def clean(text):
    """Turn Joomla INI / XML markup into Markdown-safe table text."""
    if not text or text in ('..', '...'):
        return '—'
    text = html.unescape(text)
    text = re.sub(r'<br\s*/?>', ' ', text, flags=re.I)
    text = re.sub(r'</?(b|strong|em|i)>', '**', text, flags=re.I)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace('|', '\\|')
    text = text.replace('<', '&lt;').replace('>', '&gt;')
    text = text.replace('{', '&#123;').replace('}', '&#125;')
    text = text.replace('`', '&#96;')
    return text


def label_of(text, lang):
    return clean(tr(text, lang))


def fmt_values(element, lang):
    opts = []
    for option in element.findall('option'):
        value = clean(option.get('value', ''))
        label = label_of(option.text, lang)
        opts.append(f"`{value}` = {label}" if label else f"`{value}`")
    for group in element.findall('group'):
        group_label = label_of(group.get('label'), lang)
        sub = []
        for option in group.findall('option'):
            value = clean(option.get('value', ''))
            label = label_of(option.text, lang)
            sub.append(f"`{value}` = {label}" if label else f"`{value}`")
        if sub:
            prefix = f"**{group_label}**<br />" if group_label else ''
            opts.append(prefix + '<br />'.join(sub))
    return '<br />'.join(opts) if opts else '—'


def fmt_default(element, lang):
    default = clean(element.get('default', ''))
    if not default or default == '—':
        return '—'
    labels = {}
    for option in element.findall('option'):
        labels[clean(option.get('value', ''))] = option.text
    for group in element.findall('group'):
        for option in group.findall('option'):
            labels[clean(option.get('value', ''))] = option.text
    if default in labels:
        label = label_of(labels[default], lang)
        return f"`{default}` ({label})" if label else f"`{default}`"
    resolved = tr(element.get('default', ''), lang)
    if resolved != element.get('default', '') and len(resolved) < 80:
        return f"`{default}` ({clean(resolved)})"
    return f"`{default}`"


def render_fieldset(fieldset, lang):
    lines = []
    title = label_of(fieldset.get('label'), lang)
    if title:
        lines += [f'## {title}', '']
    desc = label_of(fieldset.get('description'), lang)
    if desc and desc != '—':
        lines += [desc, '']

    table = []

    def flush():
        if table:
            lines.append('| ' + ' | '.join(HEADERS[lang]) + ' |')
            lines.append('| ' + ' | '.join(['---'] * len(HEADERS[lang])) + ' |')
            lines.extend(table)
            lines.append('')
            table.clear()

    for element in fieldset:
        if element.tag != 'field':
            continue
        ftype = element.get('type', '')
        if ftype == 'separator':
            flush()
            text = label_of(element.get('default'), lang)
            if text == '—':
                continue
            desc = label_of(element.get('description'), lang)
            level = element.get('level', '')
            css = element.get('class', '')
            is_note = level == 'level4' or 'alert' in css or len(text) > 180
            if is_note:
                lines += [':::note', text]
                if desc != '—':
                    lines.append(desc)
                lines += [':::', '']
            elif level == 'tab_open':
                lines += [f'### {text}', '']
            elif level in ('level0', 'level1'):
                lines += [f'### {text}', '']
            else:
                lines += [f'#### {text}', '']
            continue

        name = element.get('name', '')
        if not name:
            continue
        label = label_of(element.get('label'), lang)
        desc = label_of(element.get('description'), lang)
        display = f'**{label}**<br />`{name}`' if label and label != '—' else f'`{name}`'
        hint = label_of(element.get('hint'), lang)
        if hint != '—':
            desc = (desc + ' ' if desc != '—' else '') + f'_{hint}_'
        table.append(
            f"| {display} | {desc} | `{ftype}` | {fmt_values(element, lang)} | {fmt_default(element, lang)} |"
        )

    flush()
    return '\n'.join(lines).rstrip()


def render_page(field_type, lang, position):
    xml = PLUGIN_DIR / f'{field_type}.xml'
    root = ET.parse(xml).getroot()
    en_name, fr_name, _ = FIELDS[field_type]
    title = fr_name if lang == 'fr' else en_name

    raw_name = tr(root.findtext('name', ''), lang)
    raw_name = re.sub(r'^FLEXIcontent\s+-\s*', '', raw_name)
    raw_name = re.sub(r'\s*\([^)]*\)\s*$', '', raw_name)
    description = label_of(root.findtext('description', ''), lang)

    lines = [
        '---',
        f'sidebar_position: {position}',
        '---',
        '',
        f'# {title}',
        '',
    ]
    if description and description != '—':
        lines += [description, '']
    if raw_name and raw_name != title:
        lines += [f'*Plugin : `{field_type}` — {raw_name}*', '']
    lines += [
        ':::info Source',
        ('Cette page est générée depuis `plugins/flexicontent_fields/' + field_type + '/' + field_type + '.xml` '
         'et les fichiers de langue officiels de FLEXIcontent 5.x.'
         if lang == 'fr' else
         'This page is generated from `plugins/flexicontent_fields/' + field_type + '/' + field_type + '.xml` '
         'and the official FLEXIcontent 5.x language files.'),
        ':::',
        '',
    ]

    fieldsets = root.findall('./config/fields/fieldset')
    for fieldset in fieldsets:
        block = render_fieldset(fieldset, lang)
        if block:
            lines += [block, '']

    return '\n'.join(lines).rstrip() + '\n'


def render_overview(lang, stats):
    fr = lang == 'fr'
    lines = [
        '---',
        'sidebar_position: 1',
        '---',
        '',
        '# Champs' if fr else '# Fields',
        '',
        ('Les champs sont les types de contenus personnalisés de FLEXIcontent. Chaque type est fourni par un plugin '
         'et propose ses propres options d’édition, d’affichage, de référencement et de filtrage.'
         if fr else
         'Fields are the custom content types of FLEXIcontent. Each type is provided by a plugin and offers its '
         'own editing, viewing, SEO and filtering options.'),
        '',
        ('Ajoutez un champ depuis **Composants → FLEXIcontent → Champs**, puis choisissez son type. '
         'Les options disponibles dépendent du type sélectionné.'
         if fr else
         'Add a field from **Components → FLEXIcontent → Fields**, then choose its type. '
         'The available options depend on the selected type.'),
        '',
        ':::info Source' if fr else ':::info Source',
        ('Ces pages sont générées depuis les manifests XML des plugins de champs et les fichiers de langue '
         'officiels anglais et français de FLEXIcontent 5.x.'
         if fr else
         'These pages are generated from the field plugin XML manifests and the official English and French '
         'language files of FLEXIcontent 5.x.'),
        ':::',
        '',
    ]

    for category in ['Text & basic', 'Choices & tags', 'Files & media', 'Relations & users', 'Layout & structure']:
        cat_title = CATEGORY_FR[category] if fr else category
        lines += [f'## {cat_title}', '']
        lines += [
            '| ' + ('Type | Description | Options' if fr else 'Type | Description | Options') + ' |',
            '| --- | --- | --- |',
        ]
        for field_type in sorted(t for t, v in FIELDS.items() if v[2] == category):
            name = FIELDS[field_type][1] if fr else FIELDS[field_type][0]
            root = ET.parse(PLUGIN_DIR / f'{field_type}.xml').getroot()
            desc = label_of(root.findtext('description', ''), lang)
            if desc != '—' and len(desc) > 140:
                desc = desc[:137].rstrip() + '…'
            lines.append(f'| [{name}](./{field_type}.md) | {desc} | {stats[field_type]} |')
        lines.append('')

    return '\n'.join(lines).rstrip() + '\n'


def main():
    DOC_EN.mkdir(parents=True, exist_ok=True)
    DOC_FR.mkdir(parents=True, exist_ok=True)

    stats = {}
    for field_type in FIELDS:
        root = ET.parse(PLUGIN_DIR / f'{field_type}.xml').getroot()
        stats[field_type] = sum(len(fs.findall('field')) for fs in root.findall('./config/fields/fieldset'))

    (DOC_EN / 'index.md').write_text(render_overview('en', stats), encoding='utf-8')
    (DOC_FR / 'index.md').write_text(
        fr_translations.translate_content(render_overview('fr', stats)), encoding='utf-8'
    )

    for position, field_type in enumerate(sorted(FIELDS), start=2):
        en = render_page(field_type, 'en', position)
        fr = fr_translations.translate_content(render_page(field_type, 'fr', position))
        (DOC_EN / f'{field_type}.md').write_text(en, encoding='utf-8')
        (DOC_FR / f'{field_type}.md').write_text(fr, encoding='utf-8')
        print(f'{field_type:22s} {stats[field_type]:4d} options  EN={len(en):6d} FR={len(fr):6d}')

    print(f'\nTotal: {sum(stats.values())} options across {len(FIELDS)} field types')


if __name__ == '__main__':
    main()
