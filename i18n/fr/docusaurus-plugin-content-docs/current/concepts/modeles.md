---
sidebar_position: 4
---

# Modèles d'affichage

FLEXIcontent utilise un système de modèles PHP/CSS pour contrôler le rendu des contenus et des listes.

## Deux grands types de vues

- **Vue contenu** : la fiche détaillée d'un élément.
- **Vues de liste** : catégorie, multi-catégories, tags, favoris, auteurs, recherche avancée.

Chaque vue peut avoir son propre modèle. Vous pouvez également définir des modèles spécifiques par type de contenu ou par élément de menu.

## Compétences nécessaires

Pour créer ou adapter un modèle :

- connaître les bases du **HTML** et du **CSS** ;
- savoir lire des conditions et des boucles en **PHP** ;
- observer les modèles fournis pour comprendre les objets et variables disponibles.

L'interface d'administration permet aussi de placer des champs dans le rendu par glisser-déposer, ce qui couvre de nombreux besoins sans écrire de code.

## Personnaliser sans tout réécrire

Avant de créer un modèle complet depuis zéro :

1. Dupliquez un modèle existant.
2. Ajustez le HTML et les classes CSS.
3. Déplacez les champs dans la mise en page.
4. Testez sur une vue réelle avec plusieurs contenus.

:::warning
Après une mise à jour majeure de FLEXIcontent, vérifiez vos modèles personnalisés. Certains réglages ou classes peuvent nécessiter une adaptation.
:::

## Ressources officielles

- [Présentation des modèles](https://www.flexicontent.org/features/templates.html)
- [Tutoriels modèles](https://www.flexicontent.org/documentation/tutorials-english.html?filter=template+flexicontent)
