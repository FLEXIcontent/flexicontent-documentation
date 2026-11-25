---
sidebar_position: 3
---

# FLEXIcontent items

FLEXIcontent provides six frontend modules for displaying items, categories, search forms, filters, maps and tag clouds. Configure a module from **Extensions → Modules**.

> Content listings and more, in a module position

:::info Source
This page is generated from `modules/mod_flexicontent/mod_flexicontent.xml` and the official FLEXIcontent 5.x language files.
:::

The **Layout** option selects a module theme. See [Create a module theme](./create-a-module-theme.md) to add your own.

## Basic

#### Display Tabset

### Basic

### Template Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout**<br />`layout` | Choose a layout to render your module | `fclayout` | — | `news` |

:::note
Please set layout parameters in **Layout: ... TAB**. CSS/HTML developers please read: ** Custom templates HOW-TO **
:::

#### Featured / Standard items

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Total items**<br />`count` | The number of items to display (default is 5) | `text` | — | `5` |
| **Featured items**<br />`count_feat` | Note: 'Featured items' are the first NN items out of Total 'Featured items' may have different display 'Standard items'. This depends on template, e.g. they can be full width | `text` | — | `1` |
| **Standard items**<br />`count_std` | # Standard = # Total - # Featured | `text` | — | `Total - Featured` |
| **Offset items**<br />`offset_items` | Skip this many items from the start of the resulting (already ordered and filtered) list, before picking the 'Total items' to display. E.g. set to 3 to skip the first 3 items of the list. Leave 0 (default) for no offset. When multiple categories are configured, the offset is applied per category. | `text` | — | `0` |

:::note
NOTE: to list items with FEATURED FLAG, please go to TAB 'Select Items' and find scope 'Joomla Featured FLAG'
:::

### Menu item to activate

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Force menu item**<br />`itemid_force` | This option will force all links to items to use the current menu itemid or a specific menu itemid | `multilist` | `0` = No<br />`1` = Current<br />`2` = Specific | `0` (No) |
| **Specific menu itemid**<br />`itemid_force_value` | Enter the menu itemid to use for item links NOTE: menu item must point to any FLEXIcontent view, otherwise SEF links will not work, thus it will be ignored if it does not point to FLEXIcontent view | `fcmenuitem` | `—` = Click to select | — |

### Hide/Show Module

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

### Items List

#### Items List Tabset

### Header

:::note
Here you can enable creation of a header for the item listing.
:::

### Statistics

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show total items**<br />`show_found_items` | Show total found items. If apply configuration per category is enabled then this is calculated per category | `multilist` | `0` = No<br />`1` = Separate line<br />`2` = Next to title | `0` (No) |

### Categories

:::note
- The category list will show a list of category items just below the category information. - To create a category list with no items, set the number of displayed items to ZERO
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Apply configuration per category**<br />`apply_config_per_category` | Creates a list of categories. **a. To create a list of categories without items**, set number of items to ZERO. **b. To display V items after every category** set number of items to number V. **NOTE:** Display of category data is possible only if in SCOPE Slider, you set CATEGORY scope to either: (a) **Include** (static selection of categories) or (b) **current** category | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Skip category if no items**<br />`skip_category_if_noitems` | Enable this to skip printing category information when no items are listed for the category | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Category List Order**<br />`cats_orderby` | Ordering of the Category List, available options depend on the category properties available e.g. category name, backend configured ordering, etc | `list` | `—` = Use global<br />`date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified - Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most hits first<br />`rhits` = Popularity -- Least hits first<br />`order` = Category 's ordering attribute | `order` (Category 's ordering attribute) |

#### Categories Information Displayed

#### Title

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show category title**<br />`cats_showtitle` | Show the Title of current category (as defined in item view's url) | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Link title to category**<br />`cats_link_title` | Open the category when clicking on the title | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Max. Title length**<br />`cats_cuttitle` | Max. length of the title. | `text` | — | `40` |

#### Description

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show category description**<br />`cats_showdescr` | Show the Description of current category (as defined in item view's url) | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Strip tags and cut text**<br />`cats_do_cutdescr` | Controls whether the text will be stripped of html tags and then cut to a maximum length | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Introtext max length**<br />`cats_cutdescr` | Auto cut introtext after x characters. NOTE: The html tags of the main text will be stripped. | `text` | — | `100` |
| **Show more category items Link**<br />`cats_readmore` | Enable to show a 'Read more category items' link, linking to each category | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display category image**<br />`cats_show_image` | Extract the first image from the text or use the assigned image in category parameters | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Image source**<br />`cats_image_source` | Select the source of the image. You can either choose image defined in category parameters (if available) or automatically extract the first image found in the description | `radio` | `0` = Extract from description<br />`1` = Use image parameter<br />`2` = Try parameter then extract | `0` (Extract from description) |
| **Link image to category**<br />`cats_link_image` | Open the category when clicking on the image | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Processing method**<br />`cats_image_method` | Processing method | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Image width**<br />`cats_image_width` | Image width | `text` | — | `110` |
| **Image height**<br />`cats_image_height` | Image height | `text` | — | `110` |

### Current Category (item view)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Custom display for current category**<br />`currcat_custom_display` | When enabled then the category of the currently viewed item will be displayed **differently** than other categories. Appearance can be customized by the following parameters | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Current category is**<br />`currcat_source` | Select which category is considered current category | `radio` | `0` = Category of Item in item view<br />`1` = Active Category in category view<br />`2` = Both | `0` (Category of Item in item view) |
| **Fallback to main category**<br />`currcat_fallback_maincat` | If a current category id is not set in the URL, then the main category of the currently viewed item will be used | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Category Information Displayed

#### Title

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show category title**<br />`currcat_showtitle` | Show the Title of current category (as defined in item view's url) | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Link title to category**<br />`currcat_link_title` | Open the category when clicking on the title | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Max. Title length**<br />`currcat_cuttitle` | Max. length of the title. | `text` | — | `20` |

#### Description

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show category description**<br />`currcat_showdescr` | Show the Description of current category (as defined in item view's url) | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Strip tags and cut text**<br />`currcat_do_cutdescr` | Controls whether the text will be stripped of html tags and then cut to a maximum length | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Introtext max length**<br />`currcat_cutdescr` | Auto cut introtext after x characters. NOTE: The html tags of the main text will be stripped. | `text` | — | `100` |
| **Show more category items Link**<br />`currcat_readmore` | Enable to show a 'Read more category items' link, linking to each category | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display category image**<br />`currcat_show_image` | Extract the first image from the text or use the assigned image in category parameters | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Image source**<br />`currcat_image_source` | Select the source of the image. You can either choose an image field (if available) or automatically extract the first image found in the main text. | `list` | `0` = Extract from description<br />`1` = Use image parameter<br />`2` = Try parameter then extract | `0` (Extract from description) |
| **Link image to category**<br />`currcat_link_image` | Open the category when clicking on the image | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Processing method**<br />`currcat_image_method` | Processing method | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Image width**<br />`currcat_image_width` | Image width | `text` | — | `110` |
| **Image height**<br />`currcat_image_height` | Image height | `text` | — | `110` |

### Basic (order, skip, etc)

:::note
Basic options of item list (that are supported by all template layouts), like: **ordering, skipping** unwanted items that have empty value on specific fields, etc
:::

### Ordering

#### Item Ordering (Level 1)

:::note
To use scheduled / expired items orderings, please enable ignore scheduled / expired dates, inside 'Select Items' TAB
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Ordering Groups (*)**<br />`ordering` | Select in which order the items should be fetched. * You can have multiple Groups !!! But be warned that items may appear multiple times, once in each group !!! | `fcordering` | — | `added` |
| **Add Title to each Ordering Group**<br />`ordering_addtitle` | This option will add a title to the Ordering Groups, this is recommended if you use MORE THAN ONE group ... | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Custom Field Order (select this above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Custom field**<br />`orderbycustomfieldid` | Select a custom field to use for ordering, **NOTE**: you need to select/enable custom field ordering above. **NOTE:**: some types of fields cannot be ordered (file and image fields for example). | `fields` | — | `0` |
| **Direction**<br />`orderbycustomfielddir` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `radio` | `ASC` = Ascending<br />`DESC` = Descending | `ASC` (Ascending) |
| **Ordering Method**<br />`orderbycustomfieldint` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `radio` | `0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date<br />`4` = Download hits | `0` (Text) |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

#### Item Ordering (Level 2)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`ordering_2nd` | Order items by CORE fields/properties | `fcordering` | — | `alpha` |

#### CUSTOM field ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`orderbycustomfield_2nd` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Custom field**<br />`orderbycustomfieldid_2nd` | Select a custom field to use for ordering, **NOTE**: you need to select/enable custom field ordering above. **NOTE:**: some types of fields cannot be ordered (file and image fields for example). | `fields` | — | `0` |
| **Direction**<br />`orderbycustomfielddir_2nd` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `radio` | `ASC` = Ascending<br />`DESC` = Descending | `ASC` (Ascending) |
| **Ordering Method**<br />`orderbycustomfieldint_2nd` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `radio` | `0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date<br />`4` = Download hits | `0` (Text) |

:::note
Please note that: **'Download hits'** order needs a **file** field
:::

### Empty Fields Filter

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Skip Items**<br />`skip_items` | Skip Items with Empty Fields. **NOTE:** Depending on your data, it can have a **medium** performance impact | `multilist` | `0` = No<br />`1` = Yes, check field value missing (fast)<br />`2` = Yes, check for empty field display (slower) | `0` (No) |
| **Empty Fields List**<br />`skiponempty_fields` | Fields to examine if empty when skipping items. Note 1: fields must produce NO HTML OUTPUT for this to work | `fields` | — | — |
| **Maximum Items to Skip**<br />`maxskipcount` | Maximum Items to Skip before giving up, for performance reasons values above 100 are ignored | `text` | — | `50` |
| **Empty Fields Combination**<br />`onempty_fields_combination` | Skip item on any empty field or when all empty. | `radio` | `any` = Skip on any empty<br />`all` = Skip when all empty | `any` (Skip on any empty) |
| **Strip HTML on Empty Fields**<br />`striptags_onempty_fields` | Will strip html tags to consider a field as empty. WARNING: Do not enable this, on fields that only put html and then use javascript to replace it. These are not empty fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Select Items

:::note
**All enabled** filtering scopes are **required**. - **Static behaviour** will show **same items regardless** of current view/page, - **Dynamic behaviour** will show items that depend on current view (e.g. currently viewed item) or other dynamic data (e.g. server time)
:::

### Simple Filtering

#### Currently viewed item scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Method**<br />`method_curitem` | All: Display any Item(s) including current. Excluded: Display any item(s) except the currently viewed item, Include (Current Only): Display fields only for the currently viewed item. **Please use layout 'news' or similar** | `multilist` | `0` = All<br />`1` = Exclude<br />`2` = Include (Current ONLY) | `0` (All) |

#### Current Language Scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Method**<br />`method_curlang` | All: Display item(s) of any language, including current one. Excluded: Display item(s) with language different than the current one. Include (Current Only): Display item(s) of the current language only | `multilist` | `0` = All<br />`1` = Exclude<br />`2` = Include (Current ONLY) | `0` (All) |

#### Favourites Scope (current frontend user)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Method**<br />`method_curuserfavs` | All: Display all item(s) regardless of being favourited. Exclude: Display item(s) except the favourited ones. Include: Display item(s) favourited by the currently logged user | `multilist` | `0` = All<br />`1` = Exclude<br />`2` = Include | `0` (All) |

#### Featured Items Scope (Joomla's Featured Flag)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Method**<br />`method_featured` | Select to display (a) ALL items -OR- (b) normal items only (exclude) -OR- (c) featured items only (include) | `multilist` | `0` = All<br />`1` = Exclude<br />`2` = Include | `0` (All) |

#### Item State Scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Method**<br />`method_states` | Select to display items with specific state | `multilist` | `0` = Normal (Published)<br />`1` = Exclude<br />`2` = Include | `0` (Normal (Published)) |
| **Item states**<br />`item_states` | Select item states to be used for creating the items list **NOTE:** Published states include: 'published' & In progress | `fcitemstate` | — | — |
| **List all (via ACL)**<br />`use_list_items_in_any_state_acl` | Enable this to allow privileged users (ACL privilege: 'list items in any state') and super admins to see ANY state items and items that are scheduled and/or expired. NOTE that users without the ACL privilege 'list items in any state', will not see the items, still you might would want to give this module a specific / special view access level | `multilist` | `—` = Use global<br />`0` = No<br />`1` = Yes | `0` (No) |

#### Item Scheduled / Expired Scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Ignore scheduled / expired dates**<br />`ignore_up_down_dates` | You can select to ignore publish up/down dates, thus including items scheduled to be published (having a future publish up date) and / or items that have expired (having a past publish down date). This can be combined with DATE filtering scope to give a more useful result. NOTE that you would want not to add links to these items, because these will not be viewable if they have expired or scheduled. An example of such a usage would be show some info of upcoming(scheduled) items or of past (expired) items | `multilist` | `0` = No<br />`1` = Scheduled (Publish Up)<br />`2` = Expired (Publish down)<br />`3` = Both | `0` (No) |

#### Tags scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Method**<br />`method_tags` | You can set here the included or excluded category/ies. Only tags for from items that belongs (or not belongs) to these categories will be displayed. | `multilist` | `1` = All<br />`2` = Exclude<br />`3` = Include | `1` (All) |
| **Select tags**<br />`tag_ids` | Limit displayed items to those having (or not) the specified tags | `tags` | — | — |
| **Require ALL tags**<br />`tag_combine` | Select whether listed items must have ALL selected tags | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Advanced Filtering

#### Category scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Behaviour (**)**<br />`behaviour_cat` | Static behaviour: **ignores currently viewed item** and uses only parameters to **displays data in all views**. Dynamic behaviour: compares items to **currently viewed item** and thus it **displays data in item views only**, it may or may not use some parameters | `multilist` | `0` = STATIC :: Ignore currently viewed page, and use specific choices<br />**Dynamic Behaviour (Compare to currently viewed item)**<br />`1` = Items in the same category<br />`2` = Items not in the same category<br />**Dynamic Behaviour (Compare to currently viewed category(-ies))**<br />`3` = Items in active category(-ies)<br />`4` = Items not in the active category(-ies) | `0` (STATIC :: Ignore currently viewed page, and use specific choices) |
| **STATIC Method**<br />`method_cat` | This is used by static behaviour(s) and it is ignored by dynamic behaviours. **NOTE:** that dynamic behaviours are always active ! | `multilist` | `1` = All<br />`2` = Exclude<br />`3` = Include | `1` (All) |
| **Categories**<br />`catids` | Please select the categories | `flexicategories` | — | — |
| **Require ALL categories**<br />`cat_combine` | Select whether listed items must be assigned to ALL selected categories | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Extra categories**<br />`treeinclude` | Include parent/children of selected categories. **NOTE**: 'other categories of item' is used only in frontend pages that display an item | `list` | `0` = None<br />`1` = Children categories<br />`5` = Children categories, but exclude selected categories<br />`2` = Ancestor categories<br />`3` = Ancestor & Children Categories<br />`4` = Other categories of item | `0` (None) |
| **Link items via main category**<br />`link_via_main` | Links of items will be routed via main category, thus main category alias or main category menu item alias will be used in the item links | `radio` | `0` = No use selected<br />`1` = Yes | `0` (No use selected) |

#### Types scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Behaviour (**)**<br />`behaviour_types` | Static behaviour: **ignores currently viewed item** and uses only parameters to **displays data in all views**. Dynamic behaviour: compares items to **currently viewed item** and thus it **displays data in item views only**, it may or may not use some parameters | `multilist` | `0` = STATIC :: Ignore currently viewed page, and use specific choices<br />**Dynamic Behaviour (Compare to currently viewed item)**<br />`1` = From the same type<br />`2` = From another type | `0` (STATIC :: Ignore currently viewed page, and use specific choices) |
| **STATIC Method**<br />`method_types` | This is used by static behaviour(s) and it is ignored by dynamic behaviours. **NOTE:** that dynamic behaviours are always active ! | `multilist` | `1` = All<br />`2` = Exclude<br />`3` = Include | `1` (All) |
| **Types**<br />`types` | You can set here the included or excluded type/s. Only items that belongs (or not belongs) to these types will be displayed. | `types` | — | — |

#### Author/My items scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Behaviour (**)**<br />`behaviour_auth` | Static behaviour: **ignores currently viewed item** and uses only parameters to **displays data in all views**. Dynamic behaviour: compares items to **currently viewed item** and thus it **displays data in item views only**, it may or may not use some parameters | `multilist` | `0` = STATIC :: Ignore currently viewed page, and use specific choices<br />**Dynamic Behaviour (Compare to currently viewed item)**<br />`1` = From the same author<br />`2` = From another author<br />`3` = Current Logged User (=My Items) | `0` (STATIC :: Ignore currently viewed page, and use specific choices) |
| **STATIC Method**<br />`method_auth` | This is used by static behaviour(s) and it is ignored by dynamic behaviours. **NOTE:** that dynamic behaviours are always active ! | `multilist` | `1` = All<br />`2` = Exclude<br />`3` = Include | `1` (All) |
| **Authors**<br />`authors` | You can set here the included or excluded author(s). Only items that belongs (or not belongs) to these author(s) will be displayed. Enter a comma separated list of ids. | `text` | — | — |

#### Item scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Behaviour (**)**<br />`behaviour_items` | Static behaviour: **ignores currently viewed item** and uses only parameters to **displays data in all views**. Dynamic behaviour: compares items to **currently viewed item** and thus it **displays data in item views only**, it may or may not use some parameters | `multilist` | `0` = STATIC :: Ignore currently viewed page, and use specific choices<br />**Dynamic Behaviour (Compare to currently viewed item)**<br />`1` = Related items (common tags)<br />`2` = Related items (relation field)<br />`3` = Reverse Related items (relation field) | `0` (STATIC :: Ignore currently viewed page, and use specific choices) |
| **Common tags excluded**<br />`excluded_tags` | Enter the tag ids to exclude from common tags (used by behavior: Related items via common tags) | `tags` | — | — |
| **Relation Field(s)**<br />`relitems_fields` | Select the relation field(s) (used by behavior: Reverse Related Items / Related items via relation field) | `fields` | — | — |
| **STATIC Method**<br />`method_items` | This is used by static behaviour(s) and it is ignored by dynamic behaviours. **NOTE:** that dynamic behaviours are always active ! | `multilist` | `1` = All<br />`2` = Exclude<br />`3` = Include | `1` (All) |
| **Items**<br />`items` | You can set here the included or excluded item(s). Only items that belongs (or not belongs) to that list will be displayed. Enter a comma separated list of ids. | `text` | — | — |
| **Use above order**<br />`items_use_order` | Instead of the configured ordering, you may want to use the order of the items specified above | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Expert Filtering

### Date scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Behaviour (***) Please read**<br />`behaviour_dates` | Static behaviour: compares dates of items to the FROM/TO date parameters and **displays data in all views**. Dynamic behaviour: compares dates of items to **dates of currently viewed item** or to **current server time** (e.g. to current item created date -2 weeks, e.g. to previous week of current server time) - if comparing to current item dates, it **displays data in item views only** - if comparing to current server time it **displays data in all views** | `multilist` | `0` = Static: Specific FROM/TO dates or date expressions<br />**Dynamic Behaviour ( ... )**<br />`1` = FROM/TO custom offset (alters 'Compare with DYNAMIC date')<br />**Dynamic Behaviour (Same ...)**<br />`8` = Same day<br />`2` = Same month<br />`3` = Same year<br />**Dynamic Behaviour (Previous ...)**<br />`9` = Previous day<br />`4` = Previous month<br />`5` = Previous year<br />**Dynamic Behaviour (Next ...)**<br />`10` = Next day<br />`6` = Next month<br />`7` = Next year<br />**Dynamic Behaviour (ignore year)**<br />`11` = Same day of month (1-31)<br />`12` = [-3,+4] days of month<br />`13` = Same week of month (1, 4)<br />`14` = Same week of year (1-53)<br />`15` = Same month of year (1-12)<br />**Dynamic Behaviour (ignore month / year)**<br />`16` = Same day of month (1-31)<br />`17` = [-3,+4] days of month<br />`18` = Same week of month (1, 4) | `0` (Static: Specific FROM/TO dates or date expressions) |

#### Dynamic behaviours: Compare to server time or to currently viewed item

#### Static behaviour: Specific dates ... or custom offset for dynamic behaviours

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Method**<br />`method_date_dyn_ignored` | Method dynamic desc | `multilist` | `1` = Include | `1` (Include) |
| **STATIC Method**<br />`method_dates` | This is used by static behaviour(s) and it is ignored by dynamic behaviours. **NOTE:** that dynamic behaviours are always active ! | `multilist` | `1` = All<br />`2` = Exclude<br />`3` = Include | `1` (All) |
| **Date DATA to use in comparison**<br />`date_type` | The listed items items will be compared used these date DATA. **NOTE**: These are used in both static behaviour and dynamic behaviours | `multilist` | `0` = Created<br />`1` = Modified<br />`2` = Publish Up<br />`4` = Publish Down<br />`3` = Date Field | `0` (Created) |
| **Date Field**<br />`datecomp_field` | To enable using this, set above the 'Date DATA' parameter to 'Date Field'. **NOTE:** if field has multiple values only the first value of date field will be used | `fields` | — | — |
| **Null / empty dates**<br />`nulldates` | Select to include/exclude date values that are empty or NULL | `radio` | `0` = Exclude<br />`1` = Include | `0` (Exclude) |
| **First day of week**<br />`week_start` | Select which day is the first day of week is | `radio` | `0` = Sunday<br />`5` = Monday | `0` (Sunday) |

:::note
Custom offsets that shift the DYNAMIC date, e.g. -5 d (minus 5 days) - to enter **CURRENT date (now)** use: 0 d
:::

:::note
Compare to specific dates (YYYY-MM-DD) e.g. 2015-01-23 - to enter **CURRENT date (now)** use: CURDATE() &gt; , and set date type to 'SQL date expression'
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **From**<br />`bdate` | If you selected the static behaviour, choose the start date in MySQL format (YYYY-MM-DD). If you selected the custom offset behaviour enter the start offset : Use 'd' for days, 'm' for months and 'Y' for years. eg: -5 d (minus 5 days) | `fcdate` | — | — |
| **To**<br />`edate` | If you selected the static behaviour, choose the end date in MySQL format (YYYY-MM-DD). If you selected the custom offset behaviour enter the end offset : Use 'd' for days, 'm' for months and 'Y' for years. eg: 3 d (plus 3 days) | `fcdate` | — | — |
| **FROM date is**<br />`raw_bdate` | Select to enter below: (a) **Date string:** e.g. (static) specific date : 2012-04-23 e.g. (dynamic: custom offset) now minus 3 hours: -3 h (b) **Date expression** static only e.g. previous day 20:00 UTC: ADDTIME( CAST(ADDDATE(CURDATE(), -1) AS DATETIME) , '0 20:00:00') e.g. today 20:00 UTC: ADDTIME( CAST(CURDATE() AS DATETIME),'0 20:00:00') | `radio` | `0` = Specific date<br />`1` = SQL date Expression | `0` (Specific date) |
| **TO date is**<br />`raw_edate` | Select to enter below: (a) **Date string:** e.g. (static) specific date : 2012-04-23 e.g. (dynamic: custom offset) now minus 3 hours: -3 h (b) **Date expression** static only e.g. previous day 20:00 UTC: ADDTIME( CAST(ADDDATE(CURDATE(), -1) AS DATETIME) , '0 20:00:00') e.g. today 20:00 UTC: ADDTIME( CAST(CURDATE() AS DATETIME),'0 20:00:00') | `radio` | `0` = Specific date<br />`1` = SQL date Expression | `0` (Specific date) |
| **Compare with DYNAMIC date**<br />`date_compare` | Choose if you wish to compare date dynamic date DATA either with (a) current server time or (b) with date of currently viewed item | `radio` | `0` = Current server time<br />`1` = Date DATA of currently viewed item | `0` (Current server time) |

### Custom (non-CORE) fields scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Behaviour (**)**<br />`behaviour_filt` | Static behaviour: **ignores currently viewed item** and uses only parameters to **displays data in all views**. Dynamic behaviour: compares items to **currently viewed item** and thus it **displays data in item views only**, it may or may not use some parameters | `multilist` | `0` = Static: Filter using specific field values<br />`1` = Dynamic: Filter using field values of currently item<br />`2` = Dynamic + Static: Filter by both | `0` (Static: Filter using specific field values) |
| **Dynamic filters (item view only)**<br />`dynamic_filters` | These filters apply a DYNAMIC filtering, that compares to currently viewed item, so that the item list contains items that have same field values as the current item. ** Enter comma list of INTEGERs like: ** field_id1,field_id2,field_id3 example: 34,57,11 | `textarea` | — | — |
| **STATIC Method**<br />`method_filt` | This is used by static behaviour(s) and it is ignored by dynamic behaviours. **NOTE:** that dynamic behaviours are always active ! | `multilist` | `1` = All<br />`2` = Exclude<br />`3` = Include | `1` (All) |
| **Static filters (all views)**<br />`static_filters` | These filters apply a STATIC filtering, regardless of current item being displayed. Enter like: field_id##value %% field_id##value Example: 22##14 %% 47##some field value %% 19##someword - **Single values**: field_id##value1 **Ranges**: field_id##value1---value2 - **Multiple values**: field_id##value1+++value2+++value3 - **Relation / Reverse-relation**: REL_field_id##REL_ITEM_field_id~~value1 | `textarea` | — | — |

### Footer

:::note
Normally this module creates item/category lists. Here you can select to display extra 'footer' information.
:::

### Recently Added Favourites

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Recent Favourites List**<br />`display_favlist` | Display a list of recently (current session) added favourites (item titles with links). NOTE: This can be combined with the FAVORITE SCOPE to show all favorite items of the user (in a more detailed presentation) | `radio` | `0` = Hide<br />`1` = Show | `0` (Hide) |

### Footer Read More

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Read More**<br />`show_more` | Displays a link at the bottom of the module that links to the specified URL. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **More Title**<br />`more_title` | The text of the link. ** Leave blank for language default:** Read more content | `text` | — | — |
| **More Link**<br />`more_link` | More Link | `text` | — | `index.php` |
| **Open in new window**<br />`more_blank` | Open the 'More' link in a new window or tab. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **CSS - More...**<br />`more_css` | CSS code to apply on the 'More' link at the bottom of the module. | `textarea` | — | — |

#### Items List Tabset

### Layout: Options of selected Layout

### Content via parameters

:::note
This is display configuration repeated for **every listed item**. It is available to ALL templates, but not ALL templates will make use of it
:::

### Title

#### Standard

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display title**<br />`display_title` | Display hide title | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Link title**<br />`link_title` | Open the item when clicking on the Title | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Max. Title length**<br />`cuttitle` | Max. length of the title. | `text` | — | `40` |

#### Featured

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display title**<br />`display_title_feat` | Display hide title | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Link title**<br />`link_title_feat` | Open the item when clicking on the Title | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Max. Title length**<br />`cuttitle_feat` | Max. length of the title. | `text` | — | `40` |

### Description

#### Standard

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display description**<br />`display_text` | Display description text | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Strip tags and cut text**<br />`mod_do_stripcat` | Controls whether the text will be stripped of html tags and then cut to a maximum length | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Introtext max length**<br />`mod_cut_text` | Auto cut introtext after x characters. NOTE: The html tags of the main text will be stripped. | `text` | — | `100` |
| **Show readmore**<br />`mod_readmore` | Show/hide the readmore button | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Readmore align**<br />`readmore_align_std` | Number of columns for the items. NOTE: this is the max value and actually number of columns displayed will depend to width of browser window | `radio` | `left` = Left<br />`center` = Center<br />`right` = Right | `center` (Center) |
| **Btn class**<br />`readmore_class_std` | Add your css class readon btn feat by default _readon btn std_ | `text` | — | — |

#### Featured

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display description**<br />`display_text_feat` | Display description text | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Strip tags and cut text**<br />`mod_do_stripcat_feat` | Strip tags and cut text | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Introtext max length**<br />`mod_cut_text_feat` | Auto cut introtext after x characters. NOTE: The html tags of the main text will be stripped. | `text` | — | `200` |
| **Show readmore**<br />`mod_readmore_feat` | Show/hide the readmore button | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Readmore align**<br />`readmore_align_feat` | Number of columns for the items. NOTE: this is the max value and actually number of columns displayed will depend to width of browser window | `radio` | `left` = Left<br />`center` = Center<br />`right` = Right | `center` (Center) |
| **Btn class**<br />`readmore_class_feat` | Add your css class readon btn feat by default _readon btn feat_ | `text` | — | — |

### Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Image source**<br />`mod_image` | Select the source of the image. You can either choose an image field (if available) or automatically extract the first image found in the main text. | `fcimage` | — | — |
| **Field HTML as Image**<br />`mod_image_custom_display` | You can use the HTML produced by any custom field in place of image. -- Leave blank: to use the above drop-down select box value, -- **Note: image size and other parameters are not used**, -- Write: like fieldname##varname e.g. for image fields use: imgfieldname##display_small, imgfieldname##display_medium, imgfieldname##display_large | `text` | — | — |
| **Field URL as Image**<br />`mod_image_custom_url` | You can use the URL produced by any custom field in place of image. -- Leave blank: to use the above drop-down select box value, -- **Note: image size and other parameters are applied to the given URL**, -- Write: like fieldname##varname e.g. for image fields use: imgfieldname##display_small_src, imgfieldname##display_medium_src, imgfieldname##display_large_src | `text` | — | — |
| **Image Field Fallback (when image missing)**<br />`mod_image_fallback_img` | When image is missing, you can select to use some image as fallback, e.g. item introtext image when image field has no value, even if image field has default value | `list` | `0` = No fallback<br />`1` = Use introtext image<br />`2` = Use introtext image (ignore image field default image)<br />`3` = Custom fallback field | — |

:::note
Please remember to enable this above
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Custom fallback field**<br />`mod_image_fallback_field` | — | `fcimage` | — | — |

#### Standard

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use image**<br />`mod_use_image` | Extract the first image from the text or use the above field | `multilist` | `0` = No<br />`1` = Yes, Resize<br />`small` = Yes, small thumb (requires image field)<br />`medium` = Yes, medium thumb (requires image field)<br />`large` = Yes, large thumb (requires image field)<br />`original` = Yes, original image (requires image field) | `medium` (Yes, medium thumb (requires image field)) |
| **Link image**<br />`mod_link_image` | Open the item when clicking on the image | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Processing method**<br />`mod_method` | Processing method | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Image width**<br />`mod_width` | Image width | `text` | — | `80` |
| **Image height**<br />`mod_height` | Image height | `text` | — | `80` |

#### Featured

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use image**<br />`mod_use_image_feat` | Extract the first image from the text or use the above field | `multilist` | `0` = No<br />`1` = Yes, Resize<br />`small` = Yes, small thumb (requires image field)<br />`medium` = Yes, medium thumb (requires image field)<br />`large` = Yes, large thumb (requires image field)<br />`original` = Yes, original image (requires image field) | `medium` (Yes, medium thumb (requires image field)) |
| **Link image**<br />`mod_link_image_feat` | Open the item when clicking on the image | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Processing method**<br />`mod_method_feat` | Processing method | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Image width**<br />`mod_width_feat` | Image width | `text` | — | `110` |
| **Image height**<br />`mod_height_feat` | Image height | `text` | — | `110` |

#### Default Image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show default image**<br />`mod_default_img_show` | Select to show a default image for items without one | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default image**<br />`mod_default_img_path` | This is the image to show if item has no image | `text` | — | `components/com_flexicontent/assets/images/image.png` |

### Dates

#### Standard

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Date**<br />`display_date` | Display Date | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Display label**<br />`date_label` | Show/hide the field label | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display Date Type**<br />`date_fields` | Display Date Type | `fccheckbox` | — | — |
| **Date Format**<br />`date_format` | — | `multilist` | `DATE_FORMAT_LC` = Date format lc<br />`DATE_FORMAT_LC1` = Date format lc1<br />`DATE_FORMAT_LC2` = Date format lc2<br />`DATE_FORMAT_LC3` = Date format lc3<br />`DATE_FORMAT_LC4` = Date format lc4<br />`custom` = Custom | `DATE_FORMAT_LC3` (Date format lc3) |
| **Custom date format**<br />`custom_date_format` | Custom date format if you select custom from above. | `text` | — | — |

#### Featured

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Date**<br />`display_date_feat` | Display Date | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Display label**<br />`date_label_feat` | Show/hide the field label | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display Date Type**<br />`date_fields_feat` | Display Date Type | `fccheckbox` | — | — |
| **Date Format**<br />`date_format_feat` | — | `multilist` | `DATE_FORMAT_LC` = Date format lc<br />`DATE_FORMAT_LC1` = Date format lc1<br />`DATE_FORMAT_LC2` = Date format lc2<br />`DATE_FORMAT_LC3` = Date format lc3<br />`DATE_FORMAT_LC4` = Date format lc4<br />`custom` = Custom | `DATE_FORMAT_LC3` (Date format lc3) |
| **Custom date format of featured**<br />`custom_date_format_feat` | Custom date format of featured if you select custom from above. | `text` | — | — |

### Hits

#### Standard

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Hits**<br />`display_hits` | Display Hits Field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display label**<br />`hits_label` | Show/hide the field label | `radio` | `2` = No<br />`1` = Yes<br />`0` = Yes, after counter | `0` (Yes, after counter) |

#### Featured

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Hits**<br />`display_hits_feat` | Display Hits Field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display label**<br />`hits_label_feat` | Show/hide the field label | `radio` | `2` = No<br />`1` = Yes<br />`0` = Yes, after counter | `0` (Yes, after counter) |

### Voting

#### Standard

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Voting**<br />`display_voting` | Display Voting Field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display label**<br />`voting_label` | Show/hide the field label | `radio` | `2` = No<br />`1` = Yes<br />`0` = Yes, after counter | `0` (Yes, after counter) |
| **Show vote counter**<br />`vote_counter` | Display the number of votes the item has received | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Number of Stars**<br />`vote_stars` | In order to have a more compact display you can select to make the voting bar be the size of a single star | `radio` | `1` = 1 star (Recommended)<br />`5` = 5 stars | `1` (1 star (Recommended)) |
| **Allow to vote**<br />`allow_vote` | Since little information about each item is displayed, it is recommended to disable new votes | `radio` | `0` = No (Recommend)<br />`1` = Yes | `0` (No (Recommend)) |

#### Featured

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Voting**<br />`display_voting_feat` | Display Voting Field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display label**<br />`voting_label_feat` | Show/hide the field label | `radio` | `2` = No<br />`1` = Yes<br />`0` = Yes, after counter | `0` (Yes, after counter) |
| **Show vote counter**<br />`vote_counter_feat` | Display the number of votes the item has received | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Number of Stars**<br />`vote_stars_feat` | In order to have a more compact display you can select to make the voting bar be the size of a single star | `radio` | `1` = 1 star (Recommended)<br />`5` = 5 stars<br />`0` = Default stars | `1` (1 star (Recommended)) |
| **Allow to vote**<br />`allow_vote_feat` | Since little information about each item is displayed, it is recommended to disable new votes | `radio` | `0` = No (Recommend)<br />`1` = Yes | `0` (No (Recommend)) |

### Comments

#### Standard

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Comments**<br />`display_comments` | Display number of item's comments | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display label**<br />`comments_label` | Show/hide the field label | `radio` | `2` = No<br />`1` = Yes<br />`0` = Yes, after counter | `0` (Yes, after counter) |

#### Featured

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **FLEXI_DISPLAY_comments**<br />`display_comments_feat` | Display number of item's comments | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display label**<br />`comments_label_feat` | Show/hide the field label | `radio` | `2` = No<br />`1` = Yes<br />`0` = Yes, after counter | `0` (Yes, after counter) |

### Custom Fields

#### Standard

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display fields**<br />`use_fields` | Select to display any extra CORE or CUSTOM Field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display label**<br />`display_label` | Show/hide the field label | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Hide label when empty**<br />`hide_label_onempty` | Enable this to hide the field label when field's HTML display is empty | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Text after label**<br />`text_after_label` | Text to display immediately after label | `text` | — | — |
| **Please select fields**<br />`fields` | Select the fields you wish to display in this module. | `fields` | — | — |

#### Featured

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display fields**<br />`use_fields_feat` | Select to display any extra CORE or CUSTOM Field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display label**<br />`display_label_feat` | Show/hide the field label | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Hide label when empty**<br />`hide_label_onempty_feat` | Enable this to hide the field label when field's HTML display is empty | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Text after label**<br />`text_after_label_feat` | Text to display immediately after label | `text` | — | — |
| **Please select fields**<br />`fields_feat` | Select the fields you wish to display in this module. | `fields` | — | — |

### Content via Layout Builder

:::note
This is display configuration repeated for **every listed item**. It is available to ALL templates, but not ALL templates will make use of it
:::

### Layout 1

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout builder**<br />`builder_layout1` | — | `fclayoutbuilder` | — | — |
| **Html**<br />`builder_layout1_html` | — | `textarea` | — | — |
| **JS**<br />`builder_layout1_js` | — | `hidden` | — | — |
| **Css**<br />`builder_layout1_css` | — | `textarea` | — | — |
| **Styles**<br />`builder_layout1_styles` | — | `hidden` | — | — |
| **Components**<br />`builder_layout1_components` | — | `hidden` | — | — |
| **Assets**<br />`builder_layout1_assets` | — | `hidden` | — | — |
| **Hash**<br />`builder_layout1_hash` | — | `hidden` | — | — |
| **Less**<br />`builder_layout1_less` | — | `hidden` | — | `/modules/mod_flexicontent/builder/less/builder_layout1_&#123;&#123;id&#125;&#125;` |

### Layout 2

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout builder**<br />`builder_layout2` | — | `fclayoutbuilder` | — | — |
| **Html**<br />`builder_layout2_html` | — | `textarea` | — | — |
| **JS**<br />`builder_layout2_js` | — | `hidden` | — | — |
| **Css**<br />`builder_layout2_css` | — | `textarea` | — | — |
| **Styles**<br />`builder_layout2_styles` | — | `hidden` | — | — |
| **Components**<br />`builder_layout2_components` | — | `hidden` | — | — |
| **Assets**<br />`builder_layout2_assets` | — | `hidden` | — | — |
| **Hash**<br />`builder_layout2_hash` | — | `hidden` | — | — |
| **Less**<br />`builder_layout2_less` | — | `hidden` | — | `/modules/mod_flexicontent/builder/less/builder_layout2_&#123;&#123;id&#125;&#125;` |

#### Display Tabset

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
