#!/usr/bin/env python3
"""Generate documentation for content types, categories, menu links and templates.

Sources (official FLEXIcontent 5.x), copied into tools/sources/:
  forms/type.xml, forms/category.xml             -> admin/models/forms/
  menu/*.xml                                     -> site/views/*/tmpl/*.xml
  templatesforms/*.xml                           -> site/templates/*/<view>.xml
  extra-lang/                                    -> component, site and template language files

Reuses the language resolution and Markdown rendering of generate_field_docs.py.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fr_translations  # noqa: E402
import generate_field_docs as g  # noqa: E402

ROOT = HERE.parent
SOURCES = HERE / 'sources'
DOC_EN = ROOT / 'docs'
DOC_FR = ROOT / 'i18n' / 'fr' / 'docusaurus-plugin-content-docs' / 'current'

# Extend the language tables with component sys, site and template language files.
for lang, prefix in (('en', 'en-GB'), ('fr', 'fr-FR')):
    for path in sorted((SOURCES / 'extra-lang' / prefix).glob('*.ini')):
        g.LANG[lang].update(g.load_ini(path))

ORIGINAL_TR = g.tr

FALLBACK = {
    'JGLOBAL_FIELDSET_METADATA_OPTIONS': ('Metadata options', 'Options des métadonnées'),
    'JFIELD_TITLE_DESC': ('The title of the content', 'Le titre du contenu'),
    'JFIELD_ALIAS_DESC': ('The alias used in the URL', 'L’alias utilisé dans l’URL'),
    'JFIELD_ACCESS_DESC': ('The access level of the content', 'Le niveau d’accès du contenu'),
    'JFIELD_PUBLISHED_DESC': ('Whether the content is published', 'Indique si le contenu est publié'),
    'JFIELD_META_DESCRIPTION_LABEL': ('Meta description', 'Description méta'),
    'JFIELD_META_DESCRIPTION_DESC': ('A short description used by search engines', 'Une courte description utilisée par les moteurs de recherche'),
    'JFIELD_META_KEYWORDS_LABEL': ('Meta keywords', 'Mots-clés méta'),
    'JFIELD_META_KEYWORDS_DESC': ('Comma separated list of keywords', 'Liste de mots-clés séparés par des virgules'),
    'JFIELD_RULES_LABEL': ('Permissions', 'Permissions'),
    'JFIELD_RULES_DESC': ('Permissions for this item', 'Permissions pour ce contenu'),
    'JGLOBAL_CREATED': ('Created', 'Créé'),
    'JGLOBAL_MODIFIED': ('Modified', 'Modifié'),
    'JGLOBAL_HITS': ('Hits', 'Vues'),
    'JGLOBAL_DESCRIPTION': ('Description', 'Description'),
    'JGLOBAL_FIELD_ID_LABEL': ('ID', 'ID'),
    'JGLOBAL_FIELD_ID_DESC': ('The internal identifier', 'L’identifiant interne'),
    'JGLOBAL_FIELD_CREATED_BY_LABEL': ('Created by', 'Créé par'),
    'JGLOBAL_FIELD_MODIFIED_BY_LABEL': ('Modified by', 'Modifié par'),
}


def tr(value, lang, depth=0):
    if not value:
        return ''
    key = str(value).strip()
    resolved = ORIGINAL_TR(key, lang)
    if resolved != key:
        return resolved
    if key in FALLBACK:
        return FALLBACK[key][0 if lang == 'en' else 1]
    if re.fullmatch(r'[A-Z][A-Z0-9_]{2,}', key):
        words = re.sub(r'^(FLEXI|COM|JGLOBAL|JFIELD|PLG|J)_', '', key)
        words = re.sub(r'^(FLEXICONTENT|CATEGORIES|CONTENT)_', '', words)
        return words.replace('_', ' ').capitalize()
    return key


g.tr = tr  # make g.render_fieldset() and g.label_of() use the fallback

FIELDSET_TITLES = {
    'basic': ('Basic', 'Basique'),
    'cats_display': ('Category display', 'Affichage des catégories'),
    'cat_search_filter_form': ('Search & filter form', 'Formulaire de recherche et filtrage'),
    'cat_items_list': ('Items list', 'Liste des contenus'),
    'cat_rss_feeds': ('RSS feeds', 'Flux RSS'),
    'request': ('Required parameters', 'Paramètres requis'),
    'attribs': ('Template parameters', 'Paramètres du modèle'),
    'jmetadata': ('Metadata options', 'Options des métadonnées'),
    'cats_params_set': ('Category parameters', 'Paramètres de catégorie'),
    'params-basic': ('Basic parameters', 'Paramètres basiques'),
    'params-advanced': ('Advanced parameters', 'Paramètres avancés'),
    'params-seoconf': ('SEO parameters', 'Paramètres SEO'),
    'notifications_conf': ('Notifications', 'Notifications'),
    'cat_notifications_conf': ('Category notifications', 'Notifications des catégories'),
    'editing': ('Authoring', 'Rédaction'),
    'viewing': ('Viewing', 'Apparence'),
    'search_view': ('Search view', 'Vue de recherche'),
    'frontend_item_form': ('Frontend item form', 'Formulaire contenu frontend'),
    'items_manager': ('Items manager', 'Gestionnaire de contenus'),
    'themes': ('Themes', 'Modèles'),
    'seo': ('SEO', 'SEO'),
}

SECTION_FR = {
    'Basic': 'Basique', 'Category display': 'Affichage des catégories',
    'Search & filter form': 'Formulaire de recherche et filtrage', 'Items list': 'Liste des contenus',
    'RSS feeds': 'Flux RSS', 'Required parameters': 'Paramètres requis',
    'Template parameters': 'Paramètres du modèle', 'Metadata options': 'Options des métadonnées',
}


def title_for(fieldset, lang):
    label = fieldset.get('label', '')
    resolved = ORIGINAL_TR(label, lang)
    if label and resolved != label and resolved not in ('', '—'):
        title = g.clean(resolved).replace('**', '').strip()
        return title.strip('[]').strip()
    name = fieldset.get('name', '')
    if name in FIELDSET_TITLES:
        return FIELDSET_TITLES[name][0 if lang == 'en' else 1]
    return name.replace('-', ' ').replace('_', ' ').capitalize() if name else ''


def render_xml(xml_path, lang, only=None):
    """Render all fieldsets of an XML file. `only` is a set of field names to keep."""
    root = ET.parse(xml_path).getroot()
    blocks = []
    for fieldset in root.findall('.//fieldset'):
        fs = ET.fromstring(ET.tostring(fieldset, encoding='unicode'))
        if only is not None:
            children = list(fs)
            keep = []
            for i, child in enumerate(children):
                if child.tag != 'field':
                    keep.append(child)
                    continue
                if child.get('type') == 'separator':
                    # Keep the separator only if a retained field follows before the next separator
                    following = [c for c in children[i + 1:] if c.tag == 'field']
                    next_sep = next((j for j, c in enumerate(following) if c.get('type') == 'separator'), len(following))
                    if any(c.get('name') in only for c in following[:next_sep]):
                        keep.append(child)
                elif child.get('name') in only:
                    keep.append(child)
            for child in children:
                fs.remove(child)
            for child in keep:
                fs.append(child)
        if only is not None and not any(
            c.tag == 'field' and c.get('type') != 'separator' and c.get('name') in only for c in fs
        ):
            continue
        label = title_for(fieldset, lang)
        fs.set('label', label)
        block = g.render_fieldset(fs, lang)
        if block and block.strip():
            blocks.append(block)
    return '\n\n'.join(blocks)


def option_rows(xml_path):
    root = ET.parse(xml_path).getroot()
    return len([f for f in root.findall('.//field') if f.get('name') and f.get('type') != 'separator'])


def make_page(lang, position, title, intro, blocks, source):
    lines = [
        '---',
        f'sidebar_position: {position}',
        '---',
        '',
        f'# {title}',
        '',
        intro,
        '',
        ':::info Source',
        source,
        ':::',
        '',
    ]
    for block in blocks:
        lines += [block, '']
    return '\n'.join(lines).rstrip() + '\n'


def src_line(lang, paths):
    prefix = 'Cette page est générée depuis' if lang == 'fr' else 'This page is generated from'
    suffix = 'et les fichiers de langue officiels de FLEXIcontent 5.x.' if lang == 'fr' else 'and the official FLEXIcontent 5.x language files.'
    return f"{prefix} {', '.join('`' + p + '`' for p in paths)} {suffix}"


def write(section, slug, lang, content):
    base = DOC_EN if lang == 'en' else DOC_FR
    path = base / section / f'{slug}.md'
    path.parent.mkdir(parents=True, exist_ok=True)
    if lang == 'fr':
        content = fr_translations.translate_content(content)
    path.write_text(content, encoding='utf-8')
    return path


# ---------------------------------------------------------------- metadata

CONTENT_TYPES_INTRO = {
    'en': 'A content type defines the fields, authoring rules and display settings available to a category of items. Open a type from **Components → FLEXIcontent → Content Types**.',
    'fr': 'Un type de contenu définit les champs, les règles de rédaction et les paramètres d’affichage disponibles pour une catégorie de contenus. Ouvrez un type depuis **Composants → FLEXIcontent → Types de contenu**.',
}
CATEGORIES_INTRO = {
    'en': 'FLEXIcontent categories add their own display, filtering, list and RSS settings on top of the standard Joomla! category fields. Open them from **Components → FLEXIcontent → Categories**.',
    'fr': 'Les catégories FLEXIcontent ajoutent leurs propres paramètres d’affichage, de filtrage, de liste et de flux RSS aux champs standard des catégories Joomla!. Ouvrez-les depuis **Composants → FLEXIcontent → Catégories**.',
}
MENU_INTRO = {
    'en': 'Menu link types define the parameters available when creating a FLEXIcontent menu item in **Menus → Add Menu Item**. The category-based views share a common set of options.',
    'fr': 'Les types de liens de menu définissent les paramètres disponibles lors de la création d’un élément de menu FLEXIcontent dans **Menus → Ajouter un élément**. Les vues basées sur les catégories partagent un ensemble d’options commun.',
}
TEMPLATES_INTRO = {
    'en': 'FLEXIcontent ships with four layouts (templates). Each template provides its own parameters for the item view and, for most of them, for the category view as well.',
    'fr': 'FLEXIcontent fournit quatre mises en page (modèles). Chaque modèle propose ses propres paramètres pour la vue contenu et, pour la plupart, pour la vue catégorie.',
}

MENU_PAGES = [
    ('category-common', 'category-default.xml', 'Category views — common options', 'Vues catégorie — options communes',
     'Options shared by all category-based menu item types: category, multi-category, author, tagged, favourites and my items.',
     'Options communes à tous les types d’éléments de menu basés sur les catégories : catégorie, multi-catégories, auteur, étiquettes, favoris et mes contenus.'),
    ('category-author', 'category-author.xml', "Author's items", 'Contenus d’un auteur', '', ''),
    ('category-favs', 'category-favs.xml', 'Favourite items (category view)', 'Favoris (vue catégorie)', '', ''),
    ('category-mcats', 'category-mcats.xml', 'Multi-category view', 'Vue multi-catégories', '', ''),
    ('category-myitems', 'category-myitems.xml', 'My items', 'Mes contenus', '', ''),
    ('category-tags', 'category-tags.xml', 'Tagged items (category view)', 'Contenus étiquetés (vue catégorie)', '', ''),
    ('main', 'flexicontent-default.xml', 'Directory (main view)', 'Annuaire (vue principale)', '', ''),
    ('item', 'item-default.xml', 'Content item', 'Vue contenu', '', ''),
    ('item-form', 'item-form.xml', 'Item submission form', 'Formulaire de soumission', '', ''),
    ('search', 'search-default.xml', 'Search', 'Recherche', '', ''),
    ('favourites', 'favourites-default.xml', 'Favourites (legacy view)', 'Favoris (ancienne vue)', '', ''),
    ('tagged-items', 'tags-default.xml', 'Tagged items (legacy view)', 'Contenus étiquetés (ancienne vue)', '', ''),
    ('tasks', 'tasks-default.xml', 'Tasks', 'Tâches', '', ''),
]

CATEGORY_VIEWS = {'category-author', 'category-favs', 'category-mcats', 'category-myitems', 'category-tags'}

TEMPLATE_PAGES = [
    ('item', 'faq-item.xml', 'Item template — common options', 'Modèle contenu — options communes',
     'Item template parameters. They are identical for all four templates (faq, grid, items-tabbed and table).',
     'Paramètres du modèle contenu. Ils sont identiques pour les quatre modèles (faq, grid, items-tabbed et table).'),
    ('category-faq', 'faq-category.xml', 'FAQ — category view', 'FAQ — vue catégorie', '', ''),
    ('category-grid', 'grid-category.xml', 'Grid — category view', 'Grid — vue catégorie', '', ''),
    ('category-items-tabbed', 'items-tabbed-category.xml', 'Items tabbed — category view', 'Items tabbed — vue catégorie', '', ''),
    ('category-table', 'table-category.xml', 'Table — category view', 'Table — vue catégorie', '', ''),
]

TEMPLATES = [
    ('faq', 'FAQ', 'Regroupe et affiche les contenus par questions/réponses', 'Groups and displays items as questions/answers'),
    ('grid', 'Grid', 'Disposition en colonnes avec mosaïque', 'Columned layout with tiling ability'),
    ('items-tabbed', 'Items tabbed', 'Contenus présentés sous forme d’onglets', 'Items displayed as tabs'),
    ('table', 'Table', 'Contenus présentés sous forme de tableau', 'Items displayed as a table'),
]


def main():
    total = 0

    # ---- Content types
    for lang in ('en', 'fr'):
        blocks = [render_xml(SOURCES / 'forms' / 'type.xml', lang)]
        content = make_page(
            lang, 2,
            'Content types — options' if lang == 'en' else 'Types de contenu — options',
            CONTENT_TYPES_INTRO[lang], blocks,
            src_line(lang, ['admin/models/forms/type.xml']),
        )
        write('content-types', 'options', lang, content)
    total += option_rows(SOURCES / 'forms' / 'type.xml')

    # ---- Categories
    for lang in ('en', 'fr'):
        blocks = [render_xml(SOURCES / 'forms' / 'category.xml', lang)]
        content = make_page(
            lang, 2,
            'Categories — options' if lang == 'en' else 'Catégories — options',
            CATEGORIES_INTRO[lang], blocks,
            src_line(lang, ['admin/models/forms/category.xml']),
        )
        write('categories', 'options', lang, content)
    total += option_rows(SOURCES / 'forms' / 'category.xml')

    # ---- Menu links
    reference = SOURCES / 'menu' / 'category-default.xml'
    ref_root = ET.parse(reference).getroot()
    ref_names = {f.get('name') for f in ref_root.findall('.//field') if f.get('name') and f.get('type') != 'separator'}
    menu_stats = {}
    menu_unique = {}
    for slug, xml_name, _, _, _, _ in MENU_PAGES:
        root = ET.parse(SOURCES / 'menu' / xml_name).getroot()
        names = {f.get('name') for f in root.findall('.//field') if f.get('name') and f.get('type') != 'separator'}
        menu_unique[slug] = names - ref_names if slug in CATEGORY_VIEWS else None
        menu_stats[slug] = len(menu_unique[slug]) if slug in CATEGORY_VIEWS else len(names)

    for position, (slug, xml_name, en_title, fr_title, en_intro, fr_intro) in enumerate(MENU_PAGES, start=2):
        unique = menu_unique[slug]
        view, layout = xml_name[:-4].split('-', 1)
        source_path = f'site/views/{view}/tmpl/{layout}.xml'
        for lang in ('en', 'fr'):
            intro = en_intro if lang == 'en' else fr_intro
            if slug in CATEGORY_VIEWS:
                note = ('Only the options specific to this view are listed below. All other options are described in '
                        '[Category views — common options](./category-common.md).' if lang == 'en' else
                        'Seules les options propres à cette vue sont listées ci-dessous. Toutes les autres options sont '
                        'décrites dans [Vues catégorie — options communes](./category-common.md).')
                intro = (intro + ' ' if intro else '') + note
            blocks = [render_xml(SOURCES / 'menu' / xml_name, lang, only=unique)]
            content = make_page(
                lang, position, fr_title if lang == 'fr' else en_title, intro, blocks,
                src_line(lang, [source_path]),
            )
            write('menu-links', slug, lang, content)
        total += menu_stats[slug]
        print(f'menu/{slug:20s} {menu_stats[slug]:4d} options')

    # ---- Templates
    template_stats = {}
    for slug, xml_name, _, _, _, _ in TEMPLATE_PAGES:
        template_stats[slug] = option_rows(SOURCES / 'templatesforms' / xml_name)

    for position, (slug, xml_name, en_title, fr_title, en_intro, fr_intro) in enumerate(TEMPLATE_PAGES, start=2):
        for lang in ('en', 'fr'):
            content = make_page(
                lang, position, fr_title if lang == 'fr' else en_title,
                en_intro if lang == 'en' else fr_intro,
                [render_xml(SOURCES / 'templatesforms' / xml_name, lang)],
                src_line(lang, ['site/templates/' + xml_name.replace('-', '/', 1)]),
            )
            write('templates', slug, lang, content)
        total += template_stats[slug]
        print(f'templates/{slug:18s} {template_stats[slug]:4d} options')

    # ---- Overview pages
    for lang in ('en', 'fr'):
        fr = lang == 'fr'

        # Content types overview
        s = ET.parse(SOURCES / 'forms' / 'type.xml').getroot()
        rows = [(title_for(fs, lang), len(fs.findall('field'))) for fs in s.findall('.//fieldset')]
        lines = ['---', 'sidebar_position: 1', '---', '', '# Types de contenu' if fr else '# Content types', '',
                 CONTENT_TYPES_INTRO[lang], '',
                 'Toutes les options sont détaillées sur la page [Options](./options.md).' if fr else
                 'All options are detailed on the [Options](./options.md) page.', '',
                 '| Section | Options |', '| --- | --- |']
        lines += [f'| {t} | {n} |' for t, n in rows]
        write('content-types', 'index', lang, '\n'.join(lines) + '\n')

        # Categories overview
        s = ET.parse(SOURCES / 'forms' / 'category.xml').getroot()
        rows = [(title_for(fs, lang), len(fs.findall('field'))) for fs in s.findall('.//fieldset')]
        lines = ['---', 'sidebar_position: 1', '---', '', '# Catégories' if fr else '# Categories', '',
                 CATEGORIES_INTRO[lang], '',
                 'Toutes les options sont détaillées sur la page [Options](./options.md).' if fr else
                 'All options are detailed on the [Options](./options.md) page.', '',
                 '| Section | Options |', '| --- | --- |']
        lines += [f'| {t} | {n} |' for t, n in rows]
        write('categories', 'index', lang, '\n'.join(lines) + '\n')

        # Menu links overview
        lines = ['---', 'sidebar_position: 1', '---', '', '# Liens de menu' if fr else '# Menu links', '',
                 MENU_INTRO[lang], '',
                 '| Type | Options | Détails |' if fr else '| Type | Options | Details |',
                 '| --- | --- | --- |']
        for slug, xml_name, en_title, fr_title, _, _ in MENU_PAGES:
            title = fr_title if fr else en_title
            lines.append(f'| [{title}](./{slug}.md) | {menu_stats[slug]} | [→](./{slug}.md) |')
        write('menu-links', 'index', lang, '\n'.join(lines) + '\n')

        # Templates overview
        lines = ['---', 'sidebar_position: 1', '---', '', '# Modèles' if fr else '# Templates', '',
                 TEMPLATES_INTRO[lang], '',
                 '| ' + ('Modèle | Description | Options contenu | Options catégorie |' if fr else
                         'Template | Description | Item options | Category options |'),
                 '| --- | --- | --- | --- |']
        for tname, tname_fr, fr_desc, en_desc in TEMPLATES:
            key = f'category-{tname}'
            display = tname_fr if fr else tname
            lines.append(f'| **{display}** | {fr_desc if fr else en_desc} | [{template_stats["item"]}](./item.md) | [{template_stats.get(key, 0)}](./{key}.md) |')
        write('templates', 'index', lang, '\n'.join(lines) + '\n')

    print(f'\nTotal documented options: {total}')


if __name__ == '__main__':
    main()
