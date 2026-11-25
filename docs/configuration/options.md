---
sidebar_position: 2
---

# Options (general configuration)

The **Options** screen is the main configuration page of FLEXIcontent. Open it from **Components → FLEXIcontent → Options** in the Joomla! administrator.

It is organised into three sub-tabs:

| Tab | Contents |
| --- | --- |
| Basic | Text search, multi-language, mobile devices |
| CSS styles | Form element heights, page reloading |
| Advanced | Browser frameworks, performance, usage / debug |

:::info Source
This page is generated from `admin/config.xml` (fieldset `component`) and the `en-GB.com_flexicontent.ini` language file of FLEXIcontent 5.x.
:::

## Basic

### Text Search

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Log search queries**<br />`log_search_queries` | Store the search queries entered in the FLEXIcontent search module and search page, with a counter per query. The list is available via the Search Logs button of the FLEXIcontent dashboard. | `0` = No<br />`1` = Yes | `0` (No) |
| **Small / common words searchable**<br />`add_search_prefix` | Enable this to be able to include small or very common words in the text search | `0` = No<br />`1` = Yes | `0` (No) |
| **No space languages**<br />`filter_word_like_any` | This may be needed if your website has content of Asian languages with no spaces between words (Chinese, Japanese, Thai). | `0` = No<br />`1` = Yes | `0` (No) |
| **Most relevant first**<br />`filter_word_relevance_order` | When doing a text search select to show most relevant first, by default this includes title only | `0` = Only use configured order<br />`1` = Relevant Title<br />`2` = Yes | `0` (Only use configured order) |
| **Priority by field**<br />`filter_word_field_priority` | Advanced search index only. Add the kinds of field and drag them to set the priority: items that have the searched words in the first kind of field are listed first, then those matching the second kind, and so on, then the rest. Tag keywords belong to the tags field. Empty = no priority | `title` = Title<br />`categories` = Categories<br />`tags` = Tags | — |
| **Auto-complete: index rows to scan**<br />`search_autocomplete_scan` | Number of search index rows examined to collect word suggestions in the simple auto-complete. Higher values give more (and more varied) suggestions on large sites, but are slower. Default 300 | — | `300` |
| **Auto-complete: max suggestions**<br />`search_autocomplete_limit` | Maximum number of word suggestions shown by the simple auto-complete. Default 10 | — | `10` |
| **Auto-complete: suggestions and order**<br />`search_autocomplete_sources` | Simple auto-complete only (not the Tag-like one). Add the kinds of suggestions and drag them to set their order: words from the search index, item titles, tags and categories (only items the current user can access) | `words` = Words<br />`titles` = Titles<br />`tags` = Tags<br />`categories` = Categories<br />`fields` = Text field values<br />`metakeys` = Item Meta Keywords | — |
| **Auto-complete: max titles / tags / categories**<br />`search_autocomplete_titles_limit` | Maximum number of suggestions of each of these kinds (titles, tags, categories) shown by the simple auto-complete. Default 5 | — | `5` |
| **Auto-complete: max text field values / Meta Keywords**<br />`search_autocomplete_fields_limit` | Maximum number of text field value suggestions (Text fields that are searchable or advanced-searchable) shown by the simple auto-complete (also the limit of item Meta Keywords phrases). Default 3 | — | `3` |

### Multi-language

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Translation method**<br />`flexi_fish` | Native translations translate items fully (ALL fields), by associating multiple content items each of different language, that translate the same content. If you use Falang option (single content item), the custom fields will not be translatable | `0` = Native<br />`1` = Native and Falang | `0` (Native) |
| **Edit inline**<br />`editjf_translations` | You can edit Falang item translations using the --item edit form--. **NOTE:** (a) this will allow to edit fields: title, alias, description, metadesc, metakey (other Falang fields like: attributes and publish_up/publish_down will be forced to common values) (b) A warning will be displayed if you disable this option but Falang Translations are detected. **NOTE:** It is recommended that you use the native translation method for items, and use falang for other parts of the website. | `0` = No<br />`1` = No, disable warning<br />`2` = Yes | `0` (No) |

### Mobile Devices

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use Mobile Layouts**<br />`use_mobile_layouts` | Enable this to use mobile layouts in FLEXIcontent content / content list views **NOTE:** In fields mobile settings are always used | `0` = No, only in fields<br />`1` = Yes | `0` (No, only in fields) |
| **Force desktop layout**<br />`force_desktop_layout` | This is useful to **exclude tablets** from using the mobile layout. -- Usually tablets have **both** a large screen and a decently large resolution (at least 800x480) -- You will need desktop layouts with a responsive design that looks/works well with 800x480 or higher resolution screens | `0` = Never<br />`1` = Tablet detected | `0` (Never) |
| **Debug detection & status**<br />`debug_mobile` | This will print detection or existing status messages in regards to mobile detection and usage | `0` = No<br />`1` = Yes | `0` (No) |

## CSS styles

### CSS

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Form elements**<br />`form-inp-height` | Define height of form elements in record editing forms | — | `36` |
| **Form controls**<br />`ctrls-inp-height` | Define height of form controls like reorder, add, remove buttons in record editing forms | — | `36` |
| **Field filters (Frontend)**<br />`filts-inp-height` | Define height of field filters in front-end views | — | `36` |
| **Managers elements**<br />`fcman-inp-height` | Define height of elements in management views, like: text search bar elements, filters and action buttons (inside record rows) | — | `32` |

### Page reloading

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable page reloading**<br />`page_reloading_enable` | Enable page reloading when filtering is being applied (Frontend / Backend). It maybe used in other cases too. | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Background**<br />`page_reloading_overlay_bg_color` | — | — | `rgba(0, 0, 0, 0.3)` |
| **Text color**<br />`page_reloading_content_color` | — | — | `rgba(0, 0, 0, 1)` |
| **Background**<br />`page_reloading_content_bg_color` | — | — | `rgba(255, 255, 255, 1)` |
| **Image**<br />`page_reloading_logo_imgsrc` | — | — | — |
| **Opacity**<br />`page_reloading_logo_opacity` | — | — | `100` |
| **Enable**<br />`page_reloading_mssg_display` | This can be a language string | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Custom text**<br />`page_reloading_mssg_text` | — | — | — |
| **Enable**<br />`page_reloading_pbar_display` | — | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Color**<br />`page_reloading_pbar_color` | — | — | `rgba(0, 153, 255, 1)` |

## Advanced

### Browser Frameworks / Libraries

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Load FLEXIcontent CSS**<br />`disablecss` | Do not load the FLEXIcontent default CSS file (flexicontent.css). (Not recommended for inexperienced designers). **NOTE:** modules need and load this file(s), along with the module specific CSS, this is done because they may appear in non-FLEXIcontent views. There is a per module parameter to disable loading of CSS files | `0` = Both<br />`1` = Disable in frontend | `0` (Both) |
| **Load tooltips JS**<br />`add_tooltips` | Load the tooltips JS, to display nice tooltips in frontend. **NOTE:** Frontend views that use favorites or voting field (and maybe other fields too) in the frontend, may ignore this setting, and **force** the loading of the tooltips behavior | `1` = Both<br />`0` = Disable in frontend | `1` (Both) |
| **jQuery**<br />`loadfw_jquery` | Some of these libraries can be disabled, some are always needed. Normally you should leave everything here enabled. **NOTE:** If you set some of these to be manually loaded in frontend, then you should make sure that they you loaded via some 3rd party extension, e.g. in your Joomla Template. **NOTE:** If you do not load the needed frameworks then behaviour/appearance of frontend forms (mostly item form) will get broken | `1` = Both<br />`2` = Manually in frontend | `1` (Both) |
| **jQuery UI Theme**<br />`jquery_ui_theme` | — | `ui-lightness` = ui-lightness<br />`smoothness` = smoothness | `ui-lightness` (ui-lightness) |
| **image-picker**<br />`loadfw_image_picker` | Some of these libraries can be disabled, some are always needed. Normally you should leave everything here enabled. **NOTE:** If you set some of these to be manually loaded in frontend, then you should make sure that they you loaded via some 3rd party extension, e.g. in your Joomla Template. **NOTE:** If you do not load the needed frameworks then behaviour/appearance of frontend forms (mostly item form) will get broken | `1` = Both<br />`2` = Manually in frontend | `1` (Both) |
| **masonry**<br />`loadfw_masonry` | Some of these libraries can be disabled, some are always needed. Normally you should leave everything here enabled. **NOTE:** If you set some of these to be manually loaded in frontend, then you should make sure that they you loaded via some 3rd party extension, e.g. in your Joomla Template. **NOTE:** If you do not load the needed frameworks then behaviour/appearance of frontend forms (mostly item form) will get broken | `1` = Both<br />`2` = Manually in frontend | `1` (Both) |
| **inputmask**<br />`loadfw_inputmask` | Some of these libraries can be disabled, some are always needed. Normally you should leave everything here enabled. **NOTE:** If you set some of these to be manually loaded in frontend, then you should make sure that they you loaded via some 3rd party extension, e.g. in your Joomla Template. **NOTE:** If you do not load the needed frameworks then behaviour/appearance of frontend forms (mostly item form) will get broken | `1` = Both<br />`2` = Manually in frontend | `1` (Both) |
| **prettyCheckable**<br />`loadfw_prettycheckable` | Some of these libraries can be disabled, some are always needed. Normally you should leave everything here enabled. **NOTE:** If you set some of these to be manually loaded in frontend, then you should make sure that they you loaded via some 3rd party extension, e.g. in your Joomla Template. **NOTE:** If you do not load the needed frameworks then behaviour/appearance of frontend forms (mostly item form) will get broken | `1` = Both<br />`2` = Manually in frontend<br />`0` = No | `1` (Both) |
| **fancybox**<br />`loadfw_fancybox` | Some of these libraries can be disabled, some are always needed. Normally you should leave everything here enabled. **NOTE:** If you set some of these to be manually loaded in frontend, then you should make sure that they you loaded via some 3rd party extension, e.g. in your Joomla Template. **NOTE:** If you do not load the needed frameworks then behaviour/appearance of frontend forms (mostly item form) will get broken | `1` = Both<br />`2` = Manually in frontend | `1` (Both) |
| **bootstrap.css**<br />`loadfw_bootstrap_css` | Some of these libraries can be disabled, some are always needed. Normally you should leave everything here enabled. **NOTE:** If you set some of these to be manually loaded in frontend, then you should make sure that they you loaded via some 3rd party extension, e.g. in your Joomla Template. **NOTE:** If you do not load the needed frameworks then behaviour/appearance of frontend forms (mostly item form) will get broken | `1` = Frontend<br />`2` = Manually in frontend | `2` (Manually in frontend) |
| **icomoon.css**<br />`loadfw_icomoon_css` | Some of these libraries can be disabled, some are always needed. Normally you should leave everything here enabled. **NOTE:** If you set some of these to be manually loaded in frontend, then you should make sure that they you loaded via some 3rd party extension, e.g. in your Joomla Template. **NOTE:** If you do not load the needed frameworks then behaviour/appearance of frontend forms (mostly item form) will get broken | `1` = Frontend<br />`2` = Manually in frontend | `2` (Manually in frontend) |
| **Load in frontend**<br />`loadfw_select2` | Load Choice controls on the frontend. Choose 'Manually in frontend' if your template loads the library. Native selects remain available without the library. | `1` = Both<br />`2` = Manually in frontend | `1` (Both) |

### Performance

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Always create field HTML**<br />`always_create_fields_display` | It is strongly recommended that you set this to ONLY WHEN NEEDED, so that system will create fields only if they are displayed. If you have compatibility problem, of fields not displaying, try enabling this. | `1` = Always (Not Recommended)<br />`0` = Only When needed (Recommended)<br />`2` = Only in item view<br />`3` = Never unless in a template position | `0` (Only When needed (Recommended)) |
| **Data cache**<br />`advcache` | This option is highly recommended on live sites. It will significantly increase performance of your website. - This is for FLEXIcontent internal data structures, like field filter data and category data | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Cache duration**<br />`advcache_time` | The time before the items are automatically re-cached. Default is one hour (3600 sec). | — | `3600` |
| **Re-compile core LESS**<br />`recompile_core_less` | Only enable this if you are contributing to the project, and you have modified CORE LESS files - this will add a tiny delay to all views, - in production sites it should be OFF as in rare cases re-compiling may fail | `0` = No<br />`1` = Yes | `0` (No) |
| **Compress compiled CSS (LESS)**<br />`compress_core_less` | Compress the CSS output when compiling LESS files. Recommended for production. Disable only for debugging purposes. | `0` = No<br />`1` = Yes | `0` (No) |

### Usage / Debug

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Display performance statistics**<br />`print_logging_info` | Display performance statistics and other execution information | `0` = No<br />`2` = Yes<br />`1` = URL variable: fcdebug=1 | `0` (No) |
| **Show usability notices**<br />`show_usability_messages` | Enable to show important usability messages once per user login session, at the top of the management areas (for items, fields, etc) | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Debug Initial Permissions Creation**<br />`debug_initial_perms` | Enable to see log messages and warnings of the initial permission checking and creation process | `0` = No<br />`1` = Yes | `0` (No) |
