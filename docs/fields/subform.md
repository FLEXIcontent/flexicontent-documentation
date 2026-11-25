---
sidebar_position: 33
---

# Subform

Subform field Plugin for FLEXIcontent

:::info Source
This page is generated from `plugins/flexicontent_fields/subform/subform.xml` and the official FLEXIcontent 5.x language files.
:::

## Editing

#### Editing

### Values

#### Number of values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Allow multiple values**<br />`allow_multiple` | Allow more than 1 value for this field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **min # options**<br />`min_values` | The min number of options that must be selected in each value of the field | `text` | — | `0` |
| **max # options**<br />`max_values` | The max number of options that can be selected in each value of the field | `text` | — | `0` |

#### Values Creation

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default**<br />`default_value` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`default_value_use` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

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

#### Input field

:::note
e.g. layout="joomla.form.field.subform.repeatable" buttons="add,remove,move"
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Field attributes**<br />`extra_attributes` | Here you can enter some extra attributes (HTML Tag Parameters) for the form field like e.g. onkeypress="..." onmouseover="..." somename="somevalue". Take care not to break the the HTML syntax of the form field | `text` | — | — |
| **Subform form XML**<br />`subform_form_xml` | Enter PHP code to be used create the custom value, please set to empty and save to load the default example, and then customize | `editor` | — | `File Link` |

#### Prefix / Suffix

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_form` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_form` | This text is placed immediately **after** every field value | `text` | — | — |

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
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Raw values<br />`2` = Rendered values | `0` (No) |

#### Backend View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Backend view appearance**<br />`backend_view_appearance` | How this field's value is displayed in the admin items list. Overrides the global 'Custom columns appearance' setting when not set to Default. | `multilist` | `0` = Default<br />`1` = Check mark<br />`2` = Clean up HTML and trim | `0` (Default) |
| **Trim length (characters)**<br />`backend_view_trim_chars` | Number of characters to keep after stripping HTML tags. | `text` | — | `100` |

### Layout

:::note
This field is meant to be used by developers - Default display only dumps the data for previewing - You need to duplicate default layout, and then customize it, so that it displays the actual data of this field in a desirable way. See description of layout parameter below.
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |

### Value list

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Preset configurations**<br />`prx_sfx_open_close_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
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

#### Filtering

### Values

#### Filter values creation

:::note
Take care to create proper SQL query or elements -- NOTE: 'value' part of elements/query must match existing field values
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Custom Retrieval of Filter Values**<br />`filter_customize_options` | Select to use all text field values for filter, or define a custom sql query to use some of them and maybe modify display selection of the (text property in query) | `multilist` | `0` = No, use all values (default)<br />`1` = Use custom query<br />`2` = Use custom elements | `0` (No, use all values (default)) |
| **Custom Elements or SQL Query**<br />`filter_custom_options` | Custom elements or SQL query. For **custom elements**, the syntax is the following: value1::label1%% value2::label2%% For **SQL query**, enter: SELECT value, value as text FROM #__flexicontent_fields_item_relations WHERE field_id='&#123;field_id&#125;' AND value != '' GROUP BY value **You can put replacements**: for current field data: &#123;field-&gt;id&#125; &#123;field-&gt;field_type&#125; **NOTE**: The names will be passed through JText ... to allow multilanguage support (You can add them to your language files) _SELECT value, value as text FROM #__flexicontent_fields_item_relations WHERE field_id='&#123;field-&gt;id&#125;' AND value != '' GROUP BY value_ | `textarea` | — | — |
| **Filter value order**<br />`reverse_filter_order` | Enable to display filter values in reverse ordering. NOTE that in the case of slider range display, the left handle will be the maximum, and the right handle will be the minimum | `radio` | `0` = Normal<br />`1` = Reverse | `0` (Normal) |

#### Filter value comparison

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Filter value comparison**<br />`filter_compare_type` | Filter values can be compare as alphanumeric or as numeric (integer/float) | `radio` | `0` = Alphanumeric<br />`1` = Integer<br />`2` = Float | `0` (Alphanumeric) |

:::note
... if field is multi-valued (item form) ... and has a multi-valued filter appearance
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Require ALL selected values**<br />`filter_values_require_all` | Usually you will include items found to have any of the selected values. -- You can select to **require all selected** filter values to be matched for the found items. -- **WARNING** to developers of new field types: this will not work properly if your field saves SAME field value more than once for the same item. So in such a case do not add this option to your field ! | `radio` | `0` = No<br />`1` = Yes, slower | `0` (No) |
| **Require ANY / ALL inline tip**<br />`filter_values_require_all_tip` | Select to show information if ANY or ALL selected filter values of this filter are required | `radio` | `0` = Hide<br />`1` = Show | `0` (Hide) |

### Category-based views

#### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `multilist` | `0` = Drop-down selector<br />`1` = Text Search<br />`7` = Slider<br />`2` = Drop-down selector (range)<br />`3` = Text Search (range)<br />`8` = Slider (range)<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

#### Drop-down selector

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Customize default option (all values)**<br />`filter_usefirstoption` | Enable to customize the first option of the filter (=all values) . NOTE: this is used only in the case of Drop-Down Select, and also if field label is not placed inside the selector | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default Option Text (e.g. All colours)**<br />`filter_firstoptiontext` | Text of first option of the Drop-Down Select e.g. 'All colours' or FLEXI_ALL etc. **NOTE**: This option has no value **NOTE**: This text is language-filtered so you can enter a language replaceable string | `text` | — | `FLEXI_ALL` (All) |

#### Slider

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Slider data**<br />`slider_display_config` | Either use found field values, or specify your custom range of values | `multilist` | `1` = Found values<br />`2` = Custom values | `1` (Found values) |
| **Custom values**<br />`slider_custom_range` | Custom range of values, please use values that exist in the field !, for format, see example format, enter comma separated values: percentage%: 'value', and instead of 0% or 100%, you must use 'min': 'value' and 'max':'min': 'value' | `textarea` | — | `'min': '', '25%': '50', '50%': '150', '75%': '600', 'max': ''` |
| **Custom labels**<br />`slider_custom_labels` | Custom labels to match the values, please enter a ## separated labels without start/end quotes | `textarea` | — | `label_any ## label_50 ## label_150 ## label_600 ## label_any` |
| **Labels are language strings**<br />`slider_custom_labels_jtext` | Set this to yes to treat labels as language strings, remember to add these to your Joomla language overrides manager or in other loaded language files | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Prefix / Suffix

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_filter` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_filter` | This text is placed immediately **after** every field value | `text` | — | — |
| **Opening text for Field**<br />`opentag_filter` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag_filter` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

### Advanced Search View

#### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `multilist` | `0` = Drop-down selector<br />`1` = Text Search<br />`7` = Slider<br />`2` = Drop-down selector (range)<br />`3` = Text Search (range)<br />`8` = Slider (range)<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter_s` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items_s` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values_s` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

#### Drop-down selector

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Customize default option (all values)**<br />`filter_usefirstoption_s` | Enable to customize the first option of the filter (=all values) . NOTE: this is used only in the case of Drop-Down Select, and also if field label is not placed inside the selector | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default Option Text (e.g. All colours)**<br />`filter_firstoptiontext_s` | Text of first option of the Drop-Down Select e.g. 'All colours' or FLEXI_ALL etc. **NOTE**: This option has no value **NOTE**: This text is language-filtered so you can enter a language replaceable string | `text` | — | `FLEXI_ALL` (All) |

#### Slider

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Slider data**<br />`slider_display_config_s` | Either use found field values, or specify your custom range of values | `multilist` | `1` = Found values<br />`2` = Custom values | `1` (Found values) |
| **Custom values**<br />`slider_custom_range_s` | Custom range of values, please use values that exist in the field !, for format, see example format, enter comma separated values: percentage%: 'value', and instead of 0% or 100%, you must use 'min': 'value' and 'max':'min': 'value' | `textarea` | — | `'min': '', '25%': 500, '50%': 2000, '75%': 10000, 'max': ''` |
| **Custom labels**<br />`slider_custom_labels_s` | Custom labels to match the values, please enter a ## separated labels without start/end quotes | `textarea` | — | `label_any ## label_500 ## label_2000 ## label_10000 ## label_any` |
| **Labels are language strings**<br />`slider_custom_labels_jtext_s` | Set this to yes to treat labels as language strings, remember to add these to your Joomla language overrides manager or in other loaded language files | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Prefix / Suffix

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_filter_s` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_filter_s` | This text is placed immediately **after** every field value | `text` | — | — |
| **Opening text for Field**<br />`opentag_filter_s` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag_filter_s` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

#### Filtering
