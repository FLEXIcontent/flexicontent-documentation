---
sidebar_position: 4
---

# Advanced search

FLEXIcontent provides six frontend modules for displaying items, categories, search forms, filters, maps and tag clouds. Configure a module from **Extensions → Modules**.

> This module displays a simple search form that links to FLEXIcontent search view

:::info Source
This page is generated from `modules/mod_flexiadvsearch/mod_flexiadvsearch.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

### Template Layout

:::note
Please set layout parameters in **Layout: ... TAB**. CSS/HTML developers please read: ** Custom templates HOW-TO **
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout**<br />`layout` | Choose a layout to render your module | `fclayout` | — | `news` |

### Search view menu item (contains the search view configuration)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Force menu item**<br />`itemid_force` | This option will force all links to items to use the current menu itemid or a specific menu itemid | `multilist` | `0` = Default (component configuration)<br />`1` = Custom (below) | `0` (Default (component configuration)) |
| **Custom menu itemid**<br />`itemid_force_value` | Custom menu itemid | `text` | — | — |

### Basic Configuration

#### Text Search Field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Size (# of characters)**<br />`search_inner_width` | Size of the text search input field width in characters | `text` | — | `20` |
| **Inner prompt (when empty)**<br />`search_inner_prompt` | This is the text to be displayed inside text search field as a prompt before text is typed. **NOTE**: This can be a language string | `text` | — | `FLEXI_ADV_MOD_SEARCH_PROMPT` (Search ...) |

#### Go Button (submit)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`button` | Displays a go / search (submit) button, otherwise the user can submit only by clicking enter inside the text search field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **CSS class**<br />`flexi_button_class_go` | CSS class for this button, use value in selectlist or type your custom class | `multilist` | `-1` = - Custom -<br />`btn` = Plain<br />`btn btn-primary` = Primary<br />`btn btn-success` = Success<br />`btn btn-info` = Info<br />`btn btn-warning` = Warning<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn btn-success` (Success) |
| **Custom class**<br />`flexi_button_class_go_custom` | Add custom class for this button, like uk-button uk-button-large for a warp 7 template | `text` | — | — |
| **Position**<br />`button_pos` | Position of the button relative to the search box | `radio` | `right` = Right<br />`left` = Left<br />`top` = Top<br />`bottom` = Bottom | `right` (Right) |
| **Button as**<br />`button_as` | Display button as either text or an image. **NOTE**: set an image path relative to the Joomla folder | `multilist` | `0` = Text<br />`1` = Image | `0` (Text) |
| **Image path**<br />`button_image` | Image path | `text` | — | — |
| **Text**<br />`button_text` | When the Go button is text **NOTE**: This can be a language string | `text` | — | `FLEXI_ADV_MOD_GO` (Go) |

#### Search Form: Content Types

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show Label**<br />`show_type_label` | You may want to hide label or display label inside the content types search | `radio` | `—` = Use global<br />`0` = Hide<br />`1` = Show | — |
| **Searchable Types (Select NONE for -ALL-)**<br />`contenttypes` | The content types the search will include, selecting none will include ALL. NOTE: You can allow user to select Content Types. If you do then the selection list will be LIMITED to display ONLY the types specified here | `types` | — | — |
| **Allow user selection**<br />`canseltypes` | Allow users to select content types they want to include in their search | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Search Form: Advanced Options

:::note
NOTE: when advanced search options box is hidden, the options configured below will still be used
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Advanced search options box**<br />`autodisplayadvoptions` | If this is disabled. Then a clickable text will appear to allow user to toggle the advanced search box on/off. | `radio` | `0` = Hide<br />`1` = Yes, initially closed<br />`2` = Yes, initially opened | `1` (Yes, initially closed) |
| **Text search using**<br />`txtmode` | Using the basic search index is faster and is recommended for LARGE SITES, (test to see evaluate performance difference) | `multilist` | `0` = Basic Index (faster, fields not selectable)<br />`1` = Advanced Index (use configured fields)<br />`2` = Advanced Index (use configured fields, allow user selection) | `0` (Basic Index (faster, fields not selectable)) |

#### PER content type configuration (ADVANCED Index)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Text-Search Fields**<br />`show_txtfields` | Enable this to use specific text searchable fields | `multilist` | `0` = Use all searchable<br />`1` = According to type<br />`2` = Configure below | `1` (According to type) |
| **Fields (Leave EMPTY for -ALL-)**<br />`txtflds` | NOTE: only fields marked as advanced index text-searchable are listed | `filters` | — | — |

#### Search Areas (non-FC Content)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use areas**<br />`show_searchareas` | Allow the user to select and search other areas of the website content, e.g. like weblinks, user contacts, etc | `multilist` | `0` = Disable<br />`1` = Enable, show selector | `0` (Disable) |
| **Search Areas**<br />`searchareas` | The site's (non-FC content) search areas, that the search will include. NOTE: if user is allowed to select Search Areas, then the selection list will be LIMITED to display ONLY the search areas selected here | `radio` | `—` = All | — |
| **Show ordering**<br />`show_searchordering` | Allow frontend users to select ordering of results of other areas of the website content. NOTE this is different ordering from the ordering used for main content results. | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Default value**<br />`default_searchordering` | Default ordering for sorting the results of the search | `radio` | `newest` = Newest first<br />`oldest` = Oldest first<br />`popular` = Most popular<br />`alpha` = Alphabetical<br />`category` = Section/Category | `newest` (Newest first) |

#### Direct Button (Go to the first result)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`direct_button` | Displays a direct / lucky button | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **CSS class**<br />`flexi_button_class_direct` | CSS class for this button, use value in selectlist or type your custom class | `multilist` | `-1` = - Custom -<br />`btn` = Plain<br />`btn btn-primary` = Primary<br />`btn btn-success` = Success<br />`btn btn-info` = Info<br />`btn btn-warning` = Warning<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn` (Plain) |
| **Custom class**<br />`flexi_button_class_direct_custom` | Add custom class for this button, like uk-button uk-button-large for a warp 7 template | `text` | — | — |
| **Position**<br />`direct_pos` | Position of the button relative to the search box | `radio` | `right` = Right<br />`left` = Left<br />`top` = Top<br />`bottom` = Bottom | `right` (Right) |
| **Button as**<br />`direct_as` | Display button as either text or an image. **NOTE**: set an image path relative to the Joomla folder | `multilist` | `0` = Text<br />`1` = Image | `0` (Text) |
| **Image path**<br />`direct_image` | Image path | `text` | — | — |
| **Text**<br />`direct_text` | When the Direct button is text **NOTE**: This can be a language string | `text` | — | `FLEXI_ADV_MOD_DIRECT` (Lucky) |

#### Advanced search view link

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show link**<br />`link_to_advsearch` | Enable this to display a direct link to the (FLEXIcontent) advanced search view | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Linked Text**<br />`link_to_advsearch_txt` | The text that will be linked to (FLEXIcontent) advanced search view | `text` | — | `FLEXI_ADV_MOD_OPEN_DETAILED_SEARCH` (Open detailed Search) |
| **CSS class**<br />`flexi_button_class_advanced` | CSS class for this button, use value in selectlist or type your custom class | `multilist` | `-1` = - Custom -<br />`btn` = Plain<br />`btn btn-primary` = Primary<br />`btn btn-success` = Success<br />`btn btn-info` = Info<br />`btn btn-warning` = Warning<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn` (Plain) |
| **Custom class**<br />`flexi_button_class_advanced_custom` | Add custom class for this button, like uk-button uk-button-large for a warp 7 template | `text` | — | — |
| **Position**<br />`link_to_advsearch_pos` | Position of the button relative to the search box | `radio` | `right` = Right<br />`left` = Left<br />`top` = Top<br />`bottom` = Bottom | `right` (Right) |

## Auto-complete

Configuration of the search suggestions (simple auto-complete). The rich display below is used by the simple auto-complete only.

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use auto-complete**<br />`search_autocomplete` | Select to use multi-word tag-like autocomplete, or a simpler single word or disable it | `radio` | `0` = No<br />`1` = Simple<br />`2` = Tag-Like | `1` (Simple) |
| **Suggestion list width**<br />`search_ac_dropdown_width` | CSS width of the auto-complete suggestion dropdown. Leave empty to match the search input width. Examples: 40rem, 600px, 90vw, min(40rem, calc(100vw - 2rem)). The width is automatically capped to the viewport. Applies to both the simple and tag-like auto-complete. | `text` | — | — |

#### Rich suggestions

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable rich suggestions**<br />`search_ac_rich` | Add an image and extra content fields to the item title suggestions | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Image source**<br />`search_ac_image_source` | Use the first image found in the item text, an image from a FLEXIcontent image field, or the image field set in the content type of each suggested item (Content type -&gt; Search view) | `multilist` | `auto` = Extract from item text<br />`field` = FLEXIcontent image field<br />`type` = Use type settings | `auto` (Extract from item text) |
| **Image field**<br />`search_ac_image_field` | Select the FLEXIcontent image field to use when the image source is 'FLEXIcontent image field' | `fields` | — | — |
| **Image width**<br />`search_ac_image_width` | Width of the suggestion thumbnail in pixels | `number` | — | `60` |
| **Image height**<br />`search_ac_image_height` | Height of the suggestion thumbnail in pixels | `number` | — | `60` |
| **Image resize method**<br />`search_ac_image_method` | Scale keeps the whole image, crop fills the configured width and height | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Image position**<br />`search_ac_image_position` | Position of the image relative to the title and fields | `radio` | `left` = Left<br />`right` = Right | `left` (Left) |
| **Title maximum length**<br />`search_ac_title_maxlen` | Maximum number of characters displayed for the title, cut at a word boundary. Set 0 for no limit. The full title is still used when searching. | `number` | — | `60` |
| **Extra fields source**<br />`search_ac_info_source` | Use the fields listed below for all suggestions, or the extra fields set in the content type of each suggested item (Content type -&gt; Search view) | `multilist` | `module` = Fields selected below<br />`type` = Use type settings | `module` (Fields selected below) |
| **Extra fields**<br />`search_ac_info_fields` | Select fields one by one to display them next to the image. Drag the added fields to set their display order. Values are rendered as plain text. | `fields` | — | — |
| **Show field labels**<br />`search_ac_info_labels` | Display the field label before its value | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Field value maximum length**<br />`search_ac_info_maxlen` | Maximum number of characters displayed for each field value, cut at a word boundary. Set 0 for no limit. | `number` | — | `80` |

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

### Caching

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Caching**<br />`cache` | Select whether to cache the content of this module. | `list` | `1` = Use global<br />`0` = No caching | `1` (Use global) |
| **Cache Time**<br />`cache_time` | The time before the module is recached. | `text` | — | `900` |

### CSS / JS

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add css**<br />`add_ccs` | Add the module default css file | `radio` | `—` = Use component setting<br />`0` = No<br />`1` = Yes<br />`2` = CSS links inside HTML (allows capturing) | — |
| **Add tooltips JS**<br />`add_tooltips` | Add the tooltips JS behavior from Joomla to display the nice tooltips in frontend. | `radio` | `—` = Use component setting<br />`0` = No<br />`1` = Yes | — |

### Module Container

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Module Class Suffix**<br />`moduleclass_sfx` | A suffix to be applied to the css class of the module, this allows individual module styling. | `text` | — | — |
