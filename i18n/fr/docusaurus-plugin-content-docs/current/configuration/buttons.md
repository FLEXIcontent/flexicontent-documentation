---
sidebar_position: 4
---

# Boutons

Boutons de la barre d’outils affichés dans les gestionnaires du backend.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

### Boutons

#### Bouton de page

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Méthode d'impression**<br />`print_behaviour` | Selectionnez pour ouvrir automatiquement la fenêtre d'impression du navigateur, ou afficher un bouton d'impression dans la page | — | `auto` |
| **Icône imprimer**<br />`show_print_icon` | Affiche l'icône d'impression. | — | `1` |
| **Icône email**<br />`show_email_icon` | Activer le partage de la page via e-mail | — | `1` |

:::note
Bouton de liste de contenus
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Icône du flux RSS**<br />`show_feed_icon` | Activer la prévisualisation de la page actuelle dans une fenêtre popup. Cela facilitera aussi l'inscription de vos visiteurs | — | `0` |
| **Flux RSS**<br />`show_feed_link` | Activer cette option pour insérer un lien vers le flux RSS dans le HEAD de votre page HTML. Cela permet aux navigateurs de souscrire à l'actualité des contenus de la catégorie. | — | `1` |

#### Boutons contenu

:::note
Vous pouvez faire une configuration similaire pour le liste de contenu dans l'onglet '%s'
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Bouton Modifier**<br />`show_editbutton` | Affiche un bouton de modification pour tous les utilisateurs qui sont connectés et qui ont les droits nécessaires pour effectuer l'édition du contenu | — | `1` |
| **Bouton Supprimer (permanent)**<br />`show_deletebutton` | Actif l'affichage du bouton Supprimer pour tous les éléments que l'utilisateur connecté peut supprimer. REMARQUE, ce n'est pas un bouton de corbeille, cette action va supprimé définitivement l'élément. | — | `0` |
| **Bouton Statut**<br />`show_state_icon` | Activer le changement de statut rapide via AJAX | — | `1` |

### Personnalisé

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Afficher les icônes**<br />`show_icons` | Affiche les icônes imprimer et email ou utiliser uniquement le texte | — | `2` |
| **Type d'icône**<br />`use_font_icons` | Vous pouvez afficher des icônes comme des images ou utiliser les jeu de polices d’icônes | — | `1` |
| **Pré-configuration**<br />`font_icon_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | — | — |
| **Icônes polices**<br />`font_icon_classes` | Utiliser les virgules pour séparer les options, pour charger les valeurs par défaut et ainsi voir les format originels, vider le champ et sauver | — | `pdf:icon-book, print:icon-print, mail:icon-envelope, feed:icon-feed, edit:icon-pencil, new:icon-new, approval:icon-key, delete:icon-delete, csv:icon-download` |

#### Placement des boutons

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Placer dans la liste déroulante**<br />`btn_grp_dropdown` | Afficher les boutons dans une liste déroulante, en général cela utilisera les styles bootstrap ou similaire, et cela peut ne pas être modifié par les modèles personnalisés | — | `0` |
| **Icône liste**<br />`btn_grp_dropdown_class` | Icône représentant la liste déroulante | — | `icon-options` |
