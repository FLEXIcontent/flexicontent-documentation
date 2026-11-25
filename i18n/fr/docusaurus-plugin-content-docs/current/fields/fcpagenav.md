---
sidebar_position: 18
---

# Navigation entre contenus

Plugin de champ de navigation de page pour FLEXIcontent

*Plugin : `fcpagenav` — Navigation*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/fcpagenav/fcpagenav.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Apparence

### Affichage

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher pour les clients**<br />`show_in_clients` | Sélectionner si le champ sera créé et affiché à des clients spécifiques | `fccheckbox` | — | — |
| **Afficher dans les vues**<br />`show_in_views` | Sélectionner si le champ sera créé et affiché en fonction d'une vue spécifique | `fccheckbox` | — | — |

### Libellé et accès

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Montrer un message d'**accès interdit****<br />`show_acc_msg` | Si le champ est inaccessible, une message de non-accès s'affichera. **NOTE : ** SI ce paramètre est désactivé, le champ sera invisible aux utilisateurs sans accès, sans aucun message ou avertissement indiquant son existance | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Message **accès interdit****<br />`no_acc_msg` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Charger le CSS du plugin**<br />`load_css` | Charger le fichier css du plugin | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Afficher la position courante**<br />`show_prevnext_count` | Affiche le nombre total de contenu dans la navigation and aussi la position courante | `radio` | `0` = Cacher<br />`1` = Montrer | `1` (Montrer) |
| `frontend_hidden` | — | `hidden` | — | `1` |
| `backend_hidden` | — | `hidden` | — | `1` |

## Liens

### Contenus précédent / suivant

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Boucle précédent/suivant**<br />`loop_prevnext` | Le lien suivant du dernier contenu de la liste amènera au premier contenu, l'action sera similaire pour le lien précédent. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Infobulles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser les infobules**<br />`use_tooltip` | Utiliser les infobulles de Joomla! | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Infobulle (suivant)**<br />`tooltip_title_next` | Choisir le texte de l’infobulle pour \"_QQ_\"Suivant\"_QQ_\" | `text` | — | — |
| **Infobulle (précédent)**<br />`tooltip_title_prev` | Saisir un texte qui apparaitre dans une inbobulle sur le bouton précédent | `text` | — | — |

#### Texte du bouton

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le titre du contenu**<br />`use_title` | Utiliser le titre du contenu à la place des libellés suivants et précédents. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Etiquette du bouton précédent**<br />`prev_label` | — | `text` | — | — |
| **Etiquette du bouton suivant**<br />`next_label` | — | `text` | — | — |

### Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le lien "Revenir à la liste"**<br />`use_category_link` | Le lien "Revenir à la liste" permet de revenir à la vue catégorie tout en conservant la position actuelle. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Libellé du bouton de la catégorie**<br />`category_label` | — | `text` | — | — |

## Images

### Images

#### Paramètres des vignettes

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur de l'image**<br />`nav_width` | Largeur de l'image | `text` | — | `120` |
| **Hauteur de l'image**<br />`nav_height` | Hauteur de l'image | `text` | — | `60` |
| **Méthode de traitement**<br />`nav_method` | Méthode de traitement | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |

### Images du contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser l'image**<br />`item_use_image` | Extraire la première image du texte principale | `multilist` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |
| **Source de l'image**<br />`item_image` | Sélectionner la source de l'image. Vous pouvez aussi choisir un champ image (s'il y en a au moins un de disponible) ou automatiquement extraire l'image de la description. | `fcimage` | — | — |
| **Taille de l'image**<br />`item_image_size` | FLEXI_IMAGE_SIZE_DESC | `radio` | `—` = Utiliser les paramètres<br />`s` = Petite<br />`m` = Moyenne<br />`l` = Grande<br />`o` = Original | — |

### Image de catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Image de la catégorie**<br />`cat_use_image` | Afficher/Masquer l'image de la catégorie. | `multilist` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |
| **Source de l'image de la catégorie**<br />`cat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | `radio` | `0` = Extraire de la description<br />`1` = Utiliser l'image des paramètres<br />`2` = Essayer les paramètres, puis extraire de la description | `2` (Essayer les paramètres, puis extraire de la description) |
