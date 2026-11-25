---
sidebar_position: 28
---

# Relation

Plugin de champ pour FLEXIcontent - Relation

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/relation/relation.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Édition

#### Édition

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le champ dans un groupe**<br />`use_ingroup` | Activer pour permettre d'utiliser ce champ dans un groupe, qui sera configuré via champ 'Groupe de champ'. REMARQUE: Vous devez alors sélectionner ce champ UNIQUEMENT dans un groupe de champs | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Nombre de valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage conditionnel**<br />`showon` | Affiché en fonction de conditions. Utilisez le format Joomla 'fieldname:value' comme par exemple album_type:2 REMARQUE: ne pas définir ce champ en obligatoire. Également DÉSACTIVER les scripts prettyCheckable / Select2 JS dans tous les champs référencés de type select*, checkbox*, radio* | `text` | — | — |
| **Obligatoire**<br />`required` | Définit si le champ doit être obligatoire dans le formulaire de saisie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Autoriser les valeurs multiples**<br />`allow_multiple` | Autoriser plus d'1 valeur pour ce champs | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plusieurs par valeur**<br />`multiple_per_value` | — | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Position Ajouter**<br />`add_position` | Sélectionnez pour ajouter le bouton en ligne (bouton d'ajout de valeur à chaque ligne) ou afficher le bouton d'ajout au fond de la liste de valeurs | `multilist` | `0` = Bouton Ajouter en bas<br />`1` = Bouton ajouter avant<br />`2` = Bouton Ajouter après<br />`3` = Les deux (avant - après) | `3` (Les deux (avant - après)) |

#### Création des valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Valeurs par défaut**<br />`default_values` | _itemid1:catid1 , itemid2:catid2 , itemid3:catid3_ | `text` | — | — |
| **Utilisation par défaut**<br />`default_value_use` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### Options par valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **max # options**<br />`max_values` | Le nombre maximal d'options qui peuvent être sélectionnées pour chaque valeur du champ | `text` | — | `0` |
| **min # options**<br />`min_values` | Le nombre minimal d'options qui peuvent être sélectionnées pour chaque valeur du champ | `text` | — | `0` |
| **exact # options**<br />`exact_values` | Le nombre exact d'options qui peuvent être sélectionnées pour chaque valeur du champ | `text` | — | `0` |

### Champ formulaire

:::note
Configuration du champ de formulaire comme le nombre de caractères maximum
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre max de contenu dans la liste**<br />`itemcount` | Limite le nombre de contenu a afficher _Nombre_ | `text` | — | `5000` |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Sélecteur de contenus associés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe des titres avec statut**<br />`itemselector_prepend_item_state` | Ajoute le statut après le titre de l'article | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **FLEXI_RIFLD_PREPEND_ITEM_TYPE**<br />`itemselector_prepend_item_type` | — | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **FLEXI_RIFLD_PREPEND_ITEM_ID**<br />`itemselector_prepend_item_id` | — | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Ajouter des champs**<br />`itemselector_append_fields` | — | `fields` | — | — |
| **Nombre de caractères maximum pour le titre**<br />`maxtitlechars` | Nombre maximal de caractères pour le titre, tout titre plus long sera coupé | `text` | — | `40` |
| **Ordre des contenus**<br />`orderby_form` | Sélectionner l'ordre dans lequel vous souhaitez afficher votre liste de contenu. | `list` | `date` = Plus anciens en premier<br />`rdate` = Plus récents en premier<br />`modified` = Modifié -- Le plus récent en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés<br />`rhits` = Les moins consultés<br />`id` = ID -- Plus grand en premier<br />`rid` = ID -- Plus petit en premier<br />`order` = Classer dans la catégorie actuelle | `alpha` (Titre par ordre alphabétique) |

#### Liste des contenus sélectionnés

:::note
NOTE : Combine « Autoriser le tri » avec « Ordre manuel » dans l'onglet de vue
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser le tri**<br />`selected_items_sortable` | Rendre la liste des éléments sélectionnés triable. REMARQUE : dans l'onglet de vue et en « ordre manuel », sinon l’ordre ne sera pas utilisé pour la vue, confondant ainsi vos auteurs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Sélecteur de catégorie

:::note
L’utilisateur devra choisir la catégorie, ensuite les éléments de la catégorie sélectionnée seront listés
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégories sélectionnables**<br />`method_cat` | Sélectionner les catégories qui seront visibles | `multilist` | `1` = Tous<br />`2` = Exclure<br />`3` = Inclure | `1` (Tous) |
| **Catégories**<br />`catids` | Sélectionner les catégories que vous souhaitez inclure ou exclure | `flexicategories` | — | — |
| **Inclure les sous-catégories**<br />`usesubcats` | Utilise toutes les sous-catégories d'une catégorie choisie. L'ajout d'une nouvelle sous-catégorie est automatiquement prise en compte: pas besoin de modifier le champ. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Utiliser les ACL**<br />`use_cat_acl` | Inclure seulement les catégories que l'auteur du contenu peut créer / modifier | `multilist` | `0` = Non<br />`1` = Creatable / Editable | `1` (Creatable / Editable) |

### Filtres de champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Filtres personnalisés**<br />`itemselector_custom_filters` | Filtrer la liste des contenus à l’aide d’autres champs | `filters` | — | — |
| **Performance**<br />`load_method` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `3` = Charger initialement<br />`4` = Charger uniquement si au moins 1 filtre est actif | `3` (Charger initialement) |

### Sélectionner un contenu

:::note
Critères pour choisir quels sont les contenus disponibles pour la sélection étant en relation avec le contenu
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Lister les contenus des sous-catégories**<br />`subcat_items` | Lorsqu’une catégorie est sélectionnée, les contenus des sous-catégories sont également listés | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Type

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode**<br />`method_types` | Choisisez une méthode pour filtrer les contenus | `multilist` | `1` = Tous<br />`2` = Exclure<br />`3` = Inclure | `1` (Tous) |
| **Types**<br />`types` | Sélectionner le ou les type-s à inclure ou exclure | `types` | — | — |

#### Autres limites d'étendu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Seulement la même langue**<br />`samelangonly` | Lorsque cette option est activée uniquement les éléments qui ont la même langue que l'article seront listés. | `radio` | `0` = Pas de limite<br />`1` = Oui | `1` (Oui) |
| **Utiliser les dates de publication/dépublication.**<br />`use_publish_dates` | Permet d'ignorer les dates d'expirations des articles sélectionnés | `radio` | `0` = Pas de limite<br />`1` = Oui | `1` (Oui) |
| **Les articles publiés seulement**<br />`onlypublished` | Si cette option est désactivée les articles dépubliés seront également afficher | `radio` | `0` = Pas de limite<br />`1` = Oui | `1` (Oui) |
| **Article détenu par**<br />`ownedbyuser` | Articles détenus par (a) tout utilisateur ou (b) par l'utilisateur qui modifie l'élément actuellement par le propriétaire de l'élément courant | `radio` | `0` = N'importe quel utilisateur<br />`1` = Modifier l'utilisateur<br />`2` = propriétaire du contenu | `0` (N'importe quel utilisateur) |

#### Édition

## Apparence

#### Apparence

### Basique

#### Affichage

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher pour les clients**<br />`show_in_clients` | Sélectionner si le champ sera créé et affiché à des clients spécifiques | `fccheckbox` | — | — |
| **Afficher dans les vues**<br />`show_in_views` | Sélectionner si le champ sera créé et affiché en fonction d'une vue spécifique | `fccheckbox` | — | — |

#### Libellé et accès

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Montrer un message d'**accès interdit****<br />`show_acc_msg` | Si le champ est inaccessible, une message de non-accès s'affichera. **NOTE : ** SI ce paramètre est désactivé, le champ sera invisible aux utilisateurs sans accès, sans aucun message ou avertissement indiquant son existance | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Message **accès interdit****<br />`no_acc_msg` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Exporter

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### FLEXI_BACKEND_VIEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_BACKEND_VIEW_APPEARANCE**<br />`backend_view_appearance` | FLEXI_BACKEND_VIEW_APPEARANCE_DESC | `multilist` | `0` = Par défaut<br />`1` = FLEXI_CHECK_MARK<br />`2` = FLEXI_CLEAN_HTML_AND_TRIM | `0` (Par défaut) |
| **FLEXI_TRIM_LENGTH**<br />`backend_view_trim_chars` | FLEXI_TRIM_LENGTH_DESC | `text` | — | `100` |

### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |

:::note
Pour les options de configuration, communes à toutes les mises en page, veuillez voir d'autres onglets de cette page
:::

### Liste des contenus en relation

:::note
Options d'affichage: -- Liste de contenu (liée à l'élément courant)
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **List de contenu visible**<br />`itemslist_acclvl` | Seuls les utilisateurs disposant de ce niveau d’accès (appartenant à un groupe d’utilisateurs qui a ce niveau d'accès) seront en mesure de voir la liste des articles | `accesslevel` | — | `1` |

#### Liste des contenus en relation

### Contenu filtré

:::note
Les contenus correspondant à tous les critères sélectionnés seront inclus, Remarque : laissez vide pour ignorer la limitation spécifique
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Seulement la même langue**<br />`samelangonly_view` | Lorsque cette option est activée uniquement les éléments qui ont la même langue que l'article seront listés. | `radio` | `-1` = identique à l'édition<br />`1` = Oui | `-1` (identique à l'édition) |
| **Utiliser les dates de publication/dépublication.**<br />`use_publish_dates_view` | Permet d'ignorer les dates d'expirations des articles sélectionnés | `radio` | `-1` = identique à l'édition<br />`1` = Oui | `1` (Oui) |
| **Les articles publiés seulement**<br />`onlypublished_view` | Si cette option est désactivée les articles dépubliés seront également afficher | `radio` | `-1` = identique à l'édition<br />`1` = Oui | `1` (Oui) |
| **Article détenu par**<br />`ownedbyuser_view` | Articles détenus par (a) tout utilisateur ou (b) par l'utilisateur qui modifie l'élément actuellement par le propriétaire de l'élément courant | `radio` | `-1` = identique à l'édition<br />`1` = Modifier l'utilisateur<br />`2` = propriétaire du contenu | `-1` (identique à l'édition) |

### Ordre des contenus

:::note
NOTE : Combiner « Ordre manuel » avec « Permettre le tri » dans l’onglet d’édition
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby` | Trier les éléments par des champs/propriétés du noyau | `list` | `date` = Plus anciens en premier<br />`rdate` = Plus récents en premier<br />`modified` = Modifié -- Le plus récent en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés<br />`rhits` = Les moins consultés<br />`id` = ID -- Plus grand en premier<br />`rid` = ID -- Plus petit en premier<br />`commented` = Les plus commentés<br />`rated` = Les mieux notés<br />`order` = Classer dans la catégorie actuelle<br />`jorder` = Ordre (Global)<br />`random` = Aléatoire<br />`manual` = Trie manuel (ranger comme dans le formulaire d'édition) | `alpha` (Titre par ordre alphabétique) |

#### Classement personnalisé des champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`orderbycustomfield` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Champ personnalisé**<br />`orderbycustomfieldid` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | `fields` | — | `0` |
| **Sens du tri**<br />`orderbycustomfielddir` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `list` | `ASC` = Croissant<br />`DESC` = Décroissant | `ASC` (Croissant) |
| **Méthode de tri**<br />`orderbycustomfieldint` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `list` | `0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date | `0` (Texte) |

### Élément HTML

:::note
Configurer le HTML à utiliser pour afficher chaque contenu
:::

:::note
Remarque : Cette configuration peut être surchargée suivant les vue, via l'onglet 'information totale'
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Élément HTML**<br />`relitem_html` | Entrez le code HTML à utiliser pour chaque élément, **NOTE :** vous pouvez utiliser : **__display_text__** -- est remplacé par du texte personnalisé créé selon les paramètres **&#123;&#123;fieldname&#125;&#125;** ou **&#123;&#123;fieldname##displayvar&#125;&#125;** -- est remplacé par l'affichage HTML de chaque champ **&#123;&#123;fieldname##label&#125;&#125;** -- est remplacé par l'étiquette de chaque champ **%%language_string%%** -- est remplacé par la chaîne de langue Enfin, vous pouvez utiliser les remplacements liés aux objets : __item_url__, __item_title_escaped__, __item_tooltip__ et les propriétés de l'élément comme : &#123;item-&gt;id&#125;, &#123;item-&gt;title&#125;, etc | `editor` | — | `__display_text__` |

#### Contenu de __display_text__

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Texte personnalisé**<br />`displayway` | Affiche l'ID du contenu (par exemple pour l'utilisation d'un plugin Joomla) ou le titre du contenu (par exemple pour faire un lien vers le détail du contenu) | `list` | `0` = ID du contenu<br />`1` = Titre du contenu | `1` (Titre du contenu) |
| **Ajout un lien vers le contenu**<br />`addlink` | Activer cette option pour ajouter une infobulle | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Ajout d'une infobulle**<br />`addtooltip` | Activer cette option pour ajouter une infobulle | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pré-configuration**<br />`prx_sfx_open_close_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage) | — |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Séparateur de valeurs (vues frontend)**<br />`separatorf` | Choisir le séparateur pour séparer l'ensemble des valeurs dans l'affichage frontend (placé entre les valeurs) | `multilist` | `0` = Espace<br />`1` = Saut de ligne<br />`6` = Ligne Horizontale<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère)<br />`7` = Séparateur personnalisé | `1` (Saut de ligne) |
| **Séparateur personnalisé**<br />`separatorf_custom` | — | `text` | — | — |
| **Texte d'ouverture**<br />`opentag` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

#### Liste des contenus en relation

### Bouton de contenu auto-relation

:::note
Options d'affichage: Soumission en relation automatique - Permet de soumettre un nouvel élément avec mise en relation automatique à l'élément courant affiché.
Ceci est utile pour créer par exemple un nouveau ** rapport de produit**, une nouvelle **application métier**, sans que l'utilisateur ait à sélectionner le **produit** rapporté ou le **métier** appliqué
:::

:::note
Remarque : Cette configuration peut être surchargée suivant les vue, via l'onglet 'information totale'
:::

:::note
Note : votre formulaire a besoin d'un champ de RELATION-INVERSE !! qui sera configuré en miroir de ce champ !!
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le bouton**<br />`auto_relate_curritem` | Un lien de soumission s'affichera (formulaire de nouveau contenu), ce qui créera un nouveau contenu qui sera en relation avec le contenu courant. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Position Bouton**<br />`auto_relate_position` | Mettre le bouton avant ou après la liste de contenus | `radio` | `0` = Avant<br />`1` = Après<br />`2` = Les deux | `0` (Avant) |
| **Visibilité du bouton**<br />`auto_relate_acclvl` | Seuls les utilisateurs disposant de ce niveau d’accès (appartenant à un groupe d’utilisateurs qui a ce niveau d'accès) seront en mesure d’afficher le bouton. NOTE : cela masque seulement le bouton, vous devez toujours configurer les ACL en mode ajout ainsi que le lien de menu d’ajout pour les utilisateurs qui peuvent les voir. REMARQUE : du fait des ACL, vous pourriez souhaiter que certains utilisateurs puissent voir le bouton, mais qu'ils ne puissent pas soumettre, dans ce cas activez l'option « afficher non autorisés » ci-dessous !! | `accesslevel` | — | `1` |
| **Afficher les contenus non-autorisés**<br />`auto_relate_show_to_unauth` | Afficher le bouton 'soumettre' aux utilisateurs non-autorisés. **Si actif, attention**: sauf si le lien de menu permet la soumission d'éléments par les utilisateurs non autorisés -&gt; a. les invités sont redirigés vers la page de connexion / b. les utilisateurs connectés mais non autorisés sont redirigés sur l'URL indiquée - dans la configuration du composant - surclassé par l'uRL dans la configuration du type de contenu - surclassé par l'uRL dans le lien de menu de soumission | `radio` | `0` = Non<br />`1` = Oui, sauf pour les invités<br />`2` = Oui | `0` (Non) |

#### Personnalisé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Soumettre l'itemid du menu ***<br />`auto_relate_menu_itemid` | Indiquer l'ID de l'élément de menu de soumission. La configuration utile sera retrouvée à partir de l'élément de menu de soumission choisi, ex: - **Le TYPE de contenu** du nouvel élément lié (en cours de soumission), habituellement vous devriez sélectionner un type de contenu spécifique dans l'élément de menu, comme 'Rapport produit' ou 'application métier' - **Les catégories**, normalement sont contrôlées par ACL, mais dans ce cas il pourrait être approprié de sélectionner la ou les catégories dans l'élément de menu ! | `fcmenuitem` | `—` = Sélectionner | — |
| **Titre du bouton**<br />`auto_relate_submit_title` | C’est le titre qui sera affiché à la place de « Ajouter nouveau », vous pouvez par exemple utiliser une chaîne de langue comme MYTXT_SUBMIT_TEXT | `text` | — | — |
| **Texte du bouton**<br />`auto_relate_submit_text` | C’est le texte qui s’affichera à la place de « Ajouter nouveau contenu », vous pouvez par exemple utiliser une chaîne de langue comme MYTXT_SUBMIT_TEXT_TIP | `text` | — | — |
| **Message dans le formulaire**<br />`auto_relate_submit_mssg` | Le champ de relation inverse affichera ce texte, dans le formulaire du contenu | `text` | — | — |

### Décompte total

:::note
Options d'affichage: -- Total counter ** Un affichage plus compact qui permet d’ignorer ou de compacter la liste des contenus, par exemple dans la vue catégorie**
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer total**<br />`show_total_only` | Afficher le nombre total de contenus relatives, au lieu d'afficher la liste des contenus relatives | `multilist` | `0` = Non<br />`1` = Oui<br />`2` = Oui, cacher le zéro | `0` (Non) |
| **Activer dans les vues**<br />`total_in_view` | Vous pouvez activer ou désactiver le paramètre ci-dessus en fonction de la vue active de FLEXIcontent | `fccheckbox` | — | — |
| **Ajouter du texte**<br />`total_append_text` | Saisir le texte avant le total | `text` | — | — |

#### Montrer les informations supplémentaires

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bouton de contenu auto-relation**<br />`total_show_auto_btn` | Permet d'afficher un bouton de soumission d'article qui sera en automatiquement en relation avec le contenu en cours - (si fonction activée et configurée - voir ci-dessus) | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Liste des éléments en relation**<br />`total_show_list` | Activer pour montrer aussi la liste des éléments (ci-dessous il est possible surcharger la configuration de la liste) | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Surcharge par défaut

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Élément HTML**<br />`total_relitem_html` | Entrez le code HTML à utiliser pour chaque élément, **NOTE :** vous pouvez utiliser : **__display_text__** -- est remplacé par du texte personnalisé créé selon les paramètres **&#123;&#123;fieldname&#125;&#125;** ou **&#123;&#123;fieldname##displayvar&#125;&#125;** -- est remplacé par l'affichage HTML de chaque champ **&#123;&#123;fieldname##label&#125;&#125;** -- est remplacé par l'étiquette de chaque champ **%%language_string%%** -- est remplacé par la chaîne de langue Enfin, vous pouvez utiliser les remplacements liés aux objets : __item_url__, __item_title_escaped__, __item_tooltip__ et les propriétés de l'élément comme : &#123;item-&gt;id&#125;, &#123;item-&gt;title&#125;, etc | `editor` | — | `__display_text__` |

#### Apparence

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

#### Filtrer

### Valeurs

#### Comparaison des valeurs de filtre

:::note
... si le champ est multiple (Formulaire de contenu) ... et a une apparence de filtre multiple
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Requérir TOUTES les valeurs sélectionnées**<br />`filter_values_require_all` | Habituellement, vous allez inclure des éléments trouvés ayant une des valeurs sélectionnées. -- Vous pouvez sélectionner **pour que toutes les valeurs de filtre** sélectionnées soient correspondantes pour les éléments trouvés. -- **AVERTISSEMENT** aux développeurs de nouveaux types de champs : cela ne fonctionnera pas correctement si votre champ enregistre la valeur du champ SAME plus d'une fois pour le même élément. Donc, dans un tel cas, n'ajoutez pas cette option à votre champ ! | `radio` | `0` = Non<br />`1` = Oui, plus lentement | `0` (Non) |
| **Information pour Requérir AU MOINS UNE / TOUTES**<br />`filter_values_require_all_tip` | choisir de montrer l'information si aucune ou toutes les valeurs de filtre sélectionnées sont requises | `radio` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |

### Vue Catégorie

#### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Recherche texte (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Sélecteur liste déroulante

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Option par défaut personnalisé (pour toutes les valeurs)**<br />`filter_usefirstoption` | Activer pour personnaliser la première option du filtre (=toutes les valeurs) . NOTE : ceci n'est utilisé que dans le cas de la sélection déroulante, et aussi si l'étiquette du champ n'est pas placée à l'intérieur du sélecteur | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'option par défaut (ex. Toutes les couleurs)**<br />`filter_firstoptiontext` | Texte de la première option de la sélection déroulante, par exemple « Toutes les couleurs » ou « FLEXI_ALL » etc. **NOTE**: Cette option n'a aucune valeur **NOTE**: Ce texte est filtré dans la langue de sorte que vous pouvez entrer une chaîne de langue remplaçable | `text` | — | `FLEXI_ALL` (Tous) |

#### Curseur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Données du slider**<br />`slider_display_config` | Utiliser les valeurs existantes dans le champ, ou spécifier vos propre valeurs d'échelle | `multilist` | `1` = Valeurs trouvées<br />`2` = Valeurs personnalisées | `1` (Valeurs trouvées) |
| **Valeurs personnalisées**<br />`slider_custom_range` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': '50', '50%': '150', '75%': '600', 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_50 ## label_150 ## label_600 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Préfixe / Suffixe

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_filter` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_filter` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Texte d'ouverture**<br />`opentag_filter` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_filter` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

### Vue recherche avancée

#### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Recherche texte (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter_s` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items_s` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values_s` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Sélecteur liste déroulante

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Option par défaut personnalisé (pour toutes les valeurs)**<br />`filter_usefirstoption_s` | Activer pour personnaliser la première option du filtre (=toutes les valeurs) . NOTE : ceci n'est utilisé que dans le cas de la sélection déroulante, et aussi si l'étiquette du champ n'est pas placée à l'intérieur du sélecteur | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'option par défaut (ex. Toutes les couleurs)**<br />`filter_firstoptiontext_s` | Texte de la première option de la sélection déroulante, par exemple « Toutes les couleurs » ou « FLEXI_ALL » etc. **NOTE**: Cette option n'a aucune valeur **NOTE**: Ce texte est filtré dans la langue de sorte que vous pouvez entrer une chaîne de langue remplaçable | `text` | — | `FLEXI_ALL` (Tous) |

#### Curseur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Données du slider**<br />`slider_display_config_s` | Utiliser les valeurs existantes dans le champ, ou spécifier vos propre valeurs d'échelle | `multilist` | `1` = Valeurs trouvées<br />`2` = Valeurs personnalisées | `1` (Valeurs trouvées) |
| **Valeurs personnalisées**<br />`slider_custom_range_s` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': 500, '50%': 2000, '75%': 10000, 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels_s` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_500 ## label_2000 ## label_10000 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext_s` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Préfixe / Suffixe

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_filter_s` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_filter_s` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Texte d'ouverture**<br />`opentag_filter_s` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_filter_s` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

#### Filtrer
