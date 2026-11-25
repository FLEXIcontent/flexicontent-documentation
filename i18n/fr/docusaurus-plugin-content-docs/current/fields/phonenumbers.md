---
sidebar_position: 25
---

# Numéros de téléphone internationaux

Ce champ ajoute des numéros de téléphone aux contenus. Pour chaque numéro, vous pouvez ajouter un nom (ex : Bureau, Fax, etc.), un code international, un **area code** et un numéro de téléphone. La configuration du champ permet une certaine flexibilité pour répondre au mieux aux différents besoins. Le code HTML est très détaillé pour permettre une mise en forme facile grâce aux CSS.

*Plugin : `phonenumbers` — Numéros de téléphone internationaux*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/phonenumbers/phonenumbers.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
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
| **Autoriser les valeurs multiples**<br />`allow_multiple` | Autoriser plus d'1 valeur pour ce champs | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Valeurs par colonne**<br />`fields_box_placing` | Économiser de l'espace en autorisant l'affichage par ligne de valeurs multiples | `radio` | `0` = 1<br />`1` = Multiple | `0` (1) |
| **Position Ajouter**<br />`add_position` | Sélectionnez pour ajouter le bouton en ligne (bouton d'ajout de valeur à chaque ligne) ou afficher le bouton d'ajout au fond de la liste de valeurs | `multilist` | `0` = Bouton Ajouter en bas<br />`1` = Bouton ajouter avant<br />`2` = Bouton Ajouter après<br />`3` = Les deux (avant - après) | `3` (Les deux (avant - après)) |
| **Nb maximum de valeurs**<br />`max_values` | Définissez ici le nombre maximum de valeurs que l'utilisateur pourra saisir. 0 pour illimité. | `text` | — | `0` |
| **PLG_FLEXICONTENT_FIELDS_PHONENUMBERS_FORM_CARD_WIDTH**<br />`form_card_width` | PLG_FLEXICONTENT_FIELDS_PHONENUMBERS_FORM_CARD_WIDTH_DESC | `text` | — | `320` |
| **Affichage conditionnel**<br />`showon` | Affiché en fonction de conditions. Utilisez le format Joomla 'fieldname:value' comme par exemple album_type:2 REMARQUE: ne pas définir ce champ en obligatoire. Également DÉSACTIVER les scripts prettyCheckable / Select2 JS dans tous les champs référencés de type select*, checkbox*, radio* | `text` | — | — |
| **Obligatoire**<br />`required` | Définit si le champ doit être obligatoire dans le formulaire de saisie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Création des valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Libellé du téléphone**<br />`use_label` | — | `radio` | `0` = Non<br />`1` = Oui | `3` |
| **Code du pays**<br />`use_cc` | — | `multilist` | `0` = Non<br />`1` = Oui | — |
| **Pays par défaut**<br />`ac_country_default` | Choisissez un pays par défaut pour le préfixe du numéro de téléphone | `fccountriesphones` | — | — |
| **Pays autorisés**<br />`ac_country_allowed_list` | Ajouter des pays autorisés à la liste, vide ajouter tout les pays | `fccountriesphones` | — | — |
| **Numero de téléphone**<br />`use_phone` | — | `radio` | `1` = 1 partie<br />`2` = Zone de code + numéro local<br />`3` = Zone de code + partie 2 + partie 3 | `3` (Zone de code + partie 2 + partie 3) |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Libellé téléphone

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Longueur maximum du texte**<br />`label_maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | `48` |
| **Taille du champ**<br />`label_size` | Taille du champ dans le formulaire de saisie | `text` | — | `48` |

#### Code du pays

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Longueur maximum du texte**<br />`cc_maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | `6` |
| **Taille du champ**<br />`cc_size` | Taille du champ dans le formulaire de saisie | `text` | — | `6` |

#### Numero de téléphone

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Libellé de la partie**<br />`show_part_labels` | — | `radio` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |

#### Partie 1 (zone de code)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Longueur maximum du texte**<br />`phone1_maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | `12` |
| **Taille du champ**<br />`phone1_size` | Taille du champ dans le formulaire de saisie | `text` | — | `12` |

#### Partie 2

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Longueur maximum du texte**<br />`phone2_maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | `12` |
| **Taille du champ**<br />`phone2_size` | Taille du champ dans le formulaire de saisie | `text` | — | `12` |

#### Partie 3

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Longueur maximum du texte**<br />`phone3_maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | `12` |
| **Taille du champ**<br />`phone3_size` | Taille du champ dans le formulaire de saisie | `text` | — | `12` |

#### Autorise les lettres dans le numéro de téléphone

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autorise les lettres**<br />`allow_letters` | Activer l'utilisation des lettres ( A à Z , en majuscules seulement) dans le champ de numéro de téléphone . Lorsque cette option est désactivé, seuls les nombres sont autorisés . | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

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

#### Valeurs affichées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nom du numéro**<br />`display_phone_label` | Afficher le nom du numéro lors du rendu du champ | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Afficher le préfixe international**<br />`display_country_code` | — | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Afficher l'**Area Code****<br />`display_area_code` | — | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Ajouter téléphone : lien**<br />`add_tel_link` | Encapsule le numero de téléphone dans lien qui utilise le protocole tel: | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Propriétés séparateurs

#### Libellé téléphone

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe du nom du numéro**<br />`label_prefix` | HTML à placer avant le nom du numéro | `text` | — | — |
| **Suffixe du nom du numéro**<br />`label_suffix` | HTML à placer après le nom du numéro | `text` | — | — |

#### Code du pays

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe du code international**<br />`country_code_prefix` | Texte à placer avant le code international | `text` | — | — |
| **Séparateur International-Area**<br />`separator_cc_phone1` | Texte à placer entre le code international et l'**Area Code** | `text` | — | — |

#### Numero de téléphone

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Séparateur saise/partie 2**<br />`separator_phone1_phone2` | Texte à placer entre la zone de saisie et la partie 2 (ex: code de bascule) | `text` | — | — |
| **Séparateur partie 2/3**<br />`separator_phone2_phone3` | Texte à placer entre la partie 2 et 3 (ex: entre code de bascule et le numéro utilisateur) | `text` | — | — |

### Liste Valeurs

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`opentag` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`closetag` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Texte d'ouverture**<br />`field_prefix` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`field_suffix` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

### Plugins de contenu

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Apparence
