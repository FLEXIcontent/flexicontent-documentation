---
sidebar_position: 39
---

# Lien web

Plugin de champ 'Weblink' pour FLEXIcontent

*Plugin : `weblink` — Lien web*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/weblink/weblink.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
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
| **Nb maximum de valeurs**<br />`max_values` | Définissez ici le nombre maximum de valeurs que l'utilisateur pourra saisir. 0 pour illimité. | `text` | — | `0` |
| **Valeurs par colonne**<br />`fields_box_placing` | Économiser de l'espace en autorisant l'affichage par ligne de valeurs multiples | `radio` | `0` = 1<br />`1` = Multiple | `1` (Multiple) |
| **Position Ajouter**<br />`add_position` | Sélectionnez pour ajouter le bouton en ligne (bouton d'ajout de valeur à chaque ligne) ou afficher le bouton d'ajout au fond de la liste de valeurs | `multilist` | `0` = Bouton Ajouter en bas<br />`1` = Bouton ajouter avant<br />`2` = Bouton Ajouter après<br />`3` = Les deux (avant - après) | `3` (Les deux (avant - après)) |

#### Création des valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Code du lien**<br />`link_source` | (Compatibilité avec le gestionnaire d'article Joomla) - Sélectionner si ce champ permet de modifier ou d'afficher les liens d'articles Joomla | `multilist` | `-1` = Liens des articles Joomla<br />`0` = Plugin de champ 'Weblink' pour FLEXIcontent | `0` (Plugin de champ 'Weblink' pour FLEXIcontent) |
| **Lien par Défaut**<br />`default_link` | Vous pouvez sélectionner à afficher du texte à afficher par défaut dans la zone de texte du lien (non recommandé) | `text` | — | — |
| **Utilisation du lien par défaut**<br />`link_usage` | Sélectionner lorsque vous souhaitez ajouter un lien par défaut | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |
| **Autorise les adresses relatives**<br />`allow_relative_addrs` | Autoriser les utilisateurs à saisir une adresse relative. Lorsque cette option est désactivé et qu'il n'y a pas de protocol de saisie , http:// sera automatiquement ajouté. | `multilist` | `0` = Non<br />`1` = Oui<br />`2` = L'utilisateur peut choisir | `0` (Non) |

#### Création automatique de valeur

:::note
Version Flexicontent PRO uniquement
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Valeur automatique**<br />`auto_value` | Activer pour créer automatiquement la valeur de ce champ lors de l'enregistrement du formulaire d'élément. Dans certains cas, vous pouvez activer l'option de masquer ce champ dans le frontend ou backend ou dans les deux formulaires d'élément | `multilist` | `0` = Non<br />`2` = Utiliser du code personnalisé | `0` (Non) |
| **Code personnalisé**<br />`auto_value_code` | Entrez le code PHP à utiliser pour créer la valeur personnalisée, veuillez vider ce champs et enregistrez pour charger l'exemple par défaut, puis personnaliser | `editor` | — | `fields; if ( !isset($F['fieldname01']) ) return array('fieldname01 field not found'); $vals = array(); foreach($F['fieldname01']-&gt;postdata as $i =&gt; $v) &#123; $vals[$i] = 'Auto : ' . $v; &#125; return $vals;` |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage des champs**<br />`formlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/field_*. hp comme field_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Bouton Étendre**<br />`show_values_expand_btn` | Afficher un bouton pour agrandir la largeur des champs pour faciliter l'édition. NOTE : certaines mises en page comme 'table' peuvent ne pas prendre en charge ce bouton, le bouton ne sera pas affiché | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Affichage d'un formulaire simple**<br />`simple_form_layout` | (Pour les mises en page autres que les tableaux) Ceci affichera les libellés au-dessus des champs de formulaire. Dans le cas de champs de saisie vides les étiquettes deviennent également un espace réservé qui ne passe à sa place qu'après le focus ou après la saisie. Les bordures sont également supprimées | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Lien

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Longueur maximum du texte**<br />`maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | `4000` |
| **Taille du champ**<br />`size` | Taille du champ dans le formulaire de saisie | `text` | — | `30` |
| **Attributs du champ**<br />`extra_attributes` | Saisir ici quelques attributs supplémentaires (paramètres de balises HTML) pour le champ de formulaire comme par exemple onkeypress="" onmouseover="..." somename="somevalue". Veillez à ne pas briser la syntaxe HTML du champ de formulaire | `text` | — | — |
| **Masque de saisie des valeurs & Validation**<br />`inputmask` | Paramètres à la fois pour le masque et la validation des entrées utilisateur | `multilist` | `—` = Non<br />`url` = Oui | — |

### Propriétés optionnelles

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_image` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui, n'importe lequel<br />`2` = Oui, spécifique | `0` (Non) |
| **Par défaut**<br />`default_image` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `media` | — | — |
| **Utilisation par défaut**<br />`image_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |
| **Images précises**<br />`image_choices` | — | `subform` | — | — |

#### Titre du lien survolé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_title` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Par défaut**<br />`default_title` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`title_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### Texte du lien

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_text` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Par défaut**<br />`default_text` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`text_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### Type d'adresse

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_addrtype` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`2` = Oui | `0` (Non) |
| **Choix sélectionné**<br />`addrtype_choices` | Entrez les choix de sélection déroulante, la syntaxe est la suivante : valeur1 ::label1%% valeur2 ::label2%% | `textarea` | — | — |

#### Class CSS

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_class` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui, en tant que saisie de texte<br />`2` = Sélectionnez, oui | `0` (Non) |
| **Par défaut**<br />`default_class` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`class_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |
| **Choix sélectionné**<br />`class_choices` | Entrez les choix de sélection déroulante, la syntaxe est la suivante : valeur1 ::label1%% valeur2 ::label2%% | `textarea` | — | — |

#### ID de la balise

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_id` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Par défaut**<br />`default_id` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`id_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### Fenêtre-cible

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_target` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Visites

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_hits` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

### Importation

#### Manipuler les valeurs lors de l'importation

:::note
Version Flexicontent PRO uniquement
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Remapper les valeurs**<br />`import_fv_remap_mode` | Activer pour changer certaines valeurs importées en d'autres valeurs. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Remappages de valeur**<br />`import_fv_remap` | Format des données importValue1::realValue1%% importValue2::realValue2%% importValue3::realValue3%% | `textarea` | — | — |
| **Manipulation des valeurs**<br />`import_fv_ccode_mode` | Exécuter des méthodes personnalisées pour manipuler les valeurs de champ | `multilist` | `0` = Non<br />`2` = Utiliser du code personnalisé | `0` (Non) |
| **Code personnalisé**<br />`import_fv_ccode` | Entrez le code PHP à utiliser pour créer la valeur personnalisée, veuillez vider ce champs et enregistrez pour charger l'exemple par défaut, puis personnaliser | `editor` | — | `parameters-&gt;get('some_param'); foreach($values as $i =&gt; $v) &#123; $values[$i] = 'Example ' . $i . ' : ' . $v; &#125; return $values;` |

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `multilist` | `0` = Non<br />`1` = Valeurs brutes<br />`2` = Valeurs de rendu | `0` (Non) |
| **Supprimer html**<br />`csv_strip_html` | — | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

:::note
&#123;&#123;title&#125;&#125; &#123;&#123;link&#125;&#125;
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Personnalisé**<br />`csv_export_text` | — | `textarea` | — | `&#123;&#123;title&#125;&#125; &#123;&#123;link&#125;&#125;` |

#### FLEXI_BACKEND_VIEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_BACKEND_VIEW_APPEARANCE**<br />`backend_view_appearance` | FLEXI_BACKEND_VIEW_APPEARANCE_DESC | `multilist` | `0` = Par défaut<br />`1` = FLEXI_CHECK_MARK<br />`2` = FLEXI_CLEAN_HTML_AND_TRIM | `0` (Par défaut) |
| **FLEXI_TRIM_LENGTH**<br />`backend_view_trim_chars` | FLEXI_TRIM_LENGTH_DESC | `text` | — | `100` |

### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |

#### Valeurs affichées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher un message aucune valeur**<br />`show_no_value` | Afficher un message qui sera affichée pour les champs qui ne possèdent aucune valeur saisie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Message aucune valeur**<br />`no_value_msg` | Le texte qui sera affiché lorsque le champ ne possède aucune valeur, laisser vide pour afficher le message par défaut | `text` | — | — |

:::note
Note : la nouvelle fenêtre forcera un lien de type externe
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Cible par défaut du lien**<br />`target` | Sélectionnez la fenêtre cible par défaut du lien qui n’ont pas déjà une cible (via le formulaire de contenu) | `list` | `—` = - Pas de cible -<br />`_blank` = Nouvelle fenêtre/onglet<br />`_parent` = Fenêtre Parente<br />`_self` = Même fenêtre/onglet<br />`_top` = Haut de fenêtre<br />`_popup` = FLEXI_FIELD_LINK_JS_POPUP_BOX<br />`_modal` = FLEXI_FIELD_LINK_SINGLE_WIN | — |
| **Utiliser le lien direct**<br />`use_direct_link` | Ajouter des liens directs dans les URL, notez que cela désactivera le comptage. Normalement un lien indirect de sortie vers votre site web est sortie afin d'obtenir la véritable URL et également comptabiliser les accès. | `radio` | `0` = Non<br />`1` = Oui (désactive le compteur de clic) | `0` (Non) |
| **Ajouter rel-nofollow**<br />`add_rel_nofollow` | Ajoute rel=nofollow sur le lien, ce qui indique aux moteurs de recherche de ne pas l'indexé | `radio` | `0` = Oui, empêcher l'indexation des liens externes<br />`1` = Oui, empêcher l'indexation<br />`-1` = Non, autoriser l'indexation de tous les liens (!!!) | `0` (Oui, empêcher l'indexation des liens externes) |
| **Afficher les résultats**<br />`display_hits` | Afficher le nombre de hits ou de téléchargements pour chaque valeur du champ. | `radio` | `0` = Non<br />`1` = Icône<br />`2` = Texte<br />`3` = Les deux | `0` (Non) |

:::note
Image
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Montrer**<br />`display_image` | Afficher l’image si une image a été associée à l’URL | `multilist` | `0` = Non<br />`1` = Oui<br />`2` = Oui, masquer le texte du lien | `1` (Oui) |
| **Largeur de l'image**<br />`image_w` | — | `text` | — | `320` |
| **Hauteur de l'image**<br />`image_h` | — | `text` | — | `240` |

:::note
URL de vidéos
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comportement**<br />`playback_videos` | Lecture les URL vidéo au lieu d’ouvrir l’URL | `radio` | `0` = Lien<br />`1` = Lecture | `1` (Lecture) |

### Liste Valeurs

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pré-configuration**<br />`prx_sfx_open_close_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage) | — |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

:::note
Remarque : Les textes d'ouvertures et de fermetures ainsi que les texte de séparations de valeurs ne seront pas utiliser dans champ de type groupe
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Séparateur de valeurs (vues frontend)**<br />`separatorf` | Choisir le séparateur pour séparer l'ensemble des valeurs dans l'affichage frontend (placé entre les valeurs) | `multilist` | `0` = Espace<br />`1` = Saut de ligne<br />`6` = Ligne Horizontale<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère)<br />`7` = Séparateur personnalisé | `1` (Saut de ligne) |
| **Séparateur personnalisé**<br />`separatorf_custom` | — | `text` | — | — |
| **Texte d'ouverture**<br />`opentag` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

### Plugins de contenu

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Apparence

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Champ formulaire

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `1` = Texte à Rechercher | `0` |
