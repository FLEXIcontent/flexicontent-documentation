---
sidebar_position: 5
---

# Modèle de contenu — options communes

Paramètres du modèle de contenu. Ils sont identiques pour les quatre modèles (faq, grid, items-tabbed et table).

:::info Source
Cette page est générée depuis `site/templates/faq/item.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Paramètres du modèle

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage personnalisé du titre**<br />`custom_layout_title` | Ceci sera affiché à l'utilisateur dans la partie publique en tant qu'infobulle du bouton pour changer de mise en page | `text` | — | — |

#### Onglets de l’élément

### Conteneur de contenu

:::note
Style
:::

#### Couleurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur d'arrière-plan**<br />`item_bg_color` | Choisir une couleur de fond | `fccolor` | — | `inherit` |
| **Couleur texte**<br />`item_text_color` | Choisir une couleur de texte | `fccolor` | — | `inherit` |

#### Marge intérieure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Marge intérieure haute**<br />`item_pad_top` | Description du remplissage supérieur de l’élément _0_ | `number` | — | `0` |
| **Marge intérieure gauche**<br />`item_pad_left` | Espace intérieur gauche _0_ | `number` | — | `0` |
| **Marge intérieure droite**<br />`item_pad_right` | Description du remplissage droit de l’élément _0_ | `number` | — | `0` |
| **Marge intérieure basse**<br />`item_pad_bottom` | Tmpl padding bottomt description _0_ | `number` | — | `0` |

#### Bordure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bord arrondi**<br />`item_border_radius` | Arrondi des bordures _0_ | `number` | — | `0` |
| **Couleur bordure**<br />`item_border_color` | Définir la couleur des bordures | `fccolor` | — | `#cccccc` |
| **Taille bordure**<br />`item_border_size` | Définir l'épaisseur des bordures _0_ | `number` | — | `0` |
| **Type de bordure**<br />`item_border_type` | Sélectionnez le type de bordure solid groove dotted dashed double ridge inset outset _solid_ | `list` | `solid` = solide<br />`dotted` = pointillé<br />`dashed` = tiret<br />`double` = double<br />`groove` = rainure<br />`ridge` = ridge<br />`inset` = incrusté<br />`outset` = outset | `solid` (solide) |

### Titre de l'article

:::note
Style
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Taille max. du titre des contenus**<br />`title_cut_text` | Définit le nombre maximum de caractère qui peut être affiché dans le titre d'un contenu appartenant à la catégorie, les titres qui dépassent cette valeur seront automatiquement tronqués et '...' seront ajoutés à la suite du titre | `text` | — | — |

#### Couleurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur texte**<br />`title_color` | Choisir une couleur de texte | `fccolor` | — | `inherit` |
| **Couleur d'arrière-plan**<br />`title_bg_color` | Choisir une couleur de fond | `fccolor` | — | `inherit` |

#### Marge intérieure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Marge intérieure**<br />`title_pad` | Espace intérieur haut _paddng-top padding-right padding-bottom padding-left in px % rem ect_ | `text` | — | `0` |

#### Bordure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bord arrondi**<br />`title_border_radius` | Arrondi des bordures _0_ | `number` | — | `0` |

### Etiquettes

:::note
Style
:::

#### Couleurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur texte**<br />`label_txt_color` | Choisir une couleur de texte _#000000_ | `fccolor` | — | `#000000` |
| **Couleur d'arrière-plan**<br />`label_bg_color` | Choisir une couleur de fond _rgba(255, 255, 255, 0)_ | `fccolor` | — | `rgba(255, 255, 255, 0)` |

#### Marge intérieure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Marge intérieure**<br />`label_pad` | Espace intérieur haut _paddng-top padding-right padding-bottom padding-left in px % rem ect_ | `text` | — | `0` |

#### Bordure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bord arrondi**<br />`label_radius` | Arrondi des bordures _0_ | `number` | — | `0` |

### Position du champ

:::note
Positions pour le placement des champs
:::

#### Onglets de l’élément

### Onglet

#### Style d'onglet

#### Poignets

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur de début du fond**<br />`tab_bg_color_start` | Sélectionner la couleur de départ pour le fond des onglets (début du dégradé) _#3093c7_ | `fccolor` | — | `#3093c7` |
| **Titre**<br />`tab_title_color` | Sélectionner la couleur du texte de l'onglet (titre de l'onglet) _#3093c7_ | `fccolor` | — | `#3093c7` |

#### Boite de contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur texte**<br />`tab_content_bg_color` | Choisir une couleur de texte _#ffffff_ | `fccolor` | — | `#ffffff` |
| **Bord arrondi**<br />`tab_content_border_radius` | Arrondi des bordures _0_ | `number` | — | `0` |
| **Taille de la bordure en haut**<br />`tab_content_border_size_top` | Choisir la taille de la séparation entre l'onglet et l'onglet de contenu _1_ | `number` | — | `1` |
| **Couleur de la bordure en haut**<br />`tab_content_border_color_top` | Choisir la couleur de la séparation entre l'onglet et l'onglet contenu | `fccolor` | — | `#cccccc` |

#### Titres de l'onglet

#### Onglets des sous-titres

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Onglet 1**<br />`subtitle_tab1_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 2**<br />`subtitle_tab2_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 3**<br />`subtitle_tab3_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 4**<br />`subtitle_tab4_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 5**<br />`subtitle_tab5_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 6**<br />`subtitle_tab6_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 7**<br />`subtitle_tab7_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 8**<br />`subtitle_tab8_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 9**<br />`subtitle_tab9_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 10**<br />`subtitle_tab10_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 11**<br />`subtitle_tab11_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 12**<br />`subtitle_tab12_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |

#### Onglets inférieurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Onglet 1**<br />`bottom_tab1_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 2**<br />`bottom_tab2_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 3**<br />`bottom_tab3_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 4**<br />`bottom_tab4_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 5**<br />`bottom_tab5_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 6**<br />`bottom_tab6_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 7**<br />`bottom_tab7_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 8**<br />`bottom_tab8_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 9**<br />`bottom_tab9_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 10**<br />`bottom_tab10_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 11**<br />`bottom_tab11_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |
| **Onglet 12**<br />`bottom_tab12_label` | Le texte de cette étiquette est filtré via JText (vous pouvez l'ajouter à vos fichiers de langue ini) | `text` | — | — |

### Haut / Bas

#### Mode colonne

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur du bloc supérieur**<br />`top_col_width` | La valeur va de span1 à span12 (largeur 100 %). La position « Top » est adjacente à la position « Image » ; leur somme vaut 12. Si une position est vide, l’autre est étendue à 100 % _padding-top padding-right padding-bottom padding-left en px, %, rem, etc._ | `text` | — | `30%` |
| **Espacement**<br />`top_col_gap` | Définir l’espacement entre le bloc image et le bloc supérieur _valeur en px, %, rem, etc._ | `text` | — | `2rem` |
| **Colonne du haut**<br />`top_cols` | Nombre de colonnes à utiliser pour le bloc du haut | `radio` | `—` = Paramètres globaux<br />`one` = 1 colonne<br />`two` = 2 colonnes | — |
| **Colonnes du bas**<br />`bottom_cols` | Nombre de colonnes pour le bloc du bas | `radio` | `—` = Paramètres globaux<br />`one` = 1 colonne<br />`two` = 2 colonnes | — |

#### Style de la boîte du haut

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Marge intérieure haute**<br />`column_pad_top` | Espace intérieur haut _paddng-top padding-right padding-bottom padding-left in px % rem ect_ | `text` | — | `10px 10px 10px 10px` |
| **Couleur texte**<br />`column_color_top` | Choisir une couleur de texte | `fccolor` | — | `inherit` |
| **Couleur d'arrière-plan**<br />`column_bg_color_top` | Choisir une couleur de fond | `fccolor` | — | `transparent` |
| **Bord arrondi**<br />`column_border_radius_top` | Arrondi des bordures _0_ | `number` | — | `05` |
| **Taille bordure**<br />`column_border_size_top` | Définir l'épaisseur des bordures _1_ | `number` | — | `1` |
| **Couleur bordure**<br />`column_border_color_top` | Définir la couleur des bordures | `fccolor` | — | `#cccccc` |
| **Type de bordure**<br />`column_border_type_top` | Sélectionnez le type de bordure solid groove dotted dashed double ridge inset outset _solid_ | `list` | `solid` = solide<br />`dotted` = pointillé<br />`dashed` = tiret<br />`double` = double<br />`groove` = rainure<br />`ridge` = ridge<br />`inset` = incrusté<br />`outset` = outset | `solid` (solide) |

#### Style de la boite inférieure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Marge intérieure basse**<br />`column_pad_bottom` | Espace intérieur haut _paddng-top padding-right padding-bottom padding-left in px % rem ect_ | `text` | — | `0` |
| **Couleur texte**<br />`column_color_bottom` | Choisir une couleur de texte | `fccolor` | — | `#cccccc` |
| **Couleur d'arrière-plan**<br />`column_bg_color_bottom` | Choisir une couleur de fond | `fccolor` | — | `#ffffff` |
| **Bord arrondi**<br />`column_border_radius_bottom` | Arrondi des bordures _0_ | `number` | — | `0` |
| **Taille bordure**<br />`column_border_size_bottom` | Définir l'épaisseur des bordures _1_ | `number` | — | `0` |
| **Couleur bordure**<br />`column_border_color_bottom` | Définir la couleur des bordures | `fccolor` | — | `#cccccc` |
| **Type de bordure**<br />`column_border_type_bottom` | Sélectionnez le type de bordure solid groove dotted dashed double ridge inset outset _solid_ | `list` | `solid` = solide<br />`dotted` = pointillé<br />`dashed` = tiret<br />`double` = double<br />`groove` = rainure<br />`ridge` = ridge<br />`inset` = incrusté<br />`outset` = outset | `solid` (solide) |

### Classes CSS

:::note
Classe CSS pour la position des conteneurs
:::

#### Sous-titre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Sous-titre 1**<br />`box_class_subtitle1` | Classe CSS du sous-titre 1 _flexi group lineinfo subtitle1_ | `text` | — | — |
| **Sous-titre 2**<br />`box_class_subtitle2` | Classe CSS du sous-titre 2 _flexi group lineinfo subtitle2_ | `text` | — | — |
| **Sous-titre 3**<br />`box_class_subtitle3` | Classe CSS du sous-titre 3 _flexi group lineinfo subtitle3_ | `text` | — | — |

#### Onglets des sous-titres

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Onglet 1**<br />`box_class_subtitle_tab1` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 2**<br />`box_class_subtitle_tab2` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 3**<br />`box_class_subtitle_tab3` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 4**<br />`box_class_subtitle_tab4` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 5**<br />`box_class_subtitle_tab5` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 6**<br />`box_class_subtitle_tab6` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 7**<br />`box_class_subtitle_tab7` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 8**<br />`box_class_subtitle_tab8` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 9**<br />`box_class_subtitle_tab9` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 10**<br />`box_class_subtitle_tab10` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 11**<br />`box_class_subtitle_tab11` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 12**<br />`box_class_subtitle_tab12` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |

#### Contenu principal

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Image**<br />`box_class_image` | Classe CSS de l’image _flexi group image_ | `text` | — | — |
| **En haut**<br />`box_class_top` | Top class description _flexi group infoblock_ | `text` | — | — |
| **Description**<br />`box_class_descr` | Classe CSS de la description _flexi group description_ | `text` | — | — |

#### Onglets inférieurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Onglet 1**<br />`box_class_bottom_tab1` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 2**<br />`box_class_bottom_tab2` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 3**<br />`box_class_bottom_tab3` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 4**<br />`box_class_bottom_tab4` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 5**<br />`box_class_bottom_tab5` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 6**<br />`box_class_bottom_tab6` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 7**<br />`box_class_bottom_tab7` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 8**<br />`box_class_bottom_tab8` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 9**<br />`box_class_bottom_tab9` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 10**<br />`box_class_bottom_tab10` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 11**<br />`box_class_bottom_tab11` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |
| **Onglet 12**<br />`box_class_bottom_tab12` | Classe CSS de l’onglet _flexi lineinfo_ | `text` | — | — |

#### Bas

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **En bas**<br />`box_class_bottom` | Bottomfield class description _flexi group infoblock_ | `text` | — | — |

#### Onglets de l’élément

#### Onglets de l’élément
