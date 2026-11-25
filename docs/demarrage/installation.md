---
sidebar_position: 1
---

# Installation

This page explains how to install FLEXIcontent on a Joomla! 4, 5 or 6 site.

## Requirements

- A working Joomla! site on a version supported by the 5.x branch.
- A PHP configuration compatible with your Joomla! version.
- `max_input_vars` set to **4000 or higher**. You can check it in the Joomla! administrator under **System → Site Information → PHP Information**. FLEXIcontent forms can contain many fields, so a value that is too low may prevent saving.

:::tip
If you need to change `max_input_vars`, do it in the hosting `php.ini`. Changing it through `.htaccess` only works on some servers.
:::

## Install the component

1. Download the package from the official [Latest version](https://www.flexicontent.org/downloads/latest-version.html) page.
2. In the Joomla! administrator, go to **System → Install → Extensions**.
3. Upload the downloaded ZIP file.
4. Wait for the confirmation, then check that the **FLEXIcontent** component appears in the components menu.
5. Open the component options and save them once to initialise the settings.

## After installation

To get a visible site quickly:

1. Create a **content type** or use the default `Article` type.
2. Add some **fields** to it (text, date, image, select list…).
3. Create a **category** and assign it to the type.
4. Create your first **item** and fill in its fields.
5. Create a **menu item** pointing to a FLEXIcontent category view.

These steps are described in [Getting started](./premiers-pas.md).

## Upgrading

:::warning
Always back up your files and database before upgrading.
:::

1. Download the new package.
2. Install it over the existing installation via **System → Install → Extensions**.
3. Clear the Joomla! cache and the FLEXIcontent cache.
4. Open the options of templates, modules and content types, and save them again if the interface asks you to.

:::caution
After a major version upgrade, some template or style settings may change. Check your views and re-save the affected options.
:::

## Troubleshooting

- **Error during installation**: check available PHP memory and the maximum upload size.
- **Options are not saved**: check write permissions and the `max_input_vars` setting.
- **No field appears**: make sure the fields are assigned to the content type being used.
