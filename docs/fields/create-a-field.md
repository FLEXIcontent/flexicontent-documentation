---
title: Create a field
sidebar_position: 2
---

# Create a field

A field stores one piece of structured data in a FLEXIcontent item. This guide covers creating a normal custom field in FLEXIcontent 5.x, assigning it to content types, and making it available in the item form and on the frontend.

:::info Source
Based on FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), mainly `admin/models/forms/field.xml`, `admin/models/field.php`, `admin/views/field/tmpl/default.php`, `admin/tables/flexicontent_fields.php` and `admin/controllers/fields.php`.
:::

## Before you start

- Enable the **field type plugin** you need in **System → Manage → Plugins** (`flexicontent_fields` group).
- Create at least one **content type** in **Components → FLEXIcontent → Content types** ([guide](../content-types/create-a-content-type.md)).
- Your Joomla account needs permission to add fields (`CanAddField`) and, for the Permissions tab, to configure field ACL.

:::tip
Before creating a new field, check whether an existing field with a [custom layout](./field-layouts.md) can do the job. Many presentation needs do not require a new field.
:::

## 1. Open the field manager

Go to **Components → FLEXIcontent → Fields** and click **New**. The form title is **New field**.

The direct URL is:

```text
index.php?option=com_flexicontent&view=fields
```

## 2. Fill in the header

The top of the form contains the three essential settings.

| Setting | Required | Notes |
| --- | --- | --- |
| **Label** | Yes | Text shown in the item form. Can be a Joomla language key. |
| **Name** | No | Machine name used in templates, modules and the database. If empty or invalid, FLEXIcontent derives it from the label. |
| **Field type** | No | Defaults to `text`. The list contains the enabled `flexicontent_fields` plugins. |

### Name rules

- Allowed characters: ASCII letters, digits, `_` and `-` (`/^[a-z_0-9-]+$/i`).
- Invalid or empty names are automatically corrected from the label; FLEXIcontent shows a warning.
- Duplicate names receive a suffix `-2`, `-3`, etc.
- Avoid reusing the 14 built-in core names: `text`, `created`, `created_by`, `modified`, `modified_by`, `title`, `hits`, `document_type`, `version`, `state`, `voting`, `favourites`, `categories`, `tags`.

:::warning
Choose the name carefully. Renaming a field later breaks templates, modules or custom code that reference the old name.
:::

When you change the field type, click **Apply & Reload** to load the type-specific parameters. A new unsaved field shows the message “Please apply to see this field specific parameters!!!”.

## 3. Basic tab

| Option | Default | Purpose |
| --- | --- | --- |
| **Published** | `1` | An unpublished field is not loaded in the item form. |
| **Access** | `1` (Public) | Joomla view level. Restricts frontend visibility. |
| **Ordering** | `999` | General ordering. The order inside the item form is defined per content type. |
| **Types** | none | Content types that may use this field. Stored in `#__flexicontent_fields_type_relations`. |

Select at least one content type in **Types**. The field is loaded only for items whose type is assigned here.

## 4. Item form tab

These options control how the field behaves while editing an item:

| Option | Purpose |
| --- | --- |
| **Description** | Help text displayed in the item form. |
| **Label for form** (`label_form`) | Different label for the editing form. Can be a language key. |
| **Untranslatable** | Disables translation of the field value. |
| **Form hidden** (`formhidden`) | `0` No, `1` Frontend, `2` Backend, `3` Both, `4` If empty. |
| **Values editable** | Restricts who may edit existing values. |
| **Edit help** | Controls the help/information display in the form. |

Some rows are hidden when the selected field type does not support them. There is no general category-assignment tab in the field form; category scoping comes from the template/layout and from field-type options such as `catids` or `rootcatid`.

## 5. Search, filtering tab

| Option | Purpose |
| --- | --- |
| **Basic index** — `issearch`, `isfilter` | Include the field in basic search and list filters. |
| **Advanced index** — `isadvsearch`, `isadvfilter` | Include the field in advanced search and filters. |
| **Rebuild Search Index** | Rebuild the index when FLEXIcontent reports it as dirty. |

## 6. Field type configuration

The right tabset is generated from the selected plugin's XML manifest. The tabs and options differ by type; typical groups are **Editing**, **Viewing**, **SEO** and **Filtering**.

Common options include:

| Option | Purpose |
| --- | --- |
| `required` | Makes the value mandatory in the item form. |
| `allow_multiple`, `max_values` | Allows and limits multiple values. |
| `default_value`, `default_value_use` | Pre-fills a value: `0` new items, `1` every edit, `2` also show when empty. |
| `showon` | Shows the field conditionally, depending on another field. |
| `use_ingroup` | Includes the field in a repeatable field group. |
| **Values layout** (`viewlayout`) | Chooses the [field output layout](./field-layouts.md). |

The [field reference pages](./index.md) list the complete options for each type.

## 7. Permissions tab

Available to users who can configure field ACL. Joomla permissions are stored on the asset `com_flexicontent.field.<id>`. The field's **Access** level and these rules both limit who can see or edit the value.

## 8. Save the field

The toolbar offers **Apply**, **Apply & Reload**, **Save**, **Save & New**, **Save as Copy** (non-core fields only) and **Cancel**. A successful save shows **Field saved**.

At this point the field exists, but it is not yet necessarily visible in the item form or on the frontend.

## 9. Place the field in the item form

1. Return to **Components → FLEXIcontent → Fields**.
2. Filter the list by the relevant content type.
3. Use the ordering controls to position the field in that type's form.

The order is stored per content type in `#__flexicontent_fields_type_relations.ordering`.

To structure the form, add structural field types:

- `custom_form_html` — tabset and fieldset markers, custom HTML.
- `fieldgroup` — repeatable groups of fields.
- `coreprops` — places built-in core properties such as `alias`, `category`, `access`, `metadata` or `perms` in the form.

`coreprops` does not create a new value; it only positions an existing core property.

## 10. Display the field on the frontend

Field assignment and form ordering do not make a field visible on the site. The frontend uses template positions:

1. Go to the FLEXIcontent **Template manager**.
2. Edit the item layout or the category layout used by your content type/category.
3. Drag the field into a position.
4. Save the template.

See [Field positions and drag and drop](../templates/positions.md).

Two common symptoms follow from this separation:

| Symptom | Check |
| --- | --- |
| The field is absent from the item form | Published, assigned to the type, access level, field type support. |
| The field is filled in but not displayed | The field must also be in the active item/category template position. |

## Available field types

`field_type` is the name of an enabled `flexicontent_fields` plugin.

| Family | Plugin names | Documentation |
| --- | --- | --- |
| Selection | `radio`, `radioimage`, `checkbox`, `checkboximage`, `select`, `selectmultiple` | [Radio](./radio.md), [Select](./select.md), [Checkbox](./checkbox.md) |
| Single property | `color`, `date`, `text`, `textarea`, `textselect` | [Text](./text.md), [Textarea](./textarea.md), [Date](./date.md) |
| Multi property | `weblink`, `email`, `phonenumbers`, `termlist` | [Email](./email.md), [Phone](./phonenumbers.md) |
| Media | `file`, `image`, `mediafile`, `sharedmedia`, `addressint` | [Image](./image.md), [File](./file.md), [Address](./addressint.md) |
| Form structure | `subform`, `fieldgroup`, `account_via_submit`, `custom_form_html`, `coreprops` | [Subform](./subform.md), [Field group](./fieldgroup.md) |
| Display helpers | `toolbar`, `fcloadmodule`, `fcpagenav`, `linkslist`, `authoritems`, `jprofile`, `comments` | [Toolbar](./toolbar.md), [Load module](./fcloadmodule.md) |
| Relations | `relation`, `relation_reverse`, `autorelationfilters` | [Relation](./relation.md), [Reverse relation](./relation_reverse.md) |

The `core` plugin powers the built-in fields and is hidden from the normal selector.

If none of these types stores or processes the data you need, [write a new field type plugin](./create-a-field-type.md).

## Core fields vs custom fields

FLEXIcontent installs 14 core fields: `text`, `created`, `created_by`, `modified`, `modified_by`, `title`, `hits`, `document_type`, `version`, `state`, `voting`, `favourites`, `categories`, `tags`.

- New fields always have `iscore = 0`; you cannot create a core field.
- Core field names are read-only.
- Core fields with ids 1–6 cannot be unpublished or deleted.
- Core fields with ids below 15 cannot be copied.
- Core fields are automatically assigned to all content types, except `voting` and `favourites`.

Use `coreprops` when you only need to place an existing core property in the item form.

## FLEXIcontent fields are not Joomla custom fields

| | FLEXIcontent field | Joomla `com_fields` custom field |
| --- | --- | --- |
| Storage | `#__flexicontent_fields`, values in field item relations. | `#__fields`, `#__fields_values`. |
| Field types | `flexicontent_fields` plugins. | Joomla field plugins. |
| Assignment | FLEXIcontent content types. | Joomla components/categories. |
| Form order | Per FLEXIcontent content type. | Joomla field groups. |
| Frontend display | FLEXIcontent template positions. | Joomla component layout overrides. |

## Troubleshooting

| Problem | Likely cause |
| --- | --- |
| Type-specific options are empty | Click **Apply & Reload** after choosing the field type. |
| Duplicate field name | FLEXIcontent appends `-2`; consider choosing a clearer name. |
| Field name changed by the system | The original name was invalid; templates and modules must be updated. |
| Search/filter does not return results | Index is dirty; use **Rebuild Search Index**. |
| Form looks broken after adding markers | Unmatched `custom_form_html` tab/fieldset markers. |
| Cannot delete or unpublish a field | Core field restriction. |
| Access level reset to Public | Saved level was invalid for this field. |

## Official references

- [Starting with FLEXIcontent](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/330-starting-with-flexicontent-basic-usage.html)
- [Fields feature list](https://www.flexicontent.org/features/fields.html)
- [Display fields in the item view](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/261-how-to-displat-fields-in-the-frontend-item-view.html)
- [Display fields in the category view](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/262-how-to-display-fields-in-the-frontend-category-view.html)
- [English tutorials](https://www.flexicontent.org/documentation/tutorials-english.html)
