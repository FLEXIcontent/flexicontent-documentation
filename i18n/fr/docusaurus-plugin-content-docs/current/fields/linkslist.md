---
sidebar_position: 23
---

# Liste de liens

Plugin de champ 'Lien list' pour FLEXIcontent

*Plugin : `linkslist` — Liste HTML d’URL / ancres / liens JS*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/linkslist/linkslist.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Édition

#### Édition

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le champ dans un groupe**<br />`use_ingroup` | Activer pour permettre d'utiliser ce champ dans un groupe, qui sera configuré via champ 'Groupe de champ'. REMARQUE: Vous devez alors sélectionner ce champ UNIQUEMENT dans un groupe de champs | `multilist` | `0` = Non | `0` (Non) |

#### Nombre de valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage conditionnel**<br />`showon` | Affiché en fonction de conditions. Utilisez le format Joomla 'fieldname:value' comme par exemple album_type:2 REMARQUE: ne pas définir ce champ en obligatoire. Également DÉSACTIVER les scripts prettyCheckable / Select2 JS dans tous les champs référencés de type select*, checkbox*, radio* | `text` | — | — |
| **Obligatoire**<br />`required` | Définit si le champ doit être obligatoire dans le formulaire de saisie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Création des valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Valeurs par défaut**<br />`default_values` | Choisissez les valeurs par défaut ou laissez vide pour aucun. ATTENTION, les valeurs doivent être choisies à partir des éléments de champ VALEURS que vous avez définis ci-dessus. Vous devez fournir une liste séparée par des VIRGULES. | `text` | — | — |
| **Pré-configuration**<br />`extra_votes_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = Charger un exemple | — |
| **Eléments de liste**<br />`field_elements` | Les éléments d'une liste non triée () ou triée () . La syntaxe est la suivante: Title1[id=\"_QQ_\"tagid1\"_QQ_\" class=\"_QQ_\"cssclass1\"_QQ_\" ... link=\"_QQ_\"#link1\"_QQ_\"] :​: Title2[id=\"_QQ_\"tagid2\"_QQ_\" class=\"_QQ_\"cssclass2\"_QQ_\" ... link=\"_QQ_\"#link2\"_QQ_\"] :​: Title3[id=\"_QQ_\"tagid3\"_QQ_\" class=\"_QQ_\"cssclass3\"_QQ_\" ... link=\"_QQ_\"#link3\"_QQ_\"] **NOTE 1:** - utilisez :​: en tant que séparateur d’éléments de la liste, - utilisez [option=value] pour spécifier les options de chaque élément de la liste. **NOTE 2:** - 'title' est le texte à l’intérieur du tag HTML , - 'title' sera un lien (placé à l'intérieur du tag HTML ) SEULEMENT si l'option 'link' est spécifiée. - toutes les 'options' comme: id,class,... (à l'exclusion de 'link'), deviendront des paramètres de tag HTML du tag HTML. **NOTE 3:** toutes les options (incluant l'option 'link') sont optionnelles, vous pouvez donc écrire: TitleNN[] sans spécifier aucune option | `textarea` | — | — |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher comme**<br />`editform_field_type` | Vous pouvez utiliser les affichages alternatifs, par exemple pour économiser de l’espace avec des formulaires plus compacts | `radio` | `1` = Case à Cocher (multiple)<br />`2` = Sélecteur par mot clé (multiple) | `1` (Case à Cocher (multiple)) |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_form` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_form` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Séparateur de valeur formulaire de saisie**<br />`separator` | Choisir le séparateur pour séparer l'ensemble des valeurs dans les formulaires de saisies (placé entre les valeurs) | `list` | `0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | `0` (Espace) |
| **Texte d'ouverture**<br />`opentag_form` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_form` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

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
| **Afficher sans les liens les éléments non sélectionnés**<br />`add_non_selected` | Normalement les valeurs non sélectionnées ne sont pas incluses dans la liste créée. Activez cette option pour les afficher sans ajouter un tag de lien, à la place un tag SPAN sera ajouté | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Paramètres de balise HTML

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type de liste**<br />`list_type` | Définir le type de liste. Le plus courant est 'ul'. | `list` | `ul` = Liste désordonnée<br />`ol` = Liste triée | `ul` (Liste désordonnée) |
| **Classe de la liste**<br />`list_class` | Ajouter une classe CSS pour la liste, laissez vide si vous n'en avez pas besoin. | `text` | — | — |
| **ID de la liste**<br />`list_id` | Ajouter un ID pour la liste, laissez vide si vous n'en avez pas besoin. | `text` | — | — |

#### JS/CSS personnalisé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **JavaScript**<br />`js_code` | Code javascript facultatif à ajouter à la vue frontend quand ce champ est affiché, ainsi vous pouvez joindre JS aux liens insérés par ce champ et créer des actions cliquables pour manipuler votre page selon vos besoins. ** REMARQUE le code JS est ajouté même si ce champ insère ZERO liens. Ainsi votre code JS doit joindre, exemple, avec un sélecteur jQuery approprié, sélecteur qui peut ou non être trouvé. ** REMARQUE : ne sera ajouté qu'une seule fois, à la fois en vue d'élément, et en vue multi-éléments quand ce champ est affiché. Alternativement, cela pourrait également être ajouté de façon permanente par un de vos fichier JS | `textarea` | — | — |
| **Règles CSS**<br />`css_code` | Règles CSS optionnelle à appliquer à la vue frontend quand ce champ est affiché. ** REMARQUE : celles-ci ne seront ajoutées qu'une seule fois, à la fois en vue élément et en vue multi-éléments quand ce champ est affiché. Sinon, elles peuvent aussi être ajoutés en permanence via n'importe lequel de vos fichier CSS | `textarea` | — | — |

### Plugins de contenu

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Apparence
