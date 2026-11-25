---
sidebar_position: 13
---

# Files

Upload directories, allowed extensions and image handling.

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

### Files Configuration

#### Files Configuration

## Basic

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Display File Language as**<br />`display_file_lang_as` | Select appearance/behavior of the file language | — | `0` |

#### Folders

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Secure files path**<br />`file_path` | The directory to where the files should be uploaded. Change this default path to be sure to have a minimum security level. | — | `components/com_flexicontent/uploads` |
| **Media files path**<br />`media_path` | The directory where the media files should be uploaded to. This directory path will be visible (in the source code) as it will be use to play the media files. | — | `components/com_flexicontent/medias` |

#### Search Index

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Index PDF files**<br />`index_pdf_files` | Add PDF files contents to the search index (currently only text is added) | — | `0` |
| **Path to PDF parser**<br />`pdfparser_path` | This is the path to the needed library for parsing the PDF files, see https://github.com/smalot/pdfparsers Please download & extract the library from the given URL into the folder and then run composer inside it | — | — |
| **Index CSV files**<br />`index_csv_files` | Add CSV files contents to the search index | — | `0` |

## File editor

:::note
Choose which fields appear when editing a file. Hidden fields keep their saved values. Advanced settings still require the file-properties permission.
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Download filename**<br />`file_editor_show_download_filename` | — | — | `1` |
| **Title**<br />`file_editor_show_title` | — | — | `1` |
| **Description**<br />`file_editor_show_description` | — | — | `1` |
| **Replacement upload**<br />`file_editor_show_replace` | — | — | `1` |
| **Keep old upload date**<br />`file_editor_show_keep_uploaded_date` | — | — | `1` |
| **Keep old uploader**<br />`file_editor_show_keep_uploaded_by` | — | — | `1` |
| **Language**<br />`file_editor_show_language` | — | — | `1` |
| **Access**<br />`file_editor_show_access` | — | — | `1` |
| **Download stamping**<br />`file_editor_show_stamp` | — | — | `1` |
| **Hit count**<br />`file_editor_show_hits` | — | — | `1` |
| **File type**<br />`file_editor_show_type` | — | — | `1` |
| **File size**<br />`file_editor_show_size` | — | — | `1` |
| **Storage filename / URL**<br />`file_editor_show_storage` | — | — | `1` |
| **Server path**<br />`file_editor_show_path` | — | — | `0` |

:::note
These settings apply to the file manager forms (add / edit files outside of a File field). If a property is not enabled here, the settings of the first File field that enables it are used. Each File field has its own settings (Form field tab, Edit properties), which are used when files are edited via that field
:::

#### Custom file property 1 (HTML)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable**<br />`file_custom1_enable` | Enable this property: it is shown below the description in the file add/edit forms and displayed on the site when it is not empty | — | `0` |
| **Label**<br />`file_custom1_label` | Label text. You may enter a language string key (it will be translated if it exists) | — | — |
| **Display label**<br />`file_custom1_label_show` | Show the label in the forms and on the site | — | `1` |
| **Default**<br />`file_custom1_default` | Default value (HTML allowed). Its usage is controlled by the setting below | — | — |
| **Input height (rows)**<br />`file_custom1_rows` | Height of the text area in the forms, in rows (1 - 30) | — | `2` |
| **Usage of default**<br />`file_custom1_default_use` | Select when these default property value will be used | — | `0` |

#### Custom file property 2 (HTML)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable**<br />`file_custom2_enable` | Enable this property: it is shown below the description in the file add/edit forms and displayed on the site when it is not empty | — | `0` |
| **Label**<br />`file_custom2_label` | Label text. You may enter a language string key (it will be translated if it exists) | — | — |
| **Display label**<br />`file_custom2_label_show` | Show the label in the forms and on the site | — | `1` |
| **Default**<br />`file_custom2_default` | Default value (HTML allowed). Its usage is controlled by the setting below | — | — |
| **Input height (rows)**<br />`file_custom2_rows` | Height of the text area in the forms, in rows (1 - 30) | — | `2` |
| **Usage of default**<br />`file_custom2_default_use` | Select when these default property value will be used | — | `0` |

## Limits

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Maximum Size**<br />`upload_maxsize` | The maximum size for an upload (in bytes). Use zero for no limit. Note: your server has a maximum limit. | — | `10000000` |
| **Allowed extensions**<br />`upload_extensions` | Extensions (file types) that are allowed to be uploaded (comma separated) | — | `bmp,wbmp,csv,doc,docx,webp,gif,ico,jpg,jpeg,odg,odp,ods,odt,pdf,png,ppt,pptx,txt,xcf,xls,xlsx,zip,ics` |

#### Remote files (URLs)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Trusted remote file hosts**<br />`remote_trusted_hosts` | External file server hostnames, one per line. A hostname allows all ports; host:port allows only that port. Listed hosts may use private network addresses. File-size checks and downloads otherwise allow public HTTP(S) hosts on standard ports, with an exception for the verified site host. When this list is set, server-proxied downloads are restricted to listed hosts and the verified site host; other downloads redirect the browser. Automatic sizing when adding or saving a URL requires the separate option below and an explicitly listed host. | — | — |
| **Automatically read trusted URL file sizes**<br />`remote_probe_size` | When adding or saving a URL file without a supplied size, try to read its size from a server listed in Trusted remote file hosts. Every redirect must also match the list, including redirects to this site's own host. Disabled by default; an empty list makes no automatic HTTP requests. A supplied size takes precedence. Failed or unsupported lookups leave the size at 0. Checks use HEAD with a small Range GET fallback and share a short HTTP timeout budget during the save. Batch imports and existing records are not automatically recalculated. | — | `0` |

#### Auto-resize uploaded images

:::note
Resizing will be done at the user's browser, thus you get faster upload and less server space consumption
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Resize**<br />`resize_on_upload` | Resize uploaded image to save server space and to speedup uploads, since this will be done at the client size (not all 'source' modes support this) | — | `1` |
| **Image width**<br />`upload_max_w` | — | — | `4000` |
| **Image height**<br />`upload_max_h` | — | — | `3000` |
| **Processing method**<br />`upload_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | — | `0` |

## Download limits

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable download limits**<br />`dl_limit_enable` | Master switch for the whole site. Each File / MediaFile field can use these settings, use its own settings, or have no limits. | — | `0` |

:::note
Limit how many files each user group can download in a period (minutes, hours or days), across all fields that use these limits. Downloads are counted per logged-in user, and per visitor (cookie + IP) for guests. A group inherits the limit of its parent groups; if several groups match, the highest limit wins. Super users are never limited.
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Counting mode**<br />`dl_limit_count_mode` | Any file: every download counts, even of the same file. Unique file: a file counts only once during the period, downloading it again is free. | — | `0` |
| **Period**<br />`dl_limit_window` | Length of the sliding period, together with the unit below. E.g. 24 hours, 30 days, or 5 minutes (with a limit of 1 file: not more than one download every 5 minutes). Download records older than this period are deleted automatically. | — | `24` |
| **Period unit**<br />`dl_limit_window_unit` | Minutes, hours or days. | — | `60` |
| **Limit per user group**<br />`dl_limit_groups` | Number of files per period. Use -1 for unlimited. Groups not listed (and not inheriting a listed parent group) are not limited. | — | — |
| **Guest IP allowance (multiplier)**<br />`dl_limit_guest_ip_factor` | Guests are limited per browser (cookie). To stop quota resets by clearing cookies, they are also limited per IP address, at the group limit multiplied by this number, so several visitors behind one IP address (office, school) do not share a single quota. | — | `5` |
| **Count coupon / download cart downloads**<br />`dl_limit_count_special` | Downloads made through shared-link coupons or the downloads cart bypass access levels. Select Yes to also apply the limits to them. | — | `0` |
| **Limit reached: modal HTML**<br />`dl_limit_modal_html` | HTML shown in a modal window when a user with an exhausted quota clicks a disabled download button, e.g. text and a Register / Subscribe button. Leave empty for the default message. Placeholders: **&#123;reset_in&#125;** time until the next download is possible (the period is sliding, so the oldest download expires first), **&#123;reset_full_in&#125;** time until the counter is back to zero, **&#123;reset_seconds&#125;** same as &#123;reset_in&#125; in seconds, **&#123;limit&#125;** files allowed, **&#123;used&#125;** files used, **&#123;window&#125;** length of the period, e.g. 5 min, 24 h, 7 d. | — | — |

## Verify file contents

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Restrict Uploads**<br />`restrict_uploads` | Verify file types by examining contents and prevent uploads of non allowed types | — | `1` |

#### Extensions

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Legal Image Extensions**<br />`image_extensions` | Image Extensions (file types) that are allowed to be uploaded (comma separated) | — | `bmp,wbmp,gif,jpg,jpeg,png,webp,ico` |
| **No-check extensions**<br />`ignore_extensions` | Ignored file extensions for MIME type checking and restricted uploads. Please avoid this if you have non-trusted authors | — | — |

#### Mime types

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Illegal MIME Types**<br />`upload_mime_illegal` | A comma separated list of illegal MIME types for upload (blacklist) | — | `text/html` |
| **Legal MIME Types**<br />`upload_mime` | A comma separated list of legal MIME types for upload | — | `image/jpeg,image/gif,image/png,image/bmp,application/msword,application/excel,application/pdf,application/powerpoint,text/plain,application/x-zip` |

#### Files Configuration
