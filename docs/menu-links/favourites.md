---
sidebar_position: 12
---

# Favourites (legacy view)



:::info Source
This page is generated from `site/views/favourites/tmpl/default.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

### Seo

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Rel canonical tag**<br />`add_canonical` | Add a rel canonical meta tag into the source code of your pages, this helps search engines identify a page being viewed via different URLs, and give it better rank, by not indexing it multiple times | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

### Fields

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`use_image` | — | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Image source**<br />`image_source` | Select the source of the image. You can either choose an image field (if available) or automatically extract the first image found in the main text. | `fcimage` | — | — |
| **Link image**<br />`link_image` | Open the item when clicking on the image | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Intro image size**<br />`image_size` | Size of the intro images | `list` | `—` = Use parameters<br />`s` = Small<br />`m` = Medium<br />`l` = Large | — |
| **Image width**<br />`image_width` | Image width | `text` | — | `90` |
| **Image height**<br />`image_height` | Image height | `text` | — | `90` |
| **Processing method**<br />`image_method` | Processing method | `radio` | `0` = Scale<br />`1` = Crop | `0` (Scale) |

#### Revised date and time

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`show_modify_date` | — | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Date format**<br />`date_format` | Choose a date format using a Joomla Date constant (useful for multilingual websites) | `multilist` | `DATE_FORMAT_LC1` = Date format lc1<br />`DATE_FORMAT_LC2` = Date format lc2<br />`DATE_FORMAT_LC3` = Date format lc3<br />`DATE_FORMAT_LC4` = Date format lc4<br />`DATE_FORMAT_CUSTOM` = Custom format | `DATE_FORMAT_LC1` (Date format lc1) |
| **Custom format**<br />`custom_date` | If you choose 'custom format' in the dropdown above you have to specify in this field the format you wish to render using the PHP strftime syntax (http://php.net/strftime). | `text` | — | — |

#### Extra fields

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`use_fields` | — | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Fields List**<br />`fields` | Enter field names separated by commas | `textarea` | — | — |

### Pagination

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page**<br />`limit` | Number of items per page | `text` | — | `10` |
| **# per page**<br />`show_pagination` | Show/Hide pagination, such as links and page counting | `radio` | `0` = Hide<br />`1` = Show<br />`2` = Automatic | `2` (Automatic) |
| **Pagination's results (current # / total pages)**<br />`show_pagination_results` | (when pagination is enabled), you can use this option to disable the display of current active page number and total number for pages | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |

### Items Ordering

#### Item Ordering (Level 1)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby` | Order items by CORE fields/properties | `list` | `—` = Use Global<br />`date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified - Most Recent first<br />`published` = Published - Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most views first<br />`rhits` = Popularity -- Least views first<br />`id` = ID -- Highest First<br />`rid` = ID -- Lowest First<br />`commented` = Most Commented<br />`rated` = Best Rated<br />`order` = Ordering in current category<br />`jorder` = Ordering (Global) | — |

#### CUSTOM field ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`orderbycustomfield` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Custom field**<br />`orderbycustomfieldid` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | `fields` | — | — |
| **Direction**<br />`orderbycustomfielddir` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `radio` | `—` = Use Global<br />`ASC` = Ascending<br />`DESC` = Descending | — |
| **Ordering Method**<br />`orderbycustomfieldint` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `radio` | `—` = Use Global<br />`0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date | — |

#### Item Ordering (Level 2)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby_2nd` | Order items by CORE fields/properties | `list` | `—` = Use Global<br />`date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified - Most Recent first<br />`published` = Published - Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most views first<br />`rhits` = Popularity -- Least views first<br />`id` = ID -- Highest First<br />`rid` = ID -- Lowest First<br />`commented` = Most Commented<br />`rated` = Best Rated<br />`order` = Ordering in current category<br />`jorder` = Ordering (Global) | — |

#### CUSTOM field ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`orderbycustomfield_2nd` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Custom field**<br />`orderbycustomfieldid_2nd` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | `fields` | — | — |
| **Direction**<br />`orderbycustomfielddir_2nd` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `radio` | `—` = Use Global<br />`ASC` = Ascending<br />`DESC` = Descending | — |
| **Ordering Method**<br />`orderbycustomfieldint_2nd` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `radio` | `—` = Use Global<br />`0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date | — |

### Frontend Overrides

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page**<br />`limit_override` | Number of items per page | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Ordering selector (Level 1)**<br />`orderby_override` | Enable to display frontend ordering selector (Level 1) | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Ordering selector (Level 2)**<br />`orderby_override_2nd` | Enable to display frontend ordering selector (Level 2) | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |

#### Select Available Options

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page allowed to frontend user**<br />`limit_options` | Please enter a comma separated list of number, leave empty to use Global Defaults | `text` | — | — |
| **Order options (Level 1) allowed to frontend user**<br />`orderby_options` | Please select the ordering options you wish to allow. **NOTE:** (a) **Preconfigured initial order**, is order configured in categories configuration, (b)** Content 's ordering attribute** is for current category, since there is one such order for every category assigned to the item | `fccheckbox` | — | — |
| **Custom Order (Level 1) allowed to frontend user**<br />`orderby_custom` | Order options custom desc | `textarea` | — | — |
| **Order options (Level 2) allowed to frontend user**<br />`orderby_options_2nd` | Please select the ordering options you wish to allow. **NOTE:** (a) **Preconfigured initial order**, is order configured in categories configuration, (b)** Content 's ordering attribute** is for current category, since there is one such order for every category assigned to the item | `fccheckbox` | — | — |
| **Custom Order (Level 2) allowed to frontend user**<br />`orderby_custom_2nd` | Order options custom desc | `textarea` | — | — |

## Parameters

#### Text Search

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use search**<br />`use_search` | Display a text search box | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Show Label**<br />`show_search_label` | You may want to hide label or display label inside the text search input to save space | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Go Button**<br />`show_search_go` | Submit form reloading current listing, **Note**: that this will submit text search, field filters and alpha index (when any of these is present) | `radio` | `—` = Use Global<br />`0` = Automatic<br />`1` = Show | — |
| **Reset Button**<br />`show_search_reset` | Clear form reloading current listing, **Note**: Note that this will also clear field filters and alpha index (when any of these is present) | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
