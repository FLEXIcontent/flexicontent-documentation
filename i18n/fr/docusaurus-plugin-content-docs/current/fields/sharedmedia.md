---
sidebar_position: 32
---

# Vidéo / audio partagé

Ce champ intègre dans les articles , un lecteur (vidéo/audio) à partir de sites de partage vidéo comme YouTube, Vimeo, Dailymotion, Vevo, Hulu, Metacafe et audio comme soundclound, last.fm, etc.. Pour ajouter les références média (valeurs des champs) , il suffit simplement de copier l'URL de la page d'origine , les informations seront extraites ( titre, auteur , description ) et un lecteur de prévisualisation sera intégré. La configuration du champ permet de contrôler les informations à afficher , ainsi que les dimensions des joueurs. Sauf pour YouTube , Vimeo et Dailymotion , la capacité extraction est basée sur le service embed.ly , qui est gratuit pour un maximum de 5000 URL par mois. Il est recommandé d'obtenir et entrez votre propre clé API embed.ly .

*Plugin : `sharedmedia` — Vidéo/audio partagé*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/sharedmedia/sharedmedia.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
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

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |
| **PLG_FLEXICONTENT_FIELDS_SHAREDMEDIA_FORM_CARD_WIDTH**<br />`form_card_width` | PLG_FLEXICONTENT_FIELDS_SHAREDMEDIA_FORM_CARD_WIDTH_DESC | `text` | — | `250` |

#### Propriétés optionnelles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Titre**<br />`display_title_form` | Afficher le champ titre dans le formulaire d'édition | `radio` | `0` = Cacher<br />`2` = Montrer<br />`1` = Editer | `1` (Editer) |
| **Auteur**<br />`display_author_form` | Afficher le champ auteur dans le formulaire d'édition | `radio` | `0` = Cacher<br />`2` = Montrer<br />`1` = Editer | `1` (Editer) |
| **Description**<br />`display_description_form` | Afficher le champ description dans le formulaire d'édition | `radio` | `0` = Cacher<br />`2` = Montrer<br />`1` = Editer | `1` (Editer) |
| **Dimensions du lecteur**<br />`display_edit_size_form` | Autoriser l'utilisateur à choisir des tailles spécifique de lecteur pour chaque médias partagées. | `radio` | `0` = Cacher<br />`2` = Montrer<br />`1` = Editer | `1` (Editer) |

#### Informations avancées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode Encapsulation / API**<br />`display_api_type_form` | Afficher la méthode d'encapuslation/API dans le formulaire d'édition | `radio` | `0` = Cacher<br />`2` = Montrer | `0` (Cacher) |
| **PLG_FLEXICONTENT_FIELDS_SHAREDMEDIA_DISPLAY_EMBED_URL_FORM**<br />`display_embed_url_form` | Afficher le champ id dans le formulaire d'édition | `radio` | `0` = Cacher<br />`2` = Montrer | `0` (Cacher) |
| **Id du média**<br />`display_media_id_form` | Afficher le champ id dans le formulaire d'édition | `radio` | `0` = Cacher<br />`2` = Montrer | `0` (Cacher) |
| **Durée**<br />`display_duration_form` | Affiche un Champ de durée dans le formulaire d'édition Remarque : cette information est disponible via les API natives mais pas avec embed.ly) | `radio` | `0` = Cacher<br />`2` = Montrer | `0` (Cacher) |

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

#### Valeurs affichées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher un message aucune valeur**<br />`show_no_value` | Afficher un message qui sera affichée pour les champs qui ne possèdent aucune valeur saisie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Message aucune valeur**<br />`no_value_msg` | Le texte qui sera affiché lorsque le champ ne possède aucune valeur, laisser vide pour afficher le message par défaut | `text` | — | — |

### Liste Valeurs

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

## Lecture

### Médias

#### Informations sur le média

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Titre**<br />`display_title` | Indique le titre du média en dessous du lecteur | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Balise HTML pour le titre**<br />`headinglevel` | Niveau du H pour Titre (niveau de 1 à 6) | `list` | `1` = H1<br />`2` = H2<br />`3` = H3<br />`4` = H4<br />`5` = H5<br />`6` = H6 | `3` (H3) |
| **Auteur**<br />`display_author` | Affiche le nom de l'auteur sous le lecteur | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Description**<br />`display_description` | Affiche la description du média en dessous du lecteur | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### API natives uniquement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Durée**<br />`display_duration` | Affiche la durée du média au format hh:mm:ss sous le lecteur | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Lecteur média

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur Player**<br />`width` | Entrez la largeur de l'iframe contenant le lecteur, en pixels | `text` | — | `480` |
| **Hauteur Player**<br />`height` | Entrez la hauteur de l'iframe contenant le lecteur, en pixels | `text` | — | `270` |
| **Position du player**<br />`player_position` | Sélectionnez la position du lecteur par rapport aux méta-données : titre, auteur , description | `radio` | `0` = Avant les données<br />`1` = Après les données | `0` (Avant les données) |

## API (clés, etc.)

:::note
**Méthode d'intégration** Utiliser embed.ly seulement, - ou - utiliser les APIs native de : youtube, vimeo, dailymotion Remarque : cela ne changera pas les méthode des valeurs déjà enregistrées
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Intégrer avec**<br />`use_native_apis` | Désactivez pour utiliser également les API natives | `multilist` | `0` = API noembed uniquement<br />`1` = API noembed et API natives | `0` (API noembed uniquement) |
| **Mode d'intégration privé**<br />`privacy_embeed` | Si l'hébergeur de vos média le permet, le contenu sera intégré et les données personnelles des utilisateurs ne seront pas récupérer. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Démarrage automatique**<br />`autostart` | Ajoute le paramètre de lecture automatique dans l'uRL du média. Ce changement d'option nécessite la ré-importation des médias | `radio` | `0` = Browser disabled (security concerns) | `0` (Browser disabled (security concerns)) |

#### Configuration Embed.ly

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Forcer SSL**<br />`force_ssl` | Force le iframe intégré à utiliser SSL. Cette option force l'utilisation d'uRL sécurisé pour l'intégration des contenus . Un changement ici oblige à re-intégrer les médias . | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Configuration Youtube

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Clef API Youtube**<br />`youtube_key` | Obtenez votre clé API Youtube v3 (via la console développeur Google) https://developers.google.com/youtube/v3/getting-started | `text` | — | — |

### Débogage

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Débogage JavaScript**<br />`debug_to_console` | Activer pour ajouter des informations de débogage dans la console du navigateur sur les appels API AJAX | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
