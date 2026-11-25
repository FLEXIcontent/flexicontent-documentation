---
sidebar_position: 7
---

# Favourites notifications

FLEXIcontent provides plugins for search, routing, notifications, editor buttons and sitemap integrations. Enable and configure them from **Extensions → Plugins**. The 35 field-type plugins are documented in the [Fields](../fields/index.md) section.

> Sends notifications to users favouring a content that has been updated. The author can select to notify users favouring the content. This is done after the author clicks save, and at most once per author session.

:::info Source
This page is generated from `plugins/flexicontent/flexinotify/flexinotify.xml` and the official FLEXIcontent 5.x language files.
:::

## Basic

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Debug Notifications**<br />`debug_notifications` | Select to display debug messages, to temporarily check proper functionality of notifications | `list` | `0` = No<br />`1` = Show to all editors<br />`2` = Show to super admins | `0` (No) |

#### Basic Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Sender name**<br />`sendername` | Sender name. If empty the site name will be used instead. | `text` | — | — |
| **Sender email**<br />`senderemail` | Sender email address. If empty the site configuration email will be used instead. | `text` | — | — |

### Owners notifications

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Email subject**<br />`mailsubject_owner` | The title of the email _Update notification_ | `text` | — | — |
| **Email Body**<br />`mailbody_owner` | The text of the email _Hello %s,\n\nOne of your items has been recentely updated :\n\nId : %s\nTitle : %s\nCategory : %s\State : %s\nLink : %s\n\nCheers,\n%s._ | `textarea` | — | — |

### Subscribers notifications

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Email subject**<br />`mailsubject` | The title of the email _Update notification_ | `text` | — | — |
| **Email Body**<br />`mailbody` | The text of the email _Hello %s,\n\nAn item you added in your favourite list has been recentely updated :\n\nId : %s\nTitle : %s\nCategory : %s\nLink : %s\n\nCheers,\n%s._ | `textarea` | — | — |

#### Personalized notifications Sends separate email per subscriber

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`send_personalized` | Enable this to send different notification email per user, with user specific customizations like including the user's name inside message. The trade-off is that this will be slower, you may wish to avoid if you content items are updated very often and/or you have more than 100 subscribers per content item!! | `list` | `0` = No, send same email (faster)<br />`1` = Yes, send separate emails | `1` (Yes, send separate emails) |
| **Subscriber limit**<br />`personalized_limit` | If a content item has more subscribers than this limit, then a single message will be sent. **NOTE:** values higher than 100 will be ignored | `text` | — | `50` |

:::note
Customizations per email
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Include fullname**<br />`include_fullname` | User's full name will be included in the email, to make email be more user friendly | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
