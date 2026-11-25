---
sidebar_position: 11
---

# Search



:::info Source
This page is generated from `site/views/search/tmpl/default.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

:::note
Please note these reasons for some results not being included: - you have not enabled short word search in component and word is &lt; 4 characters - word is too common e.g. appears in about half of the articles - wrong language or article not publish or article has expired
:::

### Search Form

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Form placement**<br />`form_placement` | Set yes to display advanced search view with 2 columns, filter on right and result on left. | `multilist` | `0` = Top<br />`1` = Left<br />`2` = Right | `1` (Left) |
| **Column width**<br />`column_width` | set width of column for left and right position _10%_ | `text` | — | `20%` |
| **Column gap**<br />`column_gap` | set gapp between colum and results _2rem or 15px or 10%_ | `text` | — | `2rem` |
| **Selector display**<br />`selectors_display_as` | Display content types as | `radio` | `select` = Dropdown Select<br />`checkboxes` = Checkboxes list | `select` (Dropdown Select) |

#### Content Types

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show Label**<br />`show_type_label` | You may want to hide label or display label inside the content types search | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Searchable Types **(Select NONE for -ALL-)****<br />`contenttypes` | The content types the search will include, selecting none will include ALL. NOTE: You can allow user to select Content Types. If you do then the selection list will be LIMITED to display ONLY the types specified here | `types` | — | — |
| **Allow user selection**<br />`canseltypes` | Allow users to select content types they want to include in their search | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Text Search

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show Label**<br />`show_search_label` | You may want to hide label or display label inside the text search input to save space | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Outside input<br />`2` = Inside input | — |
| **Word Combination**<br />`show_searchphrase` | Allow users to select method of combining the search words, e.g. phrase, phrase with guessing relevant, all, any, exact phrase | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Default combination**<br />`default_searchphrase` | Default (preselected) method of combining the search words | `radio` | `—` = Use Global<br />`all` = All words<br />`any` = Any words<br />`exact` = Exact phrase<br />`natural` = Phrase<br />`natural_expanded` = Phrase, more results | — |
| **Use auto-complete**<br />`search_autocomplete` | Select to use multi-word tag-like auto-complete, or a simpler auto-complete method or disable auto-complete altogether | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Simple<br />`2` = Tag-Like | — |
| **Word Min Length**<br />`minchars` | Minimum character length that search words are allowed to have | `text` | — | `3` |
| **Word Max Length**<br />`maxchars` | Maximum characters length that search words are allowed to have | `text` | — | `200` |

#### Buttons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Buttons position**<br />`buttons_position` | Buttons position desc | `radio` | `0` = Buttons position after search<br />`1` = Buttons position after advsearch | `0` (Buttons position after search) |
| **Buttons append**<br />`append_buttons` | Buttons append desc | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

:::note
Go Button
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Go class**<br />`flexi_button_class_go` | Class for Go button, use value in selectlist or tip your custom class | `multilist` | `—` = Use Global<br />`-1` = - Custom -<br />`btn` = Plain<br />`btn btn-primary` = Primary<br />`btn btn-success` = Success<br />`btn btn-info` = Info<br />`btn btn-warning` = Warning<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn btn-warning` (Warning) |
| **Custom class**<br />`flexi_button_class_go_custom` | Add custom class for go button, like uk-button uk-button-large for a warp 7 template | `text` | — | — |

:::note
Reset Button
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Reset Button**<br />`show_search_reset` | Clear form reloading current listing, **Note**: Note that this will also clear field filters and alpha index (when any of these is present) | `multilist` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Reset class**<br />`flexi_button_class_reset` | Class for Go button, use value in selectlist or tip your custom class | `multilist` | `—` = Use Global<br />`-1` = - Custom -<br />`btn` = Plain<br />`btn btn-primary` = Primary<br />`btn btn-success` = Success<br />`btn btn-info` = Info<br />`btn btn-warning` = Warning<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | — |
| **Custom class**<br />`flexi_button_class_reset_custom` | Add custom class for reset button, like uk-button uk-button-large for a warp 7 template | `text` | — | — |

#### Advanced Options

#### Category selector

:::note
NOTE: single or multiple value allowed, this depends on target view (set below)
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show selector**<br />`display_cat_list` | Show selector | `multilist` | `0` = No (Use single selected or current category)<br />`1` = Yes (Include selected categories)<br />`2` = Yes (Exclude selected categories) | `0` (No (Use single selected or current category)) |
| **Categories**<br />`catids` | Categories | `flexicategories` | — | — |
| **Include subcategories**<br />`usesubcats` | Include subcategories | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default Option Text (e.g. All colours)**<br />`search_firstoptiontext_s` | Text of first option of the Drop-Down Select e.g. 'All colours' or All etc. **NOTE**: This option has no value **NOTE**: This text is language-filtered so you can enter a language replaceable string | `text` | — | `FLEXI_ALL` (All) |

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
| **Fields **(Leave EMPTY for -ALL-)****<br />`txtflds` | NOTE: only fields marked as advanced index text-searchable are listed | `filters` | — | — |
| **Fields as filters**<br />`show_filters` | Enable this to use specific fields as filters | `multilist` | `0` = Use all filterable<br />`1` = According to type<br />`2` = Configure below | `1` (According to type) |
| **Fields **(Leave EMPTY for -ALL-)****<br />`filtflds` | NOTE: only fields marked as advanced index filters are listed | `filters` | — | — |
| **Display filter in slide**<br />`disp_slide_filter` | Display each fielter value in individual slide panel | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Filter Badge**<br />`badge_position` | Display your filter value like a badge, no display nothing, top display it before search form and bottom after submit button | `radio` | `0` = No<br />`1` = Top | `0` (No) |

#### Search Areas (non-FC Content)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use areas**<br />`show_searchareas` | Allow the user to select and search other areas of the website content, e.g. like weblinks, user contacts, etc | `multilist` | `0` = Disable<br />`1` = Enable, show selector | `0` (Disable) |
| **Search Areas**<br />`searchareas` | The site's (non-FC content) search areas, that the search will include. NOTE: if user is allowed to select Search Areas, then the selection list will be LIMITED to display ONLY the search areas selected here | `radio` | `—` = All | — |
| **Show ordering**<br />`show_searchordering` | Allow frontend users to select ordering of results of other areas of the website content. NOTE this is different ordering from the ordering used for main content results. | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Default value**<br />`default_searchordering` | Default ordering for sorting the results of the search | `radio` | `newest` = Newest first<br />`oldest` = Oldest first<br />`popular` = Most popular<br />`alpha` = Alphabetical<br />`category` = Section/Category | `newest` (Newest first) |

### Results List

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **# per page**<br />`limit` | Number of items per page | `text` | — | `10` |

#### Basic Information (used by non-FC results too)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show section**<br />`show_section` | Display content section for each result, e.g. 'weblinks', 'contacts' etc, plus category tree of it. | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show context **(Always ON for non-FC results)****<br />`show_text` | Display search words found along with content text around them. The search words found are highlighted | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Context Limit ** (# of characters) ****<br />`text_chars` | Number of characters of content text shown of around each found search word | `text` | — | `240` |
| **Show creation date**<br />`show_date` | Display for each result its creation date. By default the setting of the content type of each result is used (Content type -&gt; Search view), choose Yes / No to override it for all types | `radio` | `—` = From content type<br />`0` = No<br />`1` = Yes | — |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use image**<br />`fcr_use_image` | Extract the first image from the text or use the above field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Image source**<br />`fcr_image` | By default the image field set in the content type of each result is used (Content type -&gt; Search view). Select a field, or the main text, to override it for all types | `fcimage` | — | — |
| **Image position**<br />`fcr_position` | The image position in the block. | `radio` | `0` = Left<br />`1` = Right | `0` (Left) |
| **Link image**<br />`fcr_link_image` | Open the item when clicking on the image | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Intro image size**<br />`fcr_image_size` | Size of the intro images | `list` | `—` = Use parameters<br />`s` = Small<br />`m` = Medium<br />`l` = Large | — |
| **Image width**<br />`fcr_width` | Image width | `text` | — | `180` |
| **Image height**<br />`fcr_height` | Image height | `text` | — | `180` |
| **Processing method**<br />`fcr_method` | Processing method | `radio` | `0` = Scale<br />`1` = Crop | `0` (Scale) |

#### Display Fields (Render their HTML)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Extra Fields**<br />`use_infoflds` | Display extra fields for each result. By default the fields set in the content type of each result are used (Content type -&gt; Search view). Choose Yes to use the list below for all types, or No to display no extra fields | `multilist` | `—` = From content type<br />`0` = No<br />`1` = Yes | — |
| **Select Field**<br />`info_fieldlist` | Please select one by one fields to add to textarea below. | `fields` | — | — |
| **Fields **(Leave EMPTY for -NONE-)****<br />`infoflds` | Enter Fields (their fieldnames) to render their values and display them in the search results. You can separate each fieldname by comma(,). | `textarea` | — | — |

### Items Ordering

#### Item Ordering (Level 1)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby` | Order items by CORE fields/properties | `fcordering` | — | — |

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
| **Order by CORE field/properties**<br />`orderby_2nd` | Order items by CORE fields/properties | `fcordering` | — | — |

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

### FC Advanced Search plugin: **Override Configuration**

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Search Limit**<br />`search_limit` | Limit maximum number of results the plugin can return, | `text` | — | — |
| **Language Filter**<br />`filter_lang` | Return content having current language only | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Search archived**<br />`search_archived` | Also include archive items into the search | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Browser Navigator**<br />`browsernav` | Browser Navigator | `radio` | `—` = Use Global<br />`1` = Open New Window<br />`2` = Open Same Window | — |
