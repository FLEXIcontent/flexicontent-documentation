---
sidebar_position: 7
---

# Grid — vue catégorie



:::info Source
Cette page est générée depuis `site/templates/grid/category.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Paramètres du modèle

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **# Contenus en vedette**<br />`lead_num` | Nombre de contenus en vedette. Notez que cela affecte les contenus jusqu’à ce que ce nombre soit atteint ; tous les contenus restants de la page actuelle et des suivantes seront affichés avec la configuration « standard » | `text` | — | — |

#### Onglets de l’élément

### Commun

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage personnalisé du titre**<br />`custom_layout_title` | Ceci sera affiché à l'utilisateur dans la partie publique en tant qu'infobulle du bouton pour changer de mise en page | `text` | — | — |

#### Titre de l'article

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur du texte du titre**<br />`title_color` | Couleur du texte du titre | `fccolor` | — | `none` |
| **Arrière-plan du titre**<br />`title_background` | Couleur de l’arrière-plan du titre | `fccolor` | — | `none` |
| **Taille de police du titre**<br />`title_font_size` | Taille du texte du titre | `text` | — | `none` |

#### Style des étiquettes

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Fond**<br />`label_bg_color` | Choisir l'arrière-plan de votre étiquette | `fccolor` | — | `none` |
| **Couleur texte**<br />`label_txt_color` | Sélectionner la couleur des textes dans les étiquettes | `fccolor` | — | `none` |
| **Marge intérieure haute**<br />`label_pad_top` | Espace intérieur haut | `number` | — | `8` |
| **Marge intérieure droite**<br />`label_pad_right` | Espace intérieur droite | `number` | — | `10` |
| **Marge intérieure gauche**<br />`label_pad_left` | Espace intérieur gauche | `number` | — | `10` |
| **Marge intérieure basse**<br />`label_pad_bottom` | Espace intérieur bas | `number` | — | `8` |
| **Bord arrondi**<br />`label_radius` | Arrondi des bordures des étiquettes | `number` | — | `3` |

#### Style commun de la boîte de contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bord arrondi**<br />`ibox_radius` | Arrondi des bordures des étiquettes | `text` | — | `0px 0px 0px 0px` |
| **Couleur de superposition**<br />`overlay_background` | Choisir l'arrière-plan de votre étiquette | `fccolor` | — | `rgba(0,0,0,0.4)` |

#### Boîte d’ombre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ombre X**<br />`ibox_shadow_x` | Arrondi des bordures des étiquettes | `number` | — | `0` |
| **Ombre Y**<br />`ibox_shadow_y` | Arrondi des bordures des étiquettes | `number` | — | `0` |
| **Flou de l’ombre**<br />`ibox_shadow_blur` | Arrondi des bordures des étiquettes | `number` | — | `20` |
| **Étendue de l’ombre**<br />`ibox_shadow_spread` | Arrondi des bordures des étiquettes | `number` | — | `0` |
| **Fond**<br />`ibox_shadow_color` | Choisir l'arrière-plan de votre étiquette | `fccolor` | — | `rgba(0,0,0,0.2)` |
| **Effet de survol de l’ombre**<br />`ibox_shadow_hover` | Arrondi des bordures des étiquettes | `number` | — | `50` |

#### Style du lien « Lire la suite »

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Fond**<br />`readon_bg_color` | Choisir l'arrière-plan de votre étiquette | `fccolor` | — | `none` |
| **Couleur texte**<br />`readon_txt_color` | Sélectionner la couleur des textes dans les étiquettes | `fccolor` | — | `none` |
| **Taille de police du titre**<br />`readon_font_size` | Taille du texte du titre | `text` | — | `none` |
| **Type de lien « Lire la suite »**<br />`readon_type` | Nombre de colonnes pour le contenu. NOTE : c'est la valeur maximale, le nombre de colonne affichées dépendra de la largeur de la fenêtre du navigateur | `radio` | `—` = Paramètres globaux<br />`0` = Texte<br />`1` = Image | — |
| **Image du lien « Lire la suite »**<br />`readon_image` | Sélectionner l’image à utiliser à la place de « Lire la suite », cela peut être utile si votre site n’est pas multilingue | `media` | — | — |
| **Classe du lien « Lire la suite »**<br />`readon_class` | Sélectionner la classe CSS à utiliser à la place de « Lire la suite », cela peut être utile si votre site n’est pas multilingue | `text` | — | `btn btn-default` |

#### Image en chargement différé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le chargement différé**<br />`use_lazy_loading` | Définir oui pour utiliser le chargement paresseux natif du navigateur | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

### Contenus en vedette

#### Onglets des contenus en vedette

### Disposition

#### Basique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **taille des colonnes**<br />`ibox_minsize_feat` | min size of column | `text` | — | `200px` |
| **Placement des contenus**<br />`item_placement_feat` | Méthode de placement des éléments, par exemple sélectionnez comme tuiles de maçonnerie, pour les placer, de sorte qu'il n'y ait pas d'espace vide entre eux, ressemblant à l'emplacement des tuiles de maçonnerie _0_ | `radio` | `—` = Paramètres globaux<br />`0` = En colonne<br />`1` = Comme des tuiles masonry | — |
| **Ouvrir les contenus dans une fenêtre modale**<br />`lead_link_to_popup` | Les contenus seront ouverts dans une fenêtre modale _0_ | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Mettre en évidence les contenus**<br />`hl_items_onnav_feat` | Mettre en évidence les contenus actifs et survolés en ajoutant des classes CSS _0_ | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`2` = Au survol | — |

#### Placement du contenu / de l’image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Placement du contenu par rapport à l’image**<br />`content_layout_feat` | Choisir le placement du contenu à côté, au-dessus/en dessous (dégagé) ou sur (superposé) l’image. Remarque : la superposition rogne le contenu qui ne rentre pas par le bas _3_ | `list` | `—` = Paramètres globaux<br />`0` = Flottant (droite)<br />`1` = Flottant (gauche)<br />`2` = Dégagé (au-dessus)<br />`3` = Dégagé (en dessous)<br />`4` = Superposé (en haut)<br />`5` = Superposé (en bas)<br />`6` = Superposé (plein) | — |
| **Contenu visible en superposition**<br />`content_display_feat` | Choisir comment l’image est ajustée dans le conteneur _0_ | `radio` | `—` = Paramètres globaux<br />`0` = Toujours visible<br />`2` = Au survol | — |
| **Ajustement de l’image pour dégagé / superposé**<br />`img_fit_feat` | Choisir comment l’image est ajustée dans le conteneur _1_ | `radio` | `—` = Paramètres globaux<br />`0` = Ajustement automatique<br />`1` = Ajustement automatique et étirement | — |
| **Hauteur du contenu**<br />`content_height_fit_feat` | Choisir Oui pour fixer la même hauteur pour chaque contenu _1_ | `radio` | `—` = Paramètres globaux<br />`0` = Hauteur du contenu<br />`1` = Forcer la même hauteur | — |
| **Hauteur du contenu**<br />`content_width_fit_feat` | Choisir Oui pour fixer la même hauteur pour chaque contenu _1_ | `radio` | `—` = Paramètres globaux<br />`auto-fill` = Remplissage automatique<br />`auto-fit` = Ajustement automatique | `auto-fill` (Remplissage automatique) |
| **Readmore align**<br />`readmore_align_feat` | Nombre de colonnes pour le contenu. NOTE : c'est la valeur maximale, le nombre de colonne affichées dépendra de la largeur de la fenêtre du navigateur | `radio` | `—` = Paramètres globaux<br />`left` = A gauche<br />`center` = Centre<br />`right` = A droite | `center` (Centre) |

### Style

#### Boîte de la liste des contenus

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **couleur d’arrière-plan**<br />`box_background_color_feat` | Couleur d’arrière-plan du conteneur des contenus | `fccolor` | — | `none` |
| **remplissage supérieur/inférieur**<br />`box_padding_top_bottom_feat` | Remplissage du conteneur appliqué en haut et en bas des contenus | `text` | — | `0` |
| **remplissage gauche/droite**<br />`box_padding_left_right_feat` | Remplissage du conteneur appliqué à gauche et à droite des contenus | `text` | — | `0` |
| **marge supérieure**<br />`box_margin_top_feat` | Marge du conteneur appliquée en haut et en bas des contenus | `text` | — | `4rem` |
| **marge inférieure**<br />`box_margin_bottom_feat` | Marge du conteneur appliquée en haut et en bas des contenus | `text` | — | `4rem` |
| **marge gauche/droite**<br />`box_margin_left_right_feat` | Marge du conteneur appliquée à gauche et à droite des contenus | `text` | — | `0` |

#### Boîte du contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **couleur d’arrière-plan**<br />`ibox_background_color_feat` | Couleur d’arrière-plan appliquée à chaque contenu | `fccolor` | — | `none` |
| **couleur de la description**<br />`ibox_description_color_feat` | Couleur d’arrière-plan appliquée à chaque contenu | `fccolor` | — | `none` |
| **largeur de bordure**<br />`ibox_border_width_feat` | Largeur de bordure appliquée autour des contenus | `number` | — | `0` |
| **couleur de bordure**<br />`ibox_border_color_feat` | Couleur de bordure appliquée autour des contenus | `fccolor` | — | `transparent` |
| **remplissage supérieur/inférieur**<br />`ibox_padding_top_bottom_feat` | Remplissage appliqué en haut et en bas des contenus | `text` | — | `0` |
| **remplissage gauche/droite**<br />`ibox_padding_left_right_feat` | Remplissage appliqué à gauche et à droite des contenus | `text` | — | `0` |
| **marge supérieure/inférieure**<br />`ibox_margin_top_bottom_feat` | Marge appliquée en haut et en bas des contenus | `text` | — | `2rem` |
| **marge gauche/droite**<br />`ibox_margin_left_right_feat` | Marge appliquée à gauche et à droite des contenus | `text` | — | `2rem` |

### Champs

#### Bloc (sous-)catégorie, au début de la (sous-)catégorie

:::note
Attention : cela est pertinent si vous triez vos contenus par catégorie (tri de premier niveau), le tri de second niveau pouvant être libre, par exemple le titre
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`lead_catblock` | — | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Titre de la catégorie**<br />`lead_catblock_title` | Afficher/Masquer le titre de la catégorie. | `radio` | `—` = Paramètres globaux<br />`1` = Oui | — |

#### Texte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la description**<br />`lead_use_description` | Afficher ou masquer le texte de description | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Supprimer les balises HTML & tronquer le texte**<br />`lead_strip_html` | Supprimer les balises HTML du texte et les tronque en fonction de la longueur maximum. **Remarque :** Cela forcera l'affichage du lien 'lire la suite' | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui, Forcer 'lire la suite'<br />`2` = Oui, si nécessaire | — |
| **Longueur maximum du texte**<br />`lead_cut_text` | Tronque le texte d'introduction après X caractères | `text` | — | — |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser l'image**<br />`lead_use_image` | Extraire la première image du texte principale | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Source de l'image**<br />`lead_image` | Sélectionner la source de l'image. Vous pouvez aussi choisir un champ image (s'il y en a au moins un de disponible) ou automatiquement extraire l'image de la description. | `fcimage` | — | — |
| **HTML de champ comme image**<br />`lead_image_custom_display` | Vous pouvez utiliser le HTML produit par n’importe quel champ personnalisé à la place de l’image. -- Laissez vide pour utiliser la valeur de la liste déroulante ci-dessus. -- **Remarque : la taille de l’image et les autres paramètres ne sont pas utilisés**. -- Écrivez sous la forme nomchamp##nomvariable, par exemple pour les champs image : imgfieldname##display_small, imgfieldname##display_medium, imgfieldname##display_large | `text` | — | — |
| **URL de champ comme image**<br />`lead_image_custom_url` | Vous pouvez utiliser l’URL produite par n’importe quel champ personnalisé à la place de l’image. -- Laissez vide pour utiliser la valeur de la liste déroulante ci-dessus. -- **Remarque : la taille de l’image et les autres paramètres sont appliqués à l’URL fournie**. -- Écrivez sous la forme nomchamp##nomvariable, par exemple pour les champs image : imgfieldname##display_small_src, imgfieldname##display_medium_src, imgfieldname##display_large_src | `text` | — | — |
| **Image par défaut (lorsque l'image est manquante)**<br />`lead_image_fallback_img` | Quand l'image est manquante, vous pouvez sélectionner une autre image par défaut. ex: l'image du texte d'introduction quand il n'y pas de valeur dans le champs image, même si le champ image possède une image par défaut. | `list` | `0` = Aucune image par défaut<br />`1` = Utiliser l'image du texte d'introduction<br />`2` = Utiliser l'image du texte d'introduction (ignorer l'image par défaut du champ)<br />`3` = Utiliser un champ personnalisé | — |
| **Champ personnalisé de repli**<br />`lead_fallback_field` | — | `fcimage` | — | `0` |
| **Position de l'image**<br />`lead_position` | Définit la position de l'image dans le bloc. | `radio` | `—` = Paramètres globaux<br />`0` = A gauche<br />`1` = A droite | — |
| **Lien sur l'image**<br />`lead_link_image` | Actif un lien sur l'image affichée. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Lien vers**<br />`lead_link_image_to` | Si vous utilisez un champ image, vous pouvez utiliser le lien personnalisé ajouté à l’image | `radio` | `—` = Paramètres globaux<br />`0` = Contenu<br />`1` = Lien personnalisé (champ image) | — |
| **Taille de l'image**<br />`lead_image_size` | Taille de l'image pour l'introduction | `radio` | `—` = Utiliser les paramètres<br />`s` = Petite<br />`m` = Moyenne<br />`l` = Grande<br />`o` = Original | — |
| **Largeur de l'image**<br />`lead_width` | Largeur de l'image | `text` | — | — |
| **Hauteur de l'image**<br />`lead_height` | Hauteur de l'image | `text` | — | — |
| **Méthode de traitement**<br />`lead_method` | Méthode de traitement | `radio` | `—` = Paramètres globaux<br />`0` = A l'échelle<br />`1` = Découper | — |
| **Images par défaut (par type)**<br />`lead_default_images` | Entrez soit un chemin d'image relatif au dossier racine de Joomla : image-path ou entrez par type, séparés par des virgules : _OTHER_##image-path, type-alias1##image-path1, type-alias2##image-path2 | `textarea` | — | — |

#### Onglets des contenus en vedette

### Contenus standard

#### Onglets des contenus standard

### Disposition

#### Basique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **taille des colonnes**<br />`ibox_minsize_std` | min size of column | `text` | — | `200px` |
| **Placement des contenus**<br />`item_placement` | Méthode de placement des éléments, par exemple sélectionnez comme tuiles de maçonnerie, pour les placer, de sorte qu'il n'y ait pas d'espace vide entre eux, ressemblant à l'emplacement des tuiles de maçonnerie _1_ | `radio` | `—` = Paramètres globaux<br />`0` = En colonne<br />`1` = Comme des tuiles masonry | — |
| **Ouvrir les contenus dans une fenêtre modale**<br />`intro_link_to_popup` | Les contenus seront ouverts dans une fenêtre modale _0_ | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Mettre en évidence les contenus**<br />`hl_items_onnav` | Mettre en évidence les contenus actifs et survolés en ajoutant des classes CSS _0_ | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`2` = Au survol | — |

#### Placement du contenu / de l’image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Placement du contenu par rapport à l’image**<br />`content_layout` | Choisir le placement du contenu à côté, au-dessus/en dessous (dégagé) ou sur (superposé) l’image. Remarque : la superposition rogne le contenu qui ne rentre pas par le bas _3_ | `list` | `—` = Paramètres globaux<br />`0` = Flottant (droite)<br />`1` = Flottant (gauche)<br />`2` = Dégagé (au-dessus)<br />`3` = Dégagé (en dessous)<br />`4` = Superposé (en haut)<br />`5` = Superposé (en bas)<br />`6` = Superposé (plein) | — |
| **Contenu visible en superposition**<br />`content_display` | Choisir comment l’image est ajustée dans le conteneur _0_ | `radio` | `—` = Paramètres globaux<br />`0` = Toujours visible<br />`2` = Au survol | — |
| **Ajustement de l’image pour dégagé / superposé**<br />`img_fit` | Choisir comment l’image est ajustée dans le conteneur _1_ | `radio` | `—` = Paramètres globaux<br />`0` = Ajustement automatique<br />`1` = Ajustement automatique et étirement | — |
| **Hauteur du contenu**<br />`content_height_fit_stan` | Choisir Oui pour fixer la même hauteur pour chaque contenu _1_ | `radio` | `—` = Paramètres globaux<br />`0` = Hauteur du contenu<br />`1` = Forcer la même hauteur | — |
| **Hauteur du contenu**<br />`content_width_fit` | Choisir Oui pour fixer la même hauteur pour chaque contenu _1_ | `radio` | `—` = Paramètres globaux<br />`auto-fill` = Remplissage automatique<br />`auto-fit` = Ajustement automatique | `auto-fill` (Remplissage automatique) |
| **Readmore align**<br />`readmore_align` | — | `radio` | `—` = Paramètres globaux<br />`left` = A gauche<br />`center` = Centre<br />`right` = A droite | `center` (Centre) |

### Style

#### Boîte de la liste des contenus

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **couleur d’arrière-plan**<br />`box_background_color` | Couleur d’arrière-plan du conteneur des contenus | `fccolor` | — | `none` |
| **remplissage supérieur/inférieur**<br />`box_padding_top_bottom` | Remplissage du conteneur appliqué en haut et en bas des contenus | `text` | — | `0` |
| **remplissage gauche/droite**<br />`box_padding_left_right` | Remplissage du conteneur appliqué à gauche et à droite des contenus | `text` | — | `0` |
| **marge supérieure**<br />`box_margin_top` | Marge du conteneur appliquée en haut et en bas des contenus | `text` | — | `2rem` |
| **marge inférieure**<br />`box_margin_bottom` | Marge du conteneur appliquée en haut et en bas des contenus | `text` | — | `2rem` |
| **marge gauche/droite**<br />`box_margin_left_right` | Marge du conteneur appliquée à gauche et à droite des contenus | `text` | — | `0` |

#### Boîte du contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **couleur d’arrière-plan**<br />`ibox_background_color` | Couleur d’arrière-plan appliquée à chaque contenu | `fccolor` | — | `none` |
| **couleur de la description**<br />`ibox_description_color` | Couleur d’arrière-plan appliquée à chaque contenu | `fccolor` | — | `none` |
| **largeur de bordure**<br />`ibox_border_width` | Largeur de bordure appliquée autour des contenus | `number` | — | `0` |
| **couleur de bordure**<br />`ibox_border_color` | Largeur de bordure appliquée autour des contenus | `fccolor` | — | `transparent` |
| **remplissage supérieur/inférieur**<br />`ibox_padding_top_bottom` | Remplissage appliqué en haut et en bas des contenus | `text` | — | `0` |
| **remplissage gauche/droite**<br />`ibox_padding_left_right` | Remplissage appliqué à gauche et à droite des contenus | `text` | — | `0` |
| **marge supérieure/inférieure**<br />`ibox_margin_top_bottom` | Marge appliquée en haut et en bas des contenus | `text` | — | `2rem` |
| **marge gauche/droite**<br />`ibox_margin_left_right` | Marge appliquée à gauche et à droite des contenus | `text` | — | `2rem` |

### Champs

#### Bloc (sous-)catégorie, au début de la (sous-)catégorie

:::note
Attention : cela est pertinent si vous triez vos contenus par catégorie (tri de premier niveau), le tri de second niveau pouvant être libre, par exemple le titre
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`intro_catblock` | — | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Titre de la catégorie**<br />`intro_catblock_title` | Afficher/Masquer le titre de la catégorie. | `radio` | `—` = Paramètres globaux<br />`1` = Oui | — |

#### Texte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la description**<br />`intro_use_description` | Afficher ou masquer le texte de description | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Supprimer les balises HTML & tronquer le texte**<br />`intro_strip_html` | Supprimer les balises HTML du texte et les tronque en fonction de la longueur maximum. **Remarque :** Cela forcera l'affichage du lien 'lire la suite' | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui, Forcer 'lire la suite'<br />`2` = Oui, si nécessaire | — |
| **Longueur maximum du texte**<br />`intro_cut_text` | Tronque le texte d'introduction après X caractères | `text` | — | — |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser l'image**<br />`intro_use_image` | Extraire la première image du texte principale | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Source de l'image**<br />`intro_image` | Sélectionner la source de l'image. Vous pouvez aussi choisir un champ image (s'il y en a au moins un de disponible) ou automatiquement extraire l'image de la description. | `fcimage` | — | — |
| **HTML de champ comme image**<br />`intro_image_custom_display` | Vous pouvez utiliser le HTML produit par n’importe quel champ personnalisé à la place de l’image. -- Laissez vide pour utiliser la valeur de la liste déroulante ci-dessus. -- **Remarque : la taille de l’image et les autres paramètres ne sont pas utilisés**. -- Écrivez sous la forme nomchamp##nomvariable, par exemple pour les champs image : imgfieldname##display_small, imgfieldname##display_medium, imgfieldname##display_large | `text` | — | — |
| **URL de champ comme image**<br />`intro_image_custom_url` | Vous pouvez utiliser l’URL produite par n’importe quel champ personnalisé à la place de l’image. -- Laissez vide pour utiliser la valeur de la liste déroulante ci-dessus. -- **Remarque : la taille de l’image et les autres paramètres sont appliqués à l’URL fournie**. -- Écrivez sous la forme nomchamp##nomvariable, par exemple pour les champs image : imgfieldname##display_small_src, imgfieldname##display_medium_src, imgfieldname##display_large_src | `text` | — | — |
| **Image par défaut (lorsque l'image est manquante)**<br />`intro_image_fallback_img` | Quand l'image est manquante, vous pouvez sélectionner une autre image par défaut. ex: l'image du texte d'introduction quand il n'y pas de valeur dans le champs image, même si le champ image possède une image par défaut. | `list` | `0` = Aucune image par défaut<br />`1` = Utiliser l'image du texte d'introduction<br />`2` = Utiliser l'image du texte d'introduction (ignorer l'image par défaut du champ)<br />`3` = Utiliser un champ personnalisé | — |
| **Champ personnalisé de repli**<br />`intro_fallback_field` | — | `fcimage` | — | `0` |
| **Position de l'image**<br />`intro_position` | Définit la position de l'image dans le bloc. | `radio` | `—` = Paramètres globaux<br />`0` = A gauche<br />`1` = A droite | — |
| **Lien sur l'image**<br />`intro_link_image` | Actif un lien sur l'image affichée. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Lien vers**<br />`intro_link_image_to` | Si vous utilisez un champ image, vous pouvez utiliser le lien personnalisé ajouté à l’image | `radio` | `—` = Paramètres globaux<br />`0` = Contenu<br />`1` = Lien personnalisé (champ image) | — |
| **Taille de l'image**<br />`intro_image_size` | Taille de l'image pour l'introduction | `radio` | `—` = Utiliser les paramètres<br />`s` = Petite<br />`m` = Moyenne<br />`l` = Grande<br />`o` = Original | — |
| **Largeur de l'image**<br />`intro_width` | Largeur de l'image | `text` | — | — |
| **Hauteur de l'image**<br />`intro_height` | Hauteur de l'image | `text` | — | — |
| **Méthode de traitement**<br />`intro_method` | Méthode de traitement | `radio` | `—` = Paramètres globaux<br />`0` = A l'échelle<br />`1` = Découper | — |
| **Images par défaut (par type)**<br />`intro_default_images` | Entrez soit un chemin d'image relatif au dossier racine de Joomla : image-path ou entrez par type, séparés par des virgules : _OTHER_##image-path, type-alias1##image-path1, type-alias2##image-path2 | `textarea` | — | — |

#### Onglets des contenus en vedette

#### Onglets de l’élément
