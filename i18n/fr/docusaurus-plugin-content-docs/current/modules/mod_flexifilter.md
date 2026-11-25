---
sidebar_position: 6
---

# Filtres de contenus

FLEXIcontent fournit six modules frontend pour afficher des contenus, des catégories, des formulaires de recherche, des filtres, des cartes et des nuages d’étiquettes. Configurez un module depuis **Extensions → Modules**.

> Ce module affiche un formulaire de filtrage pour les vues liste d'articles type (catégorie, auteur, mots clés, etc)

:::info Source
Cette page est générée depuis `modules/mod_flexifilter/mod_flexifilter.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

### Template du module

:::note
Veuillez définir les paramètres de disposition dans l’onglet **Disposition : ...**. Les développeurs CSS/HTML doivent consulter : ** Guide des modèles personnalisés **
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Template**<br />`layout` | Choisir la mise en page de votre module | `fclayout` | — | `default` |
| **Faire défiler vers le module**<br />`scroll_to_anchor_tag` | Activer pour faire défiler vers le module au chargement de la page | `radio` | `0` = Non<br />`1` = Oui<br />`2` = Lorsque des filtres sont actifs | `0` (Non) |

### Paramètres de la catégorie filtrée

:::note
Catégorie spécifique (pas de sélecteur de catégorie affiché) ou Categorie par défaut pour la catégorie sélectionnée ou sélectionnez Aucune pour filtrer la catégorie en cours
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégorie spécifique ou par défaut ou pas (= actuelle)**<br />`catid` | -- Une catégorie spécifique sous forme de filtre soumettra (pas de sélecteur de catégorie affichée), -- OU la catégorie par défaut, présélectionné dans la catégorie sélectionnée, -- OU sélectionnez Aucune pour filtrer la catégorie de la catégorie en actuelle | `fccategory` | — | — |
| **ID de l’élément de menu Vue catégorie**<br />`cat_itemid` | Entrez l’élément de menu de la catégorie à utiliser pour l'affichage de la liste d'éléments NOTE 1 : cette méthode est recommandée si vous avez plusieurs éléments de menu pointant vers la catégorie, qui peut-être avoir un filtrage différentes options (p. ex. une liste d'éléments en « vedette ») NOTE 2 : élément de menu doit pointer vers la catégorie la plus importante dans la hierachie, sinon il pourrait y avoir un soucis d'affichage voir aucun élément n’apparaît | `fcmenuitem` | `—` = Cliquez pour sélectionner | — |

#### Sélecteur de catégorie

:::note
NOTE 1: ceci remplace le filtre de catégorie NOTE 2: valeurs simples ou multiples autorisés, cela dépend de la vue cible (choisie ci-dessous)
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le sélecteur**<br />`display_cat_list` | Afficher le sélecteur de catégorie pour sélectionner une ou plusieurs catégories de filtrage | `multilist` | `0` = Non (la catégorie sélectionnée ou la catégorie active)<br />`1` = Oui (Inclure les catégories sélectionnées)<br />`2` = Oui (Exclure les catégories sélectionnées) | `0` (Non (la catégorie sélectionnée ou la catégorie active)) |
| **Catégorie**<br />`catids` | Vous pouvez limiter le sélecteur de catégorie à des catégories spécifiques ou exclure des catégories spécifiques. Sélectionnez Aucun pour afficher toutes les catégories que l'utilisateur pourra voir. | `flexicategories` | — | — |
| **Inclure les sous catégories**<br />`usesubcats` | Autoriser l'utilisation de toutes les sous catégories pour les catégories sélectionnées. De cette façon vous n'avez pas à paramètrer ce module à chaque fois qu'une nouvelle catégorie sera ajoutée. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Vue cible catégorie unique / multi-catégories / etc

:::note
Cette option détermine si le sélecteur de catégories autorise la sélection de plusieurs catégories
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Formulaire cible**<br />`mcats_selection` | Sélectionnez la vue que le module va filtrer, soit une vue catégorie simple, soit une vue catégories multiples, ou autre... dans le cadre d'une vue de type **catégorie simple** l'élément de menu sera sélectionné automatiquement, mais dans le cas d'une vue de type **catégories multiples** (mcats) vous devrez choisir un élément de menu à utiliser, de cette façon vous pouvez définir le gabarit, le comportement, etc... | `multilist` | `0` = Vue catégorie simple (élément de menu sélectionné automatiquement)<br />`1` = Catégories multiples (choisissez l'élément de menu ci-dessous) | `0` (Vue catégorie simple (élément de menu sélectionné automatiquement)) |
| **ID de l’élément de menu vue catégories multiple**<br />`mcats_itemid` | L'iD de l’élément de menu des vues de type catégories multiples (mcats), de sorte à ce que vous puissiez configurer la vue (gabarit, comportements, etc.). Configurer cette partie avec soin sinon vous n'aurez aucun contenus listés. | `fcmenuitem` | `—` = Cliquez pour sélectionner | — |

### Formulaire(Recherche texte / Flitrage champ)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Placement des champs formulaires**<br />`ff_placement` | Sélectionner où le formulaire sera placé | `multilist` | `0` = En ligne<br />`1` = Slider | `0` (En ligne) |
| **Bouton de formulaire déroulant**<br />`ff_toggle_search_title` | Le texte de lien/bouton d'ouverture/affichage du formulaire de recherche par défaut est « Recherche » | `text` | — | `FLEXI_TOGGLE_SEARCH_FORM_MODULE` (Rechercher) |
| **Validation automatique**<br />`filter_autosubmit` | Envoyer un formulaire automatiquement lors d'un changement de filtre. Si vous n'activez pas cela, alors les utilisateurs seront en mesure de mettre de nombreux filtres avant de soumettre le formulaire. NOTE **: ** Certains filtres peuvent auto-envoyer le formulaire en dépit de ce paramètre | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Filtre Ajax**<br />`filter_ajax` | Description du filtrage Ajax | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Badge de filtre**<br />`badge_position` | Description du badge de filtre | `fcradio` | `0` = Non<br />`1` = En haut<br />`2` = En bas | `2` (En bas) |
| **Instructions**<br />`filter_instructions` | Afficher les instructions d'utilisation du formulaire de filtrage. Vous pouvez créer des substitutions de langue joomla pour les chaînes de langue pour donner des instructions personnalisées à vos utilisateurs | `radio` | `0` = Cacher<br />`1` = Oui, avec une infobulle<br />`2` = Oui, en ligne | `1` (Oui, avec une infobulle) |

#### Boutons

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bouton rechercher**<br />`show_search_go` | Envoyer le formulaire pour recharger la liste actuelle, ** Remarque **: que cela va soumettre, la recherche de texte, les filtres dans les champs et l'indice alpha (lorsque ces valeurs sont présentes) | `multilist` | `0` = Auto<br />`1` = Afficher | `1` (Afficher) |
| **Class du bouton rechercher**<br />`flexi_button_class_go` | Classe pour le bouton de réinitialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | `multilist` | `-1` = - Personnalisé -<br />`btn` = Plein<br />`btn btn-primary` = Principale<br />`btn btn-success` = Succès<br />`btn btn-info` = Info<br />`btn btn-warning` = Avertissement<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn btn-success` (Succès) |
| **Classe personnalisée**<br />`flexi_button_class_go_custom` | Ajouter une classe personnalisée pour le bouton go, exemple uk-button uk-button-large pour un template Warp7 | `text` | — | — |
| **Bouton annuler**<br />`show_search_reset` | Effacer le formulaire pour recharger la liste actuelle, ** Remarque **: Notez que cela va aussi supprimer les filtres sur les champs et de l'indice alpha (lorsque ces produits sont présents) | `multilist` | `0` = Cacher<br />`1` = Afficher | `1` (Afficher) |
| **Classe du bouton annuler**<br />`flexi_button_class_reset` | Classe pour le bouton de réinitialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | `multilist` | `-1` = - Personnalisé -<br />`btn` = Plein<br />`btn btn-primary` = Principale<br />`btn btn-success` = Succès<br />`btn btn-info` = Info<br />`btn btn-warning` = Avertissement<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn` (Plein) |
| **Classe personnalisée**<br />`flexi_button_class_reset_custom` | Ajouter une classe personnalisée pour le bouton de réinitialisation, exemple uk-button uk-button-large pour un template Warp7 | `text` | — | — |

### Texte à Rechercher

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Permet d'afficher et d'utiliser une zone de recherche textuel.**<br />`use_search` | Afficher la zone de recherche textuel | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Afficher les étiquettes**<br />`show_search_label` | Vous pouvez cacher ou afficher le libellé à l'intérieur de la zone de recherche de texte pour économiser de l'espace | `radio` | `0` = Cacher<br />`1` = En dehors du champs<br />`2` = Dans le champs | `1` (En dehors du champs) |
| **Utiliser la subggestion automatique**<br />`search_autocomplete` | Choisissez d'utiliser le mode mots-tag comme l'auto-suggestion, ou un seul mot simple ou désactiver | `radio` | `0` = Non<br />`1` = Simple<br />`2` = Mots clés | `1` (Simple) |
| **Combinaison de mots**<br />`show_searchphrase` | Permettre aux utilisateurs de sélectionner la méthode de combiner les mots à rechercher, par exemple, phrase, expression (davantage de résultats), tous les mots, n’importe quel mot, expression exacte | `radio` | `0` = Cacher<br />`1` = Afficher | `1` (Afficher) |
| **Combinaison par défaut**<br />`default_searchphrase` | Méthode par défaut (présélectionné) pour combiner les termes de recherche | `radio` | `all` = Tous les mots<br />`any` = N'importe quel mot<br />`exact` = Phrase exacte<br />`natural` = Phrase<br />`natural_expanded` = Phrase, plus de résultats | `all` (Tous les mots) |

### Champs filtre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les filtres**<br />`use_filters` | Permettra d'afficher les filtres de champs. Notez que vous pouvez définir l'apparence et le comportement du filtre en modifiant la configuration de chaque champ individuellement | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher les filtres**<br />`display_filter_list` | Définit les filtres qui doivent être affichées | `multilist` | `0` = Tous (autoriser dans une catégorie)<br />`1` = En fonction des paramètres de la catégorie<br />`2` = Sélectionner ci-dessous<br />`3` = Sélectionner ci-dessous & paramètres de la catégorie | `0` (Tous (autoriser dans une catégorie)) |
| **Choisissez les filtres**<br />`filters` | Choisissez les filtres que vous souhaitez charger pour cette catégorie | `filters` | — | — |
| **Etiquette des filtres**<br />`show_filter_labels` | Forcer l'affichage ou non de l'ensemble des libellés pour chaque champ de filtre, ce paramètre outrepassera automatiquement les paramètre de chaque champs. | `radio` | `0` = Réglages des champs<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `1` (En dehors du filtre) |
| **Valeurs initiales de filtres**<br />`initial_filters` | Ce sont les valeurs initiales des filtres, l'utilisateur peut passer outre. Utilisation : field_id ##value%%field_id##%%valeur par exemple 22##14%%47##%%valeur19##unmot pour les plages utiliser field_id##valeur1---valeur2 pour les valeurs multiples utilisent field_id##valeur1+++valeur2+++value3 Remarque : votre champ doit être configuré pour être utiliser comme filtre ou comme multi-valeur sinon les valeurs ne seront pas utilisés comme prévu | `textarea` | — | — |
| **Filtre dans le panneau coulissant**<br />`fc_filter_in_slide` | Filtre dans le panneau coulissant | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Affichage de la liste des filtres

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **1 enregistrement par ligne**<br />`filter_placement` | Sélectionnez la façon dont les résultats seront affichés: - Afficher un seul enregistrement par ligne, ou - Utilisez un séparateur personnalisé | `radio` | `2` = Oui, mais utiliser l'option ci-dessous<br />`1` = Oui<br />`0` = Non, utilisé un séparateur<br />`3` = Placer dans un onglet | `1` (Oui) |
| **Séparateur de résultat ignoré si les enregistrements sont affichés par ligne**<br />`filter_separatorf` | Choisissez un séparateur pour séparer les enregistrements (placé entre les valeurs). ** Remarque : ** Ce paramètre est ignoré lorsque vous placez les enregistrements par ligne | `list` | `0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | `0` (Espace) |
| **Préfixe sous-catégorie**<br />`filter_pretext` | Ce texte est placé **devant** chaque titre de sous catégories | `text` | — | — |
| **Suffixe sous-catégorie**<br />`filter_posttext` | Ce texte est placé **après** chaque titre de sous catégories. | `text` | — | — |
| **Texte d'ouverture**<br />`filter_opentag` | Texte ou code HTML ajouté au début d'une liste de valeur. | `text` | — | — |
| **Texte de fermeture**<br />`filter_closetag` | Ceci a été appliqué une fois à la FIN de la liste des contenus. Il est destiné à créer le HTML de fin de la liste des enregistrements, mais plus haut, vous pouvez choisir de le placer comme texte SEPARATION des valeurs aussi. Mais préférez utiliser des paramètres : **Préfixe/Suffixe de chaque contenus** | `text` | — | — |

### Filtres bloqués

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser un filtrage bloqué**<br />`use_persistent_filters` | Filtres qui ne peut pas être remplacée par l'utilisateur, ** Remarque : ** Il peut peut-être caché ou vous pouvez choisir de les afficher (la modification par l'utilisateur sera interdite) | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Valeur des filtres bloqués**<br />`persistent_filters` | Utilisation : field_id ##value%%field_id##%%valeur par exemple 22##14%%47##%%valeur19##unmot pour les plages utiliser field_id##valeur1---valeur2 pour les valeurs multiples utilisent field_id##valeur1+++valeur2+++value3 Remarque : votre champ doit être configuré pour être utiliser comme filtre ou comme multi-valeur sinon les valeurs ne seront pas utilisés comme prévu | `textarea` | — | — |

## Masquer/afficher le module

Ces règles déterminent à quel moment le module sera affichée (donc montré) ou non (donc caché).

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Combinaison des règles**<br />`combine_show_rules` | En fonction des VUES ET/OU des règles d'expression PHP, afin de déterminer si le si le module doit s'afficher ou non. | `radio` | `OR` = OU<br />`AND` = ET | `AND` (ET) |

#### Clients

:::note
Veuillez noter que si la **mise en cache de Joomla** est activée dans **la Configuration globale de Joomla** puis - que l'option '**cache en fonction de la plateforme **' (Notez que 'la tablette' est détecté comme un 'mobile') - ou que la mise en cache de ce module est désactivée à l’intérieur de l'onglet 'Réglage avancé' alors ce paramètre sera ignoré
:::

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

## Avancé

### Mis en cache

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mis en cache**<br />`cache` | Sélectionnez si vous souhaitez mettre en cache le contenu de ce module. | `list` | `0` = Pas de mise en cache | `0` (Pas de mise en cache) |

### CSS / JS

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter css**<br />`add_ccs` | Ajouter le fichier CSS par défaut du module | `radio` | `—` = Utiliser le paramètre du composant<br />`0` = Non<br />`1` = Oui<br />`2` = Liens CSS dans le HTML (permet la capture) | — |
| **Charger le JS Tooltips**<br />`add_tooltips` | Ajouter le script d'infobulles afin d'afficher des informations supplémentaires dans des tooltips en front. | `radio` | `—` = Utiliser le paramètre du composant<br />`0` = Non<br />`1` = Oui | — |

### Conteneur du module

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Suffixe de class CSS**<br />`moduleclass_sfx` | Le suffixe sera ajouté à la classe CSS du module, cela permet d'appliquer un style particulier pour le module. | `text` | — | — |
