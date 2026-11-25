---
sidebar_position: 21
---

# Image / gallery

Image Field Plugin for FLEXIcontent

*Plugin : `image` — Image or Gallery*

:::info Source
This page is generated from `plugins/flexicontent_fields/image/image.xml` and the official FLEXIcontent 5.x language files.
:::

## Editing

#### Editing

### Values

:::note
Note: Image source is in Media manager or Intro/Full image mode. Most settings in this TAB will not be used. Exceptions: Display label, no-access message
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use field in a group**<br />`use_ingroup` | Enable to allow field to be part of field group, that is created via 'Field Group' field. NOTE: You should then select this field in ONLY ONE field group | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |

#### Number of values

:::note
Select to use single image (act as image field) or multiple images (act as gallery field)
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow multiple values**<br />`allow_multiple` | Allow more than 1 value for this field | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Values per row**<br />`fields_box_placing` | Save space by allowing multiple values to show per row | `radio` | `0` = 1<br />`1` = Multiple | `1` (Multiple) |
| **Add position**<br />`add_position` | Select to add value inline (show add button at every value) or append them to the bottom of the value list | `multilist` | `0` = Append to bottom<br />`1` = Inline append<br />`2` = Inline prepend<br />`3` = Inline both | `3` (Inline both) |
| **max # values**<br />`max_values` | The max number of values you wish to record | `text` | — | `0` |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Image Handling

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allowed extensions**<br />`upload_extensions` | Extensions (file types) that are allowed to be uploaded (comma separated) | `text` | — | `bmp,wbmp,gif,jpg,jpeg,png,webp,ico` |
| **Maximum Size**<br />`upload_maxsize` | The maximum size for an upload (in bytes). Use zero for no limit. Note: your server has a maximum limit. | `text` | — | `10000000` |

#### Link to URL

:::note
If you enable this option you will be able to add a link to url, note that no popup of the image will be created
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`linkto_url` | — | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **URL Target**<br />`url_target` | Where to open the URL | `groupedlist` | `_self` = Same Frame/Window/Tab<br />`_blank` = New Window/Tab<br />**Modal popup window**<br />`multibox` = Multibox (built-in)<br />`fancybox` = Fancybox (built-in) | `_self` (Same Frame/Window/Tab) |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Fields layout**<br />`formlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/field_*.php as field_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |

#### Buttons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **File Upload / Select**<br />`file_btns_position` | Choose how and where to display the file Select / Upload buttons | `multilist` | `0` = Icons<br />`1` = Icons, in new row<br />`2` = Icons + text, in new row | `0` (Icons) |

#### Preview thumbnails

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Resizer**<br />`thumb_size_resizer` | Display a dropdown select or a slider to resize the thumbnails | `radio` | `0` = Disable<br />`1` = Drop-down selector<br />`2` = Slider | `0` (Disable) |
| **Default size**<br />`thumb_size_default` | Note this is used only on first opening of form, then the last setting of thumbnails resizer is remembered | `radio` | `90` = 90<br />`120` = 120<br />`150` = 150<br />`200` = 200<br />`250` = 250 | `200` (200) |
| **Processing method**<br />`thumb_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |

### Image Source

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Image Source**<br />`image_source` | **Do not change after values are added, folder mode recommended when creating gallery fields** a. Use **DB MODE**, when assigning attribute images to content items that need to be **resused** by various items and more options are needed than those offered by radio-image , checkbox-image field TYPEs e.g. attributes with descriptions and popup links, etc b. Use **FOLDER mode**, when having non-reuseable images, e.g an image gallery specific to each Content Item | `multilist` | `-2` = Joomla media manager<br />`-1` = Joomla article images: (intro + full)<br />`0` = Reusable (DB mode)<br />`1` = Item+Field Specific Folder | `1` (Item+Field Specific Folder) |

:::note
About top folder (J4+ only) - You must add this folder in PLUGIN: 'FileSystem - Local', e.g. add folder downloads. - For quantum file manager. This is the scope name NOTE: please add an extra custom-named scope for the folder images !! e.g. 'imgs' DO NOT change folder name 'images', 'imgs' will be the name of the custom scope
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Top folder**<br />`jmedia_topdir` | For native media file manager, this is the folder inside Joomla ROOT (that you added in Filestorage plugin, or for Quantum file manager this will be the custom scope name _images_ | `text` | — | — |
| **Sub folder path**<br />`jmedia_subpath` | Select sub-folder to be opened _e.g. content/news -&gt; JPATH_ROOT/images/content/news_ | `text` | — | — |
| **Auto-insert on upload**<br />`autoassign` | Enable this to automatically close popup file-management and assign newly uploaded image(s) to current image value box. NOTE: If multiple new images are uploaded, then value boxes will be added after current one | `radio` | `0` = No<br />`1` = Select and assign<br />`2` = Select only | `1` (Select and assign) |
| **Intro / Full support**<br />`auto_intro_full` | Automatically set Intro(text) and Full(text) image to be the medium and large thumbnails of the first image (of this field) | `radio` | `0` = No<br />`1` = Use first image thumbnails | `0` (No) |

:::note
Note: Settings in TABs 'Values' and 'Optional properties' are not used
:::

#### Thumbnail in view

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item**<br />`img-if-for-itemlist` | — | `radio` | `1` = Intro<br />`2` = Full | `2` (Full) |
| **Category**<br />`img-if-for-catlist` | — | `radio` | `1` = Intro<br />`fulltext` = Full | `1` (Intro) |
| **Module**<br />`img-if-for-modlist` | — | `radio` | `1` = Intro<br />`2` = Full | `1` (Intro) |

### Folder-mode specific parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Same images for associated items**<br />`of_usage` | If item belongs to a translation group of associated items, then use same images for all items. NOTE: the image folder of the content item with the default site language will be used to store images | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Prevent access to original images**<br />`protect_original` | Usually you would want to prevent access to the original image files (this setting is for folder mode, **in the case of DB-mode they are always protected**). If you are are using original images in various configuration parameters, then you need to disable this setting, otherwise your image links will get a server deny error | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

### DB-mode specific parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Target directory**<br />`target_dir` | If you select secure, the users will never see the real path of the file and will only be allowed **indirect access** to the file. This option is suitable for e.g. - document files * - high resolution copyrighted images * * attach to content via **FILE** field ** attach to content via **FILE** field or **image/gallery** field NOTE: 1. If you select media folder, then direct access will be allowed thus you will be able to play media files via media players embedded in visitor's browser. 2. Image files in the secure folder can be either privileged accessed via file field or viewable by (optionally watermarked) thumbnails created by the image/gallery field and you will still keep the secure download feature. | `multilist` | `0` = Media<br />`1` = Secure | `1` (Secure) |
| **Auto delete unused**<br />`auto_delete_unused` | Images that are no longer used my any item will be automatically deleted. Automatic: will delete unused images, - if existing image selection list is hidden, - if existing image selection list is limited to the images used by this field | `radio` | `0` = Automatic<br />`1` = Yes | `1` (Yes) |

#### Existing image list

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Include added by ***<br />`list_all_media_files` | Enable/disable inclusion of images uploaded by other fields or via the file manager (aka all images in the secure folder) NOTE 1: image field does not store images to the DB media folder, but in the DB secure folder for the purpose of protection access to the original image files). NOTE 2: You can select to automatically add _fldNN_ in thubmnail names or select to use a unique thumbnail folder, but make sure you set a unique thumbnail folder for this field !!! otherwise the fields will continuesly overwrite each other thumbnails NOTE 3: If you enable selection of images that were added by any field or filemanager, then image deletion will be disabled | `multilist` | `0` = This field<br />`1` = Any field or filemanager | `0` (This field) |
| **Include uploaded by**<br />`limit_by_uploader` | When listing image uploaded by any field or filemanager then you can limit to only those uploaded by current user (recommeneded) | `radio` | `1` = Current user<br />`0` = Any user | `0` (Any user) |

### Auto-resize uploaded images

:::note
Resizing will be done at the user's browser, thus you get faster upload and less server space consumption
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Resize**<br />`resize_on_upload` | Resize uploaded image to save server space and to speedup uploads, since this will be done at the client size (not all 'source' modes support this) | `multilist` | `—` = Use component setting<br />`0` = No<br />`1` = Yes | — |
| **Image width**<br />`upload_max_w` | — | `text` | — | — |
| **Image height**<br />`upload_max_h` | — | `text` | — | — |
| **Processing method**<br />`upload_method` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `—` = Use component setting<br />`0` = Scale<br />`1` = Crop | — |

### Media URL

:::note
PLEASE NOTE: If media-URL is enabled then **fancybox** layout will be forced, except when **GLightbox** layout is selected (it supports video URLs natively)
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_mediaurl` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Video URLs (Youtube, Vimeo)<br />`2` = Any URL | `0` (No) |
| **Default**<br />`default_mediaurl` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`mediaurl_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

### Optional Properties

:::note
Note: Image source is in Media manager or Intro/Full image mode. Settings in this TAB will not be used
:::

#### Alternative Text

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_alt` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default**<br />`default_alt` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`alt_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

#### Tooltip Title

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_title` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default**<br />`default_title` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`title_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

#### Tooltip Description

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_desc` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Default**<br />`default_desc` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`text_desc` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

#### CUSTOM 1

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_cust1` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default**<br />`default_cust1` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`cust1_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

#### CUSTOM 2

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable**<br />`use_cust2` | If you enable this, then user will be able to override default property value when editing the field in item form | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Default**<br />`default_cust2` | Set a default property value to be loaded when editing field in item form and/or when displaying field in item/category/etc views | `text` | — | — |
| **Usage of default**<br />`cust2_usage` | Select when these default property value will be used | `list` | `0` = Load when editing new items, (requires saving)<br />`1` = Load when editing all items, (requires saving)<br />`2` = The above & also display it instead of empty | `0` (Load when editing new items, (requires saving)) |

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
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Export

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `multilist` | `0` = No<br />`1` = Raw values<br />`2` = Rendered values | `0` (No) |
| **Rendered format**<br />`csv_export_format` | **HTML**: the image display (as in frontend). **Importable**: values that the batch import tool can read back, to transfer images to another site. - Format: filename&#123;Alt&#125;...&#123;/Alt&#125;&#123;Title&#125;...&#123;/Title&#125;&#123;Desc&#125;...&#123;/Desc&#125;&#123;Cust1&#125;...&#123;/Cust1&#125;&#123;Cust2&#125;...&#123;/Cust2&#125;&#123;Link&#125;...&#123;/Link&#125;&#123;MediaURL&#125;...&#123;/MediaURL&#125; (only non-empty properties are added) - Only the filename of the original image is exported, place the image files inside the root of the import media folder (e.g. tmp/fcimport_media) of the target site. Values are never stripped of their &#123;...&#125; tags, even if HTML stripping is enabled. | `radio` | `html` = HTML<br />`importable` = Importable | `html` (HTML) |

#### Backend View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Backend view appearance**<br />`backend_view_appearance` | How this field's value is displayed in the admin items list. Overrides the global 'Custom columns appearance' setting when not set to Default. | `multilist` | `0` = Default<br />`1` = Check mark<br />`2` = Clean up HTML and trim | `0` (Default) |
| **Trim length (characters)**<br />`backend_view_trim_chars` | Number of characters to keep after stripping HTML tags. | `text` | — | `100` |

### Thumbnails

### Thumbnail Creation

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default Image**<br />`default_image` | Specify the path of the image that is displayed when this item field is left empty. **NOTE**: Leave blank not to display any image. Specify the image path relative to the Joomla installation: e.g. images/stories/default/mylogo.png | `media` | — | — |
| **Default image via custom code**<br />`default_image_custom` | Execute custom code to get the default image | `multilist` | `0` = No<br />`2` = Use custom code | `0` (No) |
| **Custom code**<br />`default_image_custom_code` | Enter PHP code to be used create the custom value, please set to empty and save to load the default example, and then customize | `editor` | — | `alias . '.jpg';` |
| **Thumbnails folder * Folder mode creates subfolder per item**<br />`dir` | Folder where the thumbnails will be stored, **relative to your joomla site**, (No slash at the begining, no slash at the end!) If **Folder mode** is enabled, then **subdirectories** will be created for every content item, and furthermore the image original files will be placed here instead of the Global FLEXIcontent document (secure) folder | `text` | — | `images/stories/flexicontent` |
| **Unique thumbmnail via**<br />`unique_thumb_method` | When sharing images among fields we need to prevent fields from overwriting each other thumbnails. You can select to either **automatically** add _fldNN_ in thubmnail names or select to use a unique thumbnail folder, which you must set above **manually** | `radio` | `0` = Field id (automatic)<br />`1` = Thumbnails Folder (set a unique above) | `0` (Field id (automatic)) |
| **Thumbnails quality**<br />`quality` | Thumbnails quality. This parameter affects the JPG compression rate. A large value will increase quality and file size. | `text` | — | `90` |

#### WebP Generation

:::note
Requires PHP GD compiled with WebP support (imagewebp) OR ImageMagick installed on the server. Run: php -r \"echo function_exists('imagewebp') ? 'OK' : 'NO';\
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Generate WebP variants**<br />`generate_webp` | If enabled, a .webp file will be generated alongside each thumbnail (s, m, l). Existing images will get their .webp on next page visit (lazy) or via CLI script. A exemple of CLI script is avaiable in field folder, CLI_rebuild_webp.php. | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **WebP quality (1-100)**<br />`webp_quality` | Compression quality for generated WebP images. 80 is a good balance between quality and file size. | `text` | — | `80` |

#### Watermark image

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Watermark opacity**<br />`wm_opacity` | Choose the percentage of opacity of your watermark. For better results leave this value to 100% and adjust the transparency directly in the image file. | `text` | — | `100` |
| **Watermark position**<br />`wm_position` | Choose the watermark position. | `list` | `*` = Repeat<br />`C` = Middle<br />`TL` = Top left<br />`T` = Top center<br />`TR` = Top right<br />`BL` = Bottom left<br />`B` = Bottom center<br />`BR` = Bottom right | `BR` (Bottom right) |

#### Large thumbnails

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Thumbnail width**<br />`w_l` | Thumbnail max width | `text` | — | `800` |
| **Thumbnail height**<br />`h_l` | Thumbnail max height | `text` | — | `600` |
| **Set thumbnail width as**<br />`l_thumb_width_as_min_or_max` | Set image's size as min-width or as max-width | `radio` | `0` = Min width<br />`1` = Max width | `0` (Min width) |
| **Processing method**<br />`method_l` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `0` = Scale<br />`1` = Crop | `0` (Scale) |
| **Use watermark**<br />`use_watermark_l` | Use watermark | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Watermark image**<br />`wm_l` | Choose the PNG image you would like to use as watermark. The file path must be relative to your joomla site. No slash at the begining, no slash at the end!!! | `text` | — | `plugins/flexicontent_fields/image/image/watermarks/wm_l.png` |
| **Copy original ***<br />`copy_original_l` | Copy original if thumbnail width, height match and watermark is disabled | `radio` | `0` = No<br />`1` = Yes<br />`2` = Yes, regardless settings | `1` (Yes) |

#### Medium thumbnails

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Thumbnail width**<br />`w_m` | Thumbnail max width | `text` | — | `400` |
| **Thumbnail height**<br />`h_m` | Thumbnail max height | `text` | — | `300` |
| **Set thumbnail width as**<br />`m_thumb_width_as_min_or_max` | Set image's size as min-width or as max-width | `radio` | `0` = Min width<br />`1` = Max width | `0` (Min width) |
| **Processing method**<br />`method_m` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `0` = Scale<br />`1` = Crop | `0` (Scale) |
| **Use watermark**<br />`use_watermark_m` | Use watermark | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Watermark image**<br />`wm_m` | Choose the PNG image you would like to use as watermark. The file path must be relative to your joomla site. No slash at the begining, no slash at the end!!! | `text` | — | `plugins/flexicontent_fields/image/image/watermarks/wm_m.png` |
| **Copy original ***<br />`copy_original_m` | Copy original if thumbnail width, height match and watermark is disabled | `radio` | `0` = No<br />`1` = Yes<br />`2` = Yes, regardless settings | `1` (Yes) |

#### Small thumbnails

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Thumbnail width**<br />`w_s` | Thumbnail max width | `text` | — | `120` |
| **Thumbnail height**<br />`h_s` | Thumbnail max height | `text` | — | `90` |
| **Set thumbnail width as**<br />`s_thumb_width_as_min_or_max` | Set image's size as min-width or as max-width | `radio` | `0` = Min width<br />`1` = Max width | `0` (Min width) |
| **Processing method**<br />`method_s` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Use watermark**<br />`use_watermark_s` | Use watermark | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Watermark image**<br />`wm_s` | Choose the PNG image you would like to use as watermark. The file path must be relative to your joomla site. No slash at the begining, no slash at the end!!! | `text` | — | `plugins/flexicontent_fields/image/image/watermarks/wm_s.png` |
| **Copy original ***<br />`copy_original_s` | Copy original if thumbnail width, height match and watermark is disabled | `radio` | `0` = No<br />`1` = Yes<br />`2` = Yes, regardless settings | `1` (Yes) |

#### Backend thumbnails

:::note
Please edit COMPONENT "configuration" , or TYPE configuration to select CUSTOM COLUMNS for item manager.
:::

:::note
Note: this is not used in ITEM FORM, to configure item form preview thumbnails, please visit 'Editing' TAB
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Thumbnail width**<br />`w_b` | Thumbnail max width | `text` | — | `40` |
| **Thumbnail height**<br />`h_b` | Thumbnail max height | `text` | — | `30` |
| **Processing method**<br />`method_b` | Method of creating the image thumbnail. Scale: scales to fit both dimensions, keeping the aspect (height/width) ratio Crop: scales the image and as soon as one dimension fits the other dimension is cropped to the given size | `radio` | `0` = Scale<br />`1` = Crop | `1` (Crop) |
| **Use watermark**<br />`use_watermark_b` | Use watermark | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Watermark image**<br />`wm_b` | Choose the PNG image you would like to use as watermark. The file path must be relative to your joomla site. No slash at the begining, no slash at the end!!! | `text` | — | `plugins/flexicontent_fields/image/image/watermarks/wm_s.png` |
| **Copy original ***<br />`copy_original_b` | Copy original if thumbnail width, height match and watermark is disabled | `radio` | `0` = No<br />`1` = Yes<br />`2` = Yes, regardless settings | `1` (Yes) |

### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Preset configurations**<br />`prx_sfx_open_close_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking) | — |
| **Remove space**<br />`remove_space` | Remove the space between prefix value and suffix. It's recommended for plugin use, for example &#123;play&#125;mysong.mp3&#123;/play&#125; | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

:::note
Not applied in inline (non-popup) galleries like: Elastislide / Galleriffic
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Every value prefix**<br />`pretext` | This text is placed immediately **before** every field value | `text` | — | — |
| **Every value suffix**<br />`posttext` | This text is placed immediately **after** every field value | `text` | — | — |
| **Value separator (frontend views)**<br />`separatorf` | Choose a separator to separate the values in frontend views (placed between values) | `list` | `0` = Space<br />`1` = Line break<br />`2` = Pipe<br />`3` = Comma<br />`4` = Texts: Closing + Opening<br />`5` = Empty (No characters) | `0` (Space) |
| **Opening text for Field**<br />`opentag` | This applied once at the START of the field. It is meant to create the start of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |
| **Closing text for Field**<br />`closetag` | This applied once at the END of the field. It is meant to create the end of the field HTML, but above you can choose to place it as SEPARATING text of the values too. But prefer to use parameters: **Prefix/Suffix text of values** if they exist for this field type. | `text` | — | — |

### Layout

#### Item view

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display method**<br />`default_method_item` | Default display method for the view | `multilist` | `display` = All thumbnails<br />`display_single` = Single<br />`display_single_total` = Single + total | `display` (All thumbnails) |

#### Category (content lists)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display method**<br />`default_method_cat` | Default display method for the mulit-item listings, usually you will want to display a single image that links to the item details view | `multilist` | `display` = All thumbnails<br />`display_single` = Single<br />`display_single_total` = Single + total<br />`display_link` = All thumbnails, link to item | `display_single` (Single) |
| **Link to item**<br />`cat_link_single_to` | Usually when you display the field as single thumbnail in category view, you would also want to link to the item details view | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Gallery Navigation

:::note
Gallery navigation JS has been disabled in ITEM & CATEGORY view, because parameter 'Link to URL' was enabled
:::

:::note
Gallery navigation JS has been disabled in CATEGORY view, because parameter 'Link to item' was enabled
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Gallery**<br />`usepopup` | Choose to **either** display a PLAIN thumbnail list **or** place your thumbnails inside a popup/inline/other Gallery Layout -- The **Gallery Layout** will allow opening the thumbnails in a popup or inline (manual or automatic) image slideshow / carousel | `multilist` | `0` = Thunbnail Only<br />`1` = Yes | `1` (Yes) |
| **Enable in views**<br />`popupinview` | You can turn on/off the above parameter depending on current flexicontent view | `fccheckbox` | — | — |
| **Group with other image fields**<br />`grouptype` | Enabling this will make the field participate in a chained group of images with next and previous buttons. **NOTE:** -- This is not supported by ALL JS gallery types e.g not supported for Rockbox popup **NOTE:** (a) **Per item**, will group all image fields of each item e.g. in category view images will be grouped per item, and of course in item view too, (b) **per view**, will group the image fields according to the displayed view: all images of item view, all images of category view, all images of all flexicontent modules | `radio` | `0` = No<br />`1` = Per item<br />`2` = Per view | `1` (Per item) |

#### Layout

:::note
If 'Media URL' is enabled, the layout is forced to 'fancybox' except for the 'GLightbox' layout which supports video URLs natively
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Gallery Layout (Desktop clients)**<br />`popuptype` | Choose the Gallery Layout that you wish to use | `fclayout` | **Popup layouts**<br />`1` = Multibox (built-in)<br />`2` = Rokbox (needs an active Rockettheme)<br />`3` = JCE MediaBox (needs JCE Editor installed)<br />`4` = Fancybox (built-in)<br />`6` = Widgetkit (needs manual loading)<br />`8` = PhotoSwipe (built-in)<br />`11` = GLightbox (built-in, 100% vanilla JS)<br />`12` = Swiper gallery + GLightbox (built-in, 100% vanilla JS)<br />**Inline layouts**<br />`5` = Galleriffic (Slideshow + carousel) (Built-in)<br />`7` = Elastislide (Slideshow + carousel) (Built-in)<br />`9` = Pannellum (Panorama)<br />`10` = Juxtapose<br />**Enable via parameters**<br />`value_link_to_url` = Link to URL<br />`value_link_to_item` = Link to item<br />`value_thumbnail_basic` = Thunbnail Only | `4` (Fancybox (built-in)) |
| **Gallery Layout (Mobile clients)**<br />`popuptype_mobile` | Choose the Gallery Layout that you wish to use when mobile clients are detected. You can select to use the same as for desktop clients | `fclayout` | **Popup layouts**<br />`1` = Multibox (built-in)<br />`2` = Rokbox (needs an active Rockettheme)<br />`3` = JCE MediaBox (needs JCE Editor installed)<br />`4` = Fancybox (built-in)<br />`6` = Widgetkit (needs manual loading)<br />`8` = PhotoSwipe (built-in)<br />`11` = GLightbox (built-in, 100% vanilla JS)<br />`12` = Swiper gallery + GLightbox (built-in, 100% vanilla JS)<br />**Inline layouts**<br />`5` = Galleriffic (Slideshow + carousel) (Built-in)<br />`7` = Elastislide (Slideshow + carousel) (Built-in)<br />`9` = Pannellum (Panorama)<br />`10` = Juxtapose<br />**Enable via parameters**<br />`value_link_to_url` = Link to URL<br />`value_link_to_item` = Link to item<br />`value_thumbnail_basic` = Thunbnail Only | — |

#### Thumbnails

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use lazyloading**<br />`use_lazy_loading` | Set yes to use native browser lazy loading | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Category View**<br />`thumbincatview` | Which size of thumbnail to use in category view, if you use large no popup will be added | `radio` | `1` = Small<br />`2` = Medium<br />`3` = Large<br />`4` = Original | `1` (Small) |
| **Item View**<br />`thumbinitemview` | Which size of thumbnail to use in item view, if you use large no popup will be added | `radio` | `1` = Small<br />`2` = Medium<br />`3` = Large<br />`4` = Original | `2` (Medium) |

#### Information

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show Title**<br />`showtitle` | Show (tooltip) Title next/after image (use CSS to style this) | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Show Description**<br />`showdesc` | Show (tooltip) Long Description next/after image (use CSS to style this) | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Hovering Legend

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display tooltip**<br />`uselegend` | Display the legend in a tooltip | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Enable in views**<br />`legendinview` | You can turn on/off the above parameter depending on current flexicontent view | `fccheckbox` | — | — |

### Parameters

### Parameters

#### Viewing

## Social

### Social websites support (e.g. Facebook)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Suggest field to listings**<br />`useogp` | Select to suggest (force) image to appear in social website image listings | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Image size in listings**<br />`ogpthumbsize` | Select which thumbnail image to use in the social website image listing, avoid small thumbnail, and images smaller than e.g. 250px width | `list` | `1` = Small (not recommended)<br />`2` = Medium<br />`3` = Large<br />`4` = Original | `2` (Medium) |
| **Suggest images**<br />`ogplimit` | Select to suggest all available images to social websites or limit suggestion to first image only | `radio` | `0` = All<br />`1` = First only | `1` (First only) |

## Filtering

Parameters used for filtering in (a) Category-based views , (b) search view

### Advanced Search View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display Filter as**<br />`display_filter_as_s` | Select appearance/behavior of the filter | `list` | `1` = Text Search | `0` |
