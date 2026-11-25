---
sidebar_position: 9
---

# Intégration OSMap

FLEXIcontent fournit des plugins pour la recherche, le routage, les notifications, les boutons de l’éditeur et les sitemaps. Activez-les et configurez-les depuis **Extensions → Plugins**. Les 35 plugins de types de champs sont documentés dans la section [Champs](../fields/index.md).

> Plugin OSMap pour le composant FLEXIcontent

:::info Source
Cette page est générée depuis `plugins/osmap/com_flexicontent/com_flexicontent.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| ****Eléments de contenu dans le plan du site ****<br />`myspacer1` | — | `spacer` | — | — |
| **Afficher (vue complète)**<br />`include_items` | Devont nous intégré les éléments de contenu dans le plan sitemap ? **NOTE**: cela affecte toutes les vues « extensibles » de FLEXIcontent | `list` | `0` = Jamais<br />`1` = Toujours<br />`2` = Dans le Sitemap XML seulement<br />`3` = Dans le Sitemap HTML seulement | `1` (Toujours) |
| **Dans la catégorie principale seulement**<br />`include_items_maincatonly` | FLEXIcontent permet plusieurs catégories par contenu, cela peut conduire à vos éléments d'être répertoriés plusieurs fois dans le Sitemap. Vous pouvez éviter cela en affichant chaque élément uniquement à l’intérieur de sa catégorie. | `list` | `0` = Jamais<br />`1` = Toujours<br />`2` = Dans le Sitemap XML seulement<br />`3` = Dans le Sitemap HTML seulement | `0` (Jamais) |
| ****Efficher tous les liens (y compris les éléments de contenu dans plusieurs catégories)****<br />`myspacer2` | — | `spacer` | — | — |
| **Afficher les liens de catégorie**<br />`expand_cats` | Les éléments de menu catégorie (simple/multiple) seront ouverts pour inclure tous les éléments de contenu. Normalement, c'est une option recommandée, sauf si vous avez trop d’éléments ou si vous préférez utiliser une autre façon d’ajouter vos éléments vers le plan sitemap. Par exemple via les vues mots clés ou vues de l’auteur connecté | `list` | `0` = Jamais<br />`1` = Toujours<br />`2` = Dans le Sitemap XML seulement<br />`3` = Dans le Sitemap HTML seulement | `0` (Jamais) |
| **Afficher les liens de catégorie**<br />`expand_authors` | Les éléments de menu auteur seront ouvert pour inclure tous les éléments de contenu appartenant à l’auteur. Si vous l'activez, notez que les éléments de contenu peuvent également être énumérés à l’intérieur de catégories, donc plusieurs fois | `list` | `0` = Jamais<br />`1` = Toujours<br />`2` = Dans le Sitemap XML seulement<br />`3` = Dans le Sitemap HTML seulement | `0` (Jamais) |
| **Afficher les liens par mots clés**<br />`expand_tags` | Les éléments de menu mots clés seront ouvert pour inclure tous les éléments de contenu ayant un mot clés. Si vous l'activez, notez que les éléments de contenu peuvent également être énumérés à l’intérieur de catégories, donc plusieurs fois | `list` | `0` = Jamais<br />`1` = Toujours<br />`2` = Dans le Sitemap XML seulement<br />`3` = Dans le Sitemap HTML seulement | `0` (Jamais) |
| **Limites d'affichage et contenu non autorisé**<br />`myspacer3` | — | `spacer` | — | — |
| **Max. Articles par catégorie**<br />`max_items` | Nombre maximum d’articles par catégorie a affiché sur le plan du site (laissez vide pour aucune limite). Une limitation peut être nécessaire pour le bon affichage de votre page. | `text` | — | — |
| **Max. Âge en jours**<br />`max_age` | Âge maximal des contenus à inclure dans le plan du site (laissez vide pour aucune limite). Fixer cette limite si le vieillissement rend votre contenu moins important, par exemple les sites d'actualités. | `text` | — | — |
| **Afficher les contenus non autorisés**<br />`show_noauth` | OSMAP_FLEXICONTENT_SHOW_UNAUTHORIZED_LINKS_DESC. | `list` | `—` = FC Component Setting<br />`0` = Jamais<br />`1` = Toujours<br />`2` = Dans le Sitemap XML seulement<br />`3` = Dans le Sitemap HTML seulement | — |
| ****Améliorations des éléments de contenu (plus lent)****<br />`myspacer3` | — | `spacer` | — | — |
| **Ajouter des liens de sous-page**<br />`add_pagebreaks` | (plus lent) Éléments de contenu qui sont plusieurs pages auront tous leurs liens ajoutés à la plan sitemap. | `list` | `0` = Jamais<br />`1` = Toujours<br />`2` = Dans le Sitemap XML seulement<br />`3` = Dans le Sitemap HTML seulement | `0` (Jamais) |

## XML

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Priorité des catégories**<br />`cat_priority` | Sélectionnez la priorité des catégories | `list` | `-1` = Utiliser les paramètres du menu parent<br />`0.0` = 0.0<br />`0.1` = 0.1<br />`0.2` = 0.2<br />`0.3` = 0.3<br />`0.4` = 0.4<br />`0.5` = 0.5<br />`0.6` = 0.6<br />`0.7` = 0.7<br />`0.8` = 0.8<br />`0.9` = 0.9<br />`1.0` = 1.0 | `-1` (Utiliser les paramètres du menu parent) |
| **Fréquence de changement des catégories**<br />`cat_changefreq` | Régler la fréquence de changement pour les catégories | `list` | `-1` = Utiliser les réglages du Menu Parent<br />`always` = Toujours<br />`hourly` = Chaque heure<br />`daily` = Quotidien<br />`weekly` = Hebdomadaire<br />`monthly` = Mensuel<br />`yearly` = Annuel<br />`never` = Jamais | `-1` (Utiliser les réglages du Menu Parent) |
| **Priorités des éléments**<br />`item_priority` | Sélectionnez la priorité des contenus | `list` | `-1` = Utiliser les réglages du Menu Parent<br />`0.0` = 0.0<br />`0.1` = 0.1<br />`0.2` = 0.2<br />`0.3` = 0.3<br />`0.4` = 0.4<br />`0.5` = 0.5<br />`0.6` = 0.6<br />`0.7` = 0.7<br />`0.8` = 0.8<br />`0.9` = 0.9<br />`1.0` = 1.0 | `-1` (Utiliser les réglages du Menu Parent) |
| **Fréquence de changement des contenus**<br />`item_changefreq` | Régler la fréquence de changement pour les contenus | `list` | `-1` = Utiliser les réglages du Menu Parent<br />`always` = Toujours<br />`hourly` = Chaque heure<br />`daily` = Quotidien<br />`weekly` = Hebdomadaire<br />`monthly` = Mensuel<br />`yearly` = Annuel<br />`never` = Jamais | `-1` (Utiliser les réglages du Menu Parent) |
