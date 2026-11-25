---
sidebar_position: 14
---

# Système — Tâches cœur

FLEXIcontent fournit des plugins pour la recherche, le routage, les notifications, les boutons de l’éditeur et les sitemaps. Activez-les et configurez-les depuis **Extensions → Plugins**. Les 35 plugins de types de champs sont documentés dans la section [Champs](../fields/index.md).

> Plugin système FLEXIcontent

:::info Source
Cette page est générée depuis `plugins/system/flexisystem/flexisystem.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

#### Redirections d’URL

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser le gestionnaire de catégories Joomla à**<br />`exclude_redirect_cats` | Tous les groupes d’utilisateurs non sélectionnés seront redirigés vers le gestionnaire de catégories FLEXIcontent | `flexiusergroup` | — | — |
| **Autoriser le gestionnaire d’articles Joomla à**<br />`exclude_redirect_articles` | Tous les groupes d’utilisateurs non sélectionnés seront redirigés vers le gestionnaire de contenus FLEXIcontent | `flexiusergroup` | — | — |
| **Exclure des URL de la redirection (saisir une partie) (BACKEND uniquement)**<br />`excluded_redirect_urls` | Si certaines URL sont redirigées de manière indésirable vers des URL FLEXIcontent, vous pouvez saisir ici une sous-chaîne de celles-ci afin de les exclure de la redirection. Séparez les URL par %% N’ajoutez pas de caractères de nouvelle ligne | `textarea` | — | — |
| **Rediriger le format PDF**<br />`redirect_pdf_format` | Joomla 2.5 ne prend pas en charge le PDF nativement ; cette option offre une solution pour les sites mis à niveau depuis J1.5 qui l’utilisaient, en redirigeant vers la version HTML | `radio` | `0` = Non<br />`1` = Oui<br />`2` = Oui, afficher une notification | `1` (Oui) |

#### Check-in automatiques

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Check-in à la déconnexion / expiration de session**<br />`checkin_on_session_end` | Les enregistrements verrouillés (contenus, catégories, etc.) seront déverrouillés à la déconnexion de l’utilisateur ou à l’expiration de la session | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Durée maximale de verrouillage**<br />`limit_checkout_hours` | Imposer une durée maximale pour les enregistrements verrouillés. Les enregistrements dépassant cette limite seront automatiquement déverrouillés | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Durée maximale de verrouillage (heures)**<br />`max_checkout_hours` | Durée maximale pendant laquelle un enregistrement (contenu, catégorie, etc.) peut rester verrouillé avant d’être automatiquement déverrouillé | `text` | — | `24` |

#### Archivage et dépublication automatiques

:::note
REMARQUE : si vous envoyez des e-mails d’expiration, ne modifiez pas l’état du contenu après son expiration et n’effacez pas la date de fin de publication
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Contenus avec dates expirées**<br />`archive_on_publish_down` | Activez cette option pour archiver ou dépublier automatiquement les contenus dont la date de fin de publication est atteinte | `radio` | `0` = Aucune action<br />`1` = Archiver<br />`2` = Dépublier | `0` (Aucune action) |
| **Effacer la date de fin de publication**<br />`clear_publish_down_date` | Lors de l’archivage automatique des contenus expirés, effacer également la date de fin de publication ; les contenus archivés seront ainsi visibles dans la vue archivée. | `radio` | `0` = Non<br />`1` = Oui, recommandé | `1` (Oui, recommandé) |
