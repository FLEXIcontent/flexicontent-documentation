---
sidebar_position: 32
---

# Shared video / audio

This field embeds into items, a media (video/audio) player from shared video sites like YouTube, Vimeo, Dailymotion, Vevo, Hulu, Metacafe, etc and audio site like soundclound, last.fm, etc. Media references (field values) can be added to this field, by just copying the URL of the original media page, the media information is fetched (title, author, description, etc) and a preview player is embeded when field is viewed. The field configuration allows to control what information is displayed, as well as the player dimensions. Except for YouTube, Vimeo and Dailymotion, the fetching capability is based on embed.ly service, which is free for up to 5,000 URLs per month. It is recommended to get and enter your own embed.ly API key.

*Plugin : `sharedmedia` — Shared Video/Audio*

:::info Source
This page is generated from `plugins/flexicontent_fields/sharedmedia/sharedmedia.xml` and the official FLEXIcontent 5.x language files.
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
| **Allow multiple values**<br />`allow_multiple` | Allow more than 1 value for this field | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **max # values**<br />`max_values` | The max number of values you wish to record | `text` | — | `0` |
| **Values per row**<br />`fields_box_placing` | Save space by allowing multiple values to show per row | `radio` | `0` = 1<br />`1` = Multiple | `0` (1) |
| **Add position**<br />`add_position` | Select to add value inline (show add button at every value) or append them to the bottom of the value list | `multilist` | `0` = Append to bottom<br />`1` = Inline append<br />`2` = Inline prepend<br />`3` = Inline both | `3` (Inline both) |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
| **Card width (px)**<br />`form_card_width` | Width of the video card in the item edit form, in pixels | `text` | — | `250` |

#### Optional Properties

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Title**<br />`display_title_form` | Display title field in edit form | `radio` | `0` = Hide<br />`2` = Show<br />`1` = Edit | `1` (Edit) |
| **Author**<br />`display_author_form` | Display author field in edit form | `radio` | `0` = Hide<br />`2` = Show<br />`1` = Edit | `1` (Edit) |
| **Description**<br />`display_description_form` | Display description field in edit form | `radio` | `0` = Hide<br />`2` = Show<br />`1` = Edit | `1` (Edit) |
| **Player dimensions**<br />`display_edit_size_form` | Allow user to set specific media player dimensions per media | `radio` | `0` = Hide<br />`2` = Show<br />`1` = Edit | `1` (Edit) |

#### Advanced information

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Embed method / API**<br />`display_api_type_form` | Display Embeed method/API field in edit form | `radio` | `0` = Hide<br />`2` = Show | `0` (Hide) |
| **Embed URL**<br />`display_embed_url_form` | Display ID field in edit form | `radio` | `0` = Hide<br />`2` = Show | `0` (Hide) |
| **Media ID**<br />`display_media_id_form` | Display ID field in edit form | `radio` | `0` = Hide<br />`2` = Show | `0` (Hide) |
| **Duration**<br />`display_duration_form` | Display duration field in edit form NOTE: this information is available via native APIs but not with embed.ly) | `radio` | `0` = Hide<br />`2` = Show | `0` (Hide) |

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
| **Include in CSV export**<br />`include_in_csv_export` | Select to include field in CSV export. Take care that not all fields support CSV export. Please test to determine if this field is included properly, since a special method is needed but not implemented yet by all fields | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Backend View

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Backend view appearance**<br />`backend_view_appearance` | How this field's value is displayed in the admin items list. Overrides the global 'Custom columns appearance' setting when not set to Default. | `multilist` | `0` = Default<br />`1` = Check mark<br />`2` = Clean up HTML and trim | `0` (Default) |
| **Trim length (characters)**<br />`backend_view_trim_chars` | Number of characters to keep after stripping HTML tags. | `text` | — | `100` |

### Layout

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Values layout**<br />`viewlayout` | Please note: - do not modify default layouts, - custom layouts may need updating in future to respect new configuration and work properly - to create new copy (same folder): plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*.php as value_mytemplate.php - or to folder: /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ and then modify | `fcfilelist` | — | — |

#### Value display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show no value message**<br />`show_no_value` | Display a message that field has no value instead of empty display | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No value message**<br />`no_value_msg` | The text to display when field has no value, leave empty to show default text | `text` | — | — |

### Value list

#### Prefix - Suffix - Separator

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Preset configurations**<br />`prx_sfx_open_close_configs` | This is a list of preset configurations, after loading them, you can click custom again to customize them | `multilist` | `—` = Customize<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = List (no marking)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
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

## Playback

### Media

#### Media Info

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Title**<br />`display_title` | Shows the title of the media under the media player | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Title HTML Tag**<br />`headinglevel` | HTML tag for the title (Heading Levels: 1-6) | `list` | `1` = H1<br />`2` = H2<br />`3` = H3<br />`4` = H4<br />`5` = H5<br />`6` = H6 | `3` (H3) |
| **Author**<br />`display_author` | Shows the name of the author under the media player | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Description**<br />`display_description` | Shows the media description under the player | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Native APIs only

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Duration**<br />`display_duration` | Shows the duration of the media in hh:mm:ss format under the media player | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

#### Media player

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Player Width**<br />`width` | Enter the width of the iframe containing the media player in pixels | `text` | — | `480` |
| **Player Height**<br />`height` | Enter the height of the iframe containing the media player in pixels | `text` | — | `270` |
| **Player position**<br />`player_position` | Select the position of the media player relative to the media meta data: title, author, description | `radio` | `0` = Before meta data<br />`1` = After meta data | `0` (Before meta data) |

## APIs (keys, etc)

:::note
**Embeding method** Either use embed.ly only, - or - also use native APIs: youtube, vimeo, dailymotion NOTE: this will not change embeding method of already saved values
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Embed with**<br />`use_native_apis` | Disable to also use native APIs | `multilist` | `0` = noembed API only<br />`1` = noembed API and native APIs | `0` (noembed API only) |
| **Privacy embeed**<br />`privacy_embeed` | If the media provider supports this, then try to embeed the media so that personal data logged are minimized | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Autostart**<br />`autostart` | Includes autostart/autoplay parameter to embed URL. This option is set at fetch and saved with the embed URL. Changing it here requires to re-fetch media. | `radio` | `0` = Browser disabled (security concerns) | `0` (Browser disabled (security concerns)) |

#### Embed.ly Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Force SSL**<br />`force_ssl` | Forces the embedded iframe to use SSL. This option is set at fetch and saved with the embed URL. Changing it here requires to re-fetch media. | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

#### Youtube Configuration

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Youtube API Key**<br />`youtube_key` | Get your youtube v3 API Key (at Google Developer console) https://developers.google.com/youtube/v3/getting-started | `text` | — | — |

### Debug

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Javascript debug**<br />`debug_to_console` | Enable this to add debug information to browser console about AJAX server API calls | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
