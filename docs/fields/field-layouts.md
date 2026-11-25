---
title: Create a field layout
sidebar_position: 3
---

# Create a field layout

A **field layout** controls the HTML of one field. It is not the same as an item or category template: the item template decides *where* a field is displayed; the field layout decides *how its value or form input is rendered*.

:::info Source
Based on FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), especially `admin/helpers/fcfield/parentfield.php`, `admin/elements/fcfilelist.php`, `admin/elements/fclayout.php` and the bundled `plugins/flexicontent_fields/*/tmpl/` layouts.
:::

:::tip
A layout changes rendering only. If you need a new way to store, validate or process a value, create a [field type plugin](./create-a-field-type.md) instead.
:::

## Terminology

| What you customize | Parameter | File pattern |
| --- | --- | --- |
| Frontend value output | `viewlayout` | `value_<name>.php` |
| Item form input | `formlayout` | `field_<name>.php` |
| Image gallery | `popuptype`, `popuptype_mobile` | `value_gallery_<name>.php` or `value_<name>.php` |
| Whole item page | `ilayout` | `components/com_flexicontent/templates/<layout>/item.php` |
| Whole category page | `clayout` | `components/com_flexicontent/templates/<layout>/category.php` |

The layout selector stores only the suffix. `value_MyLayout.php` is selected as `MyLayout`.

## Where layout files live

For a custom field type:

```text
plugins/flexicontent_fields/<field_type>/tmpl/value_MyLayout.php
plugins/flexicontent_fields/<field_type>/tmpl/value_MyLayout.xml   # optional parameters
plugins/flexicontent_fields/<field_type>/tmpl/field_MyForm.php
```

For a core field, a subtype folder is added:

```text
plugins/flexicontent_fields/core/tmpl/<subtype>/value_MyTitle.php
```

Examples of subtypes: `title`, `created`, `createdby`, `modified`, `modifiedby`, `voting`, `favourites`, `categories`, `tags`.

A Joomla template override can also provide the file:

```text
templates/<active_template>/html/flexicontent_fields/<field_type>/value_MyLayout.php
templates/<active_template>/html/flexicontent_fields/core/<subtype>/value_MyTitle.php
```

Runtime prefers the Joomla override over the plugin file. However, the layout dropdown generally scans the **plugin** directories. Keep a discoverable file in `tmpl/` if you want the layout to appear in the selector.

:::caution
Never modify a shipped default layout. Copy it to a new name first. Custom layouts may need to be reviewed after a FLEXIcontent upgrade.
:::

## How the selector finds layouts

Most field types use the classic `fcfilelist` selector:

```xml
<field
    name="viewlayout"
    type="fcfilelist"
    directory="plugins/flexicontent_fields/text/tmpl/"
    filter="^value_.*\.php$"
    stripext="1"
    stripprefix="value_"
    hide_none="1"
    hide_default="1"
/>
```

`fcfilelist` lists the files matching the filter, removes the `value_` prefix and the `.php` extension, and stores the remaining suffix.

Some field types use `fclayout`, which can group built-in layouts and load parameters from a same-named XML file through AJAX. The image field is a special case: it uses `popuptype` for desktop galleries and `popuptype_mobile` for a mobile override.

## Step-by-step: create a custom value layout

### 1. Choose a base layout

Copy the default layout of the **same field type**, because each plugin exposes different variables.

```text
text       → plugins/flexicontent_fields/text/tmpl/value_default.php
file       → plugins/flexicontent_fields/file/tmpl/value_InlineBoxes.php
image      → plugins/flexicontent_fields/image/tmpl/value_gallery_fancybox.php
core/title → plugins/flexicontent_fields/core/tmpl/title/value_default.php
```

Empty parameters do not always resolve to `value_default.php`. For example, `file` and `mediafile` default to `value_InlineBoxes.php`, and `toolbar` defaults to `value_sharing_button.php`.

### 2. Copy and rename the file

```text
plugins/flexicontent_fields/text/tmpl/value_default.php
→
plugins/flexicontent_fields/text/tmpl/value_MyLayout.php
```

The suffix must follow the selector rules. With the usual `value_*.php` filter, use letters, digits and underscores. `MyLayout.php` or `valueMyLayout.php` will not be found.

### 3. Edit the PHP layout

A text-like layout follows this contract:

```php
<?php
/**
 * value_MyLayout.php
 *
 * Variables supplied by the field plugin include:
 * $field, $item, $values, $prop, $view, $sfx,
 * $is_ingroup, $use_ingroup, $multiple,
 * $pretext, $posttext, $opentag, $closetag,
 * $separatorf, $itemprop, $no_value_msg, $remove_space
 */

$n = 0;

foreach ($values as $value)
{
    if ($value === null || !strlen($value))
    {
        if ($is_ingroup)
        {
            $field->{$prop}[$n++] = '';
        }
        continue;
    }

    // Escape values unless trusted HTML is intentional.
    $html = htmlspecialchars((string) $value, ENT_QUOTES, 'UTF-8');
    $html = '<span class="my-field-value">' . $html . '</span>';

    // Prefix and suffix are configured in the field parameters.
    $field->{$prop}[$n] = $pretext . $html . $posttext;

    // Per-value microdata is needed for fields inside a field group.
    if ($is_ingroup && $itemprop)
    {
        $field->{$prop}[$n] =
            '<div style="display:inline" itemprop="' . $itemprop . '">'
            . $field->{$prop}[$n]
            . '</div>';
    }

    $n++;

    if (!$multiple)
    {
        break;
    }
}
```

A layout normally **writes into** `$field->{$prop}`; it does not echo the final value. The field plugin applies `$separatorf`, `$opentag`, `$closetag`, microdata and the “no value” message after including the layout.

| Variable | Meaning |
| --- | --- |
| `$field` | Field object, including `$field->parameters`, `$field->id`, `$field->name`, `$field->label`. |
| `$item` | Current item object. |
| `$values` | Raw values for the field. |
| `$prop` | Property to fill, usually `display` or a display method suffix. |
| `$view` | Current view, for example `item` or `category`. |
| `$multiple` | Whether the field accepts several values. |
| `$is_ingroup` | Whether the field is rendered inside a repeatable field group. |
| `$pretext`, `$posttext` | Configured prefix and suffix. |
| `$separatorf` | Separator between multiple rendered values. |
| `$opentag`, `$closetag` | Wrappers added around the complete value list. |
| `$itemprop` | Microdata property. |
| `$no_value_msg` | Message shown when the field is empty. |

Complex fields expose more variables. Read the comments at the top of the base layout before editing it.

### 4. Optionally add layout parameters

A same-named XML file can define parameters for the layout:

```text
plugins/flexicontent_fields/text/tmpl/value_MyLayout.xml
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<form>
    <name>My custom layout -- Text</name>
    <author>Your Name</author>
    <version>1.0</version>
    <description>Custom parameters for value_MyLayout.php</description>

    <fields name="attribs">
        <fieldset name="layout" addfieldpath="/administrator/components/com_flexicontent/elements">
            <field
                name="PPFX_my_option"
                type="radio"
                default="0"
                label="MY_EXTENSION_MY_OPTION"
                description="MY_EXTENSION_MY_OPTION_DESC"
                class="btn-group btn-group-yesno">
                <option value="0">FLEXI_NO</option>
                <option value="1">FLEXI_YES</option>
            </field>
        </fieldset>
    </fields>
</form>
```

Read the value in the PHP layout with the layout prefix:

```php
$LP = 'viewlayout_';
$my_option = $field->parameters->get($LP . 'my_option', 0);
```

Use `popuptype_` or `popuptype_mobile_` instead of `viewlayout_` for image galleries. `PPFX_` is a placeholder that FLEXIcontent rewrites to the actual layout parameter prefix.

:::note
Per-layout XML parameters are loaded by the enhanced `fclayout` selector with `params_source="file"`. With the classic `fcfilelist` selector, the layout works, but its XML parameters are not shown automatically in the field form.
:::

### 5. Select the layout in the field configuration

1. Open the field in **Components → FLEXIcontent → Fields**.
2. In the **Viewing** section, open **Layout**.
3. Set **Values layout** (`viewlayout`) to `MyLayout`.
4. Save the field.

For an image gallery, set **Gallery Layout** (`popuptype`) instead. For the edit form, use **Fields layout** (`formlayout`) and choose the suffix of a `field_*.php` file.

### 6. Display the field

Selecting a layout does not place the field on the page. Add the field to an item or category template position in the FLEXIcontent template editor, or render it manually:

```php
$html = FlexicontentFields::getFieldDisplay($item, 'myfield');
echo $html;
```

Display methods can be selected explicitly:

```php
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display_small', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display_medium', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display_large', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display_original', 'item');
```

See [Item loops and field rendering](../templates/loops-fields.md) and [Field positions and drag and drop](../templates/positions.md).

## Form layouts

Form layouts use the `field_<name>.php` prefix and are selected with `formlayout`.

```text
plugins/flexicontent_fields/text/tmpl/field_MyForm.php
```

Copy the default `field_default.php` of the same field type, keep the form field names and JavaScript integration, then change only the markup. A wrong name or missing field attribute can prevent the value from being saved in the item form.

## Differences from item and category templates

| | Field layout | Item/category layout |
| --- | --- | --- |
| Scope | One field value or input. | Whole page and field positions. |
| Files | `value_*.php`, `field_*.php`. | `item.php`, `category_items.php`, XML manifests. |
| Selected by | `viewlayout`, `formlayout`, `popuptype`. | `ilayout`, `clayout`. |
| Stored in | Field parameters. | Item/category/layout configuration. |
| Joomla override | `html/flexicontent_fields/<type>/`. | `html/com_flexicontent/...`. |

Joomla component view overrides (`templates/<template>/html/com_flexicontent/<view>/default.php`) are a third mechanism and do not replace field layouts.

## Gotchas

- **Do not edit default layouts.** Copy them.
- **Use the exact file prefix.** `value_MyLayout.php`, not `MyLayout.php`.
- **Copy from the same field type.** Variables differ between text, file, image, relation and core fields.
- **Do not echo the final output.** Fill `$field->{$prop}` so separators and wrappers still apply.
- **Respect groups and multiple values.** Keep placeholders for empty values when `$is_ingroup` is true.
- **Escape values and URLs.** If your layout bypasses `clean_output` or `encode_output`, use `htmlspecialchars()` and validate URLs.
- **Use unique HTML ids.** The same field can be rendered for several items. Base ids on `$field->id` and `$item->id`.
- **Check every view.** Item, category, module, backend, mobile and field-group rendering can differ.
- **Clear the cache if needed.** Layout paths and template definitions are cached during a request and by Joomla.
- **Content plugins may transform the output.** Check `trigger_onprepare_content` and `trigger_plgs_incatview` if the result changes unexpectedly.
- **Trusted administrators only.** Field layouts are executable PHP, and field layout parameters are stored with elevated privileges.

## Official references

- [Create an output layout for the File field](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/711-create-a-outout-layout-for-file-field.html)
- [Override field render](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/772-override-field-render.html)
- [Using the raw value of a field inside a template or another field layout](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/312-using-the-raw-value-of-a-field-inside-a-template-file-or-inside-a-new-custom-field-type.html)
- [Author profile custom field layout example](https://www.flexicontent.org/documentation/tutorials-english/71-fields-usages-tips-joomla-plugin/304-how-to-create-a-field-that-links-to-author-listing-view-of-current-item-author.html)
- [Developer API / field plugins index](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins.html)
- [Manual field rendering with `getFieldDisplay()`](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/248-upgrading-custom-templates-to-work-in-v156.html)
