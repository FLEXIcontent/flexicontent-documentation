---
sidebar_position: 2
---

# Fields

**Fields** structure the data of an item. Each field is a Joomla! plugin, which makes it possible to extend FLEXIcontent with new field types.

## General features

- A field can be assigned to **one or several content types**.
- All fields can hold **multiple values**, reordered by drag and drop.
- Values can be **filterable** and **searchable** in list views.
- Fields respect **access rights** and keep a value history.
- Output can be customised: prefix, suffix, separator, formatting, field template, Joomla! content plugins.

## Field families

FLEXIcontent provides several dozen fields. The main families are:

### Text

- Single line text, textarea, HTML editor.
- Email, phone, URL, number, custom code.

### Selection

- Dropdown (`select`), multiple select.
- Radio buttons, checkboxes, image variants.
- Lists fed by static values or SQL queries.

### Date and time

- Date input, date range, configurable display formats.
- Usable as a filter in list views.

### Media and files

- Image and image gallery, with thumbnails and built-in layouts.
- File, audio, video.
- Address / map with geolocation.

### Relations

- **Relation** field pointing to other items.
- **Reverse relation** field showing items that point to the current one.

### Structure and display

- Field groups and tabs in the input form.
- Presentation fields: social share, item navigation, author list, module loading.

:::tip
Before creating a new field, check whether an existing field combined with a custom layout is enough.
:::

For the full procedure, see [Create a field](../fields/create-a-field.md).

## Configuring a field

The most common settings are:

- the **label** shown in the form;
- the **field type**;
- **input options** (allowed values, size, format);
- **visibility** depending on content type and permissions;
- the **display** in item, category and module views;
- the field's role in **search and filters**.

## Official resources

- [Field list](https://www.flexicontent.org/features/fields.html)
- [Tutorials about using fields](https://www.flexicontent.org/documentation/tutorials-english.html?filter=field&cc=88603e3010eb311c02874f047982cf36)
