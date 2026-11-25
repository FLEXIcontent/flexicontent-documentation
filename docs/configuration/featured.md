---
sidebar_position: 8
---

# Featured

Settings for featured items and the categories used to select them.

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

### Featured Content

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use Joomla Featured Flag**<br />`use_joomla_featured_flag` | You can select to use Joomla Featured or hide it from item form. Joomla featured flag maybe useful, if you want compatibility with non-FLEXIcontent views and modules. A more powerful solution is FLEXIcontent Featured Categories. You may decide to use both Joomla featured flag and FLEXIcontent featured categories. | — | `1` |

:::note
(a) All categories under this parent will be considered as featured. (b) It is recommended not to nest your featured categories, (place them flat)
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Parent of Featured Categories**<br />`featured_cats_parent` | The featured categories allow easier, styled-up and more intuitive management of your 'featured' web content, featured categories are: (a) **specially selectable by your editors in item form and will not appear inside the normal category tree of item form.** -- (of course) An editor will need 'create' privilege on a featured category in order to be able to select it in item form. -- e.g. users buy a **subscription** that adds them to a **usergroup which has create** privilege on some Featured Categories (b) **optionally can receive special markings (markups) in item listings / item view,** thus making the content items stand out of the crowd via CSS style markings (markups) with or without text (c) **can have special usage like being used in Frontpage or be assigned to modules** e.g. categories: 'Frontpage', 'Top Slideshow', etc, in this case you would want to hide direct links via the System Plugin **FLEXIcontent Advanced Route** (please edit plugin configuration) | — | — |
| **Disable subtree parent**<br />`featured_cats_parent_disable` | Usually you would want to disable selecting the root category of the category subtree | — | `1` |
