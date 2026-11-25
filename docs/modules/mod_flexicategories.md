---
sidebar_position: 5
---

# Categories

FLEXIcontent provides six frontend modules for displaying items, categories, search forms, filters, maps and tag clouds. Configure a module from **Extensions → Modules**.

> This module displays a list of categories from one parent category.

:::info Source
This page is generated from `modules/mod_flexicategories/mod_flexicategories.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

### Template Layout

:::note
Please set layout parameters in **Layout: ... TAB**. CSS/HTML developers please read: ** Custom templates HOW-TO **
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout**<br />`layout` | Choose a layout to render your module | `fclayout` | — | `default` |

### Basic Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Parent Category**<br />`parent` | Choose a parent category. | `category` | — | — |
| **Empty categories**<br />`show_empty_cats` | Select to skip categories that have zero items in them and in their sub-categories | `multilist` | `0` = Jhide<br />`1` = Jshow | `1` (Jshow) |
| **# First Subcategories**<br />`count` | Select the number of first level subcategories to display. Default is all. | `list` | `0` = Jall<br />`1` = J1<br />`2` = J2<br />`3` = J3<br />`4` = J4<br />`5` = J5<br />`6` = J6<br />`7` = J7<br />`8` = J8<br />`9` = J9<br />`10` = J10 | `0` (Jall) |

#### Information shown

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category Descriptions**<br />`show_description` | Show or hide category descriptions. | `radio` | `0` = Jhide<br />`1` = Jshow | `0` (Jhide) |
| **Number of Articles (cached)**<br />`numitems` | Show or hide number of articles. This is updated every e.g. 1 hour, please check value of FLEXIcontent advanced cache time in component parameters | `radio` | `0` = Jhide<br />`1` = Jshow | `0` (Jhide) |

#### Subcategories

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show Subcategories**<br />`show_children` | Show or hide subcategories. | `radio` | `0` = Jno<br />`1` = Jyes | `0` (Jno) |
| **Maximum Level Depth**<br />`maxlevel` | Select the maximum level depth for each subcategory. Default is all. | `list` | `0` = Jall<br />`1` = J1<br />`2` = J2<br />`3` = J3<br />`4` = J4<br />`5` = J5<br />`6` = J6<br />`7` = J7<br />`8` = J8<br />`9` = J9<br />`10` = J10 | `0` (Jall) |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show image**<br />`show_description_image` | Show/Hide image, also select image source | `multilist` | `0` = Jno<br />`1` = Jyes | `0` (Jno) |
| **Image source**<br />`cat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | `radio` | `0` = Extract from description<br />`1` = Use image parameter<br />`2` = Try parameter then extract | `2` (Try parameter then extract) |
| **Link image**<br />`cat_link_image` | Link image to category view | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Processing method**<br />`cat_image_method` | Method of creating the image thumbnail, scale: scales to fit both dimensions, crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Width**<br />`cat_image_width` | Width | `text` | — | `24` |
| **Height**<br />`cat_image_height` | Height | `text` | — | `24` |
| **Image position**<br />`cat_image_float` | The image position in the block | `radio` | `left` = Left<br />`right` = Right | `left` (Left) |
| **Default image**<br />`cat_default_image` | Default image for categories without one | `media` | — | — |
| **Image WebP**<br />`cat_image_webp` | Create webp via phpThumb (f=webp). If browser support webp that will be display, or using jog fallback. | `radio` | `0` = Jno<br />`1` = Jyes | `0` (Jno) |

## Hide/Show Module

These rules specify when module contents will be created (thus shown) or not created (thus hidden).

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Combine Rules**<br />`combine_show_rules` | Either require any or both VIEWS rules and PHP expression rule, in order to show the module | `radio` | `OR` = OR<br />`AND` = And | `AND` (And) |

#### Clients

:::note
Please note that if **Joomla Caching** is enabled inside Joomla **Global Configuration** then - either enable '**Platform specific caching**' (note that 'tablet' is detected as 'mobile') - or disable caching inside 'Advanced setting' TAB of this module if none of the above is done then this setting will be ignored
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select to show in desktops, tablets, mobiles | `fccheckbox` | — | — |

#### Views (category, item, etc) Rules

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in views**<br />`show_in_views` | Select view in which module will be shown | `fccheckbox` | — | — |

#### PHP Expresion Rule

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable Rule**<br />`enable_php_rule` | You can disable rule without removing the rule 's entered text | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **PHP rule code**<br />`php_rule` | The given PHP code is execute and last statement must return a boolean value (via 'return' statement) which will used to decide to show or not the module | `textarea` | — | — |

## Layout: Options of selected Layout

Layout Options specific to the chosen template layout

## Advanced

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Heading Style**<br />`item_heading` | Set the heading style to use. | `list` | `1` = Jh1<br />`2` = Jh2<br />`3` = Jh3<br />`4` = Jh4<br />`5` = Jh5 | `4` (Jh4) |
| **Modules field moduleclass sfx label**<br />`moduleclass_sfx` | Modules field moduleclass sfx desc | `textarea` | — | — |
| **Modules field caching label**<br />`owncache` | Modules field caching desc | `list` | `1` = Use global<br />`0` = Modules field value nocaching | `1` (Use global) |
| **Modules field cache time label**<br />`cache_time` | Modules field cache time desc | `text` | — | `900` |
