---
title: Create a field type
sidebar_position: 4
---

# Create a field type

A **field type** is a Joomla plugin in the `flexicontent_fields` group. It provides the PHP code that renders a field in the item form, renders its value on the frontend, validates what is saved, and optionally adds search and filter support.

Write a new field type only when an existing type plus a [field layout](./field-layouts.md) cannot do the job. If you only want to add a field of an existing type, follow [Create a field](./create-a-field.md) instead.

:::info Source
Based on FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), especially `plugins/flexicontent_fields/text/`, `admin/helpers/fcfield/parentfield.php`, `admin/models/field.php`, `admin/models/parentclassitem.php`, `site/classes/helpers/flexiutilities.php` and `site/classes/helpers/db.php`.
:::

## What you are creating

| Task | Where it happens | Documentation |
| --- | --- | --- |
| Add a field of an existing type | **Components → FLEXIcontent → Fields** | [Create a field](./create-a-field.md) |
| Change the HTML of one existing field | `viewlayout` / `formlayout` layouts | [Create a field layout](./field-layouts.md) |
| Add a new storage/rendering behavior | `plugins/flexicontent_fields/<type>/` plugin | This page |
| Add a Joomla `com_fields` field | Joomla field plugins | Joomla documentation |

A FLEXIcontent field type is **not** a Joomla custom-field plugin. It registers through `#__extensions` with `folder = 'flexicontent_fields'` and its values are stored in `#__flexicontent_fields_item_relations`.

## File structure

The plugin element is the folder name. Use lowercase letters, digits and underscores, with no spaces.

```text
plugins/flexicontent_fields/myfield/
├── myfield.php                                  # required: main class
├── myfield.xml                                  # required: Joomla plugin manifest
├── index.html                                   # empty directory marker
├── en-GB.plg_flexicontent_fields_myfield.ini    # language file
├── tmpl/
│   ├── field_default.php                        # item form input
│   └── value_default.php                        # frontend value
└── js/                                          # optional, if used
```

`FLEXIUtilities::call_FC_Field_Func()` requires the main file at exactly `plugins/flexicontent_fields/<element>/<element>.php`. The field manager also throws an exception if `<element>.xml` is missing.

### Naming contract

For element `myfield`:

| Item | Value |
| --- | --- |
| Folder | `plugins/flexicontent_fields/myfield/` |
| Main file | `myfield.php` |
| Manifest | `myfield.xml` |
| Class | `plgFlexicontent_fieldsMyfield` |
| `static $field_types` | `array('myfield')` |
| Manifest `<name>` | `FLEXIcontent - My Field` |
| Manifest `<filename plugin="...">` | `myfield` |
| Fieldset names | `group-myfield-editing`, `group-myfield-viewing`, … |
| Language file | `en-GB.plg_flexicontent_fields_myfield.ini` |

The constructor of `FCField` derives the field type from the class name (`strtolower(get_class($this))`), so capitalization matters. The selector strips the `FLEXIcontent - ` prefix from the manifest name and shows the remainder.

## Choose a base plugin

Do not start from an empty file. Copy the bundled plugin that is closest to what you need:

| Base plugin | Use when |
| --- | --- |
| `text` | Single or multiple text values, custom validation, prefixes/suffixes. Best general starting point. |
| `textarea` | Longer text with similar value handling. |
| `select`, `radio`, `checkbox` | Predefined choices; these extend `FCIndexedField` for indexed/filterable values. |
| `email` | Email-specific validation. |
| `file`, `image`, `mediafile` | Uploads, previews and file cleanup. |

The official tutorial uses exactly this approach: duplicate the `text` field and rename it.

## Step-by-step: duplicate `text` as `myfield`

### 1. Copy the folder

```bash
cp -a plugins/flexicontent_fields/text plugins/flexicontent_fields/myfield
```

Rename the files:

```text
text.php                                  → myfield.php
text.xml                                  → myfield.xml
en-GB.plg_flexicontent_fields_text.ini    → en-GB.plg_flexicontent_fields_myfield.ini
```

:::caution
Do a search-and-replace **with confirmation for each occurrence**. The word `text` also appears in unrelated names such as `JText`, `text-align` or SQL aliases like `value as text`. Only change field-type references.
:::

### 2. Update the PHP class

In `myfield.php`:

```php
<?php
defined('_JEXEC') or die('Restricted access');

// Lazy loading of the FLEXIcontent field base class (5.x style).
spl_autoload_register(static function ($class) {
    $map = array(
        'FCField' => JPATH_ADMINISTRATOR . '/components/com_flexicontent/helpers/fcfield/parentfield.php',
    );
    if (isset($map[$class]) && is_file($map[$class])) require_once $map[$class];
}, true, true);

class plgFlexicontent_fieldsMyfield extends FCField
{
    static $field_types = array('myfield');

    var $task_callable = null;  // Methods callable via AJAX; null = none.

    public function __construct(&$subject, $params)
    {
        parent::__construct($subject, $params);
    }
}
```

`FCField` extends `\Joomla\CMS\Plugin\CMSPlugin` (`admin/helpers/fcfield/parentfield.php:14`). FLEXIcontent 5.x still uses legacy plugin class names; there is no namespace declaration. Use fully qualified `\Joomla\CMS\...` calls as the bundled plugins do.

Change every guard from the old literal to the new one:

```php
if (!in_array($field->field_type, static::$field_types)) return;
```

:::note
Do not keep old 4.x boilerplate such as `jimport()` or `JLoader::register('FCField', ...)`. In 5.x the parent constructor also loads `plg_flexicontent_fields_myfield` language files automatically, so no manual `JPlugin::loadLanguage()` call is needed.
:::

### 3. Know the events you can implement

`FLEXIUtilities::call_FC_Field_Func()` instantiates the class and calls a method only if it exists. Implementing a method also enables the matching capability flags in the field options.

| Method | Exact signature | Purpose |
| --- | --- | --- |
| `onDisplayField` | `(&$field, &$item)` | Build the item form input. |
| `onDisplayFieldValue` | `(&$field, $item, $values = null, $prop = 'display')` | Build the frontend value. |
| `onBeforeSaveField` | `(&$field, &$post, &$file, &$item)` | Validate/clean posted values before the database write. Returning `false` aborts the save. |
| `onAfterSaveField` | `(&$field, &$post, &$file, &$item)` | Cleanup after the database write. |
| `onBeforeDeleteField` | `(&$field, &$item)` | Remove extra data before the field is deleted. |
| `onAllFieldsPostDataValidated` | `(&$field, &$item)` | Cross-field validation. |
| `onDisplayFilter` | `(&$filter, $value = '', $formName = 'adminForm', $isSearchView = 0)` | Category-view filter. |
| `onAdvSearchDisplayFilter` | `(&$filter, $value = '', $formName = 'searchForm')` | Advanced-search filter. |
| `getFiltered` | `(&$filter, $value, $return_sql = true)` | Matching item ids for category filters. |
| `getFilteredSearch` | `(&$filter, $value, $return_sql = true)` | Matching item ids for search filters. |
| `onIndexAdvSearch` | `(&$field, &$post, &$item)` | Advanced-search index. |
| `onIndexSearch` | `(&$field, &$post, &$item)` | Basic search index. |

There are no events named `onDisplay`, `onBeforeStore`, `onAfterStore`, `onSearch` or `onIndexAdvanced` in FLEXIcontent 5.x. Do not use those names.

For a simple text-like field, `FCField` already provides generic implementations of the display and indexing events. Override only what you need to change.

### 4. Add the rendering methods

The display methods prepare variables and then `include()` a layout from `tmpl/`. The layout writes into `$field->html` for the form and `$field->{$prop}` for the value.

A slimmed version of the `text` methods looks like this:

```php
public function onDisplayField(&$field, &$item)
{
    if (!in_array($field->field_type, static::$field_types)) return;

    $field->label = $field->parameters->get('label_form')
        ? \Joomla\CMS\Language\Text::_($field->parameters->get('label_form'))
        : \Joomla\CMS\Language\Text::_($field->label);

    $this->setField($field);
    $this->setItem($item);

    $multiple    = (int) $field->parameters->get('allow_multiple', 0);
    $use_ingroup = (int) $field->parameters->get('use_ingroup', 0);

    if (!$field->value || (count($field->value) === 1 && reset($field->value) === null)) {
        $field->value = $this->getDefaultValues(true);
    }

    $document  = \Joomla\CMS\Factory::getApplication()->getDocument();
    $fieldname = 'custom[' . $field->name . ']';
    $elementid = 'custom_' . $field->name;
    $attribs    = '';
    $classes    = 'fcfield_textval';
    $box_classes = 'fcfield_box';
    $validate_mask = '';
    $pretext_form  = $field->parameters->get('pretext_form', '');
    $posttext_form = $field->parameters->get('posttext_form', '');
    $auto_value    = 0;

    $field->html = array();

    $formlayout = $field->parameters->get('formlayout', '');
    $formlayout = $formlayout ? 'field_' . $formlayout : 'field_default';
    include(self::getFormPath($this->fieldtypes[0], $formlayout));

    $field->html = !count($field->html)
        ? ''
        : '<div class="fcfieldval_container valuebox fcfieldval_container_' . $field->id . '">'
          . implode('', $field->html) . '</div>';
}

public function onDisplayFieldValue(&$field, $item, $values = null, $prop = 'display')
{
    if (!in_array($field->field_type, static::$field_types)) return;

    $field->label = \Joomla\CMS\Language\Text::_($field->label);
    $this->setField($field);
    $this->setItem($item);

    $app  = \Joomla\CMS\Factory::getApplication();
    $view = $app->input->getCmd('flexi_callview', $app->input->getCmd('view', 'item'));
    if (!$this->checkRenderConds($prop, $view)) return;

    $values     = $values !== null ? $values : $field->value;
    $is_ingroup = !empty($field->ingroup);
    $multiple   = (int) $field->parameters->get('allow_multiple', 0);
    extract($this->getCommonParams());

    if ($prop === 'csv_export') {
        $separatorf = ', ';
        $itemprop   = false;
    }

    $field->{$prop} = array();

    $viewlayout = $field->parameters->get('viewlayout', '');
    $viewlayout = $viewlayout ? 'value_' . $viewlayout : 'value_default';
    include(self::getViewPath($field->field_type, $viewlayout));

    if (!$is_ingroup) {
        $field->{$prop} = implode($separatorf, $field->{$prop});

        if ($field->{$prop} !== '') {
            $field->{$prop} = $opentag . $field->{$prop} . $closetag;
            if ($itemprop) {
                $field->{$prop} = '<div style="display:inline" itemprop="' . $itemprop . '">' . $field->{$prop} . '</div>';
            }
        } elseif ($no_value_msg !== '') {
            $field->{$prop} = $no_value_msg;
        }
    }
}
```

Important details:

- There is no `$form`, `$input` or standalone `$id` argument passed to a field layout. Use `$field->parameters`, `$field->id`, `$item->id` and `$app->input`.
- `getFormPath()` and `getViewPath()` resolve overrides in `templates/<template>/html/flexicontent_fields/<element>/` before the plugin folder.
- `$fieldname` must be `custom[<field name>]` and inputs must be named `custom[<field name>][<n>]`, otherwise FLEXIcontent will not save the values.
- `getCommonParams()` supplies `$pretext`, `$posttext`, `$opentag`, `$closetag`, `$separatorf`, `$itemprop` and `$no_value_msg`.

### 5. Create the layout files

`tmpl/field_default.php`:

```php
<?php
defined('_JEXEC') or die('Restricted access');

$n = 0;
foreach ($field->value as $value)
{
    $value       = $value ?? '';
    $fieldname_n = $fieldname . '[' . $n . ']';
    $elementid_n = $elementid . '_' . $n;

    $field->html[] = $pretext_form .
        '<div class="' . $box_classes . '">' .
            '<input type="text" id="' . htmlspecialchars($elementid_n, ENT_QUOTES, 'UTF-8') . '"' .
            ' name="' . htmlspecialchars($fieldname_n, ENT_QUOTES, 'UTF-8') . '"' .
            ' value="' . htmlspecialchars($value, ENT_COMPAT, 'UTF-8') . '"' .
            ' class="' . $classes . '" ' . $attribs . ' />' .
        '</div>' .
        $posttext_form;

    $n++;
    if (!$multiple && !$use_ingroup) break;
}
```

`tmpl/value_default.php`:

```php
<?php
defined('_JEXEC') or die('Restricted access');

$n = 0;
foreach ($values as $value)
{
    if ($value === null || !strlen($value))
    {
        if ($is_ingroup) $field->{$prop}[$n++] = '';
        continue;
    }

    $field->{$prop}[$n] = $pretext . htmlspecialchars($value, ENT_QUOTES, 'UTF-8') . $posttext;

    if ($is_ingroup && $itemprop)
    {
        $field->{$prop}[$n] = '<div style="display:inline" itemprop="' . $itemprop . '">' . $field->{$prop}[$n] . '</div>';
    }

    $n++;
    if (!$multiple) break;
}
```

These are minimal examples. The bundled `text` layouts include multi-value controls, input masks, microdata and floating labels; copy them when you need those features.

### 6. Validate before saving

Custom field values are stored in `#__flexicontent_fields_item_relations`. FLEXIcontent reads `custom[<field name>]`, normalizes it to an array, unserializes existing values and passes the array by reference to `onBeforeSaveField()`.

Return `false` to abort the item save with an error. A typical implementation:

```php
public function onBeforeSaveField(&$field, &$post, &$file, &$item)
{
    if (!in_array($field->field_type, static::$field_types)) return;
    if (!is_array($post) && !strlen($post)) return;

    $post      = !is_array($post) ? array($post) : $post;
    $maxlength = (int) $field->parameters->get('maxlength', 0);
    $validation = $field->parameters->get('validation', 'HTML');
    $required  = (int) $field->parameters->get('required', 0);
    $clean     = array();

    foreach ($post as $value)
    {
        $value    = trim((string) $value);
        $filtered = strlen($value) ? flexicontent_html::dataFilter($value, $maxlength, $validation, 0) : '';

        if ($value !== '' && $filtered === '') return false;
        if ($required && $filtered === '') return false;

        if (strlen($filtered)) $clean[] = $filtered;
    }

    $post = $clean;
}
```

ACL, published state and view/client visibility are handled by FLEXIcontent core. `checkRenderConds()` in the display method respects those rules. There is no generic server-side `required` or `unique` enforcement in the save path, so implement such rules yourself.

### 7. Update the XML manifest

A minimal manifest for the example:

```xml
<?xml version="1.0" encoding="utf-8"?>
<extension type="plugin" version="1.6" group="flexicontent_fields" method="upgrade">
    <name>FLEXIcontent - My Field</name>
    <author>Your Name</author>
    <creationDate>2026-11-25</creationDate>
    <copyright>Copyright (C) 2026 Your Name</copyright>
    <license>GNU/GPL v2</license>
    <authorEmail>you@example.com</authorEmail>
    <authorUrl>https://example.com</authorUrl>
    <version>1.0.0</version>
    <description>FLEXI_FIELD_MYFIELD</description>
    <documentation url="https://www.flexicontent.org/documentation/" title="FLEXI_ABOUT" modal="1" icon="info" />

    <files>
        <filename plugin="myfield">myfield.php</filename>
        <filename>index.html</filename>
        <folder>tmpl</folder>
        <folder>js</folder>
    </files>

    <config>
        <fields name="attribs">
            <fieldset name="group-myfield-editing" hidden="true" icon_class="icon-pencil"
                      label="FLEXI_FIELD_EDITING"
                      addfieldpath="/administrator/components/com_flexicontent/elements">
                <field name="required" type="radio" default="0"
                       label="FLEXI_FIELD_REQUIRED" description="FLEXI_FIELD_REQUIRED_DESC"
                       class="btn-group btn-group-yesno">
                    <option value="0">FLEXI_NO</option>
                    <option value="1">FLEXI_YES</option>
                </field>
                <field name="default_value" type="text" filter="raw" default=""
                       label="FLEXI_PROPERTY_DEFAULT" description="FLEXI_PROPERTY_DEFAULT_DESC" />
                <field name="formlayout" type="fcfilelist" default=""
                       label="FLEXI_FIELD_SELECT_FORM_LAYOUT" description="FLEXI_FIELD_SELECT_FORM_LAYOUT_DESC"
                       directory="plugins/flexicontent_fields/myfield/tmpl/"
                       filter="^field_.*\.php$" stripext="1" stripprefix="field_"
                       hide_none="1" hide_default="1" />
                <field name="viewlayout" type="fcfilelist" default=""
                       label="FLEXI_FIELD_SELECT_VIEW_LAYOUT" description="FLEXI_FIELD_SELECT_VIEW_LAYOUT_DESC"
                       directory="plugins/flexicontent_fields/myfield/tmpl/"
                       filter="^value_.*\.php$" stripext="1" stripprefix="value_"
                       hide_none="1" hide_default="1" />
            </fieldset>
        </fields>
    </config>

    <languages>
        <language tag="en-GB">en-GB.plg_flexicontent_fields_myfield.ini</language>
    </languages>
</extension>
```

Key rules:

- `group="flexicontent_fields"` and `type="plugin"` register the extension with Joomla. There is no extra FLEXIcontent metadata attribute.
- The parameter container is `<fields name="attribs">`, **not** `name="params"`.
- Fieldset names must start with `group-<type>-`; otherwise the options do not appear in the field editor.
- `directory` in the layout selectors must point to your plugin's `tmpl/` folder.
- Add every asset folder you actually ship to `<files>`, and bump `<version>` for updates.

### 8. Add language strings

`en-GB.plg_flexicontent_fields_myfield.ini`:

```ini
FLEXI_FIELD_MYFIELD="My Field Plugin for FLEXIcontent"
FLEXI_FIELD_MYFIELD_NOTE="Enter a value"
```

The parent constructor loads the `en-GB` file first, then the current language. Reuse existing `FLEXI_*` keys for common labels such as `FLEXI_FIELD_REQUIRED`; define only your own keys in the plugin file.

### 9. Package, install and enable

1. ZIP the `myfield/` folder. The XML must be at the root of that folder.
2. Go to **Extensions → Install** and install the package.
3. Go to **Extensions → Plugins** and enable **My Field** in the `flexicontent_fields` group. Only enabled plugins appear in the field-type selector.
4. Clear the Joomla cache.
5. Go to **Components → FLEXIcontent → Fields** and [create a field](./create-a-field.md) with type `My Field`.
6. Assign it to a content type, place it in the form and in an item/category template position.
7. Test saving, frontend display and any search/filter options you implemented.

:::caution
Never edit `plugins/flexicontent_fields/text/` or another bundled plugin directly. A FLEXIcontent update overwrites core files. Keep your type in its own folder and version it as a separate installable package.
:::

## CSS, JavaScript and overrides

Load assets from the plugin method or layout using the document Web Asset Manager:

```php
$wa = $document->getWebAssetManager();
$wa->registerAndUseScript(
    'plg.flexicontent_fields.myfield.form',
    \Joomla\CMS\Uri\Uri::root(true) . '/plugins/flexicontent_fields/myfield/js/form.js',
    array('version' => 'auto')
);
```

Declare `js/`, `css/` or other folders in `<files>` or they will not be installed. To customize only the HTML of a custom type later, put a layout in `templates/<template>/html/flexicontent_fields/myfield/field_mylayout.php` or `value_mylayout.php`; these overrides win over the plugin's `tmpl/` files.

## Search and filtering

Search/filter capability flags are detected by checking which methods exist on the plugin class. If you omit `onIndexSearch()` and `onIndexAdvSearch()`, the corresponding options are disabled in the field editor.

The simplest implementations delegate to FLEXIcontent helpers:

```php
public function onIndexSearch(&$field, &$post, &$item)
{
    if (!in_array($field->field_type, static::$field_types)) return;
    if (!$field->issearch) return;

    FlexicontentFields::onIndexSearch($field, $post, $item, array(), array(), ' ', 'strip_tags');
    return true;
}

public function onIndexAdvSearch(&$field, &$post, &$item)
{
    if (!in_array($field->field_type, static::$field_types)) return;
    if (!$field->isadvsearch && !$field->isadvfilter) return;

    FlexicontentFields::onIndexAdvSearch($field, $post, $item, array(), array(), ' ', 'strip_tags');
    return true;
}
```

For predefined choices that need proper indexed filtering, start from `select` or `radio`, which extend `FCIndexedField` and maintain the indexed value columns. Rebuild the search index after changing indexing logic.

## Troubleshooting

| Problem | Likely cause |
| --- | --- |
| Type absent from the selector | Plugin not installed or not enabled, wrong folder/group, or missing XML. Check `#__extensions`. |
| `cann't find field type` / `seems to have been uninstalled` | Main file is not at `<element>/<element>.php`. |
| `Could not find class: plgFlexicontent_fieldsMyfield` | Class name capitalization or prefix is wrong. |
| `Error field XML file for field type ... was not found` | `<element>.xml` is missing from the plugin folder. |
| Type-specific settings tab empty | Fieldset is not named `group-myfield-*`, or the XML uses `name="params"` instead of `name="attribs"`. |
| Raw `FLEXI_FIELD_...` strings displayed | Language file name or key is wrong. |
| No form input | Missing `tmpl/field_default.php`, wrong `formlayout`, or input name is not `custom[<name>][<n>]`. |
| No frontend output | Missing `tmpl/value_default.php`, wrong `viewlayout`, or `$field->{$prop}` was never filled. |
| Search/filter options disabled | Indexing/filter methods are absent from the class. |
| Values not saved | Input name is wrong, value is empty, or `onBeforeSaveField()` returned `false`. |
| Serialized values shown as text | Stored value is an array/object; use `parseValues()` / `unserialize_array()`. |
| Stale layout or parameters | Layout paths and params are cached; clear the Joomla cache. |

## Official references

- [How to duplicate a FLEXIcontent field to create a new field type](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/245-how-to-duplicate-a-flexicontent-field-to-create-a-new-field-type.html)
- [API methods of FLEXIcontent fields](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/301-api-methods-of-flexicontent-fields.html)
- [Developer API / field plugins index](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins.html)
- [Using the raw value of a field inside a template or inside a new custom field type](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/312-using-the-raw-value-of-a-field-inside-a-template-file-or-inside-a-new-custom-field-type.html)
- [FLEXIcontent source](https://github.com/FLEXIcontent/flexicontent-cck)
