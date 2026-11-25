---
sidebar_position: 25
---

# International phone numbers

This field adds phone numbers to items. For each number you can add a label (e.g. Office, Fax, Toll Free, etc), country code, area code, and phone number. The field configuration allows for very flexible displaying to accomodate to different styles and needs. The HTML code is very detailed for easy styling with CSS classes.

*Plugin : `phonenumbers` — International Phone Numbers*

:::info Source
This page is generated from `plugins/flexicontent_fields/phonenumbers/phonenumbers.xml` and the official FLEXIcontent 5.x language files.
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
| **Allow multiple values**<br />`allow_multiple` | Allow more than 1 value for this field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Values per row**<br />`fields_box_placing` | Save space by allowing multiple values to show per row | `radio` | `0` = 1<br />`1` = Multiple | `0` (1) |
| **Add position**<br />`add_position` | Select to add value inline (show add button at every value) or append them to the bottom of the value list | `multilist` | `0` = Append to bottom<br />`1` = Inline append<br />`2` = Inline prepend<br />`3` = Inline both | `3` (Inline both) |
| **max # values**<br />`max_values` | The max number of values you wish to record | `text` | — | `0` |
| **Form card width**<br />`form_card_width` | Width in pixels of the phone card in the item form | `text` | — | `320` |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Values Creation

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Phone Label**<br />`use_label` | — | `radio` | `0` = No<br />`1` = Yes | `3` |
| **Country Code**<br />`use_cc` | — | `multilist` | `0` = No<br />`1` = Yes | — |
| **Default country**<br />`ac_country_default` | Choosz a default country for phone number prefix | `fccountriesphones` | — | — |
| **Allowed country**<br />`ac_country_allowed_list` | Add allowed country, nothing add all | `fccountriesphones` | — | — |
| **Phone Number**<br />`use_phone` | — | `radio` | `1` = 1 part<br />`2` = area code + local number<br />`3` = area code + part 2 + part 3 | `3` (area code + part 2 + part 3) |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Phone Label

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Maximum Text Length**<br />`label_maxlength` | Maximum number of characters allowed during user input | `text` | — | `48` |
| **Field size**<br />`label_size` | Field size in the HTML form | `text` | — | `48` |

#### Country Code

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Maximum Text Length**<br />`cc_maxlength` | Maximum number of characters allowed during user input | `text` | — | `6` |
| **Field size**<br />`cc_size` | Field size in the HTML form | `text` | — | `6` |

#### Phone Number

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Part labels**<br />`show_part_labels` | — | `radio` | `0` = Hide<br />`1` = Show | `0` (Hide) |

#### Part 1 (area code)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Maximum Text Length**<br />`phone1_maxlength` | Maximum number of characters allowed during user input | `text` | — | `12` |
| **Field size**<br />`phone1_size` | Field size in the HTML form | `text` | — | `12` |

#### Part 2

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Maximum Text Length**<br />`phone2_maxlength` | Maximum number of characters allowed during user input | `text` | — | `12` |
| **Field size**<br />`phone2_size` | Field size in the HTML form | `text` | — | `12` |

#### Part 3

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Maximum Text Length**<br />`phone3_maxlength` | Maximum number of characters allowed during user input | `text` | — | `12` |
| **Field size**<br />`phone3_size` | Field size in the HTML form | `text` | — | `12` |

#### Allow Letters in Phone Number

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow letters**<br />`allow_letters` | Enable to allow letters (A to Z, uppercase only) in the phone number field. When disabled only numbers are allowed. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

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
| **Display Phone Label**<br />`display_phone_label` | Show the phone label when rendering the field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Display Country Code**<br />`display_country_code` | — | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Display Area Code**<br />`display_area_code` | — | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Add tel: link**<br />`add_tel_link` | Wraps the phone number in a link that uses the tel: protocol | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Property separators

#### Phone Label

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Phone Label Prefix**<br />`label_prefix` | HTML to place before the phone label | `text` | — | — |
| **Phone Label Suffix**<br />`label_suffix` | HTML to place after the phone label | `text` | — | — |

#### Country Code

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Country Code Prefix**<br />`country_code_prefix` | Text to place before the country code | `text` | — | — |
| **Country-Area Separator**<br />`separator_cc_phone1` | Text to place between country code and area code | `text` | — | — |

#### Phone Number

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Area - Part 2 Separator**<br />`separator_phone1_phone2` | Text to place between area code and part 2 (e.g. switch code) | `text` | — | — |
| **Part 2 - Part 3 Separator**<br />`separator_phone2_phone3` | Text to place between part 2 and part3 (e.g. between switch code and user number) | `text` | — | — |

### Value list

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`opentag` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`closetag` | This text is placed immediately **after** every field value | `text` | — | — |
| **Opening text for Field**<br />`field_prefix` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`field_suffix` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

### Content plugins

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Viewing
