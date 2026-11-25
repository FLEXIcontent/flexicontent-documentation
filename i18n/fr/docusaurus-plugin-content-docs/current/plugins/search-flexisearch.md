---
sidebar_position: 11
---

# Recherche — Standard

FLEXIcontent fournit des plugins pour la recherche, le routage, les notifications, les boutons de l’éditeur et les sitemaps. Activez-les et configurez-les depuis **Extensions → Plugins**. Les 35 plugins de types de champs sont documentés dans la section [Champs](../fields/index.md).

> Le plugin de recherche standard de FLEXIcontent peut rechercher des données Flexicontent : Titre, description, tags, texte **NOTE : Vous devez désactiver tous les autres plugins Article Contenu de recherche de JOOMLA (contenu, pas les plugins pour tout autre type de contenu de site) .

:::info Source
Cette page est générée depuis `plugins/search/flexisearch/flexisearch.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Filtrer la langue**<br />`filter_lang` | Afficher les résultats uniquement de la langue active | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Limite de la recherche**<br />`search_limit` | Nombre maximum de résultat de recherche à afficher. | `text` | — | `50` |
| **Titre**<br />`search_title` | Rechercher dans le titre de l'élément | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Texte d'introduction et texte principal**<br />`search_desc` | Rechercher dans le texte d'introduction et le texte principal de l'élément | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Champs textes**<br />`search_fields` | Rechercher dans les champs de l'index basique de FLEXIcontent | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Métadonnées**<br />`search_meta` | Rechercher dans les métadonnées description et les mots-clés de l'élément | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Mots-clés**<br />`search_tags` | Rechercher dans les mots-clés de l'élément | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Sélecteur du type**<br />`search_select_types` | Laisser l'utilisateur avoir la possibilité de sélectionner un type FLEXIcontent. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Contrôle de date de la recherche standard**<br />`search_result_date_control` | Stdsearch date control description | `radio` | `created` = Par date de création<br />`modified` = Par date de modification | `created` (Par date de création) |
| **ID des types disponibles pour la recherche**<br />`search_types` | Saisir les ID des types en les séparant par une virgule, ou laisser vide pour avoir la possibilité de chercher dans tous les types publiés. | `text` | — | — |
