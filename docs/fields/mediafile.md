---
sidebar_position: 24
---

# Media file

FLEXI_FIELD_MEDIAFILE

*Plugin : `mediafile` — MediaFile*

:::info Source
This page is generated from `plugins/flexicontent_fields/mediafile/mediafile.xml` and the official FLEXIcontent 5.x language files.
:::

## Editing

#### Editing

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use field in a group**<br />`use_ingroup` | Enable to allow field to be part of field group, that is created via 'Field Group' field. NOTE: You should then select this field in ONLY ONE field group | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |

#### Number of values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Allow multiple values**<br />`allow_multiple` | Allow more than 1 value for this field | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **max # values**<br />`max_values` | The max number of values you wish to record | `text` | — | `0` |
| **Values per row**<br />`fields_box_placing` | Save space by allowing multiple values to show per row | `radio` | `0` = 1<br />`1` = Multiple | `1` (Multiple) |

#### Buttons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Add position**<br />`add_position` | Select to add value inline (show add button at every value) or append them to the bottom of the value list | `multilist` | `0` = Append to bottom<br />`1` = Inline append<br />`2` = Inline prepend<br />`3` = Inline both | `3` (Inline both) |
| **File Upload / Select**<br />`file_btns_position` | Choose how and where to display the file Select / Upload buttons | `hidden` | — | `0` |

### Remote Storage

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Type of storage**<br />`estorage_mode` | Select the type of remote storage | `multilist` | `0` = No<br />`FTP` = FTP<br />`OTHER` = Other | `0` (No) |

#### Other

:::note
Currently only FTP is supported, TO-DO more external storage options ...
:::

#### Remote Storage (FTP)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Hostname**<br />`efs_ftp_host` | — | `text` | — | — |
| **Port**<br />`efs_ftp_port` | — | `text` | — | — |
| **User**<br />`efs_ftp_user` | — | `text` | — | — |
| **Password**<br />`efs_ftp_pass` | — | `text` | — | — |
| **Folder**<br />`efs_ftp_path` | — | `text` | — | — |
| **URL**<br />`efs_www_url` | — | `text` | — | `https://some_external_servername.com/somefolder/` |

### FLEXI_FIELD_MEDIADATA_CREATE_PREVIEW_FILES

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **FFmpeg binary**<br />`mm_ffprobe_path` | Enter absolute path to ffmpeg executable. This is used to get a smaller size preview file | `text` | — | `/usr/bin/ffprobe` |
| **Create a preview file**<br />`mm_create_preview` | — | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Bit rate (kbps)**<br />`mm_preview_bitrate` | Bitrate will effect the quality of the audio preview | `text` | — | `96` |
| **FFmpeg binary**<br />`mm_ffmpeg_path` | Enter absolute path to ffmpeg executable. This is used to get a smaller size preview file | `text` | — | `/usr/bin/ffmpeg` |
| **Audiowaveform Binary**<br />`mm_audiowaveform_path` | Enter absolute path to audiowaveform executable. This is used to create an audio waveform file consisting of peaks | `text` | — | `/usr/bin/audiowaveform` |

:::note
Samples per peak. E.g. Enter 256, to use 256 input samples to create 1 waveform peak. Note: this is for sounds up to 30 seconds. For longer files we will increase this proportionally. E.g. for 60 seconds we will use 512 samples to create 1 waveform peak.
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Samples per peak**<br />`mm_wf_zoom` | — | `text` | — | — |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Card width (px)**<br />`form_card_width` | Width of the media file card in the item edit form, in pixels | `text` | — | `420` |

#### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Fields layout**<br />`formlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/field_*.php as field_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Header info**<br />`form_info_header` | — | `radio` | `1` = Server storage sub-path<br />`2` = Original filename<br />`3` = Both | `3` (Both) |
| **File preview**<br />`form_file_preview` | You can enable file preview box, e.g. it will show image thumbnail if selected file is an image | `multilist` | `0` = Disable<br />`1` = Enable | `0` (Disable) |

#### Edit properties

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`inputmode` | Select to allow editing file properties elements | `multilist` | `1` = No<br />`0` = Yes | `1` (No) |
| **Title**<br />`iform_title` | Can be displayed instead of filename | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Description**<br />`iform_desc` | This can be used by some fields, e.g. it can be optionally displayed (inline, tooltip, etc) by the file field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Language**<br />`iform_lang` | You may want to set file language, e.g. if file is a document in specific language, or media that contains audio or text in specific language | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Access**<br />`iform_access` | You may want to set the access level that users will need to have, in order to download or view the file | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Download stamping**<br />`iform_stamp` | Enable / disable stamping during file download (e.g. for PDFs) | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Defaults

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Title**<br />`iform_title_default` | Default value | `text` | — | — |
| **Description**<br />`iform_desc_default` | Default value | `text` | — | — |
| **Language**<br />`iform_lang_default` | Default value | `fclanguage` | — | `*` |
| **Access**<br />`iform_access_default` | Default value | `accesslevel` | — | `1` |
| **Download stamping**<br />`iform_stamp_default` | Default value | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

### My Files

:::note
Display a multi-upload manager, along with file-selection of files uploaded by current user, (privileged users may see all files)
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allowed extensions**<br />`upload_extensions` | Extensions (file types) that are allowed to be uploaded (comma separated) _mp3,m4a,wav,ogg,oga,webm,mp4,m4v,mov_ | `text` | — | — |
| **Maximum Size**<br />`upload_maxsize` | The maximum size for an upload (in bytes). Use zero for no limit. Note: your server has a maximum limit. | `number` | — | — |
| **Enable**<br />`use_myfiles` | Enable to allow selecting an existing file that was previously uploaded | `multilist` | `0` = Inline uploads, No My files reuse modal<br />`1` = Inline uploads + My Files reuse modal (with: Secure Uploads + URL links)<br />`2` = Inline uploads + My Files reuse modal (with: Secure Uploads + URL links + Joomla Media manager)<br />`3` = Inline uploads + My Files reuse modal (with: URL links + Joomla Media manager)<br />`4` = Joomla Media manager<br />`5` = Inline uploads + My Files reuse modal (with: Secure Uploads) | `1` (Inline uploads + My Files reuse modal (with: Secure Uploads + URL links)) |
| **Joomla media**<br />`jmedia_filetypes` | Select file types what will be allowed and selectable by the editors | `fccheckbox` | — | — |

:::note
About top folder (J4+ only) - You must add this folder in PLUGIN: 'FileSystem - Local', e.g. add folder downloads. - For quantum file manager. This is the scope name NOTE: please add an extra custom-named scope for the folder images !! e.g. 'imgs' DO NOT change folder name 'images', 'imgs' will be the name of the custom scope
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Top folder**<br />`jmedia_topdir` | For native media file manager, this is the folder inside Joomla ROOT (that you added in Filestorage plugin, or for Quantum file manager this will be the custom scope name _images_ | `text` | — | — |
| **Sub folder path**<br />`jmedia_subpath` | Select sub-folder to be opened _e.g. content/news -&gt; JPATH_ROOT/images/content/news_ | `text` | — | — |

#### Uploader

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Auto assign**<br />`autoassign` | When new files are uploaded they will be assigned to the current field automatically. This way user will not have to search and click the new file(s) | `radio` | `0` = No<br />`1` = Select and assign<br />`2` = Select only | `1` (Select and assign) |
| **Target directory**<br />`target_dir` | If you select secure, the users will never see the real path of the file and will only be allowed **indirect access** to the file. This option is suitable for e.g. - document files * - high resolution copyrighted images * * attach to content via **FILE** field ** attach to content via **FILE** field or **image/gallery** field NOTE: 1. If you select media folder, then direct access will be allowed thus you will be able to play media files via media players embedded in visitor's browser. 2. Image files in the secure folder can be either privileged accessed via file field or viewable by (optionally watermarked) thumbnails created by the image/gallery field and you will still keep the secure download feature. | `hidden` | — | `0` |

#### File list columns

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Columns**<br />`filelist_cols` | Optional columns for the file list. Some columns like filename cannot be disabled | `fccheckbox` | — | — |

#### Auto-resize uploaded images

:::note
Resizing will be done at the user's browser, thus you get faster upload and less server space consumption
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Resize**<br />`resize_on_upload` | Resize uploaded image to save server space and to speedup uploads, since this will be done at the client size (not all 'source' modes support this) | `multilist` | `—` = Use component setting<br />`0` = No<br />`1` = Yes | — |
| **Image width**<br />`upload_max_w` | — | `text` | — | — |
| **Image height**<br />`upload_max_h` | — | `text` | — | — |
| **Processing method**<br />`upload_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `—` = Use component setting<br />`0` = Scale<br />`1` = Crop | — |

#### Editing

## Viewing

#### Viewing

### Basic

#### Display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

#### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes<br />`2` = Yes, append login link | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Export

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Inaccessible files

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show**<br />`noaccess_display` | Select to display file information or skip the file altogether | `radio` | `0` = No<br />`1` = Yes<br />`2` = Yes, no description | `1` (Yes) |
| **Append file variables**<br />`noaccess_addvars` | This is meant for developers, and will enable adding variables file_id, field_id, item_id to the no access URL, allowing for custom handling e.g. purchase item | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Unlogged users

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Redirect URL**<br />`noaccess_url_unlogged` | Optional redirection URL for unlogged users, e.g. login or subscribe page | `text` | — | — |
| **Message**<br />`noaccess_msg_unlogged` | Display a custom message e.g. a message 'no access' or 'please login' or 'not purchased' | `text` | — | — |

#### Logged users

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Redirect URL**<br />`noaccess_url_logged` | Optional redirection URL for logged users, e.g. purchase page etc | `text` | — | — |
| **Message**<br />`noaccess_msg_logged` | Display a custom message to logged user e.g. a message 'no access' or 'not purchased' | `text` | — | — |

#### Backend View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Backend view appearance**<br />`backend_view_appearance` | How this field's value is displayed in the admin items list. Overrides the global 'Custom columns appearance' setting when not set to Default. | `multilist` | `0` = Default<br />`1` = Check mark<br />`2` = Clean up HTML and trim | `0` (Default) |
| **Trim length (characters)**<br />`backend_view_trim_chars` | Number of characters to keep after stripping HTML tags. | `text` | — | `100` |

### Playback

#### Waveform options

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Waveform zoom slider**<br />`wf_zoom_slider` | A slider to zoom in / out of waveform | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |
| **Waveform loading progress**<br />`wf_load_progress` | Display a loading messages (percent) while waveform is being downloaded | `radio` | `0` = Hide<br />`1` = Show | `1` (Show) |

#### Wavesurfer JS options

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **waveColor**<br />`ws_wavecolor` | — | `text` | — | `#619fc7` |
| **progressColor**<br />`ws_progress_color` | — | `text` | — | `#d0d0d0` |
| **cursorColor**<br />`ws_cursor_color` | — | `text` | — | `#619fc7` |
| **cursorWidth**<br />`ws_cursor_width` | — | `text` | — | `2` |

### File actions

:::note
Button configuration for actions such as: download, view, share, add-to-cart
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use buttons**<br />`usebutton` | Select to display links or button or other | `multilist` | `0` = Links<br />`1` = Buttons | `1` (Buttons) |
| **Buttons position**<br />`buttonsposition` | Position of the buttons (download, share, add to cart) relative to the filename | `radio` | `0` = Before<br />`1` = After | `1` (After) |

#### Action separation character(s)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use separation character(s)**<br />`use_action_separator` | You may want not to use separation characters and rely only on CSS for styling the display | `multilist` | `0` = Line break<br />`1` = Custom | `0` (Line break) |
| **Custom**<br />`action_separator` | Separation character(s) will be placed between displayed action link or action buttons | `text` | — | — |

#### File actions

### Downloads

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow downloads**<br />`allowdownloads` | Normally you would want to allow this, you can disable though if you are using downloads manager module (downloads cart module). **NOTE:** when downloads are enabled, then ACL/Access levels are always used to determine if frontend user can download the file | `multilist` | `0` = No<br />`1` = Yes<br />`2` = Yes, custom text | `1` (Yes) |
| **Custom download text**<br />`downloadstext` | Normally the button will display 'Download', you can set a custom text here, e.g. 'Get It!' , etc | `text` | — | `FLEXI_DOWNLOAD` (Download) |

#### Force file URLs to download

:::note
You can not force an external media URL to be downloaded by the browser. Enabling this will pipe the external file url though the web-server to force it to download. Disable this if you have problems downloading file URLs !!! Also external server must be able to report file sizes properly ...
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`force_url_download` | File URLs will be piped through the web-server to be able to force a download. Disable if you run into problems !!! | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Extensions to force**<br />`force_url_download_exts` | Normally the button will display 'Download', you can set a custom text here, e.g. 'Get It!' , etc | `text` | — | `bmp,wbmp,gif,jpg,jpeg,png,webp,ico,wav,mp3,aiff` |
| **Max file size (KBs)**<br />`force_url_download_max_kbs` | Download of larger files will not be piped through web-server. Instead file url will be opened via a redirection to it | `text` | — | `100000` |

### In-browser viewing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show view button**<br />`allowview` | Allows viewing the file inside the browser | `multilist` | `0` = No<br />`1` = Yes<br />`2` = Yes, custom text | `0` (No) |
| **Custom view text**<br />`viewtext` | Normally the button will display 'View', you can set a custom text here, e.g. 'Click to view' , etc | `text` | — | — |
| **View inside**<br />`viewinside` | Select to view file in same / new window | `radio` | `0` = Fancybox modal<br />`1` = GLightbox modal (responsive + fullscreen)<br />`2` = New window<br />`3` = Same window | `1` (GLightbox modal (responsive + fullscreen)) |

### Cart

#### Download cart

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show add to cart**<br />`use_downloads_manager` | Requires download manager module. This feature allows adding files to a downloads cart, then user can arrange his/her downloads into folders and download them via a single compressed archive. Also allows storing/deleting/renaming the file carts, etc ... | `multilist` | `0` = No<br />`1` = Yes<br />`2` = Yes, custom text | `0` (No) |
| **Custom add to cart**<br />`addtocarttext` | Normally the button will display 'Add to cart', you can set a custom text here, e.g. 'Add to my downloads' , etc | `text` | — | — |

### Sharing

#### Sharing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show share button**<br />`allowshare` | Allows sharing the download link via sending an email | `multilist` | `0` = No<br />`1` = Yes<br />`2` = Yes, custom text | `0` (No) |
| **Custom share text**<br />`sharetext` | Normally the button will display 'Share', you can set a custom text here, e.g. 'Share with friend' , etc | `text` | — | — |

:::note
Download coupons e.g. when a user shares (via email / etc) a file download link to a user that does not have download access
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable download coupons**<br />`enable_coupons` | When sharing file (download) links, the users receiving the link (e.g. via email/etc), may not have the required access level for downloading the file. Enable this to allow these users to download the file, by creating download coupons | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Coupon hits limit**<br />`coupon_hits_limit` | This limit the number of downloads (hits) that can be made using each coupon. Set this to -1 for no limit, thus coupons will expire only when expiration date is reached | `text` | — | `3` |
| **Coupon expiration days**<br />`coupon_expiration_days` | How long the coupon will be usable after it is created | `text` | — | `15` |

### Download limits

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Download limits for this field**<br />`dl_limit_override` | Use the component settings, use the settings below for this field, or exempt this field from download limits. | `multilist` | `0` = Component settings<br />`1` = This field's own settings<br />`2` = No limits | `0` (Component settings) |

:::note
Limit how many files each user group can download in a period (minutes, hours or days), across all fields that use these limits. Downloads are counted per logged-in user, and per visitor (cookie + IP) for guests. A group inherits the limit of its parent groups; if several groups match, the highest limit wins. Super users are never limited.
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Counting mode**<br />`dl_limit_count_mode` | Any file: every download counts, even of the same file. Unique file: a file counts only once during the period, downloading it again is free. | `radio` | `0` = Any file<br />`1` = Unique file | `0` (Any file) |
| **Period**<br />`dl_limit_window` | Length of the sliding period, together with the unit below. E.g. 24 hours, 30 days, or 5 minutes (with a limit of 1 file: not more than one download every 5 minutes). Download records older than this period are deleted automatically. | `number` | — | `24` |
| **Period unit**<br />`dl_limit_window_unit` | Minutes, hours or days. | `list` | `1` = Minutes<br />`60` = Hours<br />`1440` = Days | `60` (Hours) |
| **Limit per user group**<br />`dl_limit_groups` | Number of files per period. Use -1 for unlimited. Groups not listed (and not inheriting a listed parent group) are not limited. | `subform` | — | — |
| **Guest IP allowance (multiplier)**<br />`dl_limit_guest_ip_factor` | Guests are limited per browser (cookie). To stop quota resets by clearing cookies, they are also limited per IP address, at the group limit multiplied by this number, so several visitors behind one IP address (office, school) do not share a single quota. | `number` | — | `5` |
| **Count coupon / download cart downloads**<br />`dl_limit_count_special` | Downloads made through shared-link coupons or the downloads cart bypass access levels. Select Yes to also apply the limits to them. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Limit reached: modal HTML**<br />`dl_limit_modal_html` | HTML shown in a modal window when a user with an exhausted quota clicks a disabled download button, e.g. text and a Register / Subscribe button. Leave empty for the default message. Placeholders: **&#123;reset_in&#125;** time until the next download is possible (the period is sliding, so the oldest download expires first), **&#123;reset_full_in&#125;** time until the counter is back to zero, **&#123;reset_seconds&#125;** same as &#123;reset_in&#125; in seconds, **&#123;limit&#125;** files allowed, **&#123;used&#125;** files used, **&#123;window&#125;** length of the period, e.g. 5 min, 24 h, 7 d. | `textarea` | — | — |

#### File actions

### File display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |
| **Compact display**<br />`compact_display` | Compact display of files information and file actions to save space. | `radio` | `0` = No<br />`1` = Yes<br />`2` = Yes, as icon | `0` (No) |
| **Value list placement**<br />`values_list_placement` | Value list can be placed inline, or inside a slider | `multilist` | `0` = Inline<br />`1` = In slider | `0` (Inline) |
| **Slider title**<br />`values_slider_title` | You may customize the title of the values list slider | `text` | — | `FLEXI_FILES` (Files) |

#### Item view

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show waveform**<br />`wf_add_waveform` | — | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show Properties**<br />`mm_show_props` | — | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Media properties**<br />`mm_show_props_list` | Select properties to show | `fcmediaprops` | — | `media_format, bit_rate, bits_per_sample, sample_rate, duration, channels` |

#### Category-like views

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show waveform**<br />`wf_add_waveform_cat` | — | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show Properties**<br />`mm_show_props_cat` | — | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Media properties**<br />`mm_show_props_list_cat` | Select properties to show | `fcmediaprops` | — | `media_format, bit_rate, bits_per_sample, sample_rate, duration, channels` |

#### File totals

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Number of files**<br />`display_total_count` | Enable this to show the total number of files | `multilist` | `0` = Hide<br />`1` = Show | `0` (Hide) |
| **Total files label**<br />`total_count_label` | Customize the label text | `text` | — | `FLEXI_FIELD_FILE_TOTAL_FILES` (Total files) |
| **Downloads counter**<br />`display_total_hits` | Enable this to show a sum of the total downloads (hits) | `multilist` | `0` = Hide<br />`1` = Show | `0` (Hide) |
| **Total downloads label**<br />`total_hits_label` | Customize the label text | `text` | — | `FLEXI_FIELD_FILE_TOTAL_DOWNLOADS` (Total downloads) |

#### Individual files

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use mime icon**<br />`useicon` | Add a mime icon before the filename. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Display filename**<br />`display_filename` | Shows filename (NOTE: this you can link filename to download only when using links instead of buttons) | `radio` | `-1` = No (force)<br />`0` = No<br />`1` = Yes, prefer file title<br />`2` = Yes | `1` (Yes, prefer file title) |
| **Lowercase filename**<br />`lowercase_filename` | The filename or file title will be forced to be lowercase | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Link filename**<br />`link_filename` | This will link filename as download. NOTE: this setting is ignored when using buttons instead of links | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Information

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display language**<br />`display_lang` | Show file language. This is useful if you have multiple files with different language contained inside the same item | `radio` | `0` = No<br />`1` = Yes, as icon<br />`2` = Yes, as text<br />`3` = Yes, both | `1` (Yes, as icon) |
| **Display size**<br />`display_size` | Show file size. This can be either in KBs / MBs / GBs | `radio` | `0` = No<br />`1` = Yes, as icon<br />`2` = Yes, as text<br />`3` = Yes, both | `0` (No) |
| **Display hits**<br />`display_hits` | Display hits | `radio` | `0` = No<br />`1` = Yes, as icon<br />`2` = Yes, as text<br />`3` = Yes, both | `0` (No) |
| **Display description**<br />`display_descr` | Shows description as Tooltip OR as Inline Text | `radio` | `0` = No<br />`1` = Yes, as popup tooltip<br />`2` = Yes, as inline text | `1` (Yes, as popup tooltip) |

#### Information separation character(s)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use separation character(s)**<br />`use_info_separator` | You may want not to use separation characters and rely only on CSS for styling the display | `multilist` | `0` = Line break<br />`1` = Custom | `0` (Line break) |
| **Custom**<br />`info_separator` | Separation character(s) will be placed between displayed information | `text` | — | — |

### File list

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Preset configurations**<br />`prx_sfx_open_close_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking) | — |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |

:::note
NOTE: opening / closing texts and value separator, are not used inside a fieldgroup
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Value separator (frontend views)**<br />`separatorf` | Choose a separator to separate the values in frontend views (placed between values) | `multilist` | `0` = Space<br />`1` = Line break<br />`6` = Horizontal line<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters)<br />`7` = Custom separator | `1` (Line break) |
| **Custom separator**<br />`separatorf_custom` | — | `text` | — | — |
| **Opening text for Field**<br />`opentag` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

### Content plugins

#### Content Plugins -- You need this for description field, for other fields enable only if needed

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Trigger content plugins**<br />`trigger_onprepare_content` | Enable this option if you want to trigger content plugin event: onPrepareContent. A small number of plugins may not work outside com_content. | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Trigger inside category**<br />`trigger_plgs_incatview` | Trigger content plugins on this field when item is displayed in a category view | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Specific plugins only**<br />`plugins` | You can choose specific plugins in this list or leave empty to trigger all. This feature is useful in some cases to avoid conflicts, multiple displays or reduce the load. Keep in mind that once the plugin is imported for a field, it will automatically be executed on all following fields in the loop. | `pluginlist` | — | — |

#### Viewing

## Notifications

Enable this to send notifications emails when a file is downloaded

#### Email notifications every N downloads

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Send hit notifications**<br />`send_notifications` | Enable this to send notifications emails when a file is downloaded | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Every N hits**<br />`notifications_step` | Send email every N hits | `text` | — | `20` |
| **Notification text**<br />`notification_tmpl` | The text that will be sent for every file. **NOTE:** you may use these replacements: %%language_string%%, __file_hits__ __file_id__ __file_name__ __item_title__ __item_url__ | `textarea` | — | `%%FLEXI_HITS%% __FILE_HITS__ %%FLEXI_FDN_FILE_NO%% __FILE_ID__: [__FILE_TITLE__] %%FLEXI_FDN_FILE_IN_ITEM%% __ITEM_TITLE__: __ITEM_URL__` |

#### Send TO

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **to specific emails**<br />`send_all_to_email` | Notifications for any file will be sent these email(s) seperate emails with comma , | `text` | — | — |
| **to content item owner**<br />`send_to_current_item_owner` | Send email to owner of the content item that contains the downloaded file | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **to emails of EMAIL field**<br />`send_to_email_field` | The email field must have value(s) in the SAME content item that the file field is contained, e.g. both file field and email field are displayed inside item 'A' | `fields` | — | — |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Media properties**<br />`media_property_filters` | Select properties to show | `fcmediaprops` | — | `media_format, sample_rate, duration` |

#### Filtering

### Category-based views

:::note
Media properties Filters. Currently these effect all Media properties in the same way
:::

#### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show filter label**<br />`display_label_filter` | You can disable filter label or set it to appear at the before (left) of the filter or inside the filter. **NOTE:** This setting can be overridden in category filtering settings for ALL category filters at once | `radio` | `0` = No<br />`1` = Outside Filter<br />`2` = Inside Filter | `2` (Inside Filter) |
| **Display Filter as**<br />`display_filter_as` | Select appearance/behavior of the filter | `multilist` | `0` = Drop-down selector<br />`1` = Text Search<br />`2` = Drop-down selector (range)<br />`3` = Text Search (range)<br />`4` = Radio options<br />`5` = Checkboxes (multi)<br />`6` = Tag-like selector (multi) | `0` (Drop-down selector) |
| **Faceted Filter values according to ...**<br />`faceted_filter` | Calculate the displayed filter values according to either **page configuration** or according to **active Filters**. OPTION: **Disable** this to show all values and achieve high performance in large sites (more than 10,000 items per category or more than 10,000 items in search index). OPTION: **Page configuration** is cacheable and will have a small performance impact on first page load (for large sites) -- this option displays filter values by considering only category configuration and/or (category/search view) menu item configuration. OPTION: **Active filters** is not cacheable and it will have a moderate performance impact on every page load (large sites) when (and if) user activates some filters. -- this option displays filter values by considering everything: alpha-index, text search, field filters, etc, thus offering **best user experience**. | `multilist` | `0` = No, show all values (high performance)<br />`1` = Page configuration (fast & cacheable)<br />`2` = Active filters (best user experience) | `2` (Active filters (best user experience)) |

#### 'Active filters' Faceted Filter (set above)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show matching items per filter value**<br />`show_matching_items` | Enable this to append the number of matching items after each filter value. **NOTE**: this makes no sense when filter is displayed as range or as text input, thus it is not displayed | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Unavailable values for faceted filter using active filters**<br />`hide_disabled_values` | Select to EITHER **disable** OR **hide** the non-available values. **NOTE**: This effects values that are non-available due to active filters. **NOTE**: This work only if you are displaying filter values according to active filters (above) | `radio` | `0` = Disable<br />`1` = Hide | `0` (Disable) |

#### Drop-down selector

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Customize default option (all values)**<br />`filter_usefirstoption` | Enable to customize the first option of the filter (=all values) . NOTE: this is used only in the case of Drop-Down Select, and also if field label is not placed inside the selector | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default Option Text (e.g. All colours)**<br />`filter_firstoptiontext` | Text of first option of the Drop-Down Select e.g. 'All colours' or FLEXI_ALL etc. **NOTE**: This option has no value **NOTE**: This text is language-filtered so you can enter a language replaceable string | `text` | — | `FLEXI_ALL` (All) |

#### Slider

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Slider data**<br />`slider_display_config` | Either use found field values, or specify your custom range of values | `multilist` | `1` = Found values<br />`2` = Custom values | `1` (Found values) |
| **Custom values**<br />`slider_custom_range` | Custom range of values, please use values that exist in the field !, for format, see example format, enter comma separated values: percentage%: 'value', and instead of 0% or 100%, you must use 'min': 'value' and 'max':'min': 'value' | `textarea` | — | `'min': '', '25%': '50', '50%': '150', '75%': '600', 'max': ''` |
| **Custom labels**<br />`slider_custom_labels` | Custom labels to match the values, please enter a ## separated labels without start/end quotes | `textarea` | — | `label_any ## label_50 ## label_150 ## label_600 ## label_any` |
| **Labels are language strings**<br />`slider_custom_labels_jtext` | Set this to yes to treat labels as language strings, remember to add these to your Joomla language overrides manager or in other loaded language files | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Prefix / Suffix

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext_filter` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext_filter` | This text is placed immediately **after** every field value | `text` | — | — |
| **Opening text for Field**<br />`opentag_filter` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag_filter` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

#### Filtering
