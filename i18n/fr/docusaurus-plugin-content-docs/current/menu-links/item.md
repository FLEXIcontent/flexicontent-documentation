---
sidebar_position: 9
---

# Vue contenu



:::info Source
Cette page est générée depuis `site/views/item/tmpl/default.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Paramètres requis

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **- Sélectionner une catégorie -**<br />`cid` | Sélectionner la catégorie à afficher | `hidden` | — | `0` |
| **Sélectionner un contenu**<br />`id` | Cliquez sur le titre pour sélectionner un type | `item` | — | `0` |

## Basique

#### Chemin (fil d'ariane)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nb. catégories parentes**<br />`item_depth` | Nb. catégories parentes | `list` | `0` = racine<br />`1` = niveau 1<br />`2` = niveau 2<br />`3` = niveau 3<br />`4` = niveau 4<br />`5` = niveau 5 | `0` (racine) |
| **Ajouter au fil d'ariane**<br />`add_item_pathway` | Ajouter au fil d'ariane. Définir à non en cas de doublon. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
