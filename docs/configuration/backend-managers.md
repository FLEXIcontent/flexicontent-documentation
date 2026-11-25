---
sidebar_position: 12
---

# Backend Managers

Layout of the item, field, type, category and file management screens.

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

#### Backend Managers

## Dashboard

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Support URL**<br />`support_url` | Enter the weblink of your support terms and procedure. If you do not want to display the help icon, just leave this field empty ;-) | — | — |
| **Show version checking**<br />`show_updatecheck` | Enables a check for the latest version of FLEXIcontent and displays the update status on the dashboard. If this is disabled, then check can be performed manually by opening the version check slider | — | `1` |
| **Hide buttons**<br />`dashboard_buttons_hide` | Note this will hide the buttons. It will not disable ACCESS to the views that buttons point to, use ACL to disable access to particular views | — | — |
| **Disable sliders**<br />`dashboard_sliders_disable` | Note this will hide the buttons. It will not disable ACCESS to the views that buttons point to, use ACL to disable access to particular views | — | — |
| **Edit items in popup window**<br />`dashboard_modal_item_edit` | Slider item links will open edit form in modal popup window | — | `1` |
| **Disable FLEXIcontent logo**<br />`dashboard_disable_fc_logo` | You can hide the FLEXIcontent image, the license and copyright text will still be visible | — | `0` |
| `dashboard_layout` | — | — | — |
| **Hide license and credits**<br />`dashboard_hide_fc_license_credits` | Hide the license by placing it inside the dashboard sliders | — | `1` |

## Items Manager

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Original content language**<br />`original_content_language` | This is used to highlight content translations in backend managers that are not up-to-date (have a later modification time) compared to an original content | — | `_site_default_` |

### Behavior

#### Items List

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **List only viewable items**<br />`iman_viewable_items` | Only viewable items will be listed to the current user **NOTE:** this setting is ignored for user with the 'Display all (items)' ACL privilege | — | `1` |
| **List items in editable (main) categories**<br />`iman_editable_items` | Only list items that are assigned to editable (main) categories **NOTE:** this setting is ignored for user with the 'Display all (items)' ACL privilege **NOTE:** this does not guaranteed that all listed items will be editable | — | `0` |
| **List only author's language items**<br />`iman_authorlang_items` | Only items in the default language of the author will be listed to the current user **NOTE:** this setting is ignored for user with the 'Associate any item' ACL privilege | — | `0` |

#### Behaviour

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Allow copying of un-editable items**<br />`copytask_allow_uneditable` | This will allow backend users to copy or copy-move (but not move) items that they are not allowed to edit, using the Copy/Move Task **NOTE:**as said above this will not allow moving uneditable items | — | `1` |
| **Items editable till log-off**<br />`items_session_editable` | If an item is assigned to an un-editable category, then the item will remain editable until the user logs off | — | `1` |
| **Enable preview auto-login**<br />`autoflogin` | If yes the username and password will be added to the preview URL to log-in the user automatically. | — | `1` |

### Appearance

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Content type tabs style**<br />`iman_type_tabs_style` | Appearance of the content type tabs above the backend items list (used when the content types are shown as tabs). **Browser tabs**: the active tab is joined with the list below it. **Hanging tabs**: separate rounded tabs hanging from the top bar. **Underline**: plain tabs with a colored line under the active one. **Flat**: square tabs in a solid bar, the active one is filled with the accent color. **Pills**: rounded capsules, the active one is softly tinted. **Bootstrap tabs**: the standard Bootstrap nav tabs. | — | `browser` |
| **Quick Type-Filter links**<br />`iman_quick_itype_links` | This will create quick links in items manager for setting item-type filter to specific type | — | `1` |
| **CSV Export button**<br />`show_csvbutton_be` | Enable CSV Export functionality | — | `0` |
| **Backend list filters**<br />`backend_filters_style` | Appearance of the filters box in the backend items list. **Classic** is the original single-column layout. **Modern** arranges the filters in responsive columns so that they fit on screen. | — | `1` |
| **Apply filters (Modern style)**<br />`backend_filters_apply` | Used only when **Backend list filters** is **Modern**. **With Apply button**: changing a filter does not reload the list, the filters are applied with the **Apply** button, so several values (e.g. tags) can be picked at once. **Instantly**: the list reloads on every change. | — | `1` |
| **Show category path in category lists**<br />`cat_path_show` | Categories can have the same title in different branches. When enabled, backend category selects (filters, import, batch, forms ...) show the path of parent categories of each category, search also matches the words of the path, and the categories manager shows the path when the list is filtered / searched / re-ordered. | — | `1` |
| **Category path format**<br />`cat_path_mode` | **Full path**: all parent categories. **Last items**: only the last parent categories (shortened path is prefixed with ...) | — | `full` |
| **Number of parent categories to show**<br />`cat_path_levels` | Number of the last parent categories to show in the path | — | `3` |
| **Disable columns**<br />`iman_skip_cols` | Permanently hide columns. User will not be able to turn them ON. Note: 'Single type', mean hide column if filtering by single type | — | — |
| **Custom columns**<br />`items_manager_extra_fields` | Optionally include custom fields columns into the items list: select a field to add it, drag to reorder, click the red icon to remove it. **NOTE:** Do not include custom fields that do not fit or will clutter the list. **NOTE:** Some fields will cause problems when displayed in backend. **NOTE:** You can customize this in every content type configuration. Per content type fields will be displayed, when you - filter - the items manager listing via the content type filter. **NOTE:** Entries that were typed manually in older versions with a display variable and title (e.g. fieldname:display:Title) are kept and shown in parentheses. | — | — |
| **Custom columns appearance**<br />`items_manager_cols_appearance` | Default appearance for custom column values in the items list: the raw value, a check mark (the field value is shown in a tooltip when hovering it), or the value cleaned from HTML and trimmed. Can be overridden per-field in the field's Backend View settings. | — | `0` |
| **Trim length (characters)**<br />`items_manager_trim_chars` | Number of characters to keep after stripping HTML tags. | — | `100` |
| **Custom filters**<br />`items_manager_custom_filters` | Select custom fields to be added as items manager filters. NOTE: the drop down selector shows supported field types | — | — |
| **Items Manager Order**<br />`items_manager_order` | Default order of items in the Items Manager | — | `a.id` |
| **Items Manager Order Direction**<br />`items_manager_order_dir` | Default order direction of items in the Items Manager | — | `DESC` |

## Import Manager

### Basic

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Custom ITEM 'id'**<br />`import_id_col` | NOTE: Before final import starts, - [Create] all item ids are checked that they do not exist - [Update] all items are checked that they do exist NOTE: - [Create-Update] Use zero or a non-existing item ID to indicate creating new item - [Create] You can use zero instead of using a specific item ID for the new item | — | `0` |
| **Language**<br />`import_lang` | Enter * OR en-GB or fr-FR or de-DE ... | — | `*` |
| **State**<br />`import_state` | — | — | `1` |
| **Access**<br />`import_access` | — | — | `1` |

### Publishing

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Creator (Author)**<br />`import_created_by_col` | — | — | `0` |
| **Last modifier**<br />`import_modified_by_col` | — | — | `0` |

#### Meta

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use 'metadesc' column (METADATA Description)**<br />`import_metadesc_col` | — | — | `0` |
| **Use 'metakey' column (METADATA Keywords)**<br />`import_metakey_col` | — | — | `0` |
| **Use 'custom_ititle' column**<br />`import_custom_ititle_col` | You can customize the content of the title tag. This is very useful for specific SEO strategies. If left blank, the page title or the item title will be used. | — | `0` |

#### Dates

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Creation date**<br />`import_created_col` | — | — | `0` |
| **Modification date**<br />`import_modified_col` | — | — | `0` |
| **Use 'publish_up' column (Start Publication)**<br />`import_publish_up_col` | — | — | `0` |
| **Use 'publish_down' column (End Publication)**<br />`import_publish_down_col` | — | — | `0` |

### Tags

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Tags**<br />`import_tags_col` | — | — | `0` |

### Media / document Folders

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Media Folder (image/gallery fields)**<br />`import_media_folder` | Please enter a relative path e.g. **tmp/foldername** ... inside your Joomla installation folder **../foldername** ... just above Joomla installation folder | — | `tmp/fcimport_media` |
| **Document Folder (file fields)**<br />`import_docs_folder` | Please enter a relative path e.g. **tmp/foldername** ... inside your Joomla installation folder **../foldername** ... just above Joomla installation folder | — | `tmp/fcimport_docs` |

### CSV file format

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Field Separator**<br />`csv_field_sep` | Multiple characters recommended e.g : ~~ for tab enter: \t | — | `~~` |
| **Field Encloser Character**<br />`csv_field_enclose_char` | Use only if your data have one, e.g for double quote enter: " | — | — |
| **Item Separator**<br />`csv_item_record_sep` | Multiple characters recommended e.g : \n~~ for new line enter: \n | — | `\n~~` |
| **Debug first # items**<br />`csv_debug_records` | This will print the fields of the first # records (items). **NOTE:** this is used **only when testing the file format**. It is recommended to test your CSV file before trying to import. | — | `0` |

#### Multi-value / multi-property fields

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Multi-value separator**<br />`csv_field_mval_sep` | Fields that are multi-valued | — | `%%` |
| **Multi-property separator**<br />`csv_field_mprop_sep` | Fields that have multiple properties per value | — | `!!` |

### Advanced

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Ignore unused columns**<br />`import_ignore_unused_cols` | Enable this if you have redundant columns. | — | `0` |
| **Items per import step**<br />`import_items_per_step` | This is the number of **items to add** per step, -- a large step will give more speed, but you may cause some steps to timeout. -- So, take care to set a small number here if 1. you have items that have large 'original' images (thumbnailing is needed) 2. or if you have 'heavy' content plugins, 3. or if you are using Joomla smart search index on a large site | — | `5` |

#### Backend Managers
