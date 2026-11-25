---
sidebar_position: 6
---

# Adresse internationale / Google Maps

Ce champ ajoute les informations d'adresse aux éléments. Inclut des champs détaillés pour adresse rue, ville, état/province, code postal/zip et pays. Dans le cas des adresses aux États-Unis, il comprend une liste déroulante des États. Il a une fonction de géo-localisation en javascript qui obtient la latitude et la longitude de l'adresse en utilisant l'API Google Map pour le stockage dans la BD. Dans le frontend, il affiche automatiquement uniquement les champs qui contiennent des données, avec une image de Google Map de l'emplacement avec un marqueur. La configuration du champ a plusieurs options pour contrôler l'affichage dans l'interface.

*Plugin : `addressint` — Adresse internationale / Google Maps*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/addressint/addressint.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
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
| **Valeurs par colonne**<br />`fields_box_placing` | Économiser de l'espace en autorisant l'affichage par ligne de valeurs multiples | `radio` | `0` = 1<br />`1` = Multiple | `0` (1) |
| **Position Ajouter**<br />`add_position` | Sélectionnez pour ajouter le bouton en ligne (bouton d'ajout de valeur à chaque ligne) ou afficher le bouton d'ajout au fond de la liste de valeurs | `multilist` | `0` = Bouton Ajouter en bas<br />`1` = Bouton ajouter avant<br />`2` = Bouton Ajouter après<br />`3` = Les deux (avant - après) | `3` (Les deux (avant - après)) |

#### Création des valeurs

#### Limite de la recherche

:::note
Type
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Défaut**<br />`ac_types_default` | Sélectionner le type de recherche qui sera utilisé lors de la création d'une nouvelle adresse | `radio` | `—` = Tous<br />`geocode` = Localisation géographique<br />`address` = Adresse exacte<br />`establishment` = Lieu de l'entreprise<br />`(regions)` = Région<br />`(cities)` = Ville ou Province | — |
| **Sélection utilisateur**<br />`ac_type_allowed_list` | Sélectionner les types d’autocomplétion autorisés pour l’utilisateur | `fccheckbox` | — | — |

:::note
Pays
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Défaut**<br />`ac_country_default` | Sélectionner le pays qui sera utilisé par défaut lors de la génération de l'adresse | `fccountries` | — | — |
| **Pays autorisés (aucun = Tout)**<br />`ac_country_allowed_list` | Certains Pays peuvent être autorisés pour la recherche et la sélection. Laisser vide pour autorisé tous les pays | `fccountries` | — | — |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |
| **PLG_FLEXICONTENT_FIELDS_ADDRESSINT_FORM_CARD_WIDTH**<br />`form_card_width` | PLG_FLEXICONTENT_FIELDS_ADDRESSINT_FORM_CARD_WIDTH_DESC | `text` | — | `600` |

#### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage des champs**<br />`formlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/field_*. hp comme field_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Edition Lat/Lon**<br />`edit_latlon` | Sélectionner sir la lattitude et la longitude peuvent être édités | `radio` | `0` = Non<br />`2` = Lecture seule<br />`1` = Oui | `1` (Oui) |
| **Mode d'édition de l'adresse**<br />`addr_edit_mode` | Sélectionne le mode d'édition pour l'adresse . mode texte : utilise champ d'affichage d'adresse seulement. Mode formaté : montre les différent champ composant d'une adresse de sorte qu'ils puissent être modifiés individuellement ( rue, ville, état , etc.) | `multilist` | `plaintext` = Texte simple<br />`formatted` = Mode formaté | `plaintext` (Texte simple) |
| **Type de carte**<br />`map_type` | Sélectionnez le type de carte à afficher | `radio` | `roadmap` = Mode rue<br />`satellite` = Mode satellite<br />`hybrid` = Hybride<br />`terrain` = Relief | `roadmap` (Mode rue) |
| **Zoom par défaut de la carte**<br />`map_zoom` | Sélectionnez le niveau de zoom pour l'image de carte et le zoom initial de la carte interactive. Lors de l'édition d'un article, le niveau de zoom est enregistré et utilisé pour l'affichage. | `list` | `1` = 1 - Monde<br />`2` = 2<br />`3` = 3<br />`4` = Par continent<br />`5` = 5<br />`6` = 6<br />`7` = 7 - Pays<br />`8` = 8<br />`9` = 9<br />`10` = 10 - Région<br />`11` = 11<br />`12` = 12<br />`13` = 13 - Ville<br />`14` = 14<br />`15` = 15<br />`16` = 16 - Voisin<br />`17` = 17<br />`18` = 18<br />`19` = 19 - Rue<br />`20` = 20<br />`21` = 21 | `16` (16 - Voisin) |

:::note
Veuillez noter - Les boutons 'Modifier' et 'Ignorer' seront affichés pour chaque valeur, si le champ **n'est pas requis** - Au moins 1 propriété sera forcée d'être requise, si le champ **est obligatoire** sans les propriétés requises
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Options obligatoires**<br />`required_props_plaintext` | Sélectionnez les propriétés individuelles que vous souhaitez voir requises. Cela affecte chaque \"valeur\" individuelle du champ. | `list` | `address` = Adresse<br />`latitude` = Latitude<br />`longitude` = Longitude | — |
| **Options obligatoires**<br />`required_props` | Sélectionnez les propriétés individuelles que vous souhaitez voir requises. Cela affecte chaque \"valeur\" individuelle du champ. | `list` | `business_location` = Entreprise / lieu<br />`street_address` = Adresse postale<br />`city` = Ville<br />`us_state` = Etat Américain<br />`non_us_state_province` = Pays (Hors USA)<br />`zip_postal_code` = Code postal<br />`country` = Pays<br />`latitude` = Latitude<br />`longitude` = Longitude | — |

#### Propriétés optionnelles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Entreprise / nom de l'emplacement**<br />`use_name` | Activez cette option si vous êtes la recherche d'entreprises ou si vous souhaitez utiliser des titres pour vos adresses | `radio` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |
| **Etat Américain**<br />`use_usstate` | Afficher ou masquer la liste des états américains lors de l'édition en mode formaté | `radio` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |
| **Région**<br />`use_province` | Afficher ou masquer le champ province lors de l'édition en mode formaté | `radio` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |
| **Pays**<br />`use_country` | Afficher ou masquer lla liste des pays lors de l'édition en mode formaté | `multilist` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |

#### Icône Marqueur

:::note
Remarque : Les marqueurs personnalisés ne sont affichés que si vous utilisez la \"Carte interactive\". (Définissez ceci dans l'onglet Affichage/Onglet Disposition)
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Marqueur personnalisé**<br />`use_custom_marker` | Permettre à l'utilisateur de sélectionner un marqueur d'icône personnalisé | `multilist` | `0` = Désactiver<br />`1` = Activer | `0` (Désactiver) |
| **Dossier des marqueurs**<br />`custom_marker_path` | — | `text` | — | `modules/mod_flexigooglemap/assets/marker` |
| **Marqueur par défaut**<br />`default_marker_file` | Icône par défaut à présélectionner dans le sélecteur d'icône de marqueur _e.g. icon-blue.png_ | `text` | — | — |
| **PLG_FLEXICONTENT_FIELDS_ADDRESSINT_SHOW_MARKER_ANCHOR**<br />`show_marker_anchor` | PLG_FLEXICONTENT_FIELDS_ADDRESSINT_SHOW_MARKER_ANCHOR_DESC | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Données manuelles (non remplies automatiquement lors de la recherche)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Code postal/ ZIP suffixe**<br />`use_zip_suffix` | Afficher ou masquer le champ code postal lors de l'édition en mode formaté | `radio` | `0` = Désactiver<br />`1` = Activer | `0` (Désactiver) |
| **Adresse ligne 2**<br />`use_addr2` | Afficher ou masquer la 2ème ligne pour l'adresse lors de l'édition en mode formaté | `radio` | `0` = Désactiver<br />`1` = Activer | `0` (Désactiver) |
| **Adresse ligne 3**<br />`use_addr3` | Afficher ou masquer la 3ème ligne pour l'adresse lors de l'édition en mode formaté | `radio` | `0` = Désactiver<br />`1` = Activer | `0` (Désactiver) |

#### Configuration de la carte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur (px)**<br />`map_width_form` | Largeur de la carte en pixel | `text` | — | `350` |
| **Hauteur (px)**<br />`map_height_form` | Hauteur de la carte en pixel | `text` | — | `250` |

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
| **Personnalisé**<br />`csv_export_text` | Utiliser &#123;&#123;addr_display&#125;&#125; &#123;&#123;addr_formatted&#125;&#125; &#123;&#123;addr1&#125;&#125; &#123;&#123;city&#125;&#125; &#123;&#123;zip&#125;&#125; &#123;&#123;lat&#125;&#125; &#123;&#123;lon&#125;&#125; &#123;&#123;url&#125;&#125; &#123;&#123;zoom&#125;&#125; &#123;&#123;name&#125;&#125; &#123;&#123;addr2&#125;&#125; &#123;&#123;addr3&#125;&#125; &#123;&#123;state&#125;&#125; &#123;&#123;country&#125;&#125; &#123;&#123;province&#125;&#125; &#123;&#123;zip_suffix&#125;&#125; | `textarea` | — | `&#123;&#123;addr1&#125;&#125; &#123;&#123;city&#125;&#125; ZIP: &#123;&#123;zip&#125;&#125;` |

#### FLEXI_BACKEND_VIEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_BACKEND_VIEW_APPEARANCE**<br />`backend_view_appearance` | FLEXI_BACKEND_VIEW_APPEARANCE_DESC | `multilist` | `0` = Par défaut<br />`1` = FLEXI_CHECK_MARK<br />`2` = FLEXI_CLEAN_HTML_AND_TRIM | `0` (Par défaut) |
| **FLEXI_TRIM_LENGTH**<br />`backend_view_trim_chars` | FLEXI_TRIM_LENGTH_DESC | `text` | — | `100` |

### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |

#### Configuration de l'adresse

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher adresse**<br />`show_address` | Sélectionner si vous voulez afficher l'adresse | `multilist` | `0` = Jamais<br />`category` = Vue catégorie uniquement<br />`item` = Vue d'article uniquement<br />`both` = Toujours | `both` (Toujours) |
| **Mode d'affichage de l'adresse**<br />`addr_display_mode` | Sélectionne le mode d'affichage pour l'adresse . mode texte : affiche l'adresse dans un seul champ. Mode formaté : montre les différent champ composant d'une adresse sous format html ( rue, ville, état , etc.) | `multilist` | `plaintext` = Texte simple<br />`formatted` = Mode formaté | `plaintext` (Texte simple) |

:::note
Laissez vide pour charger les valeurs par défaut
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Format de l'adresse**<br />`addr_format_tmpl` | Définit le modèle de format HTML lorsque le mode d'affichage est Formaté. Pour entrer les valeurs de champ utilisé &#123;&#123;fieldname&#125;&#125;. Pour un affichage conditionel, uniquement si la valeur n'est pas vide, utilisez [[fieldname\|output]]. Les options valides sont : nam, addr1, addr2, addr3, city, state, province, zip, zip_suffix, country, lat, lon. Voir les valeurs par défaut pour exemple . | `textarea` | — | `[[name\|&#123;&#123;name&#125;&#125;]] [[addr1\|&#123;&#123;addr1&#125;&#125; ]] [[addr2\|&#123;&#123;addr2&#125;&#125; ]] [[addr3\|&#123;&#123;addr3&#125;&#125; ]] [[city\|&#123;&#123;city&#125;&#125;]] [[state\|&#123;&#123;state&#125;&#125;]][[province\|&#123;&#123;province&#125;&#125;,]] &#123;&#123;zip&#125;&#125;[[zip_suffix\|-&#123;&#123;zip_suffix&#125;&#125;]] &#123;&#123;country&#125;&#125;` |
| **Afficher le lien d'itinéraire**<br />`directions_position` | Sélectionner si vous voulez afficher le lien vers l'itinéraire | `multilist` | `0` = Aucun<br />`before` = Avant l'adresse<br />`after` = Après l'adresse | — |
| **Libellé du lien d'itinéraire**<br />`directions_link_label` | Libellé pour le lien d'itinéraire. Laisser vide pour la valeur par défaut | `text` | — | — |

#### Configuration de la carte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la carte**<br />`show_map` | Sélectionnez si une carte Google Maps doit être affichée avec l'adresse | `multilist` | `0` = Jamais<br />`category` = Vue catégorie uniquement<br />`item` = Vue d'article uniquement<br />`both` = Toujours | `none` |
| **type d'intégration**<br />`map_embed_type` | Sélectionner le type d'intégration : image ou carte intéractive | `multilist` | `int` = Carte intéractive<br />`img` = Carte statique (image) | `int` (Carte intéractive) |
| **Type de carte**<br />`map_type_view` | Sélectionnez le type de carte à afficher | `radio` | `—` = identique à l'édition<br />`roadmap` = Mode rue<br />`satellite` = Mode satellite<br />`hybrid` = Hybride<br />`terrain` = Relief | — |
| **Niveau zoom**<br />`map_zoom_view` | Niveau de zoom de la carte | `radio` | `—` = Par valeur | — |

#### Carte statique (image)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Carte cliquable**<br />`link_map` | Pour l'image map: ajoute un lien vers Google Maps pour l'endroit indiqué sur l'image de la carte. Ouvre dans une nouvelle fenêtre. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

:::note
Remarque : Les images de marqueurs personnalisés ne sont pas utilisées en mode image-map. Les paramètres suivants sont utilisés
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur du marqueur**<br />`marker_color` | Sélectionnez la couleur du marqueur d'emplacement sur la carte | `list` | `black` = Noir<br />`brown` = Marron<br />`green` = Vert<br />`purple` = Violet<br />`yellow` = Jaune<br />`blue` = Bleu<br />`gray` = Gris<br />`orange` = Orange<br />`red` = Rouge<br />`white` = Blanc | `red` (Rouge) |
| **Taille du marqueur**<br />`marker_size` | Sélectionnez la taille du marqueur | `radio` | `tiny` = Minuscule<br />`mid` = Intermédiaire<br />`small` = Miniscule<br />`normal` = Normal | `mid` (Intermédiaire) |

#### Tailles minimales

#### Tailles fixes

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur (px)**<br />`map_width` | Largeur de la carte en pixel | `text` | — | `200` |
| **Hauteur (px)**<br />`map_height` | Hauteur de la carte en pixel | `text` | — | `150` |

#### Position, style

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Position de la carte**<br />`map_position` | Afficher la carte avant ou après l'adresse | `radio` | `0` = Avant l'adresse<br />`1` = Après l'adresse | `0` (Avant l'adresse) |
| **Style Carte Générateur**<br />`map_style` | Copiez - collez le code json créé par snazzy. Remarque : utilisez [] AU DÉBUT ET À LA FIN du style _[custom style code]_ | `textarea` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pré-configuration**<br />`prx_sfx_open_close_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
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

## Fournisseur de carte

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Moteur de Carte**<br />`mapapi_edit` | — | `multilist` | `googlemap` = GoogleMap<br />`nominatim` = PLG_FLEXICONTENT_FIELDS_ADDRESSINT_MAP_ENGINE_NOMINATIM | `googlemap` (GoogleMap) |
| **Clef Google Map API**<br />`google_maps_js_api_key` | Entrez votre clé API Google Maps. C'est nécessaire pour le formulaire de contenu. Vous pouvez en obtenir une en suivant les instructions suivante https://developers.google.com/maps/documentation/static-maps/get-api-key | `text` | — | — |

:::note
Pour obtenir votre clé(s) Googlemap API veillez cliquer: Obtenir ma clé
:::

:::note
PLG_FLEXICONTENT_FIELDS_ADDRESSINT_NOMINATIM_INFO
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **PLG_FLEXICONTENT_FIELDS_ADDRESSINT_NOMINATIM_TILE_URL**<br />`nominatim_tile_url` | PLG_FLEXICONTENT_FIELDS_ADDRESSINT_NOMINATIM_TILE_URL_DESC _https://&#123;s&#125;.tile.openstreetmap.org/&#123;z&#125;/&#123;x&#125;/&#123;y&#125;.png_ | `text` | — | — |
| **PLG_FLEXICONTENT_FIELDS_ADDRESSINT_NOMINATIM_API_URL**<br />`nominatim_api_url` | PLG_FLEXICONTENT_FIELDS_ADDRESSINT_NOMINATIM_API_URL_DESC _https://nominatim.openstreetmap.org/_ | `url` | — | — |
| **Forcer le code de langue (ex. en)**<br />`api_lang_code_edit` | Laissez ce champ vide pour utiliser la langue de l’utilisateur actuel | `text` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Moteur de Carte**<br />`mapapi` | — | `multilist` | `googlemap` = GoogleMap<br />`openstreetmap` = OpenStreetMap | `googlemap` (GoogleMap) |

:::note
Optionnellement vous pouvez utiliser une clef différente pourl'affichage, comme par exemple pour avoir des statistiques différentes dans la console Google
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Clef Google Map API**<br />`google_maps_static_api_key` | Entrez votre clé d'affichage API Google Maps. Vous pouvez utiliser l'API Google Maps sans clé , mais les limites d'utilisation sont beaucoup plus faibles . Vous pouvez obtenir la clé en suivant les instructions à https://developers.google.com/maps/documentation/static-maps/get-api-key | `text` | — | — |
| **URL du serveur de tuiles (carte)**<br />`os_tile_server_url` | Saisir une URL de serveur de tuiles personnalisée (OpenStreetMap). Si vous prévoyez beaucoup de trafic, il est préférable d’utiliser votre propre serveur de tuiles, par ex. https://&#123;s&#125;.tile.openstreetmap.org/&#123;z&#125;/&#123;x&#125;/&#123;y&#125;.png | `text` | — | `https://&#123;s&#125;.tile.openstreetmap.org/&#123;z&#125;/&#123;x&#125;/&#123;y&#125;.png` |
| **Forcer le code de langue (ex. en)**<br />`api_lang_code` | Laissez ce champ vide pour utiliser la langue de l’utilisateur actuel | `text` | — | — |

## Propriétés dans un champ

#### Utiliser un champ comme une proporiété

:::note
Vous pouvez choisir de stocker certaines propriétés comme des champs individuels (par exemple, pour un filtrage plus simple / une recherche). **Étapes**: - créer des champs de texte - les affecter aux mêmes types que ce champ - les définir pour être cachés dans le formulaire - puis les sélectionner ici
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Entreprise ou lieu**<br />`field_name` | — | `fields` | — | — |
| **Adresse 1**<br />`field_addr1` | — | `fields` | — | — |
| **Adresse 2**<br />`field_addr2` | — | `fields` | — | — |
| **Adresse 3**<br />`field_addr3` | — | `fields` | — | — |
| **Ville**<br />`field_city` | — | `fields` | — | — |
| **Code postal**<br />`field_zip` | — | `fields` | — | — |
| **Pays**<br />`field_country` | — | `fields` | — | — |
| **Longitude**<br />`field_lon` | — | `fields` | — | — |
| **Latitude**<br />`field_lat` | — | `fields` | — | — |
| **Marqueur**<br />`field_marker` | — | `fields` | — | — |
