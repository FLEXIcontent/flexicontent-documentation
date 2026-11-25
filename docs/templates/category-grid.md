---
sidebar_position: 7
---

# Grid — category view



:::info Source
This page is generated from `site/templates/grid/category.xml` and the official FLEXIcontent 5.x language files.
:::

## Template parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# Featured**<br />`lead_num` | Number of featured items. Note effects items until featured number of items is reached, then all remains items in current and in next pages will be shown with 'standard' configuration | `text` | — | — |

#### Item tabset

### Common

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout custom title**<br />`custom_layout_title` | This will be displayed to frontend user, e.g. as tooltip of frontend layout switcher | `text` | — | — |

#### Item title

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Title text color**<br />`title_color` | Color of title text | `fccolor` | — | `none` |
| **Title background**<br />`title_background` | Color of title background | `fccolor` | — | `none` |
| **Title font size**<br />`title_font_size` | Size of title text | `text` | — | `none` |

#### Label styling

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Background**<br />`label_bg_color` | Select the background of your label | `fccolor` | — | `none` |
| **Text color**<br />`label_txt_color` | Select the color of text label | `fccolor` | — | `none` |
| **Padding top**<br />`label_pad_top` | Internal top spacing | `number` | — | `8` |
| **Padding right**<br />`label_pad_right` | Internal right spacing | `number` | — | `10` |
| **Padding left**<br />`label_pad_left` | Internal left spacing | `number` | — | `10` |
| **Padding bottom**<br />`label_pad_bottom` | Internal bottom spacing | `number` | — | `8` |
| **Border radius**<br />`label_radius` | Rounding of the label's borders | `number` | — | `3` |

#### commun Item box style

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Border radius**<br />`ibox_radius` | Rounding of the label's borders | `text` | — | `0px 0px 0px 0px` |
| **Overlay color**<br />`overlay_background` | Select the background of your label | `fccolor` | — | `rgba(0,0,0,0.4)` |

#### Shadow box

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Shadow X**<br />`ibox_shadow_x` | Rounding of the label's borders | `number` | — | `0` |
| **Shadow y**<br />`ibox_shadow_y` | Rounding of the label's borders | `number` | — | `0` |
| **Shadow blur**<br />`ibox_shadow_blur` | Rounding of the label's borders | `number` | — | `20` |
| **Shadow spread**<br />`ibox_shadow_spread` | Rounding of the label's borders | `number` | — | `0` |
| **Background**<br />`ibox_shadow_color` | Select the background of your label | `fccolor` | — | `rgba(0,0,0,0.2)` |
| **Shadow hover effect**<br />`ibox_shadow_hover` | Rounding of the label's borders | `number` | — | `50` |

#### Readon styling

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Background**<br />`readon_bg_color` | Select the background of your label | `fccolor` | — | `none` |
| **Text color**<br />`readon_txt_color` | Select the color of text label | `fccolor` | — | `none` |
| **Title font size**<br />`readon_font_size` | Size of title text | `text` | — | `none` |
| **Readon type**<br />`readon_type` | Number of columns for the items. NOTE: this is the max value and actually number of columns displayed will depend to width of browser window | `radio` | `—` = Use Global<br />`0` = Text<br />`1` = Image | — |
| **Read more image**<br />`readon_image` | Select image to use instead of read more, this is maybe useful if your website is not multilingual | `media` | — | — |
| **Read more class**<br />`readon_class` | Select class css to use instead of read more, this is maybe useful if your website is not multilingual | `text` | — | `btn btn-default` |

#### Lazy loading image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use lazy loading**<br />`use_lazy_loading` | Set yes to use native browser lazy loading | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

### Featured items

#### Items featured tabset

### Placement

#### Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **columns size**<br />`ibox_minsize_feat` | min size of column | `text` | — | `200px` |
| **Items placement**<br />`item_placement_feat` | Placement method for items, e.g. select as masonry tiles, to place them, so that no empty space gaps are between them, resembling the placement of masonry tiles _0_ | `radio` | `—` = Use Global<br />`0` = Cleared<br />`1` = As masonry tiles | — |
| **Open items in popup**<br />`lead_link_to_popup` | Items will be opened in a modal popup window _0_ | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Highlight items**<br />`hl_items_onnav_feat` | Highlight currently 'active' and 'hovered' items by adding CSS classes _0_ | `radio` | `—` = Use Global<br />`0` = No<br />`2` = On Hover | — |

#### Content / image placement

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Content Placement in regards to image**<br />`content_layout_feat` | Select to placement content next, or above/below (cleared) or over (ovelayed) the item image. Note: overlayed will crop content that does not fit from the bottom part _3_ | `list` | `—` = Use Global<br />`0` = Floated (Right)<br />`1` = Floated (Left)<br />`2` = Cleared (Above)<br />`3` = Cleared (Below)<br />`4` = Overlayed (Top)<br />`5` = Overlayed (Bottom)<br />`6` = Overlayed (Full) | — |
| **Content visible for overlayed**<br />`content_display_feat` | Select how image is fitted into the container _0_ | `radio` | `—` = Use Global<br />`0` = Always visible<br />`2` = On mouse over | — |
| **Image fit for cleared / overlayed**<br />`img_fit_feat` | Select how image is fitted into the container _1_ | `radio` | `—` = Use Global<br />`0` = Auto-Fit<br />`1` = Auto-Fit and Stretch | — |
| **Height of content**<br />`content_height_fit_feat` | Select yes to fix same height for each content _1_ | `radio` | `—` = Use Global<br />`0` = Content height<br />`1` = Force same height | — |
| **Height of content**<br />`content_width_fit_feat` | Select yes to fix same height for each content _1_ | `radio` | `—` = Use Global<br />`auto-fill` = Auto-fill<br />`auto-fit` = Auto-fit | `auto-fill` (Auto-fill) |
| **Readmore align**<br />`readmore_align_feat` | Number of columns for the items. NOTE: this is the max value and actually number of columns displayed will depend to width of browser window | `radio` | `—` = Use Global<br />`left` = Left<br />`center` = Center<br />`right` = Right | `center` (Center) |

### Styling

#### Items list box

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **background color**<br />`box_background_color_feat` | Items container's background color | `fccolor` | — | `none` |
| **padding top/bottom**<br />`box_padding_top_bottom_feat` | Items container's padding applied at top and bottom of the items | `text` | — | `0` |
| **padding left/right**<br />`box_padding_left_right_feat` | Items container's padding applied at left and right of the items | `text` | — | `0` |
| **margin top**<br />`box_margin_top_feat` | Items container's margin applied at top and bottom of the items | `text` | — | `4rem` |
| **margin bottom**<br />`box_margin_bottom_feat` | Items container's margin applied at top and bottom of the items | `text` | — | `4rem` |
| **margin left/right**<br />`box_margin_left_right_feat` | Items container's margin applied at left and right of the items | `text` | — | `0` |

#### Item box

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **background color**<br />`ibox_background_color_feat` | This is the background color applied at each item | `fccolor` | — | `none` |
| **description color**<br />`ibox_description_color_feat` | This is the background color applied at each item | `fccolor` | — | `none` |
| **border width**<br />`ibox_border_width_feat` | This is the border width applied around the items | `number` | — | `0` |
| **border color**<br />`ibox_border_color_feat` | This is the border color applied around the items | `fccolor` | — | `transparent` |
| **padding top/bottom**<br />`ibox_padding_top_bottom_feat` | This is the padding applied at top and bottom of the items | `text` | — | `0` |
| **padding left/right**<br />`ibox_padding_left_right_feat` | This is the padding applied at left and right of the items | `text` | — | `0` |
| **margin top/bottom**<br />`ibox_margin_top_bottom_feat` | This is the margin applied at top and bottom of the items | `text` | — | `2rem` |
| **margin left/right**<br />`ibox_margin_left_right_feat` | This is the margin applied at left and right of the items | `text` | — | `2rem` |

### Fields

#### (sub) Category block, at (sub-)category start

:::note
Warning: this makes sense, if you order your items by their category (1st level order), (2nd level order can be anything e.g. title)
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`lead_catblock` | — | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Category title**<br />`lead_catblock_title` | Show/hide the title of the category | `radio` | `—` = Use Global<br />`1` = Yes | — |

#### Text

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display description**<br />`lead_use_description` | Show / hide the description text | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Strip HTML tags & cut text**<br />`lead_strip_html` | Strip HTML tags from the text and also cut it to a maximum length. **NOTE:** This will force read more to appear | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes, Force Read More<br />`2` = Yes, if needed | — |
| **Introtext max length**<br />`lead_cut_text` | Auto cut introtext after x characters | `text` | — | — |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use image**<br />`lead_use_image` | Extract the first image from the text or use the above field | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Image source**<br />`lead_image` | Select the source of the image. You can either choose an image field (if available) or automatically extract the first image found in the main text. | `fcimage` | — | — |
| **Field HTML as Image**<br />`lead_image_custom_display` | You can use the HTML produced by any custom field in place of image. -- Leave blank: to use the above drop-down select box value, -- **Note: image size and other parameters are not used**, -- Write: like fieldname##varname e.g. for image fields use: imgfieldname##display_small, imgfieldname##display_medium, imgfieldname##display_large | `text` | — | — |
| **Field URL as Image**<br />`lead_image_custom_url` | You can use the URL produced by any custom field in place of image. -- Leave blank: to use the above drop-down select box value, -- **Note: image size and other parameters are applied to the given URL**, -- Write: like fieldname##varname e.g. for image fields use: imgfieldname##display_small_src, imgfieldname##display_medium_src, imgfieldname##display_large_src | `text` | — | — |
| **Image Field Fallback (when image missing)**<br />`lead_image_fallback_img` | When image is missing, you can select to use some image as fallback, e.g. item introtext image when image field has no value, even if image field has default value | `list` | `0` = No fallback<br />`1` = Use introtext image<br />`2` = Use introtext image (ignore image field default image)<br />`3` = Use custom field | — |
| **Select a custom field Fallback**<br />`lead_fallback_field` | — | `fcimage` | — | `0` |
| **Image position**<br />`lead_position` | The image position in the block. | `radio` | `—` = Use Global<br />`0` = Left<br />`1` = Right | — |
| **Link image**<br />`lead_link_image` | Open the item when clicking on the image | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Link to**<br />`lead_link_image_to` | If you are using an image field then you may use the custom link add to the image | `radio` | `—` = Use Global<br />`0` = Item<br />`1` = Custom link (image field) | — |
| **Intro image size**<br />`lead_image_size` | Size of the intro images | `radio` | `—` = Use parameters<br />`s` = Small<br />`m` = Medium<br />`l` = Large<br />`o` = Original | — |
| **Image width**<br />`lead_width` | Image width | `text` | — | — |
| **Image height**<br />`lead_height` | Image height | `text` | — | — |
| **Processing method**<br />`lead_method` | Processing method | `radio` | `—` = Use Global<br />`0` = Scale<br />`1` = Crop | — |
| **Default images (per type)**<br />`lead_default_images` | Either enter an image-path relative to Joomla root folder: image-path or enter per type, comma separated: _OTHER_##image-path, type-alias1##image-path1, type-alias2##image-path2 | `textarea` | — | — |

#### Items featured tabset

### Standard items

#### Items standard tabset

### Placement

#### Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **columns size**<br />`ibox_minsize_std` | min size of column | `text` | — | `200px` |
| **Items placement**<br />`item_placement` | Placement method for items, e.g. select as masonry tiles, to place them, so that no empty space gaps are between them, resembling the placement of masonry tiles _1_ | `radio` | `—` = Use Global<br />`0` = Cleared<br />`1` = As masonry tiles | — |
| **Open items in popup**<br />`intro_link_to_popup` | Items will be opened in a modal popup window _0_ | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Highlight items**<br />`hl_items_onnav` | Highlight currently 'active' and 'hovered' items by adding CSS classes _0_ | `radio` | `—` = Use Global<br />`0` = No<br />`2` = On Hover | — |

#### Content / image placement

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Content Placement in regards to image**<br />`content_layout` | Select to placement content next, or above/below (cleared) or over (ovelayed) the item image. Note: overlayed will crop content that does not fit from the bottom part _3_ | `list` | `—` = Use Global<br />`0` = Floated (Right)<br />`1` = Floated (Left)<br />`2` = Cleared (Above)<br />`3` = Cleared (Below)<br />`4` = Overlayed (Top)<br />`5` = Overlayed (Bottom)<br />`6` = Overlayed (Full) | — |
| **Content visible for overlayed**<br />`content_display` | Select how image is fitted into the container _0_ | `radio` | `—` = Use Global<br />`0` = Always visible<br />`2` = On mouse over | — |
| **Image fit for cleared / overlayed**<br />`img_fit` | Select how image is fitted into the container _1_ | `radio` | `—` = Use Global<br />`0` = Auto-Fit<br />`1` = Auto-Fit and Stretch | — |
| **Height of content**<br />`content_height_fit_stan` | Select yes to fix same height for each content _1_ | `radio` | `—` = Use Global<br />`0` = Content height<br />`1` = Force same height | — |
| **Height of content**<br />`content_width_fit` | Select yes to fix same height for each content _1_ | `radio` | `—` = Use Global<br />`auto-fill` = Auto-fill<br />`auto-fit` = Auto-fit | `auto-fill` (Auto-fill) |
| **Readmore align**<br />`readmore_align` | — | `radio` | `—` = Use Global<br />`left` = Left<br />`center` = Center<br />`right` = Right | `center` (Center) |

### Styling

#### Items list box

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **background color**<br />`box_background_color` | Items container's background color | `fccolor` | — | `none` |
| **padding top/bottom**<br />`box_padding_top_bottom` | Items container's padding applied at top and bottom of the items | `text` | — | `0` |
| **padding left/right**<br />`box_padding_left_right` | Items container's padding applied at left and right of the items | `text` | — | `0` |
| **margin top**<br />`box_margin_top` | Items container's margin applied at top and bottom of the items | `text` | — | `2rem` |
| **margin bottom**<br />`box_margin_bottom` | Items container's margin applied at top and bottom of the items | `text` | — | `2rem` |
| **margin left/right**<br />`box_margin_left_right` | Items container's margin applied at left and right of the items | `text` | — | `0` |

#### Item box

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **background color**<br />`ibox_background_color` | This is the background color applied at each item | `fccolor` | — | `none` |
| **description color**<br />`ibox_description_color` | This is the background color applied at each item | `fccolor` | — | `none` |
| **border width**<br />`ibox_border_width` | This is the border width applied around the items | `number` | — | `0` |
| **border color**<br />`ibox_border_color` | This is the border width applied around the items | `fccolor` | — | `transparent` |
| **padding top/bottom**<br />`ibox_padding_top_bottom` | This is the padding applied at top and bottom of the items | `text` | — | `0` |
| **padding left/right**<br />`ibox_padding_left_right` | This is the padding applied at left and right of the items | `text` | — | `0` |
| **margin top/bottom**<br />`ibox_margin_top_bottom` | This is the margin applied at top and bottom of the items | `text` | — | `2rem` |
| **margin left/right**<br />`ibox_margin_left_right` | This is the margin applied at left and right of the items | `text` | — | `2rem` |

### Fields

#### (sub) Category block, at (sub-)category start

:::note
Warning: this makes sense, if you order your items by their category (1st level order), (2nd level order can be anything e.g. title)
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`intro_catblock` | — | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Category title**<br />`intro_catblock_title` | Show/hide the title of the category | `radio` | `—` = Use Global<br />`1` = Yes | — |

#### Text

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display description**<br />`intro_use_description` | Show / hide the description text | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Strip HTML tags & cut text**<br />`intro_strip_html` | Strip HTML tags from the text and also cut it to a maximum length. **NOTE:** This will force read more to appear | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes, Force Read More<br />`2` = Yes, if needed | — |
| **Introtext max length**<br />`intro_cut_text` | Auto cut introtext after x characters | `text` | — | — |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use image**<br />`intro_use_image` | Extract the first image from the text or use the above field | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Image source**<br />`intro_image` | Select the source of the image. You can either choose an image field (if available) or automatically extract the first image found in the main text. | `fcimage` | — | — |
| **Field HTML as Image**<br />`intro_image_custom_display` | You can use the HTML produced by any custom field in place of image. -- Leave blank: to use the above drop-down select box value, -- **Note: image size and other parameters are not used**, -- Write: like fieldname##varname e.g. for image fields use: imgfieldname##display_small, imgfieldname##display_medium, imgfieldname##display_large | `text` | — | — |
| **Field URL as Image**<br />`intro_image_custom_url` | You can use the URL produced by any custom field in place of image. -- Leave blank: to use the above drop-down select box value, -- **Note: image size and other parameters are applied to the given URL**, -- Write: like fieldname##varname e.g. for image fields use: imgfieldname##display_small_src, imgfieldname##display_medium_src, imgfieldname##display_large_src | `text` | — | — |
| **Image Field Fallback (when image missing)**<br />`intro_image_fallback_img` | When image is missing, you can select to use some image as fallback, e.g. item introtext image when image field has no value, even if image field has default value | `list` | `0` = No fallback<br />`1` = Use introtext image<br />`2` = Use introtext image (ignore image field default image)<br />`3` = Use custom field | — |
| **Select a custom field Fallback**<br />`intro_fallback_field` | — | `fcimage` | — | `0` |
| **Image position**<br />`intro_position` | The image position in the block. | `radio` | `—` = Use Global<br />`0` = Left<br />`1` = Right | — |
| **Link image**<br />`intro_link_image` | Open the item when clicking on the image | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Link to**<br />`intro_link_image_to` | If you are using an image field then you may use the custom link add to the image | `radio` | `—` = Use Global<br />`0` = Item<br />`1` = Custom link (image field) | — |
| **Intro image size**<br />`intro_image_size` | Size of the intro images | `radio` | `—` = Use parameters<br />`s` = Small<br />`m` = Medium<br />`l` = Large<br />`o` = Original | — |
| **Image width**<br />`intro_width` | Image width | `text` | — | — |
| **Image height**<br />`intro_height` | Image height | `text` | — | — |
| **Processing method**<br />`intro_method` | Processing method | `radio` | `—` = Use Global<br />`0` = Scale<br />`1` = Crop | — |
| **Default images (per type)**<br />`intro_default_images` | Either enter an image-path relative to Joomla root folder: image-path or enter per type, comma separated: _OTHER_##image-path, type-alias1##image-path1, type-alias2##image-path2 | `textarea` | — | — |

#### Items featured tabset

#### Item tabset
