---
sidebar_position: 2
---

# Premiers pas

Ce parcours montre comment mettre en place une première structure de contenu avec FLEXIcontent.

## 1. Choisir ou créer un type de contenu

Un **type de contenu** définit la structure d'une famille de contenus. FLEXIcontent fournit le type `Article` par défaut, mais vous pouvez créer par exemple `Événement`, `Fiche produit` ou `Livre blanc`.

Dans l'administration : **Composants → FLEXIcontent → Types de contenu**. Voir [Créer un type de contenu](../content-types/create-a-content-type.md) pour la procédure détaillée.

:::tip
Commencez avec un seul type. Vous pourrez le dupliquer ou créer d'autres types plus tard.
:::

## 2. Ajouter des champs

Associez ensuite les champs nécessaires au type : un titre, un texte, une date, une image, une liste de choix, etc.

Un même champ peut être utilisé par plusieurs types de contenu. Vous pouvez définir s'il est obligatoire, sa valeur par défaut, son ordre d'affichage et ses permissions.

Voir [Champs](../concepts/champs.md) pour les concepts et [Créer un champ](../fields/create-a-field.md) pour la procédure pas à pas.

## 3. Créer des catégories

Créez une arborescence de catégories dans **Catégories**. Les catégories FLEXIcontent sont imbriquables et un contenu peut appartenir à plusieurs catégories.

Voir [Créer une catégorie](../categories/create-a-category.md) pour la procédure et [Catégories](../concepts/categories.md) pour les concepts.

## 4. Créer un premier contenu

Dans **Contenus**, créez un élément du type choisi, affectez-le à une catégorie, puis remplissez les champs définis à l'étape 2.

À ce stade, le contenu existe dans l'administration. Il reste à le rendre visible sur le site.

## 5. Créer le menu d'affichage

Créez un élément de menu pointant vers une **vue catégorie** ou une **vue multi-catégories** FLEXIcontent. Choisissez la catégorie à afficher, le type de contenu et le modèle à utiliser.

Vous obtenez une page de liste avec les filtres et le tri disponibles selon les champs configurés.

## 6. Affiner l'affichage

FLEXIcontent permet de personnaliser :

- le **modèle de vue catégorie** (liste, grille, tableau…) ;
- le **modèle de vue contenu** (fiche détaillée) ;
- l'affichage de chaque champ (préfixe, suffixe, mise en forme, plugin de contenu) ;
- les **modules** pour afficher des contenus ailleurs sur le site.

Voir [Modèles](../concepts/modeles.md).

## Étape suivante

Une fois ces bases en place, explorez les [ressources officielles](../ressources.md) pour approfondir la configuration, le workflow et les API de FLEXIcontent.
