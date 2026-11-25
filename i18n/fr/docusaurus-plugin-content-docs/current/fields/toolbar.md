---
sidebar_position: 38
---

# Barre d’outils

Champ de barre d’outils pour FLEXIcontent

*Plugin : `toolbar` — Barre d’outils*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/toolbar/toolbar.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Apparence

#### Apparence

### Basique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| `frontend_hidden` | — | `hidden` | — | `1` |
| `backend_hidden` | — | `hidden` | — | `1` |

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

#### FLEXI_BACKEND_VIEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_BACKEND_VIEW_APPEARANCE**<br />`backend_view_appearance` | FLEXI_BACKEND_VIEW_APPEARANCE_DESC | `multilist` | `0` = Par défaut<br />`1` = FLEXI_CHECK_MARK<br />`2` = FLEXI_CLEAN_HTML_AND_TRIM | `0` (Par défaut) |
| **FLEXI_TRIM_LENGTH**<br />`backend_view_trim_chars` | FLEXI_TRIM_LENGTH_DESC | `text` | — | `100` |

### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fclayout` | — | `default` |

#### Liste Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Texte d'ouverture**<br />`opentag` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

### Paramètres

#### Apparence

## Réseaux sociaux

### Prise en charge des réseaux sociaux (ex. Facebook)

#### Texte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nom du site**<br />`add_og_site_name` | Selectionnez ce qui devrais être prposé comme titre du site sur la page courante | `radio` | `0` = Non<br />`1` = Nom réel du site | `0` (Non) |
| **Titre**<br />`add_og_title` | Sélectionnez ce qui devrais être proposé comme titre de la page courante | `radio` | `0` = Non<br />`1` = Titre du contenu | `0` (Non) |
| **Description**<br />`add_og_descr` | Selectionnez ce qui devrais être suggéré comme descriptin de la page courante | `radio` | `0` = Non<br />`1` = Description du contenu | `0` (Non) |
| **Type de contenu**<br />`add_og_type` | Sélectionnez ce qui devrais être suggéré comme type de contenu de la page courante | `radio` | `0` = Non<br />`article` = Utiliser 'article'<br />`website` = Utilisez 'website' | `article` (Utiliser 'article') |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter**<br />`add_og_image` | Selectionnez ce qui devrait être suggéré comme image de la page courante | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Source de l'image de la catégorie**<br />`og_image_field` | NOTE : habituellement, ce devrais être un champ image | `fcimage` | — | — |
| **Image par défaut (lorsque l'image est manquante)**<br />`og_image_fallback` | Lorsqu'une image est manquante, vous pouvez choisir d'utiliser une substitution ; par exemple le texte de description de l'article quand le champ image est vide, même si il y a une valeur par défaut pour le champ d'image | `list` | `0` = Aucune image par défaut<br />`1` = Utiliser l'image du texte de description de l'article<br />`2` = Utiliser l'image du texte de description de l'article (ignorer la valeur par défaut du champ image) | — |
| **Taille de la miniature**<br />`og_image_thumbsize` | Taille de la miniature (en cas d'utilisation du champ image) | `radio` | `small` = petit<br />`medium` = moyen<br />`large` = grande | `medium` (moyen) |
