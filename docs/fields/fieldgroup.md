---
sidebar_position: 19
---

# Field group (repeatable)

Fieldgroup Field Plugin for FLEXIcontent

*Plugin : `fieldgroup` — Fieldgroup*

:::info Source
This page is generated from `plugins/flexicontent_fields/fieldgroup/fieldgroup.xml` and the official FLEXIcontent 5.x language files.
:::

## Editing

#### Editing

### Values

#### Field grouping

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Fields**<br />`fields` | Select fields that will be show shown as a group | `fields` | — | — |

#### Number of values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Allow multiple values**<br />`allow_multiple` | Allow more than 1 value for this field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **max # values**<br />`max_values` | The max number of values you wish to record | `text` | — | `0` |
| **Values per row**<br />`fields_box_placing` | Save space by allowing multiple values to show per row | `radio` | `0` = 1<br />`1` = Multiple | `0` (1) |
| **Add position**<br />`add_position` | Select to add value inline (show add button at every value) or append them to the bottom of the value list | `multilist` | `0` = Append to bottom<br />`1` = Inline append<br />`2` = Inline prepend<br />`3` = Inline both | `3` (Inline both) |

#### Fields not assigned to content type - or - fields without any form HTML

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display**<br />`form_empty_fields` | Hide / show fields that are not assigned to content type of current item form, and also fields without any form HTML | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Custom text**<br />`form_empty_fields_text` | Customize the text shown for empty / non-assigned fields | `text` | — | `FLEXI_NA` (N/A) |

### Form Display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `multilist` | `0` = No<br />`1` = Floated left<br />`2` = Cleared<br />`-1` = As placeholder | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Fields layout**<br />`formlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/field_*.php as field_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fclayout` | `list` = Default (Vertical placement)<br />`flexbox` = Flexbox (Horizontal placement with auto-wrap) | `list` (Default (Vertical placement)) |

#### Compact editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **All values toggling**<br />`compact_edit_global` | Enable this to show an all values toggler button | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Values toggling**<br />`compact_edit` | Enable this to compact the display of every fieldgroup value, and save space | `multilist` | `0` = No<br />`1` = Yes, start collapsed<br />`2` = Yes, start expanded | `0` (No) |
| **Fields always visible**<br />`compact_edit_excluded` | You should select some fields to be always visible thus these will serve as a 'title' or 'referance' for easily finding a value, example if field group is a 'contanct' then 'Firstname' and 'Lastname' should always be visible | `fields` | — | — |

### Layout parameters

#### Editing

## Viewing

#### Viewing

### Basic

#### Display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

#### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Export

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `multilist` | `0` = No<br />`1` = Raw values<br />`2` = Rendered values | `0` (No) |
| **Strip HTML tags**<br />`csv_strip_html` | — | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Backend View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Backend view appearance**<br />`backend_view_appearance` | How this field's value is displayed in the admin items list. Overrides the global 'Custom columns appearance' setting when not set to Default. | `multilist` | `0` = Default<br />`1` = Check mark<br />`2` = Clean up HTML and trim | `0` (Default) |
| **Trim length (characters)**<br />`backend_view_trim_chars` | Number of characters to keep after stripping HTML tags. | `text` | — | `100` |

### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Use customized HTML**<br />`display_mode` | Select to display default or custom HTML specified below - default HTML inlcudes all fields of the group and their labels | `multilist` | `0` = Layout<br />`1` = Custom HTML | `0` (Layout) |
| **Custom HTML**<br />`custom_html` | Leave blank for default, which include all fields with their labels, - or you can use custom HTML which supports: **NOTE:** you can use: **&#123;&#123;fieldname&#125;&#125;** or **&#123;&#123;fieldname##displayvar&#125;&#125;** -- is replaced with HTML display of each field **&#123;&#123;fieldname##label&#125;&#125;** -- is replaced with label of each field **%%language_string%%** -- is replaced with the language string **&#123;&#123;value##count&#125;&#125;** -- is replaced with (integer) position of current value Finally, you can use item properties like: &#123;item-&gt;id&#125;, &#123;item-&gt;title&#125;, etc | `editor` | — | — |

#### Fields WITHOUT value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Skip field (Label/empty html code)**<br />`hide_lbl_ifnoval` | Select fields to hide labels if they have no value. NOTE: if using 'default HTML', then this will also skip fields that produced no HTML code | `filters` | — | — |

### Value list

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Preset configurations**<br />`prx_sfx_open_close_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking) | — |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |
| **Value separator (frontend views)**<br />`separatorf` | Choose a separator to separate the values in frontend views (placed between values) | `multilist` | `0` = Space<br />`1` = Line break<br />`6` = Horizontal line<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters)<br />`7` = Custom separator | `1` (Line break) |
| **Custom separator**<br />`separatorf_custom` | — | `text` | — | — |
| **Opening text for Field**<br />`opentag` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

### Content plugins

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Viewing

## SEO

### Microdata support

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Microdata type**<br />`fieldgroup_itemtype` | Select a microdata type to that will characterize all items of the type. MICRODATA allow search engines to categorize your content appropriately, improving SEO of your pages | `microdatatype` | — | — |
