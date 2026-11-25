---
sidebar_position: 2
---

# Content — Flexibreak

FLEXIcontent provides plugins for search, routing, notifications, editor buttons and sitemap integrations. Enable and configure them from **Extensions → Plugins**. The 35 field-type plugins are documented in the [Fields](../fields/index.md) section.

> FLEXIcontent alternative to standard pagebreak plugin (offers instant javascript pagination and other alternatives). Allow the creation of a paginated article with optional table of contents. Insert page breaks through the use of the page break button normaly found in beneath the text panel in an Article. The page break will be displayed in the text window as a simple horizontal line. The text…

:::info Source
This page is generated from `plugins/content/flexibreak/flexibreak.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

### Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display method**<br />`display_method` | Select display method, (a) Show all pages and scroll to the desired one, (b and c) Show active page only via Javascript or via page reload | `multilist` | `0` = Scroll anchors<br />`1` = Inline switch<br />`2` = Reload page<br />`3` = Tabs<br />`4` = Sliders | `1` (Inline switch) |

#### Pagination

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Next / Previous Links**<br />`pagination` | Defines where navigation controls are displayed | `radio` | `0` = Hide<br />`1` = Below table of contents<br />`2` = Before description<br />`3` = After description | `3` (After description) |
| **Page counter**<br />`show_prevnext_count` | Show current page number out of total page number | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |

#### Table of contents

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Table of Contents**<br />`multipage_toc` | You may select to hide the Table of Contents, (you can still show the Page Navigation) | `multilist` | `0` = Hide<br />`1` = Show | `1` (Show) |
| **Return TOC links**<br />`return_anchors` | You may select to display return to table of content anchor links at the end of every page | `radio` | `0` = Hide<br />`1` = Show<br />`2` = Auto | `1` (Show) |
| **Table title**<br />`toc_title` | You may select to hide the title 'Table of contents' | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |
| **Table of Contents placement**<br />`toc_placement` | You may select to prepend Table of Contents to item's description or placing via item-&gt;toc variable in the latter case, please customize item.php/item_html5.php of your template | `radio` | `0` = $item-&gt;toc variable<br />`1` = Before description | `1` (Before description) |

#### All pages link

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show link**<br />`allpages_link` | Display a link to allow user to display all content pages at once | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Custom text**<br />`custom_allpages` | A custom language string as title of 'All Pages' link | `text` | — | `FLEXIBREAK_ALL_PAGES` (All pages) |

#### Introduction link

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Link text**<br />`introtext_title` | Display a link to allow user to display the intro text | `multilist` | `0` = Item title<br />`1` = Custom text | `1` (Custom text) |
| **Custom text**<br />`custom_introtext` | A custom language string as title of 'Intro Text' link | `text` | — | `FLEXIBREAK_INTRODUCTION` (Introduction) |
