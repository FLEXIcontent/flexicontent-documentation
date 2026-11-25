---
title: Create a category
sidebar_position: 2
---

# Create a category

FLEXIcontent uses Joomla!'s native categories and adds its own display, filter, list, RSS, notification and template settings. Categories are created from **Components → FLEXIcontent → Categories**. They can be nested, and an item can be assigned to a primary category plus secondary categories.

This page covers the administrator procedure. For the concept, see [Categories](../concepts/categories.md); for every setting, see [Categories — options](./options.md).

:::info Source
Based on FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), mainly `admin/models/forms/category.xml`, `admin/models/category.php`, `admin/views/category/view.html.php`, `admin/views/category/tmpl/default.php`, `admin/controllers/category.php` and `admin/access.xml`.
:::

## Before you start

- Opening the category form requires the component permission **Manage categories** (`flexicontent.managecats`, exposed as `CanCats`).
- Creating a category also requires `core.create` on `com_flexicontent`, or on at least one category. Editing a category requires `core.edit` or `core.edit.own` on that category.
- Decide where the category belongs in the tree. The **Parent Category** selector only offers categories on which you have the relevant create/edit permission.
- Prepare the title, a short alias, the access level and the language before starting.

:::tip
Keep the first tree shallow. You can nest categories later, and inheritance lets child categories reuse the parameters of a parent.
:::

FLEXIcontent categories are stored in Joomla!'s `#__categories` table with the extension defined by `FLEXI_CAT_EXTENSION` (the default component setting is `com_content`). Using the FLEXIcontent category manager ensures that the FLEXIcontent parameters are saved alongside the standard Joomla! category fields.

## 1. Open the category manager

Go to **Components → FLEXIcontent → Categories**. The direct URL is:

```text
index.php?option=com_flexicontent&view=categories
```

Click **New**. The toolbar title is **New Category** (`FLEXI_NEW_CATEGORY`).

## 2. Fill in the Basic tab

The **Basic** tab contains the identity and availability settings.

| Setting | Required / default | Notes |
| --- | --- | --- |
| **Title** (`title`) | Required | Category name shown in lists and menus. |
| **Alias** (`alias`) | Optional; generated from the title | Used in SEF URLs. |
| **Description** (`description`) | Optional | Shown in the category view when the display parameters enable it. |
| **Parent Category** (`parent_id`) | Joomla! root by default | Choose the parent in the tree. The current category and its descendants cannot be selected as their own parent. |
| **Published** (`published`) | `1` | `1` = published, `0` = unpublished, `2` = archived, `-2` = trashed. |
| **Access** (`access`) | Public (`1`) | Joomla! view level allowed to see the category. |
| **Language** (`language`) | All (`*`) | Assign a content language, or keep All for a multilingual site using associations. |
| **Category notes** (`note`) | Optional | Internal note displayed in the backend category manager. |
| **Image** / **Image alt** (`image`, `image_alt`) | Optional | Image and alternative text used by the category layout. |

The **Path**, created/modified information and hits are read-only. After saving, the toolbar also offers a **Preview** button.

## 3. Save the category

The toolbar buttons are:

| Button | Use |
| --- | --- |
| **Add** / **Apply & Reload** | Save and reload the form. For a new category, the button is labelled **Add** (`FLEXI_ADD`). |
| **Apply (fast save)** | Available for an existing category; saves without a full reload. |
| **Save** | Save and return to the category manager. |
| **Save & New** | Save, then open a blank category. |
| **Save as Copy** | Available for an existing category; useful to duplicate a structure. |
| **Preview** | Open the frontend category link in a new window (existing categories only). |
| **Cancel** / **Close** | Leave the form. |

A successful save shows **Category saved**.

## 4. Configure the display tabs

The **Display** section contains the settings that make FLEXIcontent categories different from native Joomla! categories.

| Tab | What to configure |
| --- | --- |
| Publishing, Meta | Publishing data and the meta description / meta keywords. |
| Associations | Multilingual category associations, when associations are enabled. |
| Category display header | Print, e-mail, feed and CSV buttons, the **Add new item** button, icon style and button placement. |
| Search & filter form | The filters offered above the item list. |
| Layout | Category layout (`clayout`), optional mobile layout (`clayout_mobile`), layout switcher, allowed/displayed layouts and layout-specific parameters. |
| Items list | Sorting, pagination, columns and which fields are used in the list. |
| RSS feeds | Feed settings for this category. |
| Parameters handling | Inheritance source and one-time parameter copy. |
| Notifications | Notification settings; category-specific recipients require **Allow category specific** to be enabled in the component configuration. |
| Permissions | Category ACL: create, edit, change state, delete and CSV export. |

The [template structure](../templates/structure.md) defines the category view; [template positions](../templates/positions.md) decide where its blocks appear. The exhaustive option tables are on the [Categories — options](./options.md) page.

## 5. Understand parameter inheritance

A value that is neither empty nor **Use Global** overrides the inherited value. For the category view, the override order is:

```text
Component → Inherited category → Category → Author → Menu
```

The **Inherit parameters from** (`inheritcid`) setting accepts:

| Value | Meaning |
| --- | --- |
| Empty (`Use Global`) | Use the component setting. |
| `0` (`Component only`) | Use component parameters only. |
| `-1` (`Parent categories (multi-level)`) | Inherit from the parent tree, up to the first parent that does not inherit. |
| A category ID | Inherit from that specific category. This is single-level and does not cascade further. |

For inheritance to work, leave the child category's own parameters empty or set them to **Use Global**. When a specific layout is selected, its layout parameters are also part of the inherited set.

**Copy all parameters from** (`copycid`) is different from inheritance: on the next **Save** or **Apply & Reload**, it replaces this category's parameters with a snapshot of the source category's parameters, then the selector is cleared. It happens only once.

## 6. Use the new category

1. Open the content type that authors will use and allow this category in its **Authoring** settings. See [Create a content type](../content-types/create-a-content-type.md).
2. Create an item and select the new category as its primary category; add secondary categories if needed.
3. Create a menu item pointing to a FLEXIcontent **category view** or **multi-category view**, and choose the category and layout to display.
4. Open the frontend page and check the header, filters, item list and layout.

A menu item can override category settings for its own view. This is why the same category can look different in two places on the site.

:::caution
Changing the parent of a category changes its position in the nested tree. Check permissions and existing menu links before moving a category that already contains items.
:::

## Troubleshooting

| Problem | Likely cause |
| --- | --- |
| Cannot open the category form | `flexicontent.managecats` is denied. |
| Cannot create a category under a parent | `core.create` is denied on that parent, or the parent cannot be used because it is below the current category. |
| Category is missing in the item form | Category unpublished, access level too high, or not allowed by the content type's Authoring settings. |
| Parameters do not apply | They are empty or **Use Global**, so an inherited value wins. Check the override order above. |
| Wrong layout on the frontend | `clayout` is empty/inherited, or the menu item overrides the category layout. |
| Copy parameters had no effect | Select the source category and then click **Save** or **Apply & Reload**; the choice is cleared after one save. |
| Raw `FLEXI_...` strings in the form | A language key is missing or cached language files are stale; clear the Joomla cache. |

## Official references

- [Starting with FLEXIcontent (basic usage)](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/330-starting-with-flexicontent-basic-usage.html)
- [How to use an FC category as Homepage / Frontpage](https://flexicontent.org/documentation/tutorials-english/75-basic-usage/194-how-to-use-an-fc-category-as-homepage-frontpage.html)
- [How to make multiple Featured Categories](https://flexicontent.org/documentation/tutorials-english/75-basic-usage/273-how-to-make-multiple-featured-categories.html)
- [Template FLEXIcontent — Part 1: The structure](https://flexicontent.org/documentation/tutorials-english/84-advanced-tutorials/335-template-flexicontent-part-1-the-structure.html)
