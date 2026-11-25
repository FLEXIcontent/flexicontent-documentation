---
title: API
sidebar_position: 1
---

# FLEXIcontent API

FLEXIcontent 5.x can be driven in three complementary ways. All of them use the same Joomla! permissions: the API never grants rights that the chosen Joomla! account does not already have.

## Choose an interface

| Interface | Use it when… | Documentation |
| --- | --- | --- |
| [JSON:API Web Services](./webservices.md) | An external application, script or HTTP client needs to read/write content with a Joomla! token. | [Web Services](./webservices.md) |
| [API endpoint reference](./endpoints.md) | You need the exact path, method, filter or payload for every FLEXIcontent endpoint. | [Endpoints](./endpoints.md) |
| [MCP server](./mcp.md) | An AI assistant (OpenCode, Claude, Cursor, VS Code, Gemini CLI…) needs to operate the site through tools. | [MCP](./mcp.md) |
| [PHP developer API](./php.md) | Custom Joomla! code needs to create items, use FLEXIcontent models, read fields or react to events. | [PHP API](./php.md) |

## Before you start

- Use **FLEXIcontent 5.x** on **Joomla! 4.x, 5.x or 6.x**.
- Create a **dedicated Joomla! account** with the minimum required rights, rather than using a Super User account.
- Enable the **Joomla! API token** plugins and the **FLEXIcontent Web Services** plugin. Keep **API Authentication – Basic** disabled.
- Always use **HTTPS** in production and store the token in a secret manager, never in an AI client configuration file.

## Minimal HTTP example

```bash
export FLEXI_API_TOKEN='your-joomla-api-token'

curl -H "Authorization: Bearer $FLEXI_API_TOKEN" \
  "https://example.com/api/index.php/v1/flexicontent/items?page[limit]=1"
```

A successful call returns JSON. A `401` means the token is invalid or inactive; a `403` means the Joomla! account lacks permissions.

## Official sources

- [How to use FLEXIcontent MCP](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/832-how-to-use-flexicontent-mcp.html)
- [API methods (triggered events) for plugins of type "flexicontent"](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/632-api-methods-triggered-events-for-plugins-of-type-flexicontent.html)
- [How to create/update an item by calling the item model](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/580-how-to-create-a-flexicontent-item-by-calling-the-flexicontent-item-model-in-custom-code.html)
- [How to use type / field / tag DB models](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/654-how-to-use-type-field-tag-db-models-of-flexicontent-to-create-edit-records.html)
