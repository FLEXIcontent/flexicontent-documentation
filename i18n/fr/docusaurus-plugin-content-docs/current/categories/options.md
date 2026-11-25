---
sidebar_position: 3
---

# Catégories — options

Les catégories FLEXIcontent ajoutent leurs propres paramètres d’affichage, de filtrage, de liste et de flux RSS aux champs standard des catégories Joomla!. Ouvrez-les depuis **Composants → FLEXIcontent → Catégories**.

:::info Source
Cette page est générée depuis `admin/models/forms/category.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

#### Image de la catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Image**<br />`image` | Sélectionner l'image pour la catégorie | `fcmedia` | — | — |
| **Libellé du texte alternatif de l’image du champ**<br />`image_alt` | Description du texte alternatif de l’image du champ | `text` | — | — |

## Affichage des catégories

#### En-tête

### Boutons

#### Bouton de page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode d'impression**<br />`print_behaviour` | Selectionnez pour ouvrir automatiquement la fenêtre d'impression du navigateur, ou afficher un bouton d'impression dans la page | `fcradio` | `—` = Paramètres globaux<br />`auto` = Auto<br />`button` = Bouton | — |
| **Icône imprimer**<br />`show_print_icon` | Affiche l'icône d'impression. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Icône email**<br />`show_email_icon` | Activer le partage de la page via e-mail | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Icône du flux RSS**<br />`show_feed_icon` | Activer la prévisualisation de la page actuelle dans une fenêtre popup. Cela facilitera aussi l'inscription de vos visiteurs | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Flux RSS**<br />`show_feed_link` | Activer cette option pour insérer un lien vers le flux RSS dans le HEAD de votre page HTML. Cela permet aux navigateurs de souscrire à l'actualité des contenus de la catégorie. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Bouton d'export CSV**<br />`show_csvbutton` | Activer l'export CSV | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |

#### Ajouter un nouvel article

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bouton**<br />`show_addbutton` | Permet l’affichage du bouton **Ajouter un nouvel contenu** aux catégories et** listes**, là où l’utilisateur connecté peut en ajouter | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Afficher les contenus non-autorisés**<br />`nonauth_addbutton` | Afficher le bouton 'soumettre' aux utilisateurs non-autorisés. **Si actif, attention**: sauf si le lien de menu permet la soumission d'éléments par les utilisateurs non autorisés -&gt; a. les invités sont redirigés vers la page de connexion / b. les utilisateurs connectés mais non autorisés sont redirigés sur l'URL indiquée - dans la configuration du composant - surclassé par l'uRL dans la configuration du type de contenu - surclassé par l'uRL dans le lien de menu de soumission | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui, sauf pour les invités<br />`2` = Oui | — |
| **Menu de soumission de contenu**<br />`addbutton_menu_itemid` | Vous pouvez forcer un un réglage spécifique d'un élément de menu , de sorte que la configuration personnalisée est utilisée , par exemple, limiter le type de contenu spécifique (s ) . ** NOTE 1 ** : Au cas où vous souhaitez autoriser type de contenu spécifique pour des catégories spécifiques , vous devriez refuser « créer des contenus de privilège ACL aux utilisateurs , ils seront ainsi en mesure de présenter uniquement par le type de contenu OVERRIDE par le produit soumettre menu. ** NOTE 2 ** : Vous pouvez également remplacer la catégorie ACL trop | `fcmenuitem` | `—` = Paramètres globaux | — |

#### Personnalisé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les icônes**<br />`show_icons` | Affiche les icônes imprimer et email ou utiliser uniquement le texte | `fcradio` | `—` = Paramètres globaux<br />`0` = Texte<br />`1` = Icônes<br />`2` = Les deux | — |
| **Type d'icône**<br />`use_font_icons` | Vous pouvez afficher des icônes comme des images ou utiliser les jeu de polices d’icônes | `fcradio` | `—` = Paramètres globaux<br />`0` = Image<br />`1` = Icônes polices | — |
| **Pré-configuration**<br />`font_icon_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`0` = Utiliser les paramètres du composant (nettoie)<br />`1` = Charger par défaut & personnalisation | — |
| **Icônes polices**<br />`font_icon_classes` | Utiliser les virgules pour séparer les options, pour charger les valeurs par défaut et ainsi voir les format originels, vider le champ et sauver | `textarea` | — | — |

#### Placement des boutons

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Placer dans la liste déroulante**<br />`btn_grp_dropdown` | Afficher les boutons dans une liste déroulante, en général cela utilisera les styles bootstrap ou similaire, et cela peut ne pas être modifié par les modèles personnalisés | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Icône liste**<br />`btn_grp_dropdown_class` | Icône représentant la liste déroulante | `text` | — | — |

### Information de la catégorie

:::note
Fichier de mise en page : **%s**
:::

### Information de la catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Titre de la catégorie**<br />`show_cat_title` | Afficher/Masquer le titre de la catégorie. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Taille max. du titre des contenus**<br />`title_cut_text` | Définit le nombre maximum de caractère qui peut être affiché dans le titre d'un contenu appartenant à la catégorie, les titres qui dépassent cette valeur seront automatiquement tronqués et '...' seront ajoutés à la suite du titre | `text` | — | — |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Image de la catégorie**<br />`show_description_image` | Afficher/Masquer l'image de la catégorie. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Source de l'image de la catégorie**<br />`cat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | `fcradio` | `—` = Paramètres globaux<br />`0` = Extraire de la description<br />`1` = Utiliser l'image des paramètres<br />`2` = Essayer les paramètres, puis extraire de la description | — |
| **Lien sur l'image**<br />`cat_link_image` | Actif un lien sur l'image affichée. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Méthode de traitement**<br />`cat_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `fcradio` | `—` = Paramètres globaux<br />`0` = A l'échelle<br />`1` = Découper | — |
| **Largeur de l'image**<br />`cat_image_width` | Largeur de l'image | `text` | — | — |
| **Hauteur de l'image**<br />`cat_image_height` | Hauteur de l'image | `text` | — | — |

#### Description

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description de la catégorie**<br />`show_description` | Afficher/Masquer la description de la catégorie | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content_cat` | Activer cette option si vous souhaitez exécuter les plugins de contenu (onPrepareContent) sur la description de la catégorie. Gardez à l'esprit que tous les plugins ne fonctionne pas forcément en dehors du com_content. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

### Liste des sous-catégories

:::note
Fichier de mise en page : **%s**
:::

### Sous-catégories (1er sous-niveau)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Sous-catégories**<br />`show_subcategories` | Afficher/Cacher les sous-catégories | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Ordre de la liste de catégorie**<br />`subcat_orderby` | Ordre la liste des catégories, les options disponibles dépendent des propriétés de l'ensemble des catégories. | `multilist` | `—` = Paramètres globaux<br />`date` = Les plus anciens<br />`rdate` = Plus récents en premier<br />`modified` = Derniers modifiés en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés en premier<br />`rhits` = Les moins consultés en premier<br />`order` = Attribut d'ordre des catégories<br />`random` = Aléatoire | — |

#### Information catégories

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Compteur de contenu**<br />`show_itemcount` | Afficher/cacher le nombre de contenu de chaque sous-catégorie | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer<br />`2` = Afficher avec le libellé | — |
| **Nombre de sous-catégories**<br />`show_subcatcount` | Afficher / masquer le nombre de sous-catégories de chaque sous-catégorie | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer<br />`2` = Afficher avec le libellé | — |
| **Catégories vides (nombre d'éléments requis activé)**<br />`show_empty_cats` | Afficher / masquer les catégories sans articles. REMARQUE: cela fonctionne lorsque le comptage d'éléments est activé | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Image de la catégorie**<br />`show_description_image_subcat` | Afficher/Masquer l'image de la catégorie. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Source de l'image de la catégorie**<br />`subcat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | `fcradio` | `—` = Paramètres globaux<br />`0` = Extraire de la description<br />`1` = Utiliser l'image des paramètres<br />`2` = Essayer les paramètres, puis extraire de la description | — |
| **Lien sur l'image**<br />`subcat_link_image` | Actif un lien sur l'image affichée. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Méthode de traitement**<br />`subcat_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `fcradio` | `—` = Paramètres globaux<br />`0` = A l'échelle<br />`1` = Découper | — |
| **Largeur de l'image**<br />`subcat_image_width` | Largeur de l'image | `text` | — | — |
| **Hauteur de l'image**<br />`subcat_image_height` | Hauteur de l'image | `text` | — | — |

#### Description

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description de la catégorie**<br />`show_description_subcat` | Afficher/Masquer la description de la catégorie | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Longueur maximum de la description de la catégorie**<br />`description_cut_text_subcat` | Définit le nombre maximum de caractères affichés dans la description d'une catégorie, les descriptions qui dépassent cette valeur seront automatiquement tronquées et '...' seront ajoutés à la suite de la description | `text` | — | — |

#### Liste des Catégories

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Liste des étiquettes**<br />`show_label_subcats` | Afficher un libellé 'Sous Catégories' devant chaque liste de sous catégories. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Pré-configuration**<br />`prx_sfx_open_close_configs_subcat` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
| **Préfixe sous-catégorie**<br />`subcat_pretext` | Ce texte est placé b&gt;devant** chaque titre de sous catégories. | `text` | — | — |
| **Suffixe sous-catégorie**<br />`subcat_posttext` | Ce texte est placé b&gt;après** chaque titre de sous catégories. | `text` | — | — |
| **Séparateur sous catégorie**<br />`subcat_separatorf` | Choisir le caractère qui séparera la liste des titres de sous catégories. | `multilist` | `—` = Paramètres globaux<br />`0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | — |
| **Texte d'ouverture**<br />`subcat_opentag` | Texte ou code HTML ajouté au début d'une liste de valeur. | `text` | — | — |
| **Texte de fermeture**<br />`subcat_closetag` | Texte ou code HTML ajouté au fin d'une liste de valeur. | `text` | — | — |

### Liste des catégories connexes

:::note
Fichier de mise en page : **%s**
:::

### Catégories connexes (même niveau)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégories connexes**<br />`show_peercategories` | Afficher/Cacher les catégories connexes | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Ordre de la liste de catégorie**<br />`peercat_orderby` | Ordre la liste des catégories, les options disponibles dépendent des propriétés de l'ensemble des catégories. | `multilist` | `—` = Paramètres globaux<br />`date` = Les plus anciens<br />`rdate` = Plus récents en premier<br />`modified` = Derniers modifiés en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés en premier<br />`rhits` = Les moins consultés en premier<br />`order` = Attribut d'ordre des catégories<br />`random` = Aléatoire | — |

#### Information catégories

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Compteur de contenu**<br />`show_itemcount_peercat` | Afficher/Cacher le nombre de contenu de chaque catégorie connexe | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer<br />`2` = Afficher avec le libellé | — |
| **Nombre de catégories connexes**<br />`show_subcatcount_peercat` | Afficher/Cacher le nombre de sous-catégories de chaque catégorie connexe | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer<br />`2` = Afficher avec le libellé | — |
| **Catégories vides (nombre d'éléments requis activé)**<br />`show_empty_peercats` | Afficher / masquer les catégories sans articles. REMARQUE: cela fonctionne lorsque le comptage d'éléments est activé | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Image de la catégorie**<br />`show_description_image_peercat` | Afficher/Masquer l'image de la catégorie. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Source de l'image de la catégorie**<br />`peercat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | `fcradio` | `—` = Paramètres globaux<br />`0` = Extraire de la description<br />`1` = Utiliser l'image des paramètres<br />`2` = Essayer les paramètres, puis extraire de la description | — |
| **Lien sur l'image**<br />`peercat_link_image` | Actif un lien sur l'image affichée. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Méthode de traitement**<br />`peercat_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `fcradio` | `—` = Paramètres globaux<br />`0` = A l'échelle<br />`1` = Découper | — |
| **Largeur de l'image**<br />`peercat_image_width` | Largeur de l'image | `text` | — | — |
| **Hauteur de l'image**<br />`peercat_image_height` | Hauteur de l'image | `text` | — | — |

#### Description

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description de la catégorie**<br />`show_description_peercat` | Afficher/Masquer la description de la catégorie | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Longueur maximum de la description de la catégorie**<br />`description_cut_text_peercat` | Définit le nombre maximum de caractères affichés dans la description d'une catégorie, les descriptions qui dépassent cette valeur seront automatiquement tronquées et '...' seront ajoutés à la suite de la description | `text` | — | — |

#### Liste des Catégories

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Liste des étiquettes**<br />`show_label_peercats` | Afficher un libellé avant la liste des catégories connexes **Remarque :** Si à la fois les images et descriptions de la sous-catégorie sont désactivées, alors le libellé et les enregistrements de la liste seront placés à l'intérieur des conteneurs 'inline' | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Pré-configuration**<br />`prx_sfx_open_close_configs_peercat` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
| **Préfixe sous-catégorie**<br />`peercat_pretext` | Ce texte est placé b&gt;devant** chaque titre de sous catégories. | `text` | — | — |
| **Suffixe sous-catégorie**<br />`peercat_posttext` | Ce texte est placé b&gt;après** chaque titre de sous catégories. | `text` | — | — |
| **Séparateur sous catégorie**<br />`peercat_separatorf` | Choisir le caractère qui séparera la liste des titres de sous catégories. | `multilist` | `—` = Paramètres globaux<br />`0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | — |
| **Texte d'ouverture**<br />`peercat_opentag` | Texte ou code HTML ajouté au début d'une liste de valeur. | `text` | — | — |
| **Texte de fermeture**<br />`peercat_closetag` | Texte ou code HTML ajouté au fin d'une liste de valeur. | `text` | — | — |

#### En-tête

## Formulaire de recherche et filtrage

#### Formulaire de recherche / filtrage

### Basique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Placement des champs formulaires**<br />`ff_placement` | Sélectionner où le formulaire sera placé | `multilist` | `—` = Paramètres globaux<br />`0` = En ligne<br />`1` = Slider | — |
| **Titre du slider**<br />`ff_toggle_search_title` | Le texte de lien/bouton d'ouverture/affichage du formulaire de recherche par défaut est 'Recherche' | `text` | — | — |
| **Validation automatique**<br />`filter_autosubmit` | Envoyer un formulaire automatiquement lors d'un changement de filtre. Si vous n'activez pas cela, alors les utilisateurs seront en mesure de mettre de nombreux filtres avant de soumettre le formulaire. **NOTE : ** Certains filtre peuvent auto-envoyer le formulaire en dépit de ce paramètre | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser le filtrage Ajax**<br />`filter_ajax` | Filtrage Ajax | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Badge de filtre**<br />`badge_position` | Description du badge de filtre | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = En haut<br />`2` = En bas | — |
| **Instructions**<br />`filter_instructions` | Afficher les instructions d'utilisation du formulaire de filtrage. Vous pouvez créer des substitutions de langue joomla pour les chaînes de langue pour donner des instructions personnalisées à vos utilisateurs | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Oui, comme un popup info-bulle<br />`2` = Oui, comme un texte en ligne. | — |

#### Boutons

:::note
Bouton rechercher
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bouton rechercher**<br />`show_search_go` | Envoyer le formulaire pour recharger la liste actuelle, ** Remarque **: tous les critères suivant seront pris en compte, la recherche de texte, les filtres dans les champs et l'indice alpha (lorsque ces valeurs sont présentes) | `multilist` | `—` = Paramètres globaux<br />`0` = Auto<br />`1` = Montrer | — |
| **Class du bouton rechercher**<br />`flexi_button_class_go` | Classe pour le bouton de réinitialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | `multilist` | `—` = Paramètres globaux<br />`-1` = - Personnalisé -<br />`btn` = Plein<br />`btn btn-primary` = Principale<br />`btn btn-success` = Succès<br />`btn btn-info` = Info<br />`btn btn-warning` = Avertissement<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | — |
| **Classe personnalisée**<br />`flexi_button_class_go_custom` | Ajouter une classe personnalisée pour le bouton go, exemple uk-button uk-button-large pour un template Warp7 | `text` | — | — |

:::note
Bouton annuler
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bouton annuler**<br />`show_search_reset` | Effacer le formulaire pour recharger la liste actuelle, ** Remarque **: Notez que cela va aussi supprimer les valeurs saisies dans les filtres et de l'indice alpha (lorsque ces produits sont présents) | `multilist` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Classe du bouton annuler**<br />`flexi_button_class_reset` | Classe pour le bouton de réinitialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | `multilist` | `—` = Paramètres globaux<br />`-1` = - Personnalisé -<br />`btn` = Plein<br />`btn btn-primary` = Principale<br />`btn btn-success` = Succès<br />`btn btn-info` = Info<br />`btn btn-warning` = Avertissement<br />`btn btn-danger` = Danger<br />`btn btn-inverse` = Inverse | — |
| **Classe personnalisée**<br />`flexi_button_class_reset_custom` | Ajouter une classe personnalisée pour le bouton de réinitialisation, exemple uk-button uk-button-large pour un template Warp7 | `text` | — | — |

#### Chercher / Filtrer

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe sous-catégorie**<br />`filter_pretext` | Ce texte est placé b&gt;devant** chaque titre de sous catégories. | `text` | — | — |
| **Suffixe sous-catégorie**<br />`filter_posttext` | Ce texte est placé b&gt;après** chaque titre de sous catégories. | `text` | — | — |
| **Texte d'ouverture**<br />`filter_opentag` | Texte ou code HTML ajouté au début d'une liste de valeur. | `text` | — | — |
| **Texte de fermeture**<br />`filter_closetag` | Texte ou code HTML ajouté au fin d'une liste de valeur. | `text` | — | — |
| **1 enregistrement par ligne**<br />`filter_placement` | Sélectionnez la façon dont les résultats seront affichés: - Afficher un seul enregistrement par ligne, ou - Utilisez un séparateur personnalisé | `fcradio` | `—` = Paramètres globaux<br />`0` = Non, utilisé un séparateur<br />`1` = Oui<br />`2` = Oui, mais utiliser l'option ci-dessous<br />`3` = Placer dans un onglet | — |
| **Séparateur de résultat ignoré si les enregistrements sont affichés par ligne**<br />`filter_separatorf` | Choisissez un séparateur pour séparer les enregistrements (placé entre les valeurs). ** Remarque : ** Ce paramètre est ignoré lorsque vous placez les enregistrements par ligne | `multilist` | `—` = Paramètres globaux<br />`0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | — |

### Texte à Rechercher

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser la recherche**<br />`use_search` | Afficher la zone de recherche textuel | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Afficher les étiquettes**<br />`show_search_label` | Vous pouvez cacher ou afficher le libellé à l'intérieur de la zone de recherche de texte pour économiser de l'espace | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = En dehors du champs<br />`2` = Dans le champs | — |
| **Combinaison de mots**<br />`show_searchphrase` | Permettre aux utilisateurs de sélectionner la méthode de combiner les mots à rechercher, par exemple, phrase, expression (davantage de résultats), tous les mots, n’importe quel mot, expression exacte | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Combinaison par défaut**<br />`default_searchphrase` | Méthode par défaut (présélectionné) pour combiner les termes de recherche | `fcradio` | `—` = Paramètres globaux<br />`all` = Tous les mots<br />`any` = N'importe quel mot<br />`exact` = Phrase exacte<br />`natural` = Phrase<br />`natural_expanded` = Phrase, plus de résultats | — |
| **Utiliser la subggestion automatique**<br />`search_autocomplete` | Sélectionnez cette option pour utiliser une auto-complétion multi-mots ou une méthode de saisie automatique plus simple ou désactiver la complétion automatique | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Simple<br />`2` = Mots clés | — |

### Champs filtre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les filtres**<br />`use_filters` | Permettra d'afficher les filtres de champs. Notez que vous pouvez définir l'apparence et le comportement du filtre en modifiant la configuration de chaque champ individuellement | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Afficher chaque filtre dans un accordéon**<br />`fc_filter_in_slide` | Afficher la valeur de chaque champ dans son accordéon | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | `0` (Non) |
| **Ordre de filtrage**<br />`filters_order` | Sélectionner l'ordre d'affichage des champs | `fcradio` | `—` = Paramètres globaux<br />`0` = Défaut(Gestionnaire de champ)<br />`1` = Personnalisé (en dessous) | — |
| **Choisissez les filtres**<br />`filters` | Choisissez les filtres que vous souhaitez charger pour cette catégorie | `filters` | — | — |
| **Etiquette des filtres**<br />`show_filter_labels` | Forcer l'affichage ou non de l'ensemble des libellés pour chaque champ de filtre, ce paramètre outrepassera automatiquement les paramètre de chaque champs. | `fcradio` | `—` = Paramètres globaux<br />`0` = Réglages des champs<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | — |
| **Valeurs initiales de filtres**<br />`initial_filters` | Ce sont les valeurs initiales des filtres, l'utilisateur peut les remplacer. Exemple : field_id##value %% field_id##value Exemple : 22##14 %% 47##some field value %% 19##someword - **Valeurs uniques**: field_id##value1 - **Ranges**: field_id##value1---value2 - **Valeurs multiples**: field_id##value1+++++++valeur3 - **Relation / Relation / Reverse-relation**: REL_field_id##RELEM_id~value1 - **Plages de décalage de dates**: field_id##now-50d---now+50d (utilisez d pour les jours, m pour les mois, y pour les années) e. . dates jusqu'à maintenant : 45##---now+0d Remarque : votre champ doit être configuré pour être un filtre de plage ou un filtre multi-valeur, sinon les valeurs ne seront pas utilisées comme prévu | `textarea` | — | — |

#### Filtres bloqués

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser un filtrage bloqué**<br />`use_persistent_filters` | Filtres qui ne peuvent PAS être remplacés par l'utilisateur, **NOTE :** Celles-ci peuvent être cachées ou vous pouvez choisir de les afficher (la saisie de l'utilisateur sera interdite) | `multilist` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Valeur des filtres bloqués**<br />`persistent_filters` | Filtres qui ne peuvent PAS être remplacés par un utilisateur. Exemple : field_id##value %% field_id##value Exemple : 22##14 %% 47##some field value %% 19##someword - **Valeurs uniques**: field_id##value1 - **Ranges**: field_id##value1---value2 - **Valeurs multiples**: field_id##value1+++++++valeur3 - **Relation / Relation / Reverse-relation**: REL_field_id##RELEM_id~value1 - **Plages de décalage de dates**: field_id##now-50d---now+50d (utilisez d pour les jours, m pour les mois, y pour les années) e. . dates jusqu'à maintenant : 45##---now+0d Remarque : votre champ doit être configuré pour être un filtre de plage ou un filtre multi-valeur, sinon les valeurs ne seront pas utilisées comme prévu | `textarea` | — | — |

### Index alphabétique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'index alphabétique**<br />`show_alpha` | Afficher/Masquer l'index alphabétique | `alphaindex` | — | — |
| **Liste des Index alphabétiques personnalisés**<br />`alphacharacters` | Définir une liste alphabétique personnalisée de caractères (caractère simple / gammes / listes / alias) Utilisez une virgule(,) pour séparer les caractères, et un double point d'exclamation(!!) pour séparer les groupes de caractères. **Exemple**: [default]=a,b,c,def,g,h,k-n,opq,r-z !! 0,1,2,3,4-9 Utilisez le caractère # pour spécifier tous les nombres, le caractère moins(-) pour définir les gammes et joignez les caractères pour les agrégations. Pour la personnalisation par langue, utilisez [langue]= ex: [fr]=#,a,b,c,...,z [en]=#,a,b,c,d,...x,y,z [default]=0-9,a-c,d,e... SANS caractères de retour à la ligne | `textarea` | — | `[default]=a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z!!0,1,2,3,4,5,6,7,8,9` |
| **Classes CSS pour les groupes de caractères AI**<br />`alphagrpcssclasses` | Les classes CSS pour la zone autour des groupes de caractères Index alphabétique décrits ci-dessus p.ex. si vous avez 4 groupes, vous pouvez utiliser : letters!!numbers!!letters!!letters. NOTEZ que les lettres et les chiffres sont prédéfinis et vous devez définir toute autre classe | `textarea` | — | `letters!!numbers` |
| **Séparateur de caractère personnalisé AI**<br />`alphacharseparator` | Au lieu d'encadrés autour des caractères, ce séparateur sera utlisé. Par exemple, entrez '-' ou ','. Laissez vide pour utiliser le style par défaut. Pour utiliser des caractères spéciaux comme **¦**, merci d'utiliser leur forme HTML : **&#166;** | `text` | — | — |
| **Caractère d'alias personnalisés AI**<br />`alphaaliases` | Un seul caractère ou un seul mot représentera l'entité de caractère spécifiée (par exemple, range/liste/etc). **par ex. Spécifiez comme:** A~aAäÄ!!O~oOöÖ!!U~uUüÜ **1. Alias séparés par :** !! **2. Pour chaque alias** , la partie avant ~ est un pseudonyme, ET la partie après ~ est l'entité de caractères (range/list/etc) -- Inclure ici les alias de toutes les langues que vous utilisez. **NOTE :** NE PAS ajouter d'alias pour des lettres minuscules/majuscules (p. ex. t~tT **ce n'est pas nécessaire**, mais si vous faites un alias vous devez inclure à la fois des lettres minuscules et majuscules. | `text` | — | — |
| **Ignorer les caractères AI vides**<br />`alphaskipempty` | Ne montrent pas du tout les entités caractères Alpha Index (estompées et handicapées) inutilisées | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

#### Formulaire de recherche / filtrage

## Liste des contenus

:::note
Fichier de mise en page : **%s**
:::

#### Liste des contenus

### Affichage basique, Ordre

#### Remplacer les paramètres du **Type d'élément**

:::note
Évitez de l'activer, à moins que vous ne sachiez que vous avez besoin de **2 ou plus** façons d'afficher les mêmes éléments
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Template de contenu**<br />`ilayout` | L'élément utilise généralement la disposition définie dans son type. Vous pouvez remplacer cela pour les liens de menu vers ces élément. Notez que si vous ne créer pas de liens de menu vers ces éléments alors ils utiliseront toujours la mise en page définie dans leur type d'élément !!! | `itemlayout` | — | — |

### Affichage basique

:::note
Remarque: ces paramètres sont destinés à chaque contenu listé et sont différents des paramètres similaires qui peuvent exister pour la vue contenu
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Bouton Modifier**<br />`show_editbutton_lists` | Affiche un bouton de modification pour tous les utilisateurs qui sont connectés et qui ont les droits nécessaires pour effectuer l'édition du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Lien vers la partie publique<br />`2` = Lien vers l'administration | — |
| **Bouton Statut**<br />`show_state_icon_lists` | Activer le changement de statut rapide via AJAX | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Bouton Supprimer (permanent)**<br />`show_deletebutton_lists` | Actif l'affichage du bouton Supprimer pour tous les éléments que l'utilisateur connecté peut supprimer. REMARQUE, ce n'est pas un bouton de corbeille, cette action va supprimé définitivement l'élément. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Afficher le nombre de commentaires**<br />`show_comments_count` | Affiche pour chaque contenu le nombre de commentaires | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Afficher le titre**<br />`show_title_lists` | Montrer/Masquer le titre du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Titre cliquable**<br />`link_titles_lists` | Si oui, le titre des contenus seront cliquables et seront liés à eux-mêmes. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Forcer le texte complet**<br />`force_full` | Le texte complet (principal) est utilisé afin de présenter le contenu en affichage complet et c'est le texte après le séparateur 'Lire la suite...', vous pouvez choisir ici de l'afficher lorsque le contenu est affiché en **catégorie** et d'autres listes multi-contenus, il viendra ainsi s’ajouter au texte d'introduction | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **FLEXI_Read_More_Link**<br />`show_readmore` | Si ce paramètre est activé le lien 'lire la suite...' apparaitra s'il a été ajouté dans la description principale du contenu. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer<br />`-1` = Montrer toujours | — |

### Ordre du contenu (niveau 1)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby` | Trier les éléments par des champs/propriétés du noyau | `fcordering` | — | — |

#### Classement personnalisé des champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`orderbycustomfield` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Champ personnalisé**<br />`orderbycustomfieldid` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | `fields` | — | — |
| **Sens du tri**<br />`orderbycustomfielddir` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `fcradio` | `—` = Paramètres globaux<br />`ASC` = Croissant<br />`DESC` = Décroissant | — |
| **Méthode de tri**<br />`orderbycustomfieldint` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `fcradio` | `—` = Paramètres globaux<br />`0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date<br />`4` = Nombre de téléchargement | — |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

### Ordre du contenu (niveau 2)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby_2nd` | Trier les éléments par des champs/propriétés du noyau | `fcordering` | — | — |

#### Classement personnalisé des champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`orderbycustomfield_2nd` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Champ personnalisé**<br />`orderbycustomfieldid_2nd` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | `fields` | — | — |
| **Sens du tri**<br />`orderbycustomfielddir_2nd` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `fcradio` | `—` = Paramètres globaux<br />`ASC` = Croissant<br />`DESC` = Décroissant | — |
| **Méthode de tri**<br />`orderbycustomfieldint_2nd` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `fcradio` | `—` = Paramètres globaux<br />`0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date<br />`4` = Nombre de téléchargement | — |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

#### Overide du Frontend

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Sélecteur d'ordre (Niveau 1)**<br />`orderby_override` | Activer pour afficher une liste déroulante pour changer l'ordre dans la partie publique (Niveau 1) | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Sélecteur d'ordre (Niveau 2)**<br />`orderby_override_2nd` | Activer pour afficher une liste déroulante pour changer l'ordre dans la partie publique (Niveau 2) | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |

#### Sélectionner les options disponibles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nb par page autorisé à l'utilisateur en frontend**<br />`limit_options` | Saisissez les valeurs séparées par des virgules qui indiquent les options disponibles, laisser vide pour utiliser les options par défaut. | `text` | — | — |
| **Options de tri (Niveau 1) autorisé pour l'utilisateur frontend**<br />`orderby_options` | Sélectionner les options que vous souhaitez faire apparaitre à l'utilisateur en frontend afin qu'il puisse réordonner sa liste de contenu. **Remarque :** (a) **L'ordre par défaut**, est définit dans la section 'vue catégorie -&gt; ordre des contenus', (b)** l'ordre des contenus** ne fonctionne que pour la catégorie active et donc ne fonctionne pas si des sous catégories sont incluses dans la liste. | `fccheckbox` | — | — |
| **Ordre personnalisé (Niveau 1) autorisé pour les utilisateur en**<br />`orderby_custom` | Veuillez entrer les champs personnalisés que vous souhaitez autoriser comme options de commande. Le format est (utiliser des cas multiples séparés COMMA) : champ :[alpha\|int\|décimal\|date]:[asc\|description] ou champ :[alpha\|int\|decimal\|date]:[asc\|description]:language_string ou file_fieldid:file_hits:[asc\|description]:language_string e. . (rappelez-vous : utiliser COMMA pour les choix multiples) 45:num:description, 57:decimal:asc:LANG_PRICE_LOWEST, 61:alpha:asc, 62:file_hits:description:LANG_MOST_MOWNLOADED | `textarea` | — | — |
| **Options de tri (Niveau 2) autorisé pour l'utilisateur frontend**<br />`orderby_options_2nd` | Sélectionner les options que vous souhaitez faire apparaitre à l'utilisateur en frontend afin qu'il puisse réordonner sa liste de contenu. **Remarque :** (a) **L'ordre par défaut**, est définit dans la section 'vue catégorie -&gt; ordre des contenus', (b)** l'ordre des contenus** ne fonctionne que pour la catégorie active et donc ne fonctionne pas si des sous catégories sont incluses dans la liste. | `fccheckbox` | — | — |
| **Ordre personnalisé (Niveau 2) autorisé pour les utilisateur en**<br />`orderby_custom_2nd` | Veuillez entrer les champs personnalisés que vous souhaitez autoriser comme options de commande. Le format est (utiliser des cas multiples séparés COMMA) : champ :[alpha\|int\|décimal\|date]:[asc\|description] ou champ :[alpha\|int\|decimal\|date]:[asc\|description]:language_string ou file_fieldid:file_hits:[asc\|description]:language_string e. . (rappelez-vous : utiliser COMMA pour les choix multiples) 45:num:description, 57:decimal:asc:LANG_PRICE_LOWEST, 61:alpha:asc, 62:file_hits:description:LANG_MOST_MOWNLOADED | `textarea` | — | — |

### Sélection de contenu, pagination

### Sélection de contenu, pagination

:::note
Contenus sélectionnés
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Contenus non-autorisés**<br />`show_noauth` | Les contenus non autorisés à être visibles par un invité ou un utilisateur identifié seront inclus dans les listes de contenu (liste de catégories/favoris/tags/etc.) Lorsqu'un utilisateur essaye d'accéder à la vue détaillée d'un contenu non autorisé, les utilisateurs non connectés devront s'identifier et les utilisateurs déjà dentifiés verront une page d'erreur 404 accès interdit. **Remarque :** Si vous activez cette fonctionnalité, vous devriez aussi configurer le paramètre 'Page non autorisée' avec l'URL de la page à afficher pour ces erreurs | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Contenus propres**<br />`show_owned` | Activer pour lister les éléments détenus / rédigés par l'utilisateur actuellement connecté - quel que soit leur état, - indépendamment de la planification ou de l'expiration (date de publication / date d'expiration) | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Articles mis à la corbeille**<br />`show_trashed` | Activer pour lister les éléments mis à la corbeille aux utilisateurs privilégiés. Il s'agit des utilisateurs qui ont le privilège ACL \"Ignorer l'état des éléments\ | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Contenus de sous-catégories**<br />`display_subcategories_items` | Affiche ou non les contenus des sous catégories de la catégorie active | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = 1er niveau de sous catégories<br />`2` = Toutes les sous catégories | — |
| **Filtrer les éléments en utilisant la langue courante**<br />`filtercat` | Seulement les contenus de la langue active seront affichés dans la vue catégorie | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

#### Limiter / supprimer les éléments

:::note
Limites -avant- recherche de texte, filtrage, indexation alphabétique
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`use_limit_before_search_filt` | — | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui<br />`2` = En vedette seulement | — |
| **Nombre de contenus par page**<br />`limit_before_search_filt` | Indique le nombre de contenu à afficher sur chaque page de liste. | `text` | — | — |

:::note
Limites -après- recherche de texte, filtrage, indexation alphabétique
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Marqué par un drapeau**<br />`display_flag_featured` | Certains contenus de catégorie sont marqués en vedette / favori. Choisir d'afficher: (a) tous les contenus, (b) seulement les normaux, (c) seulement les marqués | `fcradio` | `—` = Paramètres globaux<br />`0` = Les deux<br />`1` = Standard seulement<br />`2` = En vedette seulement | — |
| **Nombre de contenus par page**<br />`limit` | Indique le nombre de contenu à afficher sur chaque page de liste. | `text` | — | — |

:::note
Limite via les champs personnalisés : veuillez définir 'Filtres verrouillés' dans l'onglet 'Recherche / Filtre formulaire'
:::

### nb. par page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Défilement infini**<br />`infinite_scroll` | Défilement infini description | `fcradio` | `—` = Paramètres globaux<br />`0` = Classique pagination<br />`1` = Bouton « Charger plus » infini<br />`2` = Défilement infini | — |
| **Afficher le nombre total de contenus**<br />`show_item_total` | Cette option affichera le nombre total de contenus de la catégorie (en fonction des paramètres d'affichage et des filtres actifs) | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **nb. par page**<br />`show_pagination` | Afficher/Masquer la pagination, tels que les liens et la page de total | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer<br />`2` = FLEXI_Auto | — |
| **Résultat de la pagination (Nombre courant et total des pages)**<br />`show_pagination_results` | (lorsque la pagination est activée), vous pouvez utiliser cette option pour désactiver l'affichage du numéro de page active courante et le nombre total de pages | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |

#### Overide du Frontend

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre de contenus par page**<br />`limit_override` | Indique le nombre de contenu à afficher sur chaque page de liste. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Libellé « par page »**<br />`limit_override_label` | Ajouter le libellé à l'intérieur ou à l'extérieur le sélecteur, ou choisir de ne pas l'afficher | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Avant<br />`2` = Intérieur | — |

### Contenus avec Post-it

:::note
Liste de contenu avec post-it catégories en vedette, niveau d'accès, créer récemment...
:::

### Post-it de catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter Post-it**<br />`mu_addcss_cats` | Ajoutez un span vide avec une classe CSS appropriée. S'il vous plaît examiner la sortie HTML pour trouver le nom de classe CSS | `fccheckbox` | — | — |
| **Ajouter du texte (titre de catégorie)**<br />`mu_addtext_cats` | Sélectionnez quand le titre de la catégorie sera ajouté à l'intérieur du marquage **NOTE :** Ceci est recommandé pour les non-développeurs et pour les sites multilingues car les titres des catégories vedettes seront filtrés par langue (chaînes de langue) | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

### Post-it niveau d'accès (pour les contenus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter Post-it**<br />`mu_addcss_acclvl` | Ajoutez un span vide avec une classe CSS appropriée. S'il vous plaît examiner la sortie HTML pour trouver le nom de classe CSS | `fccheckbox` | — | — |
| **Niveaux à obtenir**<br />`mu_add_condition_obtainded_acc` | Ajouter des marquages pour le niveau obtenu (accès) toujours ou seulement quand un élément de contenu est visible. **EXPLICATION :** Un élément de contenu a un niveau d'accès pour (a) lui-même, b) sa catégorie principale, c) son type de contenu. Un pour ces niveaux d'accès pourrait ne pas être assigné à l'utilisateur actuel, donc l'élément est invisible, vous pouvez choisir si vous voulez ajouter des marquages (balises) pour un autre niveau d'accès de l'élément déjà obtenu par l'utilisateur actuel. | `fcradio` | `—` = Paramètres globaux<br />`0` = Seulement si le contenu est visible<br />`1` = Toujours | — |
| **Ajouter texte**<br />`mu_addtext_acclvl` | Vous pouvez choisir d'ajouter du texte dans la zone de marquage. Celles-ci comprennent: aucun accès, accès (public) gratuit et noms de niveau d'accès, **NOTE :** Ceci est recommandé pour les non-développeurs et pour les sites multilingues étant donné que toutes ces langues seront filtrées (chaînes de langue) | `fccheckbox` | — | — |
| **Texte pas d'accès personnalisé**<br />`mu_no_acc_text` | Le texte par défaut est « Aucun accès ». Vous pouvez définir une chaîne de langue personnalisés ici, par exemple « Restreint », « Membres seulement » | `text` | — | — |
| **Texte accès libre personnalisé**<br />`mu_free_acc_text` | Le texte par défaut est « Libre ». Vous pouvez définir une chaîne de langue personnalisée ici, par exemple 'Public', 'Tout le monde' | `text` | — | — |

### Post-it Ajouté récemment

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter Post-it**<br />`mu_addcss_radded` | Ajoutez un span vide avec une classe CSS appropriée. S'il vous plaît examiner la sortie HTML pour trouver le nom de classe CSS | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Ajouter texte (nom de l'intervalle de temps)**<br />`mu_addtext_radded` | Ajouter le nom de la période dans la zone de marquage. **NOTE :** Ceci est recommandé pour les non-développeurs et pour les sites multilingues car ils seront filtrés dans la langue (chaînes de langue) | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

#### Configuration de l'intervalle de temps

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Intervalle de temps**<br />`mu_ra_timeframe_intervals` | Il s'agit d'une liste d'intervalles de temps entier séparée par des virgules. eg écrire 48h pour un intervalle en heure ou 2d pour spécifier l'intervalle en jours | `text` | — | — |
| **Noms des intervalles de temps**<br />`mu_ra_timeframe_names` | Ceci est un liste de chaînes de langue séparées par une virgule. Elles sont liées avec les périodes ci-dessus une par une, dans le même ordre qu'au-dessus | `textarea` | — | — |

### Post-it récemment modifiés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter Post-it**<br />`mu_addcss_rupdated` | Ajoutez un span vide avec une classe CSS appropriée. S'il vous plaît examiner la sortie HTML pour trouver le nom de classe CSS | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Ajouter texte (nom de l'intervalle de temps)**<br />`mu_addtext_rupdated` | Ajouter le nom de la période dans la zone de marquage. **NOTE :** Ceci est recommandé pour les non-développeurs et pour les sites multilingues car ils seront filtrés dans la langue (chaînes de langue) | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

#### Configuration de l'intervalle de temps

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Intervalle de temps**<br />`mu_ru_timeframe_intervals` | Il s'agit d'une liste d'intervalles de temps entier séparée par des virgules. eg écrire 48h pour un intervalle en heure ou 2d pour spécifier l'intervalle en jours | `text` | — | — |
| **Noms des intervalles de temps**<br />`mu_ru_timeframe_names` | Ceci est un liste de chaînes de langue séparées par une virgule. Elles sont liées avec les périodes ci-dessus une par une, dans le même ordre qu'au-dessus | `textarea` | — | — |

### Options générales

:::note
Remarque : Celles-ci sont utilisées dans **la vue des catégories **, mais si vous définissez les mêmes paramètres dans la **configuration du type** (de l'élément) sur l'option 'Utiliser global', -- alors ceux-ci seront également utilisés dans **la vue contenu**
:::

#### Référencement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Créer le fil de navigation automatiquement**<br />`automatic_pathways` | Le chemin de catégories et de contenus (affiché dans le module de fil de navigation) sera généré automatiquement (a) en supprimant toutes les entrées du menu du fil de navigation et en ajoutant l'arborescence de catégories puis le titre de l'article. NOTE : vous pouvez surcharger ces paramètres pour chaque catégorie, type et contenu. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Tag canonique**<br />`add_canonical` | Ajouter une balise meta canonique dans le code source de vos pages, cela aide les moteurs de recherche à identifier une page visualisée via des URL différentes et lui donner meilleur rang, en ne l'indexant pas plusieurs fois | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Type microdata pour les contenus**<br />`microdata_itemtype_cat` | Ceci sera utilisé pour les éléments qui n'ont pas de type microdonnées configuré dans leur type ou dans leurs paramètres d'élément atomique. MICRODATA permettent aux moteurs de recherche de catégoriser votre contenu de manière appropriée, améliorant le référencement de vos pages | `microdatatype` | — | — |

#### Commentaires

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer l'intégration des commentaires**<br />`comments` | Autorise l'intégration d'un système de commentaires. **REMARQUE:** Ce paramètre peut être surchargé dans les types, les catégories, les éléments uniques ou les éléments de menu. **REMARQUE:** Si vous désactivez cette option, vous pourrez activer manuellement (le champ de description activera tout par défaut) le plug-in de contenu Joomla approprié de votre système de commentaires pour insérer des commentaires via un événement de contenu Joomla. Si vous ajoutez des commentaires de cette manière, vous ne pourrez pas utiliser le paramètre \"Désactiver les commentaires\" dans le formulaire, mais vous devrez le faire comme le recommande votre système de commentaires, par exemple. en insérant un texte spécial dans la description | `fcradio` | `—` = Paramètres globaux<br />`0` = Désactiver ou intégrer manuellement<br />`1` = JComments | — |

#### Liste des contenus

## Flux RSS

### Flux RSS

:::note
Activer les Flux RSS dans l'onglet '%s'
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre de contenus par page**<br />`feed_limit` | Indique le nombre de contenu à afficher sur chaque page de liste. | `text` | — | — |
| **Pour chaque contenu, afficher :**<br />`feed_summary` | Sélectionner si vous préférez inclure dans votre flux RSS uniquement le texte d'introduction ou bien le texte complet. | `fcradio` | `—` = Paramètres globaux<br />`0` = Texte d'introduction<br />`1` = Texte complet | — |
| **Longueur maximum du texte**<br />`feed_summary_cut` | Si le texte dépasse le nombre de caractère indiqué, il sera automatiquement tronqué. | `text` | — | — |
| **FLEXI_Read_More_Link**<br />`feed_show_readmore` | Si ce paramètre est activé le lien 'lire la suite...' apparaitra s'il a été ajouté dans la description principale du contenu. | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |

### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser l'image**<br />`feed_use_image` | Extraire la première image du texte principale | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Lien sur l'image**<br />`feed_link_image` | Actif un lien sur l'image affichée. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Source de l'image**<br />`feed_image_source` | Sélectionner la source de l'image. Vous pouvez aussi choisir un champ image (s'il y en a au moins un de disponible) ou automatiquement extraire l'image de la description. | `fcimage` | — | — |
| **Taille de l'image**<br />`feed_image_size` | Image size description | `fcradio` | `—` = Utiliser les paramètres<br />`s` = Petite<br />`m` = Moyenne<br />`l` = Grande | — |
| **Largeur de l'image**<br />`feed_image_width` | Largeur de l'image | `text` | — | — |
| **Hauteur de l'image**<br />`feed_image_height` | Hauteur de l'image | `text` | — | — |
| **Méthode de traitement**<br />`feed_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | `fcradio` | `—` = Paramètres globaux<br />`0` = A l'échelle<br />`1` = Découper | — |

### Champs personnalisés

:::note
Ne pas ajouter les champs qui pourraient cassés l'affichage du flux rss
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Liste des champs**<br />`feed_extra_fields` | Les champs qui nécessitent du CSS/JS supplémentaire ne fonctionneront pas correctement, les champs appropriés sont des champs comme la date, le texte, la sélection, etc. Entrez une liste séparée par des virgules des noms de champs | `textarea` | — | — |

### Ordre du contenu (niveau 1)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`feed_orderby` | Trier les éléments par des champs/propriétés du noyau | `fcordering` | — | — |

#### Classement personnalisé des champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`feed_orderbycustomfield` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Champ personnalisé**<br />`feed_orderbycustomfieldid` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | `fields` | — | — |
| **Sens du tri**<br />`feed_orderbycustomfielddir` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `fcradio` | `—` = Paramètres globaux<br />`ASC` = Croissant<br />`DESC` = Décroissant | — |
| **Méthode de tri**<br />`feed_orderbycustomfieldint` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `fcradio` | `—` = Paramètres globaux<br />`0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date<br />`4` = Nombre de téléchargement | — |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

### Ordre du contenu (niveau 2)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`feed_orderby_2nd` | Trier les éléments par des champs/propriétés du noyau | `fcordering` | — | — |

#### Classement personnalisé des champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`feed_orderbycustomfield_2nd` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Champ personnalisé**<br />`feed_orderbycustomfieldid_2nd` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | `fields` | — | — |
| **Sens du tri**<br />`feed_orderbycustomfielddir_2nd` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `fcradio` | `—` = Paramètres globaux<br />`ASC` = Croissant<br />`DESC` = Décroissant | — |
| **Méthode de tri**<br />`feed_orderbycustomfieldint_2nd` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `fcradio` | `—` = Paramètres globaux<br />`0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date<br />`4` = Nombre de téléchargement | — |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

## Notifications par Email

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer les notifications**<br />`enable_notifications` | Cette option permet d'activer l'envoi de notification automatique par email suite à la soumission ou la modification d'un contenu. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Debug des notifications**<br />`nf_enable_debug` | -- Activer ceci pour: (a) afficher les informations de débogage et aussi (b) **forcer l'envoi de notifications par e-mail sur chaque opération de sauvegarde**, -- Normalement, les notifications seront envoyées SEULEMENT (a) une fois par session pour chaque élément de contenu ou (b)**lorsque ses catégories sont modifiées**. | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

### Création d’e-mail

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Envoyer les emails en copie cachée**<br />`nf_send_as_bcc` | Activez cette option pour empêcher les destinataires de recevoir des e-mails et de voir d'autres destinataires. **NOTE**: cela obligera l'administrateur du site à être le principal destinataire de l'e-mail de notification | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

## Notifications par Email

### Email destinataires

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Choisir**<br />`cats_enable_notifications` | Sélectionner afin d'activer l'envoi d'emails de notification lors d'ajout ou de modifications de contenus assignés à cette catégorie | `fcradio` | `—` = Paramètres globaux<br />`0` = Composant configuré<br />`1` = Configuration du composant et celle en dessous<br />`2` = Ci-dessous | — |

#### Nouveau Contenu : Peu importe le statut (à partir des auteurs qui peuvent publier)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Groupes d'utilisateurs**<br />`cats_usergrps_notify_new` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | `flexiusergroup` | — | — |
| **Id Utilisateur/liste de noms**<br />`cats_userlist_notify_new` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | `text` | — | — |
| **Texte de catégorie**<br />`cats_text_notify_new` | Description du texte de catégorie | `textarea` | — | — |

#### Nouveau Contenu: En attente de publication (pour les auteurs qui n'ont pas le droit de publication)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Groupes d'utilisateurs**<br />`cats_usergrps_notify_new_pending` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | `flexiusergroup` | — | — |
| **Id Utilisateur/liste de noms**<br />`cats_userlist_notify_new_pending` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | `text` | — | — |
| **Texte de catégorie**<br />`cats_text_notify_new_pending` | Description du texte de catégorie | `textarea` | — | — |

#### Mise à jour d'un contenu: PAS BESOIN D'APPROBATION DE LA VERSION (pour les auteurs qui peuvent publier )

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Groupes d'utilisateurs**<br />`cats_usergrps_notify_existing` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | `flexiusergroup` | — | — |
| **Id Utilisateur/liste de noms**<br />`cats_userlist_notify_existing` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | `text` | — | — |
| **Texte de catégorie**<br />`cats_text_notify_existing` | Description du texte de catégorie | `textarea` | — | — |

#### Mise à jour d'un contenu: BESOIN DE L'APPROBATION DE LA VERSION (pour les auteurs qui ne peuvent pas publier, la gestion des versions doit être activé)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Groupes d'utilisateurs**<br />`cats_usergrps_notify_existing_reviewal` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | `flexiusergroup` | — | — |
| **Id Utilisateur/liste de noms**<br />`cats_userlist_notify_existing_reviewal` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | `text` | — | — |
| **Texte de catégorie**<br />`cats_text_notify_existing_reviewal` | Description du texte de catégorie | `textarea` | — | — |

## Options des métadonnées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Libellé du titre alternatif de la page**<br />`page_title` | Description du titre alternatif de la page | `text` | — | — |
| **Auteur Joomla**<br />`author` | Metadata author description | `text` | — | — |
| **Robots des moteurs de recherche**<br />`robots` | Indiquer si les robots des moteurs de recherche vont ajouter ce contenu dans leur base de données et s'ils doivent suivre (respectivement indexer) les liens qui y figurent | `fcradio` | `—` = Paramètres globaux<br />`index, follow` = index, follow<br />`noindex, follow` = noindex, follow<br />`index, nofollow` = index, nofollow<br />`noindex, nofollow` = noindex, nofollow | — |
