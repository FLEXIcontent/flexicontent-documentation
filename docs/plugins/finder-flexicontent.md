---
sidebar_position: 6
---

# Smart Search

FLEXIcontent provides plugins for search, routing, notifications, editor buttons and sitemap integrations. Enable and configure them from **Extensions → Plugins**. The 35 field-type plugins are documented in the [Fields](../fields/index.md) section.

> This plugin indexes FLEXIcontent Items.

:::info Source
This page is generated from `plugins/finder/flexicontent/flexicontent.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Index archived items**<br />`search_archived` | Finder content field search archived desc | `radio` | `0` = Jno<br />`1` = Jyes | `1` (Jyes) |
| **Select which taxonomies (filters) to create**<br />`taxonomies` | — | `taxonomytypes` | `author` = Author<br />`category` = Category<br />`language` = Language<br />`type` = Type | `type,category,language,author` |
| **Types to Index (aka searchable)**<br />`types_to_index` | Select FLEXIcontent types to be indexed by Finder. (Leave empty to index all types). _Leave empty to index all types_ | `sql` | — | — |
