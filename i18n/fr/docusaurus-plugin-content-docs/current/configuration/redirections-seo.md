---
sidebar_position: 3
---

# Redirections / référencement

Gère les redirections et les URL optimisées pour les moteurs de recherche générées par FLEXIcontent.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

### Redirections

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Page de connexion**<br />`login_page` | Spécifier l'URL de la page de connexion. Remarque : il faut saisir l'URL relative à notre site! | — | `index.php?option=com_users&view=login` |
| **Page d'accès non autorisé (visualisation d'un contenu)**<br />`unauthorized_page` | Spécifiez l'URL / ID du lien de menu de la page vers laquelle vous souhaitez que vos visiteurs / utilisateurs soient dirigés s'ils n'ont pas les droits suffisants pour accéder au contenu sélectionné. **NOTE :** Si vous ne définissez rien ici, ils seront redirigés vers une page 403 (mais toujours avec un message de ce qui s'est passé). **Remarque :** Remarque : L'URL est relative à votre site ! | — | — |

### Référencement et URL SEF

#### Création des URL (/segment1/segment2/...)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **JGLOBAL_SEF_NOIDS_LABEL**<br />`sef_ids` | JGLOBAL_SEF_NOIDS_DESC | — | `0` |
| **Liens des contenus dans les listes de catégories**<br />`item_links_in_listings` | Catégorie utilisée dans les URL des contenus affichés dans les listes de catégories. **Catégorie principale** : les contenus lient toujours leur URL via leur catégorie principale, un contenu a donc une seule URL même s’il est aussi associé à des catégories secondaires. **Catégorie actuelle** : les contenus lient via la catégorie affichée, si le contenu y est associé (un contenu peut alors être accessible via plusieurs URL, mais **rel canonical** pointe toujours vers l’URL de la catégorie principale) | — | `0` |
| **Option de réduction des URL SEF**<br />`add_item_sef_segment` | Par défaut, /item/ est ajouté après l'alias de menu **** dans un lien de MENU CATÉGORIE pour faire une URL SEF pour un élément (article), vous pouvez choisir de ne pas utiliser cela. **NOTE :** Ceci peut être désiré si vous installez FLEXIcontent sur un site Joomla qui a déjà des liens mise en signet et des liens indexés par Google et que vous voulez changer les éléments de menu de la catégorie Joomla pour qu'ils soient des éléments de menu de catégorie FLEXIcontent ou pour un nouveaux sites où vous voulez éviter /item/. ****NOTE : les URL SEF de la catégorie recevront un /category/ si un **élément de menu catégorie alias** est utilisé dans leurs URL SEF (par ex. l'élément de menu de la catégorie parent ou l'élément de menu par défaut est de la catégorie de type), pour éviter ceci : (a) sélectionnez votre élément de menu par défaut (FLEXIcontent) pour être de type 'item' ou 'directory' et (b) réglez pour préférer « élément de menu par défaut » au lieu de « actuel » | — | `1` |
| **Menu par défaut**<br />`default_menu_itemid` | L'élément de menu par défaut pour toutes les URL pour lesquelles un lien de menu plus approprié ne peut pas être trouvé, particulièrement important pour les URL SEF, car les URL SEF /menu_alias/ apparaîtront dans celles-ci. Également si vous voulez supprimer le menu caché de FLEXIcontent puis créer un lien de menu et définir son élément dans cette option. Ce lien de menu peut pointer vers un article de texte général, par exemple la politique de confidentialité, les informations générales, etc | — | — |
| **Élément de menu par défaut dans les URLs**<br />`default_menuitem_preference` | 1. Oui, si aucun autre élément approprié n'a été trouvé : joint ci-dessus si aucun autre élément de menu approprié n'est trouvé. exemple : un lien de menu pointant vers la catégorie de l'élément actuellement affiché. 2. Oui, mais préférer l'élément de menu actif : si aucun autre élément de menu approprié n'est trouvé, il essaiera d'utiliser l'élément de menu actuellement actif, et si l'actif ne pointe pas vers FLEXIcontent il utilisera la valeur par défaut ci-dessus. 3. Non, (force les menu actifs) : si aucun lien de menu approprié n'est trouvé, l'actif sera essayé, si actif ne pointe pas vers FLEXIcontent, alors aucun identifiant de lien de menu ne sera ajouté et composant/flexicontent/ apparaîtra dans l'URL SEF | — | `2` |

#### URL pour le contenu de la langue 'TOUT'

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser les éléments du menu**<br />`route_active_lang` | Les contenus (éléments, catégories, tags) **ayant la langue 'TOUT'** peuvent avoir dans leurs liens URL les alias de liens de menu de n'importe quelle autre langue (si l'autre langue est la langue de l'interface utilisateur) | — | `1` |

#### Fil d'ariane (Module de fil d'ariane)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Supprimer l'élément de menu par défaut**<br />`default_menuitem_nopathway` | Si vous définissez cette valeur sur Oui (RECOMMANDÉ), l'élément de menu par défaut ne sera pas affiché dans le chemin fil d'ariane | — | `1` |
| **Créer le fil de navigation automatiquement**<br />`automatic_pathways` | Le chemin de catégories et de contenus (affiché dans le module de fil de navigation) sera généré automatiquement (a) en supprimant toutes les entrées du menu du fil de navigation et en ajoutant l'arborescence de catégories puis le titre de l'article. NOTE : vous pouvez surcharger ces paramètres pour chaque catégorie, type et contenu. | — | `0` |

#### Indexation des moteurs de recherche

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Tag canonique**<br />`add_canonical` | Ajouter une balise meta canonique dans le code source de vos pages, cela aide les moteurs de recherche à identifier une page visualisée via des URL différentes et lui donner meilleur rang, en ne l'indexant pas plusieurs fois | — | `1` |
| **Nombre de filtre dans l'index**<br />`max_filt_to_index` | Nombre maximum de filtres dans les URL de vue multi-éléments pour permettre l'indexation par les moteurs de recherche, en ajoutant la directive 'robots' rel canonical et index + follow. Notez que ceci inclut le filtre de recherche de texte et aussi les filtres à valeur multiple qui seront comptés comme un seul filtre. Lorsque plus de filtres sont actifs alors la directive sera forcée en no-index, (mais follow) | — | `4` |
