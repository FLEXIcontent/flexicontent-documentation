---
sidebar_position: 23
---

# Links list

Links List Field Plugin for FLEXIcontent

*Plugin : `linkslist` — HTML list of URLs/Anchors/JS links*

:::info Source
This page is generated from `plugins/flexicontent_fields/linkslist/linkslist.xml` and the official FLEXIcontent 5.x language files.
:::

## Editing

#### Editing

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use field in a group**<br />`use_ingroup` | Enable to allow field to be part of field group, that is created via 'Field Group' field. NOTE: You should then select this field in ONLY ONE field group | `multilist` | `0` = No | `0` (No) |

#### Number of values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Values Creation

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default values**<br />`default_values` | Choose default values or leave blank for none. TAKE CARE, values must be chosen from the field elements VALUES you defined above. You must provide a COMMA separated list. | `text` | — | — |
| **Preset configurations**<br />`extra_votes_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = Load example | — |
| **List Elements**<br />`field_elements` | The elements of an unordered () or an ordered () list. The syntax is the following: Title1[id="tagid1" class="cssclass1" ... link="#link1"] :​: Title2[id="tagid2" class="cssclass2" ... link="#link2"] :​: Title3[id="tagid3" class="cssclass3" ... link="#link3"] **NOTE 1:** - use :​: as list elements separator, - use [option=value] to specify the options of each list element. **NOTE 2:** - 'title' is the text inside the HTML tag, - 'title' will be a link (placed inside an HTML tag) ONLY if the 'link' option is specified. - all 'options' like: id,class,... (excluding 'link'), will become HTML tag parameters of the HTML tag. **NOTE 3:** all options (including the 'link' option) are optional, thus you can write: TitleNN[] without specifying any options | `textarea` | — | — |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display as**<br />`editform_field_type` | You may use alternative displays e.g. to save space making form more compact | `radio` | `1` = Checkboxes (multi)<br />`2` = Tag-like selector (multi) | `1` (Checkboxes (multi)) |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_form` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_form` | This text is placed immediately **after** every field value | `text` | — | — |
| **Value separator (item form)**<br />`separator` | Choose a separator to separate the values in backend/frontend item forms (placed between values) | `list` | `0` = Space<br />`1` = Line break<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters) | `0` (Space) |
| **Opening text for Field**<br />`opentag_form` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag_form` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

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

#### Value display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display non-selected without link**<br />`add_non_selected` | Normally non-selected values are not included in the created list. Enable this option to show them without adding a link tag, instead as SPAN tag will be added | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### HTML TAG parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **List type**<br />`list_type` | Set the list type, usually 'ul' | `list` | `ul` = Unordered list<br />`ol` = Ordered list | `ul` (Unordered list) |
| **List class**<br />`list_class` | Add a class to the list, leave empty if you don't need it. | `text` | — | — |
| **List ID**<br />`list_id` | Add an ID to the list, leave empty if you don't need it. | `text` | — | — |

#### Custom JS/CSS

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Javascript code**<br />`js_code` | Optional javascript code to add to the frontend view when this field is displayed, thus you can attach JS to the links inserted by this field and create clickable actions that will manipulate your page according to your needs. **NOTE** the JS code is added even if this field inserts ZERO links. Thus your JS code must attach e.g. with an appropriate jQuery selector which selector may or may not be found. **NOTE**: this will be added only once, in both item view, and in multi-item views when this field is displayed. Alternatively, this could also be added permanently to any JS file of yours | `textarea` | — | — |
| **CSS rules**<br />`css_code` | Optional CSS rules to add to the frontend view when this field is displayed. **NOTE**: these will be added only once, in both item view, and in multi-item views when this field is displayed. Alternatively, these could also be added permanently to any CSS file of yours | `textarea` | — | — |

### Content plugins

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Viewing
