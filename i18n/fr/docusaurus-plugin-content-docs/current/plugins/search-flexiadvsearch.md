---
sidebar_position: 10
---

# Recherche — Avancée

FLEXIcontent fournit des plugins pour la recherche, le routage, les notifications, les boutons de l’éditeur et les sitemaps. Activez-les et configurez-les depuis **Extensions → Plugins**. Les 35 plugins de types de champs sont documentés dans la section [Champs](../fields/index.md).

> Plugin de recherche avancé de FLEXIcontent. En plus du titre et de la description du contenu, il est possible de rechercher dans tous les champs indexables de FLEXIcontent comme like les tags, les champs de texte, les champs images (ex:leur description), etc... **Remarque : Vous devez désactiver tous les autres plugins de recherche concernant les Articles**.

:::info Source
Cette page est générée depuis `plugins/search/flexiadvsearch/flexiadvsearch.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Limite de la recherche**<br />`search_limit` | Nombre maximum de résultat de recherche à afficher. | `text` | — | `50` |
| **Filtrer la langue**<br />`filter_lang` | Afficher les résultats uniquement de la langue active | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Rechercher les contenus archivés**<br />`search_archived` | Inclure également les contenus archivés dans la recherche | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Navigation du navigateur**<br />`browsernav` | Navigation dans le navigateur | `radio` | `1` = Ouvrir dans une nouvelle fenêtre<br />`2` = Ouvrir dans la même fenêtre | `2` (Ouvrir dans la même fenêtre) |
