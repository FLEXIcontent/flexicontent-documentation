---
sidebar_position: 22
---

# User profile

Joomla Profile Field Plugin for FLEXIcontent

*Plugin : `jprofile` — User Profile*

:::info Source
This page is generated from `plugins/flexicontent_fields/jprofile/jprofile.xml` and the official FLEXIcontent 5.x language files.
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
| **Displayed user**<br />`displayed_user` | Select which user profile will be shown | `multilist` | `1` = Author of the item<br />`2` = Allow selection (in item form)<br />`3` = Current frontend user | `1` (Author of the item) |

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
| **Profile link**<br />`link_to_profile` | Profile Link using specific extension | `radio` | `1` = Joomla Contact<br />`2` = Community Builder<br />`3` = Jomsocial | `1` (Joomla Contact) |
| **Displayed HTML**<br />`display_text` | Replacements: Profile url: __profile_url__ Language strings: %%string%% Item properties: &#123;&#123;item-&gt;prop&#125;&#125; User properties &#123;&#123;user-&gt;prop&#125;&#125; | `textarea` | — | `&#123;&#123;user-&gt;name&#125;&#125; %%FLEXI_FIELD_JP_VIEW_PROFILE%%` |

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
