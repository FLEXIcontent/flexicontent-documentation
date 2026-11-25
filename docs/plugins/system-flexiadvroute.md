---
sidebar_position: 12
---

# System — Advanced routing

FLEXIcontent provides plugins for search, routing, notifications, editor buttons and sitemap integrations. Enable and configure them from **Extensions → Plugins**. The 35 field-type plugins are documented in the [Fields](../fields/index.md) section.

> System Plugin for FLEXIcontent Advanced Routing

:::info Source
This page is generated from `plugins/system/flexiadvroute/flexiadvroute.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

#### Hide categories

:::note
Hide Categories from Pathway/URLs for Types - These are types that contain content not being a part of structure but rather general information content like site usage instructions or license agreement, etc
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`route_to_type` | — | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Content Types**<br />`type_to_route` | — | `types` | — | — |

:::note
Hide categories in Content / Content Listings by NOT displaying: a. direct category links b. category title as a content/content list markup - These categories are for special purposes, e.g. contain items **displayed** in frontpage or in a module Slideshow.
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Categories**<br />`cats_to_exclude` | Choose the categories to exclude from routing (eg: Homepage) | `flexicategories` | — | — |
