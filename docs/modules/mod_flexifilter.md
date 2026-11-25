---
sidebar_position: 6
---

# Item filters

FLEXIcontent provides six frontend modules for displaying items, categories, search forms, filters, maps and tag clouds. Configure a module from **Extensions → Modules**.

> This module displays a form that filters the item listing of category-based views (category, author, tags, etc)

:::info Source
This page is generated from `modules/mod_flexifilter/mod_flexifilter.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

### Template Layout

:::note
Please set layout parameters in **Layout: ... TAB**. CSS/HTML developers please read: ** Custom templates HOW-TO **
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout**<br />`layout` | Choose a layout to render your module | `fclayout` | — | `default` |
| **Scroll To Module**<br />`scroll_to_anchor_tag` | Enable this to scroll to module on page load | `radio` | `0` = No<br />`1` = Yes<br />`2` = When active filters | `0` (No) |

### Target Category

:::note
Specific Category (no category selector shown) or Default Category for Category Selector or Select none to filter the category of current category view
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category Specific OR Default OR none(=Current)**<br />`catid` | -- a specific category the filter form will submit to (no category selector shown), -- OR the default category, preselected in category selector, -- OR select none to filter category of current category view | `fccategory` | — | — |
| **Menu item category view**<br />`cat_itemid` | Enter the category menu item to use for listing items NOTE 1: this is recommended if you have multiple menu items pointing to the category, which may have different filtering options (e.g. list only 'featured' flagged items) NOTE 2: menu item must point to above category, otherwise wrong or no items will be listed | `fcmenuitem` | `—` = Click to select | — |

#### Category selector

:::note
NOTE 1: this replaces the category filter NOTE 2: single or multiple value allowed, this depends on target view (set below)
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show selector**<br />`display_cat_list` | Show the category selector for selecting one or more categories for filtering | `multilist` | `0` = NO (Use single selected or current category)<br />`1` = YES (include selected categories)<br />`2` = YES (exclude selected categories) | `0` (NO (Use single selected or current category)) |
| **Categories**<br />`catids` | You can limit category selector to specific categories or exclude specific categories. Select none to display all categories the user can see. | `flexicategories` | — | — |
| **Include subcategories**<br />`usesubcats` | Allow usage of all subcategories of the selected categories. This way you don't have to edit the field every time a new subcategory is created. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Target view single category / multi categories / etc

:::note
This effects if category selector will allow selecting multiple categories
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Form target**<br />`mcats_selection` | Select the view that the filtering form will target, either category view or multi-category view or ... other. In the case **single category view the menu item will be auto-selected**, but in the case of **multi-category view** (mcats) you should set a menu item of type multi-category to be used, this way you can define the layout, behaviour, etc parameters of the target multi category view ... | `multilist` | `0` = Category view (menu item auto-selected)<br />`1` = Multi-category view (set menu item below) | `0` (Category view (menu item auto-selected)) |
| **Menu item multi-category view**<br />`mcats_itemid` | The menu item of type multi-category view (mcats), so that you can configure the view (layout, behaviour, etc). Please set this correctly, otherwise wrong or no items will be listed | `fcmenuitem` | `—` = Click to select | — |

### Form (Text Search / Field Filters)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Form placement**<br />`ff_placement` | Select how the form container will be placed/opened | `multilist` | `0` = Inline<br />`1` = Slider | `0` (Inline) |
| **Text of Form toggle button**<br />`ff_toggle_search_title` | The text of button/link for opening/displaying the search form, default is 'Search' | `text` | — | `FLEXI_TOGGLE_SEARCH_FORM_MODULE` (Search) |
| **Auto-submit**<br />`filter_autosubmit` | Submit form automatically when a filter changes. If you do not enable this, then users will be able to set many filters before submitting the form. **NOTE:** Some filter may auto-submit the form despite this setting | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Use ajax filter**<br />`filter_ajax` | Set yes for filtering your page without reloading | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Filter Badge**<br />`badge_position` | Display your filter value like a badge, no display nothing, top display it before search form and bottom after submit button | `fcradio` | `0` = No<br />`1` = Top<br />`2` = Bottom | `2` (Bottom) |
| **Instructions**<br />`filter_instructions` | Display filter form usage instructions. You can create joomla language overrides for the language strings to give custom instructions to your users | `radio` | `0` = Hide<br />`1` = Yes, as popup Tooltip<br />`2` = Yes, as inline Text | `1` (Yes, as popup Tooltip) |

#### Buttons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Go Button**<br />`show_search_go` | Submit form reloading current listing, **Note**: that this will submit text search, field filters and alpha index (when any of these is present) | `multilist` | `0` = Automatic<br />`1` = Show | `1` (Show) |
| **Go class**<br />`flexi_button_class_go` | Class for Go button, use value in selectlist or tip your custom class | `multilist` | `-1` = - Custom -<br />`btn` = Plain<br />`btn btn-primary` = Primary<br />`btn btn-success` = Success<br />`btn btn-info` = Info<br />`btn btn-warning` = Warning<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn btn-success` (Success) |
| **Custom class**<br />`flexi_button_class_go_custom` | Add custom class for go button, like uk-button uk-button-large for a warp 7 template | `text` | — | — |
| **Reset Button**<br />`show_search_reset` | Clear form reloading current listing, **Note**: Note that this will also clear field filters and alpha index (when any of these is present) | `multilist` | `0` = Hide<br />`1` = Show | `1` (Show) |
| **Reset class**<br />`flexi_button_class_reset` | Class for Go button, use value in selectlist or tip your custom class | `multilist` | `-1` = - Custom -<br />`btn` = Plain<br />`btn btn-primary` = Primary<br />`btn btn-success` = Success<br />`btn btn-info` = Info<br />`btn btn-warning` = Warning<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn` (Plain) |
| **Custom class**<br />`flexi_button_class_reset_custom` | Add custom class for reset button, like uk-button uk-button-large for a warp 7 template | `text` | — | — |

### Text Search

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use search box**<br />`use_search` | Display search box in this category view | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show Label**<br />`show_search_label` | You may want to hide label or display label inside the text search input to save space | `radio` | `0` = Hide<br />`1` = Outside input<br />`2` = Inside input | `1` (Outside input) |
| **Use auto-complete**<br />`search_autocomplete` | Select to use multi-word tag-like autocomplete, or a simpler single word or disable it | `radio` | `0` = No<br />`1` = Simple<br />`2` = Tag-Like | `1` (Simple) |
| **Word Combination**<br />`show_searchphrase` | Allow users to select method of combining the search words, e.g. phrase, phrase (more results), all words, any words, exact phrase | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |
| **Default combination**<br />`default_searchphrase` | Default (preselected) method of combining the search words | `radio` | `all` = All words<br />`any` = Any words<br />`exact` = Exact phrase<br />`natural` = Phrase<br />`natural_expanded` = Phrase, more results | `all` (All words) |

### Field Filters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display filters**<br />`use_filters` | Enable to display field filters. NOTE, you can define the filter appearance and behaviour by editing the configuration of every individual field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Displayed filters**<br />`display_filter_list` | Filters that will be displayed | `multilist` | `0` = ALL (allowed in any category)<br />`1` = Set in category parameters<br />`2` = Selected bellow<br />`3` = Selected bellow & set in category parameters | `0` (ALL (allowed in any category)) |
| **Select filters**<br />`filters` | Select the filters you wish to load for this category view. | `filters` | — | — |
| **Filter labels**<br />`show_filter_labels` | Display all filter labels (=field names), this will automatically override the 'show filter label' setting of each individual filter | `radio` | `0` = Field configured behavior<br />`1` = Outside Filter<br />`2` = Inside Filter | `1` (Outside Filter) |
| **Initial Filter values**<br />`initial_filters` | These are the initial values of the filters, user can override them. Enter like: field_id##value %% field_id##value %% e.g. 22##14 %% 47##some field value %% 19##someword for ranges use field_id##value1---value2 for multiple values use field_id##value1+++value2+++value3 NOTE: your field must be configured to be range filter or multi-value filter or the values will not be used as expected | `textarea` | — | — |
| **Display filter in slide**<br />`fc_filter_in_slide` | Display filter in seperate slide | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Filter enclosings

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **One record per row**<br />`filter_placement` | Select how the records will be placed: -- Display a single record per row, or -- Use a custom separator | `radio` | `2` = Yes, but filter below label<br />`1` = Yes<br />`0` = No, use separator<br />`3` = Place in tabs | `1` (Yes) |
| **Record Separator ignored when placing records per row**<br />`filter_separatorf` | Choose a separator to separate the records (placed between records). **NOTE:**This setting is ignored when placing records per row | `list` | `0` = Space<br />`1` = Line break<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters) | `0` (Space) |
| **Prefix text of every record**<br />`filter_pretext` | This text is placed immediately **before** every record | `text` | — | — |
| **Suffix text of every record**<br />`filter_posttext` | This text is placed immediately **after** every record | `text` | — | — |
| **Opening text for record list**<br />`filter_opentag` | This applied once at the START of the record list. It is meant to create the starting HTML of the record list, but above you can choose to place it as SEPARATING text of the records too. But prefer to use parameters: **Prefix/Suffix text of records** | `text` | — | — |
| **Closing text for record list**<br />`filter_closetag` | This applied once at the END of the record list. It is meant to create the ending HTML of the record list, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of records** | `text` | — | — |

### Locked Filters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use locked filters**<br />`use_persistent_filters` | Filters that can NOT be overriden by user, **NOTE:** These maybe hidden or you may choose to display them (user input will be prohibited) | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Locked Filter values**<br />`persistent_filters` | Enter like: field_id##value %% field_id##value %% e.g. 22##14 %% 47##some field value %% 19##someword for ranges use field_id##value1---value2 for multiple values use field_id##value1+++value2+++value3 NOTE: your field must be configured to be range filter or multi-value filter or the values will not be used as expected | `textarea` | — | — |

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
| **Caching**<br />`cache` | Select whether to cache the content of this module. | `list` | `0` = No caching | `0` (No caching) |

### CSS / JS

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add css**<br />`add_ccs` | Add the module default css file | `radio` | `—` = Use component setting<br />`0` = No<br />`1` = Yes<br />`2` = CSS links inside HTML (allows capturing) | — |
| **Add tooltips JS**<br />`add_tooltips` | Add the tooltips JS behavior from Joomla to display the nice tooltips in frontend. | `radio` | `—` = Use component setting<br />`0` = No<br />`1` = Yes | — |

### Module Container

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Module Class Suffix**<br />`moduleclass_sfx` | A suffix to be applied to the css class of the module, this allows individual module styling. | `text` | — | — |
