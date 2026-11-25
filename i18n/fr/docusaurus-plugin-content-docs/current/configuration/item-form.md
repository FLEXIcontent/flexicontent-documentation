---
sidebar_position: 9
---

# Formulaire de contenu

Mise en page et comportement du formulaire de création et d’édition d’un contenu.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

#### Formulaire de saisie

## Formulaire de contenu (Public)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Apparence du formulaire de saisie**<br />`form_ilayout_fe` | — | — | `tabs` |

#### Formulaire de contenu (Public)

## Paramétrage du formulaire

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Boutons optionnels**<br />`allowbuttons_fe` | Sélectionner les boutons que vous souhaitez faire apparaitre dans le formulaire de saisie en frontend. | — | — |
| **Placement des boutons**<br />`buttons_placement_fe` | Selectionner pour afficher des boutons de formulaire en haut ou en bas du formulaire | — | `0` |

#### Affiche un message du type approbation nécessaire

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Dans le formulaire**<br />`approval_warning_inform_fe` | Activez ceci, pour afficher un message dans le formulaire de l'élément, si l'utilisateur actuel peut publier de nouveaux éléments ou s'il peut auto-approuver les modifications aux éléments existants | — | `1` |
| **Après la soumission du formulaire**<br />`approval_warning_aftersubmit_fe` | Activez ceci, pour afficher un avertissement après l'envoi du formulaire, en disant si l'approbation est nécessaire pour que le nouvel élément soit publié ou pour que les modifications de l'élément existant deviennent actives | — | `1` |
| **Nécessite une révision de cette version**<br />`version_reviewal_msg_fe` | — | — | — |
| **Nécessite l'approbation du contenu**<br />`document_approval_msg_fe` | — | — | — |
| **Peut nécessiter une révision de cette version**<br />`mr_version_revial_msg_fe` | — | — | — |
| **Peut nécessiter l'approbation du contenu**<br />`mr_document_approval_msg_fe` | — | — | — |
| **Modifications appliquées immédiatement**<br />`changes_applied_immediately_msg_fe` | — | — | — |

#### Instructions / redirections d'URL / etc

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Instructions pour la saisie**<br />`submit_message` | Ces instructions seront placées en haut du formulaire, après les boutons **NOTE **: Cela peut être une chaîne de langue (à ajouter à vos fichiers de langue) | — | — |
| **Redirection URL après la soumission cache le bouton Aperçu**<br />`submit_redirect_url_fe` | Vous pouvez définir une URL personnalisée vers laquelle l'utilisateur sera redirigé après avoir soumis un nouveau contenu. **NOTE :** Cela fonctionnera même si vous cliquez sur les boutons 'Ajouter' ou 'Appliquer' avant de fermer l'élément **Remarque :** Définir ceci masquera le bouton d'aperçu lors de l'envoi de nouveaux éléments | — | — |
| **Page d'accès non autorisé (saisir un contenu)**<br />`notauthurl` | Spécifiez l'URL / ID du lien de menu de la page vers laquelle vous souhaitez que vos visiteurs / utilisateurs soient dirigés s'ils n'ont pas les droits suffisants pour créer plus de contenu (ou aucun). Cela pourrait être (par exemple) la page des plans d'abonnement si vous vendez votre espace de publication. **NOTE :** Si vous ne définissez rien ici, la page générale non autorisé sera utilisée. | — | — |

#### Formulaire de sécurité critères d'affichage pour CAPTCHA

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser les captcha**<br />`use_captcha` | Choisir à quel moment afficher un champ captcha pour protéger le formulaire des robots | — | `1` |
| **Plugin de Captcha**<br />`captcha` | Choisir un plugin spécifique de captcha pour surcharger le paramètre par défaut | — | — |
| **Type d'opération**<br />`captcha_formop` | Lorsque l'opération est sur le type sélectionné | — | `0` |

## Compatibilité Joomla

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Images intro / complètes**<br />`use_jimages_fe` | Afficher les images intro/complètes | — | — |
| **URL**<br />`use_jurls_fe` | Afficher les URL | — | — |

## Édition de base

#### Nouveaux / existants contenus

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser le titre**<br />`usetitle_fe` | Sélectionnez pour afficher ou masquer le titre de l'élément - vous pouvez définir automatiquement dans les paramètres de type | — | `1` |
| **Utiliser les Alias**<br />`usealias_fe` | Autoriser l'utilisateur à saisir les alias. | — | `1` |
| **Utiliser le type**<br />`usetype_fe` | Afficher le sélecteur de type pour permettre le changement de type d'élément | — | `1` |
| **Utiliser l'état**<br />`usestate_fe` | Afficher le sélecteur d'état pour permettre le changement d'état de publication du contenu | — | `1` |
| **Utiliser l'accès**<br />`useaccess_fe` | Afficher le sélecteur d'accès pour permettre de changer le niveau d'accès du contenu | — | `1` |
| **Utiliser les vedettes**<br />`usefeatured_fe` | Afficher le sélecteur de vedette pour permettre le changement d'état du contenu | — | `0` |
| **Utiliser les tags**<br />`usetags_fe` | Autoriser les tags a être cachés, pour les groupes qui possèdent le droit sur les tags, cela n'empêche pas après de gérer les tags | — | `1` |
| **Autoriser la désactivation des commentaires**<br />`allowdisablingcomments_fe` | Vous pouvez préciser ici si les auteurs ou les éditeurs peuvent désactiver les commentaires pour le contenu qu'ils modifient ou ajoutent. Si vous autorisez ce paramètre, il est recommandé de ne pas afficher les paramètres avancés du contenu. | — | `0` |

#### Catégories

:::note
Remarque : Vous avez toujours besoin des **ACL** pour éviter les changements de catégories multiples. Cacher ces dernières, n'empêche pas les utilisateurs de les modifier ...
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser la catégorie**<br />`usemaincat_fe` | Si vous désactivez cette option, vous devez également définir une catégorie par défaut dans la configuration de chaque type (généralement vous allez créer une catégorie avec le même nom que le type et la définir comme par défaut) | — | `1` |
| **Catégories secondaires**<br />`show_seccats_fe` | — | — | `2` |
| **Catégories en vedette**<br />`show_featcats_fe` | — | — | `2` |

:::note
Filtrer
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Pas dans la langue de l'élément**<br />`iform_cats_not_in_itemlang_fe` | Masquer les catégories dans des langues différentes de la langue de l'élément ou ajouter une langue au titre de la catégorie | — | `1` |
| **États autorisés**<br />`iform_catstates_allowed_fe` | Les catégories avec des états non autorisés seront masquées, sauf si l'élément est déjà affecté à une telle catégorie | — | — |

#### Langue

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser le langage**<br />`uselang_fe` | Autoriser l'utilisateur à choisir sa langue. NOTE : Sélectionnez une langue par défaut avant de désactiver ce paramètre | — | `1` |
| **Langue par défaut**<br />`default_language_fe` | C'est la langue qui sera pré-sélectionnée, particulièrement utile si vous cachez la langue | — | `_author_lang_` |
| **Désactiver les langues**<br />`disable_languages_fe` | Par exemple, vous pourriez choisir de désactiver la langue 'ALL' | — | — |

#### Sélecteur de langue

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Afficher comme**<br />`langdisplay_fe` | Vous pouvez l'afficher ex comme une liste déroulante ou des boutons radios | — | `2` |
| **Afficher drapeaux (radio)**<br />`langdisplay_flags_fe` | Afficher les icônes drapeaux | — | `1` |
| **Montrer le texte (radio)**<br />`langdisplay_texts_fe` | Activer pour afficher le texte comme un code langue | — | `1` |

#### Contenus existants

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Autoriser les modifications de langue**<br />`allowlangmods_fe` | Permettre à l'utilisateur de modifier les propriétés de la langue pour des éléments -existant-. Habituellement, vous devriez interdire aux utilisateurs de modifier les propriétés de langue existantes comme la langue de l'élément et le contenu original de la traduction | — | — |

:::note
Vous avez accès à plus d'option de configuration ici: Plugin de Notifications
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Autoriser la notification du propriétaire**<br />`allow_owner_notify_fe` | Permettre à l'éditeur d'envoyer une notification de mise à jour (email) au propriétaire du contenu courant | — | `0` |
| **Autoriser la notification des inscrits (contenus favoris des utilisateurs)**<br />`allow_subscribers_notify_fe` | Permettre à l'éditeur d'envoyer des notifications de mise à jour (emails) aux utilisateurs qui ont en favori le contenu courant | — | `0` |

## Options avancées

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser les détails de publication**<br />`usepublicationdetails_fe` | Sélectionnez ici pour autoriser : -Basic- Publication Details: (début & date de fin de publication & alias d'auteur) aux personnes qui peuvent -EDITER- l'élément. ou - Tous les détails de la publication : (auteur de l'élément & date de création) sont disponibles UNIQUEMENT aux utilisateurs de Super Admin. | — | `1` |
| **Utiliser les métadonnées**<br />`usemetadata_fe` | Recommandé pour masquer ou uniquement autoriser -basic- META données (description et mots-clés), le reste sera inutile pour les utilisateurs | — | `1` |
| **Configuration SEO**<br />`useseoconf_fe` | Permettre à l'utilisateur de modifier les paramètres SEO, comme balise de titre personnalisée | — | `0` |
| **Options d'affichage**<br />`usedisplaydetails_fe` | Sélectionnez les groupes de paramètres que vous souhaitez rendre modifiables dans le frontend | — | `0` |
| **Options d'affichage d'un composant tiers**<br />`use3rdpartyparams_fe` | Sélectionner pour afficher les options d'affichage des extensions tierces | — | `1` |
| **Sélection du modèle**<br />`selecttheme_fe` | Activer la sélection et la configuration du modèle pour les groupes d'utilisateur de l'interface publique ayant le privilège de gestion des modèles. | — | `0` |
| **Autorisations (ACL)**<br />`permsplacement_fe` | Sélectionnez ici pour afficher les permissions pour l'utilisateur si celles-ci sont modifiables | — | `2` |
| **Versions**<br />`versionsplacement_fe` | Sélectionnez ici pour afficher la version en ligne dans une fenêtre pop-up | — | `2` |

## Mise en Page

:::note
Utiliser les paramètres par défaut
:::

## Style

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Classe du libellé**<br />`form_lbl_class_fe` | Classe pour stylé le libellé de ce champ | — | — |
| **Classe CSS du conteneur**<br />`form_container_class_fe` | Une liste de noms de classes à ajouter au conteneur de formulaire externe | — | — |
| **CSS du formulaire**<br />`form_container_css_fe` | Vous pouvez définir quelques règles CSS qui seront appliqués au formulaire de saisie. ex: 'width:800px;'pour éviter d'avoir des problèmes de dimension en frontend. | — | — |
| **Ajouter du code CSS**<br />`form_extra_css_fe` | Ajouter des règles CSS supplémentaires au formulaire de soumission/modification. - Ceci peut être écrasé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | — | — |
| **Ajouter du code JS dans le formulaire d'édition pour développeur seulement***<br />`form_extra_js_fe` | Ajouter un code JS supplémentaire au formulaire de soumission/édition. - Généralement, vous ajoutez un code JS exécuté sur l'événement DOM Ready. - N'oubliez pas de casser l'exécution JS de votre formulaire. - Cela peut être surchargé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | — | — |

#### Formulaire de contenu (Public)

## Formulaire de contenu (Administration)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Apparence du formulaire de saisie**<br />`form_ilayout_be` | — | — | `tabs` |

#### Formulaire de contenu (Administration)

## Paramétrage du formulaire

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Boutons optionnels**<br />`allowbuttons_be` | Sélectionner les boutons que vous souhaitez faire apparaitre dans le formulaire de saisie en frontend. | — | — |
| **Placement des boutons**<br />`buttons_placement_be` | Selectionner pour afficher des boutons de formulaire en haut ou en bas du formulaire | — | `-1` |

#### Affiche un message du type approbation nécessaire

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Dans le formulaire**<br />`approval_warning_inform_be` | Activez ceci, pour afficher un message dans le formulaire de l'élément, si l'utilisateur actuel peut publier de nouveaux éléments ou s'il peut auto-approuver les modifications aux éléments existants | — | `1` |
| **Après la soumission du formulaire**<br />`approval_warning_aftersubmit_be` | Activez ceci, pour afficher un avertissement après l'envoi du formulaire, en disant si l'approbation est nécessaire pour que le nouvel élément soit publié ou pour que les modifications de l'élément existant deviennent actives | — | `1` |
| **Nécessite une révision de cette version**<br />`version_reviewal_msg_be` | — | — | — |
| **Nécessite l'approbation du contenu**<br />`document_approval_msg_be` | — | — | — |
| **Peut nécessiter une révision de cette version**<br />`mr_version_revial_msg_be` | — | — | — |
| **Peut nécessiter l'approbation du contenu**<br />`mr_document_approval_msg_be` | — | — | — |
| **Modifications appliquées immédiatement**<br />`changes_applied_immediately_msg_be` | — | — | — |

#### Instructions / redirections d'URL / etc

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Instructions pour la saisie**<br />`submit_message_be` | Ces instructions seront placées en haut du formulaire, après les boutons **NOTE **: Cela peut être une chaîne de langue (à ajouter à vos fichiers de langue) | — | — |

## Compatibilité Joomla

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Images intro / complètes**<br />`use_jimages_be` | Afficher les images intro/complètes | — | — |
| **URL**<br />`use_jurls_be` | Afficher les URL | — | — |

## Édition de base

#### Nouveaux / existants contenus

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser le titre**<br />`usetitle_be` | Sélectionnez pour afficher ou masquer le titre de l'élément - vous pouvez définir automatiquement dans les paramètres de type | — | `1` |
| **Utiliser les Alias**<br />`usealias_be` | Autoriser l'utilisateur à saisir les alias. | — | `1` |
| **Utiliser le type**<br />`usetype_be` | Afficher le sélecteur de type pour permettre le changement de type d'élément | — | `1` |
| **Utiliser l'état**<br />`usestate_be` | Afficher le sélecteur d'état pour permettre le changement d'état de publication du contenu | — | `1` |
| **Utiliser l'accès**<br />`useaccess_be` | Afficher le sélecteur d'accès pour permettre de changer le niveau d'accès du contenu | — | `1` |
| **Utiliser les vedettes**<br />`usefeatured_be` | Afficher le sélecteur de vedette pour permettre le changement d'état du contenu | — | `1` |
| **Utiliser les tags**<br />`usetags_be` | Autoriser les tags a être cachés, pour les groupes qui possèdent le droit sur les tags, cela n'empêche pas après de gérer les tags | — | `1` |
| **Autoriser la désactivation des commentaires**<br />`allowdisablingcomments_be` | Vous pouvez préciser ici si les auteurs ou les éditeurs peuvent désactiver les commentaires pour le contenu qu'ils modifient ou ajoutent. Si vous autorisez ce paramètre, il est recommandé de ne pas afficher les paramètres avancés du contenu. | — | `0` |

#### Catégories

:::note
Remarque : Vous avez toujours besoin des **ACL** pour éviter les changements de catégories multiples. Cacher ces dernières, n'empêche pas les utilisateurs de les modifier ...
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser la catégorie**<br />`usemaincat_be` | Si vous désactivez cette option, vous devez également définir une catégorie par défaut dans la configuration de chaque type (généralement vous allez créer une catégorie avec le même nom que le type et la définir comme par défaut) | — | `1` |
| **Catégories secondaires**<br />`show_seccats_be` | — | — | `2` |
| **Catégories en vedette**<br />`show_featcats_be` | — | — | `2` |

:::note
Filtrer
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Pas dans la langue de l'élément**<br />`iform_cats_not_in_itemlang_be` | Masquer les catégories dans des langues différentes de la langue de l'élément ou ajouter une langue au titre de la catégorie | — | `1` |
| **États autorisés**<br />`iform_catstates_allowed_be` | Les catégories avec des états non autorisés seront masquées, sauf si l'élément est déjà affecté à une telle catégorie | — | — |

#### Langue

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser le langage**<br />`uselang_be` | Autoriser l'utilisateur à choisir sa langue. NOTE : Sélectionnez une langue par défaut avant de désactiver ce paramètre | — | `1` |
| **Langue par défaut**<br />`default_language_be` | C'est la langue qui sera pré-sélectionnée, particulièrement utile si vous cachez la langue | — | `_author_lang_` |
| **Désactiver les langues**<br />`disable_languages_be` | Par exemple, vous pourriez choisir de désactiver la langue 'ALL' | — | — |

#### Sélecteur de langue

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Afficher comme**<br />`langdisplay_be` | Vous pouvez l'afficher ex comme une liste déroulante ou des boutons radios | — | `2` |
| **Afficher drapeaux (radio)**<br />`langdisplay_flags_be` | Afficher les icônes drapeaux | — | `1` |
| **Montrer le texte (radio)**<br />`langdisplay_texts_be` | Activer pour afficher le texte comme un code langue | — | `1` |

#### Contenus existants

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Autoriser les modifications de langue**<br />`allowlangmods_be` | Permettre à l'utilisateur de modifier les propriétés de la langue pour des éléments -existant-. Habituellement, vous devriez interdire aux utilisateurs de modifier les propriétés de langue existantes comme la langue de l'élément et le contenu original de la traduction | — | — |

:::note
Vous avez accès à plus d'option de configuration ici: Plugin de Notifications
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Autoriser la notification du propriétaire**<br />`allow_owner_notify_be` | Permettre à l'éditeur d'envoyer une notification de mise à jour (email) au propriétaire du contenu courant | — | `1` |
| **Autoriser la notification des inscrits (contenus favoris des utilisateurs)**<br />`allow_subscribers_notify_be` | Permettre à l'éditeur d'envoyer des notifications de mise à jour (emails) aux utilisateurs qui ont en favori le contenu courant | — | `1` |

## Options avancées

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser les détails de publication**<br />`usepublicationdetails_be` | Sélectionnez ici pour autoriser : -Basic- Publication Details: (début & date de fin de publication & alias d'auteur) aux personnes qui peuvent -EDITER- l'élément. ou - Tous les détails de la publication : (auteur de l'élément & date de création) sont disponibles UNIQUEMENT aux utilisateurs de Super Admin. | — | `2` |
| **Utiliser les métadonnées**<br />`usemetadata_be` | Recommandé pour masquer ou uniquement autoriser -basic- META données (description et mots-clés), le reste sera inutile pour les utilisateurs | — | `2` |
| **Configuration SEO**<br />`useseoconf_be` | Permettre à l'utilisateur de modifier les paramètres SEO, comme balise de titre personnalisée | — | `1` |
| **Options d'affichage**<br />`usedisplaydetails_be` | Sélectionnez les groupes de paramètres que vous souhaitez rendre modifiables dans le frontend | — | `2` |
| **Options d'affichage d'un composant tiers**<br />`use3rdpartyparams_be` | Sélectionner pour afficher les options d'affichage des extensions tierces | — | `1` |
| **Sélection du modèle**<br />`selecttheme_be` | Activer la sélection et la configuration du modèle pour les groupes d'utilisateur de l'interface publique ayant le privilège de gestion des modèles. | — | `2` |
| **Autorisations (ACL)**<br />`permsplacement_be` | Sélectionnez ici pour afficher les permissions pour l'utilisateur si celles-ci sont modifiables | — | `2` |
| **Versions**<br />`versionsplacement_be` | Sélectionnez ici pour afficher la version en ligne dans une fenêtre pop-up | — | `2` |

## Mise en Page

:::note
Utiliser les paramètres par défaut
:::

## Style

### Style

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Classe du libellé**<br />`form_lbl_class_be` | Classe pour stylé le libellé de ce champ | — | — |
| **Classe CSS du conteneur**<br />`form_container_class_be` | Une liste de noms de classes à ajouter au conteneur de formulaire externe | — | — |
| **CSS du formulaire**<br />`form_container_css_be` | Vous pouvez définir quelques règles CSS qui seront appliqués au formulaire de saisie. ex: 'width:800px;'pour éviter d'avoir des problèmes de dimension en frontend. | — | — |
| **Ajouter du code CSS**<br />`form_extra_css_be` | Ajouter des règles CSS supplémentaires au formulaire de soumission/modification. - Ceci peut être écrasé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | — | — |
| **Ajouter du code JS dans le formulaire d'édition pour développeur seulement***<br />`form_extra_js_be` | Ajouter un code JS supplémentaire au formulaire de soumission/édition. - Généralement, vous ajoutez un code JS exécuté sur l'événement DOM Ready. - N'oubliez pas de casser l'exécution JS de votre formulaire. - Cela peut être surchargé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | — | — |

#### Formulaire de contenu (Administration)

## Formulaire de contenu (Public et administration)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Type d'icône**<br />`form_font_icons` | Vous pouvez afficher des icônes comme des images ou utiliser les jeu de polices d’icônes | — | `1` |
| **Cacher la description**<br />`hide_maintext` | Masquer le champ description (texte principal) du formulaire du contenu (pas recommandé !!!). FAITES ATTENTION, vous perdrez la rétro-compatibilité avec le composants com_content pour les contenus concerés !!! | — | `0` |

### Style

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Ajouter du code CSS**<br />`form_extra_css` | Ajouter des règles CSS supplémentaires au formulaire de soumission/modification. - Ceci peut être écrasé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | — | — |
| **Ajouter du code JS dans le formulaire d'édition pour développeur seulement***<br />`form_extra_js` | Ajouter un code JS supplémentaire au formulaire de soumission/édition. - Généralement, vous ajoutez un code JS exécuté sur l'événement DOM Ready. - N'oubliez pas de casser l'exécution JS de votre formulaire. - Cela peut être surchargé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | — | — |

## Formulaire d'article Joomla

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Type par défaut**<br />`jarticle_form_typeid` | Type par défaut pour un article Joomla lors d'un nouvel élément ou lorsque ce dernier n'a aucun type ! | — | — |

#### Chargement automatique dans la partie publique

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Formulaire de nouvel article**<br />`jarticle_allow_new_form` | Quand vous saisissez un nouvel article Joomla, vous pouvez : -Soit utiliser le formulaire de saisie FLEXIcontent -Soit utiliser le formulaire de saisie Joomla | — | `1` |

:::note
**Note**: Les éléments existants peuvent être modifiés via des liens vers le formulaire d'article Joomla si leur configuration de type -- \"Autoriser la vue article de Joomla\" -- paramètre est activé
:::

#### Formulaire de saisie
