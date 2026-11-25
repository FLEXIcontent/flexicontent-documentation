---
sidebar_position: 3
---

# Content types — options

A content type defines the fields, authoring rules and display settings available to a category of items. Open a type from **Components → FLEXIcontent → Content Types**.

:::info Source
This page is generated from `admin/models/forms/type.xml` and the official FLEXIcontent 5.x language files.
:::

## Title

### Title text

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`title_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`title_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |
| **Automatic title**<br />`auto_title` | You can set title to an automatic value | `multilist` | `0` = No<br />`1` = Set to ID<br />`2` = Use custom code | `0` (No) |
| **Custom code**<br />`auto_title_code` | Enter PHP code to be used create the custom value, please set to empty and save to load the default example, and then customize | `textarea` | — | `$F = & $item-&gt;fields; $txt = isset( $F['fieldname01'] ) ? $F['fieldname01']-&gt;postdata[0] : 'fieldname01 field not found'; return $txt;` |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`title_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`title_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Description

### Description

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description label**<br />`maintext_label` | The main text field label in the item form. Default is 'Description' or what you have set in the field screen. | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`maintext_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |
| **Editor**<br />`maintext_hide_html` | Use an HTML (WYSIWYG) editor or display a simple textarea | `radio` | `—` = Use field's setting<br />`0` = HTML Editor<br />`1` = Simple Textarea | — |
| **Editor width**<br />`maintext_width` | HTML editor width | `text` | — | — |
| **Editor height**<br />`maintext_height` | HTML editor height | `text` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`maintext_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`maintext_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Categories

### Categories

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`categories_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`categories_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`categories_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`categories_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

#### Links

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add links**<br />`categories_link_to_view` | Link every value to its item listing view | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |

## Created

### Created

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`created_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`created_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`created_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`created_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Created By

### Created By

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`created_by_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`created_by_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`created_by_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`created_by_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Modified

### Modified

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`modified_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`modified_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`modified_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`modified_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Modified By

### Modified By

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`modified_by_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`modified_by_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`modified_by_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`modified_by_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Document Type

### Document Type

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`document_type_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`document_type_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`document_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`document_type_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Hits

### Hits

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`hits_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`hits_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`hits_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`hits_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Version

### Version

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`version_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`version_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`version_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`version_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## State

### State

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`state_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`state_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`state_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`state_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Voting

### Voting

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`voting_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`voting_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`voting_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`voting_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |
| **Show vote counter**<br />`voting_main_counter` | Display total number of votes | `radio` | `—` = Use field's setting<br />`0` = Disable<br />`1` = Enable | — |
| **Show counter label**<br />`voting_main_counter_show_label` | This will add a 'votes' label after the voting counter | `radio` | `—` = Use field's setting<br />`0` = Disable<br />`1` = Enable | — |
| **Show percentage**<br />`voting_main_counter_show_percentage` | This will display the percentage rating next to each rating label | `radio` | `—` = Use field's setting<br />`0` = Disable<br />`1` = Enable | — |

#### Average rating

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`voting_main_label` | The label of average rating | `text` | — | — |
| **Rating scale texts**<br />`voting_rating_texts` | Textual representation of rating scale. Enter a comma seperated list of language strings. eg JVERYPOOR, JPOOR, JFAIR, JGOOD, JEXCELLENT | `textarea` | — | — |

#### Composite voting

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`voting_enable_extra_votes` | Turn on/off the display of partial voting characteristics, like quality, performance, accuracy, etc | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Voting characteristics**<br />`voting_extra_votes` | Here you can define the voting characteristics like e.g. Quality, Speed, Accuracy, etc ... **Write like**: 1##Quality##Description%% 2##Speed##Description%% 3##Accuracy##Description%% 4##Appearance##Description%% ... **NOTE 1**: The names will be passed through JText ... to allow multilanguage support (You can add them to your language files) | `textarea` | — | — |
| **Show vote counter**<br />`voting_extra_counter` | Display total number of votes | `radio` | `—` = Use field's setting<br />`0` = Disable<br />`1` = Enable | — |
| **Show counter label**<br />`voting_extra_counter_show_label` | This will add a 'votes' label after the voting counter | `radio` | `—` = Use field's setting<br />`0` = Disable<br />`1` = Enable | — |
| **Show percentage**<br />`voting_extra_counter_show_percentage` | This will display the percentage rating next to each rating label | `radio` | `—` = Use field's setting<br />`0` = Disable<br />`1` = Enable | — |

## Favourites

### Favourites

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`favourites_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`favourites_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`favourites_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`favourites_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

## Tags

### Tags

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label**<br />`tags_label` | Define a custom Label for this core field For per language use [shortlang]= e.g. [fr]=French Label [en]=English Label [default]=Default Label ... WITHOUT newline characters | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Description**<br />`tags_desc` | Define a custom Tooltip Description for this CORE field, when field is EDITED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT new line characters | `textarea` | — | — |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`tags_display_label` | Display or hide label of this field | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |
| **Description when viewing**<br />`tags_viewdesc` | Define a custom Tooltip Description for this CORE field, when field is VIEWED For per language use [shortlang]= e.g. [fr]=Description of field in French [en]=Description of field in English [default]=Default Description of field ... WITHOUT newline characters | `textarea` | — | — |

#### Links

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add links**<br />`tags_link_to_view` | Link every value to its item listing view | `radio` | `—` = Use field's setting<br />`0` = No<br />`1` = Yes | — |

## Authoring

### Main category

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allowed subtree --Blank allows all--**<br />`catid_allowed_parent` | Select the category subtree that will be used for selecting main category | `flexicategories` | — | — |
| **Disable subtree parent**<br />`catid_allowed_parent_disable` | Usually you would want to disable selecting the root category of the category subtree | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Default category**<br />`catid_default` | Select the default main category to for this type (that will be pre-selected on item form load) | `flexicategories` | — | — |

### Secondary categories

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allowed subtree --Blank allows all--**<br />`cid_allowed_parent` | Select the category subtree that will be allowed to be used for selecting secondary categories | `flexicategories` | — | — |
| **Disable subtree parent**<br />`cid_allowed_parent_disable` | Usually you would want to disable selecting the root category of the category subtree | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Default categories**<br />`cid_default` | Select the default secondary categories | `flexicategories` | — | — |

### Item layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allowed Item Layouts -- none allows all --**<br />`allowed_ilayouts` | Select the allowed item layouts for this Item Type **NOTE:** Every template has one item layout, so this list contains template names **NOTE:** This is especially useful if you want to allow **layout** selection for frontend users, but also for reducing the size of the selection list | `ilayoutlist` | — | — |

### Common tags (seleactable via checkboxes)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Tags**<br />`quick_tags` | Tags selectable as checkboxes in item form (for quicker / easier selection) | `tag` | — | — |

## Seo

### Microdata support

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Microdata type**<br />`microdata_itemtype` | Select a microdata type to that will characterize all items of the type. MICRODATA allow search engines to categorize your content appropriately, improving SEO of your pages | `microdatatype` | — | — |

### HTML title Tag

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Override**<br />`override_title` | Setting this to yes, allows you to use the item title (or the custom title if set) as your page title (= HTML TITLE tag), instead of using the page title set in the menu item. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Category to**<br />`addcat_title` | Add the category name to the title tag on the left or on the right of the item name | `radio` | `0` = No<br />`1` = On Left<br />`2` = On Right | `1` (On Left) |

### Other SEO parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Rel canonical tag**<br />`add_canonical` | Add a rel canonical meta tag into the source code of your pages, this helps search engines identify a page being viewed via different URLs, and give it better rank, by not indexing it multiple times | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Search-engine robots**<br />`robots` | Indicate if robots of search-engines will include this content into their search index and if they will follow (aka index) links contained in this | `radio` | `—` = Joomla's default<br />`index, follow` = index, follow<br />`noindex, follow` = noindex, follow<br />`index, nofollow` = index, nofollow<br />`noindex, nofollow` = noindex, nofollow | — |

### Menu Item

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default menu item for content item URLs**<br />`type_menu_itemid` | The menu item that will be used in item URLs when a more appropriate menu item could not be found, e.g a more appropriate menu item is one that points directly to a content item. **NOTE:** The menu item effects which modules are active. | `fcmenuitem` | — | — |
| **Default menu item usage**<br />`type_menu_itemid_usage` | The menu item that will be used in items of this type when a more appropriate menu item could not be found, e.g a more appropriate menu item is one that points directly to a content item. **NOTE:** The menu item effects which modules are active. | `radio` | `0` = None<br />`1` = try before item's category<br />`2` = try after item's category<br />`3` = Currently active menu item | `0` (None) |

## Item view

### Joomla article view

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow**<br />`allow_jview` | By default joomla article view will be re-routed to FLEXIcontent item view. If re-route / re-direct is disabled, then it will allow the item to be viewed by both the Joomla article view and the FLEXIcontent item view, thus e.g. article links in Joomla category view will not be rerouted / redirected NOTE: 'Allowed' and 'Rerouted' will show modules assigned to Joomla menu items, 'redirect' will change the URL to be FLEXIcontent item view URL and will show the module assigned to the FLEXIcontent menu items NOTE: (compatibility) this is by default allowed for 'article' Content **type**, but you can allow other types too NOTE: if enabled the search view links, will link to JOOMLA article view and URLs may contain /component/content/article/ | `multilist` | `0` = Route to FC item view<br />`2` = Redirect to FC item view<br />`1` = Yes | `0` (Route to FC item view) |
| **Search view links**<br />`search_jlinks` | Items of this type in search view can link to Joomla article view or to FLEXIcontent item view | `radio` | `0` = FC item links<br />`1` = Joomla article links | `1` (Joomla article links) |
| **Add custom fields**<br />`jview_fields_placement` | Select to add FLEXIcontent custom fields to Joomla article view. NOTE: all custom fields will be added according to the ACCESS Levels allowed to the current frontend user | `radio` | `0` = Disable<br />`1` = Before content<br />`2` = After content | `0` (Disable) |

### Content

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show Title**<br />`show_title` | Show/Hide the items title | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Show introductory text**<br />`show_intro` | Introductory Text is used to present the content in **category** and other multi-item listings, you can choose here whether to show it when the content is displayed in full view, thus prepending it before content's full text | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Enable comments integration**<br />`comments` | Enable commenting system integration. **NOTE:** This parameter may be overridden for types, categories, single items or menu items. **NOTE:** By setting to disable you may manually trigger (description field will trigger all by default), appropriate Joomla content plugin of your commenting system to insert comments via a Joomla CONTENT Event. In case of adding comments this way, you cannot use the parameter 'Disable comments' in the item form, instead you will need to do it the way your commenting system recommends, e.g. by inserting some special text inside the description | `radio` | `—` = Use Global<br />`0` = Disable or integrate manually<br />`1` = JComments | — |
| **Create pathway automatically**<br />`automatic_pathways` | Category and item pathway (displayed by breadcrumbs module) will be created automatically by (a) removing all menu items from the pathway and adding to it the tree path of category titles and the item title. NOTE you can override this setting per category, type and item | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

### Icons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Print Icon**<br />`show_print_icon` | Enable Print screen | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Email Icon**<br />`show_email_icon` | Enable emailing current page URL to a friend | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Edit button**<br />`show_editbutton` | Enables display of Item Edit button for all items that the currently logged user can edit | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Link to frontend<br />`2` = Link to backend | — |
| **(Permanent) Delete button**<br />`show_deletebutton` | Enables display of Item Delete button for all items that the currently logged user can delete. NOTE this is not a trash button, instead it permanently removes the item | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **State button**<br />`show_state_icon` | Enable quick change of publication state via an AJAX state selector button | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |

### Styling and behaviour

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add CSS to the item view**<br />`view_extra_css_fe` | Add extra CSS rules to the item view. - Usually you would set this per item type. | `editor` | — | — |
| **Add JS to item view for developers only ***<br />`view_extra_js_fe` | Add extra JS code to the item view. - Usually you would set this per item type. | `editor` | — | — |

## Search view

### Search view

:::note
Search view can do **text search** and **filtering**, differently per content type, -- you may set search behaviour here. **NOTE:** these are not used in category-like views (content lists), for these views configure in component / category / menu items
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Text searchable fields**<br />`searchable` | Text search will occur in the selected fields (if usage of specific field is enabled in search menu item configuration) | `filters` | — | — |
| **Filters**<br />`filters` | NOTE: you need to enable usage of this in the search view configuration (e.g. menu item), NOTE: you can define the filter appearance and behaviour by editing the configuration of every individual field | `filters` | — | — |
| **Search results priority**<br />`search_priority` | Search view: items of types with a higher number are listed before items of types with a lower number, before any other ordering (relevance, priority by field, configured order). 0 = no priority | `number` | — | `0` |

#### Search results display (per content type)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Search result image**<br />`search_image` | Image field shown in search results for items of this type. Leave empty to extract the first image from the main text. The search menu item may override this setting | `fcimage` | — | — |
| **Show creation date in search results**<br />`search_show_date` | Show the creation date of items of this type in search results. The search menu item may override this setting | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Extra fields in search results**<br />`search_infoflds` | Field names (comma separated) to render below each search result of this type. The search menu item may override this setting | `textarea` | — | — |

## Item form

#### Item form bof

### Item Form - Frontend

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item form layout**<br />`form_ilayout_fe` | — | `fclayout` | **Built-in layouts**<br />`tabs` = tabs (Default)<br />`flat` = flat | — |

#### Item Form - Frontend

### General Form Behavior

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Optional buttons**<br />`allowbuttons_fe` | Select the optional buttons that you want to appear in frontend form | `fccheckbox` | — | — |
| **Placement of buttons**<br />`buttons_placement_fe` | Select to display form buttons at the top or bottom of the form | `radio` | `—` = Use Global<br />`0` = Top<br />`1` = Bottom<br />`2` = Left<br />`3` = Right | — |

#### Display approval needed warnings

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Inside form**<br />`approval_warning_inform_fe` | Enable this, to show a message inside item form, whether current user can publish new items or if they can self-approve changes to existing items | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **After form submit**<br />`approval_warning_aftersubmit_fe` | Enable this, to show an after form submit warning, saying if approval is needed for new item being published or for the changes to existing item becoming active | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Requires version reviewal**<br />`version_reviewal_msg_fe` | _Please note that your new document **version** will be reviewed and approved by a site administrator_ | `textarea` | — | — |
| **Requires document approval**<br />`document_approval_msg_fe` | _Please note that your **new content** will be reviewed and accepted by a site administrator_ | `textarea` | — | — |
| **May require version reviewal**<br />`mr_version_revial_msg_fe` | _Please note, your new document **version** might need to be reviewed and approved. This may depend on the content's category AND/OR the content's type. You will be notified whether approval is needed, after you save this content._ | `textarea` | — | — |
| **May require document approval**<br />`mr_document_approval_msg_fe` | _Please note, that your new content might require approval before being accepted. This may depend on the content's category AND/OR the content's type. You will be notified whether approval is needed, after you save this content._ | `textarea` | — | — |
| **Changes applied immediately**<br />`changes_applied_immediately_msg_fe` | _Please note, that document versioning is disabled, thus any changes that you make to this content will be accepted/activated immediately and the previous version will be permanently overwritten_ | `textarea` | — | — |

#### Instructions / URL redirections / etc

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Submit Instructions**<br />`submit_message` | These instructions will be placed at the top of the form, after the form buttons **NOTE:** This can be a language string (add it to your language files) | `textarea` | — | — |
| **Submit Redirect URL hides preview button**<br />`submit_redirect_url_fe` | You can set a custom URL that the user will be redirected after submitting new content. **NOTE:** This will work with even if you click 'Add' or 'Apply' buttons before closing the item **NOTE:** Setting this will hide the preview button while submitting new items | `text` | — | — |
| **Unauthorized Page User can not submit MORE or ANY content**<br />`notauthurl` | Specify the URL / Menu Item ID of the page you wish your registered users to land if they don't have enough rights to create more (or any) content. This could be (for example) the subscriptions plans page if you sell your published content. **NOTE:** If you don't set anything here they the general unauthorized page will be used. | `menuitem` | — | — |

#### Form Security Field Display criteria for CAPTCHA

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use captcha**<br />`use_captcha` | Select when to display a captcha security field, to protect the form from robots | `multilist` | `—` = Use Global<br />`0` = Disable<br />`1` = Guests (Recommended)<br />`2` = Any user | — |
| **Captcha plugin**<br />`captcha` | Select a specific captcha plugin, to override the default setting | `plugins` | `—` = Use Global<br />`0` = Disable | — |
| **Operation Type**<br />`captcha_formop` | When operation is of the selected type | `radio` | `—` = Use Global<br />`0` = Submit (Recommended)<br />`1` = Submit / Edit | — |

### Compatibility

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Edit links**<br />`create_jarticle_form_links_fe` | Create edit links to either Joomla article form or Flexicontent item form | `multilist` | `0` = FC Item form | `0` (FC Item form) |
| **Intro / Full Images**<br />`use_jimages_fe` | Show intro/full images | `radio` | `—` = Use Global<br />`0` = Disable<br />`1` = Enable | — |
| **Urls**<br />`use_jurls_fe` | Show urls | `radio` | `—` = Use Global<br />`0` = Disable<br />`1` = Enable | — |

### Basic Editing

#### New / Existing Items

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use title**<br />`usetitle_fe` | Select to display or hide item title - you can set to automatic in type parameters | `radio` | `—` = Use Global<br />`0` = Hide if automatic<br />`1` = Yes | — |
| **Use Alias**<br />`usealias_fe` | Allow the user to enter the Alias field | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use type**<br />`usetype_fe` | Display type selector to allow changing type of item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use state**<br />`usestate_fe` | Display state selector to allow changing publication state of the item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use access**<br />`useaccess_fe` | Display access selector to allow changing access level of the item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use featured**<br />`usefeatured_fe` | Display featured selector to allow changing featured flag of the item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use tags**<br />`usetags_fe` | Allow tags to be hidden, for user groups that have the Can-Tags Privilege, note the item can still have tags managed | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes<br />`2` = Display only | — |
| **Allow disabling comments**<br />`allowdisablingcomments_fe` | Here you can give the ability to authors/editors to disable comments on Content Items they can edit. If you allow this it is recommended not to show item advanced parameters | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

#### Categories

:::note
Note: You still need **ACL** to prevent multi-category changes. Just hiding them, does not prevent users from changing them ...
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use category**<br />`usemaincat_fe` | If you disable this you need to also set a default category in the type configuration (typically you will create a category with the same name as the type and set it as default) | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Secondary categories**<br />`show_seccats_fe` | — | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Hide if non-editable<br />`2` = Show | — |
| **Featured Categories**<br />`show_featcats_fe` | — | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Hide if non-editable<br />`2` = Show | — |

:::note
Filtering
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Not in item language**<br />`iform_cats_not_in_itemlang_fe` | Either hide the categories in languages that are different than item language, or append language to category title | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Append language name | — |
| **States allowed**<br />`iform_catstates_allowed_fe` | Categories with non allowed states will be hidden, unless the item is already assigned to such a category | `fccheckbox` | — | — |

#### Language

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use language**<br />`uselang_fe` | Allow the user to select language. NOTE: select a default language before disabling this | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes<br />`3` = Yes, without associations<br />`2` = Display only | — |
| **Default language**<br />`default_language_fe` | This is the language that will be pre-selected, particularly useful if you hide the language | `fclanguage` | `_author_lang_` = Use editor's Language<br />`_site_default_` = Use site default Language | — |
| **Disable languages**<br />`disable_languages_fe` | For example you may want to disable language 'ALL' | `fclanguage` | — | — |

#### Language selector

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display as**<br />`langdisplay_fe` | You can display it e.g. as drop-down select or radio buttons | `radio` | `—` = Use Global<br />`2` = Drop-down select<br />`3` = Radio buttons | — |
| **Show flags (radio)**<br />`langdisplay_flags_fe` | Show flag icons | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Show text (radio)**<br />`langdisplay_texts_fe` | Enable to show text such language code | `radio` | `—` = Use Global<br />`0` = No Text<br />`1` = Language code<br />`2` = Title<br />`3` = Native title<br />`4` = Title + Native title | — |

#### Existing items

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow language modifications**<br />`allowlangmods_fe` | Allow user to change the language related properties for -existing- items. Usually, you should prohibit users from changing existing language properties like item language and original content of translation | `fccheckbox` | — | — |

:::note
Please edit more configuration here: Notifications plugin
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow notifying item owner**<br />`allow_owner_notify_fe` | Allow the editor to send update notification (email) to the owner of the current item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes, once per session | — |
| **Allow notifying subscribers (favoring the content item)**<br />`allow_subscribers_notify_fe` | Allow the editor to send update notifications (emails) to the users favouroting the current item | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes, once per session | — |

### Advanced Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Publication Details**<br />`usepublicationdetails_fe` | Select here to allow either: -Basic- Publication Details: (start & finish publishing dates & author alias) to people that can -EDIT- the item. or -All- publication details: (item author & creation date) are available ONLY to Super Admin users. | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Basic (recommended)<br />`2` = All * | — |
| **Metadata Details**<br />`usemetadata_fe` | Recommended to hide or only allow -basic- META data (description and keywords), the rest will be unnecessary & confusing to the users | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Basic (recommended)<br />`2` = All * | — |
| **SEO Configuration**<br />`useseoconf_fe` | Select here to allow user to edit SEO parameters, like custom page title tag | `radio` | `—` = Use Global<br />`0` = No (Recommended)<br />`1` = Yes | — |
| **Display options**<br />`usedisplaydetails_fe` | Select which item display parameters groups you want to be editable in the frontend | `radio` | `—` = Use Global<br />`0` = No (Recommended)<br />`1` = Basic<br />`2` = Advanced | — |
| **3rd party display options**<br />`use3rdpartyparams_fe` | Select to show the display options from 3rd party extensions | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Template Selection**<br />`selecttheme_fe` | Enable selection and configuration of template for frontend user groups with the Templates-Manage Privilege. | `radio` | `—` = Use Global<br />`0` = No (Recommended)<br />`1` = Select<br />`2` = Select and Configure | — |
| **Permissions (ACL)**<br />`permsplacement_fe` | Select here to show permissions to user if these are editable | `radio` | `—` = Use Global<br />`0` = Hide always (even if editable)<br />`1` = Inline<br />`2` = Slider | — |
| **Versions**<br />`versionsplacement_fe` | Inline: open the version comparison in a new browser tab. Popup: open the version comparison in a modal window. The version history table is always shown in the Versions tab. | `radio` | `—` = Use Global<br />`0` = Hide always (even if editable)<br />`1` = Popup<br />`2` = Inline | — |

### Layout

:::note
Using default settings
:::

### Styling and behaviour

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label class**<br />`form_lbl_class_fe` | A class to style the label of the fields | `text` | — | — |
| **Form Container CSS class**<br />`form_container_class_fe` | A list of classnames to add to the outer form container | `text` | — | — |
| **Form Container CSS**<br />`form_container_css_fe` | Set some CSS rules for the form container e.g. 'width:800px;' to avoid fitting problems in the frontend | `textarea` | — | — |
| **Add CSS to edit form**<br />`form_extra_css_fe` | Add extra CSS rules to the submit/edit form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | `editor` | — | — |
| **Add JS to edit form for developers only ***<br />`form_extra_js_fe` | Add extra JS code to the submit/edit form. - Usually you would add JS code executed on DOM Ready Event. - Take care not break JS execution of your Form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | `editor` | — | — |

#### Item Form - Frontend

### Item Form - Backend

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item form layout**<br />`form_ilayout_be` | — | `fclayout` | **Built-in layouts**<br />`tabs` = tabs (Default)<br />`flat` = flat | — |

#### Item Form - Backend

### General Form Behavior

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Optional buttons**<br />`allowbuttons_be` | Select the optional buttons that you want to appear in frontend form | `fccheckbox` | — | — |
| **Placement of buttons**<br />`buttons_placement_be` | Select to display form buttons at the top or bottom of the form | `radio` | `—` = Use Global<br />`-1` = Jtoolbar<br />`0` = Top<br />`1` = Bottom<br />`2` = Left<br />`3` = Right | — |

#### Display approval needed warnings

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Inside form**<br />`approval_warning_inform_be` | Enable this, to show a message inside item form, whether current user can publish new items or if they can self-approve changes to existing items | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **After form submit**<br />`approval_warning_aftersubmit_be` | Enable this, to show an after form submit warning, saying if approval is needed for new item being published or for the changes to existing item becoming active | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **Requires version reviewal**<br />`version_reviewal_msg_be` | _Please note that your new document **version** will be reviewed and approved by a site administrator_ | `textarea` | — | — |
| **Requires document approval**<br />`document_approval_msg_be` | _Please note that your **new content** will be reviewed and accepted by a site administrator_ | `textarea` | — | — |
| **May require version reviewal**<br />`mr_version_revial_msg_be` | _Please note, your new document **version** might need to be reviewed and approved. This may depend on the content's category AND/OR the content's type. You will be notified whether approval is needed, after you save this content._ | `textarea` | — | — |
| **May require document approval**<br />`mr_document_approval_msg_be` | _Please note, that your new content might require approval before being accepted. This may depend on the content's category AND/OR the content's type. You will be notified whether approval is needed, after you save this content._ | `textarea` | — | — |
| **Changes applied immediately**<br />`changes_applied_immediately_msg_be` | _Please note, that document versioning is disabled, thus any changes that you make to this content will be accepted/activated immediately and the previous version will be permanently overwritten_ | `textarea` | — | — |

#### Instructions / URL redirections / etc

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Submit Instructions**<br />`submit_message_be` | These instructions will be placed at the top of the form, after the form buttons **NOTE:** This can be a language string (add it to your language files) | `textarea` | — | — |

### Compatibility

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Edit links**<br />`create_jarticle_form_links` | Create edit links to either Joomla article form or Flexicontent item form | `multilist` | `0` = FC Item form<br />`1` = Joomla Article form | `0` (FC Item form) |
| **Intro / Full Images**<br />`use_jimages_be` | Show intro/full images | `radio` | `—` = Use Global<br />`0` = Disable<br />`1` = Enable | — |
| **Urls**<br />`use_jurls_be` | Show urls | `radio` | `—` = Use Global<br />`0` = Disable<br />`1` = Enable | — |

### Basic Editing

#### New / Existing Items

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use title**<br />`usetitle_be` | Select to display or hide item title - you can set to automatic in type parameters | `radio` | `—` = Use Global<br />`0` = Hide if automatic<br />`1` = Yes | — |
| **Use Alias**<br />`usealias_be` | Allow the user to enter the Alias field | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use type**<br />`usetype_be` | Display type selector to allow changing type of item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use state**<br />`usestate_be` | Display state selector to allow changing publication state of the item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use access**<br />`useaccess_be` | Display access selector to allow changing access level of the item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use featured**<br />`usefeatured_be` | Display featured selector to allow changing featured flag of the item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use tags**<br />`usetags_be` | Allow tags to be hidden, for user groups that have the Can-Tags Privilege, note the item can still have tags managed | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes<br />`2` = Display only | — |
| **Allow disabling comments**<br />`allowdisablingcomments_be` | Here you can give the ability to authors/editors to disable comments on Content Items they can edit. If you allow this it is recommended not to show item advanced parameters | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

#### Categories

:::note
Note: You still need **ACL** to prevent multi-category changes. Just hiding them, does not prevent users from changing them ...
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use category**<br />`usemaincat_be` | If you disable this you need to also set a default category in the type configuration (typically you will create a category with the same name as the type and set it as default) | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Secondary categories**<br />`show_seccats_be` | — | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Hide if non-editable<br />`2` = Show | — |
| **Featured Categories**<br />`show_featcats_be` | — | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Hide if non-editable<br />`2` = Show | — |

:::note
Filtering
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Not in item language**<br />`iform_cats_not_in_itemlang_be` | Either hide the categories in languages that are different than item language, or append language to category title | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Append language name | — |
| **States allowed**<br />`iform_catstates_allowed_be` | Categories with non allowed states will be hidden, unless the item is already assigned to such a category | `fccheckbox` | — | — |

#### Language

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use language**<br />`uselang_be` | Allow the user to select language. NOTE: select a default language before disabling this | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes<br />`3` = Yes, without associations<br />`2` = Display only | — |
| **Default language**<br />`default_language_be` | This is the language that will be pre-selected, particularly useful if you hide the language | `fclanguage` | `_author_lang_` = Use editor's Language<br />`_site_default_` = Use site default Language | — |
| **Disable languages**<br />`disable_languages_be` | For example you may want to disable language 'ALL' | `fclanguage` | — | — |

#### Language selector

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display as**<br />`langdisplay_be` | You can display it e.g. as drop-down select or radio buttons | `radio` | `—` = Use Global<br />`2` = Drop-down select<br />`3` = Radio buttons | — |
| **Show flags (radio)**<br />`langdisplay_flags_be` | Show flag icons | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Show text (radio)**<br />`langdisplay_texts_be` | Enable to show text such language code | `radio` | `—` = Use Global<br />`0` = No Text<br />`1` = Language code<br />`2` = Title<br />`3` = Native title<br />`4` = Title + Native title | — |

#### Existing items

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow language modifications**<br />`allowlangmods_be` | Allow user to change the language related properties for -existing- items. Usually, you should prohibit users from changing existing language properties like item language and original content of translation | `fccheckbox` | — | — |

:::note
Please edit more configuration here: Notifications plugin
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow notifying item owner**<br />`allow_owner_notify_be` | Allow the editor to send update notification (email) to the owner of the current item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes, once per session | — |
| **Allow notifying subscribers (favoring the content item)**<br />`allow_subscribers_notify_be` | Allow the editor to send update notifications (emails) to the users favouroting the current item | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes, once per session | — |

### Advanced Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Publication Details**<br />`usepublicationdetails_be` | Select here to allow either: -Basic- Publication Details: (start & finish publishing dates & author alias) to people that can -EDIT- the item. or -All- publication details: (item author & creation date) are available ONLY to Super Admin users. | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Basic (recommended)<br />`2` = All * | — |
| **Metadata Details**<br />`usemetadata_be` | Recommended to hide or only allow -basic- META data (description and keywords), the rest will be unnecessary & confusing to the users | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Basic (recommended)<br />`2` = All * | — |
| **SEO Configuration**<br />`useseoconf_be` | Select here to allow user to edit SEO parameters, like custom page title tag | `radio` | `—` = Use Global<br />`0` = No (Recommended)<br />`1` = Yes | — |
| **Display options**<br />`usedisplaydetails_be` | Select which item display parameters groups you want to be editable in the frontend | `radio` | `—` = Use Global<br />`0` = No (Recommended)<br />`1` = Basic<br />`2` = Advanced | — |
| **3rd party display options**<br />`use3rdpartyparams_be` | Select to show the display options from 3rd party extensions | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Template Selection**<br />`selecttheme_be` | Enable selection and configuration of template for frontend user groups with the Templates-Manage Privilege. | `radio` | `—` = Use Global<br />`0` = No (Recommended)<br />`1` = Select<br />`2` = Select and Configure | — |
| **Permissions (ACL)**<br />`permsplacement_be` | Select here to show permissions to user if these are editable | `radio` | `—` = Use Global<br />`0` = Hide always (even if editable)<br />`1` = Inline<br />`2` = Slider | — |
| **Versions**<br />`versionsplacement_be` | Inline: open the version comparison in a new browser tab. Popup: open the version comparison in a modal window. The version history table is always shown in the Versions tab. | `radio` | `—` = Use Global<br />`0` = Hide always (even if editable)<br />`1` = Popup<br />`2` = Inline | — |

### Layout

:::note
Using default settings
:::

### Styling and behaviour

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label class**<br />`form_lbl_class_be` | A class to style the label of the fields | `text` | — | — |
| **Form Container CSS class**<br />`form_container_class_be` | A list of classnames to add to the outer form container | `text` | — | — |
| **Form Container CSS**<br />`form_container_css_be` | Set some CSS rules for the form container e.g. 'width:800px;' to avoid fitting problems in the frontend | `textarea` | — | — |
| **Add CSS to edit form**<br />`form_extra_css_be` | Add extra CSS rules to the submit/edit form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | `editor` | — | — |
| **Add JS to edit form for developers only ***<br />`form_extra_js_be` | Add extra JS code to the submit/edit form. - Usually you would add JS code executed on DOM Ready Event. - Take care not break JS execution of your Form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | `editor` | — | — |

#### Item Form - Backend

### Item Form - Both

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Hide description field**<br />`hide_maintext` | Hide the description (maintext) field in the item form (not recommended !!!). TAKE CARE, you will loose the com_content backwards compatibility for these items !!! | `multilist` | `0` = Show<br />`1` = Both<br />`2` = Frontend<br />`3` = Backend | `0` (Show) |

### Styling and behaviour

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add CSS to edit form**<br />`form_extra_css` | Add extra CSS rules to the submit/edit form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | `editor` | — | — |
| **Add JS to edit form for developers only ***<br />`form_extra_js` | Add extra JS code to the submit/edit form. - Usually you would add JS code executed on DOM Ready Event. - Take care not break JS execution of your Form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | `editor` | — | — |

#### Item form eof

## Notifications

### Content submit/change notifications

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable notifications**<br />`enable_notifications` | Select to enable sending notification emails about content submits / updates | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Send emails as BCC**<br />`nf_send_as_bcc` | Enable this to prevent email recipients from seeing other email recipients. **NOTE**: this will force the administrator email of the website to be the main recipient of the notification email | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Debug notifications**<br />`nf_enable_debug` | Enable this to display debugging information (selected mail template, recipients, subject and body) after saving. This option does **not** control whether notifications are sent: notification emails are evaluated and sent on **every save operation**, according to the recipients and states configured above. | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

#### New Content: IN ANY STATE (from authors that can publish)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item in states**<br />`states_notify_new` | Email will be sent when item is any of the selected states | `fccheckbox` | — | — |
| **User groups**<br />`usergrps_notify_new` | Select usergroups using ctrl-click to select multiple | `flexiusergroup` | — | — |
| **User id/names list**<br />`userlist_notify_new` | Enter user ids or names (usernames not full names) and separate the list with comma | `text` | — | — |
| **Extra custom text**<br />`text_notify_new` | Enter an extra custom text to include in the notification email. **NOTE**: This will be filtered as a language string (via JText) | `textarea` | — | — |

#### New Content: PENDING PUBLICATION (from authors that cannot publish)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **User groups**<br />`usergrps_notify_new_pending` | Select usergroups using ctrl-click to select multiple | `flexiusergroup` | — | — |
| **User id/names list**<br />`userlist_notify_new_pending` | Enter user ids or names (usernames not full names) and separate the list with comma | `text` | — | — |
| **Extra custom text**<br />`text_notify_new_pending` | Enter an extra custom text to include in the notification email. **NOTE**: This will be filtered as a language string (via JText) | `textarea` | — | — |

#### Updated Content: NOT NEEDING VERSION APPROVAL (author can publish)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item in states**<br />`states_notify_existing` | Email will be sent when item is any of the selected states | `fccheckbox` | — | — |
| **User groups**<br />`usergrps_notify_existing` | Select usergroups using ctrl-click to select multiple | `flexiusergroup` | — | — |
| **User id/names list**<br />`userlist_notify_existing` | Enter user ids or names (usernames not full names) and separate the list with comma | `text` | — | — |
| **Extra custom text**<br />`text_notify_existing` | Enter an extra custom text to include in the notification email. **NOTE**: This will be filtered as a language string (via JText) | `textarea` | — | — |

#### Updated Content: NEEDING VERSION APPROVAL (author cannot publish, versioning is enabled)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **User groups**<br />`usergrps_notify_existing_reviewal` | Select usergroups using ctrl-click to select multiple | `flexiusergroup` | — | — |
| **User id/names list**<br />`userlist_notify_existing_reviewal` | Enter user ids or names (usernames not full names) and separate the list with comma | `text` | — | — |
| **Extra custom text**<br />`text_notify_existing_reviewal` | Enter an extra custom text to include in the notification email. **NOTE**: This will be filtered as a language string (via JText) | `textarea` | — | — |

## Items Manager

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Is subtype**<br />`is_subtype` | Items of this type are not meant to viewable itself. Instead they are meant to be displayed inside other items. e.g. this will hide the preview button in items manager | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Disable columns**<br />`iman_skip_cols` | Permanently hide columns. User will not be able to turn them ON. Note: 'Single type', mean hide column if filtering by single type | `fccheckbox` | — | — |
| **Custom columns**<br />`items_manager_extra_fields` | Optionally include custom fields columns into the items list: select a field to add it, drag to reorder, click the red icon to remove it. **NOTE:** Do not include custom fields that do not fit or will clutter the list. **NOTE:** Some fields will cause problems when displayed in backend. **NOTE:** You can customize this in every content type configuration. Per content type fields will be displayed, when you - filter - the items manager listing via the content type filter. **NOTE:** Entries that were typed manually in older versions with a display variable and title (e.g. fieldname:display:Title) are kept and shown in parentheses. | `fields` | — | — |
| **Custom filters**<br />`items_manager_custom_filters` | Select custom fields to be added as items manager filters. NOTE: the drop down selector shows supported field types | `filters` | — | — |

## Themes

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default Item layout**<br />`ilayout` | Set a default item layout for all the items of this type (recommended) **NOTE:** every template has one item layout, so this list contains template names **NOTE:** You can override this default item layout inside each item's configuration | `itemlayout` | — | `grid` |
| **Mobile Layout**<br />`ilayout_mobile` | Set a layout to be used when it is detected that current visitor is browsing from a mobile device and also have resolution below the configured minimum, by default the - normal - template is used | `itemlayout` | — | — |
