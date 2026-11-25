---
sidebar_position: 11
---

# Export CSV

Colonnes et format utilisés lors de l’export des contenus au format CSV.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

### Chargement automatique dans la partie publique

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Export CSV**<br />`show_csvbutton` | Activer l'export CSV | — | `0` |

### Administration

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Export CSV**<br />`show_csvbutton_be` | Activer l'export CSV | — | `0` |

### Options

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **En-têtes de colonnes**<br />`csv_export_header` | — | — | `1` |

### Format du fichier CSV

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Séparateur de champs (colonnes)**<br />`csv_export_field_sep` | — | — | `,` |
| **Séparateur de contenu**<br />`csv_export_item_record_sep` | Caractères multiples recommandés ex : \n~~ for un saut de ligne, indiquez: \n | — | `\n` |
| **Champs exportés**<br />`__exported_fields` | — | — | `0` |

#### Champs multi-valeurs

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Séparateur des valeurs multiples**<br />`csv_export_field_multivalue_sep` | Par défaut %% | — | `%%` |
| **Séparateurs Multi-proriété**<br />`csv_export_field_mprop_sep` | Champs multi propriétés par valeur | — | `!!` |
