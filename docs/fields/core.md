---
sidebar_position: 12
---

# Core fields (Joomla)

Core Fields Plugin for FLEXIcontent

*Plugin : `core` — Core Fields*

:::info Source
This page is generated from `plugins/flexicontent_fields/core/core.xml` and the official FLEXIcontent 5.x language files.
:::

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/core/tmpl/FIELD_TYPE/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/core/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## Social

### Social websites support (e.g. Facebook)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Suggest field to listings**<br />`useogp` | Select to suggest (force) text to appear in social website image listings as description | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Max Text Length**<br />`ogpmaxlen` | Enter the maximum number of characters to use after stripping HTML | `text` | — | `300` |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Form field

#### Category-based views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `list` | `1` = Text Search | `0` |

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `1` = Text Search | `0` |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/core/tmpl/FIELD_TYPE/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/core/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Date format**<br />`date_format` | If you choose 'custom format' in the dropdown above you have to specify in this field the format you wish to render using the PHP date (not strftime) syntax (http://php.net/manual/en/function.date.php). | `multilist` | `DATE_FORMAT_LC1` = DATE_FORMAT_LC1<br />`DATE_FORMAT_LC2` = DATE_FORMAT_LC2<br />`DATE_FORMAT_LC3` = DATE_FORMAT_LC3<br />`DATE_FORMAT_LC4` = DATE_FORMAT_LC4<br />`—` = Custom format | — |
| **Custom format**<br />`custom_date` | If you choose 'custom format' in the dropdown above you have to specify in this field the format you wish to render using the PHP strftime syntax (http://php.net/strftime). | `text` | — | — |
| **Language filter format**<br />`lang_filter_format` | Apply language filter JText::_() on the format string which must be a language string, either added in a language file, or added by Joomla language overrides manager. **WARNING**: You need to disable language filtering if not adding language string! otherwise some characters will be stripped out like comma | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## SEO

### Microdata support

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Microdata property**<br />`microdata_itemprop` | Select a microdata property to characterize all values of this field. This will allow search engines to categorize values of this field appropriately, improving SEO of your pages | `radio` | `0` = Disabled<br />`dateCreated` = dateCreated | `dateCreated` (dateCreated) |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Filter value order**<br />`reverse_filter_order` | Enable to display filter values in reverse ordering. NOTE that in the case of slider range display, the left handle will be the maximum, and the right handle will be the minimum | `radio` | `0` = Normal<br />`1` = Reverse | `0` (Normal) |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Disable keyboard input**<br />`disable_keyboardinput` | Enable this option if you want to disable keyboard input. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Prefix / Suffix

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_filter` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_filter` | This text is placed immediately **after** every field value | `text` | — | — |
| **Opening text for Field**<br />`opentag_filter` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag_filter` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

#### Category-based views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Filter Grouping for non-text display types**<br />`date_filter_group` | Select the grouping of dates into years or months or days. This is applicable when filter is displayed as drop-down select field (single or range) or as radio/toggle buttons | `radio` | `year` = Year<br />`month` = Month<br />`day` = Day | `month` (Month) |
| **Display date custom format**<br />`date_filter_label_format` | e.g. '%Y-%M' will display '2025-August' see docs of SQL function DATE_FORMAT, common: %d Day of the month, numeric (00..31), %b Abbreviated month name (Jan..Dec), %M Month name (January..December), %m Month numeric (00..12), %Y Year numeric, four digits, %y Year numeric (two digits) | `text` | — | — |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `multilist` | `0` = Drop-down selector<br />`1` = Date picker<br />`7` = Slider<br />`2` = Drop-down selector (range)<br />`3` = Date picker (range)<br />`8` = Slider (range)<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
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
| **Custom values**<br />`slider_custom_range` | Custom range of values, please use values that exist in the field !, for format, see example format, enter comma separated values: percentage%: 'value', and instead of 0% or 100%, you must use 'min': 'value' and 'max':'min': 'value' | `textarea` | — | `'min': '', '25%': '2000', '50%': '2005', '75%': '2020', 'max': ''` |
| **Custom labels**<br />`slider_custom_labels` | Custom labels to match the values, please enter a ## separated labels without start/end quotes | `textarea` | — | `label_any ## label_2000 ## label_2005 ## label_2020 ## label_any` |
| **Labels are language strings**<br />`slider_custom_labels_jtext` | Set this to yes to treat labels as language strings, remember to add these to your Joomla language overrides manager or in other loaded language files | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Filter Grouping for non-text display types**<br />`date_filter_group_s` | Select the grouping of dates into years or months or days. This is applicable when filter is displayed as drop-down select field (single or range) or as radio/toggle buttons | `radio` | `year` = Year<br />`month` = Month<br />`day` = Day | `month` (Month) |
| **Display date custom format**<br />`date_filter_label_format_s` | e.g. '%Y-%M' will display '2025-August' see docs of SQL function DATE_FORMAT, common: %d Day of the month, numeric (00..31), %b Abbreviated month name (Jan..Dec), %M Month name (January..December), %m Month numeric (00..12), %Y Year numeric, four digits, %y Year numeric (two digits) | `text` | — | — |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `multilist` | `0` = Drop-down selector<br />`1` = Date picker<br />`7` = Slider<br />`2` = Drop-down selector (range)<br />`3` = Date picker (range)<br />`8` = Slider (range)<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
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
| **Custom values**<br />`slider_custom_range_s` | Custom range of values, please use values that exist in the field !, for format, see example format, enter comma separated values: percentage%: 'value', and instead of 0% or 100%, you must use 'min': 'value' and 'max':'min': 'value' | `textarea` | — | `'min': '', '25%': 2000, '50%': 2005, '75%': 2020, 'max': ''` |
| **Custom labels**<br />`slider_custom_labels_s` | Custom labels to match the values, please enter a ## separated labels without start/end quotes | `textarea` | — | `label_any ## label_2000 ## label_2005 ## label_2020 ## label_any` |
| **Labels are language strings**<br />`slider_custom_labels_jtext_s` | Set this to yes to treat labels as language strings, remember to add these to your Joomla language overrides manager or in other loaded language files | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/core/tmpl/FIELD_TYPE/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/core/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Display**<br />`name_username` | Choose if you wish to display name or username | `radio` | `1` = Name<br />`2` = Username | `1` (Name) |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Form field

#### Category-based views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`1` = Text Search<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`1` = Text Search<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter_s` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items_s` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values_s` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/core/tmpl/FIELD_TYPE/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/core/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Date format**<br />`date_format` | If you choose 'custom format' in the dropdown above you have to specify in this field the format you wish to render using the PHP date (not strftime) syntax (http://php.net/manual/en/function.date.php). | `multilist` | `DATE_FORMAT_LC1` = DATE_FORMAT_LC1<br />`DATE_FORMAT_LC2` = DATE_FORMAT_LC2<br />`DATE_FORMAT_LC3` = DATE_FORMAT_LC3<br />`DATE_FORMAT_LC4` = DATE_FORMAT_LC4<br />`—` = Custom format | — |
| **Custom format**<br />`custom_date` | If you choose 'custom format' in the dropdown above you have to specify in this field the format you wish to render using the PHP strftime syntax (http://php.net/strftime). | `text` | — | — |
| **Language filter format**<br />`lang_filter_format` | Apply language filter JText::_() on the format string which must be a language string, either added in a language file, or added by Joomla language overrides manager. **WARNING**: You need to disable language filtering if not adding language string! otherwise some characters will be stripped out like comma | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## SEO

### Microdata support

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Microdata property**<br />`microdata_itemprop` | Select a microdata property to characterize all values of this field. This will allow search engines to categorize values of this field appropriately, improving SEO of your pages | `radio` | `0` = Disabled<br />`dateModified` = dateModified | `dateModified` (dateModified) |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Filter value order**<br />`reverse_filter_order` | Enable to display filter values in reverse ordering. NOTE that in the case of slider range display, the left handle will be the maximum, and the right handle will be the minimum | `radio` | `0` = Normal<br />`1` = Reverse | `0` (Normal) |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Disable keyboard input**<br />`disable_keyboardinput` | Enable this option if you want to disable keyboard input. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Prefix / Suffix

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_filter` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_filter` | This text is placed immediately **after** every field value | `text` | — | — |
| **Opening text for Field**<br />`opentag_filter` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag_filter` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

#### Category-based views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Filter Grouping for non-text display types**<br />`date_filter_group` | Select the grouping of dates into years or months or days. This is applicable when filter is displayed as drop-down select field (single or range) or as radio/toggle buttons | `radio` | `year` = Year<br />`month` = Month<br />`day` = Day | `month` (Month) |
| **Display date custom format**<br />`date_filter_label_format` | e.g. '%Y-%M' will display '2025-August' see docs of SQL function DATE_FORMAT, common: %d Day of the month, numeric (00..31), %b Abbreviated month name (Jan..Dec), %M Month name (January..December), %m Month numeric (00..12), %Y Year numeric, four digits, %y Year numeric (two digits) | `text` | — | — |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `multilist` | `0` = Drop-down selector<br />`1` = Date picker<br />`7` = Slider<br />`2` = Drop-down selector (range)<br />`3` = Date picker (range)<br />`8` = Slider (range)<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
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
| **Custom values**<br />`slider_custom_range` | Custom range of values, please use values that exist in the field !, for format, see example format, enter comma separated values: percentage%: 'value', and instead of 0% or 100%, you must use 'min': 'value' and 'max':'min': 'value' | `textarea` | — | `'min': '', '25%': '2000', '50%': '2005', '75%': '2020', 'max': ''` |
| **Custom labels**<br />`slider_custom_labels` | Custom labels to match the values, please enter a ## separated labels without start/end quotes | `textarea` | — | `label_any ## label_2000 ## label_2005 ## label_2020 ## label_any` |
| **Labels are language strings**<br />`slider_custom_labels_jtext` | Set this to yes to treat labels as language strings, remember to add these to your Joomla language overrides manager or in other loaded language files | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Filter Grouping for non-text display types**<br />`date_filter_group_s` | Select the grouping of dates into years or months or days. This is applicable when filter is displayed as drop-down select field (single or range) or as radio/toggle buttons | `radio` | `year` = Year<br />`month` = Month<br />`day` = Day | `month` (Month) |
| **Display date custom format**<br />`date_filter_label_format_s` | e.g. '%Y-%M' will display '2025-August' see docs of SQL function DATE_FORMAT, common: %d Day of the month, numeric (00..31), %b Abbreviated month name (Jan..Dec), %M Month name (January..December), %m Month numeric (00..12), %Y Year numeric, four digits, %y Year numeric (two digits) | `text` | — | — |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `multilist` | `0` = Drop-down selector<br />`1` = Date picker<br />`7` = Slider<br />`2` = Drop-down selector (range)<br />`3` = Date picker (range)<br />`8` = Slider (range)<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
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
| **Custom values**<br />`slider_custom_range_s` | Custom range of values, please use values that exist in the field !, for format, see example format, enter comma separated values: percentage%: 'value', and instead of 0% or 100%, you must use 'min': 'value' and 'max':'min': 'value' | `textarea` | — | `'min': '', '25%': 2000, '50%': 2005, '75%': 2020, 'max': ''` |
| **Custom labels**<br />`slider_custom_labels_s` | Custom labels to match the values, please enter a ## separated labels without start/end quotes | `textarea` | — | `label_any ## label_2000 ## label_2005 ## label_2020 ## label_any` |
| **Labels are language strings**<br />`slider_custom_labels_jtext_s` | Set this to yes to treat labels as language strings, remember to add these to your Joomla language overrides manager or in other loaded language files | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/core/tmpl/FIELD_TYPE/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/core/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Display**<br />`name_username` | Choose if you wish to display name or username | `radio` | `1` = Name<br />`2` = Username | `1` (Name) |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Form field

#### Category-based views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`1` = Text Search<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`1` = Text Search<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter_s` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items_s` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values_s` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Icons**<br />`show_icons` | Print, Email, PDF, etc. will utilize Icons or Text | `multilist` | `0` = Text<br />`1` = Icon<br />`2` = Both | `1` (Icon) |
| **Icon type**<br />`use_font_icons` | You may display icons as images or as using an installed font-based icon set | `radio` | `0` = Image<br />`1` = Font icons | `1` (Font icons) |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Form field

#### Category-based views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Form field

#### Category-based views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`1` = Text Search<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`1` = Text Search<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter_s` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items_s` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values_s` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## Viewing

#### Viewing

### Basic

#### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

#### Stars appearance

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Stars size**<br />`stars_size` | Size of a single star in pixels | `number` | — | `24` |
| **Star tooltips**<br />`stars_tooltips` | Display the rating text (e.g. "Good 4/5") above a star while the mouse is over it, the tooltip is hidden when the vote is made | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Stars color**<br />`stars_color` | Color of the filled (rated) stars | `fccolor` | — | `#FFB400` |
| **Empty stars color**<br />`stars_color_empty` | Color of the empty (unrated) stars | `fccolor` | — | `#CCCCCC` |

#### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Export

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Raw values | `0` (No) |

#### Backend View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Backend view appearance**<br />`backend_view_appearance` | How this field's value is displayed in the admin items list. Overrides the global 'Custom columns appearance' setting when not set to Default. | `multilist` | `0` = Default<br />`1` = Check mark<br />`2` = Clean up HTML and trim | `0` (Default) |
| **Trim length (characters)**<br />`backend_view_trim_chars` | Number of characters to keep after stripping HTML tags. | `text` | — | `100` |

### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/core/tmpl/FIELD_TYPE/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/core/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |

#### Voting

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable in views**<br />`vote_submit_inview` | You can turn on/off the above parameter depending on current flexicontent view | `fccheckbox` | — | — |

### Value list

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

### Content plugins

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Viewing

## Permission

You can configure who is allowed to submit votes, message for non-authorized users, etc

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Submit Access**<br />`submit_acclvl` | User Group assigned this access level will be able to vote. - e.g **create an access level 'Content Voting'** and assign it to the Usergroups that you need **NOTE:** You only need to assign it to the parent UserGroup e.g. if you assign this Access Level to usergroup 'Registered' then ALL usergroups being children of it will have it ... | `accesslevel` | — | `1` |

### No Access Handling

#### Logged Users

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Message**<br />`logged_no_acc_msg` | The Tooltip message (language string) that will be displayed to users that cannot vote, e.g. you can ask your users to register or buy subscription, etc **NOTE:** Leave blank to display a default message that states the name of the required Access Level | `text` | — | — |
| **Do Redirection**<br />`logged_no_acc_doredirect` | Select whether to redirect authorized users | `radio` | `0` = No<br />`1` = Redirect URL | `0` (No) |
| **User confirms redirection**<br />`logged_no_acc_askredirect` | User will be asked if he wants to be redirected | `radio` | `0` = No<br />`1` = No, inform only<br />`2` = Yes, ask user | `1` (No, inform only) |
| **Redirect URL**<br />`logged_no_acc_url` | The URL to load when user clicks on the voting field while not being authorized to vote | `text` | — | — |

#### Guest Users

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Message**<br />`guest_no_acc_msg` | The Tooltip message (language string) that will be displayed to users that cannot vote, e.g. you can ask your users to register or buy subscription, etc **NOTE:** Leave blank to display a default message that states the name of the required Access Level | `text` | — | — |
| **Do Redirection**<br />`guest_no_acc_doredirect` | Select whether to redirect authorized users | `radio` | `0` = No<br />`1` = Redirect URL<br />`2` = Login/Register | `2` (Login/Register) |
| **User confirms redirection**<br />`guest_no_acc_askredirect` | User will be asked if he wants to be redirected | `radio` | `0` = No<br />`1` = No, inform only<br />`2` = Yes, ask user | `1` (No, inform only) |
| **Redirect URL**<br />`guest_no_acc_url` | The URL to load when user clicks on the voting field while not being authorized to vote | `text` | — | — |

## Grade / Score

:::note
You may want to display the field in item form to treat it as **'Grade' / 'Score' field**. In such a case you should give to this field (inside Viewing Tab) a voting access level that is assigned (granted) only to a special usergroup that is meant to do the 'grading' / 'scoring'
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item form**<br />`vote_iform_display` | — | `radio` | `0` = Hide<br />`1` = Show<br />`2` = Readonly | `0` (Hide) |

## Reviews

Enable and configure reviewing of items

:::note
This is an unfinished ALPHA-state feature, it is meant to be enabled only by testers
:::

#### reviews_conf

### Authoring, Workflow

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`allow_reviews` | Enable reviews for items displaying this voting field | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### New reviews

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow submissions**<br />`allow_submit_review_by` | Who is allowed to submit new reviews from the frontend | `radio` | `0` = Disabled<br />`1` = Anyone (guests and logged users)<br />`2` = Logged users only<br />`3` = Use access level | `0` (Disabled) |
| **Submit access level**<br />`review_submit_access` | Used only when submissions are set to -Use access level-. Users having this access level can submit reviews | `accesslevel` | — | `1` |

#### Publishing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Publish after approval**<br />`do_approval` | Require an administrator to read and approve new and modified reviews, before they are displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Guests

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Verify email ownership**<br />`verify_email_ownership` | For every new review by a guest, an email will be sent to the guest user email to verify email ownership (not implemented yet) | `radio` | `0` = No<br />`1` = Yes (not implemented yet) | `1` (Yes (not implemented yet)) |

### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Reviews list placement**<br />`reviews_placement` | Inline: the list is displayed by the item template, Modal window: the list is opened in a popup from the N Reviews button | `multilist` | `0` = Inline<br />`1` = Modal window | `0` (Inline) |

:::note
**Inline mode:** the stars and the reviews button are displayed where this field is placed, but the reviews list is displayed by the item template, add this code where the list should appear (e.g. at the end of the item.php of the template): fields['voting']-&gt;display_reviews; ?&gt; The default FLEXIcontent templates already include it, the field must be in a field position or in the renderonly position of the template.
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Reviews loaded at a time**<br />`reviews_page_size` | Number of reviews displayed first, further reviews are loaded by scrolling inside the modal window (1 - 50, default 5) | `text` | — | `5` |
| **Useful votes of reviews**<br />`reviews_useful` | Display under each review the number of people that found it useful, and the 'Was this helpful?' question with Yes / No buttons. The users can not vote for their own review | `radio` | `0` = Disabled<br />`1` = Logged users<br />`2` = Anyone (guests by IP) | `1` (Logged users) |
| **Reviews counter in lists**<br />`reviews_counter_in_lists` | Display the number of reviews, next to the stars, in the lists of items (category, module views), the lists display only the stars and this counter | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Loading indicator**<br />`reviews_loader` | Display a loader (spinner) while the next reviews are loaded by scrolling in the modal window, and the end of the list ("That's all") after the last review | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Live update of the page**<br />`reviews_live_update` | Yes: after a review is saved, deleted or moderated, the rating, counters and reviews of the page are updated without reloading the page. No: the page is reloaded when the review window is closed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Save ratings without a review**<br />`reviews_store_rating` | **No**: voting with the stars does not create a review record, votes are protected from double voting by the session / IP address (as the voting field without reviews). The rating of a review is still a vote of the item. **Yes**: a logged user voting with the stars gets a review record without text (it is not displayed in the site), this allows a single vote per user account, that can be changed from any browser. These records are listed in the reviews manager as "rating only". | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Maximum length of a review**<br />`reviews_max_length` | Maximum number of characters of the review text, a counter is shown in the review form (default 500, 0 = no limit) | `text` | — | `500` |

#### reviews_conf

## Advanced

#### Advanced

### Unrated

### Default rating and low-voting weights

#### Default rating % during ordering, (0 votes)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Rating %**<br />`default_rating` | Rating percentage of items without a vote, used for ordering | `integer` | — | `50` |

#### Rating weights % during ordering, (1 to 9 votes), set lower % to push them down the item list

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Rating weight %**<br />`vote_1_weight` | - Enter 100 to consider them fully, - Enter lower % to push them away from the beginning | `integer` | — | `100` |
| **Rating weight %**<br />`vote_2_weight` | - Enter 100 to consider them fully, - Enter lower % to push them away from the beginning | `integer` | — | `100` |
| **Rating weight %**<br />`vote_3_weight` | - Enter 100 to consider them fully, - Enter lower % to push them away from the beginning | `integer` | — | `100` |
| **Rating weight %**<br />`vote_4_weight` | - Enter 100 to consider them fully, - Enter lower % to push them away from the beginning | `integer` | — | `100` |
| **Rating weight %**<br />`vote_5_weight` | - Enter 100 to consider them fully, - Enter lower % to push them away from the beginning | `integer` | — | `100` |
| **Rating weight %**<br />`vote_6_weight` | - Enter 100 to consider them fully, - Enter lower % to push them away from the beginning | `integer` | — | `100` |
| **Rating weight %**<br />`vote_7_weight` | - Enter 100 to consider them fully, - Enter lower % to push them away from the beginning | `integer` | — | `100` |
| **Rating weight %**<br />`vote_8_weight` | - Enter 100 to consider them fully, - Enter lower % to push them away from the beginning | `integer` | — | `100` |
| **Rating weight %**<br />`vote_9_weight` | - Enter 100 to consider them fully, - Enter lower % to push them away from the beginning | `integer` | — | `100` |

### Resolution and custom display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Rating Resolution for new sites OR ***<br />`rating_resolution` | This is to be used while building new sites or ... read below. Joomla's built-in Resolution is 5 **NOTE:** Changing this in existing sites will make rating average to appear wrongly !! **NOTE:** (for developers) It is possible to update rating table with an SQL query like: **UPDATE nnn_content_rating SET rating_sum = rating_sum * (_new_resolution_ / _old_resolution_)** and same for TABLE nnn_flexicontent_items_extravote, BACKUP these 2 tables before doing the SQL query **NOTE:** This will cause non-FLEXIcontent extensions to display vote ratings WRONGLY, so do not change this if you use non-FLEXIcontent extensions to display ratings _5_ | `text` | — | — |
| **Rating Stars resolution &gt;= stars**<br />`rating_stars` | The number of displayed stars, Joomla's built-in is also 5. **NOTE:** Must be: resolution &gt;= stars **EXAMPLES:** -- 10 stars with half star voting, set Resolution: 20, Stars 10 -- 5 stars with quarter star voting, set Resolution: 20, Stars: 5 -- 10 stars with one star voting, set Resolution: 10, Stars: 10 _5_ | `text` | — | — |

### Average rating

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show rating label**<br />`main_label_show` | Show the rating label (e.g. 'Average rating') above the stars, in the item view and in the lists. The label text can be changed in the next option | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Label**<br />`main_label` | The label of average rating | `text` | — | `FLEXI_VOTE_AVERAGE_RATING` (Average rating) |
| **Rating scale texts**<br />`rating_texts` | Textual representation of rating scale. Enter a comma seperated list of language strings. eg JVERYPOOR, JPOOR, JFAIR, JGOOD, JEXCELLENT _Very poor, Poor, Fair, Good, Excellent_ | `textarea` | — | — |
| **Show vote counter**<br />`main_counter` | Display total number of votes | `radio` | `0` = Disable<br />`1` = Enable | `1` (Enable) |
| **Show counter label**<br />`main_counter_show_label` | This will add a 'votes' label after the voting counter | `radio` | `0` = Disable<br />`1` = Enable | `1` (Enable) |
| **Show percentage**<br />`main_counter_show_percentage` | This will display the percentage rating next to each rating label | `radio` | `0` = Disable<br />`1` = Enable | `0` (Disable) |

### Composite voting

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`enable_extra_votes` | Turn on/off the display of partial voting characteristics, like quality, performance, accuracy, etc | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Enable in views**<br />`composite_inview` | You can turn on/off the above parameter depending on current flexicontent view | `fccheckbox` | — | — |
| **Preset configurations**<br />`extra_votes_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = Load example | — |
| **Voting characteristics**<br />`extra_votes` | Here you can define the voting characteristics like e.g. Quality, Speed, Accuracy, etc ... **Write like**: 1##Quality##Description%% 2##Speed##Description%% 3##Accuracy##Description%% 4##Appearance##Description%% ... **NOTE 1**: The names will be passed through JText ... to allow multilanguage support (You can add them to your language files) | `textarea` | — | — |
| **Show characteristics with the rating**<br />`extra_show_in_display` | Show the rating characteristics (with their stars) under the overall rating of the field. If No, only the overall rating is shown (read-only) and the characteristics are rated in the review form and shown in the reviews | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

### Voting characteristic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show vote counter**<br />`extra_counter` | Display total number of votes | `radio` | `0` = Disable<br />`1` = Enable | `1` (Enable) |
| **Show counter label**<br />`extra_counter_show_label` | This will add a 'votes' label after the voting counter | `radio` | `0` = Disable<br />`1` = Enable | `1` (Enable) |
| **Show percentage**<br />`extra_counter_show_percentage` | This will display the percentage rating next to each rating label | `radio` | `0` = Disable<br />`1` = Enable | `0` (Disable) |

#### Advanced

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/core/tmpl/FIELD_TYPE/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/core/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Toggle Style**<br />`toggle_style` | — | `multilist` | `0` = BootStrap Toggle<br />`1` = Image Icons<br />`2` = CSS Icons | `0` (BootStrap Toggle) |

#### Access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow guests**<br />`allow_guests_favs` | Enable to allow favourites usage to guests | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Info

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Status info**<br />`status_info` | Whether to show extra text about current subscription status | `multilist` | `0` = Icon<br />`1` = Icon + Text | `0` (Icon) |
| **Toggle info**<br />`toggle_info` | Whether to display a short time displayed text when user toggles subscription status | `multilist` | `0` = Hide<br />`1` = Show | `0` (Hide) |
| **Users counter**<br />`display_favoured_usercount` | Display a counter of total users favouring the item | `radio` | `0` = Hide<br />`1` = Show | `0` (Hide) |
| **Users list**<br />`display_favoured_userlist` | Display list of the users favouring the item, either listing their usernames or their fullnames | `multilist` | `0` = Hide<br />`1` = Yes, Usernames<br />`2` = Yes, Fullnames | `0` (Hide) |
| **Maximum users in list**<br />`display_favoured_max` | Limits the listing of users to a reasonable maximum ... | `text` | — | `12` |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Raw values<br />`2` = Rendered values | `0` (No) |

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/core/tmpl/FIELD_TYPE/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/core/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Links

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add links**<br />`link_to_view` | Link every value to its item listing view | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |
| **Value separator (frontend views)**<br />`separatorf` | Choose a separator to separate the values in frontend views (placed between values) | `list` | `0` = Space<br />`1` = Line break<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters) | `3` (Comma) |
| **Opening text for Field**<br />`opentag` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Form field

#### Category-based views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Root category for filtering**<br />`rootcatid` | Root category for filtering from frontend. This setting effect with Filterable is 'Yes' from your left side. | `flexicategories` | — | — |
| **Sub-tree depth**<br />`filter_depth` | Maximum depth of sub-category tree | `text` | — | `1` |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable) | `2` |

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Root category for filtering**<br />`rootcatid_s` | Root category for filtering from frontend. This setting effect with Filterable is 'Yes' from your left side. | `flexicategories` | — | — |
| **Sub-tree depth**<br />`filter_depth_s` | Maximum depth of sub-category tree | `text` | — | `1` |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter_s` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable) | `2` |

## Viewing

### Display

:::note
This has an effect if displaying this field by adding it to a **fields position** of your **item / category** layouts
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Raw values<br />`2` = Rendered values | `0` (No) |

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/core/tmpl/FIELD_TYPE/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/core/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Links

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add links**<br />`link_to_view` | Link every value to its item listing view | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |
| **Value separator (frontend views)**<br />`separatorf` | Choose a separator to separate the values in frontend views (placed between values) | `list` | `0` = Space<br />`1` = Line break<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters) | `3` (Comma) |
| **Opening text for Field**<br />`opentag` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Values

:::note
... if field is multi-valued (item form) ... and has a multi-valued filter appearance
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Require ALL selected values**<br />`filter_values_require_all` | Usually you will include items found to have any of the selected values. -- You can select to **require all selected** filter values to be matched for the found items. -- **WARNING** to developers of new field types: this will not work properly if your field saves SAME field value more than once for the same item. So in such a case do not add this option to your field ! | `radio` | `0` = No<br />`1` = Yes, slower | `0` (No) |
| **Require ANY / ALL inline tip**<br />`filter_values_require_all_tip` | Select to show information if ANY or ALL selected filter values of this filter are required | `radio` | `0` = Hide<br />`1` = Show | `0` (Hide) |

### Form field

#### Category-based views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`1` = Text Search<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `0` = Drop-down selector<br />`1` = Text Search<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter_s` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items_s` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values_s` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

## Editing

### Value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Server-Side validation**<br />`validation` | Allow input to be safe HTML tags, OR plain text, OR use Joomla's Text Filters (set per usergroup in Joomla global configuration), etc ..., never allow UNSAFE HTML for public forms, but if you do you should enable '**encode on display**' parameter | `list` | `2` = Joomla's Text Filters (per usergroup)<br />`1` = SAFE HTML : remove dangerous tags/attributes<br />`RAW` = UNSAFE HTML (raw HTML) : ... MAYBE: encode on display<br />`STRING` = TEXT : decode HTML entities, strip HTML tags<br />`HTML` = TEXT or ENCODED HTML: allow entities, strip tags | `2` (Joomla's Text Filters (per usergroup)) |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **Editor**<br />`hide_html` | Use an HTML (WYSIWYG) editor or display a simple textarea | `multilist` | `0` = HTML Editor<br />`1` = Simple Textarea | `0` (HTML Editor) |

#### Simple Textarea

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Maximum Text Length**<br />`maxlength` | Maximum number of characters allowed during user input | `text` | — | — |
| **Rows**<br />`rows` | Number of rows | `text` | — | `6` |
| **Columns**<br />`cols` | Number of columns | `text` | — | `80` |

#### HTML Editor

:::note
Note some of these settings also exist in type configuration form !
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Editor width**<br />`width` | HTML editor width | `text` | — | — |
| **Editor height**<br />`height` | HTML editor height | `text` | — | — |
| **HTML Editor**<br />`editor` | You can use an HTML Editor to edit the field | `plugins` | `—` = Joomla's default | — |

#### Extra (editor) buttons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`show_buttons` | You can disable all editor buttons that offer extra functionality (usually displayed at footer) | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Skip buttons (some editors *)**<br />`skip_buttons` | Select to disable individual buttons. NOTE: not all editors support this, e.g. supported for tinyMCE and possibly by other editors | `pluginlist` | — | — |

## Viewing

### Display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `multilist` | `0` = No<br />`1` = Raw values<br />`2` = Rendered values | `0` (No) |
| **Strip HTML tags**<br />`csv_strip_html` | — | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Value

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Category views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Strip HTML, cut text**<br />`cut_text_catview` | Strip HTML tags from the text and also cut it to a maximum length | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Character limit**<br />`cut_text_length_catview` | Any characters over the limit (starting at next word) will be cut off | `text` | — | `200` |
| **Toggle all text**<br />`cut_text_display_catview` | Enable this to allow showing all text | `multilist` | `0` = No<br />`1` = Inline<br />`2` = Modal window | `0` (No) |
| **Button icon**<br />`cut_text_display_btn_icon_catview` | — | `text` | — | `icon-paragraph-center` |
| **Button text**<br />`cut_text_display_btn_text_catview` | — | `text` | — | — |

## Social

### Social websites support (e.g. Facebook)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Suggest field to listings**<br />`useogp` | Select to suggest (force) text to appear in social website image listings as description | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Max Text Length**<br />`ogpmaxlen` | Enter the maximum number of characters to use after stripping HTML | `text` | — | `300` |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Form field

#### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `1` = Text Search | `0` |

## Tabs (RegEx)

Split textarea into TABs via regular expression

### Parse joomla tabs plugin code

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`editorarea_per_tab` | Enable to try to identify TABs via regex patterns | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |

#### Regular expression patterns

#### Tabset patterns

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Tab-set start**<br />`start_of_tabs_pattern` | Regular expression to much plugin code | `text` | — | — |
| **Tab-set end**<br />`end_of_tabs_pattern` | Regular expression to much plugin code | `text` | — | — |

#### Tab patterns

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Tab start**<br />`start_of_tab_pattern` | Regular expression to much plugin code | `text` | — | — |
| **Tab end**<br />`end_of_tab_pattern` | Regular expression to much plugin code | `text` | — | — |

:::note
Inside tab start text
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Tab title**<br />`title_tab_pattern` | Title should be inside TAB start code, this is regular expression to much inside title text inside it | `text` | — | — |

#### Extra editor areas

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Before tabset**<br />`force_beforetabs` | Add extra editor area | `multilist` | `0` = Automatic<br />`1` = Always | `1` (Always) |
| **After tabset**<br />`force_aftertabs` | Add extra editor area | `multilist` | `0` = Automatic<br />`1` = Always | `1` (Always) |
| **Tab code editable**<br />`allow_tabs_code_editing` | This will allow editting of TAB-set TAB code inside the item from | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
