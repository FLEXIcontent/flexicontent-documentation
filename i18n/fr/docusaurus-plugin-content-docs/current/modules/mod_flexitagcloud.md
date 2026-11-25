---
sidebar_position: 8
---

# Nuage d’étiquettes

FLEXIcontent fournit six modules frontend pour afficher des contenus, des catégories, des formulaires de recherche, des filtres, des cartes et des nuages d’étiquettes. Configurez un module depuis **Extensions → Modules**.

> Module de nuage de mots clés pour FLEXIcontent

:::info Source
Cette page est générée depuis `modules/mod_flexitagcloud/mod_flexitagcloud.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

### Template du module

:::note
Veuillez définir les paramètres de disposition dans l’onglet **Disposition : ...**. Les développeurs CSS/HTML doivent consulter : ** Guide des modèles personnalisés **
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Template**<br />`layout` | Choisir la mise en page de votre module | `fclayout` | — | `default` |

### Paramètres de base

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Taille mini du texte**<br />`min_size` | Définit la taille minimum du texte pour l'affichage d'un tag . Ne changez pas ces valeurs si vous ne savez pas configurer votre fichier CSS comme il le faut. | `text` | — | `1` |
| **Taille maxi du texte**<br />`max_size` | Définit la taille maximum du texte pour l'affichage d'un tag . Ne changez pas ces valeurs si vous ne savez pas configurer votre fichier CSS comme il le faut. | `text` | — | `10` |
| **Nombre maximum de tags**<br />`count` | Nombre de maxium de tags à afficher dans le nuage. | `text` | — | `25` |
| **Mode SEO**<br />`seo_mode` | Ne pas utiliser les options d'accessibilité afin éviter l'indexation de Google des informations destinées uniquement à l'écran pour les utilisateurs. | `radio` | `1` = Oui<br />`0` = Non | `1` (Oui) |
| **Forcer Itemid**<br />`force_itemid` | Forcer la redirection des liens vers un ItemID spécifique. | `text` | — | — |

#### Catégories

:::note
Afficher les étiquettes des contenus des catégories suivantes. **Catégorie actuelle** désigne - la catégorie en cours de visualisation - ou la catégorie principale du contenu affiché
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégorie**<br />`method` | Vous pouvez définir ici si vous souhaitez inclure ou exclure des catégories. Seuls les tags des contenus associés à ces catégories seront donc afficher ou masquer. | `multilist` | `0` = Tous<br />`1` = active<br />`2` = Exclure<br />`3` = Inclure | `1` (active) |
| **Catégories**<br />`categories` | Veuillez sélectionner les catégories à inclure ou à exclure en fonction du paramètre ci-dessus. | `flexicategories` | — | — |
| **Catégories supplémentaires**<br />`treeinclude` | — | `list` | `0` = Aucun<br />`1` = Catégories enfants | `0` (Aucun) |

#### Type de contenu

:::note
Limite l'**affichage des mots clés** et leurs **liens** pour visualiser les contenus, - aux contenus ayant le même type
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Limiter au type en cours**<br />`method_types` | Veuillez vous assurer que le champ Mots clés est configuré pour être filtrables et que la vue Mots clés n’est pas défini sur le mode hérité (il suffit de cocher cette case si vous avez modifié le paramètre par défaut dans la configuration de flexicontent) | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |

## Masquer/afficher le module

Ces règles déterminent à quel moment le module sera affichée (donc montré) ou non (donc caché).

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Combinaison des règles**<br />`combine_show_rules` | En fonction des VUES ET/OU des règles d'expression PHP, afin de déterminer si le si le module doit s'afficher ou non. | `radio` | `OR` = OU<br />`AND` = ET | `AND` (ET) |

#### Clients

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher pour les clients**<br />`show_in_clients` | Sélectionner pour afficher sur les ordinateurs de bureau, tablettes, mobiles | `fccheckbox` | — | — |

#### Règles des vues (catégorie, article, etc.)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher dans les vues**<br />`show_in_views` | Sélectionner les vues dans lesquelles vous souhaitez afficher ce module. | `fccheckbox` | — | — |

#### Règles PHP

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer la règle**<br />`enable_php_rule` | Vous pouvez désactiver cette règle sans supprimer les règles saisies ci-dessous. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Code régle PHP**<br />`php_rule` | Ce code PHP sera exécuté à la fin. Il doit retourner un booléen par le biais d'un 'return'. Cela determinera si le module doit être affiché ou non. | `textarea` | — | — |

## Mise en page : Options de la mise en page selectionnée

Options de disposition spécifiques à la mise en page du modèle choisi

## Liste de contenu par mots clés (hérité)

:::note
Note que ces options sont destinées à la vue hérité des mots clés. Pour affichage des mots clés basé sur des vues catégories, veuillez le configurer dans flexicontent/ catégorie / paramètres des éléments de menu
:::

#### Paramètres de l’ancienne vue des étiquettes

### Champs

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher**<br />`use_image` | — | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Source de l'image**<br />`image_source` | Sélectionner la source de l'image. Vous pouvez aussi choisir un champ image (s'il y en a au moins un de disponible) ou automatiquement extraire l'image de la description. | `fcimage` | — | — |
| **Lien sur l'image**<br />`link_image` | Actif un lien sur l'image affichée. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Taille de l'image**<br />`image_size` | Taille de l'image pour l'introduction | `multilist` | `—` = Utiliser les paramètres<br />`s` = Petite<br />`m` = Moyenne<br />`l` = Grande | — |
| **Largeur de l'image**<br />`image_width` | Largeur de l'image | `text` | — | `90` |
| **Hauteur de l'image**<br />`image_height` | Hauteur de l'image | `text` | — | `90` |
| **Méthode de traitement**<br />`image_method` | Méthode de traitement | `radio` | `0` = A l'échelle<br />`1` = Découper | `0` (A l'échelle) |

#### Date de modification

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher**<br />`show_modify_date` | — | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Format de la date**<br />`date_format` | Choisissez le format de la date en utilisant les constantes de Joomla! (utile pour les sites multilingues) | `multilist` | `DATE_FORMAT_LC1` = Date format lc1<br />`DATE_FORMAT_LC2` = Date format lc2<br />`DATE_FORMAT_LC3` = Date format lc3<br />`DATE_FORMAT_LC4` = Date format lc4<br />`DATE_FORMAT_CUSTOM` = Format personnalisé | `DATE_FORMAT_LC1` (Date format lc1) |
| **Format personnalisé**<br />`custom_date` | Si vous choisissez 'format personnalisé' dans la liste ci-dessus vous devez spécifier dans ce champ le format que vous souhaitez afficher en utilisant la syntaxe PHP strftime (http://php.net/strftime). | `text` | — | — |

#### Champs Personnalisés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher**<br />`use_fields` | — | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Liste des champs**<br />`fields` | Saisir les noms des champs séparés par des virgules | `textarea` | — | — |

### Pagination (lien de page & total)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre de contenus par page**<br />`limit` | Indique le nombre de contenu à afficher sur chaque page de liste. | `text` | — | `10` |
| **Pagination (lien de page & total)**<br />`show_pagination` | Afficher/Masquer la pagination, tels que les liens et la page de total | `radio` | `0` = Cacher<br />`1` = Afficher<br />`2` = Auto | `2` (Auto) |
| **Résultat de la pagination (Nombre courant et total des pages)**<br />`show_pagination_results` | (lorsque la pagination est activée), vous pouvez utiliser cette option pour désactiver l'affichage du numéro de page active courante et le nombre total de pages | `radio` | `0` = Cacher<br />`1` = Afficher | `1` (Afficher) |

### Référencement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Tag canonique**<br />`add_canonical` | Ajouter une balise meta canonique dans le code source de vos pages, cela aide les moteurs de recherche à identifier une page visualisée via des URL différentes et lui donner meilleur rang, en ne l'indexant pas plusieurs fois | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

### Ordre des contenus

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ordre primaire**<br />`orderby` | Définit l'ordre dans lequel les contenus seront affichés dans la liste. | `list` | `—` = Défaut<br />`date` = Les plus anciens<br />`rdate` = Plus récents en premier<br />`modified` = Derniers modifiés en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés<br />`rhits` = Les moins consultés<br />`order` = Classer dans la catégorie actuelle | — |
| **Champ personnalisé**<br />`orderbycustomfieldid` | Sélectionné le champ personnalisé à utiliser pour l'ordre d'affichage, overide l'ordre primaire. Attention, certains types de champs ne permettent pas de gérer l'ordre (les champs images et fichiers par exemple). | `fields` | — | `0` |
| **Sens du tri**<br />`orderbycustomfielddir` | — | `radio` | `ASC` = Croissant<br />`DESC` = Décroissant | `ASC` (Croissant) |
| **Type de tri**<br />`orderbycustomfieldint` | — | `radio` | `0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date | `0` (Texte) |

### Overide du Frontend

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre de contenus par page**<br />`limit_override` | Indique le nombre de contenu à afficher sur chaque page de liste. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Ordre primaire**<br />`orderby_override` | Définit l'ordre dans lequel les contenus seront affichés dans la liste. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

#### Sélectionner les options disponibles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nb par page autorisé à l'utilisateur en frontend**<br />`limit_options` | Saisissez les valeurs séparées par des virgules qui indiquent les options disponibles, laisser vide pour utiliser les options par défaut. | `text` | — | — |
| **Ordre primaire**<br />`orderby_options` | Sélectionner les options que vous souhaitez faire apparaitre à l'utilisateur en frontend afin qu'il puisse réordonner sa liste de contenu. **Remarque :** (a) **L'ordre par défaut**, est définit dans la section 'vue catégorie -&gt; ordre des contenus', (b)** l’ordre des contenus** ne fonctionne que pour la catégorie active et donc ne fonctionne pas si des sous catégories sont incluses dans la liste. | `fccheckbox` | — | — |

### Texte à Rechercher

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Permet d'afficher et d'utiliser une zone de recherche textuel.**<br />`use_search` | Afficher la zone de recherche textuel | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Libellé de la zone de recherche**<br />`show_search_label` | Afficher/Masquer le libellé de la zone de recherche. | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Afficher | — |
| **Infobulle pour la zone de recherche**<br />`show_search_tip` | Affiche une infobulle d'informations par rapport à la zone de recherche. | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Afficher | — |
| **Bouton rechercher**<br />`show_search_go` | Envoyer le formulaire pour recharger la liste actuelle, ** Remarque **: que cela va soumettre, la recherche de texte, les filtres dans les champs et l'indice alpha (lorsque ces valeurs sont présentes) | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Afficher | — |
| **Bouton annuler**<br />`show_search_reset` | Effacer le formulaire pour recharger la liste actuelle, ** Remarque **: Notez que cela va aussi supprimer les filtres sur les champs et de l'indice alpha (lorsque ces produits sont présents) | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Afficher | — |

#### Paramètres de l’ancienne vue des étiquettes

## Avancé

### Mis en cache

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mis en cache**<br />`cache` | Sélectionnez si vous souhaitez mettre en cache le contenu de ce module. | `list` | `1` = Paramètres globaux<br />`0` = Pas de mise en cache | `1` (Paramètres globaux) |
| **Temps de mise en cache**<br />`cache_time` | Temps avant que le module soit remis en cache. | `text` | — | `900` |

### CSS / JS

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter css**<br />`add_ccs` | Ajouter le fichier CSS par défaut du module | `radio` | `—` = Utiliser le paramètre du composant<br />`0` = Non<br />`1` = Oui<br />`2` = Liens CSS dans le HTML (permet la capture) | — |

### Conteneur du module

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Suffixe de class CSS**<br />`moduleclass_sfx` | Le suffixe sera ajouté à la classe CSS du module, cela permet d'appliquer un style particulier pour le module. | `text` | — | — |
