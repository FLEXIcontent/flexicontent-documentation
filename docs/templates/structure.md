---
title: Template file structure reference
sidebar_position: 2
---

# Template file structure reference

A FLEXIcontent template is a folder of PHP, XML, CSS and LESS files. This page describes the 5.x structure used by the bundled templates `faq`, `grid`, `items-tabbed` and `table`.

:::info Source
The paths, file roles and XML examples come from FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`). The template editor descriptions are taken from `admin/views/template/tmpl/default.php`.
:::

## Where templates live

| Context | Path |
| --- | --- |
| Installed site | `components/com_flexicontent/templates/<template_folder>/` |
| Repository | `site/templates/<template_folder>/` |
| Joomla override | `templates/<joomla_template>/html/com_flexicontent/templates/<template_folder>/` |

The template folder name is the layout key used by the `ilayout` and `clayout` parameters. For example, `?ilayout=grid` selects `components/com_flexicontent/templates/grid/`.

:::caution
Never edit a bundled template directly. Copy the folder to a new name first, then edit the copy. An update of FLEXIcontent can overwrite the built-in files.
:::

## Canonical folder tree

The `grid` template is the most complete reference:

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

Other bundled templates follow the same structure; some do not ship a `fr-FR` language file.

## File roles

The template editor itself documents the editable files (`admin/views/template/tmpl/default.php`, `$file_tip`):

| File | Role |
| --- | --- |
| `item.xml` | Item layout structure: display parameters, field positions, file list. |
| `category.xml` | Category layout structure: display parameters, field positions, file list. |
| `item.php` | PHP/HTML that displays item fields. |
| `category.php` | Top-level container of the category layout. |
| `category_items.php` | Item filtering form and item loop. |
| `category_category.php` | Category information: title, description, image, etc. |
| `category_alpha.php` | Alphanumerical index of the item list. |
| `category_peercategories.php` | Peer categories list. |
| `category_subcategories.php` | Subcategories list. |
| `item.css`, `category.css` | CSS specific to this layout. |
| `item.less`, `category.less` | LESS directives compiled into the CSS. |
| `config.less` | Imports, variables and mixins. |
| `config_auto_item.less`, `config_auto_category.less` | Automatically generated LESS variables written on every template save. |
| `title.php` | Creates the document `<title>` and page heading. |
| `meta.php` | Sets the document META tags. |

The editor also supports `_html5.php` variants: `item_html5.php`, `category_html5.php` and `category_items_html5.php`. It lists editable files with this pattern:

```php
new RegexIterator(
    new RecursiveIteratorIterator(new RecursiveDirectoryIterator($tmpldir)),
    '#('.$this->layout->view.'(_.*\.|\.)(php|xml|less|css|js)|include.*less|seo.{1}'.$this->layout->view.'.*php)#i'
);
```

## XML manifest in 5.x

Current manifests use a Joomla form root, not the old `<metadata>` / `<params>` root.

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
            <!-- layout parameters -->
        </fieldset>
    </fields>
</form>
```

When migrating a Joomla 1.5 template:

| Old syntax | 5.x syntax |
| --- | --- |
| `<metadata>...</metadata>` | `<form>...</form>` |
| `<params addpath="...">...</params>` | `<fields name="attribs"><fieldset name="attribs" addfieldpath="...">...</fieldset></fields>` |
| `<param ... />` | `<field ... />` |

### CSS and JS declarations

Declare assets in the manifest; `site/classes/helpers/tmpl.php` resolves them relative to the template folder:

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

The parser also looks for a matching LESS file by replacing `css` with `less` in the path. The category view adds the declared files with `addStyleSheet()` and `addScript()` (`site/views/category/view.html.php`).

### LESS variables from parameters

A parameter with `cssprep="less"` is exported to `less/include/config_auto_item.less` or `config_auto_category.less` every time the template is saved. A parameter named `content_width_fit_feat` produces a variable such as:

```less
@FCC_content_width_fit_feat: auto-fill;
```

The prefix is `@FCI_` for item layouts and `@FCC_` for category layouts. Do not edit the generated files by hand: they are regenerated on save.

## Built-in templates are wrappers

The bundled `item.php` files include a shared layout:

```php
<?php
    // Modular item layout
    // If customizing via CSS rules or JS scripts is not enough, then please copy the following file here to customize the HTML too
    include(JPATH_SITE.DS.'components'.DS.'com_flexicontent'.DS.'tmpl_common'.DS.'item_layouts'.DS.'modular.php');
?>
```

Bundled `category.php` files similarly include `tmpl_common/category.php`. That shared file loads:

```php
echo $this->loadTemplate('category');
echo $this->loadTemplate('subcategories');
echo $this->loadTemplate('peercategories');
echo $this->loadTemplate('items');
```

To customize the HTML, copy the relevant shared file into your template folder:

```text
site/tmpl_common/item_layouts/modular.php  →  <your_template>/item.php
site/tmpl_common/category_items.php        →  <your_template>/category_items.php
```

See [Item loop and field rendering](./loops-fields.md) and [Field positions and drag and drop](./positions.md).

## Template resolution and overrides

The component adds template paths in this order (`site/views/category/view.html.php` and `admin/views/item/view.html.php`):

1. Fallback layout (`grid` by default) in the component.
2. Fallback layout in the active Joomla template override directory.
3. Selected layout in the component.
4. Selected layout in the active Joomla template override directory.

So a Joomla override for a custom layout named `mytmpl` goes in:

```text
templates/<joomla_template>/html/com_flexicontent/templates/mytmpl/
```

A layout can also be switched per URL:

```text
&clayout=othertmpl   // category view
&ilayout=othertmpl   // item view
```

`clayout` and `ilayout` resolve to `category.xml` and `item.xml` respectively. Internally, the parser uses the layout type `items` for the item view and view name `item`; `FLEXI_ITEMVIEW` resolves to `item` on Joomla 4+.

## Authoring checklist

1. Duplicate a bundled template; do not edit built-ins.
2. Keep `item.xml`, `category.xml`, `item.php`, `category.php` and `category_items.php`.
3. Add parameters under `<fields name="attribs"><fieldset name="attribs" ...>`.
4. Declare field positions inside `<fieldgroups>` (see [positions](./positions.md)).
5. Add the PHP loops that render those positions.
6. Declare CSS/JS with `cssitem`, `jsitem`, `csscategory` and `jscategory`.
7. Copy shared `tmpl_common` files into your template if you need to change HTML.
8. Save the template in the administrator so positions and generated LESS are stored.
9. Clear the Joomla cache if you edited XML or PHP outside the template editor.

## Official references

- [Templates feature page](https://www.flexicontent.org/features/templates.html)
- [Template FLEXIcontent — part 1: the structure](https://www.flexicontent.org/documentation/tutorials-english/84-advanced-tutorials/335-template-flexicontent-part-1-the-structure.html)
- [Template FLEXIcontent — part 4: the contents template](https://www.flexicontent.org/documentation/tutorials-english/84-advanced-tutorials/338-template-flexicontent-part-4-the-contents-template.html)
- [Updating Joomla 1.5 templates to the 2.x+ form XML format](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/300-updating-your-flexicontent-j15-templates-to-work-with-fc-v2x-for-j25-j3x.html)
- [Overriding a layout with `clayout` / `ilayout`](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/290-overriding-default-itemcategory-template-layout-in-itemcategory-view.html)
- [Joomla view override](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/198-how-to-override-view.html)
- [FLEXIcontent source repository](https://github.com/FLEXIcontent/flexicontent-cck)
