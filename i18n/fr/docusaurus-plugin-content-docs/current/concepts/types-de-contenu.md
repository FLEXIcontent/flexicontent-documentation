---
sidebar_position: 1
---

# Types de contenu

Le **type de contenu** est le concept central de FLEXIcontent. Il correspond à une fiche de saisie préconfigurée pour une famille de contenus.

## Définition

Un type regroupe :

- les **champs** disponibles dans le formulaire de saisie ;
- les **options du formulaire** : champs obligatoires, valeurs par défaut, validation ;
- les **modèles d'affichage** utilisés pour la fiche et la liste ;
- les **catégories** autorisées ;
- les **règles ACL** (qui peut créer, modifier, publier) ;
- les réglages de **recherche**, de **filtrage** et de **SEO**.

Le type `Article` est configuré par défaut. Tous les autres types — blog, événement, annuaire, produit, portfolio, documentation, etc. — sont à créer selon vos besoins.

## Bonnes pratiques

- Donnez au type un nom simple et explicite : il sera visible par les rédacteurs.
- Ne multipliez pas les types pour des différences qui pourraient être gérées par un champ de sélection.
- Utilisez les **champs partagés** pour éviter de recréer les mêmes données dans plusieurs types.
- Pensez aux **droits d'accès** dès la création du type, notamment si la saisie se fait en frontend.

## Exemples

| Type | Champs typiques |
| --- | --- |
| Événement | Date de début, date de fin, lieu, prix, image |
| Fiche produit | Référence, prix, stock, galerie, caractéristiques |
| Annuaire | Adresse, téléphone, email, carte, catégorie métier |
| Documentation | Sommaire, version, fichier attaché, tags |

## Aller plus loin

- [Créer un type de contenu](../content-types/create-a-content-type.md)
- [Champs](./champs.md)
- [Modèles](./modeles.md)
- [Premiers pas](../demarrage/premiers-pas.md)
