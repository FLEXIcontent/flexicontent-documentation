---
sidebar_position: 14
---

# System — Core tasks

FLEXIcontent provides plugins for search, routing, notifications, editor buttons and sitemap integrations. Enable and configure them from **Extensions → Plugins**. The 35 field-type plugins are documented in the [Fields](../fields/index.md) section.

> FLEXIcontent System Plugin

:::info Source
This page is generated from `plugins/system/flexisystem/flexisystem.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

#### URL redirections

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow Joomla category manager to**<br />`exclude_redirect_cats` | All non-selected usergroups will be redirected to FLEXIcontent category manager | `flexiusergroup` | — | — |
| **Allow Joomla article manager to**<br />`exclude_redirect_articles` | All non-selected usergroups will be redirected to FLEXIcontent item manager | `flexiusergroup` | — | — |
| **Exclude urls from redirection (enter a part) (BACKEND Only)**<br />`excluded_redirect_urls` | if you have trouble with some URLs unwantingly redirecting to FLEXIcontent URLs, you can enter here a sub-string of them, in order to exclude them from redirection. Seperate urls with %% DO NOT add new line characters | `textarea` | — | — |
| **Redirect pdf format**<br />`redirect_pdf_format` | Joomla 2.5 does not support PDF natively, this provides a solution for J1.5 upgraded sites that used it, by redirecting to HTML version | `radio` | `0` = No<br />`1` = Yes<br />`2` = Yes, Display Notice | `1` (Yes) |

#### Auto-Checkins

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Check-in on user logout / session expiration**<br />`checkin_on_session_end` | Check-out records (items,categories,etc) will be checked-in on user logout or session expiration | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Time-Limit check-outs**<br />`limit_checkout_hours` | Impose a maximum time for checked-out records. Records exceeding this limit whill be automatically checked-in | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Max checked out hours**<br />`max_checkout_hours` | Maximum allowed time an record (item,category,etc) should be checked out before automatically checking it in | `text` | — | `24` |

#### Auto-Archive, Auto-Unpublish

:::note
NOTE: if you are sending expiration emails, after items have expired, do not change item state, and do not clear publish down date
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Items with expired dates**<br />`archive_on_publish_down` | Enable this to automatically archive or unpublish items that their publish_down date is reached | `radio` | `0` = No action<br />`1` = Archive<br />`2` = Unpublish | `0` (No action) |
| **Clear publish down date**<br />`clear_publish_down_date` | When auto-archiving expired items, also clear the publish-down date, this will make the auto-archived items visible in the archived view. | `radio` | `0` = No<br />`1` = Yes, Recommeneded | `1` (Yes, Recommeneded) |
