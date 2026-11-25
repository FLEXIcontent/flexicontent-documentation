---
sidebar_position: 7
---

# Notifications des favoris

FLEXIcontent fournit des plugins pour la recherche, le routage, les notifications, les boutons de l’éditeur et les sitemaps. Activez-les et configurez-les depuis **Extensions → Plugins**. Les 35 plugins de types de champs sont documentés dans la section [Champs](../fields/index.md).

> Envoie des notifications aux utilisateurs en favorisant un contenu qui a été mis à jour. L'auteur peut choisir d'informer les utilisateurs privilégiant le contenu. Ceci est fait après que l'auteur clique sur Enregistrer, et au plus une fois par session de l'auteur.

:::info Source
Cette page est générée depuis `plugins/flexicontent/flexinotify/flexinotify.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Debug des notifications**<br />`debug_notifications` | Sélectionnez cette option pour afficher les messages de débogage et vérifier temporairement la bonne marche des notifications | `list` | `0` = Non<br />`1` = Afficher pour tous les éditeurs<br />`2` = Afficher pour tous les super-administrateurs | `0` (Non) |

#### Paramètres de base

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nom de l'expéditeur**<br />`sendername` | Nom de l'expéditeur. Si la valeur est vide, le nom du site sera utilisé à la place. | `text` | — | — |
| **Email de l'expéditeur**<br />`senderemail` | Adresse email de l'expéditeur. Si la valeur est vide, l'email de la configuration du site Joomla sera utilisé à la place. | `text` | — | — |

### Notify plg owners notifications

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Sujet de l'email**<br />`mailsubject_owner` | Sujet de l'email _Notification de mise à jour_ | `text` | — | — |
| **Notify plg body**<br />`mailbody_owner` | Notify plg body description _Notification message owner_ | `textarea` | — | — |

### Notify plg subscribers notifications

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Sujet de l'email**<br />`mailsubject` | Sujet de l'email _Notification de mise à jour_ | `text` | — | — |
| **Notify plg body**<br />`mailbody` | Notify plg body description _Bonjour %s,\n\nUn nouvel élément que vous avez ajouté dans vos favoris vient d'être modifié :\n\nId : %s\nTitre : %s\nCatégorie : %s\nLien : %s\n\nNous vous invitions à prendre connaissance de ces modifications,\n%s._ | `textarea` | — | — |

#### Notifications personnalisées envoie un courriel séparé par abonné

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`send_personalized` | Activer cette option pour envoyer un e-mail de notification différent par utilisateur, avec des personnalisations spécifiques tels que notamment le nom de l'utilisateur dans le message. Le soucis est que ce sera plus lent, à éviter si vous des éléments de contenu qui sont mis à jour très souvent et / ou si vous avez plus de 100 abonnés par élément de contenu! | `list` | `0` = Non, envoyer le même email (rapide)<br />`1` = Oui, envoyer des emails séparés | `1` (Oui, envoyer des emails séparés) |
| **Limite d'abonnement**<br />`personalized_limit` | Si un élément de contenu a plus d'abonnés que cette limite, un seul message sera envoyé. ** Remarque : **les valeurs supérieures à 100 seront ignorées | `text` | — | `50` |

:::note
Personnalisation par email
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Inclure le nom complet**<br />`include_fullname` | Le nom complet de l'utilisateur sera inclus, pour faire que l'e-mail soit plus convivial | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
