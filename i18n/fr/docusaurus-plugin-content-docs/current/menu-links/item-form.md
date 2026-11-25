---
sidebar_position: 10
---

# Formulaire de soumission



:::info Source
Cette page est générée depuis `site/views/item/tmpl/form.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Paramètres requis

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Par type**<br />`typeid` | Imposez un type de contenu spécifique, ou laisser l'utilisateur choisir parmi les types de contenus autorisés (les autorisations sont données via le paramètre 'créer contenus' au niveau du type) | `types` | — | — |

:::note
**NOTE**: afin de configurer le formulaire de soumission/modification d'élément, utiliser : -- Configuration du formulaire dans le type de composant et de contenu, -- 'Créer' / 'Modifier' ACL pour les catégories et types, etc -- Limites de l'Auteur/Groupe d'utilisateurs, etc Activer/utiliser les paramètres dans ce lien de menu uniquement si nécessaire, -- la configuration ci-dessus mentionnée et **ACL** doivent être vérifiées et configurées **de toute façon**
:::

## Paramétrage du formulaire

(Affecte seulement la soumission initiale)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Apparence du formulaire de saisie**<br />`form_ilayout_fe` | — | `fclayout` | **Dispositions intégrées**<br />`tabs` = onglets (par défaut)<br />`flat` = plat | — |

### Paramétrage du formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Boutons optionnels**<br />`allowbuttons_fe` | Sélectionner les boutons que vous souhaitez faire apparaitre dans le formulaire de saisie en frontend. | `fccheckbox` | — | — |
| **Placement des boutons**<br />`buttons_placement_fe` | Selectionner pour afficher des boutons de formulaire en haut ou en bas du formulaire | `radio` | `—` = Paramètres globaux<br />`0` = En haut<br />`1` = En bas<br />`2` = A gauche<br />`3` = A droite | — |

#### Affiche un message du type approbation nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Dans le formulaire**<br />`approval_warning_inform_fe` | Activez ceci, pour afficher un message dans le formulaire de l'élément, si l'utilisateur actuel peut publier de nouveaux éléments ou s'il peut auto-approuver les modifications aux éléments existants | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Après la soumission du formulaire**<br />`approval_warning_aftersubmit_fe` | Activez ceci, pour afficher un avertissement après l'envoi du formulaire, en disant si l'approbation est nécessaire pour que le nouvel élément soit publié ou pour que les modifications de l'élément existant deviennent actives | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |

:::note
Si vous laissez ces champs vides, vérifiez les valeurs par défaut dans la configuration du type de contenu
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nécessite une révision de cette version**<br />`version_reviewal_msg_fe` | _Veuillez noter que la **version** de votre document devra être validée par un administrateur_ | `textarea` | — | — |
| **Nécessite l'approbation du contenu**<br />`document_approval_msg_fe` | _Veuillez noter que votre **nouvel article** devra être relu et accepté par un administrateur_ | `textarea` | — | — |
| **Peut nécessiter une révision de cette version**<br />`mr_version_revial_msg_fe` | _Veuillez noter que la nouvelle **version** de ce document a peut-être besoin d'être vérifiée et approuvée avant publication. Cela peut dépendre de la catégorie du contenu et / ou du type du contenu. Si l'approbation est nécessaire, vous serez avisé après avoir enregistré ce contenu._ | `textarea` | — | — |
| **Peut nécessiter l'approbation du contenu**<br />`mr_document_approval_msg_fe` | _Veuillez noter que votre nouveau contenu peut nécessiter une approbation avant d'être accepté. Cela peut dépendre de catégorie du contenu et/ou de type de contenu. Vous serez avisé si l'approbation est nécessaire, après avoir enregistré ce contenu._ | `textarea` | — | — |
| **Modifications appliquées immédiatement**<br />`changes_applied_immediately_msg_fe` | _Veuillez noter que la gestion des versions de document est désactivée, donc toute modification que vous apportez à ce contenu sera accepté/activé immédiatement et la version précédente sera perdue_ | `textarea` | — | — |

#### Instructions / redirections d'URL / etc

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Instructions pour la saisie**<br />`submit_message` | Ces instructions seront placées en haut du formulaire, après les boutons **NOTE **: Cela peut être une chaîne de langue (à ajouter à vos fichiers de langue) | `textarea` | — | — |
| **Redirection URL après la soumission cache le bouton Aperçu**<br />`submit_redirect_url_fe` | Vous pouvez définir une URL personnalisée vers laquelle l'utilisateur sera redirigé après avoir soumis un nouveau contenu. **NOTE :** Cela fonctionnera même si vous cliquez sur les boutons 'Ajouter' ou 'Appliquer' avant de fermer l'élément **Remarque :** Définir ceci masquera le bouton d'aperçu lors de l'envoi de nouveaux éléments | `text` | — | — |
| **Page d'accès non autorisé (saisir un contenu)**<br />`notauthurl` | Spécifiez l'URL / ID du lien de menu de la page vers laquelle vous souhaitez que vos visiteurs / utilisateurs soient dirigés s'ils n'ont pas les droits suffisants pour créer plus de contenu (ou aucun). Cela pourrait être (par exemple) la page des plans d'abonnement si vous vendez votre espace de publication. **NOTE :** Si vous ne définissez rien ici, la page générale non autorisé sera utilisée. | `menuitem` | — | — |

#### Formulaire de sécurité critères d'affichage pour CAPTCHA

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser les captcha**<br />`use_captcha` | Choisir à quel moment afficher un champ captcha pour protéger le formulaire des robots | `multilist` | `—` = Paramètres globaux<br />`0` = Désactiver<br />`1` = Invités (Recommandé)<br />`2` = Tous les utilisateurs | — |
| **Plugin de Captcha**<br />`captcha` | Choisir un plugin spécifique de captcha pour surcharger le paramètre par défaut | `plugins` | `—` = Paramètres globaux<br />`0` = Désactiver | — |

## Donnée de formulaire optionnelle

(Affecte seulement la soumission initiale)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Images intro / complètes**<br />`use_jimages_fe` | Afficher les images intro/complètes | `radio` | `—` = Par défaut de Joomla!<br />`0` = Désactiver<br />`1` = Activer | — |
| **URL**<br />`use_jurls_fe` | Afficher les URL | `radio` | `—` = Par défaut de Joomla!<br />`0` = Désactiver<br />`1` = Activer | — |

### Édition de base

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le titre**<br />`usetitle_fe` | Sélectionnez pour afficher ou masquer le titre de l'élément - vous pouvez définir automatiquement dans les paramètres de type | `radio` | `—` = Paramètres globaux<br />`0` = Cacher si automatique<br />`1` = Oui | — |
| **Utiliser les Alias**<br />`usealias_fe` | Autoriser l'utilisateur à saisir les alias. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser le type**<br />`usetype_fe` | Afficher le sélecteur de type pour permettre le changement de type d'élément | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser l'état**<br />`usestate_fe` | Afficher le sélecteur d'état pour permettre le changement d'état de publication du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser l'accès**<br />`useaccess_fe` | Afficher le sélecteur d'accès pour permettre de changer le niveau d'accès du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser les vedettes**<br />`usefeatured_fe` | Afficher le sélecteur de vedette pour permettre le changement d'état du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser les tags**<br />`usetags_fe` | Autoriser les tags a être cachés, pour les groupes qui possèdent le droit sur les tags, cela n'empêche pas après de gérer les tags | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui<br />`2` = Afficher seulement | — |
| **Autoriser la désactivation des commentaires**<br />`allowdisablingcomments_fe` | Vous pouvez préciser ici si les auteurs ou les éditeurs peuvent désactiver les commentaires pour le contenu qu'ils modifient ou ajoutent. Si vous autorisez ce paramètre, il est recommandé de ne pas afficher les paramètres avancés du contenu. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

#### Catégories

:::note
Remarque : Vous avez toujours besoin des **ACL** pour éviter les changements de catégories multiples. Cacher ces dernières, n'empêche pas les utilisateurs de les modifier ...
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser la catégorie**<br />`usemaincat_fe` | Si vous désactivez cette option, vous devez également définir une catégorie par défaut dans la configuration de chaque type (généralement vous allez créer une catégorie avec le même nom que le type et la définir comme par défaut) | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Catégories secondaires**<br />`show_seccats_fe` | — | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Cacher si non modifiable<br />`2` = Montrer | — |
| **Catégories en vedette**<br />`show_featcats_fe` | — | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Cacher si non modifiable<br />`2` = Montrer | — |

#### Langue

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le langage**<br />`uselang_fe` | Autoriser l'utilisateur à choisir sa langue. NOTE : Sélectionnez une langue par défaut avant de désactiver ce paramètre | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui<br />`3` = Oui, sans associations<br />`2` = Afficher seulement | — |
| **Langue par défaut**<br />`default_language_fe` | C'est la langue qui sera pré-sélectionnée, particulièrement utile si vous cachez la langue | `fclanguage` | `_author_lang_` = Utiliser la langue de l'éditeur<br />`_site_default_` = Utiliser la langue par défaut du site | — |
| **Désactiver les langues**<br />`disable_languages_fe` | Par exemple, vous pourriez choisir de désactiver la langue 'ALL' | `fclanguage` | — | — |

#### Sélecteur de langue

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher comme**<br />`langdisplay_fe` | Vous pouvez l'afficher ex comme une liste déroulante ou des boutons radios | `radio` | `—` = Paramètres globaux<br />`2` = Sélecteur liste déroulante<br />`3` = Bouton radio | — |
| **Afficher drapeaux (radio)**<br />`langdisplay_flags_fe` | Afficher les icônes drapeaux | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Montrer le texte (radio)**<br />`langdisplay_texts_fe` | Activer pour afficher le texte comme un code langue | `radio` | `—` = Paramètres globaux<br />`0` = Pas de texte<br />`1` = Code de la langue<br />`2` = Titre<br />`3` = Titre natif<br />`4` = Titre + Titre natif | — |

### Options avancées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser les détails de publication**<br />`usepublicationdetails_fe` | Sélectionnez ici pour autoriser : -Basic- Publication Details: (début & date de fin de publication & alias d'auteur) aux personnes qui peuvent -EDITER- l'élément. ou - Tous les détails de la publication : (auteur de l'élément & date de création) sont disponibles UNIQUEMENT aux utilisateurs de Super Admin. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Basique (recommandé)<br />`2` = Tous * | — |
| **Utiliser les métadonnées**<br />`usemetadata_fe` | Recommandé pour masquer ou uniquement autoriser -basic- META données (description et mots-clés), le reste sera inutile pour les utilisateurs | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Basique (recommandé)<br />`2` = Tous * | — |
| **Configuration SEO**<br />`useseoconf_fe` | Permettre à l'utilisateur de modifier les paramètres SEO, comme balise de titre personnalisée | `radio` | `—` = Paramètres globaux<br />`0` = Non (recommandé)<br />`1` = Oui | — |
| **Options d'affichage**<br />`usedisplaydetails_fe` | Sélectionnez les groupes de paramètres que vous souhaitez rendre modifiables dans le frontend | `radio` | `—` = Paramètres globaux<br />`0` = Non (recommandé)<br />`1` = Basique<br />`2` = Avancé | — |
| **Options d'affichage d'un composant tiers**<br />`use3rdpartyparams_fe` | Sélectionner pour afficher les options d'affichage des extensions tierces | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Sélection du modèle**<br />`selecttheme_fe` | Activer la sélection et la configuration du modèle pour les groupes d'utilisateur de l'interface publique ayant le privilège de gestion des modèles. | `radio` | `—` = Paramètres globaux<br />`0` = Non (recommandé)<br />`1` = Sélectionner<br />`2` = Sélectionner et configurer | — |
| **Autorisations (ACL)**<br />`permsplacement_fe` | Sélectionnez ici pour afficher les permissions pour l'utilisateur si celles-ci sont modifiables | `radio` | `—` = Paramètres globaux<br />`0` = Toujours masquer (même si modifiable)<br />`1` = En ligne<br />`2` = Carrousel | — |
| **Versions**<br />`versionsplacement_fe` | Sélectionnez ici pour afficher la version en ligne dans une fenêtre pop-up | `radio` | `—` = Paramètres globaux<br />`0` = Toujours masquer (même si modifiable)<br />`1` = Pop-up<br />`2` = En ligne | — |

#### Style et comportement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Classe du libellé**<br />`form_lbl_class_fe` | Classe pour stylé le libellé de ce champ | `text` | — | — |
| **CSS du formulaire**<br />`form_container_css_fe` | Vous pouvez définir quelques règles CSS qui seront appliqués au formulaire de saisie. ex: 'width:800px;'pour éviter d'avoir des problèmes de dimension en frontend. | `text` | — | — |
| **Ajouter du code CSS**<br />`form_extra_css_fe` | Ajouter des règles CSS supplémentaires au formulaire de soumission/modification. - Ceci peut être écrasé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | `editor` | — | — |
| **Ajouter du code JS dans le formulaire d'édition pour développeur seulement***<br />`form_extra_js_fe` | Ajouter un code JS supplémentaire au formulaire de soumission/édition. - Généralement, vous ajoutez un code JS exécuté sur l'événement DOM Ready. - N'oubliez pas de casser l'exécution JS de votre formulaire. - Cela peut être surchargé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | `editor` | — | — |

## Surcharge: Envoyer/publier ACL

(Affecte seulement la soumission initiale)

### Utilisateurs non-autorisés

#### - Remplacer l’autorisation ACL « create » des TYPES. - L’autorisation ACL « create » des CATÉGORIES reste appliquée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Soumission pour les non-autorisés ignoré l'ACL 'création'(**)**<br />`allowunauthorize` | Cela permet aux utilisateurs non autorisés de soumettre de nouveaux éléments de contenu, ignorant ainsi le privilège ACL 'créer' ! **NOTE :** 1. Ceci n'affecte que l'élément de menu actuel 2. La méthode préférée est d'utiliser le privilège ACL 'créer' qui, ** - gére les soumissions partout, - peut même permettre aux utilisateurs invités de soumettre des éléments** | `radio` | `0` = Non, utiliser les ACL<br />`1` = Oui<br />`2` = Oui, sauf pour les invités (non connectés) | `0` (Non, utiliser les ACL) |

### Surcharge de l'auto publication

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Publication automatique**<br />`autopublished` | Publier automatiquement les contenus soumis | `multilist` | `0` = Non, afficher les statuts (basé sur les ACL)<br />`1` = Oui, masquer l'état de publication (aucun droit nécessaire) | `0` (Non, afficher les statuts (basé sur les ACL)) |
| **Message concernant la publication automatique**<br />`autopublished_message` | Le message sera placé en haut du formulaire, après les boutons de formulaire, **NOTE :** Ceci peut être une chaîne de langue (ajoutez-les à vos fichiers de langue), aussi vous pouvez utiliser 2 remplacements : _PUBLISH_UP_DAYS_INTERVAL_ et _PUBLISH_DOWN_DAYS_INTERVAL_ | `textarea` | — | — |
| **Intervalles de début de publication (minutes)**<br />`autopublished_up_interval` | Si l'auto-publication est activée, alors la date de début de publication sera ajoutée à l'heure actuelle plus l'intervalle, une valeur de 0 déclenchera la publication du contenu immédiatement **Remarque :** ce paramètre sera ignorée pour les utilisateurs autorisés à publier **Remarque :** par ex. Pour 24 heures entrez 1440 (c'est-à-dire 24*60) | `text` | — | `0` |
| **Intervalles de fin de publication (minutes)**<br />`autopublished_down_interval` | Si l'auto-publication est activée, alors la date de fin de publication sera ajoutée à l'heure actuelle plus l'intervalle, une valeur de 0 ne fixera pas de date de fin de publication **Remarque :** ce paramètre sera IGNORÉ pour les utilisateurs autorisés à publier **Remarque :** par ex. Pour 30 jours entrez 43200 (c'est-à-dire 30*24*60) | `text` | — | `0` |

## Surcharge : Catégorie ACL

(Affecte seulement la soumission initiale)

### Catégories

#### - Remplacer l’autorisation ACL « create » des CATÉGORIES. - L’autorisation ACL « create » des TYPES reste appliquée

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer la surcharge**<br />`overridecatperms` | Si cette option est désactivée alors les catégories pour lesquelles l'utilisateur a le droit 'créer' seront affichées. **NOTE** Cela n'override les droits de l'utilisateur pour une soumission dans des catégories multiples. | `multilist` | `0` = Non, utiliser les ACL<br />`1` = Oui | `0` (Non, utiliser les ACL) |
| **Catégories autorisées**<br />`cid` | Vous pouvez sélectionné plusieurs catégories**Si vous laissez la sélection vide **alors l'override des droits sera désactivé et les catégories pour lesquelles l'utilisateur a le droit 'créer' seront affichées. | `flexicategories` | — | — |

#### Catégorie principale

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Catégorie principale par défaut**<br />`maincatid` | Vous pouvez également définir la catégorie qui sera sélectionnée comme catégorie principale par défaut lors du chargement du formulaire. - Ceci sera ajouté aux catégories autorisées | `flexicategories` | — | — |
| **Actif le sélecteur**<br />`maincat_show` | Cacher / Afficher le sélecteur de catégorie principale. NOTE : vous devez sélectionner une valeur par défaut | `radio` | `1` = Cacher<br />`2` = Montrer | `2` (Montrer) |

#### Catégorie secondaire (=multi-catégories)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer le sélecteur**<br />`postcats` | Activer / désactiver la soumission multi-catégories (activer / désactiver le sélecteur de catégories secondaires). Ou verrouiller le sélecteur et soumettre dans toutes les catégories | `multilist` | `1` = Cacher<br />`2` = Montrer<br />`0` = Bloqué (ajouter dans TOUTES) | `2` (Montrer) |

#### Remarque : les utilisateurs ne peuvent pas soumettre dans plusieurs catégories, sauf s’ils disposent de l’autorisation ACL (COMPOSANT) **« Assigner plusieurs catégories aux contenus »**

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser tous les utilisateurs**<br />`override_mulcatsperms` | Sélectionner pour ignorer l’autorisation de l’utilisateur à assigner un contenu à plusieurs catégories | `radio` | `0` = Non, utiliser les ACL<br />`1` = Oui | `1` (Oui) |
| **Afficher les titres des catégories**<br />`postcats_show` | Sélectionner pour afficher la catégorie principale ou tous les titres de catégories | `radio` | `1` = Cacher<br />`2` = Montrer | `1` (Cacher) |
