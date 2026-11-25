---
sidebar_position: 19
---

# Groupe de champs (répétable)

Champs de groupe pour les plugin champ de FLEXIContent

*Plugin : `fieldgroup` — Groupe de champs*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/fieldgroup/fieldgroup.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Édition

#### Édition

### Valeurs

#### Goupe de champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Champs**<br />`fields` | Sélectionner les champs affichés comme un groupe | `fields` | — | — |

#### Nombre de valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage conditionnel**<br />`showon` | Affiché en fonction de conditions. Utilisez le format Joomla 'fieldname:value' comme par exemple album_type:2 REMARQUE: ne pas définir ce champ en obligatoire. Également DÉSACTIVER les scripts prettyCheckable / Select2 JS dans tous les champs référencés de type select*, checkbox*, radio* | `text` | — | — |
| **Obligatoire**<br />`required` | Définit si le champ doit être obligatoire dans le formulaire de saisie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Autoriser les valeurs multiples**<br />`allow_multiple` | Autoriser plus d'1 valeur pour ce champs | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Nb maximum de valeurs**<br />`max_values` | Définissez ici le nombre maximum de valeurs que l'utilisateur pourra saisir. 0 pour illimité. | `text` | — | `0` |
| **Valeurs par colonne**<br />`fields_box_placing` | Économiser de l'espace en autorisant l'affichage par ligne de valeurs multiples | `radio` | `0` = 1<br />`1` = Multiple | `0` (1) |
| **Position Ajouter**<br />`add_position` | Sélectionnez pour ajouter le bouton en ligne (bouton d'ajout de valeur à chaque ligne) ou afficher le bouton d'ajout au fond de la liste de valeurs | `multilist` | `0` = Bouton Ajouter en bas<br />`1` = Bouton ajouter avant<br />`2` = Bouton Ajouter après<br />`3` = Les deux (avant - après) | `3` (Les deux (avant - après)) |

#### Champs non assignés ou type de contenu / n'ayant aucun contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage**<br />`form_empty_fields` | Cache/Affiche les champs qui ne sont pas assignés au type de contenu du contenu courant et aussi au champ sans aucune valeur HTML | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Texte personnalisé**<br />`form_empty_fields_text` | Personnalisé le texte affiché pour les champs vides/non assignés | `text` | — | `FLEXI_NA` (N/A) |

### Affichage du formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `multilist` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne<br />`-1` = Comme espace réservé | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage des champs**<br />`formlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/field_*. hp comme field_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fclayout` | `list` = Par défaut (placement vertical)<br />`flexbox` = Flexbox (placement horizontal avec retour automatique à la ligne) | `list` (Par défaut (placement vertical)) |

#### Édition compacte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Cacher toutes les valeurs**<br />`compact_edit_global` | Activer cette option pour afficher un bouton de masquage pour toutes les valeurs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Cacher les valeurs**<br />`compact_edit` | Activer cette option pour rendre l'affichage plus compact pour tous les champs groupe, et ainsi sauver de l'espace | `multilist` | `0` = Non<br />`1` = Oui, réduit au départ<br />`2` = Oui, développé au départ | `0` (Non) |
| **Champs toujours visible**<br />`compact_edit_excluded` | Vous devez sélectionner certains champs pour qu'ils soient toujours visible et qui serviront donc de 'titre' ou 'référence' pour retrouver facilement une valeur, exemple si le groupe de champs est un « contact » alors « Prénom » et « Nom » pourront toujours être visibles | `fields` | — | — |

### Paramètres de mise en page

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
| **HTML personnalisé**<br />`display_mode` | Sélectionner si vous souhaitez utiliser l'affichage par défaut ou le code HTML personnalisé ci-dessous - l'affichage par HTML par défaut inclus tous les champs du groupe plus leurs libellés | `multilist` | `0` = Mise en Page<br />`1` = HTML personnalisé | `0` (Mise en Page) |
| **HTML personnalisé**<br />`custom_html` | Entrez une liste de noms de champ séparés par des virgules ou insérer du HTML personnalisé avec les remplacements de chaîne de champ et de la langue : **Remarque :** vous pouvez utiliser : **&#123;&#123;fieldname&#125;&#125;** ou **&#123;&#123;fieldname ##displayvar&#125;&#125;** &#123;&#123;fieldname##label&#125;&#125; --sera remplacé avec l'affichage HTML de chaque champ **%% language_string %%** --sera remplacé par la chaîne de langue. Enfin, vous pouvez utiliser les relations entre contenus : __item_url__, __item_title_escaped__, __item_tooltip__ et des propriétés telles que: &#123;item-&gt;id&#125;, &#123;item-&gt;title&#125;, etc. | `editor` | — | — |

#### Champs SANS valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ignorer le champ (libellé / code HTML vide)**<br />`hide_lbl_ifnoval` | Sélectionner les champs dont le libellé doit être masqué s’ils n’ont pas de valeur. REMARQUE : si le HTML par défaut est utilisé, les champs n’ayant produit aucun code HTML seront également ignorés | `filters` | — | — |

### Liste Valeurs

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pré-configuration**<br />`prx_sfx_open_close_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage) | — |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
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
| **Type microdata**<br />`fieldgroup_itemtype` | Sélectionnez un type de microdonnées qui caractérisera tous les éléments du type. MICRODATA permet aux moteurs de recherche de catégoriser votre contenu de manière appropriée, améliorant le référencement de vos pages | `microdatatype` | — | — |
