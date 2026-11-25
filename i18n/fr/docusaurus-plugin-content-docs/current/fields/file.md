---
sidebar_position: 20
---

# Fichier

Plugin de champ 'fichier' pour FLEXIcontent

*Plugin : `file` — Fichier*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/file/file.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
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
| **Autoriser les valeurs multiples**<br />`allow_multiple` | Autoriser plus d'1 valeur pour ce champs | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Nb maximum de valeurs**<br />`max_values` | Définissez ici le nombre maximum de valeurs que l'utilisateur pourra saisir. 0 pour illimité. | `text` | — | `0` |
| **Valeurs par colonne**<br />`fields_box_placing` | Économiser de l'espace en autorisant l'affichage par ligne de valeurs multiples | `radio` | `0` = 1<br />`1` = Multiple | `1` (Multiple) |

#### Boutons

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Position Ajouter**<br />`add_position` | Sélectionnez pour ajouter le bouton en ligne (bouton d'ajout de valeur à chaque ligne) ou afficher le bouton d'ajout au fond de la liste de valeurs | `multilist` | `0` = Bouton Ajouter en bas<br />`1` = Bouton ajouter avant<br />`2` = Bouton Ajouter après<br />`3` = Les deux (avant - après) | `3` (Les deux (avant - après)) |
| **Fichier à transmettre / Sélectionner**<br />`file_btns_position` | Choisir comment et où afficher la sélection de fichier et le bouton d'envoi | `hidden` | — | `0` |

### Stockage à distance

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type de stockage**<br />`estorage_mode` | Sélectionnez le type de stockage à distance | `multilist` | `0` = Non<br />`FTP` = FTP<br />`OTHER` = Other | `0` (Non) |

#### Autre

:::note
Actuellement, seul FTP est pris en charge ; d’autres options de stockage externe sont à venir…
:::

#### Stockage à distance (FTP)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nom d’hôte**<br />`efs_ftp_host` | — | `text` | — | — |
| **Port**<br />`efs_ftp_port` | — | `text` | — | — |
| **Utilisateurs**<br />`efs_ftp_user` | — | `text` | — | — |
| **Mot de passe**<br />`efs_ftp_pass` | — | `text` | — | — |
| **Répertoire**<br />`efs_ftp_path` | — | `text` | — | — |
| **URL**<br />`efs_www_url` | — | `text` | — | `https://some_external_servername.com/somefolder/` |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |
| **PLG_FLEXICONTENT_FIELDS_FILE_FORM_CARD_WIDTH**<br />`form_card_width` | PLG_FLEXICONTENT_FIELDS_FILE_FORM_CARD_WIDTH_DESC | `text` | — | `400` |

#### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage des champs**<br />`formlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/field_*. hp comme field_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Informations d’en-tête**<br />`form_info_header` | — | `radio` | `1` = Sous-chemin de stockage serveur<br />`2` = Nom de fichier d’origine<br />`3` = Les deux | `3` (Les deux) |
| **Aperçu du fichier**<br />`form_file_preview` | Vous pouvez activer l’aperçu du fichier, par ex. une vignette sera affichée si le fichier sélectionné est une image | `multilist` | `0` = Désactiver<br />`1` = Activer | `0` (Désactiver) |

#### Editer les propriétés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`inputmode` | Sélectionner pour autoriser la modification des propriétés du fichier | `multilist` | `1` = Non<br />`0` = Oui | `1` (Non) |
| **Titre**<br />`iform_title` | Peut être afficher à la place du nom de fichier | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Description**<br />`iform_desc` | Cette option peut être utilisé par certain champ, ex cela peut être optionellement affiché (enligne, bulle d'aide, etc) par le champ fichier | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Langue**<br />`iform_lang` | Vous voudrez peut-être définir la langue du fichier, par exemple si le fichier est un document dans une langue spécifique ou un support contenant de l'audio ou du texte dans une langue spécifique | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Accès**<br />`iform_access` | Vous pouvez définir le niveau d’accès que les utilisateurs devront avoir, afin de télécharger ou visualiser le fichier | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Répertoire cible**<br />`iform_dir` | Si vous sélectionnez sécurisé, les utilisateurs ne verront jamais le chemin réel du fichier et ne seront autorisés **qu'à un accès indirect**au fichier. Cette option convient pour, par exemple, - fichiers de document * - images haute résolution protégées par le droit d'auteur * * joindre le contenu via le champ **FICHIER** ** joindre le contenu via le champ **FICHIER** ou le champ **image/galerie** REMARQUE: 1. Si vous sélectionnez un dossier multimédia, l'accès direct sera autorisé et vous pourrez ainsi lire des fichiers multimédia via des lecteurs multimédias intégrés au navigateur du visiteur. 2. Les fichiers image du dossier sécurisé privilégie un accès via un champ de fichier ou peuvent être visualisés à l'aide de miniatures (éventuellement dotées d'un filigrane) créées par le champ image/galerie. Vous conserverez ainsi la protection du téléchargement sécurisé. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Télécharger le filigrane**<br />`iform_stamp` | Activer / désactiver l'ajout d'un filigrane pendant le téléchargement de fichier (par exemple, pour les fichiers PDF) | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Par défaut

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Titre**<br />`iform_title_default` | Valeur par défaut | `text` | — | — |
| **Description**<br />`iform_desc_default` | Valeur par défaut | `text` | — | — |
| **Langue**<br />`iform_lang_default` | Valeur par défaut | `fclanguage` | — | `*` |
| **Accès**<br />`iform_access_default` | Valeur par défaut | `accesslevel` | — | `1` |
| **Répertoire cible**<br />`iform_dir_default` | Valeur par défaut | `radio` | `0` = Média<br />`1` = Sécurisé | `1` (Sécurisé) |
| **Télécharger le filigrane**<br />`iform_stamp_default` | Valeur par défaut | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### FLEXI_FILE_CUSTOM1_SEP

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`custom1_enable` | FLEXI_FILE_CUSTOM_ENABLE_DESC | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **FLEXI_FILE_CUSTOM_LABEL**<br />`custom1_label` | FLEXI_FILE_CUSTOM_LABEL_DESC | `text` | — | — |
| **FLEXI_FILE_CUSTOM_LABEL_SHOW**<br />`custom1_label_show` | FLEXI_FILE_CUSTOM_LABEL_SHOW_DESC | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Par défaut**<br />`custom1_default` | FLEXI_FILE_CUSTOM_DEFAULT_DESC | `textarea` | — | — |
| **FLEXI_FILE_CUSTOM_ROWS**<br />`custom1_rows` | FLEXI_FILE_CUSTOM_ROWS_DESC | `number` | — | `2` |
| **Utilisation par défaut**<br />`custom1_default_use` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### FLEXI_FILE_CUSTOM2_SEP

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`custom2_enable` | FLEXI_FILE_CUSTOM_ENABLE_DESC | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **FLEXI_FILE_CUSTOM_LABEL**<br />`custom2_label` | FLEXI_FILE_CUSTOM_LABEL_DESC | `text` | — | — |
| **FLEXI_FILE_CUSTOM_LABEL_SHOW**<br />`custom2_label_show` | FLEXI_FILE_CUSTOM_LABEL_SHOW_DESC | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Par défaut**<br />`custom2_default` | FLEXI_FILE_CUSTOM_DEFAULT_DESC | `textarea` | — | — |
| **FLEXI_FILE_CUSTOM_ROWS**<br />`custom2_rows` | FLEXI_FILE_CUSTOM_ROWS_DESC | `number` | — | `2` |
| **Utilisation par défaut**<br />`custom2_default_use` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

### Mes fichiers

:::note
Affiche un gestionnaire de multi-téléchargement, ainsi que de la sélection des fichiers téléchargés par l’utilisateur en cours d’affichage, (certains utilisateurs privilégiés peuvent voir tous les fichiers)
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_myfiles` | Activer pour permettre la sélection d’un fichier existant précédemment téléversé | `multilist` | `0` = Téléversements en ligne, sans fenêtre de réutilisation de Mes fichiers<br />`1` = Téléversements en ligne + fenêtre de réutilisation de Mes fichiers (avec : téléversements sécurisés + liens URL)<br />`2` = Téléversements en ligne + fenêtre de réutilisation de Mes fichiers (avec : téléversements sécurisés + liens URL + gestionnaire de médias Joomla)<br />`3` = Téléversements en ligne + fenêtre de réutilisation de Mes fichiers (avec : liens URL + gestionnaire de médias Joomla)<br />`4` = Gestionnaire de médias Joomla<br />`5` = Téléversements en ligne + fenêtre de réutilisation de Mes fichiers (avec : téléversements sécurisés) | `1` (Téléversements en ligne + fenêtre de réutilisation de Mes fichiers (avec : téléversements sécurisés + liens URL)) |
| **Médias Joomla**<br />`jmedia_filetypes` | Sélectionner les types de fichiers autorisés et sélectionnables par les éditeurs | `fccheckbox` | — | — |

:::note
À propos du dossier racine (Joomla 4+ uniquement) - vous devez ajouter ce dossier dans le plugin **FileSystem - Local**, par exemple le dossier downloads. - Pour le gestionnaire Quantum, il s’agit du nom de portée. REMARQUE : ajoutez une portée personnalisée supplémentaire pour le dossier images, par exemple « imgs ». NE modifiez PAS le nom du dossier « images » ; « imgs » sera le nom de la portée personnalisée
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Dossier racine**<br />`jmedia_topdir` | Pour le gestionnaire de médias natif, il s’agit du dossier situé dans la racine Joomla (ajouté dans le plugin Filestorage). Pour le gestionnaire Quantum, il s’agit du nom de portée personnalisé _images_ | `text` | — | — |
| **Chemin du sous-dossier**<br />`jmedia_subpath` | Sélectionner le sous-dossier à ouvrir, par exemple content/news -&gt; JPATH_ROOT/images/content/news_ | `text` | — | — |

#### Propriétaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affectation automatique**<br />`autoassign` | Lorsque de nouveaux fichiers sont téléchargés, ils seront automatiquement assignés au champ actuel. De cette façon, l'utilisateur n'aura pas à rechercher et cliquer sur le ou les nouveaux fichiers | `radio` | `0` = Non<br />`1` = Sélectionner et assigner<br />`2` = Sélectionnée(s) uniquement | `1` (Sélectionner et assigner) |
| **Répertoire cible**<br />`target_dir` | Si vous sélectionnez sécurisé, les utilisateurs ne verront jamais le chemin réel du fichier et ne seront autorisés **qu'à un accès indirect**au fichier. Cette option convient pour, par exemple, - fichiers de document * - images haute résolution protégées par le droit d'auteur * * joindre le contenu via le champ **FICHIER** ** joindre le contenu via le champ **FICHIER** ou le champ **image/galerie** REMARQUE: 1. Si vous sélectionnez un dossier multimédia, l'accès direct sera autorisé et vous pourrez ainsi lire des fichiers multimédia via des lecteurs multimédias intégrés au navigateur du visiteur. 2. Les fichiers image du dossier sécurisé privilégie un accès via un champ de fichier ou peuvent être visualisés à l'aide de miniatures (éventuellement dotées d'un filigrane) créées par le champ image/galerie. Vous conserverez ainsi la protection du téléchargement sécurisé. | `radio` | `0` = Média<br />`1` = Sécurisé<br />`2` = Autoriser la sélection | `1` (Sécurisé) |
| **Chemin du sous-dossier**<br />`subfolder_path` | Les fichiers téléchargés seront déplacés dans ce sous-dossier dans leur dossier parent SÉCURISÉ ou MÉDIA | `text` | — | — |
| **Renommage automatique**<br />`auto_filename` | Créer le nom de fichier à l’aide de code PHP | `multilist` | `0` = Non<br />`2` = Utiliser du code personnalisé | `0` (Non) |
| **Code personnalisé**<br />`auto_filename_code` | Remarque : renvoyer le nom de fichier sans l’extension ; laissez vide et rechargez pour voir un exemple | `editor` | — | — |

#### Colonnes des listes de fichiers

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Colonnes**<br />`filelist_cols` | Colonnes optionnelles pour la liste de fichiers. Certaines colonnes comme le nom de fichier ne peuvent pas être désactivées | `fccheckbox` | — | — |

#### Redimensionner automatiquement les images

:::note
Redimensionnement se fera au niveau du navigateur de l’utilisateur, ainsi vous obtenez un téléchargement plus rapide et moins de consommation sur l’espace serveur
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Redimensionnement**<br />`resize_on_upload` | Redimensionner une image téléchargée afin d'économiser de l’espace sur le serveur et d'accélérer les téléchargements, cela sera la taille pour le client (tous les modes ne supportes pas cette fonction) | `multilist` | `—` = Utiliser les paramètres du composant<br />`0` = Non<br />`1` = Oui | — |
| **Largeur de l'image**<br />`upload_max_w` | — | `text` | — | — |
| **Hauteur de l'image**<br />`upload_max_h` | — | `text` | — | — |
| **Méthode de traitement**<br />`upload_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `—` = Utiliser les paramètres du composant<br />`0` = A l'échelle<br />`1` = Découper | — |

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
| **Montrer un message d'**accès interdit****<br />`show_acc_msg` | Si le champ est inaccessible, une message de non-accès s'affichera. **NOTE : ** SI ce paramètre est désactivé, le champ sera invisible aux utilisateurs sans accès, sans aucun message ou avertissement indiquant son existance | `multilist` | `0` = Non<br />`1` = Oui<br />`2` = Oui, ajouter un lien de connexion | `0` (Non) |
| **Message **accès interdit****<br />`no_acc_msg` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Exporter

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `multilist` | `0` = Non<br />`1` = Valeurs brutes<br />`2` = Valeurs de rendu | `0` (Non) |
| **Supprimer html**<br />`csv_strip_html` | — | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **FLEXI_FIELD_FILE_CSV_EXPORT_FORMAT**<br />`csv_export_format` | FLEXI_FIELD_FILE_CSV_EXPORT_FORMAT_DESC | `radio` | `html` = FLEXI_FIELD_FILE_CSV_EXPORT_FORMAT_HTML<br />`importable` = FLEXI_FIELD_FILE_CSV_EXPORT_FORMAT_IMPORTABLE | `html` (FLEXI_FIELD_FILE_CSV_EXPORT_FORMAT_HTML) |

#### Fichiers inaccessibles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher**<br />`noaccess_display` | Sélectionner cette option pour afficher les informations du fichier ou bien ignorer le fichier complétement | `radio` | `0` = Non<br />`1` = Oui<br />`2` = Oui, pas de description | `1` (Oui) |
| **Ajouter les variables du fichier**<br />`noaccess_addvars` | Cette option est réservée aux développeurs, si vous l'activez les variables file_id, field_id, item_id seront ajoutés à l'URL de refus d'accès. Cela permettra ensuite de traiter de manière spécifique les redirections en fonction du fichier. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Utilisateurs non connectés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **URL de redirection**<br />`noaccess_url_unlogged` | URL de redirection URL pour les utilisateurs non connectés, ex : formulaire de connexion ou d'inscription | `text` | — | — |
| **Message**<br />`noaccess_msg_unlogged` | Affiche un message personnalisé aux utilisateurs non connectés. Ex : 'accès interdit' ou 'veuillez vous connectez' | `text` | — | — |

#### Utilisateurs connectés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **URL de redirection**<br />`noaccess_url_logged` | URL de redirection URL pour les utilisateurs connectés, ex : page de souscription | `text` | — | — |
| **Message**<br />`noaccess_msg_logged` | Affiche un message personnalisé aux utilisateurs non connectés. Ex : 'accès interdit' ou 'veuillez acheter' | `text` | — | — |

#### FLEXI_BACKEND_VIEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_BACKEND_VIEW_APPEARANCE**<br />`backend_view_appearance` | FLEXI_BACKEND_VIEW_APPEARANCE_DESC | `multilist` | `0` = Par défaut<br />`1` = FLEXI_CHECK_MARK<br />`2` = FLEXI_CLEAN_HTML_AND_TRIM | `0` (Par défaut) |
| **FLEXI_TRIM_LENGTH**<br />`backend_view_trim_chars` | FLEXI_TRIM_LENGTH_DESC | `text` | — | `100` |

### Actions fichier

:::note
Configuration des boutons pour des actions telles que : télécharger, afficher, partager, ajouter au panier
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utilisez les boutons**<br />`usebutton` | Sélectionnez pour afficher les liens, boutons ou autres | `multilist` | `0` = Liens<br />`1` = Boutons | `1` (Boutons) |
| **Position des boutons**<br />`buttonsposition` | Position des boutons (télécharger, partager, ajouter au panier), relatif au nom du fichier | `radio` | `0` = Avant<br />`1` = Après | `1` (Après) |

#### Caractère(s) de séparation entre éléments actifs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser un ou des caractères de séparation**<br />`use_action_separator` | Si vous préférez utiliser un style css, plutôt qu'un caractère de séparation, pour l'affichage des éléments | `multilist` | `0` = Saut de ligne<br />`1` = Personnalisé | `0` (Saut de ligne) |
| **Personnalisé**<br />`action_separator` | Caractère(s) de séparation affiché-s entre les liens d'action ou les boutons | `text` | — | — |

#### Actions fichier

### Téléchargements

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser les téléchargements**<br />`allowdownloads` | Normalement, vous avez besoin de ca, cependant, vous pouvez le désactiver si vous utilisez le module gestionnaire de téléchargements (module de panier de téléchargements). **Remarque :** lorsque les téléchargements sont activées, les niveaux d'ACL/accès sont toujours utilisés pour déterminer si l'interface utilisateur peut télécharger le fichier | `multilist` | `0` = Non<br />`1` = Oui<br />`2` = Oui, texte personnalisé | `1` (Oui) |
| **Texte de téléchargement personnalisé**<br />`downloadstext` | Normalement, le bouton permet d'afficher «Télécharger», vous pouvez définir un texte personnalisé ici. Exemple 'trouver!' , etc | `text` | — | `FLEXI_DOWNLOAD` (Télécharger) |

#### Forcer le téléchargement des fichier charger via URL

:::note
Vous ne pouvez pas forcer un URL de média externe à être téléchargé par le navigateur. L'activation de cette option conduira l'URL du fichier externe via le serveur web à le télécharger. Désactivez ceci si vous avez des problèmes de téléchargement l'option URL de fichier !!! Le serveur externe doit également être en mesure de rapporter les tailles de fichiers correctement ...
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`force_url_download` | Les URL de fichier seront conduites à travers le serveur web pour être en mesure de forcer un téléchargement. Désactivez cette option si vous rencontrez des problèmes !!! | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Extensions à forcer**<br />`force_url_download_exts` | Normalement, le bouton permet d'afficher «Télécharger», vous pouvez définir un texte personnalisé ici. Exemple 'trouver!' , etc | `text` | — | `bmp,wbmp,gif,jpg,jpeg,png,webp,ico,wav,mp3,aiff` |
| **Taille maximale du fichier [KB]**<br />`force_url_download_max_kbs` | Le téléchargement de fichiers plus volumineux ne sera pas effectué via le serveur web. À la place, l'uRL du fichier sera ouverte via une redirection | `text` | — | `100000` |

### Visualisation navigateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le bouton 'vue'**<br />`allowview` | Autorise l'affichage du fichier dans le navigateur | `multilist` | `0` = Non<br />`1` = Oui<br />`2` = Oui, texte personnalisé | `0` (Non) |
| **Texte personnalisé pour 'vue'**<br />`viewtext` | Ce bouton affiche le texte 'vue', mais vous pouvez personnaliser le libellé ici. Ex: 'Cliquer pour voir' etc. | `text` | — | — |
| **Affichage dans**<br />`viewinside` | Choisir d’afficher le fichier dans la même fenêtre ou une nouvelle | `radio` | `0` = Fenêtre modale Fancybox<br />`1` = Fenêtre modale GLightbox (responsive + plein écran)<br />`2` = Nouvelle fenêtre<br />`3` = Même fenêtre | `1` (Fenêtre modale GLightbox (responsive + plein écran)) |

### Filigrane PDF

### Ajouter un texte dans toutes les pages

:::note
Nécessite l’installation manuelle de 2 bibliothèques : tcpdf et fpdi dans le dossier **/components/com_flexicontent/librairies/TCPDF**
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter des textes d’estampille**<br />`stamp_pdfs` | Modifier les fichiers PDF lors du téléchargement pour ajouter un texte d’estampille | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Personnalisé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **En-tête**<br />`pdf_header_text` | Ce texte sera ajouté dans toutes les pages du PDF, Pour utiliser la date courante ou des chaînes de langue utiliser: &#123;&#123;current_date&#125;&#125; %%LANG_NAME%% | `textarea` | — | — |
| **Pied de page**<br />`pdf_footer_text` | Ce texte sera ajouté dans toutes les pages du PDF, Pour utiliser la date courante ou des chaînes de langue utiliser: &#123;&#123;current_date&#125;&#125; %%LANG_NAME%% | `textarea` | — | — |

#### En-tête

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Famille de police**<br />`pdf_header_ffamily` | Sélectionner une famille de police pour le texte d’en-tête | `list` | `Courier` = Courier<br />`Helvetica` = Helvetica<br />`Arial` = Arial<br />`Times` = Times<br />`Symbol` = Symbol<br />`ZapfDingbats` = ZapfDingbats | `Helvetica` (Helvetica) |
| **Style de police**<br />`pdf_header_fstyle` | Laissez vide pour la police normale, ou saisissez une combinaison de b i u (b : gras, i : italique, u : souligné). Exemple pour gras et italique : bi | `text` | — | — |
| **Taille de police**<br />`pdf_header_fsize` | La taille est exprimée en points. Saisissez uniquement des entiers sans suffixe | `number` | — | `11` |
| **Alignement**<br />`pdf_header_align` | Alignement du texte à gauche, à droite ou au centre | `list` | `C` = Centre<br />`L` = Gauche<br />`R` = Droite | `C` (Centre) |
| **Type de bordure**<br />`pdf_header_border_type` | Indique si des bordures doivent être tracées autour de la cellule. La valeur peut être un nombre : 0 : aucune bordure (par défaut), 1 : cadre, ou une chaîne contenant tout ou partie des caractères suivants (dans n’importe quel ordre) : L : gauche, T : haut, R : droite, B : bas | `text` | — | `0` |

#### Pied de page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Famille de police**<br />`pdf_footer_ffamily` | Sélectionner une famille de police pour le texte d’en-tête | `list` | `Courier` = Courier<br />`Helvetica` = Helvetica<br />`Arial` = Arial<br />`Times` = Times<br />`Symbol` = Symbol<br />`ZapfDingbats` = ZapfDingbats | `Helvetica` (Helvetica) |
| **Style de police**<br />`pdf_footer_fstyle` | Laissez vide pour la police normale, ou saisissez une combinaison de b i u (b : gras, i : italique, u : souligné). Exemple pour gras et italique : bi | `text` | — | — |
| **Taille de police**<br />`pdf_footer_fsize` | La taille est exprimée en points. Saisissez uniquement des entiers sans suffixe | `number` | — | `11` |
| **Alignement**<br />`pdf_footer_align` | Alignement du texte à gauche, à droite ou au centre | `list` | `C` = Centre<br />`L` = Gauche<br />`R` = Droite | `C` (Centre) |
| **Type de bordure**<br />`pdf_footer_border_type` | Indique si des bordures doivent être tracées autour de la cellule. La valeur peut être un nombre : 0 : aucune bordure (par défaut), 1 : cadre, ou une chaîne contenant tout ou partie des caractères suivants (dans n’importe quel ordre) : L : gauche, T : haut, R : droite, B : bas | `text` | — | `0` |

#### Dates

:::note
Date
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Format de la date**<br />`stamp_date_format` | Si vous choisissez 'format personnalisé' dans la liste ci-dessus vous devez spécifier dans ce champ le format que vous souhaitez afficher en utilisant la syntaxe PHP date (http://php.net/manual/en/function.date.php) (ATTENTION ne pas utilisé le strftime). | `multilist` | `DATE_FORMAT_LC1` = DATE_FORMAT_LC1<br />`DATE_FORMAT_LC2` = DATE_FORMAT_LC2<br />`DATE_FORMAT_LC3` = DATE_FORMAT_LC3<br />`DATE_FORMAT_LC4` = DATE_FORMAT_LC4<br />`_custom_` = Format personnalisé | `DATE_FORMAT_LC2` (DATE_FORMAT_LC2) |
| **Format personnalisé**<br />`stamp_custom_date` | Si vous choisissez 'format personnalisé' dans la liste ci-dessus vous devez spécifier dans ce champ le format que vous souhaitez afficher en utilisant la syntaxe PHP strftime (http://php.net/strftime). | `text` | — | — |
| **Format du filtre de langue**<br />`stamp_lang_filter_format` | Appliquer le filtre de langue JText::_() sur la chaîne de format qui doit être une chaîne de langue, soit ajouté dans un fichier de langue, soit ajouté par le gestionnaire de langue Joomla. **AVERTISSEMENT**: Vous devez désactiver le filtrage de langue si vous n'ajoutez pas de chaîne de langue ! sinon certains caractères seront supprimés comme des virgules | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

:::note
Fuseau horraire
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le fuseau horaire**<br />`stamp_display_tz_suffix` | Activer cette option pour afficher un décalage de fuseau horaire numérique lors de l'affichage des dates, ou vous pouvez faire manuellement via une chaîne de format de date personnalisée | `multilist` | `0` = Non, sélection manuelle<br />`1` = Oui | `1` (Oui) |
| **Fuseau horaire des utilisateurs connectés**<br />`stamp_display_tz_logged` | Sélectionner le fuseau horaire à utiliser pour l'affichage des dates. Uniquement pour les utilisateurs connectés. | `list` | `0` = Ignorer<br />`1` = UTC+0<br />`2` = Fuseau horaire du site<br />`3` = Heure locale de l'utilisateur | `0` (Ignorer) |
| **Fuseau horaire des invités/anonymes**<br />`stamp_display_tz_guests` | Sélectionner le fuseau horaire à utiliser pour l'affichage des dates. Uniquement pour les utilisateurs anonymes (non connectés). | `list` | `0` = Ignorer<br />`1` = UTC+0<br />`2` = Fuseau horaire du site | `0` (Ignorer) |

### Panier

#### Panier de téléchargement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher \"_QQ_\"Ajouter au panier\"_QQ_\**<br />`use_downloads_manager` | Nécessite le module de gestion de téléchargements. Cette fonction permet d'ajouter des fichiers à un panier de téléchargements - l'utilisateur peut organiser son / ses téléchargements dans des dossiers, et les télécharger en une fois via une archive compressée unique. Permet également de stocker / supprimer / renommer les paniers, etc | `multilist` | `0` = Non<br />`1` = Oui<br />`2` = Oui, texte personnalisé | `0` (Non) |
| **Ajouter au panier personnalisé**<br />`addtocarttext` | Normalement, le bouton permet d'afficher \"_QQ_\"Ajouter au panier\"_QQ_\", vous pouvez définir un texte personnalisé ici, par exemple, \"_QQ_\"Ajouter à mes téléchargements\"_QQ_\", etc | `text` | — | — |

### Partage

#### Partage

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les boutons de partage**<br />`allowshare` | Permet de partager le lien de téléchargement par e-mail | `multilist` | `0` = Non<br />`1` = Oui<br />`2` = Oui, texte personnalisé | `0` (Non) |
| **Texte de partage personnalisé**<br />`sharetext` | Normalement, le bouton permet d'afficher \"_QQ_\"Partager\"_QQ_\", vous pouvez définir un texte personnalisé ici, par exemple, \"_QQ_\"Partager avec un ami\"_QQ_\", etc | `text` | — | — |

:::note
Coupons de téléchargement ex: quand un utilisateur partage (via email / etc) un lien de téléchargement de fichier avec un utilisateur qui n'a pas l'accès au téléchargement
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer les coupons de téléchargement**<br />`enable_coupons` | Lors du partage de liens de fichier (téléchargement), les utilisateurs recevant le lien (ex: via email/etc), n'ont peut être pas le niveau d'accès requis pour télécharger le fichier. Activer cette option permet à ces utilisateurs de télécharger le fichier, en créant les coupons de téléchargement | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Limite des coupons de coupons**<br />`coupon_hits_limit` | Cela limite le nombre de téléchargements (clics) qui peuvent être effectués pour chaque coupon. Mettre -1 pour ne pas configurer de limite, ainsi, les coupons expireront uniquement quand la date d'expiration est atteinte. | `text` | — | `3` |
| **Date d'expiration du coupon**<br />`coupon_expiration_days` | Combien de temps le coupon sera utilisable après sa création | `text` | — | `15` |

### FLEXI_DL_LIMIT_TAB

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_DL_LIMIT_OVERRIDE**<br />`dl_limit_override` | FLEXI_DL_LIMIT_OVERRIDE_DESC | `multilist` | `0` = FLEXI_DL_LIMIT_USE_COMPONENT<br />`1` = FLEXI_DL_LIMIT_USE_FIELD<br />`2` = FLEXI_DL_LIMIT_NONE | `0` (FLEXI_DL_LIMIT_USE_COMPONENT) |

:::note
FLEXI_DL_LIMIT_INFO
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_DL_LIMIT_COUNT_MODE**<br />`dl_limit_count_mode` | FLEXI_DL_LIMIT_COUNT_MODE_DESC | `radio` | `0` = FLEXI_DL_LIMIT_MODE_ANY<br />`1` = FLEXI_DL_LIMIT_MODE_UNIQUE | `0` (FLEXI_DL_LIMIT_MODE_ANY) |
| **FLEXI_DL_LIMIT_WINDOW**<br />`dl_limit_window` | FLEXI_DL_LIMIT_WINDOW_DESC | `number` | — | `24` |
| **FLEXI_DL_LIMIT_WINDOW_UNIT**<br />`dl_limit_window_unit` | FLEXI_DL_LIMIT_WINDOW_UNIT_DESC | `list` | `1` = FLEXI_DL_LIMIT_UNIT_MINUTES<br />`60` = FLEXI_DL_LIMIT_UNIT_HOURS<br />`1440` = FLEXI_DL_LIMIT_UNIT_DAYS | `60` (FLEXI_DL_LIMIT_UNIT_HOURS) |
| **FLEXI_DL_LIMIT_GROUPS**<br />`dl_limit_groups` | FLEXI_DL_LIMIT_GROUPS_DESC | `subform` | — | — |
| **FLEXI_DL_LIMIT_IP_FACTOR**<br />`dl_limit_guest_ip_factor` | FLEXI_DL_LIMIT_IP_FACTOR_DESC | `number` | — | `5` |
| **FLEXI_DL_LIMIT_COUNT_SPECIAL**<br />`dl_limit_count_special` | FLEXI_DL_LIMIT_COUNT_SPECIAL_DESC | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **FLEXI_DL_LIMIT_MODAL_HTML**<br />`dl_limit_modal_html` | FLEXI_DL_LIMIT_MODAL_HTML_DESC | `textarea` | — | — |

#### Actions fichier

### Affichage fichier

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Affichage compact**<br />`compact_display` | Affichage compact des informations de fichiers et des actions de fichiers pour économiser de l'espace. | `radio` | `0` = Non<br />`1` = Oui<br />`2` = Oui, comme une icône. | `0` (Non) |
| **Placement de la liste de valeurs**<br />`values_list_placement` | La liste de valeurs peut être placée en ligne, ou à l'intérieur d'un accordéon | `multilist` | `0` = En ligne<br />`1` = Dans un slider | `0` (En ligne) |
| **Titre de l'accordéon**<br />`values_slider_title` | Vous pouvez personnaliser le titre de l'accordéon | `text` | — | `FLEXI_FILES` (Fichiers) |

#### Total des fichiers

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre de fichiers**<br />`display_total_count` | Activer cette option pour afficher le nombre total de fichier | `multilist` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |
| **Libellé du total des fichiers**<br />`total_count_label` | Texte de libellé personnalisé | `text` | — | `FLEXI_FIELD_FILE_TOTAL_FILES` (Total de fichiers) |
| **Compteur de téléchargement**<br />`display_total_hits` | Activer cette option pour afficher la somme du nombre de téléchargements (clic) | `multilist` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |
| **Libellé du total des téléchargements**<br />`total_hits_label` | Texte de libellé personnalisé | `text` | — | `FLEXI_FIELD_FILE_TOTAL_DOWNLOADS` (Téléchargements total) |

#### Fichiers individuels

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser l'icône mime**<br />`useicon` | Ajouter l'icône mime devant le nom du fichier. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher le nom du fichier**<br />`display_filename` | Afficher le nom du fichier (Remarque: vous pouvez afficher un lien sur le nom du fichier seulement si vous n'utilisez pas l'option bouton) | `radio` | `-1` = No (force)<br />`0` = Non<br />`1` = Oui, privilégier le titre du fichier<br />`2` = Oui | `1` (Oui, privilégier le titre du fichier) |
| **Nom de fichier en minuscule**<br />`lowercase_filename` | Forcer le nom du fichier à être écrit en minuscule | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Lier le nom de fichier**<br />`link_filename` | Ajoute un lien de téléchargement sur le nom de fichier. NOTE/ option ignorée si les boutons sont utilisés à la place des liens | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Informations

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la langue**<br />`display_lang` | Afficher le fichier de langue. C'est utile si vous avez différentes langues à l'intérieur d'un même article. | `radio` | `0` = Non<br />`1` = Oui, comme une icône.<br />`2` = Oui, comme un texte.<br />`3` = En partie publique et dans l'administration | `1` (Oui, comme une icône.) |
| **Afficher la taille**<br />`display_size` | Afficher la taille du fichier. Cela peut être soit en Ko / Mo / Go | `radio` | `0` = Non<br />`1` = Oui, comme une icône.<br />`2` = Oui, comme un texte.<br />`3` = En partie publique et dans l'administration | `0` (Non) |
| **Afficher les résultats**<br />`display_hits` | Afficher les résultats | `radio` | `0` = Non<br />`1` = Oui, comme une icône.<br />`2` = Oui, comme un texte.<br />`3` = En partie publique et dans l'administration | `0` (Non) |
| **Afficher la description**<br />`display_descr` | Afficher la description comme une bulle d'aide OU comme un texte simple | `radio` | `0` = Non<br />`1` = Oui, comme un popup info-bulle<br />`2` = Oui, comme un texte en ligne. | `1` (Oui, comme un popup info-bulle) |

#### Information caractère(s) de séparation

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser un ou des caractères de séparation**<br />`use_info_separator` | Si vous préférez utiliser un style css, plutôt qu'un caractère de séparation, pour l'affichage des éléments | `multilist` | `0` = Saut de ligne<br />`1` = Personnalisé | `0` (Saut de ligne) |
| **Personnalisé**<br />`info_separator` | Caractère(s) de séparation entre les informations affichées | `text` | — | — |

### Liste fichier

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

## Notifications

Option à activer pour envoyer des notifications emails lorsqu'un fichier est téléchargé

#### Notifications Email tous les N téléchargements

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Envoyer des notifications sur le nombre de clics**<br />`send_notifications` | Option à activer pour envoyer des notifications emails lorsqu'un fichier est téléchargé | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Tous les N affichages**<br />`notifications_step` | Envoyer un e-mail tous les N affichages | `text` | — | `20` |
| **Texte de notification**<br />`notification_tmpl` | Texte qui sera envoyé pour chaque fichier. **Remarque :** vous pouvez utiliser ces remplacements : %%language_string%%, __file_id__ __file_name__ __item_title__ __item_url__ | `textarea` | — | `%%FLEXI_HITS%% __FILE_HITS__ %%FLEXI_FDN_FILE_NO%% __FILE_ID__: [__FILE_TITLE__] %%FLEXI_FDN_FILE_IN_ITEM%% __ITEM_TITLE__: __ITEM_URL__` |

#### Envoyer à

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **aux e-mails spécifiques**<br />`send_all_to_email` | Les notifications pour tous fichier seront envoyées à ces email(s) séparés par des virgules, | `text` | — | — |
| **Au propriétaire du contenu de l'article**<br />`send_to_current_item_owner` | Envoyer un mail au propriétaire du contenu de l'article d'où le fichier est téléchargé | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **aux emails du champ EMAIL**<br />`send_to_email_field` | Le champ email doit avoir une ou des valeur(s) dans le MÊME élément de contenu que se trouve le champ de fichier, ex. : les champs de fichier et de e-mail sont affichés ensemble dans l'élément 'A' | `fields` | — | — |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `1` = Texte à Rechercher | `0` |
