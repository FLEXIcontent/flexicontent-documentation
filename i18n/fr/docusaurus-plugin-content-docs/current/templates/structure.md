---
title: Référence de la structure des fichiers de modèle
sidebar_position: 2
---

# Référence de la structure des fichiers de modèle

Un modèle FLEXIcontent est un dossier de fichiers PHP, XML, CSS et LESS. Cette page décrit la structure 5.x utilisée par les modèles fournis `faq`, `grid`, `items-tabbed` et `table`.

:::info Source
Les chemins, les rôles des fichiers et les exemples XML proviennent de FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`). Les descriptions de l’éditeur de modèle sont extraites de `admin/views/template/tmpl/default.php`.
:::

## Où se trouvent les modèles

| Contexte | Chemin |
| --- | --- |
| Site installé | `components/com_flexicontent/templates/<template_folder>/` |
| Dépôt | `site/templates/<template_folder>/` |
| Surcharge Joomla | `templates/<joomla_template>/html/com_flexicontent/templates/<template_folder>/` |

Le nom du dossier de modèle est la clé de mise en page utilisée par les paramètres `ilayout` et `clayout`. Par exemple, `?ilayout=grid` sélectionne `components/com_flexicontent/templates/grid/`.

:::caution
Ne modifiez jamais directement un modèle fourni. Copiez d’abord le dossier sous un autre nom, puis modifiez la copie. Une mise à jour de FLEXIcontent peut écraser les fichiers d’origine.
:::

## Arborescence canonique

Le modèle `grid` est la référence la plus complète :

```text
site/templates/grid/
├── category.php
├── category_alpha.php
├── category_category.php
├── category_items.php
├── category_peercategories.php
├── category_subcategories.php
├── category.xml
├── category.png
├── clayout.png
├── item.php
├── item.xml
├── item.png
├── index.html
├── css/
│   ├── category.css
│   ├── item.css
│   └── index.html
├── language/
│   ├── en-GB/en-GB.ini
│   └── fr-FR/fr-FR.ini
├── less/
│   ├── category.less
│   ├── item.less
│   └── include/
│       ├── config.less
│       ├── config_auto_category.less
│       ├── config_auto_item.less
│       └── _config_fc_ts
└── seo/
    ├── category/layouts/meta.php
    ├── category/layouts/title.php
    ├── item/layouts/meta.php
    └── item/layouts/title.php
```

Les autres modèles fournis suivent la même structure ; certains ne contiennent pas de fichier de langue `fr-FR`.

## Rôle des fichiers

L’éditeur de modèle documente lui-même les fichiers modifiables (`admin/views/template/tmpl/default.php`, `$file_tip`) :

| Fichier | Rôle |
| --- | --- |
| `item.xml` | Structure de la mise en page contenu : paramètres d’affichage, positions de champs, liste de fichiers. |
| `category.xml` | Structure de la mise en page catégorie : paramètres d’affichage, positions de champs, liste de fichiers. |
| `item.php` | Code PHP/HTML qui affiche les champs du contenu. |
| `category.php` | Conteneur de premier niveau de la mise en page catégorie. |
| `category_items.php` | Formulaire de filtrage et boucle des contenus. |
| `category_category.php` | Informations sur la catégorie : titre, description, image, etc. |
| `category_alpha.php` | Index alphanumérique de la liste de contenus. |
| `category_peercategories.php` | Liste des catégories sœurs. |
| `category_subcategories.php` | Liste des sous-catégories. |
| `item.css`, `category.css` | CSS propre à cette mise en page. |
| `item.less`, `category.less` | Directives LESS compilées en CSS. |
| `config.less` | Imports, variables et mixins. |
| `config_auto_item.less`, `config_auto_category.less` | Variables LESS générées automatiquement à chaque enregistrement du modèle. |
| `title.php` | Crée la balise `<title>` du document et le titre de la page. |
| `meta.php` | Définit les balises META du document. |

L’éditeur prend également en charge les variantes `_html5.php` : `item_html5.php`, `category_html5.php` et `category_items_html5.php`. Il liste les fichiers modifiables avec ce motif :

```php
new RegexIterator(
    new RecursiveIteratorIterator(new RecursiveDirectoryIterator($tmpldir)),
    '#('.$this->layout->view.'(_.*\.|\.)(php|xml|less|css|js)|include.*less|seo.{1}'.$this->layout->view.'.*php)#i'
);
```

## Manifeste XML en 5.x

Les manifestes actuels utilisent une racine de formulaire Joomla, et non l’ancienne racine `<metadata>` / `<params>`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<form>
    <author>Emmanuel Danan, George Papadakis</author>
    <website>www.flexicontent.org</website>
    <license>GPLv3</license>
    <version>2</version>
    <release>08 08 2024</release>
    <microdata_support>1</microdata_support>
    <defaulttitle>FLEXI_TMPL_ITEMSTABBED_ITEM_DEFAULT_TITLE</defaulttitle>
    <description>FLEXI_TMPL_ITEMSTABBED_ITEM_SHORT_DESC</description>

    <fields name="attribs">
        <fieldset name="attribs" addfieldpath="/administrator/components/com_flexicontent/elements">
            <!-- paramètres de la mise en page -->
        </fieldset>
    </fields>
</form>
```

Lors de la migration d’un modèle Joomla 1.5 :

| Ancienne syntaxe | Syntaxe 5.x |
| --- | --- |
| `<metadata>...</metadata>` | `<form>...</form>` |
| `<params addpath="...">...</params>` | `<fields name="attribs"><fieldset name="attribs" addfieldpath="...">...</fieldset></fields>` |
| `<param ... />` | `<field ... />` |

### Déclaration des fichiers CSS et JS

Déclarez les ressources dans le manifeste ; `site/classes/helpers/tmpl.php` les résout par rapport au dossier du modèle :

```xml
<cssitem>
    <file>css/item.css</file>
</cssitem>
<jsitem>
</jsitem>
```

```xml
<csscategory>
    <file>css/category.css</file>
</csscategory>
<jscategory>
</jscategory>
```

L’analyseur cherche aussi un fichier LESS correspondant en remplaçant `css` par `less` dans le chemin. La vue catégorie ajoute les fichiers déclarés avec `addStyleSheet()` et `addScript()` (`site/views/category/view.html.php`).

### Variables LESS issues des paramètres

Un paramètre portant `cssprep="less"` est exporté vers `less/include/config_auto_item.less` ou `config_auto_category.less` à chaque enregistrement du modèle. Un paramètre nommé `content_width_fit_feat` produit une variable telle que :

```less
@FCC_content_width_fit_feat: auto-fill;
```

Le préfixe est `@FCI_` pour les mises en page contenu et `@FCC_` pour les mises en page catégorie. Ne modifiez pas ces fichiers générés à la main : ils sont régénérés à chaque enregistrement.

## Les modèles fournis sont des conteneurs

Les fichiers `item.php` fournis incluent une mise en page partagée :

```php
<?php
    // Modular item layout
    // If customizing via CSS rules or JS scripts is not enough, then please copy the following file here to customize the HTML too
    include(JPATH_SITE.DS.'components'.DS.'com_flexicontent'.DS.'tmpl_common'.DS.'item_layouts'.DS.'modular.php');
?>
```

Les fichiers `category.php` fournis incluent de la même façon `tmpl_common/category.php`. Ce fichier partagé charge :

```php
echo $this->loadTemplate('category');
echo $this->loadTemplate('subcategories');
echo $this->loadTemplate('peercategories');
echo $this->loadTemplate('items');
```

Pour personnaliser le HTML, copiez le fichier partagé concerné dans votre dossier de modèle :

```text
site/tmpl_common/item_layouts/modular.php  →  <votre_modele>/item.php
site/tmpl_common/category_items.php        →  <votre_modele>/category_items.php
```

Voir [Boucles de contenus et rendu des champs](./loops-fields.md) et [Positions de champs et glisser-déposer](./positions.md).

## Résolution des modèles et surcharges

Le composant ajoute les chemins de modèles dans cet ordre (`site/views/category/view.html.php` et `admin/views/item/view.html.php`) :

1. Modèle de repli (`grid` par défaut) dans le composant.
2. Modèle de repli dans le dossier de surcharge du modèle Joomla actif.
3. Modèle sélectionné dans le composant.
4. Modèle sélectionné dans le dossier de surcharge du modèle Joomla actif.

Une surcharge Joomla pour un modèle personnalisé nommé `mytmpl` se place donc dans :

```text
templates/<joomla_template>/html/com_flexicontent/templates/mytmpl/
```

Une mise en page peut aussi être changée par URL :

```text
&clayout=othertmpl   // vue catégorie
&ilayout=othertmpl   // vue contenu
```

`clayout` et `ilayout` résolvent respectivement vers `category.xml` et `item.xml`. En interne, l’analyseur utilise le type de mise en page `items` pour la vue contenu et le nom de vue `item` ; `FLEXI_ITEMVIEW` vaut `item` sur Joomla 4+.

## Checklist de création

1. Dupliquez un modèle fourni ; ne modifiez pas les modèles d’origine.
2. Conservez `item.xml`, `category.xml`, `item.php`, `category.php` et `category_items.php`.
3. Ajoutez les paramètres sous `<fields name="attribs"><fieldset name="attribs" ...>`.
4. Déclarez les positions de champs dans `<fieldgroups>` (voir [positions](./positions.md)).
5. Ajoutez les boucles PHP qui affichent ces positions.
6. Déclarez le CSS/JS avec `cssitem`, `jsitem`, `csscategory` et `jscategory`.
7. Copiez les fichiers partagés de `tmpl_common` dans votre modèle si vous devez modifier le HTML.
8. Enregistrez le modèle dans l’administration pour stocker les positions et le LESS généré.
9. Videz le cache Joomla si vous avez modifié le XML ou le PHP hors de l’éditeur de modèle.

## Références officielles

- [Page des fonctionnalités Templates](https://www.flexicontent.org/features/templates.html)
- [Template FLEXIcontent — partie 1 : la structure](https://www.flexicontent.org/documentation/tutorials-english/84-advanced-tutorials/335-template-flexicontent-part-1-the-structure.html)
- [Template FLEXIcontent — partie 4 : le modèle de contenu](https://www.flexicontent.org/documentation/tutorials-english/84-advanced-tutorials/338-template-flexicontent-part-4-the-contents-template.html)
- [Mise à jour des modèles Joomla 1.5 vers le format XML de formulaire 2.x+](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/300-updating-your-flexicontent-j15-templates-to-work-with-fc-v2x-for-j25-j3x.html)
- [Surcharge d’une mise en page avec `clayout` / `ilayout`](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/290-overriding-default-itemcategory-template-layout-in-itemcategory-view.html)
- [Surcharge de vue Joomla](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/198-how-to-override-view.html)
- [Dépôt source FLEXIcontent](https://github.com/FLEXIcontent/flexicontent-cck)
