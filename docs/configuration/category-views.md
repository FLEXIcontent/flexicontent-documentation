---
sidebar_position: 6
---

# Category views

Display settings for category and multi-category list views: filters, sorting, links, pagination and more.

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

### Category-based views

#### Category, Author items, My items, Multi-category view, Tags, Favourites

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **List all (via ACL)**<br />`use_list_items_in_any_state_acl` | Enable this to allow privileged users (ACL privilege: 'list items in any state') and super admins to see ANY state items and items that are scheduled and/or expired. | — | `0` |
| **Inherit parameters from**<br />`inheritcid` | Inherit parameters from a specific category **NOTE:** Set your parameters to 'Use Global' or to empty in order for heritage to work **NOTE:** Heritage from specific category is single level, thus it does not cascade to inherit from any further categories **NOTE:** Heritage from parent categories is multi-level, thus it cascades to inherit up to parent category not inheriting from its parent | — | `-1` |
| **Debug heritage**<br />`debug_inheritcid` | Display information in frontend category views about the order that parameters are overridden | — | `0` |

#### FLEXI_LISTS

## Category image

:::note
These are default values if the category or menu item does not set them
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Image**<br />`image` | Select an image for the category | — | — |
| **Alternative text**<br />`image_alt` | — | — | — |

## Lists: Header

#### Lists: Header

## Buttons

:::note
Note: you can configure more buttons at top level TAB '%s'
:::

#### Add new item

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Button**<br />`show_addbutton` | Enables display of **Add new item** button to categories and **lists**, that the currently logged user can add | — | `1` |
| **Show to unauthorized**<br />`nonauth_addbutton` | Enable this to show add (submit) button to unauthorized users. If you do this, then remember that: -- unless the chosen submit menu item allows UNAUTHORIZED users to submit a. **guest** users are redirected to **login/register** screen b. **uauthorized logged** users are redirected to URL configured in - component settings, overidden by url in - content type settings, overidden by url in - submit menu item | — | `0` |
| **Submit menu item**<br />`addbutton_menu_itemid` | You may want to force a specific submit menu item, so that custom configuration is used, e.g. limit to specific content type(s). **NOTE 1**: In case you want to allow specific content type for specific categories, you should deny 'create items' ACL privilege to the users in each type configuration, thus they will be able to submit only via content TYPE OVERRIDE in the submit menu item. **NOTE 2**: You may also want to override category ACL too | — | — |

## Category information

:::note
Layout file: **%s**
:::

### Category Information

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Category title**<br />`show_cat_title` | Show/hide the title of the category | — | `1` |
| **Title maximum length**<br />`title_cut_text` | Item titles having more characters than this value will be trimmed and appended with ... | — | `200` |

#### Image

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Category image**<br />`show_description_image` | Show/Hide the category image | — | `0` |
| **Image source**<br />`cat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | — | `2` |
| **Link image**<br />`cat_link_image` | Open the item when clicking on the image | — | `1` |
| **Processing method**<br />`cat_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | — | `1` |
| **Image width**<br />`cat_image_width` | Image width | — | `80` |
| **Image height**<br />`cat_image_height` | Image height | — | `80` |

#### Description

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Category Description**<br />`show_description` | Show/Hide the Category Description | — | `1` |
| **Trigger content plugins**<br />`trigger_onprepare_content_cat` | Enable this option if you want to trigger content plugins (onPrepareContent) on the category description. Keep in mind not every plugin will work outside com_content. | — | `1` |

## Sub-categories list

:::note
Layout file: **%s**
:::

### Sub-categories (1st sub-level)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Sub-categories**<br />`show_subcategories` | Show/Hide the sub-categories | — | `0` |
| **Category List Order**<br />`subcat_orderby` | Ordering of the Category List, available options depend on the category properties available e.g. category name, backend confiured ordering, etc | — | `order` |

#### Categories Information

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Items count**<br />`show_itemcount` | Show/Hide the items count of each sub-category | — | `1` |
| **Sub category count**<br />`show_subcatcount` | Show/Hide the sub-categories count of each sub-category | — | `0` |
| **Empty categories (needs item count enabled)**<br />`show_empty_cats` | Show/Hide categories that have no items. NOTE: this works when item counting is enabled | — | `1` |

#### Image

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Category image**<br />`show_description_image_subcat` | Show/Hide the category image | — | `0` |
| **Image source**<br />`subcat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | — | `2` |
| **Link image**<br />`subcat_link_image` | Open the item when clicking on the image | — | `1` |
| **Processing method**<br />`subcat_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | — | `1` |
| **Image width**<br />`subcat_image_width` | Image width | — | `24` |
| **Image height**<br />`subcat_image_height` | Image height | — | `24` |

#### Description

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Category Description**<br />`show_description_subcat` | Show/Hide the Category Description | — | `0` |
| **Category description maximum length**<br />`description_cut_text_subcat` | Category descriptions having more characters than this value will be trimmed and appended with ... | — | `120` |

#### Category list

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **List label**<br />`show_label_subcats` | Display a label before the sub-categories list **NOTE:** If both sub-category images and descriptions are disabled then the label and the list of records will be placed inside 'inline' containers | — | `1` |
| **Preset configurations**<br />`prx_sfx_open_close_configs_subcat` | This is a list of preset configurations, after loading them, you can click custom again to customize them | — | — |
| **Prefix text of every record**<br />`subcat_pretext` | This text is placed immediately **before** every record | — | — |
| **Suffix text of every record**<br />`subcat_posttext` | This text is placed immediately **after** every record | — | — |
| **Record Separator**<br />`subcat_separatorf` | Choose a separator to separate the records (placed between records) | — | `0` |
| **Opening text for record list**<br />`subcat_opentag` | This applied once at the START of the record list. It is meant to create the starting HTML of the record list, but above you can choose to place it as SEPARATING text of the records too. But prefer to use parameters: **Prefix/Suffix text of records** | — | — |
| **Closing text for record list**<br />`subcat_closetag` | This applied once at the END of the record list. It is meant to create the ending HTML of the record list, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of records** | — | — |

## Peer-Categories list

:::note
Layout file: **%s**
:::

### Peer-Categories (same-level)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Peer-categories**<br />`show_peercategories` | Show/Hide the peer-categories | — | `1` |
| **Category List Order**<br />`peercat_orderby` | Ordering of the Category List, available options depend on the category properties available e.g. category name, backend confiured ordering, etc | — | `order` |

#### Categories Information

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Items count**<br />`show_itemcount_peercat` | Show/Hide the items count of each sub-category | — | `0` |
| **Sub category count**<br />`show_subcatcount_peercat` | Show/Hide the sub categories count of each peer-category | — | `0` |
| **Empty categories (needs item count enabled)**<br />`show_empty_peercats` | Show/Hide categories that have no items. NOTE: this works when item counting is enabled | — | `1` |

#### Image

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Category image**<br />`show_description_image_peercat` | Show/Hide the category image | — | `0` |
| **Image source**<br />`peercat_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | — | `2` |
| **Link image**<br />`peercat_link_image` | Open the item when clicking on the image | — | `1` |
| **Processing method**<br />`peercat_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | — | `1` |
| **Image width**<br />`peercat_image_width` | Image width | — | `24` |
| **Image height**<br />`peercat_image_height` | Image height | — | `24` |

#### Description

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Category Description**<br />`show_description_peercat` | Show/Hide the Category Description | — | `0` |
| **Category description maximum length**<br />`description_cut_text_peercat` | Category descriptions having more characters than this value will be trimmed and appended with ... | — | `120` |

#### Category list

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **List label**<br />`show_label_peercats` | Display a label before the peer-categories list **NOTE:** If both sub-category images and descriptions are disabled then the label and the list of records will be placed inside 'inline' containers | — | `1` |
| **Preset configurations**<br />`prx_sfx_open_close_configs_peercat` | This is a list of preset configurations, after loading them, you can click custom again to customize them | — | — |
| **Prefix text of every record**<br />`peercat_pretext` | This text is placed immediately **before** every record | — | — |
| **Suffix text of every record**<br />`peercat_posttext` | This text is placed immediately **after** every record | — | — |
| **Record Separator**<br />`peercat_separatorf` | Choose a separator to separate the records (placed between records) | — | `0` |
| **Opening text for record list**<br />`peercat_opentag` | This applied once at the START of the record list. It is meant to create the starting HTML of the record list, but above you can choose to place it as SEPARATING text of the records too. But prefer to use parameters: **Prefix/Suffix text of records** | — | — |
| **Closing text for record list**<br />`peercat_closetag` | This applied once at the END of the record list. It is meant to create the ending HTML of the record list, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of records** | — | — |

#### Lists: Header

## Search / Filter form

#### Search / Filter form

## Basic

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Form placement**<br />`ff_placement` | Select how the form container will be placed/opened | — | `0` |
| **Form toggle title**<br />`ff_toggle_search_title` | The button/link title for toggling the search form via click, default is 'Search' | — | `FLEXI_TOGGLE_SEARCH_FORM` (Search) |
| **Auto-submit**<br />`filter_autosubmit` | Submit form automatically when a filter changes. If you do not enable this, then users will be able to set many filters before submitting the form. **NOTE:** Some filter may auto-submit the form despite this setting | — | `1` |
| **Use ajax search**<br />`filter_ajax` | Set yes to use search and filtering without page reloading. Note its only compatible with new templates | — | `0` |
| **Filter Badge**<br />`badge_position` | Display your filter value like a badge, no display nothing, top display it before search form and bottom after submit button | — | `2` |
| **Instructions**<br />`filter_instructions` | Display filter form usage instructions. You can create joomla language overrides for the language strings to give custom instructions to your users | — | `1` |

#### Buttons

:::note
Go Button
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Go Button**<br />`show_search_go` | Submit form reloading current listing, **Note**: that this will submit text search, field filters and alpha index (when any of these is present) | — | `0` |
| **Go class**<br />`flexi_button_class_go` | Class for Go button, use value in selectlist or tip your custom class | — | `btn btn-success` |
| **Custom class**<br />`flexi_button_class_go_custom` | Add custom class for go button, like uk-button uk-button-large for a warp 7 template | — | — |

:::note
Reset Button
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Reset Button**<br />`show_search_reset` | Clear form reloading current listing, **Note**: Note that this will also clear field filters and alpha index (when any of these is present) | — | `1` |
| **Reset class**<br />`flexi_button_class_reset` | Class for Go button, use value in selectlist or tip your custom class | — | `btn` |
| **Custom class**<br />`flexi_button_class_reset_custom` | Add custom class for reset button, like uk-button uk-button-large for a warp 7 template | — | — |

#### Text Search / Filters enclosings

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Prefix text of every record**<br />`filter_pretext` | This text is placed immediately **before** every record | — | — |
| **Suffix text of every record**<br />`filter_posttext` | This text is placed immediately **after** every record | — | — |
| **Opening text for record list**<br />`filter_opentag` | This applied once at the START of the record list. It is meant to create the starting HTML of the record list, but above you can choose to place it as SEPARATING text of the records too. But prefer to use parameters: **Prefix/Suffix text of records** | — | — |
| **Closing text for record list**<br />`filter_closetag` | This applied once at the END of the record list. It is meant to create the ending HTML of the record list, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of records** | — | — |
| **One record per row**<br />`filter_placement` | Select how the records will be placed: -- Display a single record per row, or -- Use a custom separator | — | `0` |
| **Record Separator ignored when placing records per row**<br />`filter_separatorf` | Choose a separator to separate the records (placed between records). **NOTE:**This setting is ignored when placing records per row | — | `0` |

## Text Search

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use search**<br />`use_search` | Display a text search box | — | `1` |
| **Show Label**<br />`show_search_label` | You may want to hide label or display label inside the text search input to save space | — | `1` |
| **Use auto-complete**<br />`search_autocomplete` | Select to use multi-word tag-like auto-complete, or a simpler auto-complete method or disable auto-complete altogether | — | `1` |
| **Word Combination**<br />`show_searchphrase` | Allow users to select method of combining the search words, e.g. phrase, phrase (more results), all words, any words, exact phrase | — | `0` |
| **Default combination**<br />`default_searchphrase` | Default (preselected) method of combining the search words | — | `all` |

## Field Filters

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Display filters**<br />`use_filters` | Enable to display field filters. NOTE, you can define the filter appearance and behaviour by editing the configuration of every individual field | — | `0` |
| **Display filter in slide**<br />`fc_filter_in_slide` | Display each fielter value in individual slide panel | — | `0` |
| **Filter order**<br />`filters_order` | Select the order that the filters will be displayed | — | `1` |
| **Select filters**<br />`filters` | Select the filters you wish to load for this category view. | — | — |
| **Filter labels**<br />`show_filter_labels` | Display all filter labels (=field names), this will automatically override the 'show filter label' setting of each individual filter | — | `1` |
| **Initial Filter values**<br />`initial_filters` | These are the initial values of the filters, user can override them. Enter like: field_id##value %% field_id##value Example: 22##14 %% 47##some field value %% 19##someword - **Single values**: field_id##value1 - **Ranges**: field_id##value1---value2 - **Multiple values**: field_id##value1+++value2+++value3 - **Relation / Reverse-relation**: REL_field_id##REL_ITEM_field_id~~value1 - **Date offset ranges**: field_id##now-50d---now+50d (use d for days, m for months, y for years) e.g. dates up to now: 45##---now+0d NOTE: your field must be configured to be range filter or multi-value filter or the values will not be used as expected | — | — |

#### Locked Filters

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use locked filters**<br />`use_persistent_filters` | Filters that can NOT be overridden by user, **NOTE:** These maybe hidden or you may choose to display them (user input will be prohibited) | — | `0` |
| **Locked Filter values**<br />`persistent_filters` | Filters that can NOT be overridDen by user. Enter like: field_id##value %% field_id##value Example: 22##14 %% 47##some field value %% 19##someword - **Single values**: field_id##value1 - **Ranges**: field_id##value1---value2 - **Multiple values**: field_id##value1+++value2+++value3 - **Relation / Reverse-relation**: REL_field_id##REL_ITEM_field_id~~value1 - **Date offset ranges**: field_id##now-50d---now+50d (use d for days, m for months, y for years) e.g. dates up to now: 45##---now+0d NOTE: your field must be configured to be range filter or multi-value filter or the values will not be used as expected | — | — |

## Alpha Index

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Show alpha index**<br />`show_alpha` | Show/Hide the alphabetical index | — | `1` |
| **Custom Alpha Index List**<br />`alphacharacters` | Define a custom Alpha Index list of character entities (single character / ranges / lists / aliases) Use comma(,) to separate character entities, and use double exclamation mark(!!) to separate character groups. **Example**: [default]=a,b,c,def,g,h,k-n,opq,r-z !! 0,1,2,3,4-9 Use character # to specify all numbers and use minus(-) to define ranges, and put characters together with no comma to make aggregations. For per language use [shortlang]= e.g. [fr]=#,a,b,c,...,z [en]=#,a,b,c,d,...x,y,z [default]=0-9,a-c,d,e... WITHOUT new line characters | — | `[default]=a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z!!0,1,2,3,4,5,6,7,8,9` |
| **CSS classes for AI character groups**<br />`alphagrpcssclasses` | The CSS classes for the box around the above described Alpha Index character groups e.g. if you have 4 groups you can use: letters!!numbers!!letters!!letters . NOTE that letters and numbers are predefined any other class you must define yourself | — | `letters!!numbers` |
| **Custom AI character separator**<br />`alphacharseparator` | Instead of boxes around the characters entities, this separator will be used, e.g. or '-' or ',' Leave blank to use default style, to use special characters like '¦' please use &#166; | — | — |
| **Custom AI Character Aliases**<br />`alphaaliases` | A single character or word will represent the specified character entity (e.g. range/list/etc). **e.g. Specify like:** A~aAäÄ!!O~oOöÖ!!U~uUüÜ **1. Separate aliases with:** !! **2. For each alias** the part before ~ is aliasname, AND the part after ~ is character entity (range/list/etc) -- Include here aliases of all languages that you use. **NOTE:** DO NOT add aliases for just lowercase/uppercase letters e.g. t~tT **is not needed**, but if you make an alias then you must include both lowercase and upperCase letters | — | — |
| **Skip empty AI characters**<br />`alphaskipempty` | Do not show at all the unused (grayed and disabled) Alpha Index characters entities | — | `0` |

#### Search / Filter form

## Layout

### Layout

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Default category layout**<br />`clayout` | The chosen category layout of the selected template will be used, unless the category / content listing view / URL overrides it | — | `grid` |
| **Mobile Layout**<br />`clayout_mobile` | Set a layout to be used when it is detected that current visitor is browsing from a mobile device and also have resolution below the configured minimum, by default the - normal - template is used | — | — |
| **LESS include folders**<br />`less_folders` | Folders to monitor for changes. - If any files are changed, then LESS re-compiling will be triggered. NOTE: You may use replacements like: JPATH_* ACTIVE_JTEMPLATE_SITE LANG_TAG and LANG_SHORT_TAG | — | `JPATH_COMPONENT_SITE/assets/less/ ::
JTEMPLATE_SITE/less/com_flexicontent/ ::
` |

### Layout switcher

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Display**<br />`clayout_switcher` | Enable to allow frontend user to switch item list (category) layout. NOTE: selecting zero allowed templates, will disable the switcher | — | `1` |
| **Appearance**<br />`clayout_switcher_display_mode` | Select how the layout switcher will be displayed | — | `1` |
| **Label**<br />`clayout_switcher_label` | — | — | `0` |
| **Displayed layouts -- None displays none --**<br />`displayed_clayouts` | These are the allowed templates for the layout selector **NOTE:** Every template has one category layout, so this list contains template names **NOTE:** This is especially useful if you want to allow **layout** selection for frontend users, but also for reducing the size of the selection list **NOTE:** Every category or view may override these | — | — |

#### URL / Links

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Allowed layouts -- None allows all --**<br />`allowed_clayouts` | These are the allowed templates via URL **NOTE:** Every template has one category layout, so this list contains template names **NOTE:** This is especially useful if you want to allow **layout** selection for frontend users, but also for reducing the size of the selection list **NOTE:** Every category or view may override these | — | — |

## Items List

:::note
Layout file: **%s**
:::

#### Items List

## Basic display, Ordering

### Basic Display

:::note
Note: these settings are meant for every listed item, and are different than similar settings may exist for item view
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Edit button**<br />`show_editbutton_lists` | Enables display of Item Edit button for all items that the currently logged user can edit | — | `1` |
| **State button**<br />`show_state_icon_lists` | Enable quick change of publication state via an AJAX state selector button | — | `1` |
| **(Permanent) Delete button**<br />`show_deletebutton_lists` | Enables display of Item Delete button for all items that the currently logged user can delete. NOTE this is not a trash button, instead it permanently removes the item | — | `0` |
| **Comments counter**<br />`show_comments_count` | Show the number of comments written for each item | — | `1` |
| **Show Title**<br />`show_title_lists` | Show/Hide the items title | — | `1` |
| **Title linkable**<br />`link_titles_lists` | If Yes, the Title of Items will be hyperlinked to the item itself. | — | `1` |
| **Force Full (main) Text**<br />`force_full` | Full (main) Text is used to present the content in full view and is the text after the 'readmore' separator, you can choose here whether to show it when the content is displayed in **category** and other multi-item listings, thus appending it after content's introductory text | — | `0` |
| **FLEXI_Read_More_Link**<br />`show_readmore` | If set to Show, the Read more... link will show if Main text has been created for the Item. | — | `-1` |

### Items Ordering

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Fields that cannot be ordered**<br />`non_orderable_types` | Some fields cannot be ordered or are meaningless to order, e.g. toolbar, please add their type name here, separated with commas. Fields added here will not appear in custom field ordering selectors | — | `account_via_submit,authoritems,toolbar,image,groupmarker,fcpagenav,minigallery,weblink,email,fcloadmodule` |

#### Item Ordering (Level 1)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby` | Order items by CORE fields/properties | — | `rdate` |

#### CUSTOM field ordering

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`orderbycustomfield` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | — | `1` |
| **Custom field**<br />`orderbycustomfieldid` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | — | `0` |
| **Direction**<br />`orderbycustomfielddir` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | — | `ASC` |
| **Ordering Method**<br />`orderbycustomfieldint` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | — | `0` |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

#### Item Ordering (Level 2)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby_2nd` | Order items by CORE fields/properties | — | `alpha` |

#### CUSTOM field ordering

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`orderbycustomfield_2nd` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | — | `1` |
| **Custom field**<br />`orderbycustomfieldid_2nd` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | — | `0` |
| **Direction**<br />`orderbycustomfielddir_2nd` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | — | `ASC` |
| **Ordering Method**<br />`orderbycustomfieldint_2nd` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | — | `0` |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

#### Frontend Overrides

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Ordering selector (Level 1)**<br />`orderby_override` | Enable to display frontend ordering selector (Level 1) | — | `1` |
| **Ordering selector (Level 2)**<br />`orderby_override_2nd` | Enable to display frontend ordering selector (Level 2) | — | `0` |

#### Select Available Options

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **# per page allowed to frontend user**<br />`limit_options` | Please enter a comma separated list of number, leave empty to use Global Defaults | — | `5,10,20,30,50,100,150,200` |
| **Order options (Level 1) allowed to frontend user**<br />`orderby_options` | Please select the ordering options you wish to allow. **NOTE:** (a) **Preconfigured initial order**, is order configured in categories configuration, (b)** Content 's ordering attribute** is for current category, since there is one such order for every category assigned to the item | — | — |
| **Custom Order (Level 1) allowed to frontend user**<br />`orderby_custom` | Please enter the custom fields that you wish to allow as ordering options. Format is (use COMMA separate multiple cases): fieldid:[alpha\|int\|decimal\|date]:[asc\|desc] or fieldid:[alpha\|int\|decimal\|date]:[asc\|desc]:language_string or file_fieldid:file_hits:[asc\|desc]:language_string e.g. (remember: use COMMA for multiple choices) 45:num:desc, 57:decimal:asc:LANG_PRICE_LOWEST, 61:alpha:asc, 62:file_hits:desc:LANG_MOST_DOWNLOADED | — | — |
| **Order options (Level 2) allowed to frontend user**<br />`orderby_options_2nd` | Please select the ordering options you wish to allow. **NOTE:** (a) **Preconfigured initial order**, is order configured in categories configuration, (b)** Content 's ordering attribute** is for current category, since there is one such order for every category assigned to the item | — | — |
| **Custom Order (Level 2) allowed to frontend user**<br />`orderby_custom_2nd` | Please enter the custom fields that you wish to allow as ordering options. Format is (use COMMA separate multiple cases): fieldid:[alpha\|int\|decimal\|date]:[asc\|desc] or fieldid:[alpha\|int\|decimal\|date]:[asc\|desc]:language_string or file_fieldid:file_hits:[asc\|desc]:language_string e.g. (remember: use COMMA for multiple choices) 45:num:desc, 57:decimal:asc:LANG_PRICE_LOWEST, 61:alpha:asc, 62:file_hits:desc:LANG_MOST_DOWNLOADED | — | — |

## Item selection, Pagination

### Item selection, Pagination

:::note
Select items
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Unauthorised items**<br />`show_noauth` | Content items not authorized to be viewable by current guest or logged user will be included in the item lists (category-based views and search view). When a user tries to access the detailed view of any authorized content, then non-logged users will be asked to log-in, and already logged users will receive a HTTP 403 Access Forbidden Errors. **NOTE:** If you enable this feature then you should also set into the parameter 'Unauthorized Page' with the URL of the page to be displayed for these errors | — | `0` |
| **Owned items**<br />`show_owned` | Enable to list items owned / authored by currently logged user - regardless of their state, - regardless of being scheduled or expired (publish up /down dates) | — | `1` |
| **Trashed items**<br />`show_trashed` | Enable to list items trashed items to privileged users. That is users that have the 'Ignore items state' ACL privilege | — | `1` |
| **Subcategories items**<br />`display_subcategories_items` | Display items from subcategories of current category | — | `0` |
| **Filter items using current language**<br />`filtercat` | Only the items of current language will be displayed | — | `1` |

#### Limit / suppress items

:::note
Limits -before- text-search, filtering, alpha-indexing
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable**<br />`use_limit_before_search_filt` | FLEXI_LIMIT_SUPPRESS_ITEMS_LIST_TILL_SUBMIT_DESC | — | `0` |
| **# per page**<br />`limit_before_search_filt` | Number of items per page | — | `0` |

:::note
Limits -after- text-search, filtering, alpha-indexing
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Marked via flag**<br />`display_flag_featured` | Some of the category items are flagged as featured. Select to show (a) both normal and featured items, (b) normal only, (c) featured only | — | `0` |
| **# per page**<br />`limit` | Number of items per page | — | `10` |

:::note
Limits by custom fields: please set 'Locked Filters' in the 'Search / Filter Form' tab
:::

### Pagination (Page links & Totals)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Infinit scrolling**<br />`infinite_scroll` | Allow to load more item in categorie view without relaoding page. No = classic pagination. Load more = display a load more button editable with language string. Scrolling = load item automaticly on scroll down user. Load more and scrolling option disable pagination with number. | — | `0` |
| **Show items total**<br />`show_item_total` | This will display the total number items in the category (according to category display configuration and current filtering) | — | `1` |
| **Pagination (Page links & Totals)**<br />`show_pagination` | Show/Hide pagination, such as links and page counting | — | `2` |
| **Pagination's results (current # / total pages)**<br />`show_pagination_results` | (when pagination is enabled), you can use this option to disable the display of current active page number and total number for pages | — | `1` |

#### Frontend Overrides

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **# per page**<br />`limit_override` | Number of items per page | — | `1` |
| **'Per page' label**<br />`limit_override_label` | Add label inside or outside the selector, or choose not to display the label | — | `2` |

## Item markings

:::note
Content/Content List Markings featured categories, view access, recently created, etc
:::

### Category Markings

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Add Marking**<br />`mu_addcss_cats` | Add an empty span box with an appropriate CSS classes. Please examine HTML output to find the CSS classname | — | — |
| **Add text (Category title)**<br />`mu_addtext_cats` | Select when the category title will be added inside the marking **NOTE:** This is recommend for non-developers and for multi-language sites, since featured category titles will be language filtered (language strings) | — | `1` |

### Access Level Markings (for viewing content)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Add Marking**<br />`mu_addcss_acclvl` | Add an empty span box with an appropriate CSS classes. Please examine HTML output to find the CSS classname | — | — |
| **Add Obtained Levels**<br />`mu_add_condition_obtainded_acc` | Add markings for obtained (access) level always or only when a content item is viewable. **EXPLANATION:** A content item has access level for (a) itself, (b) its main category, (c) its content type. One for these access levels might not be assigned to current user, so item is unviewable, you can select whether to add markings (markups) for other access level of the item already obtained by current user. | — | `0` |
| **Add Text**<br />`mu_addtext_acclvl` | You may select to add text inside the marking box. These include: no access, free (public) access and access level names, **NOTE:** This is recommend for non-developers and for multi-language sites, since all these will be language filtered (language strings) | — | — |
| **Custom no access text**<br />`mu_no_acc_text` | Default text is 'No Access'. You can set a custom language string here, e.g. 'Restricted', 'Members Only' | — | `FLEXI_MU_NO_ACC` (No Access) |
| **Custom free access text**<br />`mu_free_acc_text` | Default text is 'Free'. You can set a custom language string here, e.g. 'Public', 'Everyone' | — | `FLEXI_MU_FREE` |

### Recently ADDED marking

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Add Marking**<br />`mu_addcss_radded` | Add an empty span box with an appropriate CSS classes. Please examine HTML output to find the CSS classname | — | `0` |
| **Add text (Timeframe name)**<br />`mu_addtext_radded` | Add the timeframe name inside the marking box. **NOTE:** This is recommend for non-developers and for multi-language sites, since these will be language filtered (language strings) | — | `1` |

#### Timeframes Configuration

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Timeframe intervals**<br />`mu_ra_timeframe_intervals` | These is a comma separated list of integer time intervals. e.g. write 48h to enter in hours or 2d to specify interval in days | — | `24h , 2d , 7d , 1m , 3m , 1y , 3y` |
| **Timeframe names**<br />`mu_ra_timeframe_names` | These is a comma separated list of language strings. These are matched with the above timeframes one to one, in the same order as entered above | — | `FLEXI_24H_RA , FLEXI_2D_RA , FLEXI_7D_RA , FLEXI_1M_RA , FLEXI_3M_RA , FLEXI_1Y_RA , FLEXI_3Y_RA` |

### Recently UPDATED markings

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Add Marking**<br />`mu_addcss_rupdated` | Add an empty span box with an appropriate CSS classes. Please examine HTML output to find the CSS classname | — | `0` |
| **Add text (Timeframe name)**<br />`mu_addtext_rupdated` | Add the timeframe name inside the marking box. **NOTE:** This is recommend for non-developers and for multi-language sites, since these will be language filtered (language strings) | — | `1` |

#### Timeframes Configuration

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Timeframe intervals**<br />`mu_ru_timeframe_intervals` | These is a comma separated list of integer time intervals. e.g. write 48h to enter in hours or 2d to specify interval in days | — | `24h , 2d , 7d , 1m , 3m , 1y , 3y` |
| **Timeframe names**<br />`mu_ru_timeframe_names` | These is a comma separated list of language strings. These are matched with the above timeframes one to one, in the same order as entered above | — | `FLEXI_24H_RU , FLEXI_2D_RU , FLEXI_7D_RU , FLEXI_1M_RU , FLEXI_3M_RU , FLEXI_1Y_RU , FLEXI_3Y_RU` |

## Options

#### SEO

:::note
Please configure at top level TAB '%s'
:::

#### Comments

:::note
Please configure at top level TAB '%s'
:::

#### Items List

## RSS Feeds

### RSS Feeds

:::note
Note: Enable RSS feeds in tab '%s'
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **# per page**<br />`feed_limit` | Number of items per page | — | `10` |
| **For each feed item show**<br />`feed_summary` | Select if you want to show only the Introtext or the full text of your Item within the generated Feed. | — | `0` |
| **Maximum length of text**<br />`feed_summary_cut` | Item text longer than this value will be cut off | — | `200` |
| **FLEXI_Read_More_Link**<br />`feed_show_readmore` | If set to Show, the Read more... link will show if Main text has been created for the Item. | — | `0` |

### Image

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use image**<br />`feed_use_image` | Extract the first image from the text or use the above field | — | `1` |
| **Link image**<br />`feed_link_image` | Open the item when clicking on the image | — | `1` |
| **Image source**<br />`feed_image_source` | Select the source of the image. You can either choose an image field (if available) or automatically extract the first image found in the main text. | — | — |
| **Image size**<br />`feed_image_size` | FLEXI_IMAGE_SIZE_DESC | — | — |
| **Image width**<br />`feed_image_width` | Image width | — | `80` |
| **Image height**<br />`feed_image_height` | Image height | — | `80` |
| **Processing method**<br />`feed_image_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | — | `1` |

### Custom fields

:::note
Do not add fields that will break feeds display
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Fields list**<br />`feed_extra_fields` | Fields that requires extra CSS/JS will not work properly, fields that might be suitable are fields like e.g. date,text,select,etc. Enter a comma separated list of field names | — | — |

### Item Ordering (Level 1)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`feed_orderby` | Order items by CORE fields/properties | — | `rdate` |

#### CUSTOM field ordering

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`feed_orderbycustomfield` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | — | `0` |
| **Custom field**<br />`feed_orderbycustomfieldid` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | — | `0` |
| **Direction**<br />`feed_orderbycustomfielddir` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | — | `ASC` |
| **Ordering Method**<br />`feed_orderbycustomfieldint` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | — | `0` |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

### Item Ordering (Level 2)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`feed_orderby_2nd` | Order items by CORE fields/properties | — | `alpha` |

#### CUSTOM field ordering

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`feed_orderbycustomfield_2nd` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | — | `1` |
| **Custom field**<br />`feed_orderbycustomfieldid_2nd` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | — | `0` |
| **Direction**<br />`feed_orderbycustomfielddir_2nd` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | — | `ASC` |
| **Ordering Method**<br />`feed_orderbycustomfieldint_2nd` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | — | `0` |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

#### FLEXI_LISTS
