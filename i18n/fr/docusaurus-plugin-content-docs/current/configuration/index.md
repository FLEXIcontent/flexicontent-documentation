---
sidebar_position: 1
---

# Configuration

FLEXIcontent regroupe tous les paramètres du composant dans un seul écran de configuration Joomla!. Ouvrez-le depuis **Composants → FLEXIcontent → Options** dans l'administration.

L'écran est divisé en onglets, chacun dédié à un domaine du composant. Chaque onglet dispose de sa propre page de documentation :

| Onglet | Rôle | Détails |
| --- | --- | --- |
| [Options](./options.md) | Paramètres généraux : recherche textuelle, traductions, modèles mobiles, CSS, bibliothèques navigateur, cache, débogage | 52 options |
| [Redirections / SEO](./redirections-seo.md) | Redirections et URL optimisées pour les moteurs de recherche | 12 options |
| [Boutons](./buttons.md) | Boutons de la barre d'outils disponibles dans le backend | 14 options |
| [Vues](./views.md) | Paramètres communs aux vues frontend | 15 options |
| [Vues de catégorie](./category-views.md) | Affichage des listes de catégories et multi-catégories (filtres, tri, liens, etc.) | 181 options |
| [Menus par défaut](./default-menus.md) | Éléments de menu par défaut utilisés par les liens créés par le composant | 9 options |
| [Contenus mis en avant](./featured.md) | Paramètres des contenus mis en avant | 3 options |
| [Formulaire de contenu](./item-form.md) | Mise en page et comportement du formulaire de création/édition d'un contenu | 107 options |
| [Workflow](./workflow.md) | États, permissions et workflow de publication | 27 options |
| [Export CSV](./csv-export.md) | Colonnes et format des exports CSV | 8 options |
| [Gestionnaires backend](./backend-managers.md) | Mise en page des gestionnaires de contenus, champs, types, catégories et fichiers | 54 options |
| [Fichiers](./files.md) | Répertoires de téléversement, extensions autorisées, gestion des images | 53 options |
| [Mise à jour Flexi](./update.md) | Notifications de mise à jour | 1 option |
| [Permissions](./permissions.md) | Règles ACL Joomla! pour le composant | ACL standard |

:::note
Les noms d'options indiqués dans la documentation (par exemple `log_search_queries`) correspondent aux clés enregistrées dans la table de configuration de Joomla!. Ils sont utiles pour définir une valeur par programme ou pour comprendre un export de configuration.
:::

## Par où commencer

Pour la plupart des sites, seuls quelques paramètres doivent être modifiés :

1. [Options](./options.md) — vérifiez le cache (`advcache`) et la méthode de traduction (`flexi_fish`).
2. [Vues de catégorie](./category-views.md) — configurez les filtres et les informations affichées dans les listes.
3. [Workflow](./workflow.md) — adaptez les états de publication à votre processus éditorial.
4. [Fichiers](./files.md) — vérifiez les répertoires de téléversement et les types de fichiers autorisés.

## Source de la documentation

Les pages de configuration sont générées depuis les sources officielles de FLEXIcontent :

- `admin/config.xml` — définition des champs et de leurs valeurs par défaut
- `admin/language/en-GB/en-GB.com_flexicontent.ini` — libellés et descriptions anglais
- le package de traduction française `fr-FR` du [projet Crowdin FLEXIcontent](https://crowdin.com/project/flexicontent-cck-for-joomla)

Le générateur se trouve dans `website/tools/generate_config_docs.py`. Relancez-le après avoir mis à jour les fichiers sources :

```bash
python3 website/tools/generate_config_docs.py
```
