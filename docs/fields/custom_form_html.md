---
sidebar_position: 14
---

# Custom HTML / form tab

Form Field Group Marker Field Plugin for FLEXIcontent. This field is used to mark the start/end of FLEXIcontent field groups in ITEM edit FORM. Group will appear inside Tabs/Fieldsets/etc. Take care to match all openings with a closing marker appropriately.

*Plugin : `custom_form_html` — Custom HTML / Item Form Tab / Fieldset*

:::info Source
This page is generated from `plugins/flexicontent_fields/custom_form_html/custom_form_html.xml` and the official FLEXIcontent 5.x language files.
:::

## Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use field in a group**<br />`use_ingroup` | Enable to allow field to be part of field group, that is created via 'Field Group' field. NOTE: You should then select this field in ONLY ONE field group | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `multilist` | `0` = No | `0` (No) |
| **Marker type**<br />`marker_type` | BE CAREFULL to match-close all open type of markers with an appropriate closing type. BE CAREFULL to which content types you assign the field to. | `multilist` | **Tabs**<br />`tabset_start` = Tab-set: START<br />`tab_open` = Tab: open<br />`tab_close` = Tab: close<br />`tabset_end` = Tab-set: END<br />**Fieldsets**<br />`fieldset_open` = Field-set: open<br />`fieldset_close` = Field-set: close<br />**Other**<br />`custom_html` = Custom HTML | `custom_html` (Custom HTML) |
| **Container CSS class**<br />`cont_cssclass` | CSS class of tab / fieldset / etc inner container, only appropriate for -start/open- markers | `text` | — | — |

#### Tab: open / Field-set: open

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Tab/Fieldset Label**<br />`cont_label` | Label of tab / fieldset / etc, only appropriate for -open- markers | `text` | — | — |

#### Custom HTML

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Custom HTML**<br />`custom_html_sep` | Enter the custom HTML code that will be placed between the fields | `editor` | — | — |
