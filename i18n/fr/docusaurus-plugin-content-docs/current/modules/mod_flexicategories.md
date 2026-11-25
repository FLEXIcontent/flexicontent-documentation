---
sidebar_position: 5
---

# Catégories

FLEXIcontent fournit six modules frontend pour afficher des contenus, des catégories, des formulaires de recherche, des filtres, des cartes et des nuages d’étiquettes. Configurez un module depuis **Extensions → Modules**.

> Ce module affiche une liste de catégories depuis une catégorie parente

:::info Source
Cette page est générée depuis `modules/mod_flexicategories/mod_flexicategories.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

### Template du module

:::note
Veuillez définir les paramètres de disposition dans l’onglet **Disposition : ...**. Les développeurs CSS/HTML doivent consulter : ** Guide des modèles personnalisés **
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Template**<br />`layout` | Choisir la mise en page de votre module | `fclayout` | — | `default` |

### Paramètres de base

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégorie parente**<br />`parent` | Choisir une catégorie parente | `category` | — | — |
| **Catégories vides**<br />`show_empty_cats` | Sélectionnez cette option pour ignorer les catégories qui sont vides et ainsi que leurs sous-catégories | `multilist` | `0` = Jhide<br />`1` = Jshow | `1` (Jshow) |
| **# Premier niveau sous-catégories**<br />`count` | Sélectionnez le nombre de premiers niveau des sous-catégories à afficher. Valeur par défaut est tous. | `list` | `0` = Jall<br />`1` = J1<br />`2` = J2<br />`3` = J3<br />`4` = J4<br />`5` = J5<br />`6` = J6<br />`7` = J7<br />`8` = J8<br />`9` = J9<br />`10` = J10 | `0` (Jall) |

#### Informations affichées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description des catégories**<br />`show_description` | Afficher/Masquer la description de la catégorie | `radio` | `0` = Jhide<br />`1` = Jshow | `0` (Jhide) |
| **Nombre de contenu (dans le cache)**<br />`numitems` | Afficher ou masquer plusieurs articles. Cela est mis à jour chaque 1 heure par exemple, veillez vérifier valeur du délai du cache de FLEXIcontent dans les paramètres avancés du composants | `radio` | `0` = Jhide<br />`1` = Jshow | `0` (Jhide) |

#### Sous-Catégories

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les sous-catégories**<br />`show_children` | Afficher/Masquer les sous catégories | `radio` | `0` = Jno<br />`1` = Jyes | `0` (Jno) |
| **Profondeur de niveau maximum**<br />`maxlevel` | Sélectionnez la profondeur maximale de niveau pour chaque sous-catégorie. Valeur par défaut est tous. | `list` | `0` = Jall<br />`1` = J1<br />`2` = J2<br />`3` = J3<br />`4` = J4<br />`5` = J5<br />`6` = J6<br />`7` = J7<br />`8` = J8<br />`9` = J9<br />`10` = J10 | `0` (Jall) |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Montrer l'image**<br />`show_description_image` | Afficher/Masquer l'image, vous pouvez aussi sélectionner la source de l'image | `multilist` | `0` = Jno<br />`1` = Jyes | `0` (Jno) |
| **Source de l'image de la catégorie**<br />`cat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | `radio` | `0` = Extraire de la description<br />`1` = Utiliser l'image via les paramètres<br />`2` = Essayer les paramètres, puis extraire l'image de la description | `2` (Essayer les paramètres, puis extraire l'image de la description) |
| **Lien sur l'image**<br />`cat_link_image` | Lien sur l'image de la vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Méthode de traitement**<br />`cat_image_method` | Méthode de traitement permettant de générer la miniature, à l'échelle: redimensionne image proportionnellement, découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `radio` | `0` = A l\\'échelle<br />`1` = Recadrage | `1` (Recadrage) |
| **largeur**<br />`cat_image_width` | largeur | `text` | — | `24` |
| **Hauteur**<br />`cat_image_height` | Hauteur | `text` | — | `24` |
| **Position de l'image**<br />`cat_image_float` | La position de l'image dans le bloc. | `radio` | `left` = A gauche<br />`right` = A droite | `left` (A gauche) |
| **Image par défaut**<br />`cat_default_image` | Catégorie par défaut pour les catégories qui n'en possèdent pas | `media` | — | — |
| **Mod flexicategories image webp**<br />`cat_image_webp` | Mod flexicategories image webp description | `radio` | `0` = Jno<br />`1` = Jyes | `0` (Jno) |

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
| **Style de titre**<br />`item_heading` | Veuillez indiquer le style à utiliser pour les titres | `list` | `1` = Jh1<br />`2` = Jh2<br />`3` = Jh3<br />`4` = Jh4<br />`5` = Jh5 | `4` (Jh4) |
| **Suffixe de classe du module**<br />`moduleclass_sfx` | Suffixe de classe CSS ajouté au module | `textarea` | — | — |
| **Cache du champ Modules**<br />`owncache` | Mise en cache de la valeur du champ Modules | `list` | `1` = Utiliser la configuration globale<br />`0` = Valeur du champ Modules sans cache | `1` (Utiliser la configuration globale) |
| **Durée du cache du champ Modules**<br />`cache_time` | Durée pendant laquelle le champ Modules est mis en cache | `text` | — | `900` |
