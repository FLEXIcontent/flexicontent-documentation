---
sidebar_position: 34
---

# Term list

FLEXI_FIELD_TERMLIST

*Plugin : `termlist` — TermList*

:::info Source
This page is generated from `plugins/flexicontent_fields/termlist/termlist.xml` and the official FLEXIcontent 5.x language files.
:::

## Editing

#### Editing

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use field in a group**<br />`use_ingroup` | Enable to allow field to be part of field group, that is created via 'Field Group' field. NOTE: You should then select this field in ONLY ONE field group | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |

#### Number of values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Allow multiple values**<br />`allow_multiple` | Allow more than 1 value for this field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **max # values**<br />`max_values` | The max number of values you wish to record | `text` | — | `0` |
| **Values per row**<br />`fields_box_placing` | Save space by allowing multiple values to show per row | `radio` | `0` = 1<br />`1` = Multiple | `0` (1) |
| **Add position**<br />`add_position` | Select to add value inline (show add button at every value) or append them to the bottom of the value list | `multilist` | `0` = Append to bottom<br />`1` = Inline append<br />`2` = Inline prepend<br />`3` = Inline both | `3` (Inline both) |

#### Values Creation

#### Term title

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default**<br />`default_value_title` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`title_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

#### Term decription

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default**<br />`default_value` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`default_value_use` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |
| **Server-Side validation**<br />`validation` | Allow input to be safe HTML tags, OR plain text, OR use Joomla's Text Filters (set per usergroup in Joomla global configuration), etc ..., never allow UNSAFE HTML for public forms, but if you do you should enable '**encode on display**' parameter | `groupedlist` | **Per user**<br />`2` = Joomla's Text Filters (per usergroup)<br />**HTML / Text**<br />`1` = SAFE HTML : remove dangerous tags/attributes<br />`RAW` = UNSAFE HTML (raw HTML) : ... MAYBE: encode on display<br />`STRING` = TEXT : decode HTML entities, strip HTML tags<br />`HTML` = TEXT or ENCODED HTML: allow entities, strip tags | `2` (Joomla's Text Filters (per usergroup)) |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

### Term title

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`title_label` | Label, this is language filtered | `text` | — | `FLEXI_FIELD_TERMTITLE` (Term title) |
| **Maximum Text Length**<br />`title_maxlength` | Maximum number of characters allowed during user input | `text` | — | `0` |
| **Field size**<br />`title_size` | Field size in the HTML form | `text` | — | `80` |

### Term description

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`value_label` | Label, this is language filtered | `text` | — | `FLEXI_FIELD_TERMTEXT` (Term description) |
| **Editor**<br />`use_html` | Use an HTML (WYSIWYG) editor or display a simple textarea | `multilist` | `1` = HTML Editor<br />`0` = Simple Textarea | `0` (Simple Textarea) |

#### Simple Textarea

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Maximum Text Length**<br />`maxlength` | Maximum number of characters allowed during user input | `text` | — | — |
| **Rows**<br />`rows` | Number of rows | `text` | — | `3` |
| **Columns**<br />`cols` | Number of columns | `text` | — | `80` |

#### HTML Editor

:::note
NOTE: about multi-value support
Only editors based on: tinyMCE** (built-in or 3rd party) and **CodeMirror** are supported, otherwise the HTML editor on new values will appear only after saving
:::

:::note
NOTE: prefer to use Joomla default editor setting (3rd party or built-in)
Adding 2 different editors on same page may break XTD editor buttons like read-more
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **HTML Editor**<br />`editor` | You can use an HTML Editor to edit the field | `plugins` | `—` = Joomla's default | — |
| **Editor width**<br />`width` | HTML editor width | `text` | — | `98%` |
| **Editor height**<br />`height` | HTML editor height | `text` | — | `250px` |

#### Extra (editor) buttons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`show_buttons` | You can disable all editor buttons that offer extra functionality (usually displayed at footer) | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Skip buttons (some editors *)**<br />`skip_buttons` | Select to disable individual buttons. NOTE: not all editors support this, e.g. supported for tinyMCE and possibly by other editors | `pluginlist` | — | — |

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

#### Value display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Language filter values**<br />`lang_filter_values` | Apply language filter JText::_() on the values, the values must be language strings, either added in a language file, or added by Joomla language overrides manager | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Encode values (XSS safe, visible HTML/JS)**<br />`encode_output` | Encode any HTML/JS inside the values this makes any HTML/JS code to become visible, thus values become XSS safe (cross site scripting). NOTE: enable this, - if you suspect that XSS unsafe values may have been added to the field by older field configurations, - or if you are want to display HTML code that is not already encoded as HTML entities | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Clean values (e.g. strip HTML / JS)**<br />`clean_output` | You can take an extra step to clean any unsafe or undesired HTML inside the values, NOTE: enable this, - if you suspect that XSS unsafe HTML, or undesired HTML formating may have been added to the field by older field configurations | `radio` | `0` = No<br />`1` = Unsafe HTML<br />`2` = ALL HTML | `0` (No) |

#### Category views

:::note
Term description
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Strip HTML, cut text**<br />`cut_text_catview` | Strip HTML tags from the text and also cut it to a maximum length | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Character limit**<br />`cut_text_length_catview` | Any characters over the limit (starting at next word) will be cut off | `text` | — | `200` |
| **Toggle all text**<br />`cut_text_display_catview` | Enable this to allow showing all text | `multilist` | `0` = No<br />`1` = Inline<br />`2` = Modal window | `0` (No) |
| **Button icon**<br />`cut_text_display_btn_icon_catview` | — | `text` | — | `icon-paragraph-center` |
| **Button text**<br />`cut_text_display_btn_text_catview` | — | `text` | — | — |

### Value list

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Preset configurations**<br />`prx_sfx_open_close_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking) | — |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

:::note
NOTE: opening / closing texts and value separator, are not used inside a fieldgroup
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
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
| **Microdata property**<br />`microdata_itemprop` | Select a microdata property to characterize all values of this field. This will allow search engines to categorize values of this field appropriately, improving SEO of your pages | `microdataprops` | — | — |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Form field

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `1` = Text Search | `0` |
