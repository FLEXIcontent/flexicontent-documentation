---
title: API
sidebar_position: 1
---

# API FLEXIcontent

FLEXIcontent 5.x peut être piloté de trois façons complémentaires. Elles utilisent toutes les mêmes autorisations Joomla! : l’API n’accorde jamais de droits que le compte Joomla! choisi ne possède pas déjà.

## Choisir une interface

| Interface | À utiliser quand… | Documentation |
| --- | --- | --- |
| [Services Web JSON:API](./webservices.md) | Une application externe, un script ou un client HTTP doit lire/écrire des contenus avec un jeton Joomla!. | [Services Web](./webservices.md) |
| [Référence des endpoints API](./endpoints.md) | Vous avez besoin du chemin, de la méthode, du filtre ou de la charge utile exacts pour chaque endpoint FLEXIcontent. | [Endpoints](./endpoints.md) |
| [Serveur MCP](./mcp.md) | Un assistant IA (OpenCode, Claude, Cursor, VS Code, Gemini CLI…) doit agir sur le site avec des outils. | [MCP](./mcp.md) |
| [API PHP pour développeurs](./php.md) | Un code Joomla! personnalisé doit créer des contenus, utiliser les modèles FLEXIcontent, lire des champs ou réagir à des événements. | [API PHP](./php.md) |

## Avant de commencer

- Utilisez **FLEXIcontent 5.x** sur **Joomla! 4.x, 5.x ou 6.x**.
- Créez un **compte Joomla! dédié** avec les droits minimaux nécessaires, plutôt qu’un compte Super Utilisateur.
- Activez les **plugins de jeton API Joomla!** et le plugin **FLEXIcontent Web Services**. Laissez **API Authentication – Basic** désactivé.
- Utilisez toujours **HTTPS** en production et stockez le jeton dans un gestionnaire de secrets, jamais dans un fichier de configuration de client IA.

## Exemple HTTP minimal

```bash
export FLEXI_API_TOKEN='your-joomla-api-token'

curl -H "Authorization: Bearer $FLEXI_API_TOKEN" \
  "https://example.com/api/index.php/v1/flexicontent/items?page[limit]=1"
```

Un appel réussi renvoie du JSON. Un `401` signifie que le jeton est invalide ou inactif ; un `403` signifie que le compte Joomla! ne dispose pas des autorisations nécessaires.

## Sources officielles

- [Comment utiliser FLEXIcontent MCP](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/832-how-to-use-flexicontent-mcp.html)
- [Méthodes API (événements déclenchés) pour les plugins de type « flexicontent »](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/632-api-methods-triggered-events-for-plugins-of-type-flexicontent.html)
- [Créer/mettre à jour un contenu avec le modèle d’élément](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/580-how-to-create-a-flexicontent-item-by-calling-the-flexicontent-item-model-in-custom-code.html)
- [Utiliser les modèles de base de données type / champ / étiquette](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/654-how-to-use-type-field-tag-db-models-of-flexicontent-to-create-edit-records.html)
