---
sidebar_position: 11
---

# Search — Standard

FLEXIcontent provides plugins for search, routing, notifications, editor buttons and sitemap integrations. Enable and configure them from **Extensions → Plugins**. The 35 field-type plugins are documented in the [Fields](../fields/index.md) section.

> Search plugin for Joomla standard search view to search for flexicontent data: title, description, tags and text fields. **NOTE: You must turn off all other Article Content search plugins (content, not plugins for other type of site content)**.

:::info Source
This page is generated from `plugins/search/flexisearch/flexisearch.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Active language only**<br />`filter_lang` | Display search results for active language only | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Search Limit**<br />`search_limit` | Maximum number of search results to return | `text` | — | `50` |
| **Title**<br />`search_title` | Search in item's title | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Intro and main text**<br />`search_desc` | Search in item's Intro and main text | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Text fields**<br />`search_fields` | Search in item's intro and main text fields | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Metadata**<br />`search_meta` | Search in item's meta description and keywords | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Tags**<br />`search_tags` | Search in item's flexicontent tags | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Type selector**<br />`search_select_types` | Let users to select FLEXIcontent type | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Order by date**<br />`search_result_date_control` | Choose your date reference to ordering result | `radio` | `created` = Created date<br />`modified` = Modified date | `created` (Created date) |
| **Id of types, avaliable for search**<br />`search_types` | Enter with comma ID of all avaliable for seach types , or leave it empty for seaching in all published types. | `text` | — | — |
