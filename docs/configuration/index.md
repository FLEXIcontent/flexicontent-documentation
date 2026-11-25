---
sidebar_position: 1
---

# Configuration

FLEXIcontent stores all of its component settings in a single Joomla! configuration screen. Open it from **Components → FLEXIcontent → Options** in the administrator.

The screen is divided into tabs, each dedicated to an area of the component. Every tab has its own documentation page:

| Tab | Purpose | Details |
| --- | --- | --- |
| [Options](./options.md) | General settings: text search, translations, mobile layouts, CSS, browser libraries, cache, debug | 52 options |
| [Redirections / SEO](./redirections-seo.md) | Redirects and search-engine-friendly URLs | 12 options |
| [Buttons](./buttons.md) | Toolbar buttons available in the backend | 14 options |
| [Views](./views.md) | Settings shared by the frontend views | 15 options |
| [Category views](./category-views.md) | Display of category and multi-category lists (filters, sorting, links, etc.) | 181 options |
| [Default menus](./default-menus.md) | Default menu items used by links created by the component | 9 options |
| [Featured](./featured.md) | Settings for featured items | 3 options |
| [Item form](./item-form.md) | Form layout and behaviour when creating/editing an item | 107 options |
| [Workflow](./workflow.md) | States, permissions and publication workflow | 27 options |
| [CSV export](./csv-export.md) | Columns and format of CSV exports | 8 options |
| [Backend Managers](./backend-managers.md) | Layout of the item, field, type, category and file managers | 54 options |
| [Files](./files.md) | Upload directories, allowed extensions, image handling | 53 options |
| [Flexi update](./update.md) | Update notifications | 1 option |
| [Permissions](./permissions.md) | Joomla! ACL rules for the component | standard ACL |

:::note
The option names shown in the documentation (for example `log_search_queries`) are the names stored in the Joomla! configuration table. They are useful when you need to set a value programmatically or to understand a configuration export.
:::

## Where to start

For most sites, only a few settings need to be changed:

1. [Options](./options.md) — check the cache settings (`advcache`) and the translation method (`flexi_fish`).
2. [Category views](./category-views.md) — configure the filters and the information shown in lists.
3. [Workflow](./workflow.md) — adapt the publication states to your editorial process.
4. [Files](./files.md) — check the upload directories and allowed file types.

## Source of the documentation

The configuration pages are generated from the official FLEXIcontent sources:

- `admin/config.xml` — definition of the fields and their default values
- `admin/language/en-GB/en-GB.com_flexicontent.ini` — English labels and descriptions
- the French `fr-FR` translation package from the [FLEXIcontent Crowdin project](https://crowdin.com/project/flexicontent-cck-for-joomla)

The generator is available in `website/tools/generate_config_docs.py`. Re-run it after updating the source files:

```bash
python3 website/tools/generate_config_docs.py
```
