---
sidebar_position: 28
---

# Relation

Relation field Plugin for FLEXIcontent

:::info Source
This page is generated from `plugins/flexicontent_fields/relation/relation.xml` and the official FLEXIcontent 5.x language files.
:::

## Editing

#### Editing

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use field in a group**<br />`use_ingroup` | Enable to allow field to be part of field group, that is created via 'Field Group' field. NOTE: You should then select this field in ONLY ONE field group | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |

#### Number of values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Allow multiple values**<br />`allow_multiple` | Allow more than 1 value for this field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Multiple per value**<br />`multiple_per_value` | — | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Add position**<br />`add_position` | Select to add value inline (show add button at every value) or append them to the bottom of the value list | `multilist` | `0` = Append to bottom<br />`1` = Inline append<br />`2` = Inline prepend<br />`3` = Inline both | `3` (Inline both) |

#### Values Creation

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default values**<br />`default_values` | _itemid1:catid1 , itemid2:catid2 , itemid3:catid3_ | `text` | — | — |
| **Usage of default**<br />`default_value_use` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

#### Options per value

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **max # options**<br />`max_values` | The max number of options that can be selected in each value of the field | `text` | — | `0` |
| **min # options**<br />`min_values` | The min number of options that must be selected in each value of the field | `text` | — | `0` |
| **exact # options**<br />`exact_values` | The exact number of options that must be selected in each value of the field | `text` | — | `0` |

### Form field

:::note
Configuration of the form field such us maximum characters
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Max listed items**<br />`itemcount` | Limit the maximum items to listed _Number_ | `text` | — | `5000` |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Related items selector

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Prefix titles with state**<br />`itemselector_prepend_item_state` | This will prepend item state to the item titles | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **FLEXI_RIFLD_PREPEND_ITEM_TYPE**<br />`itemselector_prepend_item_type` | — | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **FLEXI_RIFLD_PREPEND_ITEM_ID**<br />`itemselector_prepend_item_id` | — | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Append fields**<br />`itemselector_append_fields` | — | `fields` | — | — |
| **Maximum Title Chars**<br />`maxtitlechars` | Maximum character length for title, title longer than this will be cut off | `text` | — | `40` |
| **Items Ordering**<br />`orderby_form` | Select property or field to use for ordering the items | `list` | `date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified -- Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most hits first<br />`rhits` = Popularity -- Least hits first<br />`id` = ID -- Highest First<br />`rid` = ID -- Lowest First<br />`order` = Ordering in current category | `alpha` (Title -- Alphabetical) |

#### List of selected items

:::note
NOTE: Combine 'Allow sorting' with 'Manual order' in viewing TAB
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow sorting**<br />`selected_items_sortable` | Make the selected items list to be sortable. NOTE: in viewing TAB and select 'Manual order', otherwise the order will not be used during viewing, thus confusing your authors | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Category selector

:::note
User will need to select category, then items in the selected category will be listed
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Selectable categories**<br />`method_cat` | Select categories that will be shown | `multilist` | `1` = All<br />`2` = Exclude<br />`3` = Include | `1` (All) |
| **Categories**<br />`catids` | Select Category you want to include or exclude | `flexicategories` | — | — |
| **Include subcategories**<br />`usesubcats` | Allow usage of all subcategories of the selected categories. This way you don't have to edit the field every time a new subcategory is created. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Use ACL**<br />`use_cat_acl` | Only include categories that are creatable / editable by the item editor | `multilist` | `0` = No<br />`1` = Creatable / Editable | `1` (Creatable / Editable) |

### Field filters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Custom filters**<br />`itemselector_custom_filters` | Filter items list using other fields | `filters` | — | — |
| **Performance**<br />`load_method` | Display or hide label of this field | `radio` | `3` = Load initially<br />`4` = Load only if 1+ filters active | `3` (Load initially) |

### Selectable items

:::note
Criteria for deciding which items are available for selection as related items
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **List sub category items**<br />`subcat_items` | When a category is selected the sub-category items will be listed too | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Type scope

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Method**<br />`method_types` | Choose a method to filter content | `multilist` | `1` = All<br />`2` = Exclude<br />`3` = Include | `1` (All) |
| **Types**<br />`types` | Select types you want to include or exclude | `types` | — | — |

#### Other Scope Limits

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Same Language Only**<br />`samelangonly` | When this is enabled only items that have the same language as the item will be listed | `radio` | `0` = No limit<br />`1` = Yes | `1` (Yes) |
| **Use publish up/down dates**<br />`use_publish_dates` | Will skip selected items when their publication dates expire | `radio` | `0` = No limit<br />`1` = Yes | `1` (Yes) |
| **Only published items**<br />`onlypublished` | If this is disabled unpublished items will be shown too | `radio` | `0` = No limit<br />`1` = Yes | `1` (Yes) |
| **Item owned by**<br />`ownedbyuser` | Items owned by (a) any user or (b) by user currently editting the item by item owning the current item | `radio` | `0` = Any user<br />`1` = editing user<br />`2` = item owner | `0` (Any user) |

#### Editing

## Viewing

#### Viewing

### Basic

#### Display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

#### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Export

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Backend View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Backend view appearance**<br />`backend_view_appearance` | How this field's value is displayed in the admin items list. Overrides the global 'Custom columns appearance' setting when not set to Default. | `multilist` | `0` = Default<br />`1` = Check mark<br />`2` = Clean up HTML and trim | `0` (Default) |
| **Trim length (characters)**<br />`backend_view_trim_chars` | Number of characters to keep after stripping HTML tags. | `text` | — | `100` |

### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |

:::note
For configuration options, common to all layouts, please see other Tabs of this tab-set
:::

### Related items list

:::note
Display options: -- Item list (related to current item)
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Items list viewable**<br />`itemslist_acclvl` | Only users that have this access level (belong to a usergroup that has it) will be able to view the items list | `accesslevel` | — | `1` |

#### Related items list

### Filter items

:::note
Items matching all of the selected criteria will be items included, Note: Leave blank to ignore the specific limitation
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Same Language Only**<br />`samelangonly_view` | When this is enabled only items that have the same language as the item will be listed | `radio` | `-1` = Same as edit<br />`1` = Yes | `-1` (Same as edit) |
| **Use publish up/down dates**<br />`use_publish_dates_view` | Will skip selected items when their publication dates expire | `radio` | `-1` = Same as edit<br />`1` = Yes | `1` (Yes) |
| **Only published items**<br />`onlypublished_view` | If this is disabled unpublished items will be shown too | `radio` | `-1` = Same as edit<br />`1` = Yes | `1` (Yes) |
| **Item owned by**<br />`ownedbyuser_view` | Items owned by (a) any user or (b) by user currently editting the item by item owning the current item | `radio` | `-1` = Same as edit<br />`1` = editing user<br />`2` = item owner | `-1` (Same as edit) |

### Items Ordering

:::note
NOTE: Combine 'Manual order' with 'Allow sorting' in editing TAB
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby` | Order items by CORE fields/properties | `list` | `date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified -- Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most hits first<br />`rhits` = Popularity -- Least hits first<br />`id` = ID -- Highest First<br />`rid` = ID -- Lowest First<br />`commented` = Most Commented<br />`rated` = Best Rated<br />`order` = Ordering in current category<br />`jorder` = Ordering (Global)<br />`random` = Random<br />`manual` = Manual order (as sorted in edit form) | `alpha` (Title -- Alphabetical) |

#### CUSTOM field ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`orderbycustomfield` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Custom field**<br />`orderbycustomfieldid` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | `fields` | — | `0` |
| **Direction**<br />`orderbycustomfielddir` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `list` | `ASC` = Ascending<br />`DESC` = Descending | `ASC` (Ascending) |
| **Ordering Method**<br />`orderbycustomfieldint` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `list` | `0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date | `0` (Text) |

### Item HTML

:::note
Configure the HTML to use for displaying every item
:::

:::note
NOTE: Configuration of this can be overriden for some views, via the 'Total info' TAB
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item HTML**<br />`relitem_html` | Enter the HTML to use for each item, **NOTE:** you can use: **__display_text__** -- is replaced with custom text created according to parameters **&#123;&#123;fieldname&#125;&#125;** or **&#123;&#123;fieldname##displayvar&#125;&#125;** -- is replaced with HTML display of each field **&#123;&#123;fieldname##label&#125;&#125;** -- is replaced with label of each field **%%language_string%%** -- is replaced with the language string Finally, you can use item related replacements: __item_url__, __item_title_escaped__, __item_tooltip__ and item properties like: &#123;item-&gt;id&#125;, &#123;item-&gt;title&#125;, etc | `editor` | — | `__display_text__` |

#### Composition of __display_text__

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Custom Text**<br />`displayway` | Display Item ID (e.g. for use with Joomla plugin) or Item Title (e.g. for linking to the content item) | `list` | `0` = Item ID<br />`1` = Item Title | `1` (Item Title) |
| **Add Item Link**<br />`addlink` | Enable this add a hovering tooltip with e.g. read more message | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Add Link Tooltip**<br />`addtooltip` | Enable this add a hovering tooltip with e.g. read more message | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Preset configurations**<br />`prx_sfx_open_close_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking) | — |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |
| **Value separator (frontend views)**<br />`separatorf` | Choose a separator to separate the values in frontend views (placed between values) | `multilist` | `0` = Space<br />`1` = Line break<br />`6` = Horizontal line<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters)<br />`7` = Custom separator | `1` (Line break) |
| **Custom separator**<br />`separatorf_custom` | — | `text` | — | — |
| **Opening text for Field**<br />`opentag` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

#### Related items list

### Submit related button

:::note
Display options: -- Auto-relate submission ** Allows to submit new item that is automatically related to the currently viewed item **
This is useful for creating e.g. a new **product review**, a new **job application**, without the user having to select the **product** being reviewed or the **job** being applied
:::

:::note
NOTE: Configuration of this can be overriden for some views, via the 'Total info' TAB
:::

:::note
Note: your form needs to have a RELATION-REVERSE field !! that will be configured to reverse this field !!
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show button**<br />`auto_relate_curritem` | This will show a submit link (new item form) that will create an item that is related to current item | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |

#### Viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Button position**<br />`auto_relate_position` | Place the button before or after the item list | `radio` | `0` = Before<br />`1` = After<br />`2` = Both | `0` (Before) |
| **Button viewable**<br />`auto_relate_acclvl` | Only users that have this access level (belong to a usergroup that has it) will be able to view the button. NOTE: this will only hide the button, you still need to configure the submit ACL and the submit menu item for users that will be able to see it. NOTE: you may want some user to be able to see the button, but not be able to submit because of ACL, for this case enable the 'Show to unauthorized below' !! | `accesslevel` | — | `1` |
| **Show to unauthorized**<br />`auto_relate_show_to_unauth` | Enable this to show submit button to unauthorized users. If you do this, then remember that: -- unless the chosen submit menu item allows UNAUTHORIZED users to submit a. **guest** users are redirected to **login/register** screen b. **uauthorized logged** users are redirected to URL configured in - component settings, overidden by url in - content type settings, overidden by url in - submit menu item | `radio` | `0` = No<br />`1` = Yes, exclude guests<br />`2` = Yes | `0` (No) |

#### Customize

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Submit menu itemid ***<br />`auto_relate_menu_itemid` | Enter the ID of the submit menu item. Important configuration will be retrieved from the choosen submit menu item, e.g. -- **content TYPE** of the new related item (being submitted), usually you should select a specific content type in the menu item, like 'product review' or 'job application' -- **category(-ies)**, normally these are controlled by ACL, but in this case it maybe appropriate to select category(-ies) in the menu item ! | `fcmenuitem` | `—` = Select | — |
| **Button title**<br />`auto_relate_submit_title` | This is the title that will be displayed instead of 'Submit new', e.g. use a language string like MYTXT_SUBMIT_TEXT | `text` | — | — |
| **Button text**<br />`auto_relate_submit_text` | This is the text that will be displayed instead of 'Click to submit more', e.g. use a language string like MYTXT_SUBMIT_TEXT_TIP | `text` | — | — |
| **Form field message**<br />`auto_relate_submit_mssg` | Reverse relation field will show this text, inside the item form | `text` | — | — |

### Total count

:::note
Display options: -- Total counter ** A more compact display that allows skipping or compacting the item list e.g. in category view**
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable total**<br />`show_total_only` | Enable this to show only a total count of related items instead of showing the related items list. | `multilist` | `0` = No<br />`1` = Yes<br />`2` = Yes, hide zero | `0` (No) |
| **Enable in views**<br />`total_in_view` | You can turn on/off the above parameter depending on current flexicontent view | `fccheckbox` | — | — |
| **Append text**<br />`total_append_text` | Enter to append some text to the total count | `text` | — | — |

#### Show extra information

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Submit related button**<br />`total_show_auto_btn` | Enable to also show the Submit related button, (if enabled and configured above) | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Related items list**<br />`total_show_list` | Enable to also show items list, (below you can override item list configuration) | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |

#### Override default

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item HTML**<br />`total_relitem_html` | Enter the HTML to use for each item, **NOTE:** you can use: **__display_text__** -- is replaced with custom text created according to parameters **&#123;&#123;fieldname&#125;&#125;** or **&#123;&#123;fieldname##displayvar&#125;&#125;** -- is replaced with HTML display of each field **&#123;&#123;fieldname##label&#125;&#125;** -- is replaced with label of each field **%%language_string%%** -- is replaced with the language string Finally, you can use item related replacements: __item_url__, __item_title_escaped__, __item_tooltip__ and item properties like: &#123;item-&gt;id&#125;, &#123;item-&gt;title&#125;, etc | `editor` | — | `__display_text__` |

#### Viewing

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

#### Filtering

### Values

#### Filter value comparison

:::note
... if field is multi-valued (item form) ... and has a multi-valued filter appearance
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Require ALL selected values**<br />`filter_values_require_all` | Usually you will include items found to have any of the selected values. -- You can select to **require all selected** filter values to be matched for the found items. -- **WARNING** to developers of new field types: this will not work properly if your field saves SAME field value more than once for the same item. So in such a case do not add this option to your field ! | `radio` | `0` = No<br />`1` = Yes, slower | `0` (No) |
| **Require ANY / ALL inline tip**<br />`filter_values_require_all_tip` | Select to show information if ANY or ALL selected filter values of this filter are required | `radio` | `0` = Hide<br />`1` = Show | `0` (Hide) |

### Category-based views

#### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `multilist` | `0` = Drop-down selector<br />`1` = Text Search<br />`7` = Slider<br />`2` = Drop-down selector (range)<br />`3` = Text Search (range)<br />`8` = Slider (range)<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

#### Drop-down selector

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Customize default option (all values)**<br />`filter_usefirstoption` | Enable to customize the first option of the filter (=all values) . NOTE: this is used only in the case of Drop-Down Select, and also if field label is not placed inside the selector | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default Option Text (e.g. All colours)**<br />`filter_firstoptiontext` | Text of first option of the Drop-Down Select e.g. 'All colours' or FLEXI_ALL etc. **NOTE**: This option has no value **NOTE**: This text is language-filtered so you can enter a language replaceable string | `text` | — | `FLEXI_ALL` (All) |

#### Slider

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Slider data**<br />`slider_display_config` | Either use found field values, or specify your custom range of values | `multilist` | `1` = Found values<br />`2` = Custom values | `1` (Found values) |
| **Custom values**<br />`slider_custom_range` | Custom range of values, please use values that exist in the field !, for format, see example format, enter comma separated values: percentage%: 'value', and instead of 0% or 100%, you must use 'min': 'value' and 'max':'min': 'value' | `textarea` | — | `'min': '', '25%': '50', '50%': '150', '75%': '600', 'max': ''` |
| **Custom labels**<br />`slider_custom_labels` | Custom labels to match the values, please enter a ## separated labels without start/end quotes | `textarea` | — | `label_any ## label_50 ## label_150 ## label_600 ## label_any` |
| **Labels are language strings**<br />`slider_custom_labels_jtext` | Set this to yes to treat labels as language strings, remember to add these to your Joomla language overrides manager or in other loaded language files | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Prefix / Suffix

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_filter` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_filter` | This text is placed immediately **after** every field value | `text` | — | — |
| **Opening text for Field**<br />`opentag_filter` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag_filter` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

### Advanced Search View

#### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter_s` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `multilist` | `0` = Drop-down selector<br />`1` = Text Search<br />`7` = Slider<br />`2` = Drop-down selector (range)<br />`3` = Text Search (range)<br />`8` = Slider (range)<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter_s` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items_s` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values_s` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

#### Drop-down selector

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Customize default option (all values)**<br />`filter_usefirstoption_s` | Enable to customize the first option of the filter (=all values) . NOTE: this is used only in the case of Drop-Down Select, and also if field label is not placed inside the selector | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default Option Text (e.g. All colours)**<br />`filter_firstoptiontext_s` | Text of first option of the Drop-Down Select e.g. 'All colours' or FLEXI_ALL etc. **NOTE**: This option has no value **NOTE**: This text is language-filtered so you can enter a language replaceable string | `text` | — | `FLEXI_ALL` (All) |

#### Slider

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Slider data**<br />`slider_display_config_s` | Either use found field values, or specify your custom range of values | `multilist` | `1` = Found values<br />`2` = Custom values | `1` (Found values) |
| **Custom values**<br />`slider_custom_range_s` | Custom range of values, please use values that exist in the field !, for format, see example format, enter comma separated values: percentage%: 'value', and instead of 0% or 100%, you must use 'min': 'value' and 'max':'min': 'value' | `textarea` | — | `'min': '', '25%': 500, '50%': 2000, '75%': 10000, 'max': ''` |
| **Custom labels**<br />`slider_custom_labels_s` | Custom labels to match the values, please enter a ## separated labels without start/end quotes | `textarea` | — | `label_any ## label_500 ## label_2000 ## label_10000 ## label_any` |
| **Labels are language strings**<br />`slider_custom_labels_jtext_s` | Set this to yes to treat labels as language strings, remember to add these to your Joomla language overrides manager or in other loaded language files | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Prefix / Suffix

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_filter_s` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_filter_s` | This text is placed immediately **after** every field value | `text` | — | — |
| **Opening text for Field**<br />`opentag_filter_s` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag_filter_s` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

#### Filtering
