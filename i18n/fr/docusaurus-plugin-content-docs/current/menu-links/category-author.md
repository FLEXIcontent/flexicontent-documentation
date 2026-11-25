---
sidebar_position: 3
---

# Contenus d’un auteur

Seules les options propres à cette vue sont listées ci-dessous. Toutes les autres options sont décrites dans [Vues catégorie — options communes](./category-common.md).

:::info Source
Cette page est générée depuis `site/views/category/tmpl/author.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Paramètres requis

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Disposition**<br />`layout` | — | `hidden` | — | `author` |

:::note
Pour créer un élément de menu de configuration **d’affichage par défaut** (pour tous les auteurs sans élément de menu) : 1. Ne sélectionnez aucun auteur ici 2. Définissez un titre/alias générique, par exemple « authored » (l’alias apparaîtra dans les URL) et configurez les paramètres de l’élément 3. Ouvrez les paramètres du composant, l’onglet **Listes**, et sélectionnez cet élément comme élément par défaut de la vue catégorie « Contenus étiquetés »
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Sélectionner un auteur**<br />`authorid` | Sélectionner l'auteur que vous souhaitez afficher | `fcauthor` | `—` = Cliquez pour sélectionner | `0` |
| **Catégories à inclure pour l’auteur**<br />`cids` | Description des catégories à inclure pour l’auteur | `flexicategories` | — | — |
| **Catégories à exclure pour l’auteur**<br />`excl_cids` | Description des catégories à exclure pour l’auteur | `flexicategories` | — | — |

## Surcharger les paramètres d'affichage

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Limite totale pour l’auteur**<br />`author_limit_total` | Auteur limit total description | `text` | — | `0` |
| **Limite par catégorie pour l’auteur**<br />`author_limit_per_cat` | Auteur limit per cat description | `text` | — | `0` |
