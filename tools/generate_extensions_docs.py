#!/usr/bin/env python3
"""Generate documentation for FLEXIcontent modules and plugins.

Sources (official FLEXIcontent 5.x), copied into tools/sources/:
  modules/*.xml, modules/lang/{en-GB,fr-FR}/*.ini
  plugins/*.xml, plugins/lang/{en-GB,fr-FR}/*.ini

The 35 field-type plugins are documented separately in docs/fields/ and are only
listed in the plugins overview. Reuses the helpers of generate_forms_docs.py.
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import generate_forms_docs as f  # noqa: E402
import fr_translations  # noqa: E402

ROOT = HERE.parent
SOURCES = HERE / 'sources'

for lang, prefix in (('en', 'en-GB'), ('fr', 'fr-FR')):
    for folder in ('modules', 'plugins'):
        for path in sorted((SOURCES / folder / 'lang' / prefix).glob('*.ini')):
            f.g.LANG[lang].update(f.g.load_ini(path))

MODULES = [
    ('mod_flexicontent', 'FLEXIcontent items', 'Contenus FLEXIcontent'),
    ('mod_flexiadvsearch', 'Advanced search', 'Recherche avancée'),
    ('mod_flexicategories', 'Categories', 'Catégories'),
    ('mod_flexifilter', 'Item filters', 'Filtres de contenus'),
    ('mod_flexigooglemap', 'Google map', 'Carte Google'),
    ('mod_flexitagcloud', 'Tag cloud', 'Nuage d’étiquettes'),
]

PLUGINS = [
    ('content-flexibreak', 'Content — Flexibreak', 'Contenu — Flexibreak', 'Content'),
    ('editors-xtd-fccat', 'Editor button — Category', 'Bouton éditeur — Catégorie', 'Editor buttons'),
    ('editors-xtd-fcfile', 'Editor button — File', 'Bouton éditeur — Fichier', 'Editor buttons'),
    ('editors-xtd-fcitem', 'Editor button — Item', 'Bouton éditeur — Contenu', 'Editor buttons'),
    ('finder-flexicontent', 'Smart Search', 'Recherche intelligente', 'Search'),
    ('flexicontent-flexinotify', 'Favourites notifications', 'Notifications des favoris', 'FLEXIcontent'),
    ('jsitemap-flexicontent', 'JSitemap integration', 'Intégration JSitemap', 'Third-party'),
    ('osmap-com_flexicontent', 'OSMap integration', 'Intégration OSMap', 'Third-party'),
    ('search-flexiadvsearch', 'Search — Advanced', 'Recherche — Avancée', 'Search'),
    ('search-flexisearch', 'Search — Standard', 'Recherche — Standard', 'Search'),
    ('system-flexiadvroute', 'System — Advanced routing', 'Système — Routage avancé', 'System'),
    ('system-flexifieldsearch', 'System — Field search', 'Système — Recherche par champs', 'System'),
    ('system-flexisystem', 'System — Core tasks', 'Système — Tâches cœur', 'System'),
]

GROUP_FR = {
    'Content': 'Contenu', 'Editor buttons': 'Boutons de l’éditeur', 'Search': 'Recherche',
    'FLEXIcontent': 'FLEXIcontent', 'Third-party': 'Extensions tierces', 'System': 'Système',
}

MODULES_INTRO = {
    'en': 'FLEXIcontent provides six frontend modules for displaying items, categories, search forms, filters, maps and tag clouds. Configure a module from **Extensions → Modules**.',
    'fr': 'FLEXIcontent fournit six modules frontend pour afficher des contenus, des catégories, des formulaires de recherche, des filtres, des cartes et des nuages d’étiquettes. Configurez un module depuis **Extensions → Modules**.',
}
PLUGINS_INTRO = {
    'en': 'FLEXIcontent provides plugins for search, routing, notifications, editor buttons and sitemap integrations. Enable and configure them from **Extensions → Plugins**. The 35 field-type plugins are documented in the [Fields](../fields/index.md) section.',
    'fr': 'FLEXIcontent fournit des plugins pour la recherche, le routage, les notifications, les boutons de l’éditeur et les sitemaps. Activez-les et configurez-les depuis **Extensions → Plugins**. Les 35 plugins de types de champs sont documentés dans la section [Champs](../fields/index.md).',
}


def xml_path(folder, slug):
    return SOURCES / folder / f'{slug}.xml'


def render_page(folder, slug, lang, position, title, intro, source_path):
    root = ET.parse(xml_path(folder, slug)).getroot()
    description = f.g.clean(f.tr(root.findtext('description', ''), lang)).strip()
    if len(description) > 400:
        description = description[:397].rstrip() + '…'
    lines = [
        '---',
        f'sidebar_position: {position}',
        '---',
        '',
        f'# {title}',
        '',
        intro,
        '',
    ]
    if description:
        lines += ['> ' + description, '']
    lines += [
        ':::info Source',
        f.src_line(lang, [source_path]),
        ':::',
        '',
    ]
    block = f.render_xml(xml_path(folder, slug), lang)
    if block:
        lines += [block, '']
    return '\n'.join(lines).rstrip() + '\n'


def write(section, slug, lang, content):
    base = ROOT / 'docs' if lang == 'en' else ROOT / 'i18n' / 'fr' / 'docusaurus-plugin-content-docs' / 'current'
    path = base / section / f'{slug}.md'
    path.parent.mkdir(parents=True, exist_ok=True)
    if lang == 'fr':
        content = fr_translations.translate_content(content)
    path.write_text(content, encoding='utf-8')


def stats(folder, slug):
    root = ET.parse(xml_path(folder, slug)).getroot()
    return len([x for x in root.findall('.//field') if x.get('name') and x.get('type') != 'separator'])


def main():
    module_stats = {s: stats('modules', s) for s, _, _ in MODULES}
    plugin_stats = {s: stats('plugins', s) for s, _, _, _ in PLUGINS}

    for position, (slug, en_title, fr_title) in enumerate(MODULES, start=2):
        for lang in ('en', 'fr'):
            intro = MODULES_INTRO[lang]
            content = render_page(
                'modules', slug, lang, position,
                fr_title if lang == 'fr' else en_title, intro,
                f'modules/{slug}/{slug}.xml',
            )
            write('modules', slug, lang, content)
        print(f'modules/{slug:22s} {module_stats[slug]:4d} options')

    for position, (slug, en_title, fr_title, _) in enumerate(PLUGINS, start=2):
        group = next(g for g in ('editors-xtd', 'flexicontent', 'content', 'finder', 'jsitemap', 'osmap', 'search', 'system') if slug.startswith(g + '-'))
        name = slug[len(group) + 1:]
        source_path = f'plugins/{group}/{name}/{name}.xml'
        for lang in ('en', 'fr'):
            content = render_page(
                'plugins', slug, lang, position,
                fr_title if lang == 'fr' else en_title, PLUGINS_INTRO[lang], source_path,
            )
            write('plugins', slug, lang, content)
        print(f'plugins/{slug:30s} {plugin_stats[slug]:4d} options')

    for lang in ('en', 'fr'):
        fr = lang == 'fr'

        lines = ['---', 'sidebar_position: 1', '---', '', '# Modules' if fr else '# Modules', '',
                 MODULES_INTRO[lang], '', '| ' + ('Module | Options | Détails |' if fr else 'Module | Options | Details |'),
                 '| --- | --- | --- |']
        for slug, en_title, fr_title in MODULES:
            title = fr_title if fr else en_title
            lines.append(f'| [{title}](./{slug}.md) | {module_stats[slug]} | [→](./{slug}.md) |')
        write('modules', 'index', lang, '\n'.join(lines) + '\n')

        lines = ['---', 'sidebar_position: 1', '---', '', '# Plugins' if fr else '# Plugins', '',
                 PLUGINS_INTRO[lang], '']
        for group in ['Content', 'Editor buttons', 'Search', 'FLEXIcontent', 'Third-party', 'System']:
            lines += [f'## {GROUP_FR[group] if fr else group}', '', '| Plugin | Options | Détails |' if fr else '| Plugin | Options | Details |', '| --- | --- | --- |']
            for slug, en_title, fr_title, plugin_group in PLUGINS:
                if plugin_group != group:
                    continue
                title = fr_title if fr else en_title
                lines.append(f'| [{title}](./{slug}.md) | {plugin_stats[slug]} | [→](./{slug}.md) |')
            lines.append('')
        write('plugins', 'index', lang, '\n'.join(lines).rstrip() + '\n')

    print(f'\nTotal documented options: {sum(module_stats.values()) + sum(plugin_stats.values())}')


if __name__ == '__main__':
    main()
