---
sidebar_position: 2
---

# Options (configuration générale)

L’écran **Options** est la page de configuration principale de FLEXIcontent. Il s’ouvre depuis **Composants → FLEXIcontent → Options** dans l’administration Joomla!.

Il est organisé en trois sous-onglets :

| Onglet | Contenu |
| --- | --- |
| Général | Recherche textuelle, multilingue, appareils mobiles |
| Styles CSS | Hauteurs des éléments de formulaire, rechargement de page |
| Avancé | Frameworks navigateur, performances, utilisation / débogage |

:::info Source
Cette page est générée à partir de `admin/config.xml` (fieldset `component`) et du fichier `en-GB.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

## Général

### Recherche textuelle

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Journaliser les recherches**<br />`log_search_queries` | Enregistrer les requêtes saisies dans le module de recherche et la page de recherche FLEXIcontent, avec un compteur par requête. La liste est disponible via le bouton « Journaux de recherche » du tableau de bord FLEXIcontent. | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Rechercher les mots courts / courants**<br />`add_search_prefix` | Activez cette option pour inclure les mots courts ou très courants dans la recherche textuelle. | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Langues sans espaces**<br />`filter_word_like_any` | Cette option peut être nécessaire si votre site contient des contenus en langues asiatiques sans espaces entre les mots (chinois, japonais, thaï). | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Pertinence en premier**<br />`filter_word_relevance_order` | Lors d’une recherche textuelle, afficher d’abord les résultats les plus pertinents. Par défaut, seul le titre est pris en compte. | `0` = Utiliser uniquement l’ordre configuré<br />`1` = Titre pertinent<br />`2` = Oui | `0` (Utiliser uniquement l’ordre configuré) |
| **Priorité par champ**<br />`filter_word_field_priority` | Uniquement pour l’index de recherche avancé. Ajoutez les types de champs et réordonnez-les par glisser-déposer pour définir la priorité : les contenus contenant les mots recherchés dans le premier type de champ apparaissent en premier, puis ceux correspondant au deuxième, etc. Les mots-clés d’étiquettes appartiennent au champ Étiquettes. Vide = aucune priorité. | `title` = Titre<br />`categories` = Catégories<br />`tags` = Étiquettes | — |
| **Auto-complétion : lignes d’index à analyser**<br />`search_autocomplete_scan` | Nombre de lignes de l’index de recherche examinées pour collecter les suggestions de mots dans l’auto-complétion simple. Une valeur plus élevée donne plus de suggestions (et plus variées) sur les grands sites, mais est plus lente. Par défaut 300. | — | `300` |
| **Auto-complétion : nombre max. de suggestions**<br />`search_autocomplete_limit` | Nombre maximum de suggestions de mots affichées par l’auto-complétion simple. Par défaut 10. | — | `10` |
| **Auto-complétion : suggestions et ordre**<br />`search_autocomplete_sources` | Uniquement pour l’auto-complétion simple (pas celle de type Étiquettes). Ajoutez les types de suggestions et réordonnez-les par glisser-déposer : mots de l’index de recherche, titres de contenus, étiquettes et catégories (seuls les contenus accessibles à l’utilisateur courant). | `words` = Mots<br />`titles` = Titres<br />`tags` = Étiquettes<br />`categories` = Catégories<br />`fields` = Valeurs des champs texte<br />`metakeys` = Mots-clés meta des contenus | — |
| **Auto-complétion : max. titres / étiquettes / catégories**<br />`search_autocomplete_titles_limit` | Nombre maximum de suggestions de chacun de ces types (titres, étiquettes, catégories) affichées par l’auto-complétion simple. Par défaut 5. | — | `5` |
| **Auto-complétion : max. valeurs de champs texte / mots-clés meta**<br />`search_autocomplete_fields_limit` | Nombre maximum de suggestions de valeurs de champs texte (champs texte recherchables ou en recherche avancée) affichées par l’auto-complétion simple (également la limite des phrases de mots-clés meta des contenus). Par défaut 3. | — | `3` |

### Multilingue

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Méthode de traduction**<br />`flexi_fish` | Les traductions natives traduisent entièrement les contenus (TOUS les champs) en associant plusieurs contenus de langues différentes qui traduisent le même contenu. Si vous utilisez l’option Falang (contenu unique), les champs personnalisés ne peuvent pas être traduits. | `0` = Natif<br />`1` = Natif et Falang | `0` (Natif) |
| **Modifier en ligne**<br />`editjf_translations` | Vous pouvez modifier les traductions Falang des contenus via le formulaire d’édition de contenu. **REMARQUE :** (a) cela permet de modifier les champs : titre, alias, description, metadesc, metakey (les autres champs Falang comme les attributs et publish_up/publish_down seront forcés aux valeurs communes). (b) Un avertissement s’affiche si vous désactivez cette option alors que des traductions Falang sont détectées. Il est recommandé d’utiliser la méthode de traduction native pour les contenus et Falang pour les autres parties du site. | `0` = Non<br />`1` = Non, désactiver l’avertissement<br />`2` = Oui | `0` (Non) |

### Appareils mobiles

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser les modèles mobiles**<br />`use_mobile_layouts` | Activez cette option pour utiliser les modèles mobiles dans les vues contenu et liste de contenus FLEXIcontent. **REMARQUE :** dans les champs, les paramètres mobiles sont toujours utilisés. | `0` = Non, uniquement dans les champs<br />`1` = Oui | `0` (Non, uniquement dans les champs) |
| **Forcer la mise en page bureau**<br />`force_desktop_layout` | Utile pour **exclure les tablettes** de l’utilisation de la mise en page mobile. Les tablettes ont généralement à la fois un grand écran et une résolution suffisante (au moins 800x480). Vous devez disposer de mises en page bureau avec un design responsive qui fonctionne bien à 800x480 ou plus. | `0` = Jamais<br />`1` = Tablette détectée | `0` (Jamais) |
| **Débogage de la détection et de l’état**<br />`debug_mobile` | Affiche les messages de détection ou d’état concernant la détection et l’utilisation mobiles. | `0` = Non<br />`1` = Oui | `0` (Non) |

## Styles CSS

### CSS

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Éléments de formulaire**<br />`form-inp-height` | Définir la hauteur des éléments de formulaire dans les formulaires d’édition des contenus. | — | `36` |
| **Contrôles de formulaire**<br />`ctrls-inp-height` | Définir la hauteur des contrôles de formulaire comme les boutons de réordonnancement, d’ajout et de suppression dans les formulaires d’édition. | — | `36` |
| **Filtres de champs (frontend)**<br />`filts-inp-height` | Définir la hauteur des filtres de champs dans les vues frontend. | — | `36` |
| **Éléments des gestionnaires**<br />`fcman-inp-height` | Définir la hauteur des éléments dans les vues de gestion : barres de recherche textuelle, filtres et boutons d’action (dans les lignes de contenus). | — | `32` |

### Rechargement de page

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer le rechargement de page**<br />`page_reloading_enable` | Activer le rechargement de page lors de l’application de filtres (frontend / backend). Peut également être utilisé dans d’autres cas. | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Arrière-plan**<br />`page_reloading_overlay_bg_color` | Couleur de fond du calque affiché pendant le rechargement. | — | `rgba(0, 0, 0, 0.3)` |
| **Couleur du texte**<br />`page_reloading_content_color` | Couleur du texte affiché pendant le rechargement. | — | `rgba(0, 0, 0, 1)` |
| **Arrière-plan**<br />`page_reloading_content_bg_color` | Couleur de fond du bloc de texte affiché pendant le rechargement. | — | `rgba(255, 255, 255, 1)` |
| **Image**<br />`page_reloading_logo_imgsrc` | Logo affiché pendant le rechargement. | — | — |
| **Opacité**<br />`page_reloading_logo_opacity` | Opacité du logo (0 à 100). | — | `100` |
| **Activer**<br />`page_reloading_mssg_display` | Afficher un message personnalisé pendant le rechargement. Peut être une chaîne de langue. | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Texte personnalisé**<br />`page_reloading_mssg_text` | Texte du message affiché pendant le rechargement. | — | — |
| **Activer**<br />`page_reloading_pbar_display` | Afficher une barre de progression pendant le rechargement. | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Couleur**<br />`page_reloading_pbar_color` | Couleur de la barre de progression. | — | `rgba(0, 153, 255, 1)` |

## Avancé

### Frameworks et bibliothèques du navigateur

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Charger le CSS de FLEXIcontent**<br />`disablecss` | Ne pas charger le fichier CSS par défaut de FLEXIcontent (flexicontent.css). Non recommandé aux designers débutants. **REMARQUE :** les modules ont besoin de ce fichier et le chargent, ainsi que leur CSS spécifique, car ils peuvent apparaître dans des vues non-FLEXIcontent. Un paramètre par module permet de désactiver le chargement des fichiers CSS. | `0` = Les deux<br />`1` = Désactiver en frontend | `0` (Les deux) |
| **Charger le JS des infobulles**<br />`add_tooltips` | Charger le JavaScript des infobulles pour afficher de belles infobulles en frontend. **REMARQUE :** les vues frontend utilisant les favoris ou le champ de vote (et peut-être d’autres champs) peuvent ignorer ce paramètre et forcer le chargement des infobulles. | `1` = Les deux<br />`0` = Désactiver en frontend | `1` (Les deux) |
| **jQuery**<br />`loadfw_jquery` | Certaines bibliothèques peuvent être désactivées, d’autres sont toujours nécessaires. Normalement, laissez tout activé. **REMARQUE :** si vous choisissez un chargement manuel en frontend, assurez-vous que la bibliothèque est chargée par une extension tierce, par exemple dans votre template Joomla. Sans les frameworks nécessaires, le comportement et l’apparence des formulaires frontend (surtout le formulaire de contenu) seront cassés. | `1` = Les deux<br />`2` = Manuellement en frontend | `1` (Les deux) |
| **Thème jQuery UI**<br />`jquery_ui_theme` | Thème utilisé pour les éléments d’interface jQuery UI. | `ui-lightness` = ui-lightness<br />`smoothness` = smoothness | `ui-lightness` (ui-lightness) |
| **image-picker**<br />`loadfw_image_picker` | Certaines bibliothèques peuvent être désactivées, d’autres sont toujours nécessaires. Normalement, laissez tout activé. **REMARQUE :** si vous choisissez un chargement manuel en frontend, assurez-vous que la bibliothèque est chargée par une extension tierce, par exemple dans votre template Joomla. Sans les frameworks nécessaires, le comportement et l’apparence des formulaires frontend (surtout le formulaire de contenu) seront cassés. | `1` = Les deux<br />`2` = Manuellement en frontend | `1` (Les deux) |
| **masonry**<br />`loadfw_masonry` | Certaines bibliothèques peuvent être désactivées, d’autres sont toujours nécessaires. Normalement, laissez tout activé. **REMARQUE :** si vous choisissez un chargement manuel en frontend, assurez-vous que la bibliothèque est chargée par une extension tierce, par exemple dans votre template Joomla. Sans les frameworks nécessaires, le comportement et l’apparence des formulaires frontend (surtout le formulaire de contenu) seront cassés. | `1` = Les deux<br />`2` = Manuellement en frontend | `1` (Les deux) |
| **inputmask**<br />`loadfw_inputmask` | Certaines bibliothèques peuvent être désactivées, d’autres sont toujours nécessaires. Normalement, laissez tout activé. **REMARQUE :** si vous choisissez un chargement manuel en frontend, assurez-vous que la bibliothèque est chargée par une extension tierce, par exemple dans votre template Joomla. Sans les frameworks nécessaires, le comportement et l’apparence des formulaires frontend (surtout le formulaire de contenu) seront cassés. | `1` = Les deux<br />`2` = Manuellement en frontend | `1` (Les deux) |
| **prettyCheckable**<br />`loadfw_prettycheckable` | Certaines bibliothèques peuvent être désactivées, d’autres sont toujours nécessaires. Normalement, laissez tout activé. **REMARQUE :** si vous choisissez un chargement manuel en frontend, assurez-vous que la bibliothèque est chargée par une extension tierce, par exemple dans votre template Joomla. Sans les frameworks nécessaires, le comportement et l’apparence des formulaires frontend (surtout le formulaire de contenu) seront cassés. | `1` = Les deux<br />`2` = Manuellement en frontend<br />`0` = Non | `1` (Les deux) |
| **fancybox**<br />`loadfw_fancybox` | Certaines bibliothèques peuvent être désactivées, d’autres sont toujours nécessaires. Normalement, laissez tout activé. **REMARQUE :** si vous choisissez un chargement manuel en frontend, assurez-vous que la bibliothèque est chargée par une extension tierce, par exemple dans votre template Joomla. Sans les frameworks nécessaires, le comportement et l’apparence des formulaires frontend (surtout le formulaire de contenu) seront cassés. | `1` = Les deux<br />`2` = Manuellement en frontend | `1` (Les deux) |
| **bootstrap.css**<br />`loadfw_bootstrap_css` | Certaines bibliothèques peuvent être désactivées, d’autres sont toujours nécessaires. Normalement, laissez tout activé. **REMARQUE :** si vous choisissez un chargement manuel en frontend, assurez-vous que la bibliothèque est chargée par une extension tierce, par exemple dans votre template Joomla. Sans les frameworks nécessaires, le comportement et l’apparence des formulaires frontend (surtout le formulaire de contenu) seront cassés. | `1` = Frontend<br />`2` = Manuellement en frontend | `2` (Manuellement en frontend) |
| **icomoon.css**<br />`loadfw_icomoon_css` | Certaines bibliothèques peuvent être désactivées, d’autres sont toujours nécessaires. Normalement, laissez tout activé. **REMARQUE :** si vous choisissez un chargement manuel en frontend, assurez-vous que la bibliothèque est chargée par une extension tierce, par exemple dans votre template Joomla. Sans les frameworks nécessaires, le comportement et l’apparence des formulaires frontend (surtout le formulaire de contenu) seront cassés. | `1` = Frontend<br />`2` = Manuellement en frontend | `2` (Manuellement en frontend) |
| **Charger en frontend**<br />`loadfw_select2` | Charger les contrôles de choix (Choice) en frontend. Choisissez « Manuellement en frontend » si votre template charge la bibliothèque. Les listes déroulantes natives restent disponibles sans la bibliothèque. | `1` = Les deux<br />`2` = Manuellement en frontend | `1` (Les deux) |

### Performances

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Toujours générer le HTML des champs**<br />`always_create_fields_display` | Il est fortement recommandé de conserver « Uniquement lorsque nécessaire », afin que le système ne génère les champs que s’ils sont affichés. En cas de problème de compatibilité (champs non affichés), essayez d’activer cette option. | `1` = Toujours (non recommandé)<br />`0` = Uniquement lorsque nécessaire (recommandé)<br />`2` = Uniquement en vue contenu<br />`3` = Jamais sauf dans une position de modèle | `0` (Uniquement lorsque nécessaire (recommandé)) |
| **Cache des données**<br />`advcache` | Cette option est fortement recommandée sur les sites en production. Elle augmente sensiblement les performances. Elle concerne les structures de données internes de FLEXIcontent, comme les données des filtres de champs et des catégories. | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Durée du cache**<br />`advcache_time` | Délai avant la régénération automatique du cache des contenus. Par défaut une heure (3600 secondes). | — | `3600` |
| **Recompiler le LESS du cœur**<br />`recompile_core_less` | Activez uniquement si vous contribuez au projet et avez modifié les fichiers LESS du cœur. Cela ajoute un léger délai à toutes les vues et doit être désactivé en production (la recompilation peut parfois échouer). | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Compresser le CSS compilé (LESS)**<br />`compress_core_less` | Compresser la sortie CSS lors de la compilation des fichiers LESS. Recommandé en production. À désactiver uniquement pour le débogage. | `0` = Non<br />`1` = Oui | `0` (Non) |

### Utilisation / débogage

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Afficher les statistiques de performance**<br />`print_logging_info` | Afficher les statistiques de performance et autres informations d’exécution. | `0` = Non<br />`2` = Oui<br />`1` = Variable URL : fcdebug=1 | `0` (Non) |
| **Afficher les notices d’utilisabilité**<br />`show_usability_messages` | Afficher les messages importants d’utilisabilité une fois par session de connexion, en haut des zones de gestion (contenus, champs, etc.). | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Déboguer la création initiale des permissions**<br />`debug_initial_perms` | Afficher les messages de journalisation et les avertissements du processus initial de vérification et de création des permissions. | `0` = Non<br />`1` = Oui | `0` (Non) |
