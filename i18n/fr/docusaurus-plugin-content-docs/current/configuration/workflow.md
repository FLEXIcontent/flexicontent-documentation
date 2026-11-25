---
sidebar_position: 10
---

# Flux de travail

États de publication, permissions et workflow éditorial.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

#### Flux de travail

## Flux de travail standard

#### État par défaut pour les nouveaux contenus

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Administration**<br />`new_item_state` | Etat sélectionné par défaut lors de la création d'un nouveau contenu. | — | `1` |
| **Chargement automatique dans la partie publique**<br />`new_item_state_fe` | Etat sélectionné par défaut lors de la création d'un nouveau contenu. | — | `1` |

#### Forcer le statut des nouveaux contenus (pour les non-éditeurs)

:::note
--En attente d'approbation (génère immédiatement un courriel de notification) -- Brouillon ( l'utilisateur va mettre manuellement en état 'en attente d'approbation' avec le bouton de demande de Publication)
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Administration**<br />`non_publishers_item_state` | Le statut sera forcé lors de la création du contenu par des auteurs qui n'ont pas le droit de publier | — | `-4` |
| **Chargement automatique dans la partie publique**<br />`non_publishers_item_state_fe` | Le statut sera forcé lors de la création du contenu par des auteurs qui n'ont pas le droit de publier | — | `-3` |

## Configuration de la gestion des versions

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer la gestion des versions**<br />`use_versioning` | Activer la fonction de gestion des versions dans le composant FLEXIcontent. | — | `1` |
| **Comparaison de version**<br />`allow_versioncomparing` | Désactive le moteur de comparaison des versions qui permet de visualiser la différence entre deux versions. Remarque : le moteur peut générer certaines erreurs en fonction de l'éditeur utilisé. | — | `1` |
| **Versions à conserver**<br />`nr_versions` | Choisissez le nombre de version à conserver pour chaque contenu. Un nombre important augmentera la taille de votre base de donnée. Attention lorsque vous choisissez de grosses valeurs comme 50 ou 100. | — | `10` |
| **Nb. de versions par page**<br />`versionsperpage` | Indique le nombre de versions à afficher sur chaque page dans la section de gestion de version d'un contenu. | — | `5` |
| **Publier les changements(nouvelle version)**<br />`auto_approve` | Sélectionnez cette option pour permettre à l'utilisateur de publier des modifications (nouvelle version). Cela peut être utile pour prévisualiser les modifications avant de les rendre publiques | — | `1` |

## Notifications

:::note
Notifications suite à la soumission ou au changement d'un contenu
:::

:::note
Les e-mails de notification utilisent les modèles de messagerie de Joomla. Modifiez l’objet et le corps de chaque notification dans **Système → Modèles de messagerie**, en filtrant sur l’extension **FLEXIcontent**. Les balises disponibles incluent : **&#123;TITLE&#125;**, **&#123;STATE&#125;**, **&#123;CREATOR&#125;**, **&#123;MODIFIER&#125;**, **&#123;EDITOR_NAME&#125;**, **&#123;CREATED&#125;**, **&#123;MODIFIED&#125;**, **&#123;CATEGORIES&#125;**, **&#123;VIEW_URL&#125;**, **&#123;EDIT_URL_FE&#125;**, **&#123;EDIT_URL_BE&#125;**, **&#123;NOTIFY_TEXT&#125;**, **&#123;CATEGORY_TEXT&#125;**. Les champs personnalisés FLEXIcontent sont disponibles sous **&#123;FIELD_FIELDNAME&#125;** ou directement sous **&#123;FIELDNAME&#125;** (nom du champ en majuscules, caractères non alphanumériques remplacés par des tirets bas, ex. **&#123;FIELD_FLOORS&#125;** ou **&#123;FLOORS&#125;**), et tous les champs non cœur ensemble sous **&#123;FIELDS&#125;**. Un nom de champ ne remplace jamais une balise cœur comme **&#123;TITLE&#125;**. **Blocs conditionnels :** l’objet, le corps texte et le corps HTML du modèle peuvent contenir des blocs **&#123;if ...&#125;...&#123;elseif ...&#125;...&#123;else&#125;...&#123;/if&#125;**. Variables de contexte : **catid**, **incat**, **state_id**, **lang**, **type_id**, **item_id**, **author_id**, **editor_id**. Les champs personnalisés sont testés avec **field_name** (ex. **&#123;if field_floors&#125;Étage : &#123;FIELD_FLOORS&#125;&#123;/if&#125;**). Opérateurs : **=**, **!=**, **in**, **not in**, **contains**, **not contains**, **&gt;**, **&gt;=**, **=100000&#125;Premium&#123;/if&#125;**. Les mots-clés et les comparaisons de chaînes ne sont pas sensibles à la casse. Les conditions n’affectent que le texte, pas les destinataires. Elles sont évaluées sur le contenu du modèle enregistré dans Modèles de messagerie ; les modèles fournis utilisent des clés de langue et doivent être modifiés et enregistrés une fois pour contenir du texte conditionnel. Une condition invalide conserve le contenu et ne bloque jamais l’e-mail.
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer les notifications**<br />`enable_notifications` | Cette option permet d'activer l'envoi de notification automatique par email suite à la soumission ou la modification d'un contenu. | — | `0` |
| **Debug des notifications**<br />`nf_enable_debug` | -- Activer ceci pour: (a) afficher les informations de débogage et aussi (b) **forcer l'envoi de notifications par e-mail sur chaque opération de sauvegarde**, -- Normalement, les notifications seront envoyées SEULEMENT (a) une fois par session pour chaque élément de contenu ou (b)**lorsque ses catégories sont modifiées**. | — | `0` |

### Création d’e-mail

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Envoyer les emails en copie cachée**<br />`nf_send_as_bcc` | Activez cette option pour empêcher les destinataires de recevoir des e-mails et de voir d'autres destinataires. **NOTE**: cela obligera l'administrateur du site à être le principal destinataire de l'e-mail de notification | — | `1` |

### Email destinataires

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Choisir**<br />`nf_allow_cat_specific` | Sélectionnez cette option pour autoriser les notifications qui dépendent de la catégorie dans laquelle les contenus sont affectés. Cela montrera également la sélection des destinataires dans chaque configuration de chaque catégorie | — | `1` |

#### Nouveau Contenu : Peu importe le statut (à partir des auteurs qui peuvent publier)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **États des contenus**<br />`states_notify_new` | L'email de notification sera envoyé quand le contenu aura un des états sélectionnés. | — | — |
| **Groupes d'utilisateurs**<br />`usergrps_notify_new` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | — | — |
| **Id Utilisateur/liste de noms**<br />`userlist_notify_new` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | — | — |
| **Texte personnalisé**<br />`text_notify_new` | Entrez un texte supplémentaire personnalisé à inclure dans l'e-mail de notification. **NOTE**: Ceci sera filtré comme une chaîne de langue (via JText) | — | — |

#### Nouveau Contenu: En attente de publication (pour les auteurs qui n'ont pas le droit de publication)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Groupes d'utilisateurs**<br />`usergrps_notify_new_pending` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | — | — |
| **Id Utilisateur/liste de noms**<br />`userlist_notify_new_pending` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | — | — |
| **Texte personnalisé**<br />`text_notify_new_pending` | Entrez un texte supplémentaire personnalisé à inclure dans l'e-mail de notification. **NOTE**: Ceci sera filtré comme une chaîne de langue (via JText) | — | — |

#### Mise à jour d'un contenu: PAS BESOIN D'APPROBATION DE LA VERSION (pour les auteurs qui peuvent publier )

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **États des contenus**<br />`states_notify_existing` | L'email de notification sera envoyé quand le contenu aura un des états sélectionnés. | — | — |
| **Groupes d'utilisateurs**<br />`usergrps_notify_existing` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | — | — |
| **Id Utilisateur/liste de noms**<br />`userlist_notify_existing` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | — | — |
| **Texte personnalisé**<br />`text_notify_existing` | Entrez un texte supplémentaire personnalisé à inclure dans l'e-mail de notification. **NOTE**: Ceci sera filtré comme une chaîne de langue (via JText) | — | — |

:::note
Mise à jour d'un contenu: BESOIN DE L'APPROBATION DE LA VERSION (pour les auteurs qui ne peuvent pas publier, la gestion des versions doit être activé)
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Groupes d'utilisateurs**<br />`usergrps_notify_existing_reviewal` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | — | — |
| **Id Utilisateur/liste de noms**<br />`userlist_notify_existing_reviewal` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | — | — |
| **Texte personnalisé**<br />`text_notify_existing_reviewal` | Entrez un texte supplémentaire personnalisé à inclure dans l'e-mail de notification. **NOTE**: Ceci sera filtré comme une chaîne de langue (via JText) | — | — |

#### Flux de travail
