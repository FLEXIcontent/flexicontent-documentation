---
sidebar_position: 12
---

# Champs cœur (Joomla)

Plugin des champ systèmes pour FLEXIcontent

*Plugin : `core` — Champs cœur*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/core/core.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Réseaux sociaux

### Prise en charge des réseaux sociaux (ex. Facebook)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Suggérer le champ aux listes**<br />`useogp` | Intégrer le champ texte dans l'Open Graph (og:description ou og:title) | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Longueur maximum du texte**<br />`ogpmaxlen` | Saisir le nombre maximum de caractères à utiliser avant d'être tronqué. | `text` | — | `300` |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Champ formulaire

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `list` | `1` = Texte à Rechercher | `0` |

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `1` = Texte à Rechercher | `0` |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Format de la date**<br />`date_format` | Si vous choisissez 'format personnalisé' dans la liste ci-dessus vous devez spécifier dans ce champ le format que vous souhaitez afficher en utilisant la syntaxe PHP date (http://php.net/manual/en/function.date.php) (ATTENTION ne pas utilisé le strftime). | `multilist` | `DATE_FORMAT_LC1` = DATE_FORMAT_LC1<br />`DATE_FORMAT_LC2` = DATE_FORMAT_LC2<br />`DATE_FORMAT_LC3` = DATE_FORMAT_LC3<br />`DATE_FORMAT_LC4` = DATE_FORMAT_LC4<br />`—` = Format personnalisé | — |
| **Format personnalisé**<br />`custom_date` | Si vous choisissez 'format personnalisé' dans la liste ci-dessus vous devez spécifier dans ce champ le format que vous souhaitez afficher en utilisant la syntaxe PHP strftime (http://php.net/strftime). | `text` | — | — |
| **Format du filtre de langue**<br />`lang_filter_format` | Appliquer le filtre de langue JText::_() sur la chaîne de format qui doit être une chaîne de langue, soit ajouté dans un fichier de langue, soit ajouté par le gestionnaire de langue Joomla. **AVERTISSEMENT**: Vous devez désactiver le filtrage de langue si vous n'ajoutez pas de chaîne de langue ! sinon certains caractères seront supprimés comme des virgules | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Référencement

### Prise en charge des microdonnées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Propriété des microdonnées**<br />`microdata_itemprop` | Sélectionnez une propriété de microdonnées pour caractériser toutes les valeurs de ce champ. Cela permettra aux moteurs de recherche de classer les valeurs de ce champ de manière appropriée, améliorant ainsi le référencement de vos pages | `radio` | `0` = Désactivé<br />`dateCreated` = dateCreated | `dateCreated` (dateCreated) |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ordre des valeurs de filtrage**<br />`reverse_filter_order` | Activer pour afficher les valeurs de filtre dans l'ordre inverse. NOTE : dans le cas de l'affichage de la plage du slider, la poignée de gauche sera le maximum, et la poignée de droite sera le minimum | `radio` | `0` = Normal<br />`1` = Inverse | `0` (Normal) |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Désactiver le clavier**<br />`disable_keyboardinput` | Activez cette option pour désactiver les entrées du clavier | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Préfixe / Suffixe

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_filter` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_filter` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Texte d'ouverture**<br />`opentag_filter` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_filter` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Regroupement de filtre pour l'affichage des types non textuels**<br />`date_filter_group` | Sélectionner le regroupement par date : années,mois ou jours. Cela sera utilisé quand le filtre est affiché en tant que liste, radio ou checkbox | `radio` | `year` = Année<br />`month` = Mois<br />`day` = Jour | `month` (Mois) |
| **Afficher une date au format personnalisé**<br />`date_filter_label_format` | par exemple '%Y-%M' affichera '2025-août' voir la documentation de la fonction SQL DATE_FORMAT, commune : %d jour du mois, numérique (00. 31), %b Nom du mois abrégé (Jan. Dec), %M Month name (Janvier..Décembre), %m Mois numérique (00.. 2), %Y Année numérique, quatre chiffres, %y Année numérique (deux chiffres) | `text` | — | — |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Sélecteur de date<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Sélecteur de date (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Sélecteur liste déroulante

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Option par défaut personnalisé (pour toutes les valeurs)**<br />`filter_usefirstoption` | Activer pour personnaliser la première option du filtre (=toutes les valeurs) . NOTE : ceci n'est utilisé que dans le cas de la sélection déroulante, et aussi si l'étiquette du champ n'est pas placée à l'intérieur du sélecteur | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'option par défaut (ex. Toutes les couleurs)**<br />`filter_firstoptiontext` | Texte de la première option de la sélection déroulante, par exemple « Toutes les couleurs » ou « FLEXI_ALL » etc. **NOTE**: Cette option n'a aucune valeur **NOTE**: Ce texte est filtré dans la langue de sorte que vous pouvez entrer une chaîne de langue remplaçable | `text` | — | `FLEXI_ALL` (Tous) |

#### Curseur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Données du slider**<br />`slider_display_config` | Utiliser les valeurs existantes dans le champ, ou spécifier vos propre valeurs d'échelle | `multilist` | `1` = Valeurs trouvées<br />`2` = Valeurs personnalisées | `1` (Valeurs trouvées) |
| **Valeurs personnalisées**<br />`slider_custom_range` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': '2000', '50%': '2005', '75%': '2020', 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_2000 ## label_2005 ## label_2020 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Regroupement de filtre pour l'affichage des types non textuels**<br />`date_filter_group_s` | Sélectionner le regroupement par date : années,mois ou jours. Cela sera utilisé quand le filtre est affiché en tant que liste, radio ou checkbox | `radio` | `year` = Année<br />`month` = Mois<br />`day` = Jour | `month` (Mois) |
| **Afficher une date au format personnalisé**<br />`date_filter_label_format_s` | par exemple '%Y-%M' affichera '2025-août' voir la documentation de la fonction SQL DATE_FORMAT, commune : %d jour du mois, numérique (00. 31), %b Nom du mois abrégé (Jan. Dec), %M Month name (Janvier..Décembre), %m Mois numérique (00.. 2), %Y Année numérique, quatre chiffres, %y Année numérique (deux chiffres) | `text` | — | — |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Sélecteur de date<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Sélecteur de date (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter_s` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items_s` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values_s` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Sélecteur liste déroulante

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Option par défaut personnalisé (pour toutes les valeurs)**<br />`filter_usefirstoption_s` | Activer pour personnaliser la première option du filtre (=toutes les valeurs) . NOTE : ceci n'est utilisé que dans le cas de la sélection déroulante, et aussi si l'étiquette du champ n'est pas placée à l'intérieur du sélecteur | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'option par défaut (ex. Toutes les couleurs)**<br />`filter_firstoptiontext_s` | Texte de la première option de la sélection déroulante, par exemple « Toutes les couleurs » ou « FLEXI_ALL » etc. **NOTE**: Cette option n'a aucune valeur **NOTE**: Ce texte est filtré dans la langue de sorte que vous pouvez entrer une chaîne de langue remplaçable | `text` | — | `FLEXI_ALL` (Tous) |

#### Curseur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Données du slider**<br />`slider_display_config_s` | Utiliser les valeurs existantes dans le champ, ou spécifier vos propre valeurs d'échelle | `multilist` | `1` = Valeurs trouvées<br />`2` = Valeurs personnalisées | `1` (Valeurs trouvées) |
| **Valeurs personnalisées**<br />`slider_custom_range_s` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': 2000, '50%': 2005, '75%': 2020, 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels_s` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_2000 ## label_2005 ## label_2020 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext_s` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Afficher**<br />`name_username` | Choisir si vous souhaitez afficher le nom ou le nom d'utilisateur. | `radio` | `1` = Nom<br />`2` = Nom d'utilisateur | `1` (Nom) |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Champ formulaire

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter_s` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items_s` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values_s` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Format de la date**<br />`date_format` | Si vous choisissez 'format personnalisé' dans la liste ci-dessus vous devez spécifier dans ce champ le format que vous souhaitez afficher en utilisant la syntaxe PHP date (http://php.net/manual/en/function.date.php) (ATTENTION ne pas utilisé le strftime). | `multilist` | `DATE_FORMAT_LC1` = DATE_FORMAT_LC1<br />`DATE_FORMAT_LC2` = DATE_FORMAT_LC2<br />`DATE_FORMAT_LC3` = DATE_FORMAT_LC3<br />`DATE_FORMAT_LC4` = DATE_FORMAT_LC4<br />`—` = Format personnalisé | — |
| **Format personnalisé**<br />`custom_date` | Si vous choisissez 'format personnalisé' dans la liste ci-dessus vous devez spécifier dans ce champ le format que vous souhaitez afficher en utilisant la syntaxe PHP strftime (http://php.net/strftime). | `text` | — | — |
| **Format du filtre de langue**<br />`lang_filter_format` | Appliquer le filtre de langue JText::_() sur la chaîne de format qui doit être une chaîne de langue, soit ajouté dans un fichier de langue, soit ajouté par le gestionnaire de langue Joomla. **AVERTISSEMENT**: Vous devez désactiver le filtrage de langue si vous n'ajoutez pas de chaîne de langue ! sinon certains caractères seront supprimés comme des virgules | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Référencement

### Prise en charge des microdonnées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Propriété des microdonnées**<br />`microdata_itemprop` | Sélectionnez une propriété de microdonnées pour caractériser toutes les valeurs de ce champ. Cela permettra aux moteurs de recherche de classer les valeurs de ce champ de manière appropriée, améliorant ainsi le référencement de vos pages | `radio` | `0` = Désactivé<br />`dateModified` = dateModified | `dateModified` (dateModified) |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ordre des valeurs de filtrage**<br />`reverse_filter_order` | Activer pour afficher les valeurs de filtre dans l'ordre inverse. NOTE : dans le cas de l'affichage de la plage du slider, la poignée de gauche sera le maximum, et la poignée de droite sera le minimum | `radio` | `0` = Normal<br />`1` = Inverse | `0` (Normal) |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Désactiver le clavier**<br />`disable_keyboardinput` | Activez cette option pour désactiver les entrées du clavier | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Préfixe / Suffixe

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_filter` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_filter` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Texte d'ouverture**<br />`opentag_filter` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_filter` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Regroupement de filtre pour l'affichage des types non textuels**<br />`date_filter_group` | Sélectionner le regroupement par date : années,mois ou jours. Cela sera utilisé quand le filtre est affiché en tant que liste, radio ou checkbox | `radio` | `year` = Année<br />`month` = Mois<br />`day` = Jour | `month` (Mois) |
| **Afficher une date au format personnalisé**<br />`date_filter_label_format` | par exemple '%Y-%M' affichera '2025-août' voir la documentation de la fonction SQL DATE_FORMAT, commune : %d jour du mois, numérique (00. 31), %b Nom du mois abrégé (Jan. Dec), %M Month name (Janvier..Décembre), %m Mois numérique (00.. 2), %Y Année numérique, quatre chiffres, %y Année numérique (deux chiffres) | `text` | — | — |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Sélecteur de date<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Sélecteur de date (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Sélecteur liste déroulante

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Option par défaut personnalisé (pour toutes les valeurs)**<br />`filter_usefirstoption` | Activer pour personnaliser la première option du filtre (=toutes les valeurs) . NOTE : ceci n'est utilisé que dans le cas de la sélection déroulante, et aussi si l'étiquette du champ n'est pas placée à l'intérieur du sélecteur | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'option par défaut (ex. Toutes les couleurs)**<br />`filter_firstoptiontext` | Texte de la première option de la sélection déroulante, par exemple « Toutes les couleurs » ou « FLEXI_ALL » etc. **NOTE**: Cette option n'a aucune valeur **NOTE**: Ce texte est filtré dans la langue de sorte que vous pouvez entrer une chaîne de langue remplaçable | `text` | — | `FLEXI_ALL` (Tous) |

#### Curseur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Données du slider**<br />`slider_display_config` | Utiliser les valeurs existantes dans le champ, ou spécifier vos propre valeurs d'échelle | `multilist` | `1` = Valeurs trouvées<br />`2` = Valeurs personnalisées | `1` (Valeurs trouvées) |
| **Valeurs personnalisées**<br />`slider_custom_range` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': '2000', '50%': '2005', '75%': '2020', 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_2000 ## label_2005 ## label_2020 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Regroupement de filtre pour l'affichage des types non textuels**<br />`date_filter_group_s` | Sélectionner le regroupement par date : années,mois ou jours. Cela sera utilisé quand le filtre est affiché en tant que liste, radio ou checkbox | `radio` | `year` = Année<br />`month` = Mois<br />`day` = Jour | `month` (Mois) |
| **Afficher une date au format personnalisé**<br />`date_filter_label_format_s` | par exemple '%Y-%M' affichera '2025-août' voir la documentation de la fonction SQL DATE_FORMAT, commune : %d jour du mois, numérique (00. 31), %b Nom du mois abrégé (Jan. Dec), %M Month name (Janvier..Décembre), %m Mois numérique (00.. 2), %Y Année numérique, quatre chiffres, %y Année numérique (deux chiffres) | `text` | — | — |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Sélecteur de date<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Sélecteur de date (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter_s` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items_s` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values_s` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Sélecteur liste déroulante

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Option par défaut personnalisé (pour toutes les valeurs)**<br />`filter_usefirstoption_s` | Activer pour personnaliser la première option du filtre (=toutes les valeurs) . NOTE : ceci n'est utilisé que dans le cas de la sélection déroulante, et aussi si l'étiquette du champ n'est pas placée à l'intérieur du sélecteur | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'option par défaut (ex. Toutes les couleurs)**<br />`filter_firstoptiontext_s` | Texte de la première option de la sélection déroulante, par exemple « Toutes les couleurs » ou « FLEXI_ALL » etc. **NOTE**: Cette option n'a aucune valeur **NOTE**: Ce texte est filtré dans la langue de sorte que vous pouvez entrer une chaîne de langue remplaçable | `text` | — | `FLEXI_ALL` (Tous) |

#### Curseur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Données du slider**<br />`slider_display_config_s` | Utiliser les valeurs existantes dans le champ, ou spécifier vos propre valeurs d'échelle | `multilist` | `1` = Valeurs trouvées<br />`2` = Valeurs personnalisées | `1` (Valeurs trouvées) |
| **Valeurs personnalisées**<br />`slider_custom_range_s` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': 2000, '50%': 2005, '75%': 2020, 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels_s` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_2000 ## label_2005 ## label_2020 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext_s` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Afficher**<br />`name_username` | Choisir si vous souhaitez afficher le nom ou le nom d'utilisateur. | `radio` | `1` = Nom<br />`2` = Nom d'utilisateur | `1` (Nom) |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Champ formulaire

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter_s` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items_s` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values_s` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les icônes**<br />`show_icons` | Affiche les icônes imprimer et email ou utiliser uniquement le texte | `multilist` | `0` = Texte<br />`1` = Icône<br />`2` = Les deux | `1` (Icône) |
| **Type d'icône**<br />`use_font_icons` | Vous pouvez afficher des icônes comme des images ou utiliser les jeu de polices d’icônes | `radio` | `0` = Image<br />`1` = Icônes polices | `1` (Icônes polices) |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Champ formulaire

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Champ formulaire

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter_s` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items_s` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values_s` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Apparence

#### Apparence

### Basique

#### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher pour les clients**<br />`show_in_clients` | Sélectionner si le champ sera créé et affiché à des clients spécifiques | `fccheckbox` | — | — |
| **Afficher dans les vues**<br />`show_in_views` | Sélectionner si le champ sera créé et affiché en fonction d'une vue spécifique | `fccheckbox` | — | — |

#### FLEXI_FIELD_VOTE_STARS_APPEARANCE

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_FIELD_VOTE_STARS_SIZE**<br />`stars_size` | FLEXI_FIELD_VOTE_STARS_SIZE_DESC | `number` | — | `24` |
| **FLEXI_FIELD_VOTE_STARS_TOOLTIPS**<br />`stars_tooltips` | FLEXI_FIELD_VOTE_STARS_TOOLTIPS_DESC | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **FLEXI_FIELD_VOTE_STARS_COLOR**<br />`stars_color` | FLEXI_FIELD_VOTE_STARS_COLOR_DESC | `fccolor` | — | `#FFB400` |
| **FLEXI_FIELD_VOTE_STARS_COLOR_EMPTY**<br />`stars_color_empty` | FLEXI_FIELD_VOTE_STARS_COLOR_EMPTY_DESC | `fccolor` | — | `#CCCCCC` |

#### Libellé et accès

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Montrer un message d'**accès interdit****<br />`show_acc_msg` | Si le champ est inaccessible, une message de non-accès s'affichera. **NOTE : ** SI ce paramètre est désactivé, le champ sera invisible aux utilisateurs sans accès, sans aucun message ou avertissement indiquant son existance | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Message **accès interdit****<br />`no_acc_msg` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Exporter

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Valeurs brutes | `0` (Non) |

#### FLEXI_BACKEND_VIEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_BACKEND_VIEW_APPEARANCE**<br />`backend_view_appearance` | FLEXI_BACKEND_VIEW_APPEARANCE_DESC | `multilist` | `0` = Par défaut<br />`1` = FLEXI_CHECK_MARK<br />`2` = FLEXI_CLEAN_HTML_AND_TRIM | `0` (Par défaut) |
| **FLEXI_TRIM_LENGTH**<br />`backend_view_trim_chars` | FLEXI_TRIM_LENGTH_DESC | `text` | — | `100` |

### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |

#### Vote

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer dans les vues**<br />`vote_submit_inview` | Vous pouvez activer ou désactiver le paramètre ci-dessus en fonction de la vue active de FLEXIcontent | `fccheckbox` | — | — |

### Liste Valeurs

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

### Plugins de contenu

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Apparence

## Permissions

Vous pouvez configurer qui a le droit de soumettre un vote, le message qui sera affiché pour ceux qui n'ont pa le droit etc.

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Accès à la soumission**<br />`submit_acclvl` | Le groupe d'utilisateurs affecté à ce niveau d'accès sera en mesure de voter. - e. **créez un niveau d'accès 'Vote de contenu'** et assignez-le aux groupes d'utilisateurs dont vous avez besoin **REMARQUE:** Vous n'avez qu'à l'assigner au groupe d'utilisateurs parent. Si vous assignez ce niveau d'accès au groupe d'utilisateurs 'Enregistré', alors TOUS les groupes d'utilisateurs qui en sont enfants le verront ... | `accesslevel` | — | `1` |

### Aucun accès aux manipulations

#### Utilisateurs enregistrés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Message**<br />`logged_no_acc_msg` | Le message d'info-bulle (chaîne de langue) qui sera affiché aux utilisateurs qui ne peuvent pas voter, p. ex. vous pouvez demander à vos utilisateurs de s'inscrire ou d'acheter un abonnement, etc **NOTE :** Laisser vide pour afficher un message par défaut qui indique le nom du niveau d'accès requis | `text` | — | — |
| **Faire une redirection**<br />`logged_no_acc_doredirect` | Sélectionner quand rediriger les utilisateurs autorisés | `radio` | `0` = Non<br />`1` = URL de redirection | `0` (Non) |
| **Redirection de confirmation utilisateurs**<br />`logged_no_acc_askredirect` | Il sera demandé à l'utilisateur si il veut être redirigé | `radio` | `0` = Non<br />`1` = Non, informer seulement<br />`2` = Oui, demander à l'utilisateur | `1` (Non, informer seulement) |
| **URL de redirection**<br />`logged_no_acc_url` | L'URL à charger quand l'utilisateur clique sur le champ de vote alors qu'il n'est pas autorisé à voter | `text` | — | — |

#### Utilisateurs invités

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Message**<br />`guest_no_acc_msg` | Le message d'info-bulle (chaîne de langue) qui sera affiché aux utilisateurs qui ne peuvent pas voter, p. ex. vous pouvez demander à vos utilisateurs de s'inscrire ou d'acheter un abonnement, etc **NOTE :** Laisser vide pour afficher un message par défaut qui indique le nom du niveau d'accès requis | `text` | — | — |
| **Faire une redirection**<br />`guest_no_acc_doredirect` | Sélectionner quand rediriger les utilisateurs autorisés | `radio` | `0` = Non<br />`1` = URL de redirection<br />`2` = Connexion/enregistrement | `2` (Connexion/enregistrement) |
| **Redirection de confirmation utilisateurs**<br />`guest_no_acc_askredirect` | Il sera demandé à l'utilisateur si il veut être redirigé | `radio` | `0` = Non<br />`1` = Non, informer seulement<br />`2` = Oui, demander à l'utilisateur | `1` (Non, informer seulement) |
| **URL de redirection**<br />`guest_no_acc_url` | L'URL à charger quand l'utilisateur clique sur le champ de vote alors qu'il n'est pas autorisé à voter | `text` | — | — |

## Note / Score

:::note
Vous pouvez afficher le champ dans le formulaire de l'élément pour le traiter comme **'Note' / 'Score' champ**. Dans un tel cas, vous devriez donner à ce champ (à l'intérieur de l'onglet Affichage) un niveau d'accès au vote qui est attribué (accordé) uniquement à un groupe d'utilisateurs spécial qui est censé faire le 'notation' / 'marquage'
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Formulaire de saisie**<br />`vote_iform_display` | — | `radio` | `0` = Cacher<br />`1` = Montrer<br />`2` = Lecture seule | `0` (Cacher) |

## Critiques

Activer et configurer les revue sur les contenus

:::note
FLEXI_FIELD_VOTE_REVIEWS_ALPHA_WARNING
:::

#### reviews_conf

### FLEXI_FIELD_VOTE_REVIEWS_TAB_WORKFLOW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`allow_reviews` | FLEXI_FIELD_VOTE_REVIEWS_ENABLE_DESC | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### FLEXI_FIELD_VOTE_REVIEWS_NEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_FIELD_VOTE_REVIEWS_ALLOW_SUBMIT**<br />`allow_submit_review_by` | FLEXI_FIELD_VOTE_REVIEWS_ALLOW_SUBMIT_DESC | `radio` | `0` = Désactivé<br />`1` = FLEXI_FIELD_VOTE_REVIEWS_SUBMIT_ANYONE<br />`2` = FLEXI_FIELD_VOTE_REVIEWS_SUBMIT_LOGGED<br />`3` = FLEXI_FIELD_VOTE_REVIEWS_SUBMIT_ACCESSLEVEL | `0` (Désactivé) |
| **FLEXI_FIELD_VOTE_REVIEWS_SUBMIT_ACCESS**<br />`review_submit_access` | FLEXI_FIELD_VOTE_REVIEWS_SUBMIT_ACCESS_DESC | `accesslevel` | — | `1` |

#### FLEXI_FIELD_VOTE_REVIEWS_PUBLISHING

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_FIELD_VOTE_REVIEWS_APPROVAL**<br />`do_approval` | FLEXI_FIELD_VOTE_REVIEWS_APPROVAL_DESC | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### FLEXI_FIELD_VOTE_REVIEWS_GUESTS

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_FIELD_VOTE_REVIEWS_VERIFY_EMAIL**<br />`verify_email_ownership` | FLEXI_FIELD_VOTE_REVIEWS_VERIFY_EMAIL_DESC | `radio` | `0` = Non<br />`1` = FLEXI_FIELD_VOTE_REVIEWS_VERIFY_EMAIL_YES | `1` (FLEXI_FIELD_VOTE_REVIEWS_VERIFY_EMAIL_YES) |

### FLEXI_FIELD_VOTE_REVIEWS_TAB_LAYOUT

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_FIELD_VOTE_REVIEWS_PLACEMENT**<br />`reviews_placement` | FLEXI_FIELD_VOTE_REVIEWS_PLACEMENT_DESC | `multilist` | `0` = En ligne<br />`1` = Fenêtre Popup | `0` (En ligne) |

:::note
FLEXI_FIELD_VOTE_REVIEWS_INLINE_INFO
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_FIELD_VOTE_REVIEWS_PAGE_SIZE**<br />`reviews_page_size` | FLEXI_FIELD_VOTE_REVIEWS_PAGE_SIZE_DESC | `text` | — | `5` |
| **FLEXI_FIELD_VOTE_REVIEWS_USEFUL**<br />`reviews_useful` | FLEXI_FIELD_VOTE_REVIEWS_USEFUL_DESC | `radio` | `0` = Désactivé<br />`1` = FLEXI_FIELD_VOTE_REVIEWS_USEFUL_LOGGED<br />`2` = FLEXI_FIELD_VOTE_REVIEWS_USEFUL_ANYONE | `1` (FLEXI_FIELD_VOTE_REVIEWS_USEFUL_LOGGED) |
| **FLEXI_FIELD_VOTE_REVIEWS_COUNTER_LISTS**<br />`reviews_counter_in_lists` | FLEXI_FIELD_VOTE_REVIEWS_COUNTER_LISTS_DESC | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **FLEXI_FIELD_VOTE_REVIEWS_LOADER**<br />`reviews_loader` | FLEXI_FIELD_VOTE_REVIEWS_LOADER_DESC | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **FLEXI_FIELD_VOTE_REVIEWS_LIVE_UPDATE**<br />`reviews_live_update` | FLEXI_FIELD_VOTE_REVIEWS_LIVE_UPDATE_DESC | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **FLEXI_FIELD_VOTE_REVIEWS_STORE_RATING**<br />`reviews_store_rating` | FLEXI_FIELD_VOTE_REVIEWS_STORE_RATING_DESC | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **FLEXI_FIELD_VOTE_REVIEWS_MAX_LENGTH**<br />`reviews_max_length` | FLEXI_FIELD_VOTE_REVIEWS_MAX_LENGTH_DESC | `text` | — | `500` |

#### reviews_conf

## Avancé

#### Avancé

### Aucune évaluation

### Vote par défaut et poids pour les votes faibles

#### Vote par défaut % en fonction de l'ordre, (0 vote)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Vote %**<br />`default_rating` | Pourcentage de contenus sans vote, utilisées pour le classement de notation | `integer` | — | `50` |

#### Poids de la note % lors de la commande, (1 à 9 votes), réduire le % pour les pousser vers le bas de la liste des articles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Poids du vote %**<br />`vote_1_weight` | - Entrez 100 pour les considérer pleinement, - Entrez un % inférieur pour les éloigner du début | `integer` | — | `100` |
| **Poids du vote %**<br />`vote_2_weight` | - Entrez 100 pour les considérer pleinement, - Entrez un % inférieur pour les éloigner du début | `integer` | — | `100` |
| **Poids du vote %**<br />`vote_3_weight` | - Entrez 100 pour les considérer pleinement, - Entrez un % inférieur pour les éloigner du début | `integer` | — | `100` |
| **Poids du vote %**<br />`vote_4_weight` | - Entrez 100 pour les considérer pleinement, - Entrez un % inférieur pour les éloigner du début | `integer` | — | `100` |
| **Poids du vote %**<br />`vote_5_weight` | - Entrez 100 pour les considérer pleinement, - Entrez un % inférieur pour les éloigner du début | `integer` | — | `100` |
| **Poids du vote %**<br />`vote_6_weight` | - Entrez 100 pour les considérer pleinement, - Entrez un % inférieur pour les éloigner du début | `integer` | — | `100` |
| **Poids du vote %**<br />`vote_7_weight` | - Entrez 100 pour les considérer pleinement, - Entrez un % inférieur pour les éloigner du début | `integer` | — | `100` |
| **Poids du vote %**<br />`vote_8_weight` | - Entrez 100 pour les considérer pleinement, - Entrez un % inférieur pour les éloigner du début | `integer` | — | `100` |
| **Poids du vote %**<br />`vote_9_weight` | - Entrez 100 pour les considérer pleinement, - Entrez un % inférieur pour les éloigner du début | `integer` | — | `100` |

### Résolution et affichage personnalisé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Résolution du vote pour les nouveaux sites OU ***<br />`rating_resolution` | Ceci est à utiliser lors de la construction de nouveaux sites ou ... lisez ci-dessous. La résolution intégrée de Joomla! est de 5 **NOTE :** La modification de cette résolution dans les sites existants rendra la moyenne de notation erronée !! **REMARQUE :** (pour les développeurs) Il est possible de mettre à jour la table d'évaluation avec une requête SQL comme: **UPDATE nnn_content_rating SET rating_sum = rating_sum * (_new_resolution_ / _old_resolution_)** et même pour TABLE nnn_flexicontent_items_extravote, SAUVEGARDER ces 2 tables avant de faire la requête SQL **REMARQUE:** Ceci va faire afficher les évaluations de vote INCORRECTEMENT, non FLEXIcontent. ne changez donc pas cela si vous utilisez des extensions non-FLEXIcontent pour afficher les évaluations _5_ | `text` | — | — |
| **Etoiles de vote résolution &gt;= étoiles**<br />`rating_stars` | Le nombre d'étoiles affichées par Joomla est également de 5. **NOTE :** Doit être : résolution &gt;= étoiles **EXEMPLES:** -- 10 étoiles avec un vote demi étoile, définition de résolution : 20, Étoiles 10 -- 5 étoiles avec vote de quart étoile, résolution réglée : 20, Étoiles : 5 - 10 étoiles avec vote d'une étoile, résolution réglée : 10, étoiles: 10 _5_ | `text` | — | — |

### Note moyenne

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_FIELD_VOTE_SHOW_RATING_LABEL**<br />`main_label_show` | FLEXI_FIELD_VOTE_SHOW_RATING_LABEL_DESC | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Étiquette**<br />`main_label` | Libellé de la note moyenne | `text` | — | `FLEXI_VOTE_AVERAGE_RATING` (Note moyenne) |
| **Texte pour l'Échelle de notation**<br />`rating_texts` | Représentation textuelle de l'échelle de notation. Entrez une liste de chaînes de langue séparée par des virgules. par exemple JVERYPOOR, JPOOR, JFAIR, JBON, JEXCELLENT _Très insuffisant, Insuffisant, Moeyn, Bien, Excellent_ | `textarea` | — | — |
| **Afficher le nombre total de votes**<br />`main_counter` | Afficher le nombre total de votes | `radio` | `0` = Désactiver<br />`1` = Activer | `1` (Activer) |
| **Afficher l'étiquette du compteur**<br />`main_counter_show_label` | Cela va ajouter une étiquette « votes » après le compteur de vote | `radio` | `0` = Désactiver<br />`1` = Activer | `1` (Activer) |
| **Affiche le pourcentage**<br />`main_counter_show_percentage` | Ceci affichera le pourcentage à côté de chaque étiquette de notation | `radio` | `0` = Désactiver<br />`1` = Activer | `0` (Désactiver) |

### Vote composé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`enable_extra_votes` | Activer/désactiver l'affichage des caractéristiques de vote partiel, comme la qualité, la performance, la précision, etc | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Activer dans les vues**<br />`composite_inview` | Vous pouvez activer ou désactiver le paramètre ci-dessus en fonction de la vue active de FLEXIcontent | `fccheckbox` | — | — |
| **Pré-configuration**<br />`extra_votes_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = Charger un exemple | — |
| **Critères de vote**<br />`extra_votes` | Ici, vous pouvez définir les caractéristiques de vote comme par exemple Qualité, Vitesse, Précision, etc ... **Écrire comme**: 1##Quality##Description%% 2##Speed##Description%% 3##Accuracy##Description%% 4##Apparence##Description%% . **NOTE 1**: Les noms seront passés par JText . . pour permettre la prise en charge multilingue (vous pouvez les ajouter à vos fichiers de langue) | `textarea` | — | — |
| **FLEXI_FIELD_VOTE_EXTRA_IN_DISPLAY**<br />`extra_show_in_display` | FLEXI_FIELD_VOTE_EXTRA_IN_DISPLAY_DESC | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

### Paramètres des votes

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nombre total de votes**<br />`extra_counter` | Afficher le nombre total de votes | `radio` | `0` = Désactiver<br />`1` = Activer | `1` (Activer) |
| **Afficher l'étiquette du compteur**<br />`extra_counter_show_label` | Cela va ajouter une étiquette « votes » après le compteur de vote | `radio` | `0` = Désactiver<br />`1` = Activer | `1` (Activer) |
| **Affiche le pourcentage**<br />`extra_counter_show_percentage` | Ceci affichera le pourcentage à côté de chaque étiquette de notation | `radio` | `0` = Désactiver<br />`1` = Activer | `0` (Désactiver) |

#### Avancé

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |
| **Style du bouton bascule**<br />`toggle_style` | — | `multilist` | `0` = BootStrap Toggle<br />`1` = Image Icons<br />`2` = CSS Icons | `0` (BootStrap Toggle) |

#### Accès

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser les invités**<br />`allow_guests_favs` | Activer pour permettre aux invités d'utiliser les favoris | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Informations

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Informations sur le statut**<br />`status_info` | Indique s’il faut afficher un texte supplémentaire sur le statut actuel de l’abonnement | `multilist` | `0` = Icône<br />`1` = Icône + texte | `0` (Icône) |
| **Informations sur le statut**<br />`toggle_info` | Indique s’il faut afficher un court texte sur le statut lorsque l’utilisateur change son statut d’abonnement | `multilist` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |
| **Compteur Utilisateurs**<br />`display_favoured_usercount` | Affiche un le nombre total d'utilisateurs ayant mis ce contenu en favoris | `radio` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |
| **Liste des utilisateurs**<br />`display_favoured_userlist` | Afficher la liste des utilisateurs qui ont l'article dans leurs favoris, il est possible d'afficher leurs identifiants ou leurs noms. | `multilist` | `0` = Cacher<br />`1` = Oui, Identifiants<br />`2` = Ou, Noms | `0` (Cacher) |
| **Nb. maximum d'utilisateurs dans la liste**<br />`display_favoured_max` | Nombre maximum d'utilisateurs à afficher dans la liste | `text` | — | `12` |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Valeurs brutes<br />`2` = Valeurs de rendu | `0` (Non) |

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Liens

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter des liens**<br />`link_to_view` | Lier chaque valeur à sa vue par liste d'articles | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Séparateur de valeurs (vues frontend)**<br />`separatorf` | Choisir le séparateur pour séparer l'ensemble des valeurs dans l'affichage frontend (placé entre les valeurs) | `list` | `0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | `3` (Virgule) |
| **Texte d'ouverture**<br />`opentag` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Champ formulaire

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégorie racine pour les filtres**<br />`rootcatid` | Catégorie racine pour les filtres en frontend. Ce paramétrage affectera les champs filtrables. | `flexicategories` | — | — |
| **Profondeur maximale de l'arbre**<br />`filter_depth` | Profondeur maximale de l'arborescence des sous-catégories | `text` | — | `1` |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable) | `2` |

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégorie racine pour les filtres**<br />`rootcatid_s` | Catégorie racine pour les filtres en frontend. Ce paramétrage affectera les champs filtrables. | `flexicategories` | — | — |
| **Profondeur maximale de l'arbre**<br />`filter_depth_s` | Profondeur maximale de l'arborescence des sous-catégories | `text` | — | `1` |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter_s` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable) | `2` |

## Apparence

### Affichage

:::note
Ceci a un effet si l'affichage de ce champ en l'ajoutant à une position de **champs** de vos mises en page **contenu / catégorie**
:::

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `radio` | `0` = Non<br />`1` = Valeurs brutes<br />`2` = Valeurs de rendu | `0` (Non) |

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Liens

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter des liens**<br />`link_to_view` | Lier chaque valeur à sa vue par liste d'articles | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Séparateur de valeurs (vues frontend)**<br />`separatorf` | Choisir le séparateur pour séparer l'ensemble des valeurs dans l'affichage frontend (placé entre les valeurs) | `list` | `0` = Espace<br />`1` = Saut de ligne<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère) | `3` (Virgule) |
| **Texte d'ouverture**<br />`opentag` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Valeurs

:::note
... si le champ est multiple (Formulaire de contenu) ... et a une apparence de filtre multiple
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Requérir TOUTES les valeurs sélectionnées**<br />`filter_values_require_all` | Habituellement, vous allez inclure des éléments trouvés ayant une des valeurs sélectionnées. -- Vous pouvez sélectionner **pour que toutes les valeurs de filtre** sélectionnées soient correspondantes pour les éléments trouvés. -- **AVERTISSEMENT** aux développeurs de nouveaux types de champs : cela ne fonctionnera pas correctement si votre champ enregistre la valeur du champ SAME plus d'une fois pour le même élément. Donc, dans un tel cas, n'ajoutez pas cette option à votre champ ! | `radio` | `0` = Non<br />`1` = Oui, plus lentement | `0` (Non) |
| **Information pour Requérir AU MOINS UNE / TOUTES**<br />`filter_values_require_all_tip` | choisir de montrer l'information si aucune ou toutes les valeurs de filtre sélectionnées sont requises | `radio` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |

### Champ formulaire

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter_s` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items_s` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values_s` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

## Édition

### Valeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage conditionnel**<br />`showon` | Affiché en fonction de conditions. Utilisez le format Joomla 'fieldname:value' comme par exemple album_type:2 REMARQUE: ne pas définir ce champ en obligatoire. Également DÉSACTIVER les scripts prettyCheckable / Select2 JS dans tous les champs référencés de type select*, checkbox*, radio* | `text` | — | — |
| **Obligatoire**<br />`required` | Définit si le champ doit être obligatoire dans le formulaire de saisie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Validation coté serveur**<br />`validation` | Autoriser l'entrée de balises HTML sûres, OU de texte brut, OU utiliser les filtres texte de Joomla (paramètré par groupe d'utilisateurs dans la configuration globale de Joomla), etc ..., n'autorisez jamais le HTML NON-SÉCURISÉ pour les formulaires publics, mais uniquement pour activer le paramètre'**d'encodage à l'affichage**' | `list` | `2` = Filtrage de texte Joomla (par groupe d'utilisateur)<br />`1` = HTML SÉCURITÉ: retirer tags / attributs dangereux<br />`RAW` = HTML Non sécurisé (HTML brut): ... peut-être: à encoder à l'affichage<br />`STRING` = TEXTE: décoder les entités HTML, enlever les balises HTML<br />`HTML` = TEXTE ou ENCODEAGE HTML : autorisés les entités HTML, enlever les balises | `2` (Filtrage de texte Joomla (par groupe d'utilisateur)) |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Editeur**<br />`hide_html` | Utilser un éditeur html (WYSIWYG) ou un simple textarea | `multilist` | `0` = Editeur HTML<br />`1` = Simple Zone de texte | `0` (Editeur HTML) |

#### Simple Zone de texte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Longueur maximum du texte**<br />`maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | — |
| **Lignes**<br />`rows` | Nombre de lignes | `text` | — | `6` |
| **Colonnes**<br />`cols` | Nombre de colonnes | `text` | — | `80` |

#### Editeur HTML

:::note
Certains de ces paramètres existent également dans le formulaire de configuration du type !
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Largeur de l'éditeur**<br />`width` | Largeur de l'éditeur html | `text` | — | — |
| **Hauteur de l'éditeur**<br />`height` | Définit la hauteur de l'éditeur HTML | `text` | — | — |
| **Editeur HTML**<br />`editor` | Utilise l'éditeur HTML par défaut paramétré dans Joomla pour modifier les valeurs du champ | `plugins` | `—` = Par défaut de Joomla! | — |

#### Boutons de l'éditeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher**<br />`show_buttons` | Vous pouvez désactiver les boutons de l'éditeur (plugins editors-xtd) | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Cacher les boutons (pour certains éditeurs*)**<br />`skip_buttons` | Sélectionner les boutons à désactiver. Remarque : ne fonctionne pas dans tous les éditeurs. Suporté par tinyMCE et JCE, peut être pour d'autres | `pluginlist` | — | — |

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
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `multilist` | `0` = Non<br />`1` = Valeurs brutes<br />`2` = Valeurs de rendu | `0` (Non) |
| **Supprimer html**<br />`csv_strip_html` | — | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Valeur

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Vue Catégorie

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Supprimer HTML & tronquer le texte**<br />`cut_text_catview` | Supprimer les balises HTML du texte et les tronque en fonction de la longueur maximum. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Limite de caractères**<br />`cut_text_length_catview` | Tous les caractères dépassant la limite (commençant par le mot suivant) seront coupés | `text` | — | `200` |
| **Afficher tout le texte**<br />`cut_text_display_catview` | Activer cette option pour afficher tout le texte | `multilist` | `0` = Non<br />`1` = En ligne<br />`2` = Fenêtre Popup | `0` (Non) |
| **Icône du Bouton**<br />`cut_text_display_btn_icon_catview` | — | `text` | — | `icon-paragraph-center` |
| **Texte du bouton**<br />`cut_text_display_btn_text_catview` | — | `text` | — | — |

## Réseaux sociaux

### Prise en charge des réseaux sociaux (ex. Facebook)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Suggérer le champ aux listes**<br />`useogp` | Intégrer le champ texte dans l'Open Graph (og:description ou og:title) | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Longueur maximum du texte**<br />`ogpmaxlen` | Saisir le nombre maximum de caractères à utiliser avant d'être tronqué. | `text` | — | `300` |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

### Champ formulaire

#### Vue recherche avancée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `list` | `1` = Texte à Rechercher | `0` |

## Onglets (RegEx)

Diviser la zone de texte en onglets à l’aide d’une expression régulière

### Execution de plugin joomla dans les onglets

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`editorarea_per_tab` | Activer pour tenter d’identifier les onglets via des expressions régulières | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Expression régulière

#### Modèles Tabset

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Initialisation d'onglets**<br />`start_of_tabs_pattern` | Expression régulière pour le code des plugin | `text` | — | — |
| **Fin d'onglets**<br />`end_of_tabs_pattern` | Expression régulière pour le code des plugin | `text` | — | — |

#### Modèle d'onglet

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Début d'onglet**<br />`start_of_tab_pattern` | Expression régulière pour le code des plugin | `text` | — | — |
| **Fin d'onglet**<br />`end_of_tab_pattern` | Expression régulière pour le code des plugin | `text` | — | — |

:::note
Texte pour le départ de l'onglet
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Titre des onglets**<br />`title_tab_pattern` | Le titre doit être à l'intérieur de l'initialisation des onglets, il s'agit d'une expression régulière qui doit être à l'intérieur du titre | `text` | — | — |

#### Zones supplémentaires de l’éditeur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Avant les onglets**<br />`force_beforetabs` | Ajouter une zone d’édition supplémentaire | `multilist` | `0` = Auto<br />`1` = Toujours | `1` (Toujours) |
| **Après les onglets**<br />`force_aftertabs` | Ajouter une zone d’édition supplémentaire | `multilist` | `0` = Auto<br />`1` = Toujours | `1` (Toujours) |
| **Code d'onglet éditable**<br />`allow_tabs_code_editing` | Cette option permet d'éditer le code dans les onglet depuis le formulaire de saisie | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
