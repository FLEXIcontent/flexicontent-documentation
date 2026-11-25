---
sidebar_position: 13
---

# Contenus étiquetés (ancienne vue)



:::info Source
Cette page est générée depuis `site/views/tags/tmpl/default.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Paramètres requis

:::note
Pour créer un élément de menu de configuration **d’affichage par défaut** (pour toutes les étiquettes sans élément de menu) : 1. Ne sélectionnez aucune étiquette ici 2. Définissez un titre/alias générique, par exemple « tagged_items » (l’alias apparaîtra dans les URL) et configurez les paramètres de l’élément 3. Ouvrez les paramètres du composant, l’onglet **Listes**, et sélectionnez cet élément comme élément par défaut de l’ancienne vue « Contenus étiquetés »
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **- Sélectionner un tag -**<br />`id` | Cliquez sur le nom du tag dans le Popup pour le sélectionner | `fctag` | — | `0` |

## Basique

### Référencement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Tag canonique**<br />`add_canonical` | Ajouter une balise meta canonique dans le code source de vos pages, cela aide les moteurs de recherche à identifier une page visualisée via des URL différentes et lui donner meilleur rang, en ne l'indexant pas plusieurs fois | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

### Champs

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Montrer**<br />`use_image` | — | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Source de l'image**<br />`image_source` | Sélectionner la source de l'image. Vous pouvez aussi choisir un champ image (s'il y en a au moins un de disponible) ou automatiquement extraire l'image de la description. | `fcimage` | — | — |
| **Lien sur l'image**<br />`link_image` | Actif un lien sur l'image affichée. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Taille de l'image**<br />`image_size` | Taille de l'image pour l'introduction | `list` | `—` = Utiliser les paramètres<br />`s` = Petite<br />`m` = Moyenne<br />`l` = Grande | — |
| **Largeur de l'image**<br />`image_width` | Largeur de l'image | `text` | — | `90` |
| **Hauteur de l'image**<br />`image_height` | Hauteur de l'image | `text` | — | `90` |
| **Méthode de traitement**<br />`image_method` | Méthode de traitement | `radio` | `0` = A l'échelle<br />`1` = Découper | `0` (A l'échelle) |

#### Date de modification

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Montrer**<br />`show_modify_date` | — | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Format de la date**<br />`date_format` | Choisissez le format de la date en utilisant les constantes de Joomla! (utile pour les sites multilingues) | `multilist` | `DATE_FORMAT_LC1` = Date format lc1<br />`DATE_FORMAT_LC2` = Date format lc2<br />`DATE_FORMAT_LC3` = Date format lc3<br />`DATE_FORMAT_LC4` = Date format lc4<br />`DATE_FORMAT_CUSTOM` = Format personnalisé | `DATE_FORMAT_LC1` (Date format lc1) |
| **Format personnalisé**<br />`custom_date` | Si vous choisissez 'format personnalisé' dans la liste ci-dessus vous devez spécifier dans ce champ le format que vous souhaitez afficher en utilisant la syntaxe PHP strftime (http://php.net/strftime). | `text` | — | — |

#### Champs Personnalisés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Montrer**<br />`use_fields` | — | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Liste des champs**<br />`fields` | Saisir les noms des champs séparés par des virgules | `textarea` | — | — |

### Pagination

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre de contenus par page**<br />`limit` | Indique le nombre de contenu à afficher sur chaque page de liste. | `text` | — | `10` |
| **nb. par page**<br />`show_pagination` | Afficher/Masquer la pagination, tels que les liens et la page de total | `radio` | `0` = Cacher<br />`1` = Montrer<br />`2` = Auto | `2` (Auto) |
| **Résultat de la pagination (Nombre courant et total des pages)**<br />`show_pagination_results` | (lorsque la pagination est activée), vous pouvez utiliser cette option pour désactiver l'affichage du numéro de page active courante et le nombre total de pages | `radio` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |

### Ordre des contenus

#### Ordre du contenu (niveau 1)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby` | Trier les éléments par des champs/propriétés du noyau | `list` | `—` = Paramètres globaux<br />`date` = Les plus anciens<br />`rdate` = Plus récents en premier<br />`modified` = Derniers modifiés en premier<br />`published` = Publié - Le plus récent en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés en premier<br />`rhits` = Les moins consultés en premier<br />`id` = ID -- Plus grand en premier<br />`rid` = ID -- Plus petit en premier<br />`commented` = Les plus commentés<br />`rated` = Les mieux notés<br />`order` = Classer dans la catégorie actuelle<br />`jorder` = Ordre (Global) | — |

#### Classement personnalisé des champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`orderbycustomfield` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Champ personnalisé**<br />`orderbycustomfieldid` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | `fields` | — | — |
| **Sens du tri**<br />`orderbycustomfielddir` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `radio` | `—` = Paramètres globaux<br />`ASC` = Croissant<br />`DESC` = Décroissant | — |
| **Méthode de tri**<br />`orderbycustomfieldint` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `radio` | `—` = Paramètres globaux<br />`0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date | — |

#### Ordre du contenu (niveau 2)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby_2nd` | Trier les éléments par des champs/propriétés du noyau | `list` | `—` = Paramètres globaux<br />`date` = Les plus anciens<br />`rdate` = Plus récents en premier<br />`modified` = Derniers modifiés en premier<br />`published` = Publié - Le plus récent en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés en premier<br />`rhits` = Les moins consultés en premier<br />`id` = ID -- Plus grand en premier<br />`rid` = ID -- Plus petit en premier<br />`commented` = Les plus commentés<br />`rated` = Les mieux notés<br />`order` = Classer dans la catégorie actuelle<br />`jorder` = Ordre (Global) | — |

#### Classement personnalisé des champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`orderbycustomfield_2nd` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Champ personnalisé**<br />`orderbycustomfieldid_2nd` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | `fields` | — | — |
| **Sens du tri**<br />`orderbycustomfielddir_2nd` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `radio` | `—` = Paramètres globaux<br />`ASC` = Croissant<br />`DESC` = Décroissant | — |
| **Méthode de tri**<br />`orderbycustomfieldint_2nd` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `radio` | `—` = Paramètres globaux<br />`0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date | — |

### Overide du Frontend

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre de contenus par page**<br />`limit_override` | Indique le nombre de contenu à afficher sur chaque page de liste. | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Sélecteur d'ordre (Niveau 1)**<br />`orderby_override` | Activer pour afficher une liste déroulante pour changer l'ordre dans la partie publique (Niveau 1) | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Sélecteur d'ordre (Niveau 2)**<br />`orderby_override_2nd` | Activer pour afficher une liste déroulante pour changer l'ordre dans la partie publique (Niveau 2) | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |

#### Sélectionner les options disponibles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nb par page autorisé à l'utilisateur en frontend**<br />`limit_options` | Saisissez les valeurs séparées par des virgules qui indiquent les options disponibles, laisser vide pour utiliser les options par défaut. | `text` | — | — |
| **Options de tri (Niveau 1) autorisé pour l'utilisateur frontend**<br />`orderby_options` | Sélectionner les options que vous souhaitez faire apparaitre à l'utilisateur en frontend afin qu'il puisse réordonner sa liste de contenu. **Remarque :** (a) **L'ordre par défaut**, est définit dans la section 'vue catégorie -&gt; ordre des contenus', (b)** l'ordre des contenus** ne fonctionne que pour la catégorie active et donc ne fonctionne pas si des sous catégories sont incluses dans la liste. | `fccheckbox` | — | — |
| **Ordre personnalisé (Niveau 1) autorisé pour les utilisateur en**<br />`orderby_custom` | Description des options de tri personnalisées | `textarea` | — | — |
| **Options de tri (Niveau 2) autorisé pour l'utilisateur frontend**<br />`orderby_options_2nd` | Sélectionner les options que vous souhaitez faire apparaitre à l'utilisateur en frontend afin qu'il puisse réordonner sa liste de contenu. **Remarque :** (a) **L'ordre par défaut**, est définit dans la section 'vue catégorie -&gt; ordre des contenus', (b)** l'ordre des contenus** ne fonctionne que pour la catégorie active et donc ne fonctionne pas si des sous catégories sont incluses dans la liste. | `fccheckbox` | — | — |
| **Ordre personnalisé (Niveau 2) autorisé pour les utilisateur en**<br />`orderby_custom_2nd` | Description des options de tri personnalisées | `textarea` | — | — |

## Paramètres

#### Texte à Rechercher

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser la recherche**<br />`use_search` | Afficher la zone de recherche textuel | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Afficher les étiquettes**<br />`show_search_label` | Vous pouvez cacher ou afficher le libellé à l'intérieur de la zone de recherche de texte pour économiser de l'espace | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Bouton rechercher**<br />`show_search_go` | Envoyer le formulaire pour recharger la liste actuelle, ** Remarque **: tous les critères suivant seront pris en compte, la recherche de texte, les filtres dans les champs et l'indice alpha (lorsque ces valeurs sont présentes) | `radio` | `—` = Paramètres globaux<br />`0` = Auto<br />`1` = Montrer | — |
| **Bouton annuler**<br />`show_search_reset` | Effacer le formulaire pour recharger la liste actuelle, ** Remarque **: Notez que cela va aussi supprimer les valeurs saisies dans les filtres et de l'indice alpha (lorsque ces produits sont présents) | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
