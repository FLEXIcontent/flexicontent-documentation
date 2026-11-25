---
title: Référence des endpoints API
sidebar_position: 3
---

# Référence des endpoints API

Cette page liste tous les endpoints HTTP exposés par le plugin FLEXIcontent Web Services. Elle décrit l’implémentation de l’API FLEXIcontent 5.3 et suppose que les plugins et le jeton API décrits dans [Services Web JSON:API](./webservices.md) sont déjà configurés.

Tous les chemins sont relatifs à l’URL de base de l’API :

```text
https://example.com/api/index.php/v1/flexicontent
```

Envoyez `Accept: application/vnd.api+json` avec chaque requête et authentifiez-vous avec `Authorization: Bearer $FLEXI_API_TOKEN`. Dans les chemins ci-dessous, `:id` désigne l’identifiant numérique de l’enregistrement.

## Référence rapide

| Méthode | Chemin | Action | Succès |
| --- | --- | --- | --- |
| GET | `/items` | Liste des contenus | `200` |
| GET | `/items/:id` | Lecture d’un contenu | `200` |
| POST | `/items` | Création d’un contenu | `201` |
| PATCH | `/items/:id` | Mise à jour partielle d’un contenu | `200` |
| DELETE | `/items/:id` | Suppression d’un contenu | `204` |
| GET | `/categories` | Liste des catégories | `200` |
| GET | `/categories/:id` | Lecture d’une catégorie | `200` |
| POST | `/categories` | Création d’une catégorie | `201` |
| PATCH | `/categories/:id` | Mise à jour partielle d’une catégorie | `200` |
| DELETE | `/categories/:id` | Suppression d’une catégorie | `204` |
| GET | `/tags` | Liste des étiquettes | `200` |
| GET | `/tags/:id` | Lecture d’une étiquette | `200` |
| POST | `/tags` | Création d’une étiquette | `201` |
| PATCH | `/tags/:id` | Mise à jour partielle d’une étiquette | `200` |
| DELETE | `/tags/:id` | Suppression d’une étiquette | `204` |
| GET | `/types` | Liste des types de contenu | `200` |
| GET | `/types/:id` | Lecture d’un type de contenu | `200` |
| POST | `/types` | Création d’un type de contenu | `201` |
| PATCH | `/types/:id` | Mise à jour partielle d’un type de contenu | `200` |
| DELETE | `/types/:id` | Suppression d’un type de contenu | `204` |
| GET | `/fields` | Liste des champs personnalisés | `200` |
| GET | `/fields/:id` | Lecture d’un champ personnalisé | `200` |
| POST | `/fields` | Création d’un champ personnalisé | `201` |
| PATCH | `/fields/:id` | Mise à jour partielle d’un champ personnalisé | `200` |
| DELETE | `/fields/:id` | Suppression d’un champ personnalisé | `204` |
| POST | `/media` | Envoi d’un fichier ou d’une image | `201` |

Il n’existe pas de route de liste, de détail, de mise à jour ou de suppression pour `/media` : cette ressource implémente uniquement l’envoi de fichiers.

## Conventions communes

### Format des documents JSON:API

Les réponses de liste et de détail utilisent un document JSON:API. Les attributs de la ressource se trouvent sous `data.attributes` ; les relations sous `data.relationships`.

```json
{
  "data": [
    {
      "type": "items",
      "id": "138",
      "attributes": {
        "title": "Toulouse",
        "state": 1
      },
      "relationships": {
        "category": { "data": { "type": "categories", "id": "17" } }
      }
    }
  ],
  "meta": {
    "pagination": {
      "current": 1,
      "total-pages": 3,
      "total-items": 42
    }
  }
}
```

Les erreurs utilisent le tableau `errors` standard de JSON:API.

```json
{
  "errors": [
    {
      "status": "422",
      "title": "Unprocessable Entity",
      "detail": "title, catid and type_id are required to create an item."
    }
  ]
}
```

### Pagination et tri

Tous les endpoints de liste acceptent :

| Paramètre | Signification |
| --- | --- |
| `page[limit]` | Nombre d’enregistrements par page. |
| `page[offset]` | Nombre d’enregistrements à ignorer. Un offset au-delà de la fin renvoie `404`. |
| `list[ordering]` | Colonne de tri autorisée. Les colonnes inconnues sont ignorées. |
| `list[direction]` | `asc` ou `desc`. |

### Filtres et ACL

- Seuls les paramètres `filter[...]` documentés sont acceptés. Les filtres inconnus sont ignorés.
- Les non-gérants sont toujours limités aux enregistrements publiés et accessibles. Ils ne peuvent pas élargir leur accès avec `filter[state]` ou `filter[access]`.
- Un enregistrement masqué ou inaccessible renvoie `404` sur une requête de détail, et non `403`. Cela évite de révéler son existence.
- Les gérants disposant de `core.manage` sur `com_flexicontent` peuvent demander tous les états et tous les niveaux d’accès.

### Charges utiles d’écriture

Les endpoints d’écriture acceptent un objet JSON plat. Une enveloppe JSON:API est également acceptée :

```json
{
  "data": {
    "type": "items",
    "attributes": {
      "title": "My item"
    }
  }
}
```

Pour une requête PATCH, n’envoyez que les attributs qui doivent changer. Les valeurs core, les textes, les étiquettes, les catégories et les valeurs de champs personnalisés omis sont conservés. Le corps de la requête prévaut toujours sur un paramètre de requête `data[...]`, et un `id` fourni par le client ne modifie jamais l’enregistrement adressé par l’URL.

## Contenus

### GET /items

Renvoie une liste paginée de contenus FLEXIcontent.

| Paramètre | Signification |
| --- | --- |
| `filter[search]` | Recherche dans les titres de contenus. |
| `filter[state]` | État de publication. Les gérants peuvent utiliser `-5`, `-2`, `0` et `1`. Forcé à `1` pour les non-gérants. |
| `filter[category]` | Identifiant de la catégorie FLEXIcontent principale. Le filtre est exact : les sous-catégories ne sont pas incluses. |
| `filter[type]` | Identifiant du type de contenu FLEXIcontent. |
| `filter[language]` | Balise de langue, par exemple `fr-FR`. |
| `filter[author]` | Identifiant de l’auteur Joomla. |
| `filter[access]` | Niveau d’accès Joomla. Ignoré ou intersecté avec les niveaux de l’utilisateur pour les non-gérants. |
| `filter[featured]` | Indicateur « en vedette ». |
| `filter[tag]` | Identifiant d’étiquette FLEXIcontent. |
| `filter[field]` | Nom ou identifiant numérique d’un champ personnalisé. |
| `filter[field_value]` | Valeur à comparer. Ignoré sans `filter[field]`. |
| `filter[field_match]` | `exact` (par défaut) ou `like` / `contains`. |

Le filtre sur champ personnalisé compare la valeur stockée. `like` est utile pour les valeurs sérialisées ou partielles ; `exact` convient aux valeurs simples numériques, radio ou texte. Un champ inconnu ou interdit renvoie une liste vide plutôt qu’une erreur.

Les valeurs autorisées de `list[ordering]` sont `id`, `title`, `alias`, `catid`, `state`, `access`, `created`, `modified`, `ordering`, `language` et `type_id`, avec leurs alias SQL.

### GET /items/:id

Renvoie un seul contenu. La représentation de détail ajoute `introtext`, `fulltext`, `metakey`, `metadesc`, `images`, `urls`, `attribs`, `metadata`, `version`, `note` et `flexi_fields`.

`flexi_fields` est une table indexée par nom de champ. Il n’est présent que sur l’endpoint de détail, jamais dans les listes.

```json
{
  "field30": {
    "id": 47,
    "name": "field30",
    "label": "City",
    "field_type": "text",
    "value": "Toulouse",
    "raw": "Toulouse",
    "display": "Toulouse"
  }
}
```

Les relations exposées sur les contenus sont `category`, `categories`, `created_by`, `modified_by` et `tags`. Les attributs `category_ids` et `tag_ids` contiennent des identifiants FLEXIcontent ; la relation `tags` utilise les identifiants Joomla issus de `jtag_id`.

### POST /items

Crée un contenu. `title`, `catid` et `type_id` sont obligatoires. Si `catid` est omis, le premier identifiant de `categories` ou `category_ids` est utilisé.

| Attribut | Remarques |
| --- | --- |
| `title` | Obligatoire. |
| `catid` | Obligatoire sauf s’il peut être déduit de `categories`. Identifiant de la catégorie principale. |
| `type_id` | Obligatoire. Identifiant du type de contenu FLEXIcontent. |
| `alias` | Alias d’URL. |
| `state` | État de publication. Sa modification exige l’autorisation de modifier l’état. |
| `access`, `language` | Niveau d’accès Joomla et balise de langue. |
| `created_by`, `created_by_alias` | Informations sur l’auteur. Les autorisations legacy peuvent remplacer ces valeurs. |
| `text` | Texte principal ; FLEXIcontent le sépare au marqueur « readmore ». |
| `introtext`, `fulltext` | Acceptés à la place de `text` ; une mise à jour partielle conserve la contrepartie stockée. |
| `tags`, `tag_ids` | Identifiants d’étiquettes FLEXIcontent, et non le `jtag_id` Joomla. |
| `categories`, `category_ids` | Identifiants de catégories FLEXIcontent supplémentaires. |
| `fields`, `custom`, `flexi_fields` | Valeurs personnalisées indexées par nom de champ. `fields` est recommandé. |
| `metakey`, `metadesc`, `note` | Métadonnées et note d’administration. |
| `publish_up`, `publish_down`, `featured`, `ordering` | Données de publication et de classement. Protégées par les autorisations legacy. |

```bash
curl -X POST \
  -H "Authorization: Bearer $FLEXI_API_TOKEN" \
  -H "Accept: application/vnd.api+json" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New item",
    "catid": 17,
    "type_id": 3,
    "state": 1,
    "language": "en-GB",
    "text": "Intro text",
    "tags": [7, 21],
    "categories": [19],
    "fields": {
      "field30": "Toulouse"
    }
  }' \
  "https://example.com/api/index.php/v1/flexicontent/items"
```

Un appel réussi renvoie `201` et la représentation du contenu créé lorsqu’il est visible par l’utilisateur du jeton.

### PATCH /items/:id

Met à jour partiellement un contenu. Les mêmes attributs que pour POST sont acceptés ; aucun n’est obligatoire. La modification de l’état exige l’autorisation correspondante. Un appel réussi renvoie `200` et la représentation mise à jour.

### DELETE /items/:id

Supprime un contenu via le modèle legacy FLEXIcontent. Renvoie `204` avec un corps vide en cas de succès.

## Catégories

Les catégories sont stockées dans `#__categories` sous l’extension configurée dans les paramètres du composant. L’extension par défaut est `com_content`.

### GET /categories

| Paramètre | Signification |
| --- | --- |
| `filter[search]` | Recherche dans le titre, l’alias ou le chemin. |
| `filter[state]` | État de publication. Gérants uniquement ; forcé à `1` sinon. |
| `filter[parent_id]` | Identifiant de la catégorie parente directe. |
| `filter[level]` | Niveau d’imbrication de la catégorie. |
| `filter[language]` | Balise de langue. |
| `filter[access]` | Niveau d’accès Joomla. Gérants uniquement. |

Attributs de liste : `id`, `title`, `alias`, `extension`, `published`, `access`, `parent_id`, `level`, `path`, `language`, `item_count`. Les réponses de détail ajoutent `note`, `description`, `metadesc`, `metakey`, `metadata`, les champs de création et de modification, `hits` et `item_count`.

### POST /categories

`title` est obligatoire lors de la création.

| Attribut | Remarques |
| --- | --- |
| `title` | Obligatoire. |
| `alias`, `note`, `description` | Facultatifs. |
| `parent_id`, `published`, `access`, `language` | Facultatifs ; valeurs par défaut `1`, `1`, `1` et `*`. |
| `metadesc`, `metakey`, `metadata`, `params`, `layouts` | Facultatifs. |

La réponse inclut l’attribut calculé `extension`.

### PATCH /categories/:id

Accepte les mêmes attributs que POST. Les attributs omis conservent leur valeur stockée.

### DELETE /categories/:id

Renvoie `204` en cas de succès.

## Étiquettes

Les étiquettes FLEXIcontent sont exposées avec leur pont Joomla facultatif. L’attribut `tag_ids` des contenus utilise les identifiants FLEXIcontent ; la relation `tags` utilise le `jtag_id` Joomla.

### GET /tags

| Paramètre | Signification |
| --- | --- |
| `filter[search]` | Recherche dans le nom ou l’alias. |
| `filter[state]` | État de publication. Gérants uniquement ; forcé à `1` sinon. |
| `filter[jtag]` | `1` ne renvoie que les étiquettes pontées, `0` uniquement les étiquettes non pontées. |

Attributs de liste : `id`, `name`, `alias`, `published`, `jtag_id`, `jtag_title`, `item_count`. Les réponses de détail ajoutent `checked_out`, `checked_out_time`, `jtag_alias`, `jtag_published` et `jtag_access`.

### POST /tags

`name` est obligatoire.

| Attribut | Remarques |
| --- | --- |
| `name` | Obligatoire. |
| `alias`, `published` | Facultatifs. |
| `jtag_id` | Identifiant Joomla facultatif ; il doit exister. Le modèle legacy gère le pont. |

### PATCH /tags/:id

Accepte les mêmes attributs que POST. Les attributs omis conservent leur valeur stockée.

### DELETE /tags/:id

Renvoie `204` en cas de succès.

## Types de contenu

### GET /types

| Paramètre | Signification |
| --- | --- |
| `filter[search]` | Recherche dans le nom ou l’alias. |
| `filter[state]` | État de publication. Gérants uniquement ; forcé à `1` sinon. |
| `filter[access]` | Niveau d’accès Joomla. Gérants uniquement. |

Attributs de liste : `id`, `name`, `alias`, `published`, `access`, `itemscreatable`, `item_count`. Les réponses de détail ajoutent `description`, `checked_out` et `checked_out_time`.

### POST /types

`name` est obligatoire.

| Attribut | Remarques |
| --- | --- |
| `name` | Obligatoire. |
| `alias`, `description` | Facultatifs. |
| `published`, `access`, `itemscreatable` | Facultatifs ; valeurs par défaut `1`, `1` et `0`. |
| `attribs`, `layouts`, `iflayout` | Valeurs de configuration facultatives. |

### PATCH /types/:id

Accepte les mêmes attributs que POST. Les attributs omis conservent leur valeur stockée.

### DELETE /types/:id

Renvoie `204` en cas de succès.

## Champs personnalisés

### GET /fields

| Paramètre | Signification |
| --- | --- |
| `filter[search]` | Recherche dans le nom, le libellé ou l’alias. |
| `filter[state]` | État de publication. Gérants uniquement ; forcé à `1` sinon. |
| `filter[core]` | `0` ne renvoie que les champs personnalisés, `1` que les champs core. |
| `filter[form]` | `1` inclut les pseudo-champs de configuration `form_*`. Ils sont masqués par défaut. |
| `filter[type]` | Champs associés à cet identifiant de type de contenu. |
| `filter[access]` | Niveau d’accès Joomla. Gérants uniquement. |

Attributs de liste : `id`, `name`, `label`, `field_type`, `iscore`, `published`, `access`, `ordering`. Les réponses de détail ajoutent `description`.

### POST /fields

`label` est obligatoire. La création de champs core via l’API est refusée.

| Attribut | Remarques |
| --- | --- |
| `label` | Obligatoire. |
| `field_type` | Facultatif ; valeur par défaut `text`. |
| `name`, `description` | Facultatifs. |
| `published`, `access`, `ordering` | Facultatifs ; valeurs par défaut `1`, `1` et `999`. |
| `issearch`, `isadvsearch`, `isfilter`, `isadvfilter` | Indicateurs de recherche et de filtre. |
| `untranslatable`, `formhidden`, `valueseditable`, `edithelp`, `positions` | Paramètres de comportement du champ. |
| `attribs` | Paramètres du champ. |
| `tid`, `type_ids`, `types` | Identifiants des types de contenu associés. Le modèle legacy reconstruit les relations à l’enregistrement. |
| `layouts`, `iflayout` | Configuration de modèle facultative copiée dans `attribs`. |

### PATCH /fields/:id

Accepte les mêmes attributs que POST. Les attributs omis conservent leur valeur stockée.

### DELETE /fields/:id

Renvoie `204` en cas de succès.

## Envoi de fichiers

### POST /media

Envoie un fichier dans le stockage FLEXIcontent. Seul POST est enregistré pour cette ressource.

L’endpoint accepte soit un corps JSON, soit un formulaire multipart avec une partie `file`.

| Attribut JSON | Remarques |
| --- | --- |
| `filename` | Obligatoire en mode JSON. Doit contenir une extension. |
| `content_base64` | Contenu du fichier encodé en base64. |
| `content` | Contenu brut, accepté comme alternative à `content_base64`. |
| `tmp_name`, `error` | Utilisés en interne pour les envois multipart ; envoyez plutôt la partie `file`. |
| `field_id` | Identifiant de champ FLEXIcontent facultatif. Applique les limites d’extension et de taille du champ et choisit la zone de stockage. |
| `item_id` | Obligatoire pour les champs image en mode dossier. |
| `secure` | Stockage sécurisé (`1`) ou médias publics (`0`) pour les champs en mode base de données. |
| `alt`, `description` | Texte alternatif de l’image et description du fichier. |

```bash
curl -X POST \
  -H "Authorization: Bearer $FLEXI_API_TOKEN" \
  -H "Accept: application/vnd.api+json" \
  -H "Content-Type: application/json" \
  -d '{
    "filename": "photo.jpg",
    "content_base64": "BASE64_CONTENT",
    "field_id": 24,
    "item_id": 138,
    "alt": "Photo"
  }' \
  "https://example.com/api/index.php/v1/flexicontent/media"
```

La réponse renvoie une ressource `media` avec `id`, `filename`, `original_name`, `extension`, `size`, `mime_type`, `secure`, `storage`, `url`, `path`, `field_id`, `field_type` et `field_value`.

- Les fichiers en mode base de données sont stockés dans le répertoire uploads ou medias de FLEXIcontent et enregistrés dans `#__flexicontent_files`. `field_value` est l’identifiant du fichier.
- Les champs image en mode dossier stockent l’original dans le dossier du champ pour l’élément. `field_value` est un tableau de valeur image et peut être transmis directement à `POST /items` ou `PATCH /items/:id` via l’objet `fields`.
- Les champs image utilisant le mode source Joomla media/intro-full ne peuvent pas recevoir d’envoi via l’API.

L’envoi exige `flexicontent.uploadfiles`, `flexicontent.managefiles` ou `core.manage` sur `com_flexicontent`.

## Codes de statut

| Statut | Signification |
| --- | --- |
| `200` | Lecture ou mise à jour partielle réussie. |
| `201` | Contenu, enregistrement de taxonomie ou fichier créé. |
| `204` | Suppression réussie ; le corps de la réponse est vide. |
| `400` | Le corps de la requête n’est pas un JSON valide. |
| `401` | Jeton manquant, invalide, désactivé ou régénéré. |
| `403` | Le compte Joomla ne dispose pas de l’autorisation requise. |
| `404` | Route inconnue, enregistrement invisible, identifiant inconnu ou offset au-delà de la fin de la liste. |
| `422` | Échec de validation, attribut obligatoire manquant ou envoi invalide. |
| `500` | Erreur serveur ou du modèle legacy. Les détails internes ne sont pas exposés pour les échecs de suppression. |

## Outils liés

Le [serveur MCP](./mcp.md) est un client léger de ces endpoints. Chaque outil `flexi_*` correspond à un ou plusieurs appels décrits ici ; les mêmes autorisations du compte Joomla s’appliquent.
