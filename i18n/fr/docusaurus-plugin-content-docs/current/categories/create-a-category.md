---
title: Créer une catégorie
sidebar_position: 2
---

# Créer une catégorie

FLEXIcontent utilise les catégories natives de Joomla! et y ajoute ses propres paramètres d’affichage, de filtrage, de liste, de flux RSS, de notification et de modèle. Les catégories se créent depuis **Composants → FLEXIcontent → Catégories**. Elles peuvent être imbriquées, et un contenu peut être associé à une catégorie principale ainsi qu’à des catégories secondaires.

Cette page décrit la procédure dans l’administration. Pour le concept, voir [Catégories](../concepts/categories.md) ; pour tous les réglages, voir [Catégories — options](./options.md).

:::info Source
Basé sur FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), notamment `admin/models/forms/category.xml`, `admin/models/category.php`, `admin/views/category/view.html.php`, `admin/views/category/tmpl/default.php`, `admin/controllers/category.php` et `admin/access.xml`.
:::

## Avant de commencer

- L’ouverture du formulaire de catégorie nécessite la permission composant **Gérer les catégories** (`flexicontent.managecats`, exposée comme `CanCats`).
- La création d’une catégorie nécessite aussi `core.create` sur `com_flexicontent`, ou sur au moins une catégorie. La modification nécessite `core.edit` ou `core.edit.own` sur la catégorie concernée.
- Décidez de la place de la catégorie dans l’arborescence. Le sélecteur **Parent Category** ne propose que les catégories sur lesquelles vous avez la permission de création ou de modification correspondante.
- Préparez le titre, un alias court, le niveau d’accès et la langue avant de commencer.

:::tip
Gardez la première arborescence peu profonde. Vous pourrez imbriquer les catégories plus tard, et l’héritage permet aux catégories enfants de réutiliser les paramètres d’un parent.
:::

Les catégories FLEXIcontent sont stockées dans la table native `#__categories` avec l’extension définie par `FLEXI_CAT_EXTENSION` (le réglage par défaut du composant est `com_content`). Utiliser le gestionnaire de catégories FLEXIcontent garantit que les paramètres FLEXIcontent sont enregistrés en même temps que les champs standard de catégorie Joomla!.

## 1. Ouvrir le gestionnaire de catégories

Allez dans **Composants → FLEXIcontent → Catégories**. L’URL directe est :

```text
index.php?option=com_flexicontent&view=categories
```

Cliquez sur **New**. Le titre de la barre d’outils est **New Category** (`FLEXI_NEW_CATEGORY`).

## 2. Remplir l’onglet Basic

L’onglet **Basic** contient l’identité et les réglages de disponibilité.

| Réglage | Obligatoire / défaut | Remarques |
| --- | --- | --- |
| **Title** (`title`) | Obligatoire | Nom de la catégorie affiché dans les listes et les menus. |
| **Alias** (`alias`) | Facultatif ; généré depuis le titre | Utilisé dans les URL SEF. |
| **Description** (`description`) | Facultative | Affichée dans la vue catégorie lorsque les paramètres d’affichage l’autorisent. |
| **Parent Category** (`parent_id`) | Racine Joomla! par défaut | Choisissez le parent dans l’arborescence. La catégorie courante et ses descendants ne peuvent pas être leur propre parent. |
| **Published** (`published`) | `1` | `1` = publiée, `0` = non publiée, `2` = archivée, `-2` = corbeille. |
| **Access** (`access`) | Public (`1`) | Niveau de vue Joomla! autorisé à voir la catégorie. |
| **Language** (`language`) | Toutes (`*`) | Assigne une langue de contenu, ou conserve Toutes pour un site multilingue utilisant les associations. |
| **Category notes** (`note`) | Facultative | Note interne affichée dans le gestionnaire de catégories de l’administration. |
| **Image** / **Image alt** (`image`, `image_alt`) | Facultatifs | Image et texte alternatif utilisés par le modèle de catégorie. |

Le **Path**, les informations de création/modification et les vues sont en lecture seule. Après l’enregistrement, la barre d’outils propose aussi un bouton **Preview**.

## 3. Enregistrer la catégorie

La barre d’outils propose :

| Bouton | Usage |
| --- | --- |
| **Add** / **Apply & Reload** | Enregistrer et recharger le formulaire. Pour une nouvelle catégorie, le bouton est libellé **Add** (`FLEXI_ADD`). |
| **Apply (fast save)** | Disponible pour une catégorie existante ; enregistre sans rechargement complet. |
| **Save** | Enregistrer et revenir au gestionnaire de catégories. |
| **Save & New** | Enregistrer, puis ouvrir une catégorie vide. |
| **Save as Copy** | Disponible pour une catégorie existante ; utile pour dupliquer une structure. |
| **Preview** | Ouvrir le lien frontend de la catégorie dans une nouvelle fenêtre (catégories existantes uniquement). |
| **Cancel** / **Close** | Quitter le formulaire. |

Un enregistrement réussi affiche **Category saved**.

## 4. Configurer les onglets d’affichage

La section **Display** contient les réglages qui distinguent les catégories FLEXIcontent des catégories natives de Joomla!.

| Onglet | À configurer |
| --- | --- |
| Publishing, Meta | Informations de publication, meta description et meta keywords. |
| Associations | Associations linguistiques des catégories, lorsque les associations sont activées. |
| Category display header | Boutons impression, e-mail, flux et CSV, bouton **Add new item**, style des icônes et placement des boutons. |
| Search & filter form | Les filtres proposés au-dessus de la liste des contenus. |
| Layout | Layout de catégorie (`clayout`), layout mobile facultatif (`clayout_mobile`), sélecteur de layout, layouts autorisés/affichés et paramètres propres au layout. |
| Items list | Tri, pagination, colonnes et champs utilisés dans la liste. |
| RSS feeds | Paramètres du flux RSS pour cette catégorie. |
| Parameters handling | Source d’héritage et copie unique des paramètres. |
| Notifications | Paramètres de notification ; les destinataires spécifiques à la catégorie nécessitent l’activation de **Allow category specific** dans la configuration du composant. |
| Permissions | ACL de la catégorie : création, modification, changement d’état, suppression et export CSV. |

La [structure des modèles](../templates/structure.md) définit la vue catégorie ; les [positions de modèle](../templates/positions.md) décident où ses blocs apparaissent. Les tableaux exhaustifs des options se trouvent sur la page [Catégories — options](./options.md).

## 5. Comprendre l’héritage des paramètres

Une valeur qui n’est ni vide ni **Use Global** remplace la valeur héritée. Pour la vue catégorie, l’ordre de surcharge est :

```text
Composant → Catégorie héritée → Catégorie → Auteur → Menu
```

Le réglage **Inherit parameters from** (`inheritcid`) accepte :

| Valeur | Signification |
| --- | --- |
| Vide (`Use Global`) | Utiliser le réglage du composant. |
| `0` (`Component only`) | Utiliser uniquement les paramètres du composant. |
| `-1` (`Parent categories (multi-level)`) | Hériter de l’arborescence parente, jusqu’au premier parent qui n’hérite pas. |
| Un identifiant de catégorie | Hériter de cette catégorie précise. L’héritage est alors d’un seul niveau et ne se propage pas davantage. |

Pour que l’héritage fonctionne, laissez les propres paramètres de la catégorie enfant vides ou réglés sur **Use Global**. Lorsqu’un layout précis est sélectionné, ses paramètres font également partie de l’ensemble hérité.

**Copy all parameters from** (`copycid`) est différent de l’héritage : lors du prochain **Save** ou **Apply & Reload**, il remplace les paramètres de cette catégorie par une copie de ceux de la catégorie source, puis le sélecteur est vidé. Cela ne se produit qu’une fois.

## 6. Utiliser la nouvelle catégorie

1. Ouvrez le type de contenu utilisé par les rédacteurs et autorisez cette catégorie dans ses réglages **Authoring**. Voir [Créer un type de contenu](../content-types/create-a-content-type.md).
2. Créez un contenu et sélectionnez la nouvelle catégorie comme catégorie principale ; ajoutez des catégories secondaires si nécessaire.
3. Créez un élément de menu pointant vers une **vue catégorie** ou une **vue multi-catégories** FLEXIcontent, puis choisissez la catégorie et le layout à afficher.
4. Ouvrez la page frontend et vérifiez l’en-tête, les filtres, la liste et le layout.

Un élément de menu peut remplacer les paramètres de la catégorie pour sa propre vue. C’est pourquoi une même catégorie peut avoir un aspect différent à deux endroits du site.

:::caution
Changer le parent d’une catégorie modifie sa position dans l’arborescence imbriquée. Vérifiez les permissions et les liens de menu existants avant de déplacer une catégorie qui contient déjà des contenus.
:::

## Dépannage

| Problème | Cause probable |
| --- | --- |
| Impossible d’ouvrir le formulaire de catégorie | `flexicontent.managecats` est refusé. |
| Impossible de créer une catégorie sous un parent | `core.create` est refusé sur ce parent, ou le parent ne peut pas être utilisé car il se trouve sous la catégorie courante. |
| Catégorie absente du formulaire de contenu | Catégorie non publiée, niveau d’accès trop élevé ou non autorisée par les réglages Authoring du type de contenu. |
| Les paramètres ne s’appliquent pas | Ils sont vides ou réglés sur **Use Global**, donc une valeur héritée gagne. Vérifiez l’ordre de surcharge ci-dessus. |
| Mauvais layout en frontend | `clayout` est vide/hérité, ou l’élément de menu remplace le layout de la catégorie. |
| La copie des paramètres n’a rien changé | Sélectionnez la catégorie source, puis cliquez sur **Save** ou **Apply & Reload** ; le choix est vidé après un enregistrement. |
| Chaînes `FLEXI_...` affichées littéralement | Clé de langue manquante ou fichiers de langue périmés ; videz le cache Joomla. |

## Références officielles

- [Démarrer avec FLEXIcontent (utilisation de base)](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/330-starting-with-flexicontent-basic-usage.html)
- [Utiliser une catégorie FC comme page d’accueil](https://flexicontent.org/documentation/tutorials-english/75-basic-usage/194-how-to-use-an-fc-category-as-homepage-frontpage.html)
- [Créer plusieurs catégories « À la une »](https://flexicontent.org/documentation/tutorials-english/75-basic-usage/273-how-to-make-multiple-featured-categories.html)
- [Template FLEXIcontent — Partie 1 : La structure](https://flexicontent.org/documentation/tutorials-english/84-advanced-tutorials/335-template-flexicontent-part-1-the-structure.html)
