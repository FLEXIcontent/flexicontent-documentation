---
sidebar_position: 12
---

# Gestionnaires backend

Mise en page des gestionnaires de contenus, champs, types, catégories et fichiers.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

#### Configuration de l'administration

## Tableau de bord

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **URL de support**<br />`support_url` | Saisir l'adresse du site de votre support et des procédures. Si vous ne souhaitez pas faire apparaître l'icône d'aide, laissez ce champ vide. | — | — |
| **Afficher la vérification de la version**<br />`show_updatecheck` | Actif la vérification de la dernière version de FLEXIcontent et affiche le statut dans le panneau d'administration. | — | `1` |
| **Cacher les boutons**<br />`dashboard_buttons_hide` | À noter que cela masquera les boutons. Cela ne désactivera pas l'ACCÈS aux vues pointées par un boutons, utiliser les ACL pour désactiver l'accès à certaines vues. | — | — |
| **Désactiver les sliders**<br />`dashboard_sliders_disable` | À noter que cela masquera les boutons. Cela ne désactivera pas l'ACCÈS aux vues pointées par un boutons, utiliser les ACL pour désactiver l'accès à certaines vues. | — | — |
| **Editer les contenus dans une fenêtre popup**<br />`dashboard_modal_item_edit` | Les liens d'édition de contenus dans le slider seront ouverts dans une fenêtre popup | — | `1` |
| **Désactiver le logo FLEXIcontent**<br />`dashboard_disable_fc_logo` | Vous pouvez masquer l'image de FLEXIcontent, le texte de la licence et le droit d'auteur sera toujours visible | — | `0` |
| `dashboard_layout` | — | — | — |
| **Cacher les licences et crédits**<br />`dashboard_hide_fc_license_credits` | Cacher la licence en la plaçant dans les sliders du tableau de bord | — | `1` |

## Gestionnaire de contenu

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Langue du contenu original**<br />`original_content_language` | Ceci est utilisé pour mettre en évidence les traductions de contenu qui ne sont pas à jour dans les gestionnaires backend (À mettre à jour plus tard) par rapport à un contenu original | — | `_site_default_` |

### Comportement

#### Liste des contenus

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Afficher seulement les contenus visibles**<br />`iman_viewable_items` | Seuls les contenus visibles seront listés à l'utilisateur **NOTE : ** ce paramètre est ignoré pour l'utilisateur ayant le privilège ACL 'Afficher tous (contenus)' | — | `1` |
| **Liste des contenus dans la catégorie (principale) éditable**<br />`iman_editable_items` | Seuls la liste des contenus qui sont assignés à la catégorie (principale) éditable **NOTE : ** ce paramètre est ignoré pour l'utilisateur ayant le privilège ACL 'Afficher tous (contenus)' **Remarque :**cela ne garantira pas que tous les articles énumérés soient modifiables | — | `0` |
| **Liste uniquement les contenus de la langue de l'auteur**<br />`iman_authorlang_items` | Seuls les contenus dans la langue par défaut de l'auteur seront listés à l'utilisateur courant **NOTE :** ce paramètre est ignoré pour l'utilisateur avec le privilège ACL 'Associer n'importe quel élément' | — | `0` |

#### Comportement

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Autoriser la copie des contenus non éditables**<br />`copytask_allow_uneditable` | Ceci autorise les utilisateur de l'administration à copier ou copier-déplacer (mais pas déplacer) les contenus qu'ils n'ont pas le droit d'éditer, en utilisant l'outil copier/déplacer. **NOTE : **Comme précisé plus haut, ceci ne permettra pas de déplacer les contenus non-éditables. | — | `1` |
| **Contenus modifiables tant que l’utilisateur est connecté**<br />`items_session_editable` | Si un contenu est assigné à une catégorie dont il n'a pas les droits suffisant pour éditer alors le contenu restera éditable tant que l'utilisateur n'est pas déconnecté. | — | `1` |
| **Activer la connexion automatique pour la prévisualisation**<br />`autoflogin` | Si cette option est activée, le nom de l'utilisateur et son mot de passe seront ajoutés dans le lien de prévisualisation afin de connecter l'utilisateur automatiquement en frontend. | — | `1` |

### Apparence

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Style des onglets des types de contenu**<br />`iman_type_tabs_style` | Apparence des onglets des types de contenu au-dessus de la liste backend (lorsque les types sont affichés sous forme d’onglets). **Onglets navigateur** : l’onglet actif est relié à la liste ci-dessous. **Onglets suspendus** : onglets arrondis séparés, suspendus à la barre supérieure. **Soulignement** : onglets simples avec une ligne colorée sous l’onglet actif. **Plat** : onglets carrés dans une barre pleine, l’actif est rempli de la couleur d’accent. **Pastilles** : capsules arrondies, l’active est légèrement teintée. **Onglets Bootstrap** : onglets de navigation Bootstrap standard. | — | `browser` |
| **Lien rapide de filtrage par type**<br />`iman_quick_itype_links` | Ceci va créer des liens rapides dans le gestionnaire d'éléments pour définir le filtre de type d'élément à un type spécifique | — | `1` |
| **Bouton d'export CSV**<br />`show_csvbutton_be` | Activer l'export CSV | — | `0` |
| **Filtres de la liste backend**<br />`backend_filters_style` | Apparence de la boîte de filtres dans la liste backend des contenus. **Classique** correspond à la disposition d’origine en une seule colonne. **Moderne** organise les filtres en colonnes responsives afin qu’ils tiennent à l’écran. | — | `1` |
| **Appliquer les filtres (style moderne)**<br />`backend_filters_apply` | Utilisé uniquement lorsque **Filtres de la liste backend** est **Moderne**. **Avec bouton Appliquer** : la modification d’un filtre ne recharge pas la liste, les filtres sont appliqués avec le bouton **Appliquer**, ce qui permet de choisir plusieurs valeurs (ex. étiquettes) à la fois. **Instantanément** : la liste se recharge à chaque modification. | — | `1` |
| **Afficher le chemin des catégories dans les listes**<br />`cat_path_show` | Des catégories peuvent avoir le même titre dans différentes branches. Lorsque cette option est active, les sélecteurs backend (filtres, import, traitement par lot, formulaires…) affichent le chemin des catégories parentes, la recherche correspond aussi aux mots du chemin, et le gestionnaire des catégories affiche le chemin lorsque la liste est filtrée, recherchée ou réordonnée. | — | `1` |
| **Format du chemin des catégories**<br />`cat_path_mode` | **Chemin complet** : toutes les catégories parentes. **Derniers éléments** : uniquement les dernières catégories parentes (le chemin raccourci est préfixé par ...) | — | `full` |
| **Nombre de catégories parentes à afficher**<br />`cat_path_levels` | Nombre de dernières catégories parentes à afficher dans le chemin | — | `3` |
| **Désactiver les colonnes**<br />`iman_skip_cols` | Cacher définitivement les colonnes. L'utilisateur ne sera pas en mesure de les activer. Remarque : 'Type unique', signifie masquer la colonne si le filtrage par type est unique | — | — |
| **Colonnes personnalisées**<br />`items_manager_extra_fields` | En option inclure des colonnes de champs personnalisés dans la liste des contenus. ** Remarque : ** Ne pas inclure de champs personnalisés qui ne rentre pas ou qui désorganise la liste, ** Remarque : ** Certains champs peuvent poser problème lors de l'affichage dans le backend, dans ce cas essayer d'utiliser une autre variable d'affichage (par défaut c'est 'display') OU les enlever de la liste, ** Remarque : ** Vous pouvez personnaliser cela dans toutes les configurations de type de contenu. Par contenu les types de champs seront affichés quand vous filtrez la liste du gestionnaire de contenus grâce au filtre de type de contenu. ** FORMAT : ** fieldname1, fieldname2, fieldname3:dispname3, fieldname4:dispname4, fieldname5 | — | — |
| **Apparence des colonnes personnalisées**<br />`items_manager_cols_appearance` | Apparence par défaut des valeurs des colonnes personnalisées dans la liste : valeur brute, coche (la valeur du champ apparaît dans une infobulle au survol) ou valeur nettoyée du HTML et coupée. Peut être redéfinie par champ dans les paramètres d’affichage backend du champ. | — | `0` |
| **Longueur de coupure (caractères)**<br />`items_manager_trim_chars` | Nombre de caractères à conserver après suppression des balises HTML. | — | `100` |
| **Filtrage personnalisé**<br />`items_manager_custom_filters` | Sélectionnez les champs personnalisés à ajouter en tant que filtres du gestionnaire d'éléments. NOTE : le sélecteur déroulant affiche les types de champs pris en charge | — | — |
| **Gestion de l'ordre d'affichage des contenus**<br />`items_manager_order` | Sélection de l'ordre par défaut pour la liste des contenus | — | `a.id` |
| **Direction de l'ordre de tri**<br />`items_manager_order_dir` | Sélection de l'ordre de tri par défaut pour l'affichage de la liste de contenu | — | `DESC` |

## Gestionnaire d'importation

### Basique

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **ID du contenu personnalisé**<br />`import_id_col` | REMARQUE : Avant le début de l'importation finale, - [Créer] tous les identifiants d'élément sont vérifiés qu'ils n'existent pas - [Mettre à jour] tous les éléments sont vérifiés qu'ils existent Remarque : - [Créer-Mettre à jour] Utilisez zéro ou un ID d'élément non existant pour indiquer la création d'un nouvel élément - [Créer] Vous pouvez utiliser zéro au lieu d'utiliser un ID d'élément spécifique pour le nouvel élément | — | `0` |
| **Langue**<br />`import_lang` | Saisir * OU en-GB ou fr-FR ou de-DE ... | — | `*` |
| **Statut**<br />`import_state` | — | — | `1` |
| **Accès**<br />`import_access` | — | — | `1` |

### Publier

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Créateur (auteur)**<br />`import_created_by_col` | — | — | `0` |
| **Dernière modification**<br />`import_modified_by_col` | — | — | `0` |

#### Métadonnées

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utilisez la colonne « metadesc » (Description de métadonnées)**<br />`import_metadesc_col` | — | — | `0` |
| **Utilisez la colonne « metakey » (métadonnées Mots-clés)**<br />`import_metakey_col` | — | — | `0` |
| **Utiliser la colonne 'custom_ititle'**<br />`import_custom_ititle_col` | Vous pouvez définir un titre personnalisé qui sera utilisé comme tag HTML TITLE. Cela peut être très utile pour vos stratégies SEO. Si vous laissez ce champ vide, cela sera le titre de l'article qui sera utilisé. | — | `0` |

#### Dates

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Date de création**<br />`import_created_col` | — | — | `0` |
| **Date de modification**<br />`import_modified_col` | — | — | `0` |
| **Utilisez la colonne « publish_up » (Début de Publication)**<br />`import_publish_up_col` | — | — | `0` |
| **Utilisez la colonne « publish_down » (Fin de Publication)**<br />`import_publish_down_col` | — | — | `0` |

### Mots clés

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Mots clés**<br />`import_tags_col` | — | — | `0` |

### Dossier média/document

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Dossier média (champs image/galerie)**<br />`import_media_folder` | Veuillez entrer un chemin relatif par exemple **tmp/nom de dossier** ... depuis votre dossier d'installation Joomla **../foldername** ... juste au-dessus du dossier d'installation de Joomla | — | `tmp/fcimport_media` |
| **Dossier document (champs fichier)**<br />`import_docs_folder` | Veuillez entrer un chemin relatif par exemple **tmp/nom de dossier** ... depuis votre dossier d'installation Joomla **../foldername** ... juste au-dessus du dossier d'installation de Joomla | — | `tmp/fcimport_docs` |

### Format du fichier CSV

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Séparateur de champs**<br />`csv_field_sep` | Caractères multiples recommandés ex: ~~ pour une tabulation indiquer: \t | — | `~~` |
| **Caractère d'encadrement des champs**<br />`csv_field_enclose_char` | A n'utiliser que si vos données en contiennent, par exemple pour une double apostrophe, indiquer : ' | — | — |
| **Séparateur de contenu**<br />`csv_item_record_sep` | Caractères multiples recommandés ex : \n~~ for un saut de ligne, indiquez: \n | — | `\n~~` |
| **Déboguer les # premiers contenus**<br />`csv_debug_records` | Cela affichera les champs des premiers # enregistrements (éléments). **NOTE :** ceci est utilisé **seulement lors du test du format de fichier**. Il est recommandé de tester votre fichier CSV avant d'essayer d'importer. | — | `0` |

#### Champs multi-valeurs

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Séparateur de multi-valeur**<br />`csv_field_mval_sep` | Champs multi valeurs | — | `%%` |
| **Séparateurs Multi-proriété**<br />`csv_field_mprop_sep` | Champs multi propriétés par valeur | — | `!!` |

### Avancé

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Ignorer les colonnes non-utilisées**<br />`import_ignore_unused_cols` | Activer cette option si vous avez des colonnes redondantes. | — | `0` |
| **Contenus par étape d’import**<br />`import_items_per_step` | Ceci est le nombre de **éléments à ajouter** par étape. -- une grande étape donnera plus de vitesse, mais vous pouvez provoquer certaines étapes à expirer. -- Alors, prenez soin de définir un petit nombre ici si 1. vous avez des éléments qui ont de grandes images 'original' (il faut une miniature) 2. ou si vous avez des plugins de contenu \"lourds\" 3. ou si vous utilisez l'index de recherche intelligente de Joomla sur un grand site | — | `5` |

#### Configuration de l'administration
