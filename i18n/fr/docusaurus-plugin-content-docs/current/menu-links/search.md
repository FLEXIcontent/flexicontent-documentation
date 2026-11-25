---
sidebar_position: 11
---

# Recherche



:::info Source
Cette page est générée depuis `site/views/search/tmpl/default.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

:::note
Voici pourquoi certains résultats peuvent être absents : - la recherche de mots courts n’est pas activée dans le composant et le mot compte moins de 4 caractères - le mot est trop courant, par exemple présent dans environ la moitié des articles - langue incorrecte, article non publié ou article expiré
:::

### Formulaire de recherche

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Placement du formulaire**<br />`form_placement` | Définir oui pour afficher la vue de recherche avancée avec 2 colonnes, filtrer à droite et résultat à gauche. | `multilist` | `0` = En haut<br />`1` = A gauche<br />`2` = A droite | `1` (A gauche) |
| **Largeur de colonne**<br />`column_width` | Définir la largeur de la colonne pour les positions gauche et droite _10 %_ | `text` | — | `20%` |
| **Espacement entre colonnes**<br />`column_gap` | Définir l’espacement entre la colonne et les résultats _2rem ou 15px ou 10 %_ | `text` | — | `2rem` |
| **Affichage du sélecteur**<br />`selectors_display_as` | Afficher les types de contenu sous forme de | `radio` | `select` = Liste déroulante<br />`checkboxes` = Liste de cases à cocher | `select` (Liste déroulante) |

#### Types de contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les étiquettes**<br />`show_type_label` | Vous pouvez cacher ou afficher l'étiquette dans la recherche de type de contenu | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Types recherchables **(Ne rien sélectionner pour TOUS)****<br />`contenttypes` | Les types de contenu inclus dans la recherche ; ne rien sélectionner inclut TOUS les types. REMARQUE : vous pouvez autoriser l’utilisateur à sélectionner les types de contenu ; dans ce cas, la liste sera LIMITÉE aux types indiqués ici | `types` | — | — |
| **Autoriser la sélection par l’utilisateur**<br />`canseltypes` | Autoriser les utilisateurs à sélectionner les types de contenu à inclure dans leur recherche | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Recherche textuelle

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les étiquettes**<br />`show_search_label` | Vous pouvez cacher ou afficher le libellé à l'intérieur de la zone de recherche de texte pour économiser de l'espace | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = En dehors du champs<br />`2` = Dans le champs | — |
| **Combinaison des mots**<br />`show_searchphrase` | Autoriser les utilisateurs à choisir la méthode de combinaison des mots recherchés, par exemple phrase, pertinence approximative, tous, n’importe lequel, phrase exacte | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Combinaison par défaut**<br />`default_searchphrase` | Méthode par défaut (présélectionné) pour combiner les termes de recherche | `radio` | `—` = Paramètres globaux<br />`all` = Tous les mots<br />`any` = N'importe quel mot<br />`exact` = Phrase exacte<br />`natural` = Phrase<br />`natural_expanded` = Phrase, plus de résultats | — |
| **Utiliser la subggestion automatique**<br />`search_autocomplete` | Sélectionnez cette option pour utiliser une auto-complétion multi-mots ou une méthode de saisie automatique plus simple ou désactiver la complétion automatique | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Simple<br />`2` = Mots clés | — |
| **Longueur minimale des mots**<br />`minchars` | Longueur minimale autorisée pour les mots recherchés | `text` | — | `3` |
| **Longueur maximale des mots**<br />`maxchars` | Longueur maximale autorisée pour les mots recherchés | `text` | — | `200` |

#### Boutons

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Position des boutons**<br />`buttons_position` | Position des boutons | `radio` | `0` = Boutons après la recherche<br />`1` = Boutons après la recherche avancée | `0` (Boutons après la recherche) |
| **Boutons ajoutés**<br />`append_buttons` | Description des boutons ajoutés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

:::note
Bouton rechercher
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Class du bouton rechercher**<br />`flexi_button_class_go` | Classe pour le bouton de réinitialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | `multilist` | `—` = Paramètres globaux<br />`-1` = - Personnalisé -<br />`btn` = Plein<br />`btn btn-primary` = Principale<br />`btn btn-success` = Succès<br />`btn btn-info` = Info<br />`btn btn-warning` = Avertissement<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn btn-warning` (Avertissement) |
| **Classe personnalisée**<br />`flexi_button_class_go_custom` | Ajouter une classe personnalisée pour le bouton go, exemple uk-button uk-button-large pour un template Warp7 | `text` | — | — |

:::note
Bouton annuler
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bouton annuler**<br />`show_search_reset` | Effacer le formulaire pour recharger la liste actuelle, ** Remarque **: Notez que cela va aussi supprimer les valeurs saisies dans les filtres et de l'indice alpha (lorsque ces produits sont présents) | `multilist` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Classe du bouton annuler**<br />`flexi_button_class_reset` | Classe pour le bouton de réinitialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | `multilist` | `—` = Paramètres globaux<br />`-1` = - Personnalisé -<br />`btn` = Plein<br />`btn btn-primary` = Principale<br />`btn btn-success` = Succès<br />`btn btn-info` = Info<br />`btn btn-warning` = Avertissement<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | — |
| **Classe personnalisée**<br />`flexi_button_class_reset_custom` | Ajouter une classe personnalisée pour le bouton de réinitialisation, exemple uk-button uk-button-large pour un template Warp7 | `text` | — | — |

#### Options avancées

#### Sélecteur de catégories

:::note
REMARQUE : une ou plusieurs valeurs sont autorisées, selon la vue cible (définie ci-dessous)
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le sélecteur**<br />`display_cat_list` | Afficher le sélecteur | `multilist` | `0` = Non (utiliser la catégorie sélectionnée ou actuelle)<br />`1` = Oui (inclure les catégories sélectionnées)<br />`2` = Oui (exclure les catégories sélectionnées) | `0` (Non (utiliser la catégorie sélectionnée ou actuelle)) |
| **Catégories**<br />`catids` | Catégories | `flexicategories` | — | — |
| **Inclure les sous-catégories**<br />`usesubcats` | Inclure les sous-catégories | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'option par défaut (ex. Toutes les couleurs)**<br />`search_firstoptiontext_s` | Texte de la première option de la sélection déroulante, par exemple « Toutes les couleurs » ou « Tous » etc. **NOTE**: Cette option n'a aucune valeur **NOTE**: Ce texte est filtré dans la langue de sorte que vous pouvez entrer une chaîne de langue remplaçable | `text` | — | `FLEXI_ALL` (Tous) |

:::note
REMARQUE : même lorsque la boîte des options de recherche avancée est masquée, les options configurées ci-dessous sont utilisées
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Boîte des options de recherche avancée**<br />`autodisplayadvoptions` | Si cette option est désactivée, un texte cliquable permettra à l’utilisateur d’ouvrir/fermer la boîte de recherche avancée. | `radio` | `0` = Cacher<br />`1` = Oui, initialement fermé<br />`2` = Oui, initialement ouvert | `1` (Oui, initialement fermé) |
| **Recherche textuelle avec**<br />`txtmode` | L’index de recherche de base est plus rapide et recommandé pour les GRANDS SITES (testez pour évaluer la différence de performance) | `multilist` | `0` = Index de base (plus rapide, champs non sélectionnables)<br />`1` = Index avancé (utilise les champs configurés)<br />`2` = Index avancé (utilise les champs configurés, autorise la sélection utilisateur) | `0` (Index de base (plus rapide, champs non sélectionnables)) |

#### Configuration par type de contenu (index avancé)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Champ de recherche texte**<br />`show_txtfields` | Activez cette option pour utiliser des champs spécifiques de recherche | `multilist` | `0` = Utiliser tous les champs recherchables<br />`1` = Selon le type<br />`2` = Configuration en dessous | `1` (Selon le type) |
| **Champs**(Laisser vide pour TOUS)****<br />`txtflds` | Remarque : seuls les champs marqués comme recherchables dans l’index avancé sont listés | `filters` | — | — |
| **Champs comme filtres**<br />`show_filters` | Activer ceci pour utiliser des champs spécifiques comme filtre | `multilist` | `0` = Utiliser tous les champs filtrables<br />`1` = Selon le type<br />`2` = Configuration en dessous | `1` (Selon le type) |
| **Champs**(Laisser vide pour TOUS)****<br />`filtflds` | Remarque : seuls les champs marqués comme filtres de l’index avancé sont listés | `filters` | — | — |
| **Afficher chaque filtre dans un accordéon**<br />`disp_slide_filter` | Afficher la valeur de chaque champ dans son accordéon | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Badge de filtre**<br />`badge_position` | Description du badge de filtre | `radio` | `0` = Non<br />`1` = En haut | `0` (Non) |

#### Zones de recherche (contenus non-FC)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser les zones**<br />`show_searchareas` | Autoriser l’utilisateur à sélectionner et rechercher d’autres zones du site, par exemple les liens web, les contacts utilisateur, etc. | `multilist` | `0` = Désactiver<br />`1` = Activer, afficher le sélecteur | `0` (Désactiver) |
| **Zones de recherche**<br />`searchareas` | Zones de recherche du site (contenus non-FC) incluses dans la recherche. Remarque : si l’utilisateur peut sélectionner les zones de recherche, la liste sera LIMITÉE aux zones sélectionnées ici | `radio` | `—` = Tous | — |
| **Afficher le tri**<br />`show_searchordering` | Autoriser les utilisateurs du frontend à choisir le tri des résultats des autres zones du site. REMARQUE : ce tri est différent de celui utilisé pour les contenus principaux. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeur par défaut**<br />`default_searchordering` | Tri par défaut des résultats de recherche | `radio` | `newest` = Les plus récents en premier<br />`oldest` = Les plus anciens en premier<br />`popular` = Les plus populaires<br />`alpha` = Ordre Alphabétique<br />`category` = Section/Catégorie | `newest` (Les plus récents en premier) |

### Liste des résultats

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre de contenus par page**<br />`limit` | Indique le nombre de contenu à afficher sur chaque page de liste. | `text` | — | `10` |

#### Informations de base (également utilisées pour les résultats non-FC)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la section**<br />`show_section` | Afficher la section de contenu pour chaque résultat, par exemple « liens web », « contacts », etc., ainsi que son arborescence de catégories. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Afficher le contexte**(Toujours actif pour les résultats non-FC)****<br />`show_text` | Afficher les mots recherchés trouvés avec le texte environnant. Les mots trouvés sont mis en évidence | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Limite du contexte** (# of characters) ****<br />`text_chars` | Nombre de caractères du texte affichés autour de chaque mot recherché trouvé | `text` | — | `240` |
| **Afficher la date de création**<br />`show_date` | Afficher la date de création de chaque résultat. Par défaut, le paramètre du type de contenu de chaque résultat est utilisé (Type de contenu → Vue de recherche), choisissez Oui/Non pour remplacer ce paramètre pour tous les types | `radio` | `—` = Rechercher depuis le type<br />`0` = Non<br />`1` = Oui | — |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser l'image**<br />`fcr_use_image` | Extraire la première image du texte principale | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Source de l'image**<br />`fcr_image` | Par défaut, le champ image défini dans le type de contenu de chaque résultat est utilisé (Type de contenu → Vue de recherche). Sélectionnez un champ ou le texte principal pour remplacer ce paramètre pour tous les types | `fcimage` | — | — |
| **Position de l'image**<br />`fcr_position` | Définit la position de l'image dans le bloc. | `radio` | `0` = A gauche<br />`1` = A droite | `0` (A gauche) |
| **Lien sur l'image**<br />`fcr_link_image` | Actif un lien sur l'image affichée. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Taille de l'image**<br />`fcr_image_size` | Taille de l'image pour l'introduction | `list` | `—` = Utiliser les paramètres<br />`s` = Petite<br />`m` = Moyenne<br />`l` = Grande | — |
| **Largeur de l'image**<br />`fcr_width` | Largeur de l'image | `text` | — | `180` |
| **Hauteur de l'image**<br />`fcr_height` | Hauteur de l'image | `text` | — | `180` |
| **Méthode de traitement**<br />`fcr_method` | Méthode de traitement | `radio` | `0` = A l'échelle<br />`1` = Découper | `0` (A l'échelle) |

#### Champs affichés (rendu de leur HTML)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les champs supplémentaires**<br />`use_infoflds` | Afficher les champs supplémentaires pour chaque résultat. Par défaut, les champs définis dans le type de contenu de chaque résultat sont utilisés (Type de contenu → Vue de recherche). Choisissez Oui pour utiliser la liste ci-dessous pour tous les types, ou Non pour n’afficher aucun champ supplémentaire | `multilist` | `—` = Rechercher depuis le type<br />`0` = Non<br />`1` = Oui | — |
| **Sélectionner un champ**<br />`info_fieldlist` | Veuillez sélectionner les champs un par un pour les ajouter à la zone de texte ci-dessous. | `fields` | — | — |
| **Champs**(Laisser vide pour AUCUN)****<br />`infoflds` | Saisir les champs (leurs noms) dont les valeurs doivent être affichées et les afficher dans les résultats de recherche. Vous pouvez séparer les noms de champs par une virgule (,). | `textarea` | — | — |

### Ordre des contenus

#### Ordre du contenu (niveau 1)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby` | Trier les éléments par des champs/propriétés du noyau | `fcordering` | — | — |

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
| **Trier par champ/propriétés du noyau**<br />`orderby_2nd` | Trier les éléments par des champs/propriétés du noyau | `fcordering` | — | — |

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

### Plugin FC Advanced Search : **Surcharger la configuration**

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Limite de recherche**<br />`search_limit` | Limiter le nombre maximal de résultats renvoyés par le plugin, | `text` | — | — |
| **Filtre de langue**<br />`filter_lang` | Renvoie uniquement les contenus dans la langue actuelle | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Rechercher les contenus archivés**<br />`search_archived` | Inclure également les contenus archivés dans la recherche | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Navigation du navigateur**<br />`browsernav` | Browser Navigator | `radio` | `—` = Paramètres globaux<br />`1` = Ouvrir dans une nouvelle fenêtre<br />`2` = Ouvrir dans la même fenêtre | — |
