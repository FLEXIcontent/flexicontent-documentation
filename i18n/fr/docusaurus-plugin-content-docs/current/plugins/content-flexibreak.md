---
sidebar_position: 2
---

# Contenu — Flexibreak

FLEXIcontent fournit des plugins pour la recherche, le routage, les notifications, les boutons de l’éditeur et les sitemaps. Activez-les et configurez-les depuis **Extensions → Plugins**. Les 35 plugins de types de champs sont documentés dans la section [Champs](../fields/index.md).

> Alternative FLEXIcontent au plugin saut de page standard (offre une pagination instantanée en javascript et autres alternatives). Permettre la création d'un article paginé avec table des matières optionnelle. Insérer des sauts de page à l'aide du bouton de saut de page normalement trouvé sous le texte dans un article. Le saut de page sera affiché dans la fenêtre de texte comme une simple ligne…

:::info Source
Cette page est générée depuis `plugins/content/flexibreak/flexibreak.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Basique

### De base

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode d’affichage**<br />`display_method` | Sélectionner la méthode d’affichage : (a) afficher toutes les pages et défiler jusqu’à la page souhaitée, (b et c) afficher uniquement la page active via JavaScript ou via rechargement de la page | `multilist` | `0` = Dérouelement aux ancres<br />`1` = Changement en ligne<br />`2` = Rechargement de la page<br />`3` = Onglets<br />`4` = Panneaux déroulant | `1` (Changement en ligne) |

#### Pagination

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Liens précédent / suivant**<br />`pagination` | Définit où les contrôles de navigation sont affichés | `radio` | `0` = Cacher<br />`1` = Après la table des matières<br />`2` = Avant la description<br />`3` = Après la description | `3` (Après la description) |
| **Compteur de pages**<br />`show_prevnext_count` | Afficher le numéro de la page actuelle sur le nombre total de pages | `radio` | `0` = Cacher<br />`1` = Afficher | `1` (Afficher) |

#### Table des matières

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Table des matières**<br />`multipage_toc` | Vous pouvez masquer la table des matières (la navigation de page peut rester affichée) | `multilist` | `0` = Cacher<br />`1` = Afficher | `1` (Afficher) |
| **Liens de retour à la table des matières**<br />`return_anchors` | Vous pouvez afficher des liens d’ancrage de retour à la table des matières à la fin de chaque page | `radio` | `0` = Cacher<br />`1` = Afficher<br />`2` = Auto | `1` (Afficher) |
| **Titre de la table**<br />`toc_title` | Vous pouvez masquer le titre « Table des matières » | `radio` | `0` = Cacher<br />`1` = Afficher | `1` (Afficher) |
| **Position de la table des matières**<br />`toc_placement` | Vous pouvez ajouter la table des matières avant la description du contenu ou la placer via la variable item-&gt;toc ; dans ce dernier cas, personnalisez item.php / item_html5.php de votre modèle | `radio` | `0` = variable $item-&gt;toc<br />`1` = Avant la description | `1` (Avant la description) |

#### Lien pour afficher toutes les pages

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher ien**<br />`allpages_link` | Afficher un lien pour permettre aux utilisateurs d'afficher toutes les pages de contenu à la fois | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Texte personnalisé**<br />`custom_allpages` | Une chaîne de langue personnalisées comme titre pour le lien 'Toutes les Pages' | `text` | — | `FLEXIBREAK_ALL_PAGES` (Toutes les pages) |

#### Lien d'introduction

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Texte du lien**<br />`introtext_title` | Afficher un lien pour permettre aux utilisateurs d'afficher le texte d'introduction | `multilist` | `0` = Titre de l'article<br />`1` = Texte personnalisé | `1` (Texte personnalisé) |
| **Texte personnalisé**<br />`custom_introtext` | Une chaîne de langue personnalisées comme titre pour le lien 'texte d’introduction' | `text` | — | `FLEXIBREAK_INTRODUCTION` (Introduction) |
