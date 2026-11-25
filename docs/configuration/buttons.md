---
sidebar_position: 4
---

# Buttons

Toolbar buttons displayed in the backend managers.

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

### Buttons

#### Page buttons

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Print Method**<br />`print_behaviour` | Select to automatically open browser print dialog, or display a print button inside the page | — | `auto` |
| **Print Icon**<br />`show_print_icon` | Enable Print screen | — | `1` |
| **Email Icon**<br />`show_email_icon` | Enable emailing current page URL to a friend | — | `1` |

:::note
Items list buttons
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Feed Icon**<br />`show_feed_icon` | Enable previewing of current page feeds in a popup window. This will also make subscribing easier for your visitors | — | `0` |
| **Feed head link**<br />`show_feed_link` | Enable this to insert an RSS feed link inside the HTML Head. This make possible for browsers and RSS readers to discover your RSS feeds and subscribe to them | — | `1` |

#### Item buttons

:::note
Please configure similar settings for item lists inside TAB '%s'
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Edit button**<br />`show_editbutton` | Enables display of Item Edit button for all items that the currently logged user can edit | — | `1` |
| **(Permanent) Delete button**<br />`show_deletebutton` | Enables display of Item Delete button for all items that the currently logged user can delete. NOTE this is not a trash button, instead it permanently removes the item | — | `0` |
| **State button**<br />`show_state_icon` | Enable quick change of publication state via an AJAX state selector button | — | `1` |

### Customize

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Icons**<br />`show_icons` | Print, Email, PDF, etc. will utilize Icons or Text | — | `2` |
| **Icon type**<br />`use_font_icons` | You may display icons as images or as using an installed font-based icon set | — | `1` |
| **Preset configurations**<br />`font_icon_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | — | — |
| **Font icons**<br />`font_icon_classes` | Use comma separated list, to load defaults and see the format, leave parameter empty and save | — | `pdf:icon-book, print:icon-print, mail:icon-envelope, feed:icon-feed, edit:icon-pencil, new:icon-new, approval:icon-key, delete:icon-delete, csv:icon-download` |

#### Placement of buttons

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Place inside dropdown**<br />`btn_grp_dropdown` | Display buttons as drop down, typically this will use bootstrap or similar, and it may not be ignored by custom templates | — | `0` |
| **Dropdown button icon**<br />`btn_grp_dropdown_class` | Icon of the dropdown button | — | `icon-options` |
