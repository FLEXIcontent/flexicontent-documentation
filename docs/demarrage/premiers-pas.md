---
sidebar_position: 2
---

# Getting started

This walkthrough sets up a first content structure with FLEXIcontent.

## 1. Choose or create a content type

A **content type** defines the structure of a family of content. FLEXIcontent provides the `Article` type by default, but you can create types such as `Event`, `Product sheet` or `Whitepaper`.

In the administrator: **Components → FLEXIcontent → Content types**. See [Create a content type](../content-types/create-a-content-type.md) for the detailed procedure.

:::tip
Start with a single type. You can duplicate it or create other types later.
:::

## 2. Add fields

Next, assign the fields needed by the type: a title, text, date, image, select list, etc.

A field can be used by several content types. You can define whether it is required, its default value, its display order and its permissions.

See [Fields](../concepts/champs.md) for concepts and [Create a field](../fields/create-a-field.md) for the step-by-step procedure.

## 3. Create categories

Create a category tree under **Categories**. FLEXIcontent categories can be nested and an item can belong to several categories.

See [Create a category](../categories/create-a-category.md) for the procedure and [Categories](../concepts/categories.md) for the concepts.

## 4. Create your first item

Under **Items**, create an item of the chosen type, assign it to a category and fill in the fields defined in step 2.

At this point the item exists in the administrator. It still needs to be made visible on the site.

## 5. Create the display menu item

Create a menu item pointing to a **category view** or a **multi-category view** FLEXIcontent view. Choose the category to display, the content type and the template to use.

You now get a list page with the sorting and filters enabled according to your field configuration.

## 6. Refine the display

FLEXIcontent lets you customise:

- the **category view template** (list, grid, table…);
- the **item view template** (detail page);
- the rendering of each field (prefix, suffix, formatting, content plugin);
- the **modules** used to display content elsewhere on the site.

See [Templates](../concepts/modeles.md).

## Next step

Once these basics are in place, explore the [resources](../ressources.md) to go deeper into configuration, workflow and FLEXIcontent APIs.
