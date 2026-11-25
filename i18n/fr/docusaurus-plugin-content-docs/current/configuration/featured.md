---
sidebar_position: 8
---

# Contenus mis en avant

Paramètres des contenus mis en avant et des catégories utilisées pour les sélectionner.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

### Contenu en vedette

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Utiliser le drapeau en vedette joomla**<br />`use_joomla_featured_flag` | Vous pouvez sélectionner l'utilisation du champ 'En vedette' de Joomla! ou le cacher du formulaire de contenu. Le drapeau 'en vedette' de Joomla! peut être utile, si vous voulez une compatibilité avec les vues et modules non-FLEXIcontent. Une solution plus efficace sont les catégories en vedette de FLEXIcontent. Vous pouvez décider d'utiliser à la fois le drapeau 'En vedette' de Joomla et les catégories en vedette de FLEXIcontent. | — | `1` |

:::note
(a) Toutes les catégories sous ce parent seront considérées comme en vedette. (b) Il est recommandé de ne pas imbriquer vos catégories en vedette, (placez-les à plat)
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Parent des catégories en vedette**<br />`featured_cats_parent` | Les catégories vedettes permettent une gestion plus facile, stylisée et plus intuitive de votre contenu web \"en vedette\" les catégories en vedette sont: (a) **spécialement sélectionnables par vos éditeurs dans le formulaire d'article et n'apparaîtront pas dans l'arborescence normale des catégories du formulaire.** -- (bien sûr) Un éditeur aura besoin du privilège 'créer' sur une catégorie en vedette afin de pouvoir la sélectionner dans la forme de l'élément. -- par ex. les utilisateurs achètent un **abonnement** qui les ajoute à un **groupe d'utilisateurs qui a le droit de créer** sur certaines catégories en vedette (b) **peuvent éventuellement recevoir des marquages spéciaux (balises) dans les listes d'articles / vue d'article,** faisant ainsi ressortir les éléments de contenu de la foule via des balises de style CSS (balises) avec ou sans texte (c) **peut avoir une utilisation spéciale comme être utilisé dans la page d'accueil ou être affecté aux modules** e. . catégories: 'Frontpage', 'Top Slideshow', etc, dans ce cas, vous souhaiteriez cacher les liens directs via le plugin système **FLEXIcontent Advanced Route** (veuillez modifier la configuration du plugin) | — | — |
| **Désactiver le parent de la sous-arborescence**<br />`featured_cats_parent_disable` | Il est généralement souhaitable d’empêcher la sélection de la catégorie racine de la sous-arborescence | — | `1` |
