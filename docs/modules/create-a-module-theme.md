---
title: Create a module theme
sidebar_position: 2
---

# Create a module theme

In FLEXIcontent, a module **theme** is called a **layout**. It is a PHP file, optionally accompanied by an XML parameter file, CSS and header/footer fragments. The module parameter `layout` selects which one is used.

This guide shows the upgrade-safe method: put the custom layout in the active Joomla template. It applies to all FLEXIcontent modules; the examples use `mod_flexicontent`.

:::info Source
Based on FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), especially `modules/mod_flexicontent/mod_flexicontent.xml`, `modules/mod_flexicontent/mod_flexicontent.php`, `modules/mod_flexicontent/helper.php`, `admin/elements/fclayout.php` and `admin/controllers/templates.raw.php`.
:::

## Terminology

| What you customize | Mechanism | Documentation |
| --- | --- | --- |
| Output of a module | `layout` parameter, `modules/<module>/tmpl/<layout>.php` or Joomla override | This page |
| Whole item/category page | FLEXIcontent content templates | [Template structure](../templates/structure.md) |
| Rendering of one field | Field layouts | [Create a field layout](../fields/field-layouts.md) |
| Outer HTML around a module | Joomla module chrome, `modChrome_*` in `templates/<template>/html/modules.php` | Joomla documentation |

A module theme does **not** replace the item template: field values are already computed in `$item->fields[...]->display` before the module layout renders them.

## Before you start

- Install and enable the FLEXIcontent module you want to customize.
- Identify the Joomla template style actually used on the pages where the module appears.
- Use FTP, a file manager or your deployment tool: the layout is a file, not an option in the module manager.
- Never edit the bundled files in `modules/<module>/tmpl/` directly. A FLEXIcontent update can overwrite them.

## How the selector finds layouts

In the module manager, open the module and go to **Basic → Template Layout → Layout**. The field is defined with `type="fclayout"` and, for `mod_flexicontent`, scans:

```xml
<field
    name="layout"
    type="fclayout"
    default="news"
    label="FLEXI_CHOOSE_TMPL"
    directory="/modules/mod_flexicontent/tmpl"
    ext_name="mod_flexicontent"
    hide_default="1"
    hide_none="1"
    stripext="1"
    filter="\.php$"
    exclude="^_"
    params_source="file"
/>
```

The selector lists direct `.php` children of the configured directory. Files whose name starts with `_` are ignored. It also scans enabled Joomla templates for:

```text
templates/<active_template>/html/<module>/<layout>.php
```

An override with the same name as a built-in layout is applied automatically and is disabled in the selector. To force a specific template, use the value `template:layout`, for example `my_template:mynews`.

A same-named `.xml` file supplies the layout parameters. The selector label can be translated with `TPL_<template>_<module>_LAYOUT_<name>` in the template language file.

## File locations

For `mod_flexicontent`:

| Purpose | Core location | Upgrade-safe override |
| --- | --- | --- |
| Layout PHP | `modules/mod_flexicontent/tmpl/news.php` | `templates/<template>/html/mod_flexicontent/mynews.php` |
| Layout params | `modules/mod_flexicontent/tmpl/news.xml` | `templates/<template>/html/mod_flexicontent/mynews.xml` |
| Layout CSS | `modules/mod_flexicontent/tmpl/news/news.css` | `templates/<template>/html/mod_flexicontent/mynews/mynews.css` |
| Header fragment | `modules/mod_flexicontent/tmpl/news/header.php` | `templates/<template>/html/mod_flexicontent/mynews/header.php` |
| Footer fragment | `modules/mod_flexicontent/tmpl/news/footer.php` | `templates/<template>/html/mod_flexicontent/mynews/footer.php` |

Substitute the module name for the others: `mod_flexicategories`, `mod_flexifilter`, `mod_flexiadvsearch`, `mod_flexigooglemap`, `mod_flexitagcloud`.

:::caution
The override path has **no** `/tmpl/` segment after `html/<module>/`. Some old local README files show `html/mod_flexicontent/tmpl/news.php`; do not follow that pattern. Joomla's `ModuleHelper::getLayoutPath()` and FLEXIcontent's selector use `html/mod_flexicontent/news.php`.
:::

Built-in `mod_flexicontent` layouts are `default.php`, `news.php`, `select.php`, `carousel.php` and `swiper.php`. Shared snippets live in `modules/mod_flexicontent/tmpl_common/`.

## Step-by-step: create an override theme

### 1. Copy a base layout

Choose the built-in layout closest to the result you want:

```text
modules/mod_flexicontent/tmpl/default.php  → simple list of titles
modules/mod_flexicontent/tmpl/news.php     → images, dates, fields, tabs, voting, comments
modules/mod_flexicontent/tmpl/select.php   → dropdown
modules/mod_flexicontent/tmpl/carousel.php → carousel
modules/mod_flexicontent/tmpl/swiper.php   → Swiper carousel
```

Copy the PHP file, its XML file and its CSS folder into the Joomla template:

```text
templates/my_template/html/mod_flexicontent/mynews.php
templates/my_template/html/mod_flexicontent/mynews.xml
templates/my_template/html/mod_flexicontent/mynews/mynews.css
```

Use a unique name (`mynews`, not `news`) so the override appears clearly in the selector.

### 2. Rename CSS classes and parameter names

If you copied `news.php`, rename its layout-specific CSS class and parameter prefixes:

```php
class="news mod_flexicontent_wrapper"   → class="mynews mod_flexicontent_wrapper"
```

```xml
name="news_params_layout"               → name="mynews_params_layout"
name="news_item_placement_*"            → name="mynews_item_placement_*"
```

In CSS, replace the `.news` selector with `.mynews`. Namespace IDs with `$module->id` and, for per-category output, the category id.

### 3. Check the PHP contract

Start from the copied file: variables differ between modules and between layouts. For `mod_flexicontent`, the main scope includes `$params`, `$module`, `$moduleclass_sfx`, `$layout`, `$ordering`, `$list`, `$list_totals`, `$catdata`, `$catdata_arr`, `$count`, `$featured` and `$wa`.

A minimal structure looks like this:

```php
<?php
defined('_JEXEC') or die('Restricted access');

// $list is an array of ordering groups, each with 'featured' and 'standard' items.
?>
<div class="mynews mod_flexicontent_wrapper mod_flexicontent_wrap<?php echo $moduleclass_sfx; ?>"
     id="mod_flexicontent_<?php echo $layout . '_' . $module->id; ?>">

    <?php foreach ($ordering as $ord) : ?>
        <?php if (!isset($list[$ord])) continue; ?>

        <div class="order_group" id="order_<?php echo $ord . $module->id; ?>">
            <?php if (!empty($ordering_addtitle) && isset($ordering[$ord])) : ?>
                <h4><?php echo htmlspecialchars($ordering[$ord], ENT_QUOTES, 'UTF-8'); ?></h4>
            <?php endif; ?>

            <?php foreach (array('featured', 'standard') as $group) : ?>
                <?php if (empty($list[$ord][$group])) continue; ?>

                <ul class="mod_flexicontent mod_flexicontent_<?php echo $group; ?>">
                    <?php foreach ($list[$ord][$group] as $item) : ?>
                        <li class="<?php echo !empty($item->is_active_item) ? 'fcitem_active' : ''; ?>">
                            <a href="<?php echo htmlspecialchars($item->link, ENT_QUOTES, 'UTF-8'); ?>">
                                <?php echo htmlspecialchars($item->title, ENT_QUOTES, 'UTF-8'); ?>
                            </a>

                            <?php if (!empty($item->fields)) : ?>
                                <?php foreach ($item->fields as $name => $field) : ?>
                                    <div class="mynews_field mynews_field_<?php echo $name; ?>">
                                        <span class="mynews_label">
                                            <?php echo htmlspecialchars($field->label, ENT_QUOTES, 'UTF-8'); ?>
                                        </span>
                                        <span class="mynews_value"><?php echo $field->display; ?></span>
                                    </div>
                                <?php endforeach; ?>
                            <?php endif; ?>
                        </li>
                    <?php endforeach; ?>
                </ul>
            <?php endforeach; ?>
        </div>
    <?php endforeach; ?>
</div>
```

`$field->display` is already rendered and access-filtered by FLEXIcontent. Do not query raw field values again in the layout unless you know the ACL implications.

Common item properties include `id`, `title`, `fulltitle`, `alias`, `link`, `text`, `image`, `image_rendered`, `date_created`, `date_modified`, `hits_rendered`, `voting`, `comments_rendered`, `fields`, `catid`, `itemcats`, `typename`, `access` and `featured`.

Use `Text::_('KEY')` for translatable strings. Shared snippets can be included from their absolute core path:

```php
include(JPATH_SITE . '/modules/mod_flexicontent/tmpl_common/category.php');
include(JPATH_SITE . '/modules/mod_flexicontent/tmpl_common/favlist.php');
include(JPATH_SITE . '/modules/mod_flexicontent/tmpl_common/readon.php');
```

### 4. Add layout parameters

Create `mynews.xml` next to `mynews.php`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<form>
    <name>mod_flexicontent - mynews Layout</name>
    <version>1.0</version>
    <description>Parameters for the mynews module theme</description>

    <fields name="params">
        <fieldset name="layout" addfieldpath="/administrator/components/com_flexicontent/elements">
            <field
                name="mynews_columns"
                type="list"
                default="2"
                label="Columns"
            >
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </field>
        </fieldset>
    </fields>
</form>
```

Read the value in the layout with:

```php
$columns = (int) $params->get('mynews_columns', 2);
```

The XML structure must be `<fields name="params">` containing `<fieldset name="layout">`. If no XML is found, FLEXIcontent falls back to `tmpl/_fallback/_fallback.xml`, which exposes generic `custom1`–`custom5` parameters.

:::note
Layout parameters are saved through Joomla's `onExtensionBeforeSave` event. Some third-party module managers may not persist them.
:::

### 5. Register the CSS in the override

Core auto-loads layout CSS only from `modules/<module>/tmpl/<layout>/<layout>.css`. For an override, register the stylesheet explicitly:

```php
$wa = $app->getWebAssetManager();
$wa->registerAndUseStyle(
    'mod_flexicontent.mynews',
    'templates/' . $app->getTemplate() . '/html/mod_flexicontent/mynews/mynews.css',
    array('version' => FLEXI_VHASH)
);
```

If the module output is captured by another extension and CSS is not injected into `<head>`, set the module option **Add CSS** (`add_ccs`) to `2` to inline the `<link>` in the module HTML.

### 6. Select the theme in the module

1. Go to **Extensions → Modules** and open the FLEXIcontent module.
2. In the **Basic** tab, under **Template Layout**, choose the new layout.
3. If you forced a specific template, select `my_template:mynews`; otherwise select the plain `mynews` entry.
4. Save the module.
5. Clear the Joomla cache and reload the front page if the layout or its parameters do not appear.

## Alternative: add a layout inside the module folder

You can duplicate the files directly under `modules/mod_flexicontent/tmpl/`:

```text
modules/mod_flexicontent/tmpl/mynews.php
modules/mod_flexicontent/tmpl/mynews.xml
modules/mod_flexicontent/tmpl/mynews/mynews.css
```

This is simpler, but **not upgrade-safe**. Prefer the Joomla template override unless you are developing the layout in a version-controlled custom package.

## Header and footer fragments

Some shipped layouts use optional `header.php` and `footer.php` files. The main module code captures them with output buffering and renders them only for layouts that declare these fragments. When creating a fresh theme, put all markup in the main layout unless you deliberately copy the corresponding core fragment structure.

## Language strings

To give the selector a readable label, add a key to the active template language file:

```ini
TPL_MY_TEMPLATE_MOD_FLEXICONTENT_LAYOUT_MYNEWS="My news theme"
```

Pattern: `TPL_<template>_<module>_LAYOUT_<name>`. Without that key, the selector shows the raw filename.

## Caching and display rules

- The module supports Joomla caching (`cache`, `cache_time`). Clear the cache after changing layout files or parameters.
- **Show in views**, **Show in clients**, **Enable PHP rule** and **PHP rule code** are evaluated before the layout is included. A theme cannot display a module hidden by these rules.
- Client detection is ignored when Joomla caching is on unless platform-specific caching is configured.
- There is no pagination in the module layout. Use `count`, `count_feat` and `offset_items`.
- Ordering groups come from `$ordering`; `$ordering_addtitle` controls group headings.
- With **Apply configuration per category**, the layout is included once per category. `$catdata`, `$list`, `$list_totals` and `$items_exist` are in scope.

## Troubleshooting

| Problem | Likely cause |
| --- | --- |
| Layout missing from the selector | The PHP file must be a direct `.php` child of the module layout directory, not start with `_`, and the Joomla template style must be enabled. Clear the cache. |
| Override not used | Wrong path: use `templates/<template>/html/<module>/<layout>.php`, with no `/tmpl/` segment. Use `template:layout` to force a template. |
| Layout parameters tab empty | XML basename must match the PHP basename and use `<fields name="params"><fieldset name="layout">`. |
| CSS not applied | Register the stylesheet in the override; core auto-loading only checks the module directory. Try `add_ccs=2` if output is captured. |
| Header/footer ignored | The layout must declare the corresponding core `header.php` / `footer.php` structure. |
| Duplicate JavaScript or DOM ids | Namespace classes and include `$module->id` and the category id in generated ids. |
| Parameters not saved | The module manager must trigger `onExtensionBeforeSave`. |

## Official references

- [How to create a custom layout for the Universal Content module and other FLEXIcontent modules](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/274-how-to-create-a-custom-layout-for-universal-content-module-and-other-flexicontent-modules.html)
- [English tutorials](https://flexicontent.org/documentation/tutorials-english.html)
- [Official documentation notes](https://flexicontent.org/_documentation_notes/)
- [FLEXIcontent source](https://github.com/FLEXIcontent/flexicontent-cck)
