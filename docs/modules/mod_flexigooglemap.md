---
sidebar_position: 7
---

# Google map

FLEXIcontent provides six frontend modules for displaying items, categories, search forms, filters, maps and tag clouds. Configure a module from **Extensions → Modules**.

> Module to display a googlemap with item like marker, position is done by flexicontent address field Thanks for helping : Georgios Papadakis and Marc Studer

:::info Source
This page is generated from `modules/mod_flexigooglemap/mod_flexigooglemap.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

### Template Layout

:::note
Please set layout parameters in **Layout: ... TAB**. CSS/HTML developers please read: ** Custom templates HOW-TO **
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout**<br />`layout` | Choose a layout to render your module | `fclayout` | — | `news` |
| **Hide map when empty**<br />`hide_map_when_empty` | — | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

### Map API

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Choose your API**<br />`mapapi` | Choose your API, if you have a Googlemap Key you can use this api, or choose Openstreetmap for a map without limitation | `radio` | `googlemap` = Googlemap<br />`openstreetmap` = Openstreetmap | `googlemap` (Googlemap) |
| **Category selection**<br />`catidmode` | Use current category or select an specific category in dropdown | `radio` | `0` = Specific categories<br />`1` = Current category<br />`2` = Current item | `0` (Specific categories) |
| **Method**<br />`method_category` | Excluded: Display any item(s) except the currently(s) selected categorie(s), Include: Display any item(s) in selected categories | `radio` | `0` = Include<br />`1` = Exclude | `0` (Include) |
| **Category**<br />`catid` | Module that displays items as points on a map (Google map), using the coordinates from an address-international FLEXIcontent field | `flexicategories` | — | — |
| **Extra categories**<br />`treeinclude` | Include parent/children of selected categories. **NOTE**: 'other categories of item' is used only in frontend pages that display an item | `list` | `0` = None<br />`1` = Children categories<br />`5` = Children categories, but exclude selected categories<br />`2` = Ancestor categories<br />`3` = Ancestor & Children Categories | `1` (Children categories) |
| **Address field**<br />`fieldaddressid` | Tip id of your address field | `fields` | — | — |
| **Tile (Map) Server URL**<br />`os_tile_server_url` | Enter a custom tile server URL (of Openstreet Maps). If you are going to be having a lot of traffic it is best to setup your own tiles server for hosting your map tiles, e.g. https://&#123;s&#125;.tile.openstreetmap.org/&#123;z&#125;/&#123;x&#125;/&#123;y&#125;.png | `text` | — | `https://&#123;s&#125;.tile.openstreetmap.org/&#123;z&#125;/&#123;x&#125;/&#123;y&#125;.png` |
| **API key**<br />`apikey` | Tip your API google map key if you need more than 25000 display by month | `text` | — | — |

### Map display

#### Map bounding container

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Width**<br />`width` | Tip width of map with px | `text` | — | `300px` |
| **MOD_FLEXIGOOGLEMAP_height**<br />`height` | tip height of map with px | `text` | — | `60vh` |

#### Map basic configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Map type**<br />`maptype` | Choose map type | `list` | `ROADMAP` = Road map<br />`HYBRID` = Hybride<br />`SATELLITE` = Satellite<br />`TERRAIN` = Terrain | `ROADMAP` (Road map) |
| **Zoom limit**<br />`maxzoommarker` | Set zooming limit, when map displaying non-grouped markers (single markers) | `number` | — | `18` |
| **Initial map padding (%)**<br />`mappadding` | Set initial map's padding distance. This is distance of markers or clusters to the map edge. Value is a percent of map area | `number` | — | `50` |
| **Max # markers**<br />`count` | Select a number to limit marker and speed up map display. For now google api can't load more 250 markers (in relation with your title and url size) | `list` | `—` = Display all points<br />`DESC LIMIT 10` = 10<br />`DESC LIMIT 50` = 50<br />`DESC LIMIT 100` = 100<br />`DESC LIMIT 150` = 150<br />`DESC LIMIT 200` = 200<br />`DESC LIMIT 250` = 250<br />`DESC LIMIT 300` = 300<br />`DESC LIMIT 350` = 350<br />`DESC LIMIT 400` = 400<br />`DESC LIMIT 450` = 450<br />`DESC LIMIT 500` = 500<br />`DESC LIMIT 1000` = 1000 | — |

#### Geo Location options

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Zoom map to visitor**<br />`geo_locate` | On load map will be zoom to visitor's location | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Near Me button**<br />`geo_locate_btn` | Add button to re-center map to visitor's location | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Near Me zoom selection**<br />`geo_locate_zoom_sel` | Add selector to select map zoom level to visitor's location | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Near Me zoom default**<br />`geo_locate_zoom_def` | Default zoom level for near-me locations | `number` | — | `10` |

#### Marker display

:::note
Per location custom marker (via item form), and a fallback (a default) icon that will be used for locations without a custom icon
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Per location**<br />`use_custom_marker` | Use custom icon per map location, if this was specified in item form. The default icon will be used for locations without a custom icon | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Fallback

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default Marker**<br />`markermode` | Select specific image, or you can select letter mode to create a marker with a Letter inside | `radio` | `-1` = API 's default icon<br />`0` = Specific image<br />`1` = Letter mode | `-1` (API 's default icon) |
| **Specific image**<br />`markerimage` | Choose or upload your marker image | `fcmedia` | — | — |
| **Color marker**<br />`markercolor` | Choose your color marker | `list` | `red` = Red<br />`green` = Green | `redpt` |
| **Letter marker**<br />`lettermarker` | Type your letter marker | `text` | — | `A` |

#### Behaviour and style

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Scroll wheel zoom**<br />`usescrollmouse` | Enable disable Scroll wheel zoom | `radio` | `false` = No<br />`true` = Yes | `true` (Yes) |
| **Animation**<br />`animationmarker` | If you choose yes all marker will be display with bounce effect at first. This is doesn't work for grouped icons | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Map style Gen style**<br />`mapstyle` | Copie Past json code done by snazzy mpas. BECARFULL USE [] AT START AND END OF VALUE _[Your style code]_ | `textarea` | — | — |

#### Marker grouping

:::note
Group markers as a total number, to prevent many markers showing very close together
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Group markers**<br />`clustermode` | This groups together markers in same zone (area). The total number of markers will be shown when map is zoomed out | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Marker image**<br />`imgcluster` | Define a icon image for cluster (only for Googlemap api) | `fcmedia` | — | — |
| **Grid size**<br />`gridsize` | Size of grid for grouped marker together. A big size create 1 big marker | `text` | — | `50` |
| **Group at zoom level**<br />`maxzoom` | The zoom level at which cluster effect is activated, if user zooms in more than this limit, the cluster effect will be deactivated | `text` | — | `17` |

### Marker actions

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Click action**<br />`info_popup` | Action to do when clicking on the marker | `multilist` | `0` = None<br />`1` = Info window<br />`2` = Item link | `1` (Info window) |
| **Target window**<br />`marker_clicktarget` | Open link in | `multilist` | `—` = - No target -<br />`_blank` = New Window/Tab<br />`_parent` = Parent Frame<br />`_self` = Same Frame/Window/Tab<br />`_top` = Top of window<br />`_popup` = Modal popup window<br />`_modal` = Html Popup (without js) | `_popup` (Modal popup window) |

#### Modal / Popup Options

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item layout**<br />`ilayout` | Set a specific layout for this item | `itemlayout` | — | — |
| **Width**<br />`modal_width` | Tip width of map with px | `number` | — | — |
| **Height**<br />`modal_height` | Set Height of modal /popup . Leave empty for fullscreen size | `number` | — | — |

#### Info windows

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Custom display**<br />`info_windows_custom_display` | This is by default same as the popup windows | `radio` | `0` = Same display as markers list | `0` (Same display as markers list) |

### Markers list

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Markers List**<br />`use_dynamic_marker_list` | Show and dynamically update a list of markers, that currently visible according to current viewport of the map. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Sync markers List to visible markers**<br />`marker_list_update_to_map_bounds` | Sync markers List to display only markers visible in the map bounds | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Marker list wrapping

:::note
Limit at which marker list will be wrapped
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Marker list container wrap limit (pixels)**<br />`marker_list_wrap_limit` | At this width the marker list will wrap to the bottom of the map | `text` | — | `1200` |
| **Height when wrapped (Map)**<br />`map_height_wrapped` | tip height of map with px | `text` | — | `45vh` |
| **Height when wrapped (Marker-list)**<br />`marker_list_height_wrapped` | tip height of map with px | `text` | — | `45vh` |

#### Markers List options

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Marker info display**<br />`infotextmode` | Basic mode will display only item title and Custom mode can insert custom HTML with FLEXIcontent fields | `radio` | `0` = Basic (title and address)<br />`1` = Custom with HTML and fields | `0` (Basic (title and address)) |
| **Address**<br />`useadress` | If you choose yes, address will be display in info windows | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Custom HTML with fields replacements**<br />`custom_html_with_replacements` | Enter the HTML to use for each item, **NOTE: address-field within a field-group works. Add fields of address-field field-group and these will be rendered together with every value of the address-field **NOTE:** you can use: &#123;__address__&#125; to replace with value of current address field **&#123;&#123;fieldname&#125;&#125;** or **&#123;&#123;fieldname##displayvar&#125;&#125;** -- is replaced with HTML display of each field **&#123;&#123;fieldname##label&#125;&#125;** -- is replaced with label of each field **%%language_string%%** -- is replaced with the language string Finally, you can use item related replacements: __item_url__, __item_title_escaped__, __item_tooltip__ and item properties like: &#123;item-&gt;id&#125;, &#123;item-&gt;title&#125;, etc | `editor` | — | `&#123;item-&gt;title&#125; &#123;__address__&#125;` |

#### Link to item (Read more button)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`uselink` | This will link to the content item that contains the marker's address | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Target link**<br />`linkmode` | choose if link open a new windows or loading item in same view | `radio` | `_blank` = New window<br />`—` = Same window | — |
| **Force itemid**<br />`forced_itemid` | You can use an specific itemid to manage display item after link. | `text` | — | — |
| **Text for read more**<br />`readmore` | Insert your text for reamore link. You can use MOD_FLEXIGOOGLEMAP_READMORE_TXT by defaut for multilangue link _Readmore_ | `text` | — | — |

#### Directions button (Open marker Location in new window)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`usedirection` | This will display a link to open a new window with directions for current marker location | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Name of link**<br />`directionname` | You can change name of direction link or use MOD_FLEXIGOOGLEMAP_DIRECTIONNAME_TXT for translation string _Directions_ | `text` | — | — |

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

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Modules field caching label**<br />`cache` | Modules field caching desc | `list` | `1` = Use global<br />`0` = Modules field value nocaching | `1` (Use global) |
