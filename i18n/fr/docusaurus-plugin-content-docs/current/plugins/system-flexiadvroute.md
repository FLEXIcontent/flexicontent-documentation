---
sidebar_position: 12
---

# Système — Routage avancé

FLEXIcontent fournit des plugins pour la recherche, le routage, les notifications, les boutons de l’éditeur et les sitemaps. Activez-les et configurez-les depuis **Extensions → Plugins**. Les 35 plugins de types de champs sont documentés dans la section [Champs](../fields/index.md).

> Plugin système pour le routage avancé de FLEXIcontent

:::info Source
Cette page est générée depuis `plugins/system/flexiadvroute/flexiadvroute.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

#### Masquer les catégories

:::note
Masquer les catégories du fil d’Ariane / des URL pour les types - il s’agit des types dont le contenu ne fait pas partie de la structure mais contient des informations générales, comme les instructions d’utilisation du site ou un contrat de licence, etc.
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`route_to_type` | — | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Types de contenu**<br />`type_to_route` | — | `types` | — | — |

:::note
Masquer les catégories dans les contenus / listes de contenus en n’affichant pas : a. les liens directs vers les catégories b. le titre de la catégorie comme balisage de contenu / liste - ces catégories ont un usage particulier, par exemple contenir des éléments **affichés** en page d’accueil ou dans un diaporama de module.
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégories**<br />`cats_to_exclude` | choisir les catégories à exclure du routage (ex: la catégorie 'accueil') | `flexicategories` | — | — |
