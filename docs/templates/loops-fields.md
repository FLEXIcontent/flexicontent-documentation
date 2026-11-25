---
title: Item loops and field rendering
sidebar_position: 3
---

# Item loops and field rendering

FLEXIcontent views bind custom fields to items and render the configured positions before a template runs. A template normally reads the prepared values instead of querying fields itself.

:::info Source
Examples and signatures come from FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), mainly `site/classes/flexicontent.fields.php`, `site/views/category/view.html.php`, `admin/views/item/view.html.php` and the bundled `site/templates/*/category_items.php`.
:::

## Core API: `FlexicontentFields`

Defined in `site/classes/flexicontent.fields.php`.

```php
FlexicontentFields::renderFields(
    $item_per_field = true,
    $item_ids = array(),
    $field_names = array(),
    $view = FLEXI_ITEMVIEW,
    $methods = array(),
    $cfparams = array()
);

FlexicontentFields::getFields(
    &$_items,
    $view = FLEXI_ITEMVIEW,
    $params = null,
    $aid = false,
    $use_tmpl = true,
    $reuse_loaded = false
);

FlexicontentFields::getFieldDisplay(
    &$item_arr,
    $fieldname,
    $single_item_vals = null,
    $method = 'display',
    $view = FLEXI_ITEMVIEW,
    $reload_field_params = true,
    $options = null
);

FlexicontentFields::renderField(
    &$_item,
    &$_field,
    &$values,
    $method = 'display',
    $view = FLEXI_ITEMVIEW,
    $skip_trigger_plgs = false,
    $event_row = false,
    $reload_field_params = true
);

FlexicontentFields::renderPositions(
    &$items,
    $view = FLEXI_ITEMVIEW,
    $params = null,
    $use_tmpl = true,
    & $_rendered = array()
);
```

`getFields()` loads field values and, when `$params` is provided, calls `renderPositions()`. Passing `null` parameters only retrieves values without rendering anything.

## What is already available in each view

### Category view

Before `category_items.php` runs, the category view calls:

```php
$items = FlexicontentFields::getFields($items, 'category', $params, $aid);
```

The template receives those items as `$this->items`. Each item has:

| Property | Contents |
| --- | --- |
| `$item->fields['name']->display` | Rendered HTML of the field. |
| `$item->fields['name']->label` | Label according to field parameters. |
| `$item->positions['position']` | Object of fields assigned to a template position. |
| `$item->onDemandFields` | Fields rendered on demand. |

### Item view

The item view calls:

```php
$_items = array(&$item);
FlexicontentFields::getFields($_items, FLEXI_ITEMVIEW, $params, $aid);
```

`item.php` can therefore use `$item->fields` and `$item->positions` directly.

## Category item loop: canonical reference

A minimal `category_items.php` keeps the filter form, the item loop and one position loop. This mirrors the pattern used by the bundled templates.

```php
<?php
defined('_JEXEC') or die;

// Text search, field filters, alpha index, pagination and ordering form.
ob_start();
file_exists(dirname(__FILE__).DS.'listings_filter_form.php')
    ? include(dirname(__FILE__).DS.'listings_filter_form.php')
    : include(JPATH_SITE.DS.'components'.DS.'com_flexicontent'.DS.'tmpl_common'.DS.'listings_filter_form.php');

$filter_form_html = trim(ob_get_contents());
ob_end_clean();

if ($filter_form_html) {
    echo '<div class="fcclear"></div><aside class="group">' . $filter_form_html . '</aside>';
}

if (!$this->items) {
    echo '<div class="fc-mssg fc-info">' . \Joomla\CMS\Language\Text::_('FLEXI_NO_ITEMS_FOUND') . '</div>';
    return;
}

$items = & $this->items;
$count = count($items);
?>

<div class="fc_category_items">
    <?php foreach ($items as $i => $item) : ?>
        <article class="fc_item flexi item_<?php echo (int) $item->id; ?>">

            <?php if (isset($item->positions['image'])) : ?>
                <div class="flexi lineinfo image group">
                    <?php foreach ($item->positions['image'] as $field) : ?>
                        <div class="flexi element field_<?php echo $field->name; ?>">
                            <?php if ($field->label) : ?>
                                <span class="flexi label field_<?php echo $field->name; ?>">
                                    <?php echo $field->label; ?>
                                </span>
                            <?php endif; ?>
                            <div class="flexi value field_<?php echo $field->name; ?>">
                                <?php echo $field->display; ?>
                            </div>
                        </div>
                    <?php endforeach; ?>
                </div>
            <?php endif; ?>

            <h2 class="fc_item_title">
                <a href="<?php echo $item->link; ?>"><?php echo $item->title; ?></a>
            </h2>

            <?php if (isset($item->fields['text'])) : ?>
                <div class="fcitem_text">
                    <?php echo $item->fields['text']->display; ?>
                </div>
            <?php endif; ?>

        </article>
    <?php endforeach; ?>
</div>
```

The position object shape is:

```php
$item->positions['position_name']->{$field_name}->id;
$item->positions['position_name']->{$field_name}->name;
$item->positions['position_name']->{$field_name}->label;
$item->positions['position_name']->{$field_name}->display;
```

`foreach ($item->positions['image'] as $field)` iterates this object, so `$field->name`, `$field->label` and `$field->display` are always available.

## Rendering a field for the whole list

The bundled `grid` template renders the `text` field for every item in one call before the loop:

```php
FlexicontentFields::getFieldDisplay($items, 'text', null, 'display', 'category');
```

Then the loop only reads the prepared value:

```php
$desc_text = $this->params->get('lead_strip_html', 1)
    ? flexicontent_html::striptagsandcut($item->fields['text']->display, $lead_cut_text, $uncut_length)
    : $item->fields['text']->display;

echo strlen($desc_text) ? '<p>' . $desc_text . '</p>' : '';
```

This avoids rendering the same field once per item. Call `getFieldDisplay()` before `foreach ($items as $item)`, not inside it.

## Rendering one field on demand

`getFieldDisplay()` returns a string for a single item and an array indexed by item id for an array of items. It also populates `$item->fields` and `$item->onDemandFields`.

```php
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname');
echo $html;
```

Available display methods depend on the field plugin:

```php
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display_small', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display_medium', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display_large', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display_original', 'item');
```

A direct read such as `echo $item->fields['fieldname']->display;` requires the field to have been rendered first. Put it in a visible position, in `renderonly`, or render it explicitly as above. See [Field positions and drag and drop](./positions.md). To change the HTML produced by the field itself, create a [field layout](../fields/field-layouts.md).

## Item template: position loop

The template editor generates this skeleton when a new position is added. It works in `item.php` (or `item_html5.php`).

```php
<!-- BOF myposition block -->
<?php $_position_name = "myposition"; ?>

<?php if (isset($item->positions[$_position_name])) : ?>
<div class="flexi lineinfo <?php echo $_position_name; ?> group">

    <?php foreach ($item->positions[$_position_name] as $field) : ?>
    <div class="flexi element field_<?php echo $field->name; ?>">

        <?php if ($field->label) : ?>
            <span class="flexi label field_<?php echo $field->name; ?>">
                <?php echo $field->label; ?>
            </span>
        <?php endif; ?>

        <div class="flexi value field_<?php echo $field->name; ?>">
            <?php echo $field->display; ?>
        </div>

    </div>
    <?php endforeach; ?>

</div>
<?php endif; ?>

<!-- EOF myposition block -->
```

The bundled `modular.php` uses the same structure for positions `subtitle1`, `subtitle2`, `subtitle3`, `subtitle_tab1` to `subtitle_tab12`, `image`, `top`, `description`, `bottom_tab1` to `bottom_tab12` and `bottom`.

Dynamic positions are addressed by name:

```php
$tabpos_name  = 'subtitle_tab'.$tc;
$tabpos_label = \Joomla\CMS\Language\Text::_($this->params->get('subtitle_tab'.$tc.'_label', $tabpos_name));

if (isset($item->positions[$tabpos_name])) : ?>
    <?php foreach ($item->positions[$tabpos_name] as $field) : ?>
        <?php echo $field->display; ?>
    <?php endforeach; ?>
<?php endif; ?>
```

## Common mistakes

| Symptom | Cause |
| --- | --- |
| `$item->fields['name']` is undefined | The field was not rendered. Add it to a position or call `getFieldDisplay()`. |
| A position loop prints nothing | The PHP name does not exactly match the XML `<group>` name, or no field has been assigned in the template editor. |
| Values differ between category and item view | A field method such as `display_small` was used in one view only, or a view-level parameter overrides the field. |
| Slow category pages | `getFieldDisplay()` or `renderField()` called inside the item loop. Move the call before the loop. |

## Official references

- [Template FLEXIcontent — part 4: the contents template](https://www.flexicontent.org/documentation/tutorials-english/84-advanced-tutorials/338-template-flexicontent-part-4-the-contents-template.html)
- [Basic usage: display fields in the item view](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/261-how-to-displat-fields-in-the-frontend-item-view.html)
- [Basic usage: display fields in the category view](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/262-how-to-display-fields-in-the-frontend-category-view.html)
- [Manual field rendering and `renderonly`](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/248-upgrading-custom-templates-to-work-in-v156.html)
- [Displaying a field in multiple places](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/635-how-to-display-a-field-in-multiple-places.html)
- [Source: `flexicontent.fields.php`](https://github.com/FLEXIcontent/flexicontent-cck/blob/master/site/classes/flexicontent.fields.php)
