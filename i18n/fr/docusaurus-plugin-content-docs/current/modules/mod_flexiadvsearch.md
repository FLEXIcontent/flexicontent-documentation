---
sidebar_position: 4
---

# Recherche avancée

FLEXIcontent fournit six modules frontend pour afficher des contenus, des catégories, des formulaires de recherche, des filtres, des cartes et des nuages d’étiquettes. Configurez un module depuis **Extensions → Modules**.

> Ce module affiche un formulaire de recherche simple qui est en lien avec la vue recherche de FLEXIcontent

:::info Source
Cette page est générée depuis `modules/mod_flexiadvsearch/mod_flexiadvsearch.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

### Template du module

:::note
Veuillez définir les paramètres de disposition dans l’onglet **Disposition : ...**. Les développeurs CSS/HTML doivent consulter : ** Guide des modèles personnalisés **
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Template**<br />`layout` | Choisir la mise en page de votre module | `fclayout` | — | `news` |

### Lien menu pour la vue recherche (contient la configuration de vue de recherche)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Forcer l'ItemID du menu**<br />`itemid_force` | Cette option permet de forcer pour l'ensemble des liens des contenus. Vous pouvez utiliser celui de la page active, un celui d'un menu spécifique | `multilist` | `0` = Défaut (configuration du composant)<br />`1` = Personnalisé (en-dessous) | `0` (Défaut (configuration du composant)) |
| **Personnalisation par l'ID du menu**<br />`itemid_force_value` | Personnalisation par l'ID du menu | `text` | — | — |

### Paramètres de base

#### Champ de recherche texte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Taille (# de caractères)**<br />`search_inner_width` | Taille du champ de texte Recherche en nombre de caractères | `text` | — | `20` |
| **Message intérieur (si vide)**<br />`search_inner_prompt` | Ceci est le texte à afficher à l’intérieur du champ de recherche de texte comme exemple d'information à saisir. **NOTE**: il peut s’agir d’une chaîne de langue | `text` | — | `FLEXI_ADV_MOD_SEARCH_PROMPT` (Rechercher...) |

#### Bouton envoyer (envoyer)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Montrer**<br />`button` | Affiche un bouton go /recherche (envoyer), sinon l'utilisateur ne pourra seulement soumettre en cliquant entrer dans le champ de recherche de texte | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Classe CSS**<br />`flexi_button_class_go` | Classe pour le bouton re-initialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | `multilist` | `-1` = - Personnalisé -<br />`btn` = Plein<br />`btn btn-primary` = Principale<br />`btn btn-success` = Succès<br />`btn btn-info` = Info<br />`btn btn-warning` = Avertissement<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn btn-success` (Succès) |
| **Classe personnalisée**<br />`flexi_button_class_go_custom` | Ajouter une classe personnalisée pour le bouton Chance, exemple uk-button uk-button-large pour un template Warp7 | `text` | — | — |
| **Position**<br />`button_pos` | Position du bouton de recherche en fonction de la zone de saisie | `radio` | `right` = A droite<br />`left` = A gauche<br />`top` = En haut<br />`bottom` = En bas | `right` (A droite) |
| **Bouton comme**<br />`button_as` | Affiche le bouton sous forme de texte ou une image. **NOTE**: définissez un chemin d’accès de l’image relatif au dossier Joomla | `multilist` | `0` = Texte<br />`1` = Image | `0` (Texte) |
| **chemin de l'image**<br />`button_image` | chemin de l'image | `text` | — | — |
| **Texte**<br />`button_text` | Lorsque le bouton Go est un texte **NOTE **: Cela peut être une chaîne de langue** | `text` | — | `FLEXI_ADV_MOD_GO` (C'est parti) |

#### Formulaire de recherche : types de contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les étiquettes**<br />`show_type_label` | Vous pouvez cacher ou afficher l'étiquette dans la recherche de type de contenu | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Afficher | — |
| **Types recherchables (ne rien sélectionner pour TOUS)**<br />`contenttypes` | Les types de contenu inclus dans la recherche, ne rien sélectionner inclut TOUS les types. Remarque : Vous pouvez autoriser l’utilisateur à sélectionner les types de contenu. Si vous l’autorisez, la liste de sélection sera LIMITÉE aux types indiqués ici | `types` | — | — |
| **Autoriser la sélection par l’utilisateur**<br />`canseltypes` | Autoriser les utilisateurs à sélectionner les types de contenu à inclure dans leur recherche | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Formulaire de recherche : options avancées

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
| **Champs (laisser vide pour TOUS)**<br />`txtflds` | Remarque : seuls les champs marqués comme recherchables dans l’index avancé sont listés | `filters` | — | — |

#### Zones de recherche (contenus non-FC)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser les zones**<br />`show_searchareas` | Autoriser l’utilisateur à sélectionner et rechercher d’autres zones du site, par exemple les liens web, les contacts utilisateur, etc. | `multilist` | `0` = Désactiver<br />`1` = Activer, afficher le sélecteur | `0` (Désactiver) |
| **Zones de recherche**<br />`searchareas` | Zones de recherche du site (contenus non-FC) incluses dans la recherche. Remarque : si l’utilisateur peut sélectionner les zones de recherche, la liste sera LIMITÉE aux zones sélectionnées ici | `radio` | `—` = Tous | — |
| **Afficher le tri**<br />`show_searchordering` | Autoriser les utilisateurs du frontend à choisir le tri des résultats des autres zones du site. REMARQUE : ce tri est différent de celui utilisé pour les contenus principaux. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeur par défaut**<br />`default_searchordering` | Tri par défaut des résultats de recherche | `radio` | `newest` = Les plus récents en premier<br />`oldest` = Les plus anciens en premier<br />`popular` = Les plus populaires<br />`alpha` = Ordre Alphabétique<br />`category` = Section/Catégorie | `newest` (Les plus récents en premier) |

#### Bouton Chance (aller au premier résultat)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher**<br />`direct_button` | Afficher un bouton direct / j'ai de la chance | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Classe CSS**<br />`flexi_button_class_direct` | Classe pour le bouton re-initialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | `multilist` | `-1` = - Personnalisé -<br />`btn` = Plein<br />`btn btn-primary` = Principale<br />`btn btn-success` = Succès<br />`btn btn-info` = Info<br />`btn btn-warning` = Avertissement<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn` (Plein) |
| **Classe personnalisée**<br />`flexi_button_class_direct_custom` | Ajouter une classe personnalisée pour le bouton Chance, exemple uk-button uk-button-large pour un template Warp7 | `text` | — | — |
| **Poste**<br />`direct_pos` | Position du bouton de recherche en fonction de la zone de saisie | `radio` | `right` = Droite<br />`left` = Gauche<br />`top` = Haut<br />`bottom` = Bas | `right` (Droite) |
| **Bouton comme**<br />`direct_as` | Affiche le bouton sous forme de texte ou une image. **NOTE**: définissez un chemin d’accès de l’image relatif au dossier Joomla | `multilist` | `0` = Texte<br />`1` = Image | `0` (Texte) |
| **Chemin de l'image**<br />`direct_image` | Chemin de l'image | `text` | — | — |
| **Texte**<br />`direct_text` | Lorsque le bouton Chance est un texte **NOTE **: Cela peut être une chaîne de langue | `text` | — | `FLEXI_ADV_MOD_DIRECT` (Chance) |

#### Lien vers la vue Recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le lien**<br />`link_to_advsearch` | Activer cette option pour afficher un lien direct vers (FLEXIcontent) la vue recherche avancée | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte du lien**<br />`link_to_advsearch_txt` | Le texte qui sera le lien vers (FLEXIcontent) la vue recherche avancée | `text` | — | `FLEXI_ADV_MOD_OPEN_DETAILED_SEARCH` (Ouvrir la recherche détaillée) |
| **Classe CSS**<br />`flexi_button_class_advanced` | Classe pour le bouton re-initialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | `multilist` | `-1` = - Personnalisé -<br />`btn` = Plein<br />`btn btn-primary` = Principale<br />`btn btn-success` = Succès<br />`btn btn-info` = Info<br />`btn btn-warning` = Avertissement<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | `btn` (Plein) |
| **Classe personnalisée**<br />`flexi_button_class_advanced_custom` | Ajouter une classe personnalisée pour le bouton Chance, exemple uk-button uk-button-large pour un template Warp7 | `text` | — | — |
| **Position**<br />`link_to_advsearch_pos` | Position du bouton de recherche en fonction de la zone de saisie | `radio` | `right` = A droite<br />`left` = A gauche<br />`top` = En haut<br />`bottom` = En bas | `right` (A droite) |

## Autocomplétion de la recherche Flexi

Description de l’autocomplétion de la recherche

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser la subggestion automatique**<br />`search_autocomplete` | Choisissez d'utiliser le mode mots-tag comme l'auto-suggestion, ou un seul mot simple ou désactiver | `radio` | `0` = Non<br />`1` = Simple<br />`2` = Mots clés | `1` (Simple) |
| **Largeur de la liste déroulante de l’autocomplétion**<br />`search_ac_dropdown_width` | Description de la largeur de la liste déroulante de l’autocomplétion | `text` | — | — |

#### Autocomplétion enrichie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer l’autocomplétion enrichie**<br />`search_ac_rich` | Description de l’activation de l’autocomplétion enrichie | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Source de l’image de l’autocomplétion**<br />`search_ac_image_source` | Description de la source de l’image de l’autocomplétion | `multilist` | `auto` = Automatique<br />`field` = Champ image<br />`type` = Utiliser les paramètres du type | `auto` (Automatique) |
| **Libellé du champ image de l’autocomplétion**<br />`search_ac_image_field` | Champ image lbl description | `fields` | — | — |
| **Largeur de l’image de l’autocomplétion**<br />`search_ac_image_width` | Description de la largeur de l’image de l’autocomplétion | `number` | — | `60` |
| **Hauteur de l’image de l’autocomplétion**<br />`search_ac_image_height` | Description de la hauteur de l’image de l’autocomplétion | `number` | — | `60` |
| **Méthode de l’image de l’autocomplétion**<br />`search_ac_image_method` | Description de la méthode de l’image de l’autocomplétion | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |
| **Position de l’image de l’autocomplétion**<br />`search_ac_image_position` | Description de la position de l’image de l’autocomplétion | `radio` | `left` = A gauche<br />`right` = A droite | `left` (A gauche) |
| **Longueur maximale du titre de l’autocomplétion**<br />`search_ac_title_maxlen` | Description de la longueur maximale du titre de l’autocomplétion | `number` | — | `60` |
| **Source des informations de l’autocomplétion**<br />`search_ac_info_source` | Description de la source des informations de l’autocomplétion | `multilist` | `module` = Module<br />`type` = Utiliser les paramètres du type | `module` (Module) |
| **Champs d’information de l’autocomplétion**<br />`search_ac_info_fields` | Description des champs d’information de l’autocomplétion | `fields` | — | — |
| **Libellés d’information de l’autocomplétion**<br />`search_ac_info_labels` | Description des libellés d’information de l’autocomplétion | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Longueur maximale des informations de l’autocomplétion**<br />`search_ac_info_maxlen` | Description de la longueur maximale des informations de l’autocomplétion | `number` | — | `80` |

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
| **Mis en cache**<br />`cache` | Sélectionnez si vous souhaitez mettre en cache le contenu de ce module. | `list` | `1` = Paramètres globaux<br />`0` = Pas de mise en cache | `1` (Paramètres globaux) |
| **Temps de mise en cache**<br />`cache_time` | Temps avant que le module soit remis en cache. | `text` | — | `900` |

### CSS / JS

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter css**<br />`add_ccs` | Ajouter le fichier CSS par défaut du module | `radio` | `—` = Utiliser le paramètre du composant<br />`0` = Non<br />`1` = Oui<br />`2` = Liens CSS dans le HTML (permet la capture) | — |
| **Charger le JS Tooltips**<br />`add_tooltips` | Ajouter le script d'infobulles afin d'afficher des informations supplémentaires dans des tooltips en front. | `radio` | `—` = Utiliser le paramètre du composant<br />`0` = Non<br />`1` = Oui | — |

### Conteneur du module

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Suffixe de class CSS**<br />`moduleclass_sfx` | Le suffixe sera ajouté à la classe CSS du module, cela permet d'appliquer un style particulier pour le module. | `text` | — | — |
