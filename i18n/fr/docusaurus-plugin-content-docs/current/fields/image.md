---
sidebar_position: 21
---

# Image / galerie

Plugin de champ 'Image' pour FLEXIcontent

*Plugin : `image` — Image ou galerie*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/image/image.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Édition

#### Édition

### Valeurs

:::note
Remarque : Le source de l'image sera le Média Manager ou le mode image Intro/complet. Exceptions : Afficher le libellé, le message de non accès
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le champ dans un groupe**<br />`use_ingroup` | Activer pour permettre d'utiliser ce champ dans un groupe, qui sera configuré via champ 'Groupe de champ'. REMARQUE: Vous devez alors sélectionner ce champ UNIQUEMENT dans un groupe de champs | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Nombre de valeurs

:::note
Utiliser une image simple (agir comme un champ image) ou images multiples (agir comme une gallerie)
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser les valeurs multiples**<br />`allow_multiple` | Autoriser plus d'1 valeur pour ce champs | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs par colonne**<br />`fields_box_placing` | Économiser de l'espace en autorisant l'affichage par ligne de valeurs multiples | `radio` | `0` = 1<br />`1` = Multiple | `1` (Multiple) |
| **Position Ajouter**<br />`add_position` | Sélectionnez pour ajouter le bouton en ligne (bouton d'ajout de valeur à chaque ligne) ou afficher le bouton d'ajout au fond de la liste de valeurs | `multilist` | `0` = Bouton Ajouter en bas<br />`1` = Bouton ajouter avant<br />`2` = Bouton Ajouter après<br />`3` = Les deux (avant - après) | `3` (Les deux (avant - après)) |
| **Nb maximum de valeurs**<br />`max_values` | Définissez ici le nombre maximum de valeurs que l'utilisateur pourra saisir. 0 pour illimité. | `text` | — | `0` |
| **Affichage conditionnel**<br />`showon` | Affiché en fonction de conditions. Utilisez le format Joomla 'fieldname:value' comme par exemple album_type:2 REMARQUE: ne pas définir ce champ en obligatoire. Également DÉSACTIVER les scripts prettyCheckable / Select2 JS dans tous les champs référencés de type select*, checkbox*, radio* | `text` | — | — |
| **Obligatoire**<br />`required` | Définit si le champ doit être obligatoire dans le formulaire de saisie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Manipulation des images

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Extensions autorisées**<br />`upload_extensions` | Les extensions (types de fichier) que vous êtes autorisés à envoyer pour une image (séparé par virgule). | `text` | — | `bmp,wbmp,gif,jpg,jpeg,png,webp,ico` |
| **Taille maximum**<br />`upload_maxsize` | Spécifie la taille maximum d'un fichier qui peut être uploadé sur le site (en octet). Utiliser 0 pour ne mettre aucune limite. NOTE : la taille maximum dépend également de la configuration de votre serveur. | `text` | — | `10000000` |

#### Lien vers une URL

:::note
Si vous activez cette option, vous pourrez ajouter un lien personnalisé sur la miniature. Note : la popup de l'image ne sera pas utilisé.
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`linkto_url` | — | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Cible du lien**<br />`url_target` | Sélectionner la cible du lien personnalisé | `groupedlist` | `_self` = Même fenêtre/onglet<br />`_blank` = Nouvelle fenêtre/onglet<br />**Fenêtre modale en popup**<br />`multibox` = Multibox (popup Joomla)<br />`fancybox` = Fancybox (pré-installé) | `_self` (Même fenêtre/onglet) |

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

#### Boutons

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Fichier à transmettre / Sélectionner**<br />`file_btns_position` | Choisir comment et où afficher la sélection de fichier et le bouton d'envoi | `multilist` | `0` = Icônes<br />`1` = Icônes, sur une nouvelle ligne<br />`2` = Icônes + texte, sur une nouvelle ligne | `0` (Icônes) |

#### Miniatures

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Redimensionner**<br />`thumb_size_resizer` | Afficher une sélection déroulante ou un curseur pour redimensionner les vignettes | `radio` | `0` = Désactiver<br />`1` = Sélecteur liste déroulante<br />`2` = Slider | `0` (Désactiver) |
| **Taille par défaut**<br />`thumb_size_default` | À noter que cela est utilisé uniquement lors de la première ouverture du formulaire, puis le dernier paramètre du redimensionnement des vignettes est mémorisé | `radio` | `90` = 90<br />`120` = 120<br />`150` = 150<br />`200` = 200<br />`250` = 250 | `200` (200) |
| **Méthode de traitement**<br />`thumb_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |

### Source de l'image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Source de l'image**<br />`image_source` | **Ne pas changer après que des valeurs aient été ajoutées, le mode dossier est recommandé pour les champs de gallerie d'images** a. Utiliser **le mode DB**, lorsque vous utilisez des images que vous allez réutiliser par plusieurs contenus b. Utilisez **le mode dossier**, quand vous utilisez des images dans un seul contenu. | `multilist` | `-2` = Gestionnaire de médias Joomla<br />`-1` = Images d’article Joomla : (intro + texte complet)<br />`0` = Réutilisable (mode DB)<br />`1` = Dossier contenu/champ (mode dossier) | `1` (Dossier contenu/champ (mode dossier)) |

:::note
À propos du dossier racine (Joomla 4+ uniquement) - vous devez ajouter ce dossier dans le plugin **FileSystem - Local**, par exemple le dossier downloads. - Pour le gestionnaire Quantum, il s’agit du nom de portée. REMARQUE : ajoutez une portée personnalisée supplémentaire pour le dossier images, par exemple « imgs ». NE modifiez PAS le nom du dossier « images » ; « imgs » sera le nom de la portée personnalisée
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Dossier racine**<br />`jmedia_topdir` | Pour le gestionnaire de médias natif, il s’agit du dossier situé dans la racine Joomla (ajouté dans le plugin Filestorage). Pour le gestionnaire Quantum, il s’agit du nom de portée personnalisé _images_ | `text` | — | — |
| **Chemin du sous-dossier**<br />`jmedia_subpath` | Sélectionner le sous-dossier à ouvrir, par exemple content/news -&gt; JPATH_ROOT/images/content/news_ | `text` | — | — |
| **Insertion automatique des images**<br />`autoassign` | Activer cette option pour affecter automatiquement les nouvelles images chargées au contenus. Remarque : Si plusieurs images sont chargées en même temps, alors elles seront automatiquement ajoutés en tant que valeur dans le contenu | `radio` | `0` = Non<br />`1` = Sélectionner et assigner<br />`2` = Sélectionnée(s) uniquement | `1` (Sélectionner et assigner) |
| **Prise en charge de l’intro / du texte complet**<br />`auto_intro_full` | Assigne automatiquement les miniatures de taille et moyen et grande (de ce champs) en tant qu'image d'intro(texte) et de complet(texte) | `radio` | `0` = Non<br />`1` = Utiliser les premières vignettes d’image | `0` (Non) |

:::note
Note : Les options des onglets 'valeurs' et 'Propriétés optionnelles' ne seront utilisés
:::

#### Miniatures dans la vue

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Contenu**<br />`img-if-for-itemlist` | — | `radio` | `1` = Intro<br />`2` = Complet | `2` (Complet) |
| **Catégorie**<br />`img-if-for-catlist` | — | `radio` | `1` = Intro<br />`fulltext` = Complet | `1` (Intro) |
| **Module**<br />`img-if-for-modlist` | — | `radio` | `1` = Intro<br />`2` = Complet | `1` (Intro) |

### Mode dossier - Paramètres spécifiques

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Même image pour les éléments associés**<br />`of_usage` | Si le contenu appartient à des contenus traduits et associés, le champ utilisera les même images. Remarque : le dossier d'image partagé sera celui de la langue par défaut du site sera utilisé pour stocker des images | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Protéger l'accès à l'image originale**<br />`protect_original` | Habituellement, vous voulez empêcher l'accès aux fichiers images originaux (ce paramètre est pour le mode de dossier, ** dans le cas du mode de DB ils sont toujours protégés ). Si vous utilisez des images originales dans divers paramètres de configuration, alors vous devez désactiver ce paramètre, sinon vos liens d'image obtiendront une erreur server deny error | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

### Mode DB - Paramètres spécifiques

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Répertoire cible**<br />`target_dir` | Si vous sélectionnez sécurisé, les utilisateurs ne verront jamais le chemin réel du fichier et ne seront autorisés **qu'à un accès indirect**au fichier. Cette option convient pour, par exemple, - fichiers de document * - images haute résolution protégées par le droit d'auteur * * joindre le contenu via le champ **FICHIER** ** joindre le contenu via le champ **FICHIER** ou le champ **image/galerie** REMARQUE: 1. Si vous sélectionnez un dossier multimédia, l'accès direct sera autorisé et vous pourrez ainsi lire des fichiers multimédia via des lecteurs multimédias intégrés au navigateur du visiteur. 2. Les fichiers image du dossier sécurisé privilégie un accès via un champ de fichier ou peuvent être visualisés à l'aide de miniatures (éventuellement dotées d'un filigrane) créées par le champ image/galerie. Vous conserverez ainsi la protection du téléchargement sécurisé. | `multilist` | `0` = Média<br />`1` = Sécurisé | `1` (Sécurisé) |
| **Effacer automatiquement les images non utilisées**<br />`auto_delete_unused` | Les images qui ne sont plus utilisées seront automatiquement supprimés. Automatique: supprime les images non utilisées, - si la liste de sélection d'image existante est cachée, - si la liste de sélection d'image existante est limitée aux images utilisées par ce champ | `radio` | `0` = Auto<br />`1` = Oui | `1` (Oui) |

#### Liste des images existantes

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Inclure, ajouter par ***<br />`list_all_media_files` | Actif/désactive l'inclusion des images envoyées par les autres champs ou via le gestionnaire de fichiers (aka toutes les images dans le dossier sécurisé) NOTE 1 : le champ image ne stocke pas dans le dossier Media de la BDD, mais dans le dossier Secure pour permettre d'empècher l'accès au fichier original si besoin. NOTE 2 : Vous pouvez choisir d'ajouter automatiquement _fldNN_ dans les noms des miniatures, ou choisir d'utiliser un dossier de miniatures unique, mais soyez certains d'avoir défini un dossier pour ce champ !! Sans quoi les champs vont continuellement écraser les minatures des uns et des autres. NOTE 3 : Si vous activez la sélection des images ajoutées par n'importe quel champ ou gestionnaire de fichier, alors la suppression sera désactivée | `multilist` | `0` = Ce champ<br />`1` = Tout les fichiers | `0` (Ce champ) |
| **Inclure charger par**<br />`limit_by_uploader` | Dans la liste des fichiers, faire apparaitre les fichiers de tous les utilisateurs (recommandé) ou uniquement ceux de l'utilisateur actif | `radio` | `1` = Utilisateur courant<br />`0` = N'importe quel utilisateur | `0` (N'importe quel utilisateur) |

### Redimensionner automatiquement les images

:::note
Redimensionnement se fera au niveau du navigateur de l’utilisateur, ainsi vous obtenez un téléchargement plus rapide et moins de consommation sur l’espace serveur
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Redimensionnement**<br />`resize_on_upload` | Redimensionner une image téléchargée afin d'économiser de l’espace sur le serveur et d'accélérer les téléchargements, cela sera la taille pour le client (tous les modes ne supportes pas cette fonction) | `multilist` | `—` = Utiliser les paramètres du composant<br />`0` = Non<br />`1` = Oui | — |
| **Largeur de l'image**<br />`upload_max_w` | — | `text` | — | — |
| **Hauteur de l'image**<br />`upload_max_h` | — | `text` | — | — |
| **Méthode de traitement**<br />`upload_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `—` = Utiliser les paramètres du composant<br />`0` = A l'échelle<br />`1` = Découper | — |

### URL du média

:::note
VEUILLEZ NOTER : si l’URL média est activée, la disposition **fancybox** sera forcée, sauf si la disposition **GLightbox** est sélectionnée (elle prend en charge nativement les URL de vidéo)
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_mediaurl` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Video URLs (Youtube, Vimeo)<br />`2` = Any URL | `0` (Non) |
| **Par défaut**<br />`default_mediaurl` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`mediaurl_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

### Propriétés optionnelles

:::note
Remarque : Le source de l'image sera le Média Manager ou le mode image Intro/complet. Les options de cet onglet ne seront pas utilisés
:::

#### Texte alternatif

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_alt` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Par défaut**<br />`default_alt` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`alt_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### Titre de l'info-bulle

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_title` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Par défaut**<br />`default_title` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`title_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### Description Tooltip

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_desc` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Par défaut**<br />`default_desc` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`text_desc` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### PERSONNALISÉ 1

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_cust1` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Par défaut**<br />`default_cust1` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`cust1_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### PERSONNALISÉ 2

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_cust2` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Par défaut**<br />`default_cust2` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`cust2_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

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
| **FLEXI_FIELD_IMAGE_CSV_EXPORT_FORMAT**<br />`csv_export_format` | FLEXI_FIELD_IMAGE_CSV_EXPORT_FORMAT_DESC | `radio` | `html` = FLEXI_FIELD_IMAGE_CSV_EXPORT_FORMAT_HTML<br />`importable` = FLEXI_FIELD_IMAGE_CSV_EXPORT_FORMAT_IMPORTABLE | `html` (FLEXI_FIELD_IMAGE_CSV_EXPORT_FORMAT_HTML) |

#### FLEXI_BACKEND_VIEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_BACKEND_VIEW_APPEARANCE**<br />`backend_view_appearance` | FLEXI_BACKEND_VIEW_APPEARANCE_DESC | `multilist` | `0` = Par défaut<br />`1` = FLEXI_CHECK_MARK<br />`2` = FLEXI_CLEAN_HTML_AND_TRIM | `0` (Par défaut) |
| **FLEXI_TRIM_LENGTH**<br />`backend_view_trim_chars` | FLEXI_TRIM_LENGTH_DESC | `text` | — | `100` |

### Vignettes

### Création des miniatures

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Image par défaut**<br />`default_image` | Spécifiez le chemin de l'image que vous souhaitez afficher lorsque le champ n'a aucune valeur. **NOTE**: Laissez vide pour n'afficher aucune image. Spécifier le chemin relatif de l'image par rapport au site Joomla : ex. images/stories/default/mylogo.png | `media` | — | — |
| **Image par défaut via code personnalisé**<br />`default_image_custom` | Exécuter un code personnalisé pour obtenir l’image par défaut | `multilist` | `0` = Non<br />`2` = Utiliser du code personnalisé | `0` (Non) |
| **Code personnalisé**<br />`default_image_custom_code` | Entrez le code PHP à utiliser pour créer la valeur personnalisée, veuillez vider ce champs et enregistrez pour charger l'exemple par défaut, puis personnaliser | `editor` | — | `alias . '.jpg';` |
| **Répertoire des miniatures * Le mode dossier va créer des sous répertoires pour chaque contenu**<br />`dir` | Le répertoire où sont stockés les miniatures, **relatif au site Joomla**, (aucun slash au début et à la fin) Si **le mode dossier** est activé, alors **les sous répertoires** seront créés pour chaque contenu, et par ailleurs les fichiers originaux seront remplacés ici par le dossier des fichiers sécurisés de FLEXIcontent | `text` | — | `images/stories/flexicontent` |
| **Miniature unique via**<br />`unique_thumb_method` | Lorsque des images sont partagées entre les champs, nous devons empêcher les champs d'écraser les miniatures des uns et des autres. Vous pouvez choisir de selectionner soit d'ajouter **automatiquement** _fldNN_ dans les noms des miniatures, ou choisir d'untiliser un dossier de miniature unique, que vous devrez saisir ci-dessous **manuellement** | `radio` | `0` = Id du champ (automatique)<br />`1` = Dossier des miniatures (à choisir manuellement) | `0` (Id du champ (automatique)) |
| **Qualité des miniatures**<br />`quality` | Qualité de la miniature. Ce paramètre affecte le taux de compression JPG. Une valeur importante augmentera la qualité et la taille du fichier. | `text` | — | `90` |

#### FLEXI_IMGFIELD_WEBP_GENERATION

:::note
FLEXI_IMGFIELD_WEBP_NOTE
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_IMGFIELD_GENERATE_WEBP**<br />`generate_webp` | FLEXI_IMGFIELD_GENERATE_WEBP_DESC | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **FLEXI_IMGFIELD_WEBP_QUALITY**<br />`webp_quality` | FLEXI_IMGFIELD_WEBP_QUALITY_DESC | `text` | — | `80` |

#### Image du filigrane

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Transparence droits d'auteurs**<br />`wm_opacity` | Choisissez le pourcentage de transparence de l'image des droits d'auteurs. Pour un meilleur résultat, laisser 100% et ajuster plutôt la transparence dans le fichier d'origine. | `text` | — | `100` |
| **Postion du filigrane**<br />`wm_position` | Choisir position des droits d'auteurs. | `list` | `*` = Répéter<br />`C` = Milieu<br />`TL` = Haut gauche<br />`T` = Haut centré<br />`TR` = Haut droite<br />`BL` = Bas Gauche<br />`B` = Bas Centré<br />`BR` = Bas Droite | `BR` (Bas Droite) |

#### Grandes miniatures

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur Miniature**<br />`w_l` | Largeur maximum de la miniature | `text` | — | `800` |
| **Hauteur de la miniature**<br />`h_l` | Hauteur maximum de la miniature | `text` | — | `600` |
| **Définir la largeur de la miniature comme**<br />`l_thumb_width_as_min_or_max` | Définir la taille de l'image comme largeur minimale ou comme largeur maximale | `radio` | `0` = Largeur Minimum<br />`1` = Largeur max | `0` (Largeur Minimum) |
| **Méthode de traitement**<br />`method_l` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `0` = A l'échelle<br />`1` = Découper | `0` (A l'échelle) |
| **Utiliser le filigrane**<br />`use_watermark_l` | Utiliser un filigrane pour afficher en surimpression les droits d'auteurs. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Image du filigrane**<br />`wm_l` | Choisir le fichier PNG que vous souhaitez utiliser pour vos droits d'auteurs. Le chemin est relatif à votre site Joomla!. Ne saisir aucun slash au début et à la fin !!! | `text` | — | `plugins/flexicontent_fields/image/image/watermarks/wm_l.png` |
| **Copier l'original ***<br />`copy_original_l` | Copier l'original si la largeur et la hauteur de la miniature original correspodent et que les droits d'auteurs sont désactivés | `radio` | `0` = Non<br />`1` = Oui<br />`2` = Oui, peu importe les paramètres | `1` (Oui) |

#### Moyennes miniatures

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur Miniature**<br />`w_m` | Largeur maximum de la miniature | `text` | — | `400` |
| **Hauteur de la miniature**<br />`h_m` | Hauteur maximum de la miniature | `text` | — | `300` |
| **Définir la largeur de la miniature comme**<br />`m_thumb_width_as_min_or_max` | Définir la taille de l'image comme largeur minimale ou comme largeur maximale | `radio` | `0` = Largeur Minimum<br />`1` = Largeur max | `0` (Largeur Minimum) |
| **Méthode de traitement**<br />`method_m` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `0` = A l'échelle<br />`1` = Découper | `0` (A l'échelle) |
| **Utiliser le filigrane**<br />`use_watermark_m` | Utiliser un filigrane pour afficher en surimpression les droits d'auteurs. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Image du filigrane**<br />`wm_m` | Choisir le fichier PNG que vous souhaitez utiliser pour vos droits d'auteurs. Le chemin est relatif à votre site Joomla!. Ne saisir aucun slash au début et à la fin !!! | `text` | — | `plugins/flexicontent_fields/image/image/watermarks/wm_m.png` |
| **Copier l'original ***<br />`copy_original_m` | Copier l'original si la largeur et la hauteur de la miniature original correspodent et que les droits d'auteurs sont désactivés | `radio` | `0` = Non<br />`1` = Oui<br />`2` = Oui, peu importe les paramètres | `1` (Oui) |

#### Petites miniatures

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur Miniature**<br />`w_s` | Largeur maximum de la miniature | `text` | — | `120` |
| **Hauteur de la miniature**<br />`h_s` | Hauteur maximum de la miniature | `text` | — | `90` |
| **Définir la largeur de la miniature comme**<br />`s_thumb_width_as_min_or_max` | Définir la taille de l'image comme largeur minimale ou comme largeur maximale | `radio` | `0` = Largeur Minimum<br />`1` = Largeur max | `0` (Largeur Minimum) |
| **Méthode de traitement**<br />`method_s` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |
| **Utiliser le filigrane**<br />`use_watermark_s` | Utiliser un filigrane pour afficher en surimpression les droits d'auteurs. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Image du filigrane**<br />`wm_s` | Choisir le fichier PNG que vous souhaitez utiliser pour vos droits d'auteurs. Le chemin est relatif à votre site Joomla!. Ne saisir aucun slash au début et à la fin !!! | `text` | — | `plugins/flexicontent_fields/image/image/watermarks/wm_s.png` |
| **Copier l'original ***<br />`copy_original_s` | Copier l'original si la largeur et la hauteur de la miniature original correspodent et que les droits d'auteurs sont désactivés | `radio` | `0` = Non<br />`1` = Oui<br />`2` = Oui, peu importe les paramètres | `1` (Oui) |

#### Miniatures de l'administration

:::note
Veillez editer la configuration du Composant, ou la configuration du type pour sélectionner colonnes personnalisés pour le gestionnaire de contenu
:::

:::note
Remarque : Ce ne sera pas utiliser dans le formulaire de contenu, pour configuré la prévisualistion des miniature dans le formulaire, veillez utiliser l'onglet 'édition'
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur Miniature**<br />`w_b` | Largeur maximum de la miniature | `text` | — | `40` |
| **Hauteur de la miniature**<br />`h_b` | Hauteur maximum de la miniature | `text` | — | `30` |
| **Méthode de traitement**<br />`method_b` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |
| **Utiliser le filigrane**<br />`use_watermark_b` | Utiliser un filigrane pour afficher en surimpression les droits d'auteurs. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Image du filigrane**<br />`wm_b` | Choisir le fichier PNG que vous souhaitez utiliser pour vos droits d'auteurs. Le chemin est relatif à votre site Joomla!. Ne saisir aucun slash au début et à la fin !!! | `text` | — | `plugins/flexicontent_fields/image/image/watermarks/wm_s.png` |
| **Copier l'original ***<br />`copy_original_b` | Copier l'original si la largeur et la hauteur de la miniature original correspodent et que les droits d'auteurs sont désactivés | `radio` | `0` = Non<br />`1` = Oui<br />`2` = Oui, peu importe les paramètres | `1` (Oui) |

### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pré-configuration**<br />`prx_sfx_open_close_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage) | — |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

:::note
Non applicable aux galeries en ligne (sans fenêtre modale) comme Elastislide / Galleriffic
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Séparateur de valeurs (vues frontend)**<br />`separatorf` | Choisir le séparateur pour séparer l'ensemble des valeurs dans l'affichage frontend (placé entre les valeurs) | `list` | `0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | `0` (Espace) |
| **Texte d'ouverture**<br />`opentag` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

### Mise en Page

#### Vue contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode d'affichage**<br />`default_method_item` | Méthode d'affichage par défaut pour cette vue | `multilist` | `display` = Toutes les vignettes<br />`display_single` = Une seule<br />`display_single_total` = Une seule + total | `display` (Toutes les vignettes) |

#### Catégorie (liste de contenu)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode d'affichage**<br />`default_method_cat` | Méthode d'affichage par défaut pour les listes multi-contenus ; souvent, vous voudrez afficher une seule image qui renvoie vers le détail dans la vue contenu | `multilist` | `display` = Toutes les vignettes<br />`display_single` = Une seule<br />`display_single_total` = Une seule + total<br />`display_link` = Toutes les vignettes, lien vers le contenu | `display_single` (Une seule) |
| **Lien vers le contenu**<br />`cat_link_single_to` | Habituellement, lorsque vous affichez le champ sous forme de vignette unique dans la vue catégorie, vous voudriez également un lien vers l' article en détails | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Navigation galerie

:::note
Le JavaScript de navigation de la galerie a été désactivé dans les vues contenu et catégorie, car le paramètre « Lien vers l’URL » est activé
:::

:::note
Le JavaScript de navigation de la galerie a été désactivé dans la vue catégorie, car le paramètre « Lien vers le contenu » est activé
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Gallery**<br />`usepopup` | Choisissez affichage **soit** une liste miniature simple**ou** placer vos vignettes à l'intérieur d'un popup/inline/autre mise en page de la Galerie -- la **Mise en page de la Galerie** permettra d'ouvrir les vignettes dans une popup (manuelle ou automatique) ou un diaporama / carrousel | `multilist` | `0` = Miniature seulement<br />`1` = Oui | `1` (Oui) |
| **Activer dans les vues**<br />`popupinview` | Vous pouvez activer ou désactiver le paramètre ci-dessus en fonction de la vue active de FLEXIcontent | `fccheckbox` | — | — |
| **Groupe avec les autres images**<br />`grouptype` | L'activation de cette option chainera le champ à un groupe d'images avec des boutons suivant et précédent **. Remarque : (a) Ce sera ** ignoré lorsque l'option valeur multiples sera activée. (b) Actuellement, cette option n'est pas pris en charge par Rockbox, (c) Pour Multibox dans J1.5, ce paramètre est ignoré et toutes les images du MultiBox de la page Web en cours seront regroupés. NOTE **: (a) ** Par contenu , regroupera tous les champs image de chaque élément, par exemple dans la vue catégorie les images seront regroupés par article, et bien sûr en vue d'un élément aussi, (b) ** par vue , regroupera les champs image en fonction de la vue affichée: toutes les images de l'article vue, toutes les images de vue des catégories, toutes les images de tous les modules de FLEXIcontent | `radio` | `0` = Non<br />`1` = Par contenu<br />`2` = Par vue | `1` (Par contenu) |

#### Disposition

:::note
Si « URL média » est activé, la disposition est forcée sur « fancybox », sauf pour la disposition « GLightbox » qui prend en charge nativement les URL de vidéo
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Disposition de la galerie (Pour les ordinateurs de bureau)**<br />`popuptype` | Choisissez le type d'affichage de la galerie que vous souhaitez utiliser | `fclayout` | **Popup layouts**<br />`1` = Multibox (popup Joomla)<br />`2` = Rokbox (un thème Rockettheme doit être actif)<br />`3` = JCE MediaBox (l'éditeur JCE Editor doit être installée)<br />`4` = Fancybox (pré-installé)<br />`6` = Widgetkit (composant a installé)<br />`8` = PhotoSwipe (intégré)<br />`11` = FLEXI_FIELD_IMAGE_GLIGHTBOX<br />`12` = FLEXI_FIELD_IMAGE_SWIPER<br />**Inline layouts**<br />`5` = Galleriffic (Slideshow + carrousel) (Intégré)<br />`7` = Elastislide (Slideshow + carrousel) (Intégré)<br />`9` = Pannellum (Panorama)<br />`10` = Juxtapose<br />**Activer via les paramètres**<br />`value_link_to_url` = Lien vers une URL<br />`value_link_to_item` = Lien vers le contenu<br />`value_thumbnail_basic` = Miniature seulement | `4` (Fancybox (pré-installé)) |
| **Affichage galerie (Client mobile)**<br />`popuptype_mobile` | Choisissez la mise en page de la galerie que vous voulez utiliser lorsque des clients mobiles sont détectés. Vous pouvez choisir d'utiliser les mêmes que pour des clients de bureau | `fclayout` | **Popup layouts**<br />`1` = Multibox (popup Joomla)<br />`2` = Rokbox (un thème Rockettheme doit être actif)<br />`3` = JCE MediaBox (l'éditeur JCE Editor doit être installée)<br />`4` = Fancybox (pré-installé)<br />`6` = Widgetkit (composant a installé)<br />`8` = PhotoSwipe (intégré)<br />`11` = FLEXI_FIELD_IMAGE_GLIGHTBOX<br />`12` = FLEXI_FIELD_IMAGE_SWIPER<br />**Inline layouts**<br />`5` = Galleriffic (Slideshow + carrousel) (Intégré)<br />`7` = Elastislide (Slideshow + carrousel) (Intégré)<br />`9` = Pannellum (Panorama)<br />`10` = Juxtapose<br />**Activer via les paramètres**<br />`value_link_to_url` = Lien vers une URL<br />`value_link_to_item` = Lien vers le contenu<br />`value_thumbnail_basic` = Miniature seulement | — |

#### Miniatures

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le lazyloading**<br />`use_lazy_loading` | Définir oui pour utiliser le chargement paresseux natif du navigateur | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Vue Catégorie**<br />`thumbincatview` | Quelle taille de miniature souhaitez vous utiliser dans la vue catégorie, si vous sélectionnez la grande miniature, la popup ne sera pas utilisée. | `radio` | `1` = Petite<br />`2` = Moyenne<br />`3` = Grande<br />`4` = Original | `1` (Petite) |
| **Vue contenu**<br />`thumbinitemview` | Quelle taille de miniature souhaitez vous utiliser dans la vue contenu, si vous sélectionnez la grande miniature, la popup ne sera pas utilisée. | `radio` | `1` = Petite<br />`2` = Moyenne<br />`3` = Grande<br />`4` = Original | `2` (Moyenne) |

#### Informations

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le titre**<br />`showtitle` | Afficher le titre (infobulle) avant/après image (utiliser le style CSS) | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher la description**<br />`showdesc` | Afficher la description (infobulle) avant/après image (utiliser le style CSS) | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Legend au survol

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher Infobulle**<br />`uselegend` | Afficher la légende dans une infobulle | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Activer dans les vues**<br />`legendinview` | Vous pouvez activer ou désactiver le paramètre ci-dessus en fonction de la vue active de FLEXIcontent | `fccheckbox` | — | — |

### Paramètres

### Paramètres

#### Apparence

## Réseaux sociaux

### Prise en charge des réseaux sociaux (ex. Facebook)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Suggérer le champ aux listes**<br />`useogp` | Intégrer le champ image dans l'Open Graph (og:image) | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Taille de l'image**<br />`ogpthumbsize` | Sélectionner quelle miniature à utiliser dans l'Open Graph (og:image) | `list` | `1` = Petite (non recommandé)<br />`2` = Moyenne<br />`3` = Grande<br />`4` = Original | `2` (Moyenne) |
| **Proposer des images**<br />`ogplimit` | Sélectionnez pour suggérer toutes les images disponibles aux sites sociaux ou limiter la suggestion à la première image uniquement | `radio` | `0` = Tous<br />`1` = Premier seulement | `1` (Premier seulement) |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `1` = Texte à Rechercher | `0` |
