---
sidebar_position: 6
---

# Recherche intelligente

FLEXIcontent fournit des plugins pour la recherche, le routage, les notifications, les boutons de l’éditeur et les sitemaps. Activez-les et configurez-les depuis **Extensions → Plugins**. Les 35 plugins de types de champs sont documentés dans la section [Champs](../fields/index.md).

> Ce plugin indexe les contenus FLEXIcontent

:::info Source
Cette page est générée depuis `plugins/finder/flexicontent/flexicontent.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Indexer les contenus archivés**<br />`search_archived` | Rechercher également les contenus archivés | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Sélectionner les taxonomies (filtres) à créer**<br />`taxonomies` | — | `taxonomytypes` | `author` = Auteur<br />`category` = Catégorie<br />`language` = Langue<br />`type` = Type | `type,category,language,author` |
| **Types à indexer (recherchables)**<br />`types_to_index` | Sélectionner les types FLEXIcontent à indexer par Finder. (Laissez vide pour indexer tous les types). _Laissez vide pour indexer tous les types_ | `sql` | — | — |
