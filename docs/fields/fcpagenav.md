---
sidebar_position: 18
---

# Page navigation

Page Navigation Field Plugin for FLEXIcontent

*Plugin : `fcpagenav` — Navigation*

:::info Source
This page is generated from `plugins/flexicontent_fields/fcpagenav/fcpagenav.xml` and the official FLEXIcontent 5.x language files.
:::

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

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Add the plugin CSS**<br />`load_css` | Load the plugin CSS file | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Current position**<br />`show_prevnext_count` | Display total number of items being navigated and also the current position | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |
| `frontend_hidden` | — | `hidden` | — | `1` |
| `backend_hidden` | — | `hidden` | — | `1` |

## Links

### Previous / Next items

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Loop previous / next**<br />`loop_prevnext` | The next link will link to first item when last item is viewed, similarly the previous link will to last item when first item is viewed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Tooltips

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use tooltip**<br />`use_tooltip` | Use the standard Joomla fancy mootools tooltip behavior | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Tooltip legend (next)**<br />`tooltip_title_next` | Choose the legend of your tooltip for the next item | `text` | — | — |
| **Tooltip legend (previous)**<br />`tooltip_title_prev` | Choose the legend of your tooltip for the previous item | `text` | — | — |

#### Button Text

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use item title**<br />`use_title` | Use the item title instead of the prev/next buttons for accessiblity and SEO purposes. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Previous button label**<br />`prev_label` | — | `text` | — | — |
| **Next button label**<br />`next_label` | — | `text` | — | — |

### Category

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use the link "back to category"**<br />`use_category_link` | The link "Back to category" returns to the category of article with conserving its position | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Category button label**<br />`category_label` | — | `text` | — | — |

## Images

### Images

#### Thumbnailing parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Image width**<br />`nav_width` | Image width | `text` | — | `120` |
| **Image height**<br />`nav_height` | Image height | `text` | — | `60` |
| **Processing method**<br />`nav_method` | Processing method | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |

### Item images

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use image**<br />`item_use_image` | Extract the first image from the text or use the above field | `multilist` | `0` = Hide<br />`1` = Show | `0` (Hide) |
| **Image source**<br />`item_image` | Select the source of the image. You can either choose an image field (if available) or automatically extract the first image found in the main text. | `fcimage` | — | — |
| **Image size**<br />`item_image_size` | FLEXI_IMAGE_SIZE_DESC | `radio` | `—` = Use parameters<br />`s` = Small<br />`m` = Medium<br />`l` = Large<br />`o` = Original | — |

### Category image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category image**<br />`cat_use_image` | Show/Hide the category image | `multilist` | `0` = Hide<br />`1` = Show | `0` (Hide) |
| **Image source**<br />`cat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | `radio` | `0` = Extract from description<br />`1` = Use image parameter<br />`2` = Try parameter then extract | `2` (Try parameter then extract) |
