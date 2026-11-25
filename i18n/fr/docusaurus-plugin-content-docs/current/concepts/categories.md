---
sidebar_position: 3
---

# Catégories

FLEXIcontent utilise les catégories natives de Joomla!, mais ajoute deux fonctionnalités importantes : l'imbrication illimitée et la multi-catégorisation.

## Arborescence illimitée

Contrairement à la gestion native de Joomla!, les catégories FLEXIcontent peuvent être imbriquées sans profondeur maximale pratique. Vous pouvez donc construire une arborescence du type :

```text
Documentation
├── Guide utilisateur
│   ├── Installation
│   └── Saisie des contenus
└── Guide développeur
    ├── API
    └── Champs personnalisés
```

## Catégorie principale et catégories secondaires

Un contenu peut être affecté à plusieurs catégories :

- la **catégorie principale** est utilisée notamment pour l'héritage des permissions et le routage par défaut ;
- les **catégories secondaires** permettent d'ajouter d'autres classifications (thématique, région, année, etc.).

Dans l'administration, la catégorie principale est affichée en bleu dans la table des contenus.

:::tip
Choisissez la catégorie principale en fonction du contexte de lecture le plus fréquent. Les autres affectations servent surtout au filtrage et aux vues secondaires.
:::

## Éviter le contenu dupliqué

Lorsqu'un contenu apparaît dans plusieurs catégories, FLEXIcontent peut générer un lien canonique pour éviter que les moteurs de recherche ne considèrent ces pages comme des doublons.

## Vues de liste

Les vues catégorie et multi-catégories affichent les contenus avec :

- le tri et la pagination ;
- les filtres sur les champs ;
- les sous-catégories ;
- les options de modèle propres à la vue.

Voir [Modèles](./modeles.md) pour personnaliser ces vues.

## Aller plus loin

- [Créer une catégorie](../categories/create-a-category.md)
- [Options des catégories](../categories/options.md)
