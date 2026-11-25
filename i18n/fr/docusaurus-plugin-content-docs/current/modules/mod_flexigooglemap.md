---
sidebar_position: 7
---

# Carte Google

FLEXIcontent fournit six modules frontend pour afficher des contenus, des catégories, des formulaires de recherche, des filtres, des cartes et des nuages d’étiquettes. Configurez un module depuis **Extensions → Modules**.

> Module permettant d'afficher une carte Googlemap avec l'article en tant que marqueur, la position étant créée à partir des champs adresse de Flexicontent. Merci pour leur aide à Georgios Papadakis et Marc Studer

:::info Source
Cette page est générée depuis `modules/mod_flexigooglemap/mod_flexigooglemap.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

### Template du module

:::note
Veuillez définir les paramètres de disposition dans l’onglet **Disposition : ...**. Les développeurs CSS/HTML doivent consulter : ** Guide des modèles personnalisés **
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Template**<br />`layout` | Choisir la mise en page de votre module | `fclayout` | — | `news` |
| **Masquer la carte si vide**<br />`hide_map_when_empty` | — | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

### API de carte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Choisissez votre API**<br />`mapapi` | Choisissez votre API, si vous avez une clé Googlemap Key, vous pouvez utiliser cette api, ou choisir Openstreetmap pour une carte sans limitation | `radio` | `googlemap` = GoogleMap<br />`openstreetmap` = OpenStreetMap | `googlemap` (GoogleMap) |
| **Sélection de la catégorie**<br />`catidmode` | Utiliser la catégorie courante ou choisir une catégorie fixe dans la liste ci-dessous | `radio` | `0` = Catégories spécifiques<br />`1` = Catégorie en cours<br />`2` = Article actuel | `0` (Catégories spécifiques) |
| **Méthode**<br />`method_category` | Exclure: Affiche tous les contenu(s) excepté ceux de(s) catégorie(s) sélectionnée(s), Inclure : Affiche tous les contenu(s) des catégorie(s) sélectionnée(s) | `radio` | `0` = Inclure<br />`1` = Exclure | `0` (Inclure) |
| **Catégorie**<br />`catid` | Module qui affiche les articles comme des points sur une carte Google map en utilisant le champ adresse de FLEXIContent | `flexicategories` | — | — |
| **Catégories supplémentaires**<br />`treeinclude` | Inclure les parents/enfants des catégories sélectionnées. **NOTE**: 'autre catégories du contenu' est utilisé uniquement sur le site (frontend) pour l'affichage d'un contenu | `list` | `0` = Aucun<br />`1` = Catégories enfants<br />`5` = Catégories enfants, mais exclure les catégories sélectionnées<br />`2` = Catégories parentes<br />`3` = Catégories parentes & enfants | `1` (Catégories enfants) |
| **Champ adresse**<br />`fieldaddressid` | Insérer l'id de votre champ adresse | `fields` | — | — |
| **URL du serveur de tuiles (carte)**<br />`os_tile_server_url` | Saisir une URL de serveur de tuiles personnalisée (OpenStreetMap). Si vous prévoyez beaucoup de trafic, il est préférable d’utiliser votre propre serveur de tuiles, par ex. https://&#123;s&#125;.tile.openstreetmap.org/&#123;z&#125;/&#123;x&#125;/&#123;y&#125;.png | `text` | — | `https://&#123;s&#125;.tile.openstreetmap.org/&#123;z&#125;/&#123;x&#125;/&#123;y&#125;.png` |
| **Clé API**<br />`apikey` | Insérer votre clé API Googlemap si votre site génére plus de 25000 affichage par mois | `text` | — | — |

### Affichage de la carte

#### Conteneur de limites de la carte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur**<br />`width` | Insérer la largeur de votre carte en px | `text` | — | `300px` |
| **MOD_FLEXIGOOGLEMAP_height**<br />`height` | Insérer la hauteur de votre carte en px | `text` | — | `60vh` |

#### Configuration de base de la carte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type de carte**<br />`maptype` | Sélectionner le type de carte | `list` | `ROADMAP` = Carte routière<br />`HYBRID` = Carte Hybride<br />`SATELLITE` = Carte satellite<br />`TERRAIN` = Relief | `ROADMAP` (Carte routière) |
| **Limite du zoom**<br />`maxzoommarker` | Définir la limite du zoom lorsque la carte affiche des marqueurs non groupés (marqueurs uniques) | `number` | — | `18` |
| **Marge initiale de la carte (%)**<br />`mappadding` | Défini la distance de remplissage de la carte initiale. Il s'agit de la distance des marqueurs ou des groupes par rapport au bord de la carte. La valeur est un pourcentage de la zone de la carte | `number` | — | `50` |
| **Nombre Max de marqueur**<br />`count` | Limiter le nombre de marqueur pour accélérer l'affichage. Attention suivant les cas (taille de vos uRL ou titre) vous serez limité en nombre de point. Actuellement le script permet d'affiché environ 250 points | `list` | `—` = Affiche tous les points<br />`DESC LIMIT 10` = 10<br />`DESC LIMIT 50` = 50<br />`DESC LIMIT 100` = 100<br />`DESC LIMIT 150` = 150<br />`DESC LIMIT 200` = 200<br />`DESC LIMIT 250` = 250<br />`DESC LIMIT 300` = 300<br />`DESC LIMIT 350` = 350<br />`DESC LIMIT 400` = 400<br />`DESC LIMIT 450` = 450<br />`DESC LIMIT 500` = 500<br />`DESC LIMIT 1000` = 1000 | — |

#### Options de géolocalisation

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Zoomer la carte sur le visiteur**<br />`geo_locate` | Au chargement, la carte sera centrée sur la position du visiteur | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Bouton « Près de moi »**<br />`geo_locate_btn` | Ajouter un bouton pour recentrer la carte sur la position du visiteur | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Sélection du zoom « Près de moi »**<br />`geo_locate_zoom_sel` | Ajouter un sélecteur de niveau de zoom vers la position du visiteur | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Zoom par défaut pour « Near Me »**<br />`geo_locate_zoom_def` | Niveau de zoom par défaut pour la géolocalisation « Near Me » | `number` | — | `10` |

#### Affichage maqueur

:::note
Par marqueur personnalisé (via le formulaire de l'élément), et une icône de secours (par défaut) qui sera utilisée pour les emplacements sans icône personnalisée
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Par emplacement**<br />`use_custom_marker` | Utiliser une icône personnalisée par emplacement sur la carte, si cela a été spécifié dans le formulaire de contenu. L'icône par défaut sera utilisée pour les emplacements sans icône personnalisée | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Remplacement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Marqueur par défaut**<br />`markermode` | Choisissez une image spécifique, ou choisissez le mode lettre pour créer un marqueur avec une lettre | `radio` | `-1` = Icône par défaut de l'API<br />`0` = Image spécifique<br />`1` = Mode lettre | `-1` (Icône par défaut de l'API) |
| **Image spécifique**<br />`markerimage` | Choisissez où charger l'image pour vos marqueurs | `fcmedia` | — | — |
| **Couleur du marqueur**<br />`markercolor` | Choissez la couleur du marqueur en mode lettre | `list` | `red` = Rouge<br />`green` = Vert | `redpt` |
| **Lettre marqueur**<br />`lettermarker` | Insérer la lettre souhaitée pour vos marqueurs | `text` | — | `A` |

#### Comportement et apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Zoom par la molette de défilement**<br />`usescrollmouse` | Activer désactiver le zoom par la molette de défilement | `radio` | `false` = Non<br />`true` = Oui | `true` (Oui) |
| **Animation**<br />`animationmarker` | Si cette option est sur oui alors les marqueurs auront une animation de rebond à l'affichage de la carte. Ne fonctionne pas pour les groupes de points | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Style Carte Générateur**<br />`mapstyle` | Copier coller le code JSON créer par Snazzy map. Attention de bien utiliser les [ ] en dévut et fin de valeur _[Your style code]_ | `textarea` | — | — |

#### Groupe de marqueur

:::note
Regrouper les marqueurs en un nombre total, afin d’éviter que de nombreux marqueurs très proches ne s’affichent
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Grouper les marqueurs**<br />`clustermode` | Cette option regroupe les marqueurs dans la même zone (zone) en un seul. Le nombre total de marqueurs sera affiché lorsque la carte est agrandie | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Image marqueur**<br />`imgcluster` | Définir une image pour l'icône du cluster (uniquement pour l'api de Googlemap) | `fcmedia` | — | — |
| **Taille Grille**<br />`gridsize` | Taille de la grille qui regroupe les marqueurs entre eux. Plus la grille est grande plus les points seront regroupés entre eux en 1 seul marqueur | `text` | — | `50` |
| **Niveau de zoom pour le groupe**<br />`maxzoom` | Le niveau de zoom à partir duquel l'effet cluster sera activé, si l'utilisateur zoom plus que cette limite alors, l'effet cluster sera désactivé. | `text` | — | `17` |

### Actions sur les marqueurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Action au clic**<br />`info_popup` | Action à effectuer lors du clic sur le marqueur | `multilist` | `0` = Aucune<br />`1` = Fenêtre d’informations<br />`2` = Lien vers le contenu | `1` (Fenêtre d’informations) |
| **Fenêtre cible**<br />`marker_clicktarget` | Ouvrir le lien dans | `multilist` | `—` = - Pas de cible -<br />`_blank` = Nouvelle fenêtre/onglet<br />`_parent` = Fenêtre Parente<br />`_self` = Même fenêtre/onglet<br />`_top` = Haut de fenêtre<br />`_popup` = Fenêtre modale en popup<br />`_modal` = Popup Html (sans js) | `_popup` (Fenêtre modale en popup) |

#### Options de la fenêtre modale / pop-up

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Template de contenu**<br />`ilayout` | Définissez un template personnalisé pour ce contenu | `itemlayout` | — | — |
| **Largeur**<br />`modal_width` | Insérer la largeur de votre carte en px | `number` | — | — |
| **Hauteur**<br />`modal_height` | Définir la hauteur de la fenêtre modale /popup . Laisser vide pour la taille plein écran | `number` | — | — |

#### Infos bulles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage personnalisé**<br />`info_windows_custom_display` | Par défaut, identique aux fenêtres contextuelles | `radio` | `0` = Même affichage que la liste des marqueurs | `0` (Même affichage que la liste des marqueurs) |

### Liste des marqueurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la liste des marqueurs**<br />`use_dynamic_marker_list` | Afficher et mettre à jour dynamiquement une liste des marqueurs actuellement visibles selon la zone affichée de la carte. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Synchroniser la liste des marqueurs avec les marqueurs visibles**<br />`marker_list_update_to_map_bounds` | Synchroniser la liste des marqueurs pour n’afficher que ceux visibles dans les limites de la carte | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Retour à la ligne de la liste des marqueurs

:::note
Largeur à partir de laquelle la liste des marqueurs passe à la ligne
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Limite de retour à la ligne de la liste des marqueurs (pixels)**<br />`marker_list_wrap_limit` | À cette largeur, la liste des marqueurs passe sous la carte | `text` | — | `1200` |
| **Hauteur lors du retour à la ligne (carte)**<br />`map_height_wrapped` | Insérer la hauteur de votre carte en px | `text` | — | `45vh` |
| **Hauteur lors du retour à la ligne (liste des marqueurs)**<br />`marker_list_height_wrapped` | Insérer la hauteur de votre carte en px | `text` | — | `45vh` |

#### Options de la liste des marqueurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage des informations du marqueur**<br />`infotextmode` | Description de l’affichage des informations du marqueur | `radio` | `0` = Basique<br />`1` = HTML personnalisé | `0` (Basique) |
| **Adresse**<br />`useadress` | Si cette option est sur oui alors l'adresse sera affichée dans l'info bulle | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **HTML personnalisé avec remplacements de champs**<br />`custom_html_with_replacements` | Description du HTML personnalisé avec remplacements de champs | `editor` | — | `&#123;item-&gt;title&#125; &#123;__address__&#125;` |

#### Utiliser le lien « Lire la suite »

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher**<br />`uselink` | Description de l’utilisation du lien « Lire la suite » | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Cible du lien**<br />`linkmode` | L'option nouvelle fenêtre permet d'ouvrir le lien de l'article dans une nouvelle fenêtre, sinon ce sera dans la même | `radio` | `_blank` = Nouvelle fenêtre<br />`—` = Même fenêtre | — |
| **Forcer l'itemid**<br />`forced_itemid` | En insérant un itemid dans ce champ vous pourrez gérer l'affichage de la page affichée via le lien lire la suite. | `text` | — | — |
| **Texte lire la suite**<br />`readmore` | Modifier le texte de lire la suite. FLEXI_GOOGLEMAP_READMORE_TXT est la valeur par défaut directement traduite _Lire la suite_ | `text` | — | — |

#### Bouton de direction

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher**<br />`usedirection` | Mod flexigooglemap usedirection btn description | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Nom du lien**<br />`directionname` | Permet de changer le nom du lien d'itinéraire. Vous pouvez utiliser FLEXI_GOOGLEMAP_DIRECTIONNAME_TXT pour un site multilangue _Itinéraires_ | `text` | — | — |

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

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Cache du champ Modules**<br />`cache` | Description du cache du champ Modules | `list` | `1` = Utiliser la configuration globale<br />`0` = Valeur du champ Modules sans cache | `1` (Utiliser la configuration globale) |
