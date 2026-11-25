---
sidebar_position: 7
---

# Default menus

Default menu items used when the component creates links.

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

### Default menus

:::note
- Each menu item will be used as **default configuration** - SEF URLs will use the menu item's alias
:::

:::note
- Create these (menu items) inside **Flexicontent hidden menu** - Do not select specific TAG / category / author / etc
:::

#### Category-based views

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Tagged items**<br />`cat_tags_default_menu_itemid` | Category-based views | — | — |
| **Authored items**<br />`cat_author_default_menu_itemid` | Category-based views | — | — |

#### Optional

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Favoured items**<br />`cat_favs_default_menu_itemid` | Category-based views | — | — |
| **My items**<br />`cat_myitems_default_menu_itemid` | Category-based views | — | — |
| **Multi category**<br />`cat_mcats_default_menu_itemid` | Category-based views | — | — |

#### Legacy views

:::note
If using / * needing legacy views. e.g. if search engines / 3rd party web-sites are referencing legacy views, then create 2 legacy menu items and select them as default below
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Tagged Items**<br />`tags_view_default_menu_itemid` | Tags links that do not originate from (a) a Tags Cloud module or (b) a Tag Menu Item, need to get a default configuration. You can create a published Tag Menu Item of public access level (and set it here), and in this menu item configure the tags view default configuration to use for these tags links | — | — |
| **Filter tag views**<br />`filtertag` | Display only content from the active language in the tag view. | — | `1` |
| **Favourited Items**<br />`favs_view_default_menu_itemid` | Favourites links that do not originate from (a) a Favourites Menu Item, need to get a default configuration. You can create a published Favourites Menu Item of public access level (and set it here), and in this menu item configure the favourites view default configuration to use for these favourites links | — | — |

#### Other views

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Search**<br />`search_view_default_menu_itemid` | Search links that do not originate from (a) a Search module or (b) a Search Menu Item, need to get a default configuration. You can create a published Search Menu Item of public access level (and set it here), and in this menu item configure the search view default configuration to use for these search links | — | — |
