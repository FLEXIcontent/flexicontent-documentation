---
sidebar_position: 2
---

# Champs

Les **champs** servent à structurer les données d'un contenu. Chaque champ est un plugin Joomla!, ce qui permet d'étendre FLEXIcontent avec de nouveaux types de champs.

## Caractéristiques générales

- Un champ peut être associé à **un ou plusieurs types de contenu**.
- Tous les champs peuvent être **multivalués**, avec réordonnancement par glisser-déposer.
- Les valeurs peuvent être **filtrables** et **recherchables** dans les vues de liste.
- Les champs respectent les **droits d'accès** et disposent d'un historique de valeurs.
- La sortie peut être personnalisée : préfixe, suffixe, séparateur, mise en forme, template de champ, plugins de contenu Joomla!.

## Familles de champs

FLEXIcontent fournit plusieurs dizaines de champs. Les principales familles sont :

### Texte

- Champ texte simple, zone de texte, éditeur HTML.
- Email, téléphone, URL, nombre, code personnalisé.

### Sélection

- Liste déroulante (`select`), liste multiple.
- Boutons radio, cases à cocher, variantes avec images.
- Listes alimentées par des valeurs statiques ou par des requêtes SQL.

### Date et heure

- Saisie de date, plage de dates, formats d'affichage configurables.
- Utilisable comme filtre dans les vues de liste.

### Médias et fichiers

- Image et galerie d'images, avec vignettes et mises en page intégrées.
- Fichier, audio, vidéo.
- Adresse / carte avec géolocalisation.

### Relations

- Champ **Relation** vers d'autres contenus.
- Champ **Relation inverse** pour afficher les contenus qui pointent vers l'élément courant.

### Structure et affichage

- Groupes de champs et onglets dans le formulaire de saisie.
- Champs de présentation : partage social, navigation entre contenus, liste d'auteurs, chargement de module.

:::tip
Avant de créer un nouveau champ, vérifiez si un champ existant combiné à un layout personnalisé ne suffit pas.
:::

Pour la procédure complète, voir [Créer un champ](../fields/create-a-field.md).

## Configuration d'un champ

Les réglages les plus courants sont :

- le **libellé** affiché dans le formulaire ;
- le **type de champ** ;
- les **options de saisie** (valeurs autorisées, taille, format) ;
- la **visibilité** selon le type de contenu et les droits ;
- l'**affichage** dans les vues contenu, catégorie et module ;
- le rôle du champ dans la **recherche et les filtres**.

## Ressources officielles

- [Liste des champs](https://www.flexicontent.org/features/fields.html)
- [Tutoriels sur l'utilisation des champs](https://www.flexicontent.org/documentation/tutorials-english.html?filter=field&cc=88603e3010eb311c02874f047982cf36)
