---
sidebar_position: 39
---

# Web link

Weblink Field Plugin for FLEXIcontent

*Plugin : `weblink` — Weblink*

:::info Source
This page is generated from `plugins/flexicontent_fields/weblink/weblink.xml` and the official FLEXIcontent 5.x language files.
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
| **Values per row**<br />`fields_box_placing` | Save space by allowing multiple values to show per row | `radio` | `0` = 1<br />`1` = Multiple | `1` (Multiple) |
| **Add position**<br />`add_position` | Select to add value inline (show add button at every value) or append them to the bottom of the value list | `multilist` | `0` = Append to bottom<br />`1` = Inline append<br />`2` = Inline prepend<br />`3` = Inline both | `3` (Inline both) |

#### Values Creation

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Links source**<br />`link_source` | (Joomla article manager compatibility) - Select if this field will edit and display the Joomla article links | `multilist` | `-1` = Joomla article links<br />`0` = Weblink Field Plugin for FLEXIcontent | `0` (Weblink Field Plugin for FLEXIcontent) |
| **Default Link**<br />`default_link` | You can select to display some text inside the link (not recommended) | `text` | — | — |
| **Default Link USAGE**<br />`link_usage` | Select when you want the default link to be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |
| **Allow relative addresses**<br />`allow_relative_addrs` | Allow users to enter relative addresses. When this is disabled addresses not having a protocol prefix will be automatically prefixed with HTTP:// | `multilist` | `0` = No<br />`1` = Yes<br />`2` = User can select | `0` (No) |

#### Automatic value creation

:::note
Flexicontent PRO version only
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Automatic value**<br />`auto_value` | Enable to create the value of this field automatically on item form save. In some cases, you might want to enable option of hiding this field in frontend or backend or both item forms | `multilist` | `0` = No<br />`2` = Use custom code | `0` (No) |
| **Custom code**<br />`auto_value_code` | Enter PHP code to be used create the custom value, please set to empty and save to load the default example, and then customize | `editor` | — | `fields; if ( !isset($F['fieldname01']) ) return array('fieldname01 field not found'); $vals = array(); foreach($F['fieldname01']-&gt;postdata as $i =&gt; $v) &#123; $vals[$i] = 'Auto : ' . $v; &#125; return $vals;` |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Fields layout**<br />`formlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/field_*.php as field_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Expand button**<br />`show_values_expand_btn` | Display a button to expand width of properties to allow easier editing. NOTE: some layout like 'table' may not support this button, button will not be shown | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Simple form design**<br />`simple_form_layout` | (For non-table layouts) This will show labels above the form fields. In the case of empty input fields the labels also become a placeholder that transitions to its place only after focus or after typing. Also borders are removed | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Link

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Maximum Text Length**<br />`maxlength` | Maximum number of characters allowed during user input | `text` | — | `4000` |
| **Field size**<br />`size` | Field size in the HTML form | `text` | — | `30` |
| **Field attributes**<br />`extra_attributes` | Here you can enter some extra attributes (HTML Tag Parameters) for the form field like e.g. onkeypress="..." onmouseover="..." somename="somevalue". Take care not to break the the HTML syntax of the form field | `text` | — | — |
| **Input value Masking & Validation**<br />`inputmask` | Parameters for both masking and validating user input | `multilist` | `—` = No<br />`url` = Yes | — |

### Optional Properties

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_image` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes, any<br />`2` = Yes, specific | `0` (No) |
| **Default**<br />`default_image` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `media` | — | — |
| **Usage of default**<br />`image_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |
| **Specific images**<br />`image_choices` | — | `subform` | — | — |

#### Mouse-over title

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_title` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default**<br />`default_title` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`title_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

#### Linking Text

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_text` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default**<br />`default_text` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`text_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

#### Address type

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_addrtype` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`2` = Yes | `0` (No) |
| **Select Choices**<br />`addrtype_choices` | Enter drop down select choices, the syntax is the following: value1::label1%% value2::label2%% | `textarea` | — | — |

#### Styling (CSS) Class

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_class` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes, as Text Input<br />`2` = Yes, as Select | `0` (No) |
| **Default**<br />`default_class` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`class_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |
| **Select Choices**<br />`class_choices` | Enter drop down select choices, the syntax is the following: value1::label1%% value2::label2%% | `textarea` | — | — |

#### HTML Tag id

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_id` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default**<br />`default_id` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`id_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

#### Target window

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_target` | If you enable this, then user will be able to override default property value when editing the field in item form | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Hits

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_hits` | If you enable this, then user will be able to override default property value when editing the field in item form | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

### Import

#### Manipulate values during import

:::note
Flexicontent PRO version only
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remap Values**<br />`import_fv_remap_mode` | Enable to change some imported values to some other values. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Value Remappings**<br />`import_fv_remap` | Enter like importValue1::realValue1%% importValue2::realValue2%% importValue3::realValue3%% | `textarea` | — | — |
| **Values manipulation**<br />`import_fv_ccode_mode` | Execute custom methods to manipulate field values | `multilist` | `0` = No<br />`2` = Use custom code | `0` (No) |
| **Custom code**<br />`import_fv_ccode` | Enter PHP code to be used create the custom value, please set to empty and save to load the default example, and then customize | `editor` | — | `parameters-&gt;get('some_param'); foreach($values as $i =&gt; $v) &#123; $values[$i] = 'Example ' . $i . ' : ' . $v; &#125; return $values;` |

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

:::note
&#123;&#123;title&#125;&#125; &#123;&#123;link&#125;&#125;
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Customize**<br />`csv_export_text` | — | `textarea` | — | `&#123;&#123;title&#125;&#125; &#123;&#123;link&#125;&#125;` |

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
| **Show no value message**<br />`show_no_value` | Display a message that field has no value instead of empty display | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No value message**<br />`no_value_msg` | The text to display when field has no value, leave empty to show default text | `text` | — | — |

:::note
Note: new window will be forced for external links
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default Link Target**<br />`target` | Select default target window of link that do not have a target already (via item form) | `list` | `—` = - No target -<br />`_blank` = New Window/Tab<br />`_parent` = Parent Frame<br />`_self` = Same Frame/Window/Tab<br />`_top` = Top of window<br />`_popup` = FLEXI_FIELD_LINK_JS_POPUP_BOX<br />`_modal` = FLEXI_FIELD_LINK_SINGLE_WIN | — |
| **Use direct link**<br />`use_direct_link` | Add direct links to the URLs, note that this will disable hits counting. Normally an indirect link to your site web server is output in order to get the real URL and also count hits. | `radio` | `0` = No<br />`1` = Yes, (disable hits counting) | `0` (No) |
| **Add rel-nofollow**<br />`add_rel_nofollow` | Adds rel=nofollow to the links, this indicates to the search engines not to index the link | `radio` | `0` = Yes, prevent indexing external links<br />`1` = Yes, prevent indexing<br />`-1` = No, allow indexing any link (!!!) | `0` (Yes, prevent indexing external links) |
| **Display hits**<br />`display_hits` | Shows the number of hits or downloads for each value of the field | `radio` | `0` = No<br />`1` = Icon<br />`2` = Text<br />`3` = Both | `0` (No) |

:::note
Image
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`display_image` | Display image if one has beeng associated with the URL | `multilist` | `0` = No<br />`1` = Yes<br />`2` = Yes, hide linking text | `1` (Yes) |
| **Image width**<br />`image_w` | — | `text` | — | `320` |
| **Image height**<br />`image_h` | — | `text` | — | `240` |

:::note
Video URLs
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Behaviour**<br />`playback_videos` | Playback video URLs instead of opening the URL | `radio` | `0` = Link<br />`1` = Playback | `1` (Playback) |

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

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Form field

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `1` = Text Search | `0` |
