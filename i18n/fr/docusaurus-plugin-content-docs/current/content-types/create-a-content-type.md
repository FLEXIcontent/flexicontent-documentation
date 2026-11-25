---
title: Créer un type de contenu
sidebar_position: 2
---

# Créer un type de contenu

Un **type de contenu** est un enregistrement de l’administration qui définit les champs, les règles de saisie et les paramètres d’affichage d’une famille de contenus. FLEXIcontent installe le type `Article` par défaut ; toute autre structure — événement, fiche produit, annuaire, portfolio — se crée depuis **Composants → FLEXIcontent → Types de contenu**.

Cette page décrit la procédure dans l’administration. Pour écrire le code PHP d’un nouveau type de champ, voir [Créer un type de champ](../fields/create-a-field-type.md).

:::info Source
Basé sur FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), notamment `admin/models/forms/type.xml`, `admin/models/type.php`, `admin/tables/flexicontent_types.php`, `admin/views/type/view.html.php`, `admin/views/type/tmpl/default.php`, `admin/controllers/types.php` et `admin/access.xml`.
:::

## Avant de commencer

- Votre compte Joomla doit disposer de la permission composant **Gérer les types de contenu** (`flexicontent.managetypes`, exposée comme `CanTypes`) pour créer ou modifier un type.
- Pour ajouter des champs personnalisés, vous devez aussi avoir `flexicontent.createfield`.
- Préparez la liste des champs souhaités et vérifiez qu’un simple champ de sélection ne suffit pas avant de créer plusieurs types similaires.
- Créez les catégories que vous voulez autoriser ([guide](../categories/create-a-category.md)), ou prévoyez de le faire après la création du type.

:::tip
Commencez avec un seul type et dupliquez-le ensuite avec **Enregistrer sous forme de copie**. Un type est plus facile à affiner par étapes qu’à repenser une fois que des contenus l’utilisent.
:::

## 1. Ouvrir le gestionnaire de types

Allez dans **Composants → FLEXIcontent → Types de contenu**. L’URL directe est :

```text
index.php?option=com_flexicontent&view=types
```

Cliquez sur **New**. Le titre de la barre d’outils est **New type** (`FLEXI_ADD_TYPE`).

## 2. Remplir l’en-tête

Le haut du formulaire contient l’identité et les réglages de disponibilité.

| Réglage | Obligatoire / défaut | Remarques |
| --- | --- | --- |
| **Name** (`name`) | Obligatoire | Affiché aux rédacteurs lors du choix d’un type pour un nouveau contenu. Stocké dans `#__flexicontent_types.name`. |
| **Alias** (`alias`) | Facultatif ; généré depuis le nom | Uniquement ASCII, tirets bas autorisés. Utilisé dans les URL et les recherches internes. |
| **Description** | Facultative | Texte affiché lors de la sélection du type pour un nouveau contenu (`FLEXI_REGARDING_ITEM_TYPE_DESCRIPTION_TEXT_USAGE`). |
| **Published** (`published`) | `1` | La dépublication est bloquée tant que des contenus sont associés au type. |
| **Access** (`access`) | Public (`1`) | Niveau de vue Joomla. Limite les utilisateurs pouvant utiliser le type. |
| **Permit Submission** (`itemscreatable`) | `0` | `0` = tout auteur, `1` = masquer le type dans le sélecteur si l’utilisateur n’a pas `core.create`, `2` = l’afficher désactivé. |

L’enregistrement est stocké dans `#__flexicontent_types` ; les paramètres spécifiques au type sont sérialisés dans la colonne `attribs`.

:::note
`Permit Submission` n’accorde pas par lui-même le droit de créer des contenus. Définissez la permission **Create Items** (`core.create`) dans l’onglet **Permissions** du type. Cet onglet expose aussi **Change main category**, **Change secondary categories** et **Change featured category**.
:::

## 3. Appliquer avant de configurer

Pour un nouveau type, cliquez sur **Apply** (libellé **Add**) après avoir saisi le nom. Cela crée l’enregistrement et recharge le formulaire afin que les paramètres de layout et les options spécifiques au type soient disponibles.

La barre d’outils propose :

| Bouton | Usage |
| --- | --- |
| **Apply** / **Apply & Reload** | Enregistrer et recharger le formulaire. Pour un nouveau type, c’est le bouton libellé **Add**. |
| **Apply (fast save)** | Disponible pour un enregistrement existant ; enregistre sans rechargement complet. |
| **Save** | Enregistrer et revenir au gestionnaire de types. |
| **Save & New** | Enregistrer, puis ouvrir un type vide. |
| **Save as Copy** | Disponible pour un type existant ; utile pour dupliquer une structure. |
| **Cancel** | Fermer le formulaire. |

Un enregistrement réussi affiche **Type saved**.

## 4. Configurer les onglets du type

Le formulaire est réparti en onglets. Toute valeur qui n’est ni vide ni **Use Global** remplace la valeur héritée d’un niveau supérieur. L’ordre complet de surcharge pour la vue contenu est :

```text
Composant → Menu → Catégorie → Type de contenu → Contenu
```

| Onglet | À configurer |
| --- | --- |
| Description | Description affichée aux rédacteurs sur l’écran de sélection du type. |
| Core fields | Libellés, descriptions et règles d’affichage des 14 champs intégrés (titre, texte principal, catégories, dates, tags, vote, etc.). |
| Authoring | Arborescence de catégories autorisée, catégorie par défaut et comportement du formulaire de saisie. |
| SEO | Titre de page, métadonnées et élément de menu par défaut utilisé pour construire les URL des contenus. |
| Item view | Layouts de contenu autorisés, layout par défaut (`ilayout`) et layout mobile. |
| Search view | Champs recherchables, priorité des résultats, filtres et affichage des résultats. |
| Item form | Layouts des formulaires frontend et backend (`form_ilayout_fe`, `form_ilayout_be`) et comportement du formulaire. |
| Notifications | E-mails envoyés lors de la soumission ou des changements de statut. |
| Items manager | Filtres et colonnes par défaut dans la liste des contenus de l’administration. |
| Layout / Themes | Layout de contenu et ses paramètres. Les champs sont placés dans des positions de modèle. |

La liste exhaustive des options se trouve sur la page [Types de contenu — options](./options.md).

:::caution
Évitez de changer le type d’un contenu **existant**. FLEXIcontent avertit que les valeurs des champs qui ne sont pas communs à l’ancien et au nouveau type seront perdues. Le choix du type est prévu au moment de la création du contenu.
:::

## 5. Associer les champs au type

L’association des champs se fait dans le gestionnaire **Champs**, pas dans le formulaire du type.

1. Allez dans **Composants → FLEXIcontent → Champs**.
2. Créez un champ ou modifiez un champ existant.
3. Dans l’onglet **Basic**, sélectionnez ce type de contenu dans **Types**. Un champ peut être associé à plusieurs types.
4. Cliquez sur **Apply & Reload** si vous avez changé le type de champ, puis sur **Save**.
5. Dans le formulaire du type, utilisez les contrôles d’ordre pour placer le champ dans le formulaire de contenu.

L’association est stockée dans `#__flexicontent_fields_type_relations`, avec l’`ordering` propre au type utilisé dans le formulaire de contenu. Les champs core sont automatiquement associés à tous les types de contenu, sauf `voting` et `favourites`.

Voir [Créer un champ](../fields/create-a-field.md) pour la procédure complète. Pour structurer un long formulaire, ajoutez des marqueurs `custom_form_html` pour les onglets/fieldsets ou `fieldgroup` pour des groupes répétables.

:::tip
Si un nouveau champ n’apparaît pas, vérifiez qu’il est publié, associé à ce type et accessible à votre niveau d’utilisateur. Videz aussi le cache Joomla après avoir modifié les associations.
:::

## 6. Choisir les modèles d’affichage

Dans l’onglet **Layout / Themes**, sélectionnez le layout de contenu qui rendra les éléments de ce type. Les [positions de modèle](../templates/positions.md) décident *où* les champs apparaissent ; les [layouts de champ](../fields/field-layouts.md) décident *comment* leurs valeurs sont rendues.

Un élément de menu pointant vers une vue catégorie ou multi-catégories peut remplacer le layout du type pour cette vue. C’est pourquoi un même type peut avoir un aspect différent à deux endroits du site.

## 7. Créer et tester un contenu

1. Allez dans **Composants → FLEXIcontent → Contenus** et cliquez sur **New**.
2. Sélectionnez le nouveau type. Sa description s’affiche dans le sélecteur de type.
3. Choisissez une catégorie, remplissez les champs associés et enregistrez.
4. Créez un élément de menu pointant vers une **vue catégorie** ou une **vue multi-catégories** FLEXIcontent pour voir la liste en frontend.
5. Ouvrez le contenu pour vérifier le layout de la vue contenu et les valeurs des champs.

## Dépannage

| Problème | Cause probable |
| --- | --- |
| Type absent du sélecteur | Type non publié, niveau d’accès trop élevé, ou `core.create` refusé par les ACL du type. |
| Aucun champ personnalisé dans le formulaire | Champ non associé à ce type, non publié ou restreint par accès. |
| Options spécifiques au type vides | Cliquez d’abord sur **Apply** pour créer l’enregistrement, puis rechargez le formulaire. |
| Impossible de dépublier ou supprimer le type | Des contenus sont encore associés. Déplacez ou supprimez-les d’abord. |
| Des valeurs ont disparu après changement de type | L’ancien et le nouveau type n’ont pas les mêmes champs. Ne changez pas le type d’un contenu existant. |
| Chaînes `FLEXI_...` affichées littéralement | Clé de langue manquante ou fichiers de langue périmés ; videz le cache Joomla. |
| Le frontend utilise un autre layout | Une valeur au niveau menu, catégorie ou contenu remplace celle du type. Vérifiez l’ordre de surcharge. |
| Nouveau champ absent du type | Videz le cache Joomla ; les relations champs/types et les chemins de layout sont mis en cache. |

## Références officielles

- [Démarrer avec FLEXIcontent (utilisation de base)](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/330-starting-with-flexicontent-basic-usage.html)
- [Petit tour d’horizon de FLEXIcontent](https://flexicontent.org/documentation/tutorials-english/83-starting-tutorials/355-eng-4-flexicontent-small-turn-arround-flexicontent.html)
- [Fonctionnalités Types de contenu](https://www.flexicontent.org/features/content-types.html)
