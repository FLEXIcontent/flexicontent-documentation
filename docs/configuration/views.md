---
sidebar_position: 5
---

# Views

Settings shared by the frontend views (tags, authors, search, favourites, etc.).

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

### Item view

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Show Title**<br />`show_title` | Show Title | — | `1` |
| **Title linkable**<br />`link_titles` | If Yes, the Title of Items will be hyperlinked to the item itself. | — | `1` |
| **Show introductory text**<br />`show_intro` | Introductory Text is used to present the content in **category** and other multi-item listings, you can choose here whether to show it when the content is displayed in full view, thus prepending it before content's full text | — | `1` |

#### Comments

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable comments integration**<br />`comments` | Enable commenting system integration. **NOTE:** This parameter may be overridden for types, categories, single items or menu items. **NOTE:** By setting to disable you may manually trigger (description field will trigger all by default), appropriate Joomla content plugin of your commenting system to insert comments via a Joomla CONTENT Event. In case of adding comments this way, you cannot use the parameter 'Disable comments' in the item form, instead you will need to do it the way your commenting system recommends, e.g. by inserting some special text inside the description | — | `0` |

:::note
Manual comments integration
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Backend administration link**<br />`comments_admin_link` | If you add comments manually (e.g. by triggering a Joomla plugin), then you can add the full link to the backend administration of the component, so that you integrate it, into the FLEXIcontent dashboard | — | — |

#### Item Hits Configuration

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Count unique hits only**<br />`hits_count_unique` | By enabling this parameter item hits will be incremented only by unique visitors. NOTE: this effects all following options | — | `0` |
| **Minutes between unique hits**<br />`hits_mins_to_unique` | Minimum of minutes before counting a new hit from from same IP | — | `600` |
| **Skip (blocked) IPs**<br />`hits_skip_ips` | The IPs in the following list will not increment hits | — | `1` |
| **IP List**<br />`hits_ips_list` | The list of IPs that will never produce a hit | — | `127.0.0.1` |
| **Skip bots**<br />`hits_skip_bots` | Do not count hits from non-human visitors | — | `1` |
| **List of bots**<br />`hits_bots_list` | The list of names of the bots | — | `bot,spider,crawler,search,libwww,archive,slurp,teoma` |

### Legacy views

:::note
- **Author's Items** and **My Items** always use category view. Usually only 1 menu item is needed. - Using category view allows using 'Templates' And 'List' configuration.
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Tagged Items**<br />`tags_using_catview` | Enable this to create category-based links, thus being able to use 'category' layouts and other 'item list' configuration like advanced filtering, etc, and also makes possible to limit to specific categories | — | `0` |
| **Favoured Items**<br />`favs_using_catview` | Enable this to create category-based links, thus being able to use 'category' layouts and other 'item list' configuration like advanced filtering, etc, and also makes possible to limit to specific categories | — | `0` |

### Directory view

:::note
Displays category lists. It has no default menu item. For more configuration options create a menu item
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Category List Order**<br />`cat_orderby` | Ordering of the Category List, available options depend on the category properties available e.g. category name, backend confiured ordering, etc | — | `order` |
| **Categories List limit**<br />`catlimit` | Max categories listed in categories lists | — | `100` |
