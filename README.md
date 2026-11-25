# Documentation FLEXIcontent

Site de documentation bilingue (**anglais** puis **français**) pour [FLEXIcontent](https://www.flexicontent.org/), construit avec [Docusaurus](https://docusaurus.io/).

## Langues

- **Anglais** (`en`) : langue par défaut, contenus dans `docs/`.
- **Français** (`fr`) : contenus traduits dans `i18n/fr/docusaurus-plugin-content-docs/current/` et traductions de l'interface dans `i18n/fr/*.json`.

Le sélecteur de langue est disponible dans la barre de navigation.

## Aperçu local

Le service DDEV (`http://flexi-documentation.ddev.site:2999`, ou HTTPS sur le port `3001`) lance `docusaurus serve` : il sert le build terminé, avec `/docs/...` et `/fr/docs/...`, ce qui permet au sélecteur de langue de fonctionner. `docusaurus start` ne sert que la locale anglaise ; si vous l'utilisez, les URL `/fr/...` afficheront « Page not found ». Après une modification des contenus, relancez :

```bash
ddev exec --dir /var/www/html/website npm run build
```

## Traduction française de repli

Les pages FR sont générées depuis les manifestes XML et les fichiers de langue officiels. Lorsque ceux-ci ne contiennent pas de traduction, un mécanisme de repli traduit les titres, libellés, valeurs d'options, descriptions et noms de langues restés en anglais, sans modifier les identifiants techniques, les clés de langue ni le code. Les destinations des liens Markdown sont également protégées : traduire « Categories » en « Catégories » ne réécrit pas `../concepts/categories.md`.

Les correspondances sont réparties dans `tools/fr_translations.py`, `tools/fr_exact_extra.py` et `tools/fr_more.py`. Les générateurs les appellent automatiquement ; pour retraduire uniquement les pages FR déjà présentes, exécuter :

```bash
python3 website/tools/translate_fr_docs.py
```

## Structure

```text
docs/                                      # contenus anglais (source)
├── index.md                               # accueil /docs/ (slug: /)
├── intro.mdx
├── demarrage/                             # installation et premiers pas
├── concepts/                              # types, champs, catégories, modèles
├── configuration/                         # 15 pages : Options + 14 onglets
├── fields/                                # 36 pages : vue d'ensemble + 35 types de champs
├── content-types/                         # options des types de contenu
├── categories/                            # options des catégories
├── menu-links/                            # 14 pages : options des liens de menu
├── templates/                             # 6 pages : options des modèles
├── modules/                               # 7 pages : modules frontend
├── plugins/                               # 14 pages : plugins hors champs
└── ressources.md
i18n/fr/                                   # traductions françaises
├── code.json                              # interface et page d'accueil
├── docusaurus-theme-classic/              # navbar et footer
├── docusaurus-plugin-content-docs/
│   ├── current.json                       # libellés du menu latéral
│   └── current/                           # pages traduites
sidebars.js                                # organisation du menu latéral
docusaurus.config.js                       # configuration du site
tools/
├── sources/                               # sources officielles FLEXIcontent 5.x
│   ├── config.xml                         # admin/config.xml
│   ├── en-GB.com_flexicontent.ini         # langue anglaise
│   ├── fr-FR.com_flexicontent.ini         # package de traduction française
│   ├── fields/                            # manifests XML + langues des 35 plugins de champs
│   ├── extra-lang/                        # langues complémentaires (composant, site, modèles)
│   ├── forms/                             # formulaires type.xml et category.xml
│   ├── menu/                              # manifests des liens de menu
│   ├── templatesforms/                    # manifests des modèles
│   ├── modules/                           # manifests et langues des modules
│   └── plugins/                           # manifests et langues des plugins
├── generate_config_docs.py                # générateur des pages de configuration
├── generate_field_docs.py                 # générateur des pages de champs
├── generate_forms_docs.py                 # types, catégories, liens de menu, modèles
├── generate_extensions_docs.py            # modules et plugins
├── fr_translations.py                     # traductions FR de repli + API de traduction
├── fr_exact_extra.py                      # traductions exactes complémentaires
├── fr_more.py                             # titres, libellés, valeurs et noms de langues
└── translate_fr_docs.py                   # applique les traductions aux pages FR existantes
```

Le blog est désactivé (`blog: false`).

## Documentation de configuration

Les 15 pages de la section **Configuration** sont générées à partir des sources officielles de FLEXIcontent 5.x : `admin/config.xml` et les fichiers de langue `en-GB` / `fr-FR`. La page `options.md` (onglet Options) est maintenue manuellement ; les 13 autres onglets sont générés automatiquement.

Pour régénérer les pages après mise à jour des fichiers dans `tools/sources/` :

```bash
python3 website/tools/generate_config_docs.py
```

Les fichiers de langue proviennent du dépôt [FLEXIcontent/flexicontent-translations](https://github.com/FLEXIcontent/flexicontent-translations) (package `fr-FR`, projet Crowdin).

## Documentation des champs

Les 35 types de champs FLEXIcontent sont documentés dans `docs/fields/` (une page par type, plus une vue d'ensemble). Chaque page liste les options d'édition, d'affichage, de SEO et de filtrage définies dans le manifest XML du plugin, avec les libellés et descriptions traduits.

Pour régénérer les pages après mise à jour des manifests ou des fichiers de langue dans `tools/sources/fields/` :

```bash
python3 website/tools/generate_field_docs.py
```

## Types, catégories, menus et modèles

Les options des types de contenu, des catégories, des liens de menu et des modèles sont générées depuis les formulaires et manifests officiels (`admin/models/forms/`, `site/views/*/tmpl/`, `site/templates/`). Les six vues basées sur les catégories partagent une page d'options commune ; chaque vue ne documente que ses options spécifiques. Il en va de même pour les options de modèle communes aux quatre templates.

```bash
python3 website/tools/generate_forms_docs.py
```

## Modules et plugins

Les six modules frontend et les plugins hors champs sont documentés depuis leurs manifests XML et leurs fichiers de langue officiels. Les plugins de types de champs restent documentés dans `docs/fields/`.

```bash
python3 website/tools/generate_extensions_docs.py
```

## Fonctionnalités activées

- **Recherche locale** via `@cmfcmf/docusaurus-search-local` (index générés pour `en` et `fr`, sans service externe).
- **Images optimisées** via `@docusaurus/plugin-ideal-image` (composant `IdealImage`).
- **Diagrammes Mermaid** via `@docusaurus/theme-mermaid` (blocs ```mermaid).

## Développement avec DDEV

Le projet tourne dans le conteneur web DDEV. Node.js n'est pas nécessaire sur la machine hôte.

Le serveur de développement démarre automatiquement avec `ddev restart` et est disponible sur :

- https://flexi-documentation.ddev.site:3001
- http://flexi-documentation.ddev.site:2999

Commandes utiles :

```bash
ddev restart
ddev exec --dir /var/www/html/website npm run build
ddev exec --dir /var/www/html/website npm run clear
```

Après modification des traductions de l'interface, régénérer les fichiers `i18n/fr/*.json` :

```bash
ddev exec --dir /var/www/html/website npm run write-translations -- --locale fr
```

Pour travailler directement dans le conteneur :

```bash
ddev ssh
cd /var/www/html/website
npm start
```

## Build

```bash
ddev exec --dir /var/www/html/website npm run build
```

Les fichiers statiques sont générés dans `website/build/` et `website/build/fr/`.

## Déploiement

Le site est configuré pour l'URL publique définitive :

```text
https://flexicontent.org/_documentation_notes/
```

Après un build, copiez **le contenu** de `website/build/` dans le dossier `_documentation_notes/` de l'espace web, pas à la racine du domaine. Les fichiers doivent donner :

```text
_documentation_notes/index.html
_documentation_notes/docs/...
_documentation_notes/fr/docs/...
_documentation_notes/assets/...
_documentation_notes/sitemap.xml
```

Si l'URL publique change, mettez à jour `url` et `baseUrl` dans `website/docusaurus.config.js`, puis relancez le build.
