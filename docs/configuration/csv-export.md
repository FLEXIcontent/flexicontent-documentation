---
sidebar_position: 11
---

# CSV export

Columns and format used when exporting items to CSV.

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

### Frontend

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **CSV export**<br />`show_csvbutton` | Enable CSV Export functionality | — | `0` |

### Backend

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **CSV export**<br />`show_csvbutton_be` | Enable CSV Export functionality | — | `0` |

### Options

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Column Headers**<br />`csv_export_header` | — | — | `1` |

### CSV file format

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Field (Column) separator**<br />`csv_export_field_sep` | — | — | `,` |
| **Item Separator**<br />`csv_export_item_record_sep` | Multiple characters recommended e.g : \n~~ for new line enter: \n | — | `\n` |
| **Exported fields**<br />`__exported_fields` | — | — | `0` |

#### Multi-value / multi-property fields

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Multivalue separator**<br />`csv_export_field_multivalue_sep` | By defaut %% | — | `%%` |
| **Multi-property separator**<br />`csv_export_field_mprop_sep` | Fields that have multiple properties per value | — | `!!` |
