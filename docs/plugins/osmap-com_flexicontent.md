---
sidebar_position: 9
---

# OSMap integration

FLEXIcontent provides plugins for search, routing, notifications, editor buttons and sitemap integrations. Enable and configure them from **Extensions → Plugins**. The 35 field-type plugins are documented in the [Fields](../fields/index.md) section.

> OSMap Plugin for FLEXIcontent Component

:::info Source
This page is generated from `plugins/osmap/com_flexicontent/com_flexicontent.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| ****Content Items in Sitemap ****<br />`myspacer1` | — | `spacer` | — | — |
| **Show (expand views)**<br />`include_items` | Should we include content items in the sitemap? **NOTE**: this effects all FLEXIcontent 'expandable' views | `list` | `0` = Never<br />`1` = Always<br />`2` = In XML Sitemap Only<br />`3` = In HTML Sitemap Only | `1` (Always) |
| **In main category only**<br />`include_items_maincatonly` | FLEXIcontent allows multiple categories per content Item, this may lead to your items being listed multiple times in the Sitemap. You can avoid this by showing each item only inside its main category. | `list` | `0` = Never<br />`1` = Always<br />`2` = In XML Sitemap Only<br />`3` = In HTML Sitemap Only | `0` (Never) |
| ****Expand links (include contained content items)****<br />`myspacer2` | — | `spacer` | — | — |
| **Expand Category Links**<br />`expand_cats` | Category (single/multiple) menu items will be expanded to include all Content Items. Normally you would want this to be turned on, unless you have too many items or you prefer to use a different way for adding your items to the sitemap. E.g. via tagged views or via author views | `list` | `0` = Never<br />`1` = Always<br />`2` = In XML Sitemap Only<br />`3` = In HTML Sitemap Only | `0` (Never) |
| **Expand Author Links**<br />`expand_authors` | Author menu items will be expanded to include all Content Items owned by the author. If you enable this, then note that the content items may also be listed in inside categories, thus listed multiple times | `list` | `0` = Never<br />`1` = Always<br />`2` = In XML Sitemap Only<br />`3` = In HTML Sitemap Only | `0` (Never) |
| **Expand Tag Links**<br />`expand_tags` | Tag menu items will be expanded to include all tagged Content Items. If you enable this, then note that the content items may also be listed in inside categories, thus listed multiple times | `list` | `0` = Never<br />`1` = Always<br />`2` = In XML Sitemap Only<br />`3` = In HTML Sitemap Only | `0` (Never) |
| **Listing Limits and Unauthorized Content**<br />`myspacer3` | — | `spacer` | — | — |
| **Max. Items per Category**<br />`max_items` | Max number of Items per category to include on sitemap (leave empty for no limit). A sanity limitation for categories with many items. | `text` | — | — |
| **Max. Age in Days**<br />`max_age` | Maximum age of Items to include in sitemap (leave empty for no limit). Set this limit if aging makes your content less important, e.g. news sites. | `text` | — | — |
| **Show Unauthorized Links**<br />`show_noauth` | OSMAP_FLEXICONTENT_SHOW_UNAUTHORIZED_LINKS_DESC. | `list` | `—` = FC Component Setting<br />`0` = Never<br />`1` = Always<br />`2` = In XML Sitemap Only<br />`3` = In HTML Sitemap Only | — |
| ****Content Item Enhancements (slower)****<br />`myspacer3` | — | `spacer` | — | — |
| **Add sub-page links**<br />`add_pagebreaks` | (slower) Content items that are multi-paged will be have all of their page links added to the sitemmap. | `list` | `0` = Never<br />`1` = Always<br />`2` = In XML Sitemap Only<br />`3` = In HTML Sitemap Only | `0` (Never) |

## Xml

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Category Priority**<br />`cat_priority` | Set the priority for the categories | `list` | `-1` = Use Parent Menu Settings<br />`0.0` = 0.0<br />`0.1` = 0.1<br />`0.2` = 0.2<br />`0.3` = 0.3<br />`0.4` = 0.4<br />`0.5` = 0.5<br />`0.6` = 0.6<br />`0.7` = 0.7<br />`0.8` = 0.8<br />`0.9` = 0.9<br />`1.0` = 1.0 | `-1` (Use Parent Menu Settings) |
| **Category Change Frequency**<br />`cat_changefreq` | Set the change frequency for the categories | `list` | `-1` = Use Parent Menu Settings<br />`always` = Always<br />`hourly` = Hourly<br />`daily` = Daily<br />`weekly` = Weekly<br />`monthly` = Monthly<br />`yearly` = Yearly<br />`never` = Never | `-1` (Use Parent Menu Settings) |
| **Item Priority**<br />`item_priority` | Set the priority for the Items | `list` | `-1` = Use Parent Menu Settings<br />`0.0` = 0.0<br />`0.1` = 0.1<br />`0.2` = 0.2<br />`0.3` = 0.3<br />`0.4` = 0.4<br />`0.5` = 0.5<br />`0.6` = 0.6<br />`0.7` = 0.7<br />`0.8` = 0.8<br />`0.9` = 0.9<br />`1.0` = 1.0 | `-1` (Use Parent Menu Settings) |
| **Item Change Frequency**<br />`item_changefreq` | Set the change frequency for the Items | `list` | `-1` = Use Parent Menu Settings<br />`always` = Always<br />`hourly` = Hourly<br />`daily` = Daily<br />`weekly` = Weekly<br />`monthly` = Monthly<br />`yearly` = Yearly<br />`never` = Never | `-1` (Use Parent Menu Settings) |
