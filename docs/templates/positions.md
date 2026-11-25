---
title: Field positions and drag and drop
sidebar_position: 4
---

# Field positions and drag and drop

FLEXIcontent templates expose **field positions**. In the administrator template editor, core and custom fields can be dragged into these positions. The saved order is then rendered by the template.

:::info Source
Based on FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`): `admin/views/template/tmpl/default.php`, `admin/views/template/view.html.php`, `admin/assets/js/layout_editor.js`, `admin/controllers/templates.php`, `admin/models/template.php`, `site/classes/helpers/tmpl.php` and `site/classes/flexicontent.fields.php`.
:::

:::caution Field positions are not Joomla module positions
This mechanism assigns FLEXIcontent **fields** to template slots. Joomla module positions are a separate concept. See [Module positions](#module-positions) below.
:::

## 1. Declare a position in XML

Open `item.xml`, `category.xml` or both and add a `<group>` inside `<fieldgroups>`.

```xml
<fieldgroups>
    <group>myposition</group>
    <group title="My Position" tcolor="darkcyan">another_position</group>
    <group posrow="image" tcolor="#3A2459" title="Image">image</group>
    <group tcolor="gray" readonly="true">subcategory_title</group>
    <group tcolor="darkgray" title="Render only, no display">renderonly</group>
</fieldgroups>
```

| Attribute | Effect |
| --- | --- |
| (text content) | Machine name of the position. Use it in the PHP loop. |
| `title` | Human-readable label in the template editor. |
| `tcolor` | Background color in the editor. |
| `posrow` | Groups positions into a row/column in the editor. |
| `readonly` | Shows an informational message and disables drag and drop for the position. |

The editor asks you to place the new position inside `<fieldgroups>` and to remember its name for `item.php` or `category_items.php`. Use a simple name: no spaces and no accented characters.

`renderonly` is a convention, not a special rendering mode. Fields assigned to it are rendered into `$item->fields` but are not displayed automatically. See [Render-only fields](#render-only-fields).

## 2. Add the matching PHP loop

For `item.php`:

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

For `category_items.php`, the same loop goes inside the item loop:

```php
<?php foreach ($this->items as $item) : ?>
    <?php if (isset($item->positions['myposition'])) : ?>
        <?php foreach ($item->positions['myposition'] as $field) : ?>
            <div class="flexi value field_<?php echo $field->name; ?>">
                <?php echo $field->display; ?>
            </div>
        <?php endforeach; ?>
    <?php endif; ?>
<?php endforeach; ?>
```

The XML name and `$_position_name` must match exactly. See [Item loops and field rendering](./loops-fields.md) for the full loop and the shape of `$item->positions`.

## 3. Assign fields in the template editor

In the administrator, open the template configuration and the **Field's placement** tab. The editor builds three kinds of sortable lists:

```text
#sortablecorefields      available core fields
#sortableuserfields      available custom fields
#sortable-myposition     fields currently assigned to "myposition"
```

Each field is a list item with an id such as `field_myfield`. Custom fields are displayed with their id, for example `City #47`.

The editor stores the order in hidden inputs: one per position and a global `positions` CSV list. The JavaScript in `admin/assets/js/layout_editor.js` uses Sortable:

```js
Sortable.create(list, {
    group: 'flexicontent-layout-fields',
    draggable: 'li[id^="field_"]',
    onEnd(event) {
        storeOrder(event.from);
        if (event.to !== event.from) storeOrder(event.to);
    }
});
```

`storeOrder()` writes the field names as a comma-separated value, for example `image,introtext,city`.

## 4. Save the template

The controller reads the `positions` input and calls the model:

```php
$positions = $this->input->getString('positions', '');
$positions = explode(',', $positions);
$model->setConfig($positions, $attribs);
$model->store($post);
```

The model then stores field positions, layout parameters, generated LESS variables and refreshes the template cache:

```php
$this->storeFieldPositions($this->_folder, $this->_cfgname, $this->_type, $this->_config['positions'], $data);
$this->storeLayoutConf($this->_folder, $this->_cfgname, $this->_type, $this->_config['attribs']);
$this->check_less_files($this->_folder);
$this->storeLessConf($this->_folder, $this->_cfgname, $this->_type, $this->_config['attribs']);
flexicontent_tmpl::getTemplates($this->_folder, false);
```

:::warning
After editing XML or PHP directly on the server, save the template again in the administrator. Otherwise the position assignments for the new `<group>` are not stored, and the cached template definition may remain unchanged. Clear the Joomla cache if needed.
:::

## How positions are stored

Positions are saved per template, layout configuration (`cfgname`) and view in `#__flexicontent_templates`:

```sql
CREATE TABLE IF NOT EXISTS `#__flexicontent_templates` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `template` varchar(50) NOT NULL default '',
  `cfgname` varchar(50) NOT NULL default '',
  `layout` varchar(20) NOT NULL default '',
  `position` varchar(100) NOT NULL default '',
  `fields` text NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `configuration` (`template`,`cfgname`,`layout`,`position`)
);
```

The `fields` column contains the comma-separated field names. On the frontend, `flexicontent_tmpl::getFieldsByPositions()` loads the rows for the active template and layout, mapping the view name `item` to the internal layout key `items`.

At render time, `FlexicontentFields::renderPositions()` fills each position:

```php
$item->positions['position_name']->{$field_name}->id;
$item->positions['position_name']->{$field_name}->name;
$item->positions['position_name']->{$field_name}->label;
$item->positions['position_name']->{$field_name}->display;
```

Fields with an empty display output are skipped.

## Render-only fields

Use `renderonly` when a field must be output manually, for example twice in one template or inside another HTML structure:

```xml
<fieldgroups>
    <group tcolor="darkgray" title="Render only, no display">renderonly</group>
</fieldgroups>
```

```php
<?php echo $item->fields["fieldname"]->display; ?>
```

The template editor attaches this note to the snippet:

> You need to add this field to the renderonly position, in the "Field's placement" TAB

Some field plugins generate HTML IDs. Displaying the same field several times can therefore produce invalid duplicate IDs.

## Module positions

Joomla module positions are managed by Joomla, not by `item.xml` or `category.xml`. The `fcloadmodule` field exposes a dropdown of published site module positions through `type="fcpositions"`:

```xml
<field
    name="position"
    type="fcpositions"
    default=""
    label="FLEXI_FIELD_MODULE_POSITIONS_LIST"
    description="FLEXI_FIELD_MODULE_POSITIONS_LIST_DESC"
/>
```

That form element queries `#__modules` for distinct published positions with `client_id = 0`. There is no drag-and-drop definition for Joomla modules in a FLEXIcontent template manifest.

## Position checklist

1. Copy a bundled template before editing it.
2. Add the `<group>` to `item.xml`, `category.xml` or both.
3. Add the PHP position loop with the identical name.
4. Save the template to update `#__flexicontent_templates`.
5. Drag core/custom fields into the position in the template editor.
6. Save again after changing assignment order.
7. Check the frontend with the relevant `ilayout` or `clayout`.
8. For manual output, assign the field to `renderonly` and echo `$item->fields['name']->display`.

## Official references

- [Adding a position in item view](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/661-adding-position-in-item-view.html)
- [Creating an extra field position in a custom template](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/255-creating-an-extra-field-position-in-a-custom-template.html)
- [Displaying a field in multiple places](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/635-how-to-display-a-field-in-multiple-places.html)
- [Editing template parameters](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/305-editing-template-parameters-to-customize-template-appearance.html)
- [Source: template editor](https://github.com/FLEXIcontent/flexicontent-cck/blob/master/admin/views/template/tmpl/default.php)
