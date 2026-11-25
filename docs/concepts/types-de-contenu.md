---
sidebar_position: 1
---

# Content types

The **content type** is the central concept of FLEXIcontent. It is a preconfigured input form for a family of content.

## Definition

A type groups:

- the **fields** available in the input form;
- **form options**: required fields, default values, validation;
- the **display templates** used for the item and the list;
- the allowed **categories**;
- **ACL rules** defining who can create, edit and publish;
- **search**, **filtering** and **SEO** settings.

The `Article` type is configured by default. Every other type — blog, event, directory, product, portfolio, documentation, etc. — is yours to create.

## Best practices

- Give the type a short, explicit name: editors will see it.
- Avoid multiplying types for differences that could be handled by a select field.
- Use **shared fields** to avoid recreating the same data in several types.
- Think about **access rights** when creating the type, especially if content is submitted from the frontend.

## Examples

| Type | Typical fields |
| --- | --- |
| Event | Start date, end date, venue, price, image |
| Product sheet | SKU, price, stock, gallery, specifications |
| Directory | Address, phone, email, map, business category |
| Documentation | Table of contents, version, attached file, tags |

## Go further

- [Create a content type](../content-types/create-a-content-type.md)
- [Fields](./champs.md)
- [Templates](./modeles.md)
- [Getting started](../demarrage/premiers-pas.md)
