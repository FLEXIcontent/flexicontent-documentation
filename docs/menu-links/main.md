---
sidebar_position: 8
---

# Directory (main view)



:::info Source
This page is generated from `site/views/flexicontent/tmpl/default.xml` and the official FLEXIcontent 5.x language files.
:::

## Required parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Root category**<br />`rootcat` | Please select the root category for this directory | `fccategory` | — | `1` |

## Basic

#### Pathway (Breadcrumbs)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Start to add parents categories at depth**<br />`item_depth` | You can set the category tree depth, at which adding of parent category links to the pathway should start. **NOTE:** Inside FLEXIcontent Advanced Route - System Plugin, you can select to disable the adding of categories to the pathway for specific item CONTENT TYPES | `list` | `0` = root<br />`1` = level 1<br />`2` = level 2<br />`3` = level 3<br />`4` = level 4<br />`5` = level 5 | `0` (root) |

#### Basic Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Introtext**<br />`introtext` | Will be displayed above the category listing | `textarea` | — | — |
| **Display introtext**<br />`showintrotext` | Choose whether or not you want to display the introtext | `radio` | `0` = Hide<br />`1` = Show | `0` (Hide) |
| **Items count**<br />`showassignated` | Show/Hide the items count of each sub-category | `radio` | `0` = Hide<br />`1` = Show | `0` (Hide) |
| **Categories List limit**<br />`catlimit` | Max categories listed in categories lists | `text` | — | `200` |

### Categories Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category List Order**<br />`cat_orderby` | Ordering of the Category List, available options depend on the category properties available e.g. category name, backend confiured ordering, etc | `list` | `—` = Use Global<br />`date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified - Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most views first<br />`rhits` = Popularity -- Least views first<br />`order` = Category 's ordering attribute | `order` (Category 's ordering attribute) |
| **Hide Empty Categories**<br />`hide_empty_cats` | As empty categories are considered the ones that: 1. Have no assigned items 2. All their subcategories have no assigned items, and have no subcategories. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Description**<br />`show_cat_descr` | Show/Hide description, also enter a maximum length | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |
| **Description length**<br />`cat_descr_cut` | Description text longer than this value will be cut off | `text` | — | `100` |
| **Title linkable**<br />`cat_link_title` | Link title to the respective view | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Image**<br />`show_cat_image` | Show/Hide image, also select image source | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |
| **Image source**<br />`cat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | `list` | `0` = Extract from description<br />`1` = Use image parameter<br />`2` = Try parameter then extract | `2` (Try parameter then extract) |
| **Link image**<br />`cat_link_image` | Open the item when clicking on the image | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Processing method**<br />`cat_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Image width**<br />`cat_image_width` | Image width | `text` | — | `80` |
| **Image height**<br />`cat_image_height` | Image height | `text` | — | `80` |

### Subcategories Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Subcategory List Order**<br />`subcat_orderby` | Order that the items will be displayed in | `list` | `—` = Order defaukt<br />`date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified - Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most views first<br />`rhits` = Popularity -- Least views first<br />`order` = Ordering in current category | `order` (Ordering in current category) |
| **Hide Empty Subcategories**<br />`hide_empty_subcats` | As empty subcategories are considered the ones that have no assigned items, and have no subcategories. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Description**<br />`show_subcat_descr` | Show/Hide description, also enter a maximum length | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |
| **Description length**<br />`subcat_descr_cut` | Description text longer than this value will be cut off | `text` | — | `50` |
| **Image**<br />`show_subcat_image` | Show/Hide image, also select image source | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |
| **Image source**<br />`subcat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | `list` | `0` = Extract from description<br />`1` = Use image parameter<br />`2` = Try parameter then extract | `2` (Try parameter then extract) |
| **Link image**<br />`subcat_link_image` | Open the item when clicking on the image | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Processing method**<br />`subcat_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Image width**<br />`subcat_image_width` | Image width | `text` | — | `40` |
| **Image height**<br />`subcat_image_height` | Image height | `text` | — | `40` |

### Layout Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# columns**<br />`columns_count` | Choose the number of columns for this directory | `list` | `1` = 1 column<br />`2` = 2 columns<br />`3` = 3 columns<br />`4` = 4 columns | `1` (1 column) |
| **# blocks for col nr1**<br />`column1` | Choose the number of blocks you wish to display in the first column. Note: 1 block represents the main category and its subcategories. | `text` | — | `0` |
| **# blocks for col nr2**<br />`column2` | Choose the number of blocks you wish to display in the second column. Note: 1 block represents the main category and its subcategories. | `text` | — | `0` |
| **# blocks for col nr3**<br />`column3` | Choose the number of blocks you wish to display in the third column. Note: 1 block represents the main category and its subcategories. | `text` | — | `0` |
