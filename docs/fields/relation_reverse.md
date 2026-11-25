---
sidebar_position: 29
---

# Reverse relation

Relation Reverse field Plugin for FLEXIcontent

*Plugin : `relation_reverse` — Relation - Reverse*

:::info Source
This page is generated from `plugins/flexicontent_fields/relation_reverse/relation_reverse.xml` and the official FLEXIcontent 5.x language files.
:::

## Reversing

:::note
List items related to 'current' item via the chosen field
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Reverse relation field**<br />`reverse_field` | Select an existing relation field for reversing | `fields` | — | — |

## Editing

#### Related items list

### Related items list

:::note
ITEM FORM: you can customize the display of the **read-only** items list (related to current item)
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Max listed items**<br />`itemcount_form` | Limit the maximum items to listed _Number_ | `text` | — | — |

#### Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

### Items Ordering

:::note
Select property or field to use for ordering the items
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby_form` | Order items by CORE fields/properties | `list` | `—` = FLEXI_ORDER_DEFAULT<br />`date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified -- Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most hits first<br />`rhits` = Popularity -- Least hits first<br />`id` = ID -- Highest First<br />`rid` = ID -- Lowest First<br />`order` = Ordering in current category | `alpha` (Title -- Alphabetical) |

#### CUSTOM field ordering

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable *** overrides CORE order****<br />`orderbycustomfield_form` | Enable this to order by the selected CUSTOM field. NOTE: This setting is ignored if you do not select a custom field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Custom field**<br />`orderbycustomfieldid_form` | Select a custom field to use for ordering. Attention, some types of fields cannot be ordered (file and image fields for example). | `fields` | — | `0` |
| **Direction**<br />`orderbycustomfielddir_form` | Select to creating either an ascending (increasing) or a descending (decreasing) ordered list. | `list` | `ASC` = Ascending<br />`DESC` = Descending | `ASC` (Ascending) |
| **Ordering Method**<br />`orderbycustomfieldint_form` | Select to order alphanumerically (dictionary order) or numerically e.g. in alphanumerically '1000 my-title' is before '200 my-title' | `list` | `0` = Text<br />`1` = Integer<br />`2` = Float<br />`3` = Date | `0` (Text) |

### Item HTML

:::note
Configure the HTML to use for displaying every item
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item HTML**<br />`relitem_html_form` | Enter the HTML to use for each item, **NOTE:** you can use: **__display_text__** -- is replaced with custom text created according to parameters **&#123;&#123;fieldname&#125;&#125;** or **&#123;&#123;fieldname##displayvar&#125;&#125;** -- is replaced with HTML display of each field **&#123;&#123;fieldname##label&#125;&#125;** -- is replaced with label of each field **%%language_string%%** -- is replaced with the language string Finally, you can use item related replacements: __item_url__, __item_title_escaped__, __item_tooltip__ and item properties like: &#123;item-&gt;id&#125;, &#123;item-&gt;title&#125;, etc | `editor` | — | `__display_text__` |

#### Composition of __display_text__

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Custom Text**<br />`displayway_form` | Display Item ID (e.g. for use with Joomla plugin) or Item Title (e.g. for linking to the content item) | `list` | `0` = Item ID<br />`1` = Item Title | `1` (Item Title) |
| **Add Item Link**<br />`addlink_form` | Enable this add a hovering tooltip with e.g. read more message | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Add Link Tooltip**<br />`addtooltip_form` | Enable this add a hovering tooltip with e.g. read more message | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_form` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_form` | This text is placed immediately **after** every field value | `text` | — | — |
| **Value separator (item form)**<br />`separator` | Choose a separator to separate the values in backend/frontend item forms (placed between values) | `list` | `0` = Space<br />`1` = Line break<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters) | `1` (Line break) |
| **Opening text for Field**<br />`opentag_form` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag_form` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

#### Related items list

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
| **Max listed items**<br />`itemcount` | Limit the maximum items to listed _Number_ | `text` | — | — |
| **Items list viewable**<br />`itemslist_acclvl` | Only users that have this access level (belong to a usergroup that has it) will be able to view the items list | `accesslevel` | — | `1` |

#### Related items list

### Filter items

:::note
Items matching all of the selected criteria will be items included, Note: Leave blank to ignore the specific limitation
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category**<br />`reverse_scope_category` | Select Category | `flexicategories` | — | — |
| **Types**<br />`reverse_scope_types` | Select types you want to include or exclude | `types` | — | — |

#### Other Scope Limits

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Same Language Only**<br />`samelangonly` | When this is enabled only items that have the same language as the item will be listed | `radio` | `0` = No limit<br />`1` = Yes | `1` (Yes) |
| **Use publish up/down dates**<br />`use_publish_dates` | Will skip selected items when their publication dates expire | `radio` | `0` = No limit<br />`1` = Yes | `1` (Yes) |
| **Only published items**<br />`onlypublished` | If this is disabled unpublished items will be shown too | `radio` | `0` = No limit<br />`1` = Yes | `1` (Yes) |
| **Item owned by**<br />`ownedbyuser` | Items owned by (a) any user or (b) by user currently editting the item by item owning the current item | `radio` | `0` = Any user<br />`1` = editing user<br />`2` = item owner | `0` (Any user) |

### Items Ordering

:::note
Select property or field to use for ordering the items
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Order by CORE field/properties**<br />`orderby` | Order items by CORE fields/properties | `list` | `date` = Added -- Oldest first<br />`rdate` = Added -- Most Recent first<br />`modified` = Modified -- Most Recent first<br />`alpha` = Title -- Alphabetical<br />`ralpha` = Title -- Alphabetical Reverse<br />`author` = Author -- Alphabetical<br />`rauthor` = Author -- Alphabetical Reverse<br />`hits` = Popularity -- Most hits first<br />`rhits` = Popularity -- Least hits first<br />`id` = ID -- Highest First<br />`rid` = ID -- Lowest First<br />`commented` = Most Commented<br />`rated` = Best Rated<br />`order` = Ordering in current category<br />`jorder` = Ordering (Global)<br />`random` = Random | `alpha` (Title -- Alphabetical) |

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
