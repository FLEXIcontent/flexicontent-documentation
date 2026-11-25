---
title: Services Web JSON:API
sidebar_position: 2
---

# Services Web JSON:API

L’API Web Services de Joomla! expose FLEXIcontent via un point d’accès HTTP. C’est la couche utilisée directement par les scripts et par le [serveur MCP](./mcp.md).

## 1. Activer les plugins nécessaires

Dans l’administration Joomla!, allez dans **Système → Gérer → Extensions** et activez :

- **User – Joomla API Token**
- **API Authentication – Joomla Token**
- le plugin **FLEXIcontent Web Services** fourni avec l’extension

Laissez **API Authentication – Basic** désactivé : il enverrait le mot de passe à chaque appel.

Dans **User – Joomla API Token → Allowed User Groups**, gardez la liste aussi courte que possible. Par défaut, seuls les Super Users peuvent avoir un jeton.

## 2. Créer un compte dédié

Créez un utilisateur réservé à l’automatisation. Donnez-lui uniquement les droits dont il a besoin, par exemple la création et la modification dans une seule catégorie.

Accordez à cet utilisateur l’action **Web Services Login** (`core.login.api`) via **Système → Configuration globale → Autorisations**, ou via les autorisations du groupe. Le jeton agit **avec les autorisations Joomla! de cet utilisateur** : l’API n’accorde aucun droit supplémentaire.

## 3. Générer le jeton API

1. Allez dans **Utilisateurs → Gérer** et ouvrez cet utilisateur.
2. Ouvrez l’onglet **Joomla API Token**.
3. Si le champ est vide, enregistrez une fois le profil, puis rouvrez l’onglet.
4. Cliquez sur **Copy** et stockez le jeton dans un gestionnaire de secrets. Joomla! ne pourra plus l’afficher.
5. Vérifiez que le jeton est **actif**.

## 4. URL de base

```text
https://example.com/api/index.php/v1/flexicontent
```

Remplacez `example.com` par votre domaine. N’ajoutez pas de barre oblique finale.

## 5. Tester la connexion

```bash
export FLEXI_API_TOKEN='your-joomla-api-token'

curl -H "Authorization: Bearer $FLEXI_API_TOKEN" \
  "https://example.com/api/index.php/v1/flexicontent/items?page[limit]=1"
```

Vous devez recevoir du JSON. Consultez la [référence des endpoints API](./endpoints.md) pour toutes les routes, tous les filtres et toutes les charges utiles disponibles.

| Réponse | Cause probable |
| --- | --- |
| `401` | Jeton invalide, désactivé ou régénéré. |
| `403` | ACL insuffisante : vérifiez les droits du compte et `core.login.api`. |
| `404` | URL de base ou identifiant incorrect. L’URL doit se terminer par `/v1/flexicontent`, sans barre oblique finale. |
| `422` | Champ ou type invalide lors d’une écriture. Découvrez d’abord les identifiants valides (voir [MCP](./mcp.md) et `flexi_describe`). |

## Liste de contrôle de sécurité

- Utilisez HTTPS en production.
- Stockez le jeton dans un fichier en `0600`, une variable d’environnement ou un trousseau.
- Ne placez jamais le jeton dans un fichier de configuration de client IA.
- Révoquez immédiatement le jeton s’il fuit.
- Gardez l’authentification Basic désactivée.
