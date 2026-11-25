---
sidebar_position: 6
---

# Vues de catégorie

Paramètres d’affichage des vues de liste de catégories et multi-catégories : filtres, tri, liens, pagination, etc.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

### Vue Catégorie

#### Catégorie, Contenu de l'auteur, Mes Contenus, Vue multi-catégorie, Mots clés, Favoris

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Tout lister (via ACL)**<br />`use_list_items_in_any_state_acl` | Activez cette option pour autoriser les utilisateurs privilégiés (autorisation ACL : « lister les contenus dans n’importe quel état ») et les super administrateurs à voir les contenus dans n’importe quel état, y compris programmés et/ou expirés. | — | `0` |
| **Héritage des paramètres**<br />`inheritcid` | Hériter les paramètres d'une catégorie spécifique **NOTE :** Définissez vos paramètres à 'Utiliser global' ou à vide afin que le patrimoine puisse fonctionner **Remarque :** Le patrimoine de la catégorie spécifique est un niveau unique, donc il ne cascade pas d'hériter d'autres catégories **NOTE :** Héritage des catégories parentes est multiniveau, donc il cascade d'hériter jusqu'à la catégorie parente qui n'hérite pas de son parent | — | `-1` |
| **Déboguer l'héritage des paramètres**<br />`debug_inheritcid` | Afficher des informations dans les vues des catégories de la partie publique à propos de l'ordre surchargé des paramètres | — | `0` |

#### FLEXI_LISTS

## Image de la catégorie

:::note
Ce sont des valeurs par défaut si la catégorie ou l'élément du menu ne les définit pas
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Image**<br />`image` | Sélectionner l'image pour la catégorie | — | — |
| **Texte alternatif**<br />`image_alt` | — | — | — |

## Liste : Entête

#### Liste : Entête

## Boutons

:::note
Remarque: vous pouvez configurer plus d'option dans l'onglet '%s'
:::

#### Ajouter un nouvel article

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Bouton**<br />`show_addbutton` | Permet l’affichage du bouton **Ajouter un nouvel contenu** aux catégories et** listes**, là où l’utilisateur connecté peut en ajouter | — | `1` |
| **Afficher les contenus non-autorisés**<br />`nonauth_addbutton` | Afficher le bouton 'soumettre' aux utilisateurs non-autorisés. **Si actif, attention**: sauf si le lien de menu permet la soumission d'éléments par les utilisateurs non autorisés -&gt; a. les invités sont redirigés vers la page de connexion / b. les utilisateurs connectés mais non autorisés sont redirigés sur l'URL indiquée - dans la configuration du composant - surclassé par l'uRL dans la configuration du type de contenu - surclassé par l'uRL dans le lien de menu de soumission | — | `0` |
| **Menu de soumission de contenu**<br />`addbutton_menu_itemid` | Vous pouvez forcer un un réglage spécifique d'un élément de menu , de sorte que la configuration personnalisée est utilisée , par exemple, limiter le type de contenu spécifique (s ) . ** NOTE 1 ** : Au cas où vous souhaitez autoriser type de contenu spécifique pour des catégories spécifiques , vous devriez refuser « créer des contenus de privilège ACL aux utilisateurs , ils seront ainsi en mesure de présenter uniquement par le type de contenu OVERRIDE par le produit soumettre menu. ** NOTE 2 ** : Vous pouvez également remplacer la catégorie ACL trop | — | — |

## Information de la catégorie

:::note
Fichier de mise en page : **%s**
:::

### Information de la catégorie

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Titre de la catégorie**<br />`show_cat_title` | Afficher/Masquer le titre de la catégorie. | — | `1` |
| **Taille max. du titre des contenus**<br />`title_cut_text` | Définit le nombre maximum de caractère qui peut être affiché dans le titre d'un contenu appartenant à la catégorie, les titres qui dépassent cette valeur seront automatiquement tronqués et '...' seront ajoutés à la suite du titre | — | `200` |

#### Image

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Image de la catégorie**<br />`show_description_image` | Afficher/Masquer l'image de la catégorie. | — | `0` |
| **Source de l'image de la catégorie**<br />`cat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | — | `2` |
| **Lien sur l'image**<br />`cat_link_image` | Actif un lien sur l'image affichée. | — | `1` |
| **Méthode de traitement**<br />`cat_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | — | `1` |
| **Largeur de l'image**<br />`cat_image_width` | Largeur de l'image | — | `80` |
| **Hauteur de l'image**<br />`cat_image_height` | Hauteur de l'image | — | `80` |

#### Description

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Description de la catégorie**<br />`show_description` | Afficher/Masquer la description de la catégorie | — | `1` |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content_cat` | Activer cette option si vous souhaitez exécuter les plugins de contenu (onPrepareContent) sur la description de la catégorie. Gardez à l'esprit que tous les plugins ne fonctionne pas forcément en dehors du com_content. | — | `1` |

## Liste des sous-catégories

:::note
Fichier de mise en page : **%s**
:::

### Sous-catégories (1er sous-niveau)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Sous-catégories**<br />`show_subcategories` | Afficher/Cacher les sous-catégories | — | `0` |
| **Ordre de la liste de catégorie**<br />`subcat_orderby` | Ordre la liste des catégories, les options disponibles dépendent des propriétés de l'ensemble des catégories. | — | `order` |

#### Information catégories

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Compteur de contenu**<br />`show_itemcount` | Afficher/cacher le nombre de contenu de chaque sous-catégorie | — | `1` |
| **Nombre de sous-catégories**<br />`show_subcatcount` | Afficher / masquer le nombre de sous-catégories de chaque sous-catégorie | — | `0` |
| **Catégories vides (nombre d'éléments requis activé)**<br />`show_empty_cats` | Afficher / masquer les catégories sans articles. REMARQUE: cela fonctionne lorsque le comptage d'éléments est activé | — | `1` |

#### Image

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Image de la catégorie**<br />`show_description_image_subcat` | Afficher/Masquer l'image de la catégorie. | — | `0` |
| **Source de l'image de la catégorie**<br />`subcat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | — | `2` |
| **Lien sur l'image**<br />`subcat_link_image` | Actif un lien sur l'image affichée. | — | `1` |
| **Méthode de traitement**<br />`subcat_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | — | `1` |
| **Largeur de l'image**<br />`subcat_image_width` | Largeur de l'image | — | `24` |
| **Hauteur de l'image**<br />`subcat_image_height` | Hauteur de l'image | — | `24` |

#### Description

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Description de la catégorie**<br />`show_description_subcat` | Afficher/Masquer la description de la catégorie | — | `0` |
| **Longueur maximum de la description de la catégorie**<br />`description_cut_text_subcat` | Définit le nombre maximum de caractères affichés dans la description d'une catégorie, les descriptions qui dépassent cette valeur seront automatiquement tronquées et '...' seront ajoutés à la suite de la description | — | `120` |

#### Liste des Catégories

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Liste des étiquettes**<br />`show_label_subcats` | Afficher un libellé 'Sous Catégories' devant chaque liste de sous catégories. | — | `1` |
| **Pré-configuration**<br />`prx_sfx_open_close_configs_subcat` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | — | — |
| **Préfixe sous-catégorie**<br />`subcat_pretext` | Ce texte est placé b&gt;devant** chaque titre de sous catégories. | — | — |
| **Suffixe sous-catégorie**<br />`subcat_posttext` | Ce texte est placé b&gt;après** chaque titre de sous catégories. | — | — |
| **Séparateur sous catégorie**<br />`subcat_separatorf` | Choisir le caractère qui séparera la liste des titres de sous catégories. | — | `0` |
| **Texte d'ouverture**<br />`subcat_opentag` | Texte ou code HTML ajouté au début d'une liste de valeur. | — | — |
| **Texte de fermeture**<br />`subcat_closetag` | Texte ou code HTML ajouté au fin d'une liste de valeur. | — | — |

## Liste des catégories connexes

:::note
Fichier de mise en page : **%s**
:::

### Catégories connexes (même niveau)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Catégories connexes**<br />`show_peercategories` | Afficher/Cacher les catégories connexes | — | `1` |
| **Ordre de la liste de catégorie**<br />`peercat_orderby` | Ordre la liste des catégories, les options disponibles dépendent des propriétés de l'ensemble des catégories. | — | `order` |

#### Information catégories

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Compteur de contenu**<br />`show_itemcount_peercat` | Afficher/cacher le nombre de contenu de chaque sous-catégorie | — | `0` |
| **Nombre de catégories connexes**<br />`show_subcatcount_peercat` | Afficher/Cacher le nombre de sous-catégories de chaque catégorie connexe | — | `0` |
| **Catégories vides (nombre d'éléments requis activé)**<br />`show_empty_peercats` | Afficher / masquer les catégories sans articles. REMARQUE: cela fonctionne lorsque le comptage d'éléments est activé | — | `1` |

#### Image

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Image de la catégorie**<br />`show_description_image_peercat` | Afficher/Masquer l'image de la catégorie. | — | `0` |
| **Source de l'image de la catégorie**<br />`peercat_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | — | `2` |
| **Lien sur l'image**<br />`peercat_link_image` | Actif un lien sur l'image affichée. | — | `1` |
| **Méthode de traitement**<br />`peercat_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | — | `1` |
| **Largeur de l'image**<br />`peercat_image_width` | Largeur de l'image | — | `24` |
| **Hauteur de l'image**<br />`peercat_image_height` | Hauteur de l'image | — | `24` |

#### Description

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Description de la catégorie**<br />`show_description_peercat` | Afficher/Masquer la description de la catégorie | — | `0` |
| **Longueur maximum de la description de la catégorie**<br />`description_cut_text_peercat` | Définit le nombre maximum de caractères affichés dans la description d'une catégorie, les descriptions qui dépassent cette valeur seront automatiquement tronquées et '...' seront ajoutés à la suite de la description | — | `120` |

#### Liste des Catégories

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Liste des étiquettes**<br />`show_label_peercats` | Afficher un libellé avant la liste des catégories connexes **Remarque :** Si à la fois les images et descriptions de la sous-catégorie sont désactivées, alors le libellé et les enregistrements de la liste seront placés à l'intérieur des conteneurs 'inline' | — | `1` |
| **Pré-configuration**<br />`prx_sfx_open_close_configs_peercat` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | — | — |
| **Préfixe sous-catégorie**<br />`peercat_pretext` | Ce texte est placé b&gt;devant** chaque titre de sous catégories. | — | — |
| **Suffixe sous-catégorie**<br />`peercat_posttext` | Ce texte est placé b&gt;après** chaque titre de sous catégories. | — | — |
| **Séparateur sous catégorie**<br />`peercat_separatorf` | Choisir le caractère qui séparera la liste des titres de sous catégories. | — | `0` |
| **Texte d'ouverture**<br />`peercat_opentag` | Texte ou code HTML ajouté au début d'une liste de valeur. | — | — |
| **Texte de fermeture**<br />`peercat_closetag` | Texte ou code HTML ajouté au fin d'une liste de valeur. | — | — |

#### Liste : Entête

## Formulaire de recherche / filtrage

#### Formulaire de recherche / filtrage

## Basique

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Placement des champs formulaires**<br />`ff_placement` | Sélectionner où le formulaire sera placé | — | `0` |
| **Titre du slider**<br />`ff_toggle_search_title` | Le texte de lien/bouton d'ouverture/affichage du formulaire de recherche par défaut est 'Recherche' | — | `FLEXI_TOGGLE_SEARCH_FORM` (Rechercher) |
| **Validation automatique**<br />`filter_autosubmit` | Envoyer un formulaire automatiquement lors d'un changement de filtre. Si vous n'activez pas cela, alors les utilisateurs seront en mesure de mettre de nombreux filtres avant de soumettre le formulaire. **NOTE : ** Certains filtre peuvent auto-envoyer le formulaire en dépit de ce paramètre | — | `1` |
| **Utiliser la recherche Ajax**<br />`filter_ajax` | Réglage Oui pour utiliser la recherche et le filtrage sans rechargement de page. Compatible uniquement avec les nouveaux modèles. | — | `0` |
| **Badge de filtre**<br />`badge_position` | Afficher la valeur du filtre sous forme de badge : aucun n’affiche rien, haut l’affiche avant le formulaire de recherche, bas après le bouton d’envoi | — | `2` |
| **Instructions**<br />`filter_instructions` | Afficher les instructions d'utilisation du formulaire de filtrage. Vous pouvez créer des substitutions de langue joomla pour les chaînes de langue pour donner des instructions personnalisées à vos utilisateurs | — | `1` |

#### Boutons

:::note
Bouton rechercher
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Bouton rechercher**<br />`show_search_go` | Envoyer le formulaire pour recharger la liste actuelle, ** Remarque **: tous les critères suivant seront pris en compte, la recherche de texte, les filtres dans les champs et l'indice alpha (lorsque ces valeurs sont présentes) | — | `0` |
| **Class du bouton rechercher**<br />`flexi_button_class_go` | Classe pour le bouton de réinitialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | — | `btn btn-success` |
| **Classe personnalisée**<br />`flexi_button_class_go_custom` | Ajouter une classe personnalisée pour le bouton go, exemple uk-button uk-button-large pour un template Warp7 | — | — |

:::note
Bouton annuler
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Bouton annuler**<br />`show_search_reset` | Effacer le formulaire pour recharger la liste actuelle, ** Remarque **: Notez que cela va aussi supprimer les valeurs saisies dans les filtres et de l'indice alpha (lorsque ces produits sont présents) | — | `1` |
| **Classe du bouton annuler**<br />`flexi_button_class_reset` | Classe pour le bouton de réinitialisation, utilisez la valeur dans la liste déroulante ou insérer votre classe personnalisée | — | `btn` |
| **Classe personnalisée**<br />`flexi_button_class_reset_custom` | Ajouter une classe personnalisée pour le bouton de réinitialisation, exemple uk-button uk-button-large pour un template Warp7 | — | — |

#### Chercher / Filtrer

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Préfixe sous-catégorie**<br />`filter_pretext` | Ce texte est placé b&gt;devant** chaque titre de sous catégories. | — | — |
| **Suffixe sous-catégorie**<br />`filter_posttext` | Ce texte est placé b&gt;après** chaque titre de sous catégories. | — | — |
| **Texte d'ouverture**<br />`filter_opentag` | Texte ou code HTML ajouté au début d'une liste de valeur. | — | — |
| **Texte de fermeture**<br />`filter_closetag` | Texte ou code HTML ajouté au fin d'une liste de valeur. | — | — |
| **1 enregistrement par ligne**<br />`filter_placement` | Sélectionnez la façon dont les résultats seront affichés: - Afficher un seul enregistrement par ligne, ou - Utilisez un séparateur personnalisé | — | `0` |
| **Séparateur de résultat ignoré si les enregistrements sont affichés par ligne**<br />`filter_separatorf` | Choisissez un séparateur pour séparer les enregistrements (placé entre les valeurs). ** Remarque : ** Ce paramètre est ignoré lorsque vous placez les enregistrements par ligne | — | `0` |

## Texte à Rechercher

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser la recherche**<br />`use_search` | Afficher la zone de recherche textuel | — | `1` |
| **Afficher les étiquettes**<br />`show_search_label` | Vous pouvez cacher ou afficher le libellé à l'intérieur de la zone de recherche de texte pour économiser de l'espace | — | `1` |
| **Utiliser la subggestion automatique**<br />`search_autocomplete` | Sélectionnez cette option pour utiliser une auto-complétion multi-mots ou une méthode de saisie automatique plus simple ou désactiver la complétion automatique | — | `1` |
| **Combinaison de mots**<br />`show_searchphrase` | Permettre aux utilisateurs de sélectionner la méthode de combiner les mots à rechercher, par exemple, phrase, expression (davantage de résultats), tous les mots, n’importe quel mot, expression exacte | — | `0` |
| **Combinaison par défaut**<br />`default_searchphrase` | Méthode par défaut (présélectionné) pour combiner les termes de recherche | — | `all` |

## Champs filtre

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Afficher les filtres**<br />`use_filters` | Permettra d'afficher les filtres de champs. Notez que vous pouvez définir l'apparence et le comportement du filtre en modifiant la configuration de chaque champ individuellement | — | `0` |
| **Afficher chaque filtre dans un accordéon**<br />`fc_filter_in_slide` | Afficher la valeur de chaque champ dans son accordéon | — | `0` |
| **Ordre de filtrage**<br />`filters_order` | Sélectionner l'ordre d'affichage des champs | — | `1` |
| **Choisissez les filtres**<br />`filters` | Choisissez les filtres que vous souhaitez charger pour cette catégorie | — | — |
| **Etiquette des filtres**<br />`show_filter_labels` | Forcer l'affichage ou non de l'ensemble des libellés pour chaque champ de filtre, ce paramètre outrepassera automatiquement les paramètre de chaque champs. | — | `1` |
| **Valeurs initiales de filtres**<br />`initial_filters` | Ce sont les valeurs initiales des filtres, l'utilisateur peut les remplacer. Exemple : field_id##value %% field_id##value Exemple : 22##14 %% 47##some field value %% 19##someword - **Valeurs uniques**: field_id##value1 - **Ranges**: field_id##value1---value2 - **Valeurs multiples**: field_id##value1+++++++valeur3 - **Relation / Relation / Reverse-relation**: REL_field_id##RELEM_id~value1 - **Plages de décalage de dates**: field_id##now-50d---now+50d (utilisez d pour les jours, m pour les mois, y pour les années) e. . dates jusqu'à maintenant : 45##---now+0d Remarque : votre champ doit être configuré pour être un filtre de plage ou un filtre multi-valeur, sinon les valeurs ne seront pas utilisées comme prévu | — | — |

#### Filtres bloqués

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser un filtrage bloqué**<br />`use_persistent_filters` | Filtres qui ne peuvent PAS être remplacés par l'utilisateur, **NOTE :** Celles-ci peuvent être cachées ou vous pouvez choisir de les afficher (la saisie de l'utilisateur sera interdite) | — | `0` |
| **Valeur des filtres bloqués**<br />`persistent_filters` | Filtres qui ne peuvent PAS être remplacés par un utilisateur. Exemple : field_id##value %% field_id##value Exemple : 22##14 %% 47##some field value %% 19##someword - **Valeurs uniques**: field_id##value1 - **Ranges**: field_id##value1---value2 - **Valeurs multiples**: field_id##value1+++++++valeur3 - **Relation / Relation / Reverse-relation**: REL_field_id##RELEM_id~value1 - **Plages de décalage de dates**: field_id##now-50d---now+50d (utilisez d pour les jours, m pour les mois, y pour les années) e. . dates jusqu'à maintenant : 45##---now+0d Remarque : votre champ doit être configuré pour être un filtre de plage ou un filtre multi-valeur, sinon les valeurs ne seront pas utilisées comme prévu | — | — |

## Index alphabétique

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Afficher l'index alphabétique**<br />`show_alpha` | Afficher/Masquer l'index alphabétique | — | `1` |
| **Liste des Index alphabétiques personnalisés**<br />`alphacharacters` | Définir une liste alphabétique personnalisée de caractères (caractère simple / gammes / listes / alias) Utilisez une virgule(,) pour séparer les caractères, et un double point d'exclamation(!!) pour séparer les groupes de caractères. **Exemple**: [default]=a,b,c,def,g,h,k-n,opq,r-z !! 0,1,2,3,4-9 Utilisez le caractère # pour spécifier tous les nombres, le caractère moins(-) pour définir les gammes et joignez les caractères pour les agrégations. Pour la personnalisation par langue, utilisez [langue]= ex: [fr]=#,a,b,c,...,z [en]=#,a,b,c,d,...x,y,z [default]=0-9,a-c,d,e... SANS caractères de retour à la ligne | — | `[default]=a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z!!0,1,2,3,4,5,6,7,8,9` |
| **Classes CSS pour les groupes de caractères AI**<br />`alphagrpcssclasses` | Les classes CSS pour la zone autour des groupes de caractères Index alphabétique décrits ci-dessus p.ex. si vous avez 4 groupes, vous pouvez utiliser : letters!!numbers!!letters!!letters. NOTEZ que les lettres et les chiffres sont prédéfinis et vous devez définir toute autre classe | — | `letters!!numbers` |
| **Séparateur de caractère personnalisé AI**<br />`alphacharseparator` | Au lieu d'encadrés autour des caractères, ce séparateur sera utlisé. Par exemple, entrez '-' ou ','. Laissez vide pour utiliser le style par défaut. Pour utiliser des caractères spéciaux comme **¦**, merci d'utiliser leur forme HTML : **&#166;** | — | — |
| **Caractère d'alias personnalisés AI**<br />`alphaaliases` | Un seul caractère ou un seul mot représentera l'entité de caractère spécifiée (par exemple, range/liste/etc). **par ex. Spécifiez comme:** A~aAäÄ!!O~oOöÖ!!U~uUüÜ **1. Alias séparés par :** !! **2. Pour chaque alias** , la partie avant ~ est un pseudonyme, ET la partie après ~ est l'entité de caractères (range/list/etc) -- Inclure ici les alias de toutes les langues que vous utilisez. **NOTE :** NE PAS ajouter d'alias pour des lettres minuscules/majuscules (p. ex. t~tT **ce n'est pas nécessaire**, mais si vous faites un alias vous devez inclure à la fois des lettres minuscules et majuscules. | — | — |
| **Ignorer les caractères AI vides**<br />`alphaskipempty` | Ne montrent pas du tout les entités caractères Alpha Index (estompées et handicapées) inutilisées | — | `0` |

#### Formulaire de recherche / filtrage

## Mise en page

### Mise en Page

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Mise en page de catégorie par défaut**<br />`clayout` | La mise en page de catégorie choisie du modèle sélectionné sera utilisée, sauf si la vue catégorie / liste de contenu / URL le remplace | — | `grid` |
| **Modèle mobile**<br />`clayout_mobile` | Définit si un modèle mobile doit être utilisé quand le visiteur utilise un support mobile pour afficher le site, le modèle « normal » sera utilisé par défaut. Cette option permet de résoudre des problèmes de résolution | — | — |
| **Dossiers LESS à inclure**<br />`less_folders` | Dossiers à surveiller pour les modifications. - Si des fichiers sont modifiés, la recompilation LESS sera déclenchée. REMARQUE : Vous pouvez utiliser des remplacements tels que : JPATH_* ACTIVE_JTEMPLATE_SITE LANG_TAG et LANG_SHORT_TAG | — | `JPATH_COMPONENT_SITE/assets/less/ ::
JTEMPLATE_SITE/less/com_flexicontent/ ::
` |

### Sélecteur de template

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Affichage**<br />`clayout_switcher` | Activer pour permettre à l'utilisateur du frontend de changer la disposition de la liste des éléments (catégorie). NOTE : la sélection de zéro modèles autorisés, désactivera le commutateur | — | `1` |
| **Apparence**<br />`clayout_switcher_display_mode` | Sélectionner comment le sélecteur d'affichage doit être affiché | — | `1` |
| **Etiquette**<br />`clayout_switcher_label` | — | — | `0` |
| **Templates de contenu autorisé -- aucun autorise tout --**<br />`displayed_clayouts` | Sélectionner les templates autorisés pour ce type **Remarque :** C'est utilie si vous souhaitez autoriser la sélection des templates pour les utilisateurs frontend ayant des droits de saisie de contenu, surtout pour réduire la sélection dans la liste des templates. | — | — |

#### URL / liens

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Templates de contenu autorisés -- Aucun autorise tout --**<br />`allowed_clayouts` | Sélectionner les templates autorisés pour ce type **Remarque :** C'est utilie si vous souhaitez autoriser la sélection des templates pour les utilisateurs frontend ayant des droits de saisie de contenu, surtout pour réduire la sélection dans la liste des templates. | — | — |

## Liste des contenus

:::note
Fichier de mise en page : **%s**
:::

#### Liste des contenus

## Affichage basique, Ordre

### Affichage basique

:::note
Remarque: ces paramètres sont destinés à chaque contenu listé et sont différents des paramètres similaires qui peuvent exister pour la vue contenu
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Bouton Modifier**<br />`show_editbutton_lists` | Affiche un bouton de modification pour tous les utilisateurs qui sont connectés et qui ont les droits nécessaires pour effectuer l'édition du contenu | — | `1` |
| **Bouton Statut**<br />`show_state_icon_lists` | Activer le changement de statut rapide via AJAX | — | `1` |
| **Bouton Supprimer (permanent)**<br />`show_deletebutton_lists` | Actif l'affichage du bouton Supprimer pour tous les éléments que l'utilisateur connecté peut supprimer. REMARQUE, ce n'est pas un bouton de corbeille, cette action va supprimé définitivement l'élément. | — | `0` |
| **Afficher le nombre de commentaires**<br />`show_comments_count` | Affiche pour chaque contenu le nombre de commentaires | — | `1` |
| **Afficher le titre**<br />`show_title_lists` | Montrer/Masquer le titre du contenu | — | `1` |
| **Titre cliquable**<br />`link_titles_lists` | Si oui, le titre des contenus seront cliquables et seront liés à eux-mêmes. | — | `1` |
| **Forcer le texte complet**<br />`force_full` | Le texte complet (principal) est utilisé afin de présenter le contenu en affichage complet et c'est le texte après le séparateur 'Lire la suite...', vous pouvez choisir ici de l'afficher lorsque le contenu est affiché en **catégorie** et d'autres listes multi-contenus, il viendra ainsi s’ajouter au texte d'introduction | — | `0` |
| **FLEXI_Read_More_Link**<br />`show_readmore` | Si ce paramètre est activé le lien 'lire la suite...' apparaitra s'il a été ajouté dans la description principale du contenu. | — | `-1` |

### Ordre des contenus

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Les champs ne pouvant pas être ordonnés**<br />`non_orderable_types` | Certains champs ne peuvent être triés ou sont sans intérêt pour le tri, ex: barre d'outils, merci d'indiquer les noms des types ici, séparés par des virgules. Les champs ajoutés ici n'apparaitront pas dans les sélecteurs de tri des champs personnalisés | — | `account_via_submit,authoritems,toolbar,image,groupmarker,fcpagenav,minigallery,weblink,email,fcloadmodule` |

#### Ordre du contenu (niveau 1)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby` | Trier les éléments par des champs/propriétés du noyau | — | `rdate` |

#### Classement personnalisé des champs

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`orderbycustomfield` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | — | `1` |
| **Champ personnalisé**<br />`orderbycustomfieldid` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | — | `0` |
| **Sens du tri**<br />`orderbycustomfielddir` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | — | `ASC` |
| **Méthode de tri**<br />`orderbycustomfieldint` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | — | `0` |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

#### Ordre du contenu (niveau 2)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`orderby_2nd` | Trier les éléments par des champs/propriétés du noyau | — | `alpha` |

#### Classement personnalisé des champs

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`orderbycustomfield_2nd` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | — | `1` |
| **Champ personnalisé**<br />`orderbycustomfieldid_2nd` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | — | `0` |
| **Sens du tri**<br />`orderbycustomfielddir_2nd` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | — | `ASC` |
| **Méthode de tri**<br />`orderbycustomfieldint_2nd` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | — | `0` |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

#### Overide du Frontend

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Sélecteur d'ordre (Niveau 1)**<br />`orderby_override` | Activer pour afficher une liste déroulante pour changer l'ordre dans la partie publique (Niveau 1) | — | `1` |
| **Sélecteur d'ordre (Niveau 2)**<br />`orderby_override_2nd` | Activer pour afficher une liste déroulante pour changer l'ordre dans la partie publique (Niveau 2) | — | `0` |

#### Sélectionner les options disponibles

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Nb par page autorisé à l'utilisateur en frontend**<br />`limit_options` | Saisissez les valeurs séparées par des virgules qui indiquent les options disponibles, laisser vide pour utiliser les options par défaut. | — | `5,10,20,30,50,100,150,200` |
| **Options de tri (Niveau 1) autorisé pour l'utilisateur frontend**<br />`orderby_options` | Sélectionner les options que vous souhaitez faire apparaitre à l'utilisateur en frontend afin qu'il puisse réordonner sa liste de contenu. **Remarque :** (a) **L'ordre par défaut**, est définit dans la section 'vue catégorie -&gt; ordre des contenus', (b)** l'ordre des contenus** ne fonctionne que pour la catégorie active et donc ne fonctionne pas si des sous catégories sont incluses dans la liste. | — | — |
| **Ordre personnalisé (Niveau 1) autorisé pour les utilisateur en**<br />`orderby_custom` | Veuillez entrer les champs personnalisés que vous souhaitez autoriser comme options de commande. Le format est (utiliser des cas multiples séparés COMMA) : champ :[alpha\|int\|décimal\|date]:[asc\|description] ou champ :[alpha\|int\|decimal\|date]:[asc\|description]:language_string ou file_fieldid:file_hits:[asc\|description]:language_string e. . (rappelez-vous : utiliser COMMA pour les choix multiples) 45:num:description, 57:decimal:asc:LANG_PRICE_LOWEST, 61:alpha:asc, 62:file_hits:description:LANG_MOST_MOWNLOADED | — | — |
| **Options de tri (Niveau 2) autorisé pour l'utilisateur frontend**<br />`orderby_options_2nd` | Sélectionner les options que vous souhaitez faire apparaitre à l'utilisateur en frontend afin qu'il puisse réordonner sa liste de contenu. **Remarque :** (a) **L'ordre par défaut**, est définit dans la section 'vue catégorie -&gt; ordre des contenus', (b)** l'ordre des contenus** ne fonctionne que pour la catégorie active et donc ne fonctionne pas si des sous catégories sont incluses dans la liste. | — | — |
| **Ordre personnalisé (Niveau 2) autorisé pour les utilisateur en**<br />`orderby_custom_2nd` | Veuillez entrer les champs personnalisés que vous souhaitez autoriser comme options de commande. Le format est (utiliser des cas multiples séparés COMMA) : champ :[alpha\|int\|décimal\|date]:[asc\|description] ou champ :[alpha\|int\|decimal\|date]:[asc\|description]:language_string ou file_fieldid:file_hits:[asc\|description]:language_string e. . (rappelez-vous : utiliser COMMA pour les choix multiples) 45:num:description, 57:decimal:asc:LANG_PRICE_LOWEST, 61:alpha:asc, 62:file_hits:description:LANG_MOST_MOWNLOADED | — | — |

## Sélection de contenu, pagination

### Sélection de contenu, pagination

:::note
Contenus sélectionnés
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Contenus non-autorisés**<br />`show_noauth` | Les contenus non autorisés à être visibles par un invité ou un utilisateur identifié seront inclus dans les listes de contenu (liste de catégories/favoris/tags/etc.) Lorsqu'un utilisateur essaye d'accéder à la vue détaillée d'un contenu non autorisé, les utilisateurs non connectés devront s'identifier et les utilisateurs déjà dentifiés verront une page d'erreur 404 accès interdit. **Remarque :** Si vous activez cette fonctionnalité, vous devriez aussi configurer le paramètre 'Page non autorisée' avec l'URL de la page à afficher pour ces erreurs | — | `0` |
| **Contenus propres**<br />`show_owned` | Activer pour lister les éléments détenus / rédigés par l'utilisateur actuellement connecté - quel que soit leur état, - indépendamment de la planification ou de l'expiration (date de publication / date d'expiration) | — | `1` |
| **Articles mis à la corbeille**<br />`show_trashed` | Activer pour lister les éléments mis à la corbeille aux utilisateurs privilégiés. Il s'agit des utilisateurs qui ont le privilège ACL \"Ignorer l'état des éléments\ | — | `1` |
| **Contenus de sous-catégories**<br />`display_subcategories_items` | Affiche ou non les contenus des sous catégories de la catégorie active | — | `0` |
| **Filtrer les éléments en utilisant la langue courante**<br />`filtercat` | Seulement les contenus de la langue active seront affichés dans la vue catégorie | — | `1` |

#### Limiter / supprimer les éléments

:::note
Limites -avant- recherche de texte, filtrage, indexation alphabétique
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer**<br />`use_limit_before_search_filt` | FLEXI_LIMIT_SUPPRESS_ITEMS_LIST_TILL_SUBMIT_DESC | — | `0` |
| **Nombre de contenus par page**<br />`limit_before_search_filt` | Indique le nombre de contenu à afficher sur chaque page de liste. | — | `0` |

:::note
Limites -après- recherche de texte, filtrage, indexation alphabétique
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Marqué par un drapeau**<br />`display_flag_featured` | Certains contenus de catégorie sont marqués en vedette / favori. Choisir d'afficher: (a) tous les contenus, (b) seulement les normaux, (c) seulement les marqués | — | `0` |
| **Nombre de contenus par page**<br />`limit` | Indique le nombre de contenu à afficher sur chaque page de liste. | — | `10` |

:::note
Limite via les champs personnalisés : veuillez définir 'Filtres verrouillés' dans l'onglet 'Recherche / Filtre formulaire'
:::

### Pagination (lien de page & total)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Défilement infini**<br />`infinite_scroll` | Autorise le chargement de contenus supplémentaires dans la vue catégorie sans recharger la page. Non = pagination classique. Charger plus = affiche un bouton « Charger plus » modifiable via une clé de langue. Défilement = charge les contenus automatiquement lorsque l’utilisateur fait défiler vers le bas. Les options Charger plus et Défilement désactivent la pagination numérotée. | — | `0` |
| **Afficher le nombre total de contenus**<br />`show_item_total` | Cette option affichera le nombre total de contenus de la catégorie (en fonction des paramètres d'affichage et des filtres actifs) | — | `1` |
| **Pagination (lien de page & total)**<br />`show_pagination` | Afficher/Masquer la pagination, tels que les liens et la page de total | — | `2` |
| **Résultat de la pagination (Nombre courant et total des pages)**<br />`show_pagination_results` | (lorsque la pagination est activée), vous pouvez utiliser cette option pour désactiver l'affichage du numéro de page active courante et le nombre total de pages | — | `1` |

#### Overide du Frontend

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Nombre de contenus par page**<br />`limit_override` | Indique le nombre de contenu à afficher sur chaque page de liste. | — | `1` |
| **Libellé « par page »**<br />`limit_override_label` | Ajouter le libellé à l'intérieur ou à l'extérieur le sélecteur, ou choisir de ne pas l'afficher | — | `2` |

## Contenus avec Post-it

:::note
Liste de contenu avec post-it catégories en vedette, niveau d'accès, créer récemment...
:::

### Post-it de catégorie

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Ajouter Post-it**<br />`mu_addcss_cats` | Ajoutez un span vide avec une classe CSS appropriée. S'il vous plaît examiner la sortie HTML pour trouver le nom de classe CSS | — | — |
| **Ajouter du texte (titre de catégorie)**<br />`mu_addtext_cats` | Sélectionnez quand le titre de la catégorie sera ajouté à l'intérieur du marquage **NOTE :** Ceci est recommandé pour les non-développeurs et pour les sites multilingues car les titres des catégories vedettes seront filtrés par langue (chaînes de langue) | — | `1` |

### Post-it niveau d'accès (pour les contenus)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Ajouter Post-it**<br />`mu_addcss_acclvl` | Ajoutez un span vide avec une classe CSS appropriée. S'il vous plaît examiner la sortie HTML pour trouver le nom de classe CSS | — | — |
| **Niveaux à obtenir**<br />`mu_add_condition_obtainded_acc` | Ajouter des marquages pour le niveau obtenu (accès) toujours ou seulement quand un élément de contenu est visible. **EXPLICATION :** Un élément de contenu a un niveau d'accès pour (a) lui-même, b) sa catégorie principale, c) son type de contenu. Un pour ces niveaux d'accès pourrait ne pas être assigné à l'utilisateur actuel, donc l'élément est invisible, vous pouvez choisir si vous voulez ajouter des marquages (balises) pour un autre niveau d'accès de l'élément déjà obtenu par l'utilisateur actuel. | — | `0` |
| **Ajouter texte**<br />`mu_addtext_acclvl` | Vous pouvez choisir d'ajouter du texte dans la zone de marquage. Celles-ci comprennent: aucun accès, accès (public) gratuit et noms de niveau d'accès, **NOTE :** Ceci est recommandé pour les non-développeurs et pour les sites multilingues étant donné que toutes ces langues seront filtrées (chaînes de langue) | — | — |
| **Texte pas d'accès personnalisé**<br />`mu_no_acc_text` | Le texte par défaut est « Aucun accès ». Vous pouvez définir une chaîne de langue personnalisés ici, par exemple « Restreint », « Membres seulement » | — | `FLEXI_MU_NO_ACC` (Accès interdit) |
| **Texte accès libre personnalisé**<br />`mu_free_acc_text` | Le texte par défaut est « Libre ». Vous pouvez définir une chaîne de langue personnalisée ici, par exemple 'Public', 'Tout le monde' | — | `FLEXI_MU_FREE` |

### Post-it Ajouté récemment

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Ajouter Post-it**<br />`mu_addcss_radded` | Ajoutez un span vide avec une classe CSS appropriée. S'il vous plaît examiner la sortie HTML pour trouver le nom de classe CSS | — | `0` |
| **Ajouter texte (nom de l'intervalle de temps)**<br />`mu_addtext_radded` | Ajouter le nom de la période dans la zone de marquage. **NOTE :** Ceci est recommandé pour les non-développeurs et pour les sites multilingues car ils seront filtrés dans la langue (chaînes de langue) | — | `1` |

#### Configuration de l'intervalle de temps

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Intervalle de temps**<br />`mu_ra_timeframe_intervals` | Il s'agit d'une liste d'intervalles de temps entier séparée par des virgules. eg écrire 48h pour un intervalle en heure ou 2d pour spécifier l'intervalle en jours | — | `24h , 2d , 7d , 1m , 3m , 1y , 3y` |
| **Noms des intervalles de temps**<br />`mu_ra_timeframe_names` | Ceci est un liste de chaînes de langue séparées par une virgule. Elles sont liées avec les périodes ci-dessus une par une, dans le même ordre qu'au-dessus | — | `FLEXI_24H_RA , FLEXI_2D_RA , FLEXI_7D_RA , FLEXI_1M_RA , FLEXI_3M_RA , FLEXI_1Y_RA , FLEXI_3Y_RA` |

### Post-it récemment modifiés

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Ajouter Post-it**<br />`mu_addcss_rupdated` | Ajoutez un span vide avec une classe CSS appropriée. S'il vous plaît examiner la sortie HTML pour trouver le nom de classe CSS | — | `0` |
| **Ajouter texte (nom de l'intervalle de temps)**<br />`mu_addtext_rupdated` | Ajouter le nom de la période dans la zone de marquage. **NOTE :** Ceci est recommandé pour les non-développeurs et pour les sites multilingues car ils seront filtrés dans la langue (chaînes de langue) | — | `1` |

#### Configuration de l'intervalle de temps

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Intervalle de temps**<br />`mu_ru_timeframe_intervals` | Il s'agit d'une liste d'intervalles de temps entier séparée par des virgules. eg écrire 48h pour un intervalle en heure ou 2d pour spécifier l'intervalle en jours | — | `24h , 2d , 7d , 1m , 3m , 1y , 3y` |
| **Noms des intervalles de temps**<br />`mu_ru_timeframe_names` | Ceci est un liste de chaînes de langue séparées par une virgule. Elles sont liées avec les périodes ci-dessus une par une, dans le même ordre qu'au-dessus | — | `FLEXI_24H_RU , FLEXI_2D_RU , FLEXI_7D_RU , FLEXI_1M_RU , FLEXI_3M_RU , FLEXI_1Y_RU , FLEXI_3Y_RU` |

## Options générales

#### Référencement

:::note
Vous pouvez configurer plus d'option dans l'onglet '%s'
:::

#### Commentaires

:::note
Vous pouvez configurer plus d'option dans l'onglet '%s'
:::

#### Liste des contenus

## Flux RSS

### Flux RSS

:::note
Activer les Flux RSS dans l'onglet '%s'
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Nombre de contenus par page**<br />`feed_limit` | Indique le nombre de contenu à afficher sur chaque page de liste. | — | `10` |
| **Pour chaque contenu, afficher :**<br />`feed_summary` | Sélectionner si vous préférez inclure dans votre flux RSS uniquement le texte d'introduction ou bien le texte complet. | — | `0` |
| **Longueur maximum du texte**<br />`feed_summary_cut` | Si le texte dépasse le nombre de caractère indiqué, il sera automatiquement tronqué. | — | `200` |
| **FLEXI_Read_More_Link**<br />`feed_show_readmore` | Si ce paramètre est activé le lien 'lire la suite...' apparaitra s'il a été ajouté dans la description principale du contenu. | — | `0` |

### Image

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser l'image**<br />`feed_use_image` | Extraire la première image du texte principale | — | `1` |
| **Lien sur l'image**<br />`feed_link_image` | Actif un lien sur l'image affichée. | — | `1` |
| **Source de l'image**<br />`feed_image_source` | Sélectionner la source de l'image. Vous pouvez aussi choisir un champ image (s'il y en a au moins un de disponible) ou automatiquement extraire l'image de la description. | — | — |
| **Taille de l'image**<br />`feed_image_size` | FLEXI_IMAGE_SIZE_DESC | — | — |
| **Largeur de l'image**<br />`feed_image_width` | Largeur de l'image | — | `80` |
| **Hauteur de l'image**<br />`feed_image_height` | Hauteur de l'image | — | `80` |
| **Méthode de traitement**<br />`feed_image_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | — | `1` |

### Champs personnalisés

:::note
Ne pas ajouter les champs qui pourraient cassés l'affichage du flux rss
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Liste des champs**<br />`feed_extra_fields` | Les champs qui nécessitent du CSS/JS supplémentaire ne fonctionneront pas correctement, les champs appropriés sont des champs comme la date, le texte, la sélection, etc. Entrez une liste séparée par des virgules des noms de champs | — | — |

### Ordre du contenu (niveau 1)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`feed_orderby` | Trier les éléments par des champs/propriétés du noyau | — | `rdate` |

#### Classement personnalisé des champs

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`feed_orderbycustomfield` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | — | `0` |
| **Champ personnalisé**<br />`feed_orderbycustomfieldid` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | — | `0` |
| **Sens du tri**<br />`feed_orderbycustomfielddir` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | — | `ASC` |
| **Méthode de tri**<br />`feed_orderbycustomfieldint` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | — | `0` |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

### Ordre du contenu (niveau 2)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`feed_orderby_2nd` | Trier les éléments par des champs/propriétés du noyau | — | `alpha` |

#### Classement personnalisé des champs

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`feed_orderbycustomfield_2nd` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | — | `1` |
| **Champ personnalisé**<br />`feed_orderbycustomfieldid_2nd` | Sélectionnez un champ personnalisé à utiliser pour l'ordre. Attention, certains types de champ ne peuvent pas être ordonnés (champ fichier et champ image par exemple). | — | `0` |
| **Sens du tri**<br />`feed_orderbycustomfielddir_2nd` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | — | `ASC` |
| **Méthode de tri**<br />`feed_orderbycustomfieldint_2nd` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | — | `0` |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

#### FLEXI_LISTS
