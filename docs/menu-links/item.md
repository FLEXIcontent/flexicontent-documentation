---
sidebar_position: 9
---

# Content item



:::info Source
This page is generated from `site/views/item/tmpl/default.xml` and the official FLEXIcontent 5.x language files.
:::

## Required parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Please select a category**<br />`cid` | Select the category you wish to display | `hidden` | — | `0` |
| **Select an Item**<br />`id` | Click on the title in the Popup to select an item | `item` | — | `0` |

## Basic

#### Pathway (Breadcrumbs)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Start to add parents categories at depth**<br />`item_depth` | Start to add parents categories at depth | `list` | `0` = root<br />`1` = level 1<br />`2` = level 2<br />`3` = level 3<br />`4` = level 4<br />`5` = level 5 | `0` (root) |
| **Add item to pathway**<br />`add_item_pathway` | Add the item to the pathway. Set it to no in case of duplicate pathway. | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
