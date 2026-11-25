---
sidebar_position: 8
---

# Tag cloud

FLEXIcontent provides six frontend modules for displaying items, categories, search forms, filters, maps and tag clouds. Configure a module from **Extensions → Modules**.

> Tags Cloud Module for FLEXIcontent

:::info Source
This page is generated from `modules/mod_flexitagcloud/mod_flexitagcloud.xml` and the official FLEXIcontent 5.x language files.
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
| **Minimum Font Size**<br />`min_size` | The minimum font size. Don't change if you have no idea how to adjust the CSS file accordingly!!! | `text` | — | `1` |
| **Maximum Font Size**<br />`max_size` | The maximum font size. Don't change if you have no idea how to adjust the CSS file accordingly!!! | `text` | — | `10` |
| **Max number of tags**<br />`count` | The maximum number of Tags in the cloud. | `text` | — | `25` |
| **Seo mode**<br />`seo_mode` | Don't use the accessibility options to avoid google indexing the screenreader informations | `radio` | `1` = Yes<br />`0` = No | `1` (Yes) |
| **Force Itemid**<br />`force_itemid` | Force routing the tags to a specific Itemid | `text` | — | — |

#### Categories

:::note
Show tags of items in the following categories. **Current category** is - either currently viewed category - or main category of the item currently viewed
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category**<br />`method` | You can set here the included or excluded category/ies. Only tags for from items that belongs (or not belongs) to these categories will be displayed. | `multilist` | `0` = Any<br />`1` = current<br />`2` = Exclude<br />`3` = Include | `1` (current) |
| **Categories**<br />`categories` | Please select the categories | `flexicategories` | — | — |
| **Extra categories**<br />`treeinclude` | — | `list` | `0` = None<br />`1` = Children categories | `0` (None) |

#### Item type

:::note
Limit **displayed tags** and their **links** to tagged items view, - to items having the same type
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Limit to current type**<br />`method_types` | Please make sure that tags field is configured to be filterable and that tags view is not set to legacy mode (only need to check this if you changed the default setting in component configuration) | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |

## Hide/Show Module

These rules specify when module contents will be created (thus shown) or not created (thus hidden).

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Combine Rules**<br />`combine_show_rules` | Either require any or both VIEWS rules and PHP expression rule, in order to show the module | `radio` | `OR` = OR<br />`AND` = And | `AND` (And) |

#### Clients

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

## Tagged items view (Legacy)

:::note
Note these are meant for tags legacy view. For category-based tags view, please configure in component / category / menu items parameters
:::

#### Parameters tags view legacy

### Fields

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`use_image` | — | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Image source**<br />`image_source` | Select the source of the image. You can either choose an image field (if available) or automatically extract the first image found in the main text. | `fcimage` | — | — |
| **Link image**<br />`link_image` | Open the item when clicking on the image | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Intro image size**<br />`image_size` | Size of the intro images | `multilist` | `—` = Use parameters<br />`s` = Small<br />`m` = Medium<br />`l` = Large | — |
| **Image width**<br />`image_width` | Image width | `text` | — | `90` |
| **Image height**<br />`image_height` | Image height | `text` | — | `90` |
| **Processing method**<br />`image_method` | Processing method | `radio` | `0` = Scale<br />`1` = Crop | `0` (Scale) |

#### Revised date and time

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`show_modify_date` | — | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Date format**<br />`date_format` | Choose a date format using a Joomla Date constant (useful for multilingual websites) | `multilist` | `DATE_FORMAT_LC1` = Date format lc1<br />`DATE_FORMAT_LC2` = Date format lc2<br />`DATE_FORMAT_LC3` = Date format lc3<br />`DATE_FORMAT_LC4` = Date format lc4<br />`DATE_FORMAT_CUSTOM` = Custom format | `DATE_FORMAT_LC1` (Date format lc1) |
| **Custom format**<br />`custom_date` | If you choose 'custom format' in the dropdown above you have to specify in this field the format you wish to render using the PHP strftime syntax (http://www.php.net/strftime). | `text` | — | — |

#### Extra fields

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`use_fields` | — | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Fields List**<br />`fields` | Enter field names seperated by commas | `textarea` | — | — |

### Pagination (Page links & Totals)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page**<br />`limit` | Number of items per page | `text` | — | `10` |
| **Pagination (Page links & Totals)**<br />`show_pagination` | Show/Hide pagination, such as links and page counting | `radio` | `0` = Hide<br />`1` = Show<br />`2` = Auto | `2` (Auto) |
| **Pagination's results (current # / total pages)**<br />`show_pagination_results` | (when pagination is enabled), you can use this option to disable the display of current active page number and total number for pages | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |

### Seo

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Rel canonical tag**<br />`add_canonical` | Add a rel canonical meta tag into the source code of your pages, this helps search engines identify a page being viewed via different URLs, and give it better rank, by not indexing it multiple times | `radio` | `—` = Use global<br />`0` = No<br />`1` = Yes | — |

### Items Ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Primary Order**<br />`orderby` | Order that the items will be displayed in | `list` | `—` = Default<br />`date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified - Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most hits first<br />`rhits` = Popularity -- Least hits first<br />`order` = Ordering in current category | — |
| **Custom field**<br />`orderbycustomfieldid` | Select a custom field to use for ordering, overriding the primary order. Attention, some type of fields can not be ordained (file and image field for example). | `fields` | — | `0` |
| **Direction**<br />`orderbycustomfielddir` | — | `radio` | `ASC` = Ascending<br />`DESC` = Descending | `ASC` (Ascending) |
| **Field Type**<br />`orderbycustomfieldint` | — | `radio` | `0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date | `0` (Text) |

### Frontend Overrides

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page**<br />`limit_override` | Number of items per page | `radio` | `—` = Use global<br />`0` = No<br />`1` = Yes | — |
| **Primary Order**<br />`orderby_override` | Order that the items will be displayed in | `radio` | `—` = Use global<br />`0` = No<br />`1` = Yes | — |

#### Select Available Options

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page allowed to frontend user**<br />`limit_options` | Please enter a comma seperated list of number, leave empty to use Global Defaults | `text` | — | — |
| **Primary order allowed to frontend user**<br />`orderby_options` | Please select the ordering options you wish to allow. **NOTE:** (a) **Preconfigured initial order**, is order configured in categories configuration, (b)** Content 's ordering attribute** is for current category, since there is one such order for every category assigned to the item | `fccheckbox` | — | — |

### Text Search

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use search box**<br />`use_search` | Display search box in this category view | `radio` | `—` = Use global<br />`0` = No<br />`1` = Yes | — |
| **Text search label**<br />`show_search_label` | You may want to hide this label to save space, e.g. in combination with compact filter area parameter | `radio` | `—` = Use global<br />`0` = Hide<br />`1` = Show | — |
| **Tooltip for text search**<br />`show_search_tip` | Display an informative popup text about text search | `radio` | `—` = Use global<br />`0` = Hide<br />`1` = Show | — |
| **Go Button**<br />`show_search_go` | Submit form reloading current listing, **Note**: that this will submit text search, field filters and alpha index (when any of these is present) | `radio` | `—` = Use global<br />`0` = Hide<br />`1` = Show | — |
| **Reset Button**<br />`show_search_reset` | Clear form reloading current listing, **Note**: Note that this will also clear field filters and alpha index (when any of these is present) | `radio` | `—` = Use global<br />`0` = Hide<br />`1` = Show | — |

#### Parameters tags view legacy

## Advanced

### Caching

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Caching**<br />`cache` | Select whether to cache the content of this module. | `list` | `1` = Use global<br />`0` = No caching | `1` (Use global) |
| **Cache Time**<br />`cache_time` | The time before the module is recached. | `text` | — | `900` |

### CSS / JS

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add css**<br />`add_ccs` | Add the module default css file | `radio` | `—` = Use component setting<br />`0` = No<br />`1` = Yes<br />`2` = CSS links inside HTML (allows capturing) | — |

### Module Container

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Module Class Suffix**<br />`moduleclass_sfx` | A suffix to be applied to the css class of the module, this allows individual module styling. | `text` | — | — |
