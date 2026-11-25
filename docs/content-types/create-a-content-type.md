---
title: Create a content type
sidebar_position: 2
---

# Create a content type

A **content type** is an administrator record that defines the fields, authoring rules and display settings for a family of items. FLEXIcontent installs an `Article` type by default; every other structure — event, product sheet, directory, portfolio — is created from **Components → FLEXIcontent → Content Types**.

This page covers the administrator procedure. To write the PHP code of a new field type, see [Create a field type](../fields/create-a-field-type.md).

:::info Source
Based on FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), mainly `admin/models/forms/type.xml`, `admin/models/type.php`, `admin/tables/flexicontent_types.php`, `admin/views/type/view.html.php`, `admin/views/type/tmpl/default.php`, `admin/controllers/types.php` and `admin/access.xml`.
:::

## Before you start

- Your Joomla account must have the component permission **Manage content types** (`flexicontent.managetypes`, exposed as `CanTypes`) to create or edit types.
- To add custom fields, you also need `flexicontent.createfield`.
- Prepare the list of fields you want, and decide whether a simple select field would be enough before creating several similar types.
- Create the categories you want to allow ([guide](../categories/create-a-category.md)), or plan to do it after the type exists.

:::tip
Start with one type and duplicate it later with **Save as Copy**. A type is easier to refine in small steps than to redesign after items already use it.
:::

## 1. Open the type manager

Go to **Components → FLEXIcontent → Content Types**. The direct URL is:

```text
index.php?option=com_flexicontent&view=types
```

Click **New**. The toolbar title is **New type** (`FLEXI_ADD_TYPE`).

## 2. Fill in the header

The top of the form contains the identity and availability settings.

| Setting | Required / default | Notes |
| --- | --- | --- |
| **Name** (`name`) | Required | Shown to editors when they choose a type for a new item. Stored in `#__flexicontent_types.name`. |
| **Alias** (`alias`) | Optional; generated from the name | ASCII-only, underscores allowed. Used in URLs and internal lookups. |
| **Description** | Optional | Text shown when selecting the type for a new item (`FLEXI_REGARDING_ITEM_TYPE_DESCRIPTION_TEXT_USAGE`). |
| **Published** (`published`) | `1` | Unpublishing a type is blocked while items are still associated with it. |
| **Access** (`access`) | Public (`1`) | Joomla view level. Limits who can use the type. |
| **Permit Submission** (`itemscreatable`) | `0` | `0` = any author, `1` = hide the type in the selector when the user lacks `core.create`, `2` = show it disabled. |

The record is stored in `#__flexicontent_types`; its type-specific settings are serialized in the `attribs` column.

:::note
`Permit Submission` does not grant the right to create items by itself. Set the **Create Items** (`core.create`) permission in the type's own **Permissions** tab. The tab also exposes **Change main category**, **Change secondary categories** and **Change featured category**.
:::

## 3. Apply first, then configure

For a new type, click **Apply** (labelled **Add**) after entering the name. This creates the record and reloads the form so that the layout parameters and the type-specific options are available.

The toolbar offers:

| Button | Use |
| --- | --- |
| **Apply** / **Apply & Reload** | Save and reload the form. For a new type it is the button labelled **Add**. |
| **Apply (fast save)** | Available for an existing record; saves without a full reload. |
| **Save** | Save and return to the type manager. |
| **Save & New** | Save, then open a blank type. |
| **Save as Copy** | Available for an existing type; useful to duplicate a structure. |
| **Cancel** | Close the form. |

A successful save shows **Type saved**.

## 4. Configure the type tabs

The form is split into tabs. Every value that is neither empty nor **Use Global** overrides the value inherited from a higher level. The full item override order is:

```text
Component → Menu → Category → Content Type → Item
```

| Tab | What to configure |
| --- | --- |
| Description | The editor-facing description shown on the type selection screen. |
| Core fields | Labels, descriptions and viewing rules for the 14 built-in fields (title, main text, categories, dates, tags, voting, etc.). |
| Authoring | Allowed category subtree, default category and submission-form behaviour. |
| SEO | Page title, metadata and default menu item used to build item URLs. |
| Item view | Allowed item layouts, default item layout (`ilayout`) and mobile layout. |
| Search view | Searchable fields, result priority, filters and result display. |
| Item form | Frontend and backend item-form layouts (`form_ilayout_fe`, `form_ilayout_be`) and form behaviour. |
| Notifications | Emails sent on submission or status changes. |
| Items manager | Default filters and columns in the backend item list. |
| Layout / Themes | Item layout and its parameters. Fields are placed into template positions. |

The exhaustive list of options is on the [Content types — options](./options.md) page.

:::caution
Avoid changing the type of an **existing** item. FLEXIcontent warns that values of fields which are not common between the old and new type will be lost. The type choice is meant to be made when the item is created.
:::

## 5. Assign fields to the type

Field assignment is done in the **Fields** manager, not in the type form.

1. Go to **Components → FLEXIcontent → Fields**.
2. Create a new field or edit an existing one.
3. In the **Basic** tab, select this content type in **Types**. A field can be assigned to several types.
4. Click **Apply & Reload** if you changed the field type, then **Save**.
5. Back in the type's form ordering controls, place the field where you want it in the item form.

The assignment is stored in `#__flexicontent_fields_type_relations`, with the per-type `ordering` used in the item form. Core fields are automatically assigned to all content types except `voting` and `favourites`.

See [Create a field](../fields/create-a-field.md) for the complete field procedure. To structure a long form, add `custom_form_html` markers for tabs/fieldsets or `fieldgroup` for repeatable groups.

:::tip
If a new field does not appear, check that it is published, assigned to this type, and accessible to your user level. Also clear the Joomla cache after changing field assignments.
:::

## 6. Choose the display templates

In the **Layout / Themes** tab, select the item layout that will render items of this type. The [template positions](../templates/positions.md) decide *where* fields appear; the [field layouts](../fields/field-layouts.md) decide *how* their values are rendered.

A menu item pointing to a category or multi-category view can override the type layout for that view. This is why the same type can look different in two places on the site.

## 7. Create and test an item

1. Go to **Components → FLEXIcontent → Contents** and click **New**.
2. Select the new type. Its description is displayed in the type selector.
3. Choose a category, fill in the assigned fields and save.
4. Create a menu item pointing to a FLEXIcontent **category view** or **multi-category view** to see the list on the frontend.
5. Open the item to check the item view layout and the field values.

## Troubleshooting

| Problem | Likely cause |
| --- | --- |
| Type is not in the selector | Type unpublished, access level too high, or `core.create` denied by the type ACL. |
| No custom fields in the item form | Field not assigned to this type, unpublished, or restricted by access. |
| Type-specific options are empty | Click **Apply** first so the new record exists, then reload the form. |
| Cannot unpublish or delete the type | Items are still associated with it. Move or delete those items first. |
| Values disappeared after changing an item's type | The old and new types do not share the same fields. Do not change the type of an existing item. |
| Raw `FLEXI_...` strings in the form | A language key is missing or the cached language files are stale; clear the Joomla cache. |
| Frontend uses another layout | A menu, category or item level value overrides the type setting. Check the override order above. |
| New field is not listed in the type | Clear the Joomla cache; field/type relations and layout paths are cached. |

## Official references

- [Starting with FLEXIcontent (basic usage)](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/330-starting-with-flexicontent-basic-usage.html)
- [Small turn-around FLEXIcontent](https://flexicontent.org/documentation/tutorials-english/83-starting-tutorials/355-eng-4-flexicontent-small-turn-arround-flexicontent.html)
- [Content types feature list](https://www.flexicontent.org/features/content-types.html)
