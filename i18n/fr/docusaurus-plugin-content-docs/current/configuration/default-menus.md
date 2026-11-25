---
sidebar_position: 7
---

# Menus par défaut

Éléments de menu par défaut utilisés lorsque le composant crée des liens.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

### Menus par défaut

:::note
- Chaque élément de menu servira de **configuration par défaut** - Les URL SEF utiliseront l’alias de l’élément de menu
:::

:::note
- Créez ces éléments de menu dans le **menu caché FLEXIcontent** - Ne sélectionnez pas d’étiquette, catégorie, auteur, etc. précis
:::

#### Vue Catégorie

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Contenus étiquetés**<br />`cat_tags_default_menu_itemid` | Vue Catégorie | — | — |
| **Contenus de l’auteur**<br />`cat_author_default_menu_itemid` | Vue Catégorie | — | — |

#### Optionnel

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Contenus favoris**<br />`cat_favs_default_menu_itemid` | Vue Catégorie | — | — |
| **Mes contenus**<br />`cat_myitems_default_menu_itemid` | Vue Catégorie | — | — |
| **Multi-catégories**<br />`cat_mcats_default_menu_itemid` | Vue Catégorie | — | — |

#### Anciennes vues

:::note
Si vous utilisez / avez besoin des anciennes vues, par exemple si des moteurs de recherche ou des sites tiers référencent ces vues, créez 2 éléments de menu d’ancienne vue et sélectionnez-les comme valeurs par défaut ci-dessous
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Contenus taggés**<br />`tags_view_default_menu_itemid` | Les liens de tags qui ne proviennent pas de (a) un module de nuage de tags ou (b) un élément de menu de tags ont besoin d'une configuration par défaut. Vous pouvez créer un élément de menu de tags publié avec un niveau d'accès public (et le configurer ici), et dans cet élément de menu configurer les paramètres par défaut de la vue de tags pour ces liens de tags. | — | — |
| **Filtrer les vues tags**<br />`filtertag` | Affiche seulement les contenus de la langue active dans les vues tags. | — | `1` |
| **Articles favoris**<br />`favs_view_default_menu_itemid` | Les liens favoris qui ne proviennent pas de (a) un élément de menu de favoris ont besoin d'une configuration par défaut. Vous pouvez créer un élément de menu de favoris publié avec un niveau d'accès public (et le configurer ici), et dans cet élément de menu configurer les paramètres par défaut de la vue de favoris pour ces liens de favoris. | — | — |

#### Autres vues

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Rechercher**<br />`search_view_default_menu_itemid` | Les liens de recherche qui ne proviennent pas de (a) un module de recherche ou (b) un élément de menu de recherche ont besoin d'une configuration par défaut. Vous pouvez créer un élément de menu de recherche publié avec un niveau d'accès public (et le configurer ici), et dans cet élément de menu configurer les paramètres par défaut de la vue de recherche pour ces liens de recherche. | — | — |
