---
title: JSON:API Web Services
sidebar_position: 2
---

# JSON:API Web Services

The Joomla! Web Services API exposes FLEXIcontent through an HTTP endpoint. It is the layer used directly by scripts and by the [MCP server](./mcp.md).

## 1. Enable the required plugins

In the Joomla! administrator area, go to **System → Manage → Plugins** and enable:

- **User – Joomla API Token**
- **API Authentication – Joomla Token**
- the **FLEXIcontent Web Services** plugin shipped with the extension

Leave **API Authentication – Basic** disabled: it would send the password on every call.

In **User – Joomla API Token → Allowed User Groups**, keep the list as short as possible. By default, only Super Users may have a token.

## 2. Create a dedicated account

Create a user reserved for automation. Give it only the rights it needs, for example create/edit in a single category.

Grant that user the **Web Services Login** action (`core.login.api`) through **System → Global Configuration → Permissions**, or through the group permissions. The token acts with this user's Joomla! permissions: the API grants no extra rights.

## 3. Generate the API token

1. Go to **Users → Manage** and open the dedicated user.
2. Open the **Joomla API Token** tab.
3. If the field is empty, save the profile once, then reopen the tab.
4. Click **Copy** and store the token in a secret manager. Joomla! cannot display it again.
5. Make sure the token is active.

## 4. Base URL

```text
https://example.com/api/index.php/v1/flexicontent
```

Replace `example.com` with your domain. Do not add a trailing slash.

## 5. Test the connection

```bash
export FLEXI_API_TOKEN='your-joomla-api-token'

curl -H "Authorization: Bearer $FLEXI_API_TOKEN" \
  "https://example.com/api/index.php/v1/flexicontent/items?page[limit]=1"
```

You should receive JSON. See the [API endpoint reference](./endpoints.md) for every available route, filter and payload.

| Response | Likely cause |
| --- | --- |
| `401` | Invalid, disabled or regenerated token. |
| `403` | Insufficient ACL: check the account rights and `core.login.api`. |
| `404` | Wrong base URL or id. The URL must end in `/v1/flexicontent`, with no trailing slash. |
| `422` | Invalid field or type when writing. Discover valid ids first (see [MCP](./mcp.md) and `flexi_describe`). |

## Security checklist

- Use HTTPS in production.
- Store the token in a `0600` file, an environment variable or a keychain.
- Never put the token in an AI client configuration file.
- Revoke the token immediately if it leaks.
- Keep Basic Authentication disabled.
