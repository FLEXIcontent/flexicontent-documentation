---
sidebar_position: 29
---

# Relation inverse

Plugin de champ 'Relation Reverse' pour FLEXIcontent

*Plugin : `relation_reverse` — Relation inverse*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/relation_reverse/relation_reverse.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Inversion

:::note
Liste de contenu relatif au contenu 'courant' via un champ liste déroulante
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Champ de relation inversé**<br />`reverse_field` | Sélectionner un champ de relation pour faire un lien réciproque | `fields` | — | — |

## Édition

#### Liste des contenus en relation

### Liste des contenus en relation

:::note
Formulaire de contenu : vous pouvez modifier l'affichage de la liste des contenus en **lecture seule** (relative au contenu courant)
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre max de contenu dans la liste**<br />`itemcount_form` | Limite le nombre de contenu a afficher _Nombre_ | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

### Ordre des contenus

:::note
Sélectionner l'ordre dans lequel vous souhaitez afficher votre liste de contenu.
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby_form` | Trier les éléments par des champs/propriétés du noyau | `list` | `—` = FLEXI_ORDER_DEFAULT<br />`date` = Plus anciens en premier<br />`rdate` = Plus récents en premier<br />`modified` = Modifié -- Le plus récent en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés<br />`rhits` = Les moins consultés<br />`id` = ID -- Plus grand en premier<br />`rid` = ID -- Plus petit en premier<br />`order` = Classer dans la catégorie actuelle | `alpha` (Titre par ordre alphabétique) |

#### Classement personnalisé des champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`orderbycustomfield_form` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Champ personnalisé**<br />`orderbycustomfieldid_form` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | `fields` | — | `0` |
| **Sens du tri**<br />`orderbycustomfielddir_form` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `list` | `ASC` = Croissant<br />`DESC` = Décroissant | `ASC` (Croissant) |
| **Méthode de tri**<br />`orderbycustomfieldint_form` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `list` | `0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date | `0` (Texte) |

### Élément HTML

:::note
Configurer le HTML à utiliser pour afficher chaque contenu
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Élément HTML**<br />`relitem_html_form` | Entrez le code HTML à utiliser pour chaque élément, **NOTE :** vous pouvez utiliser : **__display_text__** -- est remplacé par du texte personnalisé créé selon les paramètres **&#123;&#123;fieldname&#125;&#125;** ou **&#123;&#123;fieldname##displayvar&#125;&#125;** -- est remplacé par l'affichage HTML de chaque champ **&#123;&#123;fieldname##label&#125;&#125;** -- est remplacé par l'étiquette de chaque champ **%%language_string%%** -- est remplacé par la chaîne de langue Enfin, vous pouvez utiliser les remplacements liés aux objets : __item_url__, __item_title_escaped__, __item_tooltip__ et les propriétés de l'élément comme : &#123;item-&gt;id&#125;, &#123;item-&gt;title&#125;, etc | `editor` | — | `__display_text__` |

#### Contenu de __display_text__

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Texte personnalisé**<br />`displayway_form` | Affiche l'ID du contenu (par exemple pour l'utilisation d'un plugin Joomla) ou le titre du contenu (par exemple pour faire un lien vers le détail du contenu) | `list` | `0` = ID du contenu<br />`1` = Titre du contenu | `1` (Titre du contenu) |
| **Ajout un lien vers le contenu**<br />`addlink_form` | Activer cette option pour ajouter une infobulle | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Ajout d'une infobulle**<br />`addtooltip_form` | Activer cette option pour ajouter une infobulle | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_form` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_form` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Séparateur de valeur formulaire de saisie**<br />`separator` | Choisir le séparateur pour séparer l'ensemble des valeurs dans les formulaires de saisies (placé entre les valeurs) | `list` | `0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | `1` (Saut de ligne) |
| **Texte d'ouverture**<br />`opentag_form` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_form` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

#### Liste des contenus en relation

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
| **Nombre max de contenu dans la liste**<br />`itemcount` | Limite le nombre de contenu a afficher _Nombre_ | `text` | — | — |
| **List de contenu visible**<br />`itemslist_acclvl` | Seuls les utilisateurs disposant de ce niveau d’accès (appartenant à un groupe d’utilisateurs qui a ce niveau d'accès) seront en mesure de voir la liste des articles | `accesslevel` | — | `1` |

#### Liste des contenus en relation

### Contenu filtré

:::note
Les contenus correspondant à tous les critères sélectionnés seront inclus, Remarque : laissez vide pour ignorer la limitation spécifique
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégorie**<br />`reverse_scope_category` | Sélectionnez une catégorie | `flexicategories` | — | — |
| **Types**<br />`reverse_scope_types` | Sélectionner le ou les type-s à inclure ou exclure | `types` | — | — |

#### Autres limites d'étendu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Seulement la même langue**<br />`samelangonly` | Lorsque cette option est activée uniquement les éléments qui ont la même langue que l'article seront listés. | `radio` | `0` = Pas de limite<br />`1` = Oui | `1` (Oui) |
| **Utiliser les dates de publication/dépublication.**<br />`use_publish_dates` | Permet d'ignorer les dates d'expirations des articles sélectionnés | `radio` | `0` = Pas de limite<br />`1` = Oui | `1` (Oui) |
| **Les articles publiés seulement**<br />`onlypublished` | Si cette option est désactivée les articles dépubliés seront également afficher | `radio` | `0` = Pas de limite<br />`1` = Oui | `1` (Oui) |
| **Article détenu par**<br />`ownedbyuser` | Articles détenus par (a) tout utilisateur ou (b) par l'utilisateur qui modifie l'élément actuellement par le propriétaire de l'élément courant | `radio` | `0` = N'importe quel utilisateur<br />`1` = Modifier l'utilisateur<br />`2` = propriétaire du contenu | `0` (N'importe quel utilisateur) |

### Ordre des contenus

:::note
Sélectionner l'ordre dans lequel vous souhaitez afficher votre liste de contenu.
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby` | Trier les éléments par des champs/propriétés du noyau | `list` | `date` = Plus anciens en premier<br />`rdate` = Plus récents en premier<br />`modified` = Modifié -- Le plus récent en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés<br />`rhits` = Les moins consultés<br />`id` = ID -- Plus grand en premier<br />`rid` = ID -- Plus petit en premier<br />`commented` = Les plus commentés<br />`rated` = Les mieux notés<br />`order` = Classer dans la catégorie actuelle<br />`jorder` = Ordre (Global)<br />`random` = Aléatoire | `alpha` (Titre par ordre alphabétique) |

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
