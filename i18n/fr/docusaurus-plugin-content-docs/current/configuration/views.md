---
sidebar_position: 5
---

# Vues

Paramètres communs aux vues frontend (étiquettes, auteurs, recherche, favoris, etc.).

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

### Vue contenu

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Afficher le titre**<br />`show_title` | Afficher le titre | — | `1` |
| **Titre cliquable**<br />`link_titles` | Si oui, le titre des contenus seront cliquables et seront liés à eux-mêmes. | — | `1` |
| **Montrer le texte d'introduction**<br />`show_intro` | Permet de montrer le texte d'introduction même dans la vue contenu, en plus de la description complète. | — | `1` |

#### Commentaires

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer l'intégration des commentaires**<br />`comments` | Autorise l'intégration d'un système de commentaires. **REMARQUE:** Ce paramètre peut être surchargé dans les types, les catégories, les éléments uniques ou les éléments de menu. **REMARQUE:** Si vous désactivez cette option, vous pourrez activer manuellement (le champ de description activera tout par défaut) le plug-in de contenu Joomla approprié de votre système de commentaires pour insérer des commentaires via un événement de contenu Joomla. Si vous ajoutez des commentaires de cette manière, vous ne pourrez pas utiliser le paramètre \"Désactiver les commentaires\" dans le formulaire, mais vous devrez le faire comme le recommande votre système de commentaires, par exemple. en insérant un texte spécial dans la description | — | `0` |

:::note
Intégration manuelle des commentaires
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Lien d'édition de l'administration**<br />`comments_admin_link` | Si vous ajoutez des commentaires manuellement (par exemple, en activant un plugin Joomla), vous pourrez alors ajouter le lien complet vers l'administration du composant afin de l’intégrer au tableau de bord FLEXIcontent | — | — |

#### Configuration du compteur de visites

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Compter les visites uniques**<br />`hits_count_unique` | En activant ce paramètre, le compteur ne sera incrémenté qu'une seule fois par visiteur unique. Remarque : ce paramètre affecte les autre options du compteur. | — | `0` |
| **Nb minutes entre deux visites**<br />`hits_mins_to_unique` | Nombre de minutes minimum pour compter une nouvelle visite pour une même adresse IP. | — | `600` |
| **Utiliser la liste des IP ignorées**<br />`hits_skip_ips` | Utilise ou non la liste des IP ignorées dans le compteur de visite. | — | `1` |
| **Liste des IP ignorées**<br />`hits_ips_list` | Liste des adresses IP qui ne seront pas comptabilisées dans le compteur de visite. | — | `127.0.0.1` |
| **Ignorer les robots**<br />`hits_skip_bots` | Ne pas comptabiliser les visites des robots. | — | `1` |
| **Liste des robots**<br />`hits_bots_list` | Liste des robots à ignorer dans le compteur de visite. | — | `bot,spider,crawler,search,libwww,archive,slurp,teoma` |

### Anciennes vues

:::note
- **Contenus de l’auteur** et **Mes contenus** utilisent toujours la vue catégorie. Un seul élément de menu suffit généralement. - La vue catégorie permet d’utiliser la configuration **Modèles** et **Liste**.
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Contenus étiquetés**<br />`tags_using_catview` | Activez cette option pour créer des liens par catégorie, permettant ainsi d'utiliser les mises en page 'catégorie' et d'autres configurations de la 'liste d'éléments' comme le filtrage avancé, etc, et permet également de limiter à des catégories spécifiques | — | `0` |
| **Contenus favoris**<br />`favs_using_catview` | Activez cette option pour créer des liens par catégorie, permettant ainsi d'utiliser les mises en page 'catégorie' et d'autres configurations de la 'liste d'éléments' comme le filtrage avancé, etc, et permet également de limiter à des catégories spécifiques | — | `0` |

### Vue annuaire

:::note
Affiche les listes de catégories. Il n'a pas d'élément de menu par défaut. Pour plus d'options de configuration, créez un élément de menu
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Ordre de la liste de catégorie**<br />`cat_orderby` | Ordre la liste des catégories, les options disponibles dépendent des propriétés de l'ensemble des catégories. | — | `order` |
| **Nombre de catégories affichées**<br />`catlimit` | Indique le nombre maximum de catégories à afficher dans la liste. | — | `100` |
