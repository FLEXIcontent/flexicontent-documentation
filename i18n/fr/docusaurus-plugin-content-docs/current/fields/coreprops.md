---
sidebar_position: 13
---

# Propriété cœur

Plugin de placement des propriétés cœur du formulaire de contenu pour FLEXIcontent. Ce champ définit l’emplacement de la propriété cœur dans le formulaire, en l’ordonnançant dans le gestionnaire de champs lorsque le filtre par type de contenu est actif

*Plugin : `coreprops` — Propriété cœur*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/coreprops/coreprops.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Type propriété

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type propriété**<br />`props_type` | Sélectionnez la propriété système ou le groupe de propriétés systèmes (normalement ils apparaîtront dans un onglet par défaut) que vous voulez placer dans le formulaire. | `multilist` | **Propriétés Basique ou Simple**<br />`id` = Identifiant<br />`alias` = Alias<br />`category` = Catégorie (principale)<br />`lang` = Langue<br />`vstate` = Publier les modifications<br />`disable_comments` = Interdire les commentaires<br />`notify_subscribers` = Notification abonnés<br />`notify_owner` = Notifier le propriétaire<br />`captcha` = Captcha<br />`layout_selection` = Sélecteur de mises en page<br />**Propriétés de publication**<br />`timezone_info` = Information fuseau horaire<br />`created_by_alias` = Alias d'auteur<br />`publish_up` = Date de publication<br />`publish_down` = Date de dé-publication<br />`access` = Accès<br />**Propriété groupes**<br />`item_screen` = Informations de version<br />`lang_assocs` = Associations de langue<br />`jimages` = JImages<br />`jurls` = JUrls<br />`metadata` = Méta données<br />`seoconf` = Configuration SEO<br />`display_params` = Paramètres d'affichage<br />`layout_params` = Paramètres de mise en page<br />`perms` = Gestion des droits<br />`versions` = Versions<br />**Déprécié (héritage)**<br />`language` = Langue et associations | — |

## Édition

#### Formulaire de contenu en partie publique seulement Permet de définir un emplacement spécifique pour le champ core sélectionné via l'ordre défini dans le gestionnaire de champs

#### Pour le placement : titre, État, créé, créer par, modifier, modifier par, veuillez utiliser les champs CORE existants

## Apparence

#### Apparence

### Basique

#### Affichage

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher pour les clients**<br />`show_in_clients` | Sélectionner si le champ sera créé et affiché à des clients spécifiques | `fccheckbox` | — | — |
| **Afficher dans les vues**<br />`show_in_views` | Sélectionner si le champ sera créé et affiché en fonction d'une vue spécifique | `fccheckbox` | — | — |

#### Libellé et accès

#### REMARQUE : - les champs affichables sont : langue, alias, catégorie principale, accès, - pour afficher « publish_up » et « publish_down », utilisez un champ Date dans le mode approprié

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Montrer un message d'**accès interdit****<br />`show_acc_msg` | Si le champ est inaccessible, une message de non-accès s'affichera. **NOTE : ** SI ce paramètre est désactivé, le champ sera invisible aux utilisateurs sans accès, sans aucun message ou avertissement indiquant son existance | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Message **accès interdit****<br />`no_acc_msg` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Exporter

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `multilist` | `0` = Non<br />`1` = Valeurs brutes<br />`2` = Valeurs de rendu | `0` (Non) |
| **Supprimer html**<br />`csv_strip_html` | — | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Catégorie (principale)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter des liens**<br />`link_maincat` | Lier chaque valeur à sa vue par liste d'articles | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### FLEXI_BACKEND_VIEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_BACKEND_VIEW_APPEARANCE**<br />`backend_view_appearance` | FLEXI_BACKEND_VIEW_APPEARANCE_DESC | `multilist` | `0` = Par défaut<br />`1` = FLEXI_CHECK_MARK<br />`2` = FLEXI_CLEAN_HTML_AND_TRIM | `0` (Par défaut) |
| **FLEXI_TRIM_LENGTH**<br />`backend_view_trim_chars` | FLEXI_TRIM_LENGTH_DESC | `text` | — | `100` |

### Liste Valeurs

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pré-configuration**<br />`prx_sfx_open_close_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Séparateur de valeurs (vues frontend)**<br />`separatorf` | Choisir le séparateur pour séparer l'ensemble des valeurs dans l'affichage frontend (placé entre les valeurs) | `multilist` | `0` = Espace<br />`1` = Saut de ligne<br />`6` = Ligne Horizontale<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère)<br />`7` = Séparateur personnalisé | `1` (Saut de ligne) |
| **Séparateur personnalisé**<br />`separatorf_custom` | — | `text` | — | — |
| **Texte d'ouverture**<br />`opentag` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

#### Apparence

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

#### Filtrer

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ordre des valeurs de filtrage**<br />`reverse_filter_order` | Activer pour afficher les valeurs de filtre dans l'ordre inverse. NOTE : dans le cas de l'affichage de la plage du slider, la poignée de gauche sera le maximum, et la poignée de droite sera le minimum | `radio` | `0` = Normal<br />`1` = Inverse | `0` (Normal) |

#### Comparaison des valeurs de filtre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comparaison des valeurs de filtre**<br />`filter_compare_type` | Valeurs de filtrage qui peuvent être comparées de manière alphanumérique ou numérique (entier / à virgule flottante) | `radio` | `0` = Alphanumérique<br />`1` = Entier<br />`2` = Virgule flottante | `0` (Alphanumérique) |

:::note
... si le champ est multiple (Formulaire de contenu) ... et a une apparence de filtre multiple
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Requérir TOUTES les valeurs sélectionnées**<br />`filter_values_require_all` | Habituellement, vous allez inclure des éléments trouvés ayant une des valeurs sélectionnées. -- Vous pouvez sélectionner **pour que toutes les valeurs de filtre** sélectionnées soient correspondantes pour les éléments trouvés. -- **AVERTISSEMENT** aux développeurs de nouveaux types de champs : cela ne fonctionnera pas correctement si votre champ enregistre la valeur du champ SAME plus d'une fois pour le même élément. Donc, dans un tel cas, n'ajoutez pas cette option à votre champ ! | `radio` | `0` = Non<br />`1` = Oui, plus lentement | `0` (Non) |
| **Information pour Requérir AU MOINS UNE / TOUTES**<br />`filter_values_require_all_tip` | choisir de montrer l'information si aucune ou toutes les valeurs de filtre sélectionnées sont requises | `radio` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |

### Vue Catégorie

#### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |

:::note
Notez que certaines propriétés cœur ne prennent en charge que des affichages spécifiques, par exemple uniquement le champ de texte
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Recherche texte (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
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
| **Valeurs personnalisées**<br />`slider_custom_range` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': '50', '50%': '150', '75%': '600', 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_50 ## label_150 ## label_600 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Préfixe / Suffixe

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_filter` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_filter` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Texte d'ouverture**<br />`opentag_filter` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_filter` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

### Vue recherche avancée

#### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |

:::note
Notez que certaines propriétés cœur ne prennent en charge que des affichages spécifiques, par exemple uniquement le champ de texte
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Recherche texte (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
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
| **Valeurs personnalisées**<br />`slider_custom_range_s` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': 500, '50%': 2000, '75%': 10000, 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels_s` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_500 ## label_2000 ## label_10000 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext_s` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Préfixe / Suffixe

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_filter_s` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_filter_s` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Texte d'ouverture**<br />`opentag_filter_s` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_filter_s` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

#### Filtrer
