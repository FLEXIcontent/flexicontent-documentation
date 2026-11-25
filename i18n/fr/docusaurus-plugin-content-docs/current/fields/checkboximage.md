---
sidebar_position: 9
---

# Case à cocher avec image

Plugin de champ 'Checkbox Image' pour FLEXIcontent

*Plugin : `checkboximage` — Case à cocher avec image*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/checkboximage/checkboximage.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
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
| **Valeurs par colonne**<br />`fields_box_placing` | Économiser de l'espace en autorisant l'affichage par ligne de valeurs multiples | `radio` | `0` = 1<br />`1` = Multiple | `0` (1) |
| **Position Ajouter**<br />`add_position` | Sélectionnez pour ajouter le bouton en ligne (bouton d'ajout de valeur à chaque ligne) ou afficher le bouton d'ajout au fond de la liste de valeurs | `multilist` | `0` = Bouton Ajouter en bas<br />`1` = Bouton ajouter avant<br />`2` = Bouton Ajouter après<br />`3` = Les deux (avant - après) | `3` (Les deux (avant - après)) |

#### Options par valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **max # options**<br />`max_values` | Le nombre maximal d'options qui peuvent être sélectionnées pour chaque valeur du champ | `text` | — | `0` |
| **min # options**<br />`min_values` | Le nombre minimal d'options qui peuvent être sélectionnées pour chaque valeur du champ | `text` | — | `0` |
| **exact # options**<br />`exact_values` | Le nombre exact d'options qui peuvent être sélectionnées pour chaque valeur du champ | `text` | — | `0` |

#### Création des valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Valeurs par défaut**<br />`default_values` | Choisissez les valeurs par défaut ou laissez vide pour aucun. ATTENTION, les valeurs doivent être choisies à partir des éléments de champ VALEURS que vous avez définis ci-dessus. Vous devez fournir une liste séparée par des VIRGULES. | `text` | — | — |
| **Utilisation par défaut**<br />`default_value_use` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |
| **Utiliser une requête SQL**<br />`sql_mode` | Ce mode vous permet de construire la liste de manière dynamique avec des requêtes SQL. Si vous choisissez ce mode, placez votre requête dans les éléments de champ. Il doit renvoyer Colonnes : 'value', 'text' et éventuellement 'image' et 'valgrp', par exemple: SELECT id AS value, name AS text FROM #__users REMARQUE, vous pouvez mettre des remplacements tels que: Données de l’élément : &#123;item-&gt;created_by&#125; &#123;item-&gt;catid&#125; Données du champ : &#123;field-&gt;id&#125; Langue: &#123;curr_userlang_shorttag&#125; &#123;curr_userlang_fulltag&#125; | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Valeurs du champ**<br />`field_elements` | SQL : SELECTIONNER... COMME valeur,... COMME texte,... COMME image,... COMME valgrp Liste d'éléments : valeur1 : :label1::imageFile1:: masterValue1%% valeur2 : :label2::imageFile2::masterValue2%% ... **NOTE 1** : - 'imageFile*' sont des noms de fichiers / classes CSS utilisés seulement par l'image des champs radio/case à cocher - 'masterValue *' sont utilisés si le champ dépend d’un champ maître **NOTE 1** : lors de l’ajout 'masterValue', entrez aussi un 'imageFile', par exemple _NONE_ **NOTE 2** : les noms peuvent être des chaînes de langue (Vous pouvez les ajouter à vos fichiers de langue ou au gestionnaire de substitutions de langue Joomla) | `fcsortablelist` | — | `1::Information::information.png%% 0::Warning::warning.png%%` |

#### Propriétés optionnelles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Etat**<br />`use_elements_state` | Activer pour permettre aux éléments individuels d'être archivés / non publiés / mis à la corbeille, tout en conservant les affectations de valeurs existantes dans les éléments de contenu | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Dépend du champ maître

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Champ maître**<br />`cascade_after` | Lorsque le champ maître change, ce champ chargera les valeurs qui dépendent de la valeur sélectionnée dans le champ maître. Par exemple : le champ maître est « Pays » et ce champ est « Ville » | `fields` | — | — |
| **Sélectionner le message pour le champ maître**<br />`cascade_prompt` | Une invite à demander à l'utilisateur de sélectionner une valeur dans le champ maître, de sorte que ce champ charge les valeurs dépendantes | `text` | — | — |

#### Image / icône

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type**<br />`image_type` | Sélectionnez si 'image' sera un nom de fichier image (par exemple image1.png) ou une classe d'icône de police (par exemple icon-mail, icon-lamp) | `multilist` | `0` = Nom de fichier image<br />`1` = Classe de police | `0` (Nom de fichier image) |
| **Répertoire Images**<br />`imagedir` | Dossier contenant le fichier image | `text` | — | `images/stories/` |
| **Largeur de l’image dans le formulaire**<br />`form_image_width` | — | `text` | — | `1.2em` |
| **Hauteur de l’image dans le formulaire**<br />`form_image_height` | — | `text` | — | `1.2em` |
| **Taille icône**<br />`icon_size_form` | — | `list` | `—` = Taille via les CSS<br />`16` = 16x16<br />`20` = 20x20<br />`24` = 24x24<br />`32` = 32x32<br />`48` = 48x48<br />`64` = 64x64 | — |
| **Couleur icône**<br />`icon_color_form` | — | `fccolor` | — | — |

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
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `multilist` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne<br />`-1` = Comme espace réservé | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |
| **Appliquer une librairie JS**<br />`use_jslib` | \nAutoriser le javascript pour les manipulation / style sur le champ de formulaire, pour permettre un meilleur aspect. par exemple prettyCheckable pour les cases à cocher et plus facile à utiliser par exemple un comportement des liste déroulantes type select2 JS | `multilist` | `0` = Non<br />`2` = prettyCheckable / Select2<br />`3` = Style CSS | `2` (prettyCheckable / Select2) |
| **Valeurs affichées**<br />`form_vals_display` | Sélectionner pour afficher le libellé, l'image ou les deux | `radio` | `0` = Etiquette<br />`1` = Image<br />`2` = Les deux | `1` (Image) |

#### Conseil

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajout message**<br />`usefirstoption` | Activer pour ajouter un texte au champ de formulaire, par exemple pour demander à l'utilisateur de sélectionner une option dans la liste déroulante | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'exemple (par ex. Sélection)**<br />`firstoptiontext` | Texte d'invitation personnalisé **NOTE**: Ce texte est filtré dans la langue afin que vous puissiez entrer une chaîne de caractères remplaçable dans la langue | `text` | — | `FLEXI_PLEASE_SELECT` (- Sélectionner -) |

#### Affichage alternatif

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comme une liste déroulante multiple**<br />`display_as_select` | Dans le formulaire de saisie, le champ sera affiché sous forme de liste à sélection multiple à la place de cases à cocher avec images | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Taille du champ**<br />`size` | Taille du champ dans le formulaire de saisie | `text` | — | `6` |
| **Triable**<br />`sortable` | Autoriser le tri des valeurs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_form` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_form` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Séparateur de valeur formulaire de saisie**<br />`separator` | Choisir le séparateur pour séparer l'ensemble des valeurs dans les formulaires de saisies (placé entre les valeurs) | `list` | `0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | `0` (Espace) |
| **Texte d'ouverture**<br />`opentag_form` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_form` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Valeurs brutes<br />`2` = Valeurs de rendu | `0` (Non) |

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
| **Libellés du filtre de langue**<br />`lang_filter_values` | Applique le filtre de langue JText::_() aux libellés ; ces libellés doivent être des chaînes de langue, ajoutées dans un fichier de langue ou via le gestionnaire de surcharges de langue Joomla | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Affichage Frontend**<br />`text_or_value` | Choisir si vous souhaitez afficher la valeur ou l'étiquette en frontend | `multilist` | `0` = Valeur<br />`1` = Etiquette<br />`2` = Image<br />`3` = Image & Etiquette<br />`4` = Image & Valeur | `2` (Image) |
| **Taille icône**<br />`icon_size` | — | `list` | `—` = Pareil que le formulaire<br />`16` = 16x16<br />`20` = 20x20<br />`24` = 24x24<br />`32` = 32x32<br />`48` = 48x48<br />`64` = 64x64 | — |
| **Couleur icône**<br />`icon_color` | — | `fccolor` | — | — |
| **Afficher les valeurs non sélectionnées**<br />`display_all` | Cela permet l'affichage de toutes les valeurs de champ disponibles (donc les valeurs non sélectionnées), les valeurs non-sélectionnées seront affichées comme désactivées, par exemple, barré dans le texte pour les valeurs de texte (domaines: radio, cases à cocher, sélectionner, selectMultiple, etc) ou avec une faible opacité des valeurs d'image (les champs: radioimage, checkboximage, etc) | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Liste Valeurs

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pré-configuration**<br />`prx_sfx_open_close_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Séparateur de valeurs (vues frontend)**<br />`separatorf` | Choisir le séparateur pour séparer l'ensemble des valeurs dans l'affichage frontend (placé entre les valeurs) | `multilist` | `0` = Espace<br />`1` = Saut de ligne<br />`6` = Ligne Horizontale<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère)<br />`7` = Séparateur personnalisé | `1` (Saut de ligne) |
| **Séparateur personnalisé**<br />`separatorf_custom` | — | `text` | — | — |
| **Texte d'ouverture**<br />`opentag` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

#### Valeurs non-sélectionnées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Le préfixe pour les valeurs non-sélectionnées**<br />`ns_pretext` | Ce texte sera placé immédiatement **après** toutes les valeurs non sélectionnées | `text` | — | — |
| **Suffixe du Texte des valeurs non-sélectionnés**<br />`ns_posttext` | Ce texte sera placé immédiatement**après**chaque valeur de champ non sélectionné | `text` | — | — |

### Plugins de contenu

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Apparence

## Référencement

### Prise en charge des microdonnées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Propriété des microdonnées**<br />`microdata_itemprop` | Sélectionnez une propriété de microdonnées pour caractériser toutes les valeurs de ce champ. Cela permettra aux moteurs de recherche de classer les valeurs de ce champ de manière appropriée, améliorant ainsi le référencement de vos pages | `microdataprops` | — | — |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

#### Filtrer

### Valeurs

#### Créer les options de filtre

:::note
Veuillez faire attention à bien construire votre requête SQL ou la liste d'éléments -- Remarque : la partie 'valeur' pour la requête SQL/la liste d'éléments doit correspondre aux valeurs existantes du champ
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Récupération personnalisé des valeurs du filtre**<br />`filter_customize_options` | Définissez si vous souhaitez utiliser toutes les valeurs pour le filtre, ou construire une liste de valeurs spécifiques à partir d'une requête SQL/ liste d'éléments | `multilist` | `0` = Non, utiliser toutes les valeurs (par défaut)<br />`1` = Utiliser une requête personnalisée<br />`2` = Utiliser des valeurs personnalisées | `0` (Non, utiliser toutes les valeurs (par défaut)) |
| **Liste d'éléments ou requête SQL personnalisée**<br />`filter_custom_options` | Éléments personnalisés ou une requête SQL. Pour les **éléments personnalisés**, la syntaxe est la suivante : valeur1 : :label1%% value2: :label2%% Pour une**requête SQL**, entrez : SELECT value, value as text FROM #__flexicontent_fields_item_relations WHERE field_id='&#123;field_id&#125;' AND value != '' GROUP BY value **Vous pouvez utiliser des valeurs de remplacement** : pour des données du champ actuel : &#123;field-&gt;id&#125; &#123;field-&gt;field_type&#125; et pour des données du contenu : &#123;item-&gt;created_by&#125; &#123;item-&gt;catid&#125; etc. **NOTE** : Les noms seront transmises par le biais de JText... pour permettre la prise en charge multilingue (vous pouvez les ajouter à vos fichiers de langue) _SELECT value, value as text FROM #__flexicontent_fields_item_relations WHERE field_id='&#123;field-&gt;id&#125;' AND value != '' GROUP BY value_ | `textarea` | — | — |

#### Comparaison des valeurs de filtre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comparaison des valeurs de filtre**<br />`filter_compare_type` | Valeurs de filtrage qui peuvent être comparées de manière alphanumérique ou numérique (entier / à virgule flottante) | `radio` | `0` = Alphanumérique<br />`1` = Entier<br />`2` = Virgule flottante | `0` (Alphanumérique) |

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
| **Valeurs affichées**<br />`filter_vals_display` | Sélectionner pour afficher le libellé, l'image ou les deux | `multilist` | `0` = Etiquette<br />`1` = Image<br />`2` = Les deux | `0` (Etiquette) |
| **Taille icône**<br />`icon_size_filter` | — | `list` | `—` = Pareil que le formulaire<br />`16` = 16x16<br />`20` = 20x20<br />`24` = 24x24<br />`32` = 32x32<br />`48` = 48x48<br />`64` = 64x64 | — |
| **Couleur icône**<br />`icon_color_filter` | — | `fccolor` | — | — |
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
| **Valeurs affichées**<br />`filter_vals_display_s` | Sélectionner pour afficher le libellé, l'image ou les deux | `multilist` | `0` = Etiquette<br />`1` = Image<br />`2` = Les deux | `0` (Etiquette) |
| **Taille icône**<br />`icon_size_filter_s` | — | `list` | `—` = Pareil que le formulaire<br />`16` = 16x16<br />`20` = 20x20<br />`24` = 24x24<br />`32` = 32x32<br />`48` = 48x48<br />`64` = 64x64 | — |
| **Couleur icône**<br />`icon_color_filter_s` | — | `fccolor` | — | — |
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
