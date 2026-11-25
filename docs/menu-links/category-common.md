---
sidebar_position: 2
---

# Category views — common options

Options shared by all category-based menu item types: category, multi-category, author, tagged, favourites and my items.

:::info Source
This page is generated from `site/views/category/tmpl/default.xml` and the official FLEXIcontent 5.x language files.
:::

## Required parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Please select a category**<br />`cid` | Select the category you wish to display | `fccategory` | — | `0` |

## Override view parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Start to add parents categories at depth**<br />`item_depth` | You can set the category tree depth, at which adding of parent category links to the pathway should start. **NOTE:** Inside FLEXIcontent Advanced Route - System Plugin, you can select to disable the adding of categories to the pathway for specific item CONTENT TYPES | `multilist` | `0` = root<br />`1` = level 1<br />`2` = level 2<br />`3` = level 3<br />`4` = level 4<br />`5` = level 5 | `0` (root) |

### Category Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Override Configuration**<br />`override_defaultconf` | Default Category Configuration will be used (recommended in most cases), unless you -enable- this override and thus use configuration in this menu item. | `multilist` | `0` = No, use defaults<br />`1` = Yes | `0` (No, use defaults) |

## Parameters

#### Cats params set

### Category image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Image**<br />`image` | Select an image for the category | `fcmedia` | — | — |
| **Alternative text**<br />`image_alt` | — | `text` | — | — |

### Lists: Header

#### Header

### Buttons

#### Page buttons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Print Method**<br />`print_behaviour` | Select to automatically open browser print dialog, or display a print button inside the page | `fcradio` | `—` = Use Global<br />`auto` = Automatic<br />`button` = Button | — |
| **Print Icon**<br />`show_print_icon` | Enable Print screen | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Email Icon**<br />`show_email_icon` | Enable emailing current page URL to a friend | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Feed Icon**<br />`show_feed_icon` | Enable previewing of current page feeds in a popup window. This will also make subscribing easier for your visitors | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Feed head link**<br />`show_feed_link` | Enable this to insert an RSS feed link inside the HTML Head. This make possible for browsers and RSS readers to discover your RSS feeds and subscribe to them | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **CSV Export button**<br />`show_csvbutton` | Enable CSV Export functionality | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |

#### Add new item

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Button**<br />`show_addbutton` | Enables display of **Add new item** button to categories and **lists**, that the currently logged user can add | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Show to unauthorized**<br />`nonauth_addbutton` | Enable this to show add (submit) button to unauthorized users. If you do this, then remember that: -- unless the chosen submit menu item allows UNAUTHORIZED users to submit a. **guest** users are redirected to **login/register** screen b. **uauthorized logged** users are redirected to URL configured in - component settings, overidden by url in - content type settings, overidden by url in - submit menu item | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes, exclude guests<br />`2` = Yes | — |
| **Submit menu item**<br />`addbutton_menu_itemid` | You may want to force a specific submit menu item, so that custom configuration is used, e.g. limit to specific content type(s). **NOTE 1**: In case you want to allow specific content type for specific categories, you should deny 'create items' ACL privilege to the users in each type configuration, thus they will be able to submit only via content TYPE OVERRIDE in the submit menu item. **NOTE 2**: You may also want to override category ACL too | `fcmenuitem` | `—` = Use Global | — |

#### Customize

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Icons**<br />`show_icons` | Print, Email, PDF, etc. will utilize Icons or Text | `fcradio` | `—` = Use Global<br />`0` = Text<br />`1` = Icons<br />`2` = Both | — |
| **Icon type**<br />`use_font_icons` | You may display icons as images or as using an installed font-based icon set | `fcradio` | `—` = Use Global<br />`0` = Image<br />`1` = Font icons | — |
| **Preset configurations**<br />`font_icon_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`0` = Use component settings (clear)<br />`1` = Load defaults & customize | — |
| **Font icons**<br />`font_icon_classes` | Use comma separated list, to load defaults and see the format, leave parameter empty and save | `textarea` | — | — |

#### Placement of buttons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Place inside dropdown**<br />`btn_grp_dropdown` | Display buttons as drop down, typically this will use bootstrap or similar, and it may not be ignored by custom templates | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Dropdown button icon**<br />`btn_grp_dropdown_class` | Icon of the dropdown button | `text` | — | — |

### Category information

:::note
Layout file: **%s**
:::

### Category Information

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category title**<br />`show_cat_title` | Show/hide the title of the category | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Title maximum length**<br />`title_cut_text` | Item titles having more characters than this value will be trimmed and appended with ... | `text` | — | — |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category image**<br />`show_description_image` | Show/Hide the category image | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Image source**<br />`cat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | `fcradio` | `—` = Use Global<br />`0` = Extract from description<br />`1` = Use image parameter<br />`2` = Try parameter then extract | — |
| **Link image**<br />`cat_link_image` | Open the item when clicking on the image | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Processing method**<br />`cat_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `fcradio` | `—` = Use Global<br />`0` = Scale<br />`1` = Crop | — |
| **Image width**<br />`cat_image_width` | Image width | `text` | — | — |
| **Image height**<br />`cat_image_height` | Image height | `text` | — | — |

#### Description

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category Description**<br />`show_description` | Show/Hide the Category Description | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Trigger content plugins**<br />`trigger_onprepare_content_cat` | Enable this option if you want to trigger content plugins (onPrepareContent) on the category description. Keep in mind not every plugin will work outside com_content. | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

### Sub-categories list

:::note
Layout file: **%s**
:::

### Sub-categories (1st sub-level)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Sub-categories**<br />`show_subcategories` | Show/Hide the sub-categories | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Category List Order**<br />`subcat_orderby` | Ordering of the Category List, available options depend on the category properties available e.g. category name, backend confiured ordering, etc | `multilist` | `—` = Use Global<br />`date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified - Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most views first<br />`rhits` = Popularity -- Least views first<br />`order` = Category 's ordering attribute<br />`random` = Random | — |

#### Categories Information

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Items count**<br />`show_itemcount` | Show/Hide the items count of each sub-category | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show<br />`2` = Show with label | — |
| **Sub category count**<br />`show_subcatcount` | Show/Hide the sub-categories count of each sub-category | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show<br />`2` = Show with label | — |
| **Empty categories (needs item count enabled)**<br />`show_empty_cats` | Show/Hide categories that have no items. NOTE: this works when item counting is enabled | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category image**<br />`show_description_image_subcat` | Show/Hide the category image | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Image source**<br />`subcat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | `fcradio` | `—` = Use Global<br />`0` = Extract from description<br />`1` = Use image parameter<br />`2` = Try parameter then extract | — |
| **Link image**<br />`subcat_link_image` | Open the item when clicking on the image | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Processing method**<br />`subcat_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `fcradio` | `—` = Use Global<br />`0` = Scale<br />`1` = Crop | — |
| **Image width**<br />`subcat_image_width` | Image width | `text` | — | — |
| **Image height**<br />`subcat_image_height` | Image height | `text` | — | — |

#### Description

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category Description**<br />`show_description_subcat` | Show/Hide the Category Description | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Category description maximum length**<br />`description_cut_text_subcat` | Category descriptions having more characters than this value will be trimmed and appended with ... | `text` | — | — |

#### Category list

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **List label**<br />`show_label_subcats` | Display a label before the sub-categories list **NOTE:** If both sub-category images and descriptions are disabled then the label and the list of records will be placed inside 'inline' containers | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Preset configurations**<br />`prx_sfx_open_close_configs_subcat` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
| **Prefix text of every record**<br />`subcat_pretext` | This text is placed immediately **before** every record | `text` | — | — |
| **Suffix text of every record**<br />`subcat_posttext` | This text is placed immediately **after** every record | `text` | — | — |
| **Record Separator**<br />`subcat_separatorf` | Choose a separator to separate the records (placed between records) | `multilist` | `—` = Use Global<br />`0` = Space<br />`1` = Line break<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters) | — |
| **Opening text for record list**<br />`subcat_opentag` | This applied once at the START of the record list. It is meant to create the starting HTML of the record list, but above you can choose to place it as SEPARATING text of the records too. But prefer to use parameters: **Prefix/Suffix text of records** | `text` | — | — |
| **Closing text for record list**<br />`subcat_closetag` | This applied once at the END of the record list. It is meant to create the ending HTML of the record list, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of records** | `text` | — | — |

### Peer-Categories list

:::note
Layout file: **%s**
:::

### Peer-Categories (same-level)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Peer-categories**<br />`show_peercategories` | Show/Hide the peer-categories | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Category List Order**<br />`peercat_orderby` | Ordering of the Category List, available options depend on the category properties available e.g. category name, backend confiured ordering, etc | `multilist` | `—` = Use Global<br />`date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified - Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most views first<br />`rhits` = Popularity -- Least views first<br />`order` = Category 's ordering attribute<br />`random` = Random | — |

#### Categories Information

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Items count**<br />`show_itemcount_peercat` | Show/Hide the items count of each peer-category | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show<br />`2` = Show with label | — |
| **Sub category count**<br />`show_subcatcount_peercat` | Show/Hide the sub categories count of each peer-category | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show<br />`2` = Show with label | — |
| **Empty categories (needs item count enabled)**<br />`show_empty_peercats` | Show/Hide categories that have no items. NOTE: this works when item counting is enabled | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category image**<br />`show_description_image_peercat` | Show/Hide the category image | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Image source**<br />`peercat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | `fcradio` | `—` = Use Global<br />`0` = Extract from description<br />`1` = Use image parameter<br />`2` = Try parameter then extract | — |
| **Link image**<br />`peercat_link_image` | Open the item when clicking on the image | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Processing method**<br />`peercat_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `fcradio` | `—` = Use Global<br />`0` = Scale<br />`1` = Crop | — |
| **Image width**<br />`peercat_image_width` | Image width | `text` | — | — |
| **Image height**<br />`peercat_image_height` | Image height | `text` | — | — |

#### Description

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category Description**<br />`show_description_peercat` | Show/Hide the Category Description | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Category description maximum length**<br />`description_cut_text_peercat` | Category descriptions having more characters than this value will be trimmed and appended with ... | `text` | — | — |

#### Category list

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **List label**<br />`show_label_peercats` | Display a label before the peer-categories list **NOTE:** If both sub-category images and descriptions are disabled then the label and the list of records will be placed inside 'inline' containers | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Preset configurations**<br />`prx_sfx_open_close_configs_peercat` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
| **Prefix text of every record**<br />`peercat_pretext` | This text is placed immediately **before** every record | `text` | — | — |
| **Suffix text of every record**<br />`peercat_posttext` | This text is placed immediately **after** every record | `text` | — | — |
| **Record Separator**<br />`peercat_separatorf` | Choose a separator to separate the records (placed between records) | `multilist` | `—` = Use Global<br />`0` = Space<br />`1` = Line break<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters) | — |
| **Opening text for record list**<br />`peercat_opentag` | This applied once at the START of the record list. It is meant to create the starting HTML of the record list, but above you can choose to place it as SEPARATING text of the records too. But prefer to use parameters: **Prefix/Suffix text of records** | `text` | — | — |
| **Closing text for record list**<br />`peercat_closetag` | This applied once at the END of the record list. It is meant to create the ending HTML of the record list, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of records** | `text` | — | — |

#### Header

### Search / Filter form

#### Search / Filter form

### Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Form placement**<br />`ff_placement` | Select how the form container will be placed/opened | `multilist` | `—` = Use Global<br />`0` = Inline<br />`1` = Slider | — |
| **Form toggle title**<br />`ff_toggle_search_title` | The button/link title for toggling the search form via click, default is 'Search' | `text` | — | — |
| **Auto-submit**<br />`filter_autosubmit` | Submit form automatically when a filter changes. If you do not enable this, then users will be able to set many filters before submitting the form. **NOTE:** Some filter may auto-submit the form despite this setting | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Instructions**<br />`filter_instructions` | Display filter form usage instructions. You can create joomla language overrides for the language strings to give custom instructions to your users | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Yes, as popup tooltip<br />`2` = Yes, as inline text | — |

#### Buttons

:::note
Go Button
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Go Button**<br />`show_search_go` | Submit form reloading current listing, **Note**: that this will submit text search, field filters and alpha index (when any of these is present) | `multilist` | `—` = Use Global<br />`0` = Automatic<br />`1` = Show | — |
| **Go class**<br />`flexi_button_class_go` | Class for Go button, use value in selectlist or tip your custom class | `multilist` | `—` = Use Global<br />`-1` = - Custom -<br />`btn` = Plain<br />`btn btn-primary` = Primary<br />`btn btn-success` = Success<br />`btn btn-info` = Info<br />`btn btn-warning` = Warning<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | — |
| **Custom class**<br />`flexi_button_class_go_custom` | Add custom class for go button, like uk-button uk-button-large for a warp 7 template | `text` | — | — |

:::note
Reset Button
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Reset Button**<br />`show_search_reset` | Clear form reloading current listing, **Note**: Note that this will also clear field filters and alpha index (when any of these is present) | `multilist` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Reset class**<br />`flexi_button_class_reset` | Class for Go button, use value in selectlist or tip your custom class | `multilist` | `—` = Use Global<br />`-1` = - Custom -<br />`btn` = Plain<br />`btn btn-primary` = Primary<br />`btn btn-success` = Success<br />`btn btn-info` = Info<br />`btn btn-warning` = Warning<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | — |
| **Custom class**<br />`flexi_button_class_reset_custom` | Add custom class for reset button, like uk-button uk-button-large for a warp 7 template | `text` | — | — |

#### Text Search / Filters enclosings

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Prefix text of every record**<br />`filter_pretext` | This text is placed immediately **before** every record | `text` | — | — |
| **Suffix text of every record**<br />`filter_posttext` | This text is placed immediately **after** every record | `text` | — | — |
| **Opening text for record list**<br />`filter_opentag` | This applied once at the START of the record list. It is meant to create the starting HTML of the record list, but above you can choose to place it as SEPARATING text of the records too. But prefer to use parameters: **Prefix/Suffix text of records** | `text` | — | — |
| **Closing text for record list**<br />`filter_closetag` | This applied once at the END of the record list. It is meant to create the ending HTML of the record list, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of records** | `text` | — | — |
| **One record per row**<br />`filter_placement` | Select how the records will be placed: -- Display a single record per row, or -- Use a custom separator | `fcradio` | `—` = Use Global<br />`0` = No, use separator<br />`1` = Yes<br />`2` = Yes, but filter below label<br />`3` = Place in tabs | — |
| **Record Separator ignored when placing records per row**<br />`filter_separatorf` | Choose a separator to separate the records (placed between records). **NOTE:**This setting is ignored when placing records per row | `multilist` | `—` = Use Global<br />`0` = Space<br />`1` = Line break<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters) | — |

### Text Search

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use search**<br />`use_search` | Display a text search box | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Show Label**<br />`show_search_label` | You may want to hide label or display label inside the text search input to save space | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Outside input<br />`2` = Inside input | — |
| **Word Combination**<br />`show_searchphrase` | Allow users to select method of combining the search words, e.g. phrase, phrase (more results), all words, any words, exact phrase | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Default combination**<br />`default_searchphrase` | Default (preselected) method of combining the search words | `fcradio` | `—` = Use Global<br />`all` = All words<br />`any` = Any words<br />`exact` = Exact phrase<br />`natural` = Phrase<br />`natural_expanded` = Phrase, more results | — |
| **Use auto-complete**<br />`search_autocomplete` | Select to use multi-word tag-like auto-complete, or a simpler auto-complete method or disable auto-complete altogether | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Simple<br />`2` = Tag-Like | — |

### Field Filters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display filters**<br />`use_filters` | Enable to display field filters. NOTE, you can define the filter appearance and behaviour by editing the configuration of every individual field | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Display filter in slide**<br />`fc_filter_in_slide` | Display each fielter value in individual slide panel | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | `0` (No) |
| **Filter order**<br />`filters_order` | Select the order that the filters will be displayed | `fcradio` | `—` = Use Global<br />`0` = Default (Fields manager)<br />`1` = Custom (below) | — |
| **Select filters**<br />`filters` | Select the filters you wish to load for this category view. | `filters` | — | — |
| **Filter labels**<br />`show_filter_labels` | Display all filter labels (=field names), this will automatically override the 'show filter label' setting of each individual filter | `fcradio` | `—` = Use Global<br />`0` = Field configured behavior<br />`1` = Outside Filter<br />`2` = Inside Filter | — |
| **Initial Filter values**<br />`initial_filters` | These are the initial values of the filters, user can override them. Enter like: field_id##value %% field_id##value Example: 22##14 %% 47##some field value %% 19##someword - **Single values**: field_id##value1 - **Ranges**: field_id##value1---value2 - **Multiple values**: field_id##value1+++value2+++value3 - **Relation / Reverse-relation**: REL_field_id##REL_ITEM_field_id~~value1 - **Date offset ranges**: field_id##now-50d---now+50d (use d for days, m for months, y for years) e.g. dates up to now: 45##---now+0d NOTE: your field must be configured to be range filter or multi-value filter or the values will not be used as expected | `textarea` | — | — |

#### Locked Filters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use locked filters**<br />`use_persistent_filters` | Filters that can NOT be overridden by user, **NOTE:** These maybe hidden or you may choose to display them (user input will be prohibited) | `multilist` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Locked Filter values**<br />`persistent_filters` | Filters that can NOT be overridDen by user. Enter like: field_id##value %% field_id##value Example: 22##14 %% 47##some field value %% 19##someword - **Single values**: field_id##value1 - **Ranges**: field_id##value1---value2 - **Multiple values**: field_id##value1+++value2+++value3 - **Relation / Reverse-relation**: REL_field_id##REL_ITEM_field_id~~value1 - **Date offset ranges**: field_id##now-50d---now+50d (use d for days, m for months, y for years) e.g. dates up to now: 45##---now+0d NOTE: your field must be configured to be range filter or multi-value filter or the values will not be used as expected | `textarea` | — | — |

### Alpha Index

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show alpha index**<br />`show_alpha` | Show/Hide the alphabetical index | `alphaindex` | — | — |
| **Custom Alpha Index List**<br />`alphacharacters` | Define a custom Alpha Index list of character entities (single character / ranges / lists / aliases) Use comma(,) to separate character entities, and use double exclamation mark(!!) to separate character groups. **Example**: [default]=a,b,c,def,g,h,k-n,opq,r-z !! 0,1,2,3,4-9 Use character # to specify all numbers and use minus(-) to define ranges, and put characters together with no comma to make aggregations. For per language use [shortlang]= e.g. [fr]=#,a,b,c,...,z [en]=#,a,b,c,d,...x,y,z [default]=0-9,a-c,d,e... WITHOUT new line characters | `textarea` | — | `[default]=a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z!!0,1,2,3,4,5,6,7,8,9` |
| **CSS classes for AI character groups**<br />`alphagrpcssclasses` | The CSS classes for the box around the above described Alpha Index character groups e.g. if you have 4 groups you can use: letters!!numbers!!letters!!letters . NOTE that letters and numbers are predefined any other class you must define yourself | `textarea` | — | `letters!!numbers` |
| **Custom AI character separator**<br />`alphacharseparator` | Instead of boxes around the characters entities, this separator will be used, e.g. or '-' or ',' Leave blank to use default style, to use special characters like '¦' please use &#166; | `text` | — | — |
| **Custom AI Character Aliases**<br />`alphaaliases` | A single character or word will represent the specified character entity (e.g. range/list/etc). **e.g. Specify like:** A~aAäÄ!!O~oOöÖ!!U~uUüÜ **1. Separate aliases with:** !! **2. For each alias** the part before ~ is aliasname, AND the part after ~ is character entity (range/list/etc) -- Include here aliases of all languages that you use. **NOTE:** DO NOT add aliases for just lowercase/uppercase letters e.g. t~tT **is not needed**, but if you make an alias then you must include both lowercase and upperCase letters | `text` | — | — |
| **Skip empty AI characters**<br />`alphaskipempty` | Do not show at all the unused (grayed and disabled) Alpha Index characters entities | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

#### Search / Filter form

### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category layout**<br />`clayout` | Set a specific category layout for this category | `categorylayout` | — | — |
| **Mobile Layout**<br />`clayout_mobile` | Set a layout to be used when it is detected that current visitor is browsing from a mobile device and also have resolution below the configured minimum, by default the - normal - template is used | `categorylayout` | — | — |

:::note
About template parameters
Please note you cannot set template parameters here. Template parameters for the choosen template will be retrieved from the template configuration (then inherited from category configuration). For fields shown, please add your fields in layout positions in template configuration management tab
:::

### Layout switcher

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display**<br />`clayout_switcher` | Enable to allow frontend user to switch item list (category) layout. NOTE: selecting zero allowed templates, will disable the switcher | `multilist` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Appearance**<br />`clayout_switcher_display_mode` | Select how the layout switcher will be displayed | `multilist` | `—` = Use Global<br />`0` = Drop-down select<br />`1` = Radio-image | — |
| **Label**<br />`clayout_switcher_label` | — | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Before<br />`2` = Inside | — |
| **Displayed layouts -- None displays none --**<br />`displayed_clayouts` | These are the allowed templates for the layout selector **NOTE:** Every template has one category layout, so this list contains template names **NOTE:** This is especially useful if you want to allow **layout** selection for frontend users, but also for reducing the size of the selection list **NOTE:** Every category or view may override these | `clayoutlist` | — | — |

#### URL / Links

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allowed layouts -- None allows all --**<br />`allowed_clayouts` | These are the allowed templates via URL **NOTE:** Every template has one category layout, so this list contains template names **NOTE:** This is especially useful if you want to allow **layout** selection for frontend users, but also for reducing the size of the selection list **NOTE:** Every category or view may override these | `clayoutlist` | — | — |

### Items List

:::note
Layout file: **%s**
:::

#### Items List

### Basic display, Ordering

#### Override **Item Type** settings

:::note
Avoid enabling this, unless you know, that you need **2 or more** ways to display the same items
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item layout**<br />`ilayout` | Item typically use the layout defined in their item type. You can override this for item links created inside the pages of this view. Note that item links not created inside this view will still use the layout defined in their item type !!! | `itemlayout` | — | — |

### Basic Display

:::note
Note: these settings are meant for every listed item, and are different than similar settings may exist for item view
:::

### Basic Display

:::note
Note: these settings are meant for every listed item, and are different than similar settings may exist for item view
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Edit button**<br />`show_editbutton_lists` | Enables display of Item Edit button for all items that the currently logged user can edit | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Link to frontend<br />`2` = Link to backend | — |
| **State button**<br />`show_state_icon_lists` | Enable quick change of publication state via an AJAX state selector button | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **(Permanent) Delete button**<br />`show_deletebutton_lists` | Enables display of Item Delete button for all items that the currently logged user can delete. NOTE this is not a trash button, instead it permanently removes the item | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Comments counter**<br />`show_comments_count` | Show the number of comments written for each item | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Show Title**<br />`show_title_lists` | Show/Hide the items title | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Title linkable**<br />`link_titles_lists` | If Yes, the Title of Items will be hyperlinked to the item itself. | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Force Full (main) Text**<br />`force_full` | Full (main) Text is used to present the content in full view and is the text after the 'readmore' separator, you can choose here whether to show it when the content is displayed in **category** and other multi-item listings, thus appending it after content's introductory text | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **FLEXI_Read_More_Link**<br />`show_readmore` | If set to Show, the Read more... link will show if Main text has been created for the Item. | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show<br />`-1` = Show always | — |

### Item Ordering (Level 1)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby` | Order items by CORE fields/properties | `fcordering` | — | — |

#### CUSTOM field ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`orderbycustomfield` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Custom field**<br />`orderbycustomfieldid` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | `fields` | — | — |
| **Direction**<br />`orderbycustomfielddir` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `fcradio` | `—` = Use Global<br />`ASC` = Ascending<br />`DESC` = Descending | — |
| **Ordering Method**<br />`orderbycustomfieldint` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `fcradio` | `—` = Use Global<br />`0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date<br />`4` = Download hits | — |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

### Item Ordering (Level 2)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby_2nd` | Order items by CORE fields/properties | `fcordering` | — | — |

#### CUSTOM field ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`orderbycustomfield_2nd` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Custom field**<br />`orderbycustomfieldid_2nd` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | `fields` | — | — |
| **Direction**<br />`orderbycustomfielddir_2nd` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `fcradio` | `—` = Use Global<br />`ASC` = Ascending<br />`DESC` = Descending | — |
| **Ordering Method**<br />`orderbycustomfieldint_2nd` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `fcradio` | `—` = Use Global<br />`0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date<br />`4` = Download hits | — |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

#### Frontend Overrides

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Ordering selector (Level 1)**<br />`orderby_override` | Enable to display frontend ordering selector (Level 1) | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Ordering selector (Level 2)**<br />`orderby_override_2nd` | Enable to display frontend ordering selector (Level 2) | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |

#### Select Available Options

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page allowed to frontend user**<br />`limit_options` | Please enter a comma separated list of number, leave empty to use Global Defaults | `text` | — | — |
| **Order options (Level 1) allowed to frontend user**<br />`orderby_options` | Please select the ordering options you wish to allow. **NOTE:** (a) **Preconfigured initial order**, is order configured in categories configuration, (b)** Content 's ordering attribute** is for current category, since there is one such order for every category assigned to the item | `fccheckbox` | — | — |
| **Custom Order (Level 1) allowed to frontend user**<br />`orderby_custom` | Please enter the custom fields that you wish to allow as ordering options. Format is (use COMMA separate multiple cases): fieldid:[alpha\|int\|decimal\|date]:[asc\|desc] or fieldid:[alpha\|int\|decimal\|date]:[asc\|desc]:language_string or file_fieldid:file_hits:[asc\|desc]:language_string e.g. (remember: use COMMA for multiple choices) 45:num:desc, 57:decimal:asc:LANG_PRICE_LOWEST, 61:alpha:asc, 62:file_hits:desc:LANG_MOST_DOWNLOADED | `textarea` | — | — |
| **Order options (Level 2) allowed to frontend user**<br />`orderby_options_2nd` | Please select the ordering options you wish to allow. **NOTE:** (a) **Preconfigured initial order**, is order configured in categories configuration, (b)** Content 's ordering attribute** is for current category, since there is one such order for every category assigned to the item | `fccheckbox` | — | — |
| **Custom Order (Level 2) allowed to frontend user**<br />`orderby_custom_2nd` | Please enter the custom fields that you wish to allow as ordering options. Format is (use COMMA separate multiple cases): fieldid:[alpha\|int\|decimal\|date]:[asc\|desc] or fieldid:[alpha\|int\|decimal\|date]:[asc\|desc]:language_string or file_fieldid:file_hits:[asc\|desc]:language_string e.g. (remember: use COMMA for multiple choices) 45:num:desc, 57:decimal:asc:LANG_PRICE_LOWEST, 61:alpha:asc, 62:file_hits:desc:LANG_MOST_DOWNLOADED | `textarea` | — | — |

### Item selection, Pagination

### Item selection, Pagination

:::note
Select items
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Unauthorised items**<br />`show_noauth` | Content items not authorized to be viewable by current guest or logged user will be included in the item lists (category-based views and search view). When a user tries to access the detailed view of any authorized content, then non-logged users will be asked to log-in, and already logged users will receive a HTTP 403 Access Forbidden Errors. **NOTE:** If you enable this feature then you should also set into the parameter 'Unauthorized Page' with the URL of the page to be displayed for these errors | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Owned items**<br />`show_owned` | Enable to list items owned / authored by currently logged user - regardless of their state, - regardless of being scheduled or expired (publish up /down dates) | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Trashed items**<br />`show_trashed` | Enable to list items trashed items to privileged users. That is users that have the 'Ignore items state' ACL privilege | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Subcategories items**<br />`display_subcategories_items` | Display items from subcategories of current category | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = 1st sublevel<br />`2` = All sublevels | — |
| **Filter items using current language**<br />`filtercat` | Only the items of current language will be displayed | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

#### Limit / suppress items

:::note
Limits -before- text-search, filtering, alpha-indexing
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_limit_before_search_filt` | — | `multilist` | `—` = Use Global<br />`0` = No<br />`1` = Yes<br />`2` = Featured Only | — |
| **# per page**<br />`limit_before_search_filt` | Number of items per page | `text` | — | — |

:::note
Limits -after- text-search, filtering, alpha-indexing
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Marked via flag**<br />`display_flag_featured` | Some of the category items are flagged as featured. Select to show (a) both normal and featured items, (b) normal only, (c) featured only | `fcradio` | `—` = Use Global<br />`0` = Both<br />`1` = Normal only<br />`2` = Featured Only | — |
| **# per page**<br />`limit` | Number of items per page | `text` | — | — |

:::note
Limits by custom fields: please set 'Locked Filters' in the 'Search / Filter Form' tab
:::

### # per page

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Infinit scrolling**<br />`infinite_scroll` | Allow to load more item in categorie view without relaoding page. No = classic pagination. Load more = display a load more button editable with language string. Scrolling = load item automaticly on scroll down user. Load more and scrolling option disable pagination with number. | `fcradio` | `—` = Use Global<br />`0` = No Classic<br />`1` = Load more button<br />`2` = Infinit scrolling | — |
| **Show items total**<br />`show_item_total` | This will display the total number items in the category (according to category display configuration and current filtering) | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **# per page**<br />`show_pagination` | Show/Hide pagination, such as links and page counting | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show<br />`2` = FLEXI_Auto | — |
| **Pagination's results (current # / total pages)**<br />`show_pagination_results` | (when pagination is enabled), you can use this option to disable the display of current active page number and total number for pages | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |

#### Frontend Overrides

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page**<br />`limit_override` | Number of items per page | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **'Per page' label**<br />`limit_override_label` | Add label inside or outside the selector, or choose not to display the label | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Before<br />`2` = Inside | — |

### Item markings

:::note
Content/Content List Markings featured categories, view access, recently created, etc
:::

### Category Markings

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add Marking**<br />`mu_addcss_cats` | Add an empty span box with an appropriate CSS classes. Please examine HTML output to find the CSS classname | `fccheckbox` | — | — |
| **Add text (Category title)**<br />`mu_addtext_cats` | Select when the category title will be added inside the marking **NOTE:** This is recommend for non-developers and for multi-language sites, since featured category titles will be language filtered (language strings) | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

### Access Level Markings (for viewing content)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add Marking**<br />`mu_addcss_acclvl` | Add an empty span box with an appropriate CSS classes. Please examine HTML output to find the CSS classname | `fccheckbox` | — | — |
| **Add Obtained Levels**<br />`mu_add_condition_obtainded_acc` | Add markings for obtained (access) level always or only when a content item is viewable. **EXPLANATION:** A content item has access level for (a) itself, (b) its main category, (c) its content type. One for these access levels might not be assigned to current user, so item is unviewable, you can select whether to add markings (markups) for other access level of the item already obtained by current user. | `fcradio` | `—` = Use Global<br />`0` = Only if item viewable<br />`1` = Always | — |
| **Add Text**<br />`mu_addtext_acclvl` | You may select to add text inside the marking box. These include: no access, free (public) access and access level names, **NOTE:** This is recommend for non-developers and for multi-language sites, since all these will be language filtered (language strings) | `fccheckbox` | — | — |
| **Custom no access text**<br />`mu_no_acc_text` | Default text is 'No Access'. You can set a custom language string here, e.g. 'Restricted', 'Members Only' | `text` | — | — |
| **Custom free access text**<br />`mu_free_acc_text` | Default text is 'Free'. You can set a custom language string here, e.g. 'Public', 'Everyone' | `text` | — | — |

### Recently ADDED marking

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add Marking**<br />`mu_addcss_radded` | Add an empty span box with an appropriate CSS classes. Please examine HTML output to find the CSS classname | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Add text (Timeframe name)**<br />`mu_addtext_radded` | Add the timeframe name inside the marking box. **NOTE:** This is recommend for non-developers and for multi-language sites, since these will be language filtered (language strings) | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

#### Timeframes Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Timeframe intervals**<br />`mu_ra_timeframe_intervals` | These is a comma separated list of integer time intervals. e.g. write 48h to enter in hours or 2d to specify interval in days | `text` | — | — |
| **Timeframe names**<br />`mu_ra_timeframe_names` | These is a comma separated list of language strings. These are matched with the above timeframes one to one, in the same order as entered above | `textarea` | — | — |

### Recently UPDATED markings

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add Marking**<br />`mu_addcss_rupdated` | Add an empty span box with an appropriate CSS classes. Please examine HTML output to find the CSS classname | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Add text (Timeframe name)**<br />`mu_addtext_rupdated` | Add the timeframe name inside the marking box. **NOTE:** This is recommend for non-developers and for multi-language sites, since these will be language filtered (language strings) | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

#### Timeframes Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Timeframe intervals**<br />`mu_ru_timeframe_intervals` | These is a comma separated list of integer time intervals. e.g. write 48h to enter in hours or 2d to specify interval in days | `text` | — | — |
| **Timeframe names**<br />`mu_ru_timeframe_names` | These is a comma separated list of language strings. These are matched with the above timeframes one to one, in the same order as entered above | `textarea` | — | — |

### Options

:::note
Note: These are used in **category view**, but if you set same settings in **type configuration** (of the item) to 'Use global', -- then these will also be used in **item view**
:::

#### Seo

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Create pathway automatically**<br />`automatic_pathways` | Category and item pathway (displayed by breadcrumbs module) will be created automatically by (a) removing all menu items from the pathway and adding to it the tree path of category titles and the item title. NOTE you can override this setting per category, type and item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Rel canonical tag**<br />`add_canonical` | Add a rel canonical meta tag into the source code of your pages, this helps search engines identify a page being viewed via different URLs, and give it better rank, by not indexing it multiple times | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Microdata type for items**<br />`microdata_itemtype_cat` | This will be used for items that do not have a microdata type configured in their type or in their atomic item parameters. MICRODATA allow search engines to categorize your content appropriately, improving SEO of your pages | `microdatatype` | — | — |

#### Comments

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable comments integration**<br />`comments` | Enable commenting system integration. **NOTE:** This parameter may be overridden for types, categories, single items or menu items. **NOTE:** By setting to disable you may manually trigger (description field will trigger all by default), appropriate Joomla content plugin of your commenting system to insert comments via a Joomla CONTENT Event. In case of adding comments this way, you cannot use the parameter 'Disable comments' in the item form, instead you will need to do it the way your commenting system recommends, e.g. by inserting some special text inside the description | `fcradio` | `—` = Use Global<br />`0` = Disable or integrate manually<br />`1` = JComments | — |

#### Items List

### RSS Feeds

### RSS Feeds

:::note
Note: Enable RSS feeds in tab '%s'
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page**<br />`feed_limit` | Number of items per page | `text` | — | — |
| **For each feed item show**<br />`feed_summary` | Select if you want to show only the Introtext or the full text of your Item within the generated Feed. | `fcradio` | `—` = Use Global<br />`0` = Intro text<br />`1` = Full Text | — |
| **Maximum length of text**<br />`feed_summary_cut` | Item text longer than this value will be cut off | `text` | — | — |
| **FLEXI_Read_More_Link**<br />`feed_show_readmore` | If set to Show, the Read more... link will show if Main text has been created for the Item. | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |

### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use image**<br />`feed_use_image` | Extract the first image from the text or use the above field | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Link image**<br />`feed_link_image` | Open the item when clicking on the image | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Image source**<br />`feed_image_source` | Select the source of the image. You can either choose an image field (if available) or automatically extract the first image found in the main text. | `fcimage` | — | — |
| **Image size**<br />`feed_image_size` | Image size desc | `fcradio` | `—` = Use parameters<br />`s` = Small<br />`m` = Medium<br />`l` = Large | — |
| **Image width**<br />`feed_image_width` | Image width | `text` | — | — |
| **Image height**<br />`feed_image_height` | Image height | `text` | — | — |
| **Processing method**<br />`feed_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `fcradio` | `—` = Use Global<br />`0` = Scale<br />`1` = Crop | — |

### Custom fields

:::note
Do not add fields that will break feeds display
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Fields list**<br />`feed_extra_fields` | Fields that requires extra CSS/JS will not work properly, fields that might be suitable are fields like e.g. date,text,select,etc. Enter a comma separated list of field names | `textarea` | — | — |

### Item Ordering (Level 1)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`feed_orderby` | Order items by CORE fields/properties | `fcordering` | — | — |

#### CUSTOM field ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`feed_orderbycustomfield` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Custom field**<br />`feed_orderbycustomfieldid` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | `fields` | — | — |
| **Direction**<br />`feed_orderbycustomfielddir` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `fcradio` | `—` = Use Global<br />`ASC` = Ascending<br />`DESC` = Descending | — |
| **Ordering Method**<br />`feed_orderbycustomfieldint` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `fcradio` | `—` = Use Global<br />`0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date<br />`4` = Download hits | — |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

### Item Ordering (Level 2)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`feed_orderby_2nd` | Order items by CORE fields/properties | `fcordering` | — | — |

#### CUSTOM field ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`feed_orderbycustomfield_2nd` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Custom field**<br />`feed_orderbycustomfieldid_2nd` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | `fields` | — | — |
| **Direction**<br />`feed_orderbycustomfielddir_2nd` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `fcradio` | `—` = Use Global<br />`ASC` = Ascending<br />`DESC` = Descending | — |
| **Ordering Method**<br />`feed_orderbycustomfieldint_2nd` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `fcradio` | `—` = Use Global<br />`0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date<br />`4` = Download hits | — |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

#### Cats params set
