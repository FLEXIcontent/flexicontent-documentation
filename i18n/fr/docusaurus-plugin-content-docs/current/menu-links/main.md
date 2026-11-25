---
sidebar_position: 8
---

# Annuaire (vue principale)



:::info Source
Cette page est générée depuis `site/views/flexicontent/tmpl/default.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Paramètres requis

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégorie racine**<br />`rootcat` | Veuillez sélectionner la catégorie racine pour ce répertoire | `fccategory` | — | `1` |

## Basique

#### Chemin (fil d'ariane)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nb. catégories parentes**<br />`item_depth` | Vous pouvez régler la profondeur de l'arbre catégorie, à laquelle ajouter des liens catégorie des parents à la voie doit commencer. **Remarque :** Dans le plugin système FLEXIcontent Advanced Route, vous pouvez désactiver l’ajout des catégories au fil d’Ariane pour certains types de contenu | `list` | `0` = racine<br />`1` = niveau 1<br />`2` = niveau 2<br />`3` = niveau 3<br />`4` = niveau 4<br />`5` = niveau 5 | `0` (racine) |

#### Paramètres de base

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Texte d'introduction**<br />`introtext` | Afficher le texte d'introduction sous la catégorie | `textarea` | — | — |
| **Afficher le texte d'introduction**<br />`showintrotext` | Choisir d'afficher le texte d’introduction ou non | `radio` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |
| **Compteur de contenu**<br />`showassignated` | Afficher/cacher le nombre de contenu de chaque sous-catégorie | `radio` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |
| **Nombre de catégories affichées**<br />`catlimit` | Indique le nombre maximum de catégories à afficher dans la liste. | `text` | — | `200` |

### Configuration des catégories

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ordre de la liste de catégorie**<br />`cat_orderby` | Ordre la liste des catégories, les options disponibles dépendent des propriétés de l'ensemble des catégories. | `list` | `—` = Paramètres globaux<br />`date` = Les plus anciens<br />`rdate` = Plus récents en premier<br />`modified` = Derniers modifiés en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés en premier<br />`rhits` = Les moins consultés en premier<br />`order` = Attribut d'ordre des catégories | `order` (Attribut d'ordre des catégories) |
| **Masquer les catégories vides**<br />`hide_empty_cats` | Sont considérées comme vides les catégories : 1. Qui n'ont aucun contenu d'assigné directement 2. Dont les sous-catégories n'ont pas de contenu assigné, et aucune sous-catégorie. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Description**<br />`show_cat_descr` | Afficher/Masquer la description, vous pouvez aussi définir le nombre de caractères à afficher | `radio` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |
| **Longueur de la description**<br />`cat_descr_cut` | Longueur du texte de description , la description sera tronquée après le nombre de caractère défini | `text` | — | `100` |
| **Titre cliquable**<br />`cat_link_title` | Lien sur le titre dans la vue actuelle | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Image**<br />`show_cat_image` | Afficher/Masquer l'image, vous pouvez aussi sélectionner la source de l'image | `radio` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |
| **Source de l'image de la catégorie**<br />`cat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | `list` | `0` = Extraire de la description<br />`1` = Utiliser l'image des paramètres<br />`2` = Essayer les paramètres, puis extraire de la description | `2` (Essayer les paramètres, puis extraire de la description) |
| **Lien sur l'image**<br />`cat_link_image` | Actif un lien sur l'image affichée. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Méthode de traitement**<br />`cat_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |
| **Largeur de l'image**<br />`cat_image_width` | Largeur de l'image | `text` | — | `80` |
| **Hauteur de l'image**<br />`cat_image_height` | Hauteur de l'image | `text` | — | `80` |

### Configuration des sous-catégories

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ordre des sous catégories**<br />`subcat_orderby` | Ordre dans lequel les contenus seront affichés | `list` | `—` = Ordre par défaut<br />`date` = Les plus anciens<br />`rdate` = Plus récents en premier<br />`modified` = Derniers modifiés en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés en premier<br />`rhits` = Les moins consultés en premier<br />`order` = Classer dans la catégorie actuelle | `order` (Classer dans la catégorie actuelle) |
| **Masquer les sous-catégories vides**<br />`hide_empty_subcats` | Une sous catégorie est considérée comme vide lorsqu'elle n'a aucun contenu rattaché, et n'ont pas de sous catégories. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Description**<br />`show_subcat_descr` | Afficher/Masquer la description, vous pouvez aussi définir le nombre de caractères à afficher | `radio` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |
| **Longueur de la description**<br />`subcat_descr_cut` | Longueur du texte de description , la description sera tronquée après le nombre de caractère défini | `text` | — | `50` |
| **Image**<br />`show_subcat_image` | Afficher/Masquer l'image, vous pouvez aussi sélectionner la source de l'image | `radio` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |
| **Source de l'image de la catégorie**<br />`subcat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | `list` | `0` = Extraire de la description<br />`1` = Utiliser l'image des paramètres<br />`2` = Essayer les paramètres, puis extraire de la description | `2` (Essayer les paramètres, puis extraire de la description) |
| **Lien sur l'image**<br />`subcat_link_image` | Actif un lien sur l'image affichée. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Méthode de traitement**<br />`subcat_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |
| **Largeur de l'image**<br />`subcat_image_width` | Largeur de l'image | `text` | — | `40` |
| **Hauteur de l'image**<br />`subcat_image_height` | Hauteur de l'image | `text` | — | `40` |

### Configuration de l'affichage

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nb. colonnes**<br />`columns_count` | Choisir le nombre de colonnes pour ce répertoire | `list` | `1` = 1 colonne<br />`2` = 2 colonnes<br />`3` = 3 colonnes<br />`4` = 4 colonnes | `1` (1 colonne) |
| **Nb. blocs col1**<br />`column1` | Choisir le nombre de blocs que vous souhaitez afficher dans la première colonne. Remarque : 1 bloc représente la catégorie principale et ses sous catégories. | `text` | — | `0` |
| **Nb. blocs col2**<br />`column2` | Choisir le nombre de blocs que vous souhaitez afficher dans la seconde colonne. Remarque : 1 bloc représente la catégorie principale et ses sous catégories. | `text` | — | `0` |
| **Nb. blocs col3**<br />`column3` | Choisir le nombre de blocs que vous souhaitez afficher dans la troisième colonne. Remarque : 1 bloc représente la catégorie principale et ses sous catégories. | `text` | — | `0` |
