---
sidebar_position: 3
---

# Author's items

Only the options specific to this view are listed below. All other options are described in [Category views — common options](./category-common.md).

:::info Source
This page is generated from `site/views/category/tmpl/author.xml` and the official FLEXIcontent 5.x language files.
:::

## Required parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Layout**<br />`layout` | — | `hidden` | — | `author` |

:::note
To create a menu item for DEFAULT DISPLAY -configuration- (for all authors that do not have a menu item) 1. Select no author here 2. Set a generic title/alias e.g. 'authored' (as alias will be show in the URLs) and configure menu item parameters 3. Go to component parameters, open TAB 'Lists' and select this menu item as default menu item for (category-based view) 'Tagged items'
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Please select an Author**<br />`authorid` | Select the author you wish to display | `fcauthor` | `—` = Click to select | `0` |
| **Limit author items to categories**<br />`cids` | Optionally limit the displayed author items to several categories. Subcategory items are always included | `flexicategories` | — | — |
| **Exclude categories from author items**<br />`excl_cids` | Optionally hide author items assigned to any of these categories. Their subcategories are excluded too | `flexicategories` | — | — |

## Override view parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Max author items in total**<br />`author_limit_total` | Maximum number of items to list for the author, in all categories together. 0 = no limit | `text` | — | `0` |
| **Max author items per category**<br />`author_limit_per_cat` | Maximum number of items to list from each category (the first ones in the list ordering). An item assigned to several categories is counted once. 0 = no limit | `text` | — | `0` |
