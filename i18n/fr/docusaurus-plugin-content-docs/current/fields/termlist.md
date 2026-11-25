---
sidebar_position: 34
---

# Liste de termes

FLEXI_FIELD_TERMLIST

*Plugin : `termlist` — Liste de termes*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/termlist/termlist.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
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

#### Titre terme

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Par défaut**<br />`default_value_title` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`title_usage` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### Description du terme

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Par défaut**<br />`default_value` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`default_value_use` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |
| **Validation coté serveur**<br />`validation` | Autoriser l'entrée de balises HTML sûres, OU de texte brut, OU utiliser les filtres texte de Joomla (paramètré par groupe d'utilisateurs dans la configuration globale de Joomla), etc ..., n'autorisez jamais le HTML NON-SÉCURISÉ pour les formulaires publics, mais uniquement pour activer le paramètre'**d'encodage à l'affichage**' | `groupedlist` | **Par utilisateur**<br />`2` = Filtrage de texte Joomla (par groupe d'utilisateur)<br />**HTML / Texte**<br />`1` = HTML SÉCURITÉ: retirer tags / attributs dangereux<br />`RAW` = HTML Non sécurisé (HTML brut): ... peut-être: à encoder à l'affichage<br />`STRING` = TEXTE: décoder les entités HTML, enlever les balises HTML<br />`HTML` = TEXTE ou ENCODEAGE HTML : autorisés les entités HTML, enlever les balises | `2` (Filtrage de texte Joomla (par groupe d'utilisateur)) |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

### Titre terme

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Etiquette**<br />`title_label` | Libellé, filtré selon la langue | `text` | — | `FLEXI_FIELD_TERMTITLE` (Titre terme) |
| **Longueur maximum du texte**<br />`title_maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | `0` |
| **Taille du champ**<br />`title_size` | Taille du champ dans le formulaire de saisie | `text` | — | `80` |

### Description terme

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Etiquette**<br />`value_label` | Libellé, filtré selon la langue | `text` | — | `FLEXI_FIELD_TERMTEXT` (Description terme) |
| **Editeur**<br />`use_html` | Utilser un éditeur html (WYSIWYG) ou un simple textarea | `multilist` | `1` = Editeur HTML<br />`0` = Simple Zone de texte | `0` (Simple Zone de texte) |

#### Simple Zone de texte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Longueur maximum du texte**<br />`maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | — |
| **Lignes**<br />`rows` | Nombre de lignes | `text` | — | `3` |
| **Colonnes**<br />`cols` | Nombre de colonnes | `text` | — | `80` |

#### Editeur HTML

:::note
Remarque : à propos de la prise en charge des valeurs multiples
Seuls les éditeurs basés sur : tinyMCE** (intégré ou en installation) et **CodeMirror** sont supportés, sinon l'éditeur HTML sur de nouvelles valeurs n'apparaîtra qu'après sauvegarde
:::

:::note
REMARQUE : préférez l'utilisation du paramètre d'éditeur par défaut de Joomla (tiers ou intégré)
Ajouter 2 éditeurs différents sur la même page peut casser les boutons d'édition XTD comme lire-la-suite
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Editeur HTML**<br />`editor` | Utilise l'éditeur HTML par défaut paramétré dans Joomla pour modifier les valeurs du champ | `plugins` | `—` = Par défaut de Joomla! | — |
| **Largeur de l'éditeur**<br />`width` | Largeur de l'éditeur html | `text` | — | `98%` |
| **Hauteur de l'éditeur**<br />`height` | Définit la hauteur de l'éditeur HTML | `text` | — | `250px` |

#### Boutons de l'éditeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher**<br />`show_buttons` | Vous pouvez désactiver les boutons de l'éditeur (plugins editors-xtd) | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Cacher les boutons (pour certains éditeurs*)**<br />`skip_buttons` | Sélectionner les boutons à désactiver. Remarque : ne fonctionne pas dans tous les éditeurs. Suporté par tinyMCE et JCE, peut être pour d'autres | `pluginlist` | — | — |

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
| **Valeurs du filtre de langue**<br />`lang_filter_values` | Applique le filtre de langue JText::_() aux libellés ; ces libellés doivent être des chaînes de langue, ajoutées dans un fichier de langue ou via le gestionnaire de surcharges de langue Joomla | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Encoder les valeurs (sécurisation XSS, HTML/JS visible)**<br />`encode_output` | Encoder n'importe quel HTML/JS à l'intérieur des valeurs rendra visible n'importe quel code HTML/JS, donc les valeurs deviennent XSS en sécurité (cross site scripting). NOTE : activez ceci, - si vous soupçonnez que les valeurs dangereuses XSS ont été ajoutées au champ par des configurations de champs plus anciennes, - ou si vous voulez afficher le code HTML qui n'est pas déjà encodé en tant qu'entités HTML | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Nettoyer valeurs (par ex. enlever HTML / JS)**<br />`clean_output` | Vous pouvez faire une étape supplémentaire pour nettoyer tout HTML non sûr ou non désiré dans les valeurs, NOTE : activez ceci, - si vous soupçonnez que le html peut être dangereux via une faille XSS, ou que du formatage du HTML non désiré pourrait être ajouté au champ par des configurations de champs plus anciennes | `radio` | `0` = Non<br />`1` = HTML non-sécurisé<br />`2` = TOUT HTML | `0` (Non) |

#### Vue Catégorie

:::note
Description terme
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer HTML & tronquer le texte**<br />`cut_text_catview` | Supprimer les balises HTML du texte et les tronque en fonction de la longueur maximum. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Limite de caractères**<br />`cut_text_length_catview` | Tous les caractères dépassant la limite (commençant par le mot suivant) seront coupés | `text` | — | `200` |
| **Afficher tout le texte**<br />`cut_text_display_catview` | Activer cette option pour afficher tout le texte | `multilist` | `0` = Non<br />`1` = En ligne<br />`2` = Fenêtre Popup | `0` (Non) |
| **Icône du Bouton**<br />`cut_text_display_btn_icon_catview` | — | `text` | — | `icon-paragraph-center` |
| **Texte du bouton**<br />`cut_text_display_btn_text_catview` | — | `text` | — | — |

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

## Référencement

### Prise en charge des microdonnées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Propriété des microdonnées**<br />`microdata_itemprop` | Sélectionnez une propriété de microdonnées pour caractériser toutes les valeurs de ce champ. Cela permettra aux moteurs de recherche de classer les valeurs de ce champ de manière appropriée, améliorant ainsi le référencement de vos pages | `microdataprops` | — | — |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Champ formulaire

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `1` = Texte à Rechercher | `0` |
