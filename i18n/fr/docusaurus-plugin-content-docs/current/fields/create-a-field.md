---
title: Créer un champ
sidebar_position: 2
---

# Créer un champ

Un champ stocke une donnée structurée dans un contenu FLEXIcontent. Ce guide explique comment créer un champ personnalisé dans FLEXIcontent 5.x, l’associer à des types de contenu, puis le rendre disponible dans le formulaire de contenu et sur le site.

:::info Source
Basé sur FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), notamment `admin/models/forms/field.xml`, `admin/models/field.php`, `admin/views/field/tmpl/default.php`, `admin/tables/flexicontent_fields.php` et `admin/controllers/fields.php`.
:::

## Avant de commencer

- Activez le **plugin du type de champ** nécessaire dans **Système → Gérer → Extensions** (groupe `flexicontent_fields`).
- Créez au moins un **type de contenu** dans **Composants → FLEXIcontent → Types de contenu** ([guide](../content-types/create-a-content-type.md)).
- Votre compte Joomla doit pouvoir ajouter des champs (`CanAddField`) et, pour l’onglet Permissions, configurer les ACL des champs.

:::tip
Avant de créer un nouveau champ, vérifiez si un champ existant avec un [layout personnalisé](./field-layouts.md) suffit. De nombreux besoins de présentation ne nécessitent pas un nouveau champ.
:::

## 1. Ouvrir le gestionnaire de champs

Allez dans **Composants → FLEXIcontent → Champs**, puis cliquez sur **New**. Le titre du formulaire est **New field**.

L’URL directe est :

```text
index.php?option=com_flexicontent&view=fields
```

## 2. Remplir l’en-tête

Le haut du formulaire contient les trois réglages essentiels.

| Réglage | Obligatoire | Remarques |
| --- | --- | --- |
| **Label** | Oui | Texte affiché dans le formulaire de contenu. Peut être une clé de langue Joomla. |
| **Name** | Non | Nom technique utilisé dans les modèles, modules et la base de données. Si vide ou invalide, FLEXIcontent le déduit du libellé. |
| **Field type** | Non | Vaut `text` par défaut. La liste contient les plugins `flexicontent_fields` activés. |

### Règles du nom

- Caractères autorisés : lettres ASCII, chiffres, `_` et `-` (`/^[a-z_0-9-]+$/i`).
- Les noms invalides ou vides sont corrigés automatiquement à partir du libellé ; FLEXIcontent affiche un avertissement.
- Les doublons reçoivent un suffixe `-2`, `-3`, etc.
- Évitez de réutiliser les 14 noms core intégrés : `text`, `created`, `created_by`, `modified`, `modified_by`, `title`, `hits`, `document_type`, `version`, `state`, `voting`, `favourites`, `categories`, `tags`.

:::warning
Choisissez le nom avec soin. Renommer un champ ensuite casse les modèles, modules ou codes personnalisés qui référencent l’ancien nom.
:::

Lorsque vous changez le type de champ, cliquez sur **Apply & Reload** pour charger les paramètres spécifiques au type. Un champ nouveau non enregistré affiche le message « Please apply to see this field specific parameters!!! ».

## 3. Onglet Basic

| Option | Valeur par défaut | Rôle |
| --- | --- | --- |
| **Published** | `1` | Un champ non publié n’est pas chargé dans le formulaire. |
| **Access** | `1` (Public) | Niveau de vue Joomla. Limite la visibilité en frontend. |
| **Ordering** | `999` | Classement général. L’ordre dans le formulaire est défini par type de contenu. |
| **Types** | aucun | Types de contenu autorisés à utiliser ce champ. Stocké dans `#__flexicontent_fields_type_relations`. |

Sélectionnez au moins un type de contenu dans **Types**. Le champ n’est chargé que pour les contenus dont le type est associé ici.

## 4. Onglet Item form

Ces options contrôlent le comportement du champ pendant l’édition d’un contenu :

| Option | Rôle |
| --- | --- |
| **Description** | Texte d’aide affiché dans le formulaire. |
| **Label for form** (`label_form`) | Libellé différent pour le formulaire d’édition. Peut être une clé de langue. |
| **Untranslatable** | Désactive la traduction de la valeur du champ. |
| **Form hidden** (`formhidden`) | `0` Non, `1` Frontend, `2` Backend, `3` Les deux, `4` Si vide. |
| **Values editable** | Limite les personnes pouvant modifier les valeurs existantes. |
| **Edit help** | Contrôle l’affichage de l’aide dans le formulaire. |

Certaines lignes sont masquées lorsque le type de champ sélectionné ne les prend pas en charge. Il n’existe pas d’onglet général d’association aux catégories dans le formulaire du champ : la portée par catégorie vient du modèle/mise en page et d’options propres au type, comme `catids` ou `rootcatid`.

## 5. Onglet Search, filtering

| Option | Rôle |
| --- | --- |
| **Basic index** — `issearch`, `isfilter` | Inclut le champ dans la recherche et les filtres de base. |
| **Advanced index** — `isadvsearch`, `isadvfilter` | Inclut le champ dans la recherche et les filtres avancés. |
| **Rebuild Search Index** | Reconstruit l’index quand FLEXIcontent le signale comme obsolète. |

## 6. Configuration spécifique au type de champ

Le tabset de droite est généré depuis le manifeste XML du plugin sélectionné. Les onglets et options varient selon le type ; les groupes courants sont **Editing**, **Viewing**, **SEO** et **Filtering**.

Options fréquentes :

| Option | Rôle |
| --- | --- |
| `required` | Rend la valeur obligatoire dans le formulaire. |
| `allow_multiple`, `max_values` | Autorise et limite les valeurs multiples. |
| `default_value`, `default_value_use` | Pré-remplit une valeur : `0` nouveaux contenus, `1` chaque édition, `2` affiche aussi quand la valeur est vide. |
| `showon` | Affiche le champ conditionnellement selon un autre champ. |
| `use_ingroup` | Inclut le champ dans un groupe de champs répétable. |
| **Values layout** (`viewlayout`) | Choisissez le [layout d’affichage du champ](./field-layouts.md). |

Les [pages de référence des champs](./index.md) listent toutes les options de chaque type.

## 7. Onglet Permissions

Disponible pour les utilisateurs autorisés à configurer les ACL des champs. Les permissions Joomla sont stockées sur la ressource `com_flexicontent.field.<id>`. Le niveau **Access** du champ et ces règles limitent qui peut voir ou modifier la valeur.

## 8. Enregistrer le champ

La barre d’outils propose **Apply**, **Apply & Reload**, **Save**, **Save & New**, **Save as Copy** (champs non core uniquement) et **Cancel**. Un enregistrement réussi affiche **Field saved**.

À ce stade, le champ existe, mais il n’est pas forcément visible dans le formulaire ni sur le site.

## 9. Placer le champ dans le formulaire de contenu

1. Revenez dans **Composants → FLEXIcontent → Champs**.
2. Filtrez la liste par le type de contenu concerné.
3. Utilisez les contrôles de classement pour positionner le champ dans le formulaire de ce type.

L’ordre est stocké par type de contenu dans `#__flexicontent_fields_type_relations.ordering`.

Pour structurer le formulaire, ajoutez des types de champs structurels :

- `custom_form_html` — marqueurs d’onglets et de groupes, HTML personnalisé.
- `fieldgroup` — groupes de champs répétables.
- `coreprops` — place des propriétés core intégrées comme `alias`, `category`, `access`, `metadata` ou `perms` dans le formulaire.

`coreprops` ne crée pas de nouvelle valeur ; il positionne seulement une propriété core existante.

## 10. Afficher le champ sur le frontend

L’association au type et l’ordre dans le formulaire ne rendent pas le champ visible sur le site. Le frontend utilise les positions des modèles :

1. Ouvrez le **Template manager** FLEXIcontent.
2. Modifiez la mise en page contenu ou catégorie utilisée par votre type/catégorie.
3. Glissez le champ dans une position.
4. Enregistrez le modèle.

Voir [Positions de champs et glisser-déposer](../templates/positions.md).

Deux symptômes fréquents découlent de cette séparation :

| Symptôme | À vérifier |
| --- | --- |
| Le champ est absent du formulaire | Publié, associé au type, niveau d’accès, prise en charge par le type de champ. |
| Le champ est rempli mais pas affiché | Il doit aussi se trouver dans une position du modèle contenu/catégorie actif. |

## Types de champs disponibles

`field_type` correspond au nom d’un plugin `flexicontent_fields` activé.

| Famille | Noms des plugins | Documentation |
| --- | --- | --- |
| Sélection | `radio`, `radioimage`, `checkbox`, `checkboximage`, `select`, `selectmultiple` | [Radio](./radio.md), [Select](./select.md), [Checkbox](./checkbox.md) |
| Propriété simple | `color`, `date`, `text`, `textarea`, `textselect` | [Text](./text.md), [Textarea](./textarea.md), [Date](./date.md) |
| Propriétés multiples | `weblink`, `email`, `phonenumbers`, `termlist` | [Email](./email.md), [Téléphone](./phonenumbers.md) |
| Médias | `file`, `image`, `mediafile`, `sharedmedia`, `addressint` | [Image](./image.md), [File](./file.md), [Adresse](./addressint.md) |
| Structure du formulaire | `subform`, `fieldgroup`, `account_via_submit`, `custom_form_html`, `coreprops` | [Subform](./subform.md), [Groupe de champs](./fieldgroup.md) |
| Aides à l’affichage | `toolbar`, `fcloadmodule`, `fcpagenav`, `linkslist`, `authoritems`, `jprofile`, `comments` | [Toolbar](./toolbar.md), [Charger un module](./fcloadmodule.md) |
| Relations | `relation`, `relation_reverse`, `autorelationfilters` | [Relation](./relation.md), [Relation inverse](./relation_reverse.md) |

Le plugin `core` alimente les champs intégrés et est masqué dans le sélecteur normal.

Si aucun de ces types ne permet de stocker ou de traiter la donnée dont vous avez besoin, [écrivez un nouveau plugin de type de champ](./create-a-field-type.md).

## Champs core et champs personnalisés

FLEXIcontent installe 14 champs core : `text`, `created`, `created_by`, `modified`, `modified_by`, `title`, `hits`, `document_type`, `version`, `state`, `voting`, `favourites`, `categories`, `tags`.

- Les nouveaux champs ont toujours `iscore = 0` ; vous ne pouvez pas créer de champ core.
- Le nom des champs core est en lecture seule.
- Les champs core aux identifiants 1 à 6 ne peuvent pas être dépubliés ni supprimés.
- Les champs core dont l’identifiant est inférieur à 15 ne peuvent pas être copiés.
- Les champs core sont automatiquement associés à tous les types de contenu, sauf `voting` et `favourites`.

Utilisez `coreprops` si vous souhaitez seulement placer une propriété core existante dans le formulaire.

## Les champs FLEXIcontent ne sont pas les champs personnalisés Joomla

| | Champ FLEXIcontent | Champ personnalisé Joomla `com_fields` |
| --- | --- | --- |
| Stockage | `#__flexicontent_fields`, valeurs dans les relations champ/contenu. | `#__fields`, `#__fields_values`. |
| Types de champs | Plugins `flexicontent_fields`. | Plugins de champs Joomla. |
| Association | Types de contenu FLEXIcontent. | Composants/catégories Joomla. |
| Ordre dans le formulaire | Par type de contenu FLEXIcontent. | Groupes de champs Joomla. |
| Affichage frontend | Positions des modèles FLEXIcontent. | Surcharges de mise en page du composant Joomla. |

## Dépannage

| Problème | Cause probable |
| --- | --- |
| Les options spécifiques au type sont vides | Cliquez sur **Apply & Reload** après avoir choisi le type. |
| Nom de champ en doublon | FLEXIcontent ajoute `-2` ; choisissez un nom plus explicite. |
| Nom modifié par le système | Le nom d’origine était invalide ; modèles et modules doivent être mis à jour. |
| La recherche/filtre ne renvoie rien | Index obsolète ; utilisez **Rebuild Search Index**. |
| Formulaire cassé après ajout de marqueurs | Marqueurs d’onglets/groupes `custom_form_html` non appariés. |
| Impossible de supprimer ou dépublier un champ | Restriction sur un champ core. |
| Niveau d’accès réinitialisé à Public | Le niveau enregistré était invalide pour ce champ. |

## Références officielles

- [Démarrer avec FLEXIcontent](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/330-starting-with-flexicontent-basic-usage.html)
- [Liste des fonctionnalités Champs](https://www.flexicontent.org/features/fields.html)
- [Afficher les champs dans la vue contenu](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/261-how-to-displat-fields-in-the-frontend-item-view.html)
- [Afficher les champs dans la vue catégorie](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/262-how-to-display-fields-in-the-frontend-category-view.html)
- [Tutoriels en anglais](https://www.flexicontent.org/documentation/tutorials-english.html)
