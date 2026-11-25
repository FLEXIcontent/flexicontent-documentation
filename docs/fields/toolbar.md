---
sidebar_position: 38
---

# Toolbar

Toolbar Field for FLEXIcontent

:::info Source
This page is generated from `plugins/flexicontent_fields/toolbar/toolbar.xml` and the official FLEXIcontent 5.x language files.
:::

## Viewing

#### Viewing

### Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| `frontend_hidden` | — | `hidden` | — | `1` |
| `backend_hidden` | — | `hidden` | — | `1` |

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

#### Backend View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Backend view appearance**<br />`backend_view_appearance` | How this field's value is displayed in the admin items list. Overrides the global 'Custom columns appearance' setting when not set to Default. | `multilist` | `0` = Default<br />`1` = Check mark<br />`2` = Clean up HTML and trim | `0` (Default) |
| **Trim length (characters)**<br />`backend_view_trim_chars` | Number of characters to keep after stripping HTML tags. | `text` | — | `100` |

### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fclayout` | — | `default` |

#### Value list

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Opening text for Field**<br />`opentag` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

### Parameters

#### Viewing

## Social

### Social websites support (e.g. Facebook)

#### Text

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Site name**<br />`add_og_site_name` | Select what should be suggested as site name of current page | `radio` | `0` = No<br />`1` = Real site name | `0` (No) |
| **Title**<br />`add_og_title` | Select what should be suggested as title of current page | `radio` | `0` = No<br />`1` = Item's title | `0` (No) |
| **Description**<br />`add_og_descr` | Select what should be suggested as description of current page | `radio` | `0` = No<br />`1` = Item's description | `0` (No) |
| **Content type**<br />`add_og_type` | Select what should be suggested as content type of current page | `radio` | `0` = No<br />`article` = Use 'article'<br />`website` = Use 'website' | `article` (Use 'article') |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add**<br />`add_og_image` | Select what should be suggested as image of current page | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Image source**<br />`og_image_field` | NOTE: usually, this should be an image field | `fcimage` | — | — |
| **Image Field Fallback (when image missing)**<br />`og_image_fallback` | When image is missing, you can select to use some image as fallback, e.g. item description text image when image field has no value, even if image field has default value | `list` | `0` = No fallback<br />`1` = Use image description text<br />`2` = Use item description text image (ignore image field default image) | — |
| **Thumbnail size**<br />`og_image_thumbsize` | Thumbnail size (if using image field) | `radio` | `small` = small<br />`medium` = medium<br />`large` = large | `medium` (medium) |
