---
sidebar_position: 10
---

# Search — Advanced

FLEXIcontent provides plugins for search, routing, notifications, editor buttons and sitemap integrations. Enable and configure them from **Extensions → Plugins**. The 35 field-type plugins are documented in the [Fields](../fields/index.md) section.

> Search plugin for FLEXIcontent advanced search view. Besides searching item title and description, it can search any flexicontent field that can create searchable data, like tags field, text fields, image fields (e.g. their description), etc. **NOTE:** You should turn off the joomla 'content' search plugin, but not plugins for other type of site content.

:::info Source
This page is generated from `plugins/search/flexiadvsearch/flexiadvsearch.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Search Limit**<br />`search_limit` | Maximum number of search results to return | `text` | — | `50` |
| **Active language only**<br />`filter_lang` | Display search results for active language only (in J1.5 it requires JoomFish) | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Search archived**<br />`search_archived` | Also include archive items into the search | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Browser Navigator**<br />`browsernav` | Browser Navigator | `radio` | `1` = Open New Window<br />`2` = Open Same Window | `2` (Open Same Window) |
