---
sidebar_position: 3
---

# Categories

FLEXIcontent uses Joomla!'s native categories, but adds two important features: unlimited nesting and multi-category assignment.

## Unlimited nesting

Unlike native Joomla! category management, FLEXIcontent categories can be nested with no practical depth limit. You can build a tree such as:

```text
Documentation
├── User guide
│   ├── Installation
│   └── Entering content
└── Developer guide
    ├── API
    └── Custom fields
```

## Primary category and secondary categories

An item can be assigned to several categories:

- the **primary category** is used in particular for permission inheritance and default routing;
- **secondary categories** add other classifications (topic, region, year, etc.).

In the administrator, the primary category is shown in blue in the items table.

:::tip
Choose the primary category based on the most common reading context. The other assignments are mainly useful for filtering and secondary views.
:::

## Avoiding duplicate content

When an item appears in several categories, FLEXIcontent can generate a canonical link so search engines do not treat these pages as duplicates.

## List views

Category and multi-category views display items with:

- sorting and pagination;
- filters on fields;
- subcategories;
- template options specific to the view.

See [Templates](./modeles.md) to customise these views.

## Go further

- [Create a category](../categories/create-a-category.md)
- [Category options](../categories/options.md)
