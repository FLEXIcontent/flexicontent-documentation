---
sidebar_position: 9
---

# Table — vue catégorie



:::info Source
Cette page est générée depuis `site/templates/table/category.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Paramètres du modèle

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage personnalisé du titre**<br />`custom_layout_title` | Ceci sera affiché à l'utilisateur dans la partie publique en tant qu'infobulle du bouton pour changer de mise en page | `text` | — | — |

#### Onglets de l’élément

### Base

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Classe CSS du tableau**<br />`table_class` | Remplacer la classe Css du tableau. Par défaut \"adminlist\", vous pouvez utiliser \"table table-striped\", \"table table-hover\", etc ... par rapport au framework utiliser par votre template | `text` | — | — |

### Affichage

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Titre (Libellé des champs)**<br />`show_field_labels_row` | Afficher dans l'entête du tableau les libellés de chaque champ affiché. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Personnaliser l’en-tête de la colonne Titre**<br />`customize_titlecol_header` | Sélectionnez Oui pour utiliser un texte personnalisé pour l’en-tête de la colonne de titre | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Texte d’en-tête de la colonne titre**<br />`titlecol_header_text` | Entrez le texte d’en-tête de la colonne. Il peut s’agir d’une chaîne de langue | `text` | — | — |
| **Colonnes désactivables**<br />`togglable_table_cols` | Autoriser l’utilisateur à activer/désactiver (cacher/montrer) les colonnes du tableau | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

### Titre de l'article

#### Titre de l'article

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
| **Marge intérieure haute**<br />`title_pad_top` | Espace intérieur haut _0_ | `number` | — | `0` |
| **Marge intérieure gauche**<br />`title_pad_left` | Espace intérieur gauche _0_ | `number` | — | `0` |
| **Marge intérieure droite**<br />`title_pad_right` | Espace intérieur droite _0_ | `number` | — | `0` |
| **Marge intérieure basse**<br />`title_pad_bottom` | Espace intérieur bas _0_ | `number` | — | `0` |

#### Bordure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bord arrondi**<br />`title_border_radius` | Arrondi des bordures _0_ | `number` | — | `0` |

### Etiquettes

#### Style des étiquettes

#### Couleurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur texte**<br />`label_txt_color` | Choisir une couleur de texte _#ffffff_ | `fccolor` | — | `#ffffff` |
| **Couleur d'arrière-plan**<br />`label_bg_color` | Choisir une couleur de fond _#999999_ | `fccolor` | — | `#999999` |

#### Marge intérieure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Marge intérieure haute**<br />`label_pad_top` | Espace intérieur haut _2_ | `number` | — | `2` |
| **Marge intérieure gauche**<br />`label_pad_left` | Espace intérieur gauche _4_ | `number` | — | `4` |
| **Marge intérieure droite**<br />`label_pad_right` | Espace intérieur droite _4_ | `number` | — | `4` |
| **Marge intérieure basse**<br />`label_pad_bottom` | Espace intérieur bas _2_ | `number` | — | `2` |

#### Bordure

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bord arrondi**<br />`label_radius` | Arrondi des bordures _3_ | `number` | — | `3` |

### Titre (libellé des champs)

#### Style des cellules d'en-tête du tableau

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur texte**<br />`th_txt_color` | Choisir une couleur de texte | `fccolor` | — | `inherit` |
| **Couleur d'arrière-plan**<br />`th_bg_color` | Choisir une couleur de fond | `fccolor` | — | `inherit` |

### Lignes d'élément (Valeurs du champ)

#### Style des cellules de données du tableau

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Couleur bordure**<br />`td_border_color` | Définir la couleur des bordures _#dadada_ | `fccolor` | — | `#dadada` |
| **Taille bordure**<br />`td_border_size` | Définir l'épaisseur des bordures _0_ | `number` | — | `0` |

#### Version HTML

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Alignement du texte**<br />`td_txt_align` | Choisir l'alignement du texte dans la cellule | `radio` | `inherit` = Inherit<br />`left` = Left<br />`right` = Right<br />`center` = Center | `inherit` (Inherit) |

#### Style tableau

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Fond des lignes impaires**<br />`table_row0_bg_color` | Sélectionner la couleur de fond pour les lignes impaires du tableau _#ffffff_ | `fccolor` | — | `#ffffff` |
| **Fond des lignes paires**<br />`table_row1_bg_color` | Sélectionner la couleur de fond pour les lignes impaires du tableau _#f7f7f7_ | `fccolor` | — | `#f7f7f7` |
| **Couleur texte**<br />`table_value_color` | Sélectionner la couleur du texte dans le tableau _#555555_ | `fccolor` | — | `#555555` |
| **Couleur au survol**<br />`td_bg_hoverbgcolor` | Définir la couleur d'arrière-plan pour le survol de la td | `fccolor` | — | `inherit` |

#### Onglets de l’élément
