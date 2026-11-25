---
sidebar_position: 13
---

# Core property

Item Form CORE property placer Plugin for FLEXIcontent. This field is used to define the place that the CORE property will appear in Item Form. This is done by ordering it in fields manager, while Content Type filter is enabled

*Plugin : `coreprops` — CORE property*

:::info Source
This page is generated from `plugins/flexicontent_fields/coreprops/coreprops.xml` and the official FLEXIcontent 5.x language files.
:::

## Property type

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Property type**<br />`props_type` | Select the CORE property or CORE property group (normally these will appear in a TAB by default), that you want to place in item form | `multilist` | **Basic or Single properties**<br />`id` = ID<br />`alias` = Alias<br />`category` = Category (main)<br />`lang` = Language<br />`vstate` = Publish changes<br />`disable_comments` = Disable comments<br />`notify_subscribers` = Notify subscibers<br />`notify_owner` = Notify owner<br />`captcha` = Captcha<br />`layout_selection` = Layout selection<br />**Publishing properties**<br />`timezone_info` = Timezone info<br />`created_by_alias` = Created by alias<br />`publish_up` = Publish up (date)<br />`publish_down` = Publish down (date)<br />`access` = View access<br />**Property groups**<br />`item_screen` = Version information<br />`lang_assocs` = Language associations<br />`jimages` = JImages<br />`jurls` = JUrls<br />`metadata` = META data<br />`seoconf` = SEO configuration<br />`display_params` = Displaying parameters<br />`layout_params` = Layout parameters<br />`perms` = Permissions<br />`versions` = Versions<br />**Deprecated (legacy)**<br />`language` = Language and associations | — |

## Editing

#### Frontend Item Form only Custom place this selected CORE property via field manager ordering

#### For placing: title, state, created, createdby, modified, modified, please use the existing CORE fields

## Viewing

#### Viewing

### Basic

#### Display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

#### Label and access

#### NOTE: - Fields that can be displayed are: language, alias, main category, access, - for displaying 'publish_up', 'publish_down' please use date field in appropriate mode

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

#### Category (main)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add links**<br />`link_maincat` | Link every value to its item listing view | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Backend View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Backend view appearance**<br />`backend_view_appearance` | How this field's value is displayed in the admin items list. Overrides the global 'Custom columns appearance' setting when not set to Default. | `multilist` | `0` = Default<br />`1` = Check mark<br />`2` = Clean up HTML and trim | `0` (Default) |
| **Trim length (characters)**<br />`backend_view_trim_chars` | Number of characters to keep after stripping HTML tags. | `text` | — | `100` |

### Value list

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Preset configurations**<br />`prx_sfx_open_close_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |
| **Value separator (frontend views)**<br />`separatorf` | Choose a separator to separate the values in frontend views (placed between values) | `multilist` | `0` = Space<br />`1` = Line break<br />`6` = Horizontal line<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters)<br />`7` = Custom separator | `1` (Line break) |
| **Custom separator**<br />`separatorf_custom` | — | `text` | — | — |
| **Opening text for Field**<br />`opentag` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

#### Viewing

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

#### Filtering

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
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

:::note
Note, some core properties only support specific displays, e.g only the text input
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
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

:::note
Note, some core properties only support specific displays, e.g only the text input
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
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
