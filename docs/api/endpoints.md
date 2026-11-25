---
title: API endpoint reference
sidebar_position: 3
---

# API endpoint reference

This page lists every HTTP endpoint exposed by the FLEXIcontent Web Services plugin. It describes the FLEXIcontent 5.3 API implementation and assumes the plugins and API token described in [JSON:API Web Services](./webservices.md) are already configured.

All paths are relative to the API base URL:

```text
https://example.com/api/index.php/v1/flexicontent
```

Send `Accept: application/vnd.api+json` with every request and authenticate with `Authorization: Bearer $FLEXI_API_TOKEN`. In the paths below, `:id` denotes the numeric id of the record.

## Quick reference

| Method | Path | Action | Success |
| --- | --- | --- | --- |
| GET | `/items` | List items | `200` |
| GET | `/items/:id` | Read one item | `200` |
| POST | `/items` | Create an item | `201` |
| PATCH | `/items/:id` | Partially update an item | `200` |
| DELETE | `/items/:id` | Delete an item | `204` |
| GET | `/categories` | List categories | `200` |
| GET | `/categories/:id` | Read one category | `200` |
| POST | `/categories` | Create a category | `201` |
| PATCH | `/categories/:id` | Partially update a category | `200` |
| DELETE | `/categories/:id` | Delete a category | `204` |
| GET | `/tags` | List tags | `200` |
| GET | `/tags/:id` | Read one tag | `200` |
| POST | `/tags` | Create a tag | `201` |
| PATCH | `/tags/:id` | Partially update a tag | `200` |
| DELETE | `/tags/:id` | Delete a tag | `204` |
| GET | `/types` | List content types | `200` |
| GET | `/types/:id` | Read one content type | `200` |
| POST | `/types` | Create a content type | `201` |
| PATCH | `/types/:id` | Partially update a content type | `200` |
| DELETE | `/types/:id` | Delete a content type | `204` |
| GET | `/fields` | List custom fields | `200` |
| GET | `/fields/:id` | Read one custom field | `200` |
| POST | `/fields` | Create a custom field | `201` |
| PATCH | `/fields/:id` | Partially update a custom field | `200` |
| DELETE | `/fields/:id` | Delete a custom field | `204` |
| POST | `/media` | Upload a file or image | `201` |

There is no list, detail, update or delete route for `/media`: the resource only implements uploads.

## Common conventions

### JSON:API document shape

List and detail responses use a JSON:API document. Resource attributes are nested under `data.attributes`; relationships are nested under `data.relationships`.

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

Errors use the standard JSON:API `errors` array.

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

### Pagination and ordering

All list endpoints accept:

| Parameter | Meaning |
| --- | --- |
| `page[limit]` | Number of records per page. |
| `page[offset]` | Number of records to skip. An offset past the end returns `404`. |
| `list[ordering]` | Allowed sort column. Unknown columns are ignored. |
| `list[direction]` | `asc` or `desc`. |

### Filters and ACL

- Only the documented `filter[...]` parameters are accepted. Unknown filters are ignored.
- Non-managers are always restricted to published, accessible records. They cannot widen their access with `filter[state]` or `filter[access]`.
- A hidden or inaccessible record returns `404` on a detail request, not `403`. This avoids revealing whether the record exists.
- Managers with `core.manage` on `com_flexicontent` may request all states and access levels.

### Write payloads

Write endpoints accept a flat JSON object. A JSON:API envelope is also accepted:

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

For PATCH requests, only send the attributes that must change. Omitted core values, text, tags, categories and custom field values are preserved. The request body always wins over a `data[...]` query parameter, and a client-supplied `id` never changes the record addressed by the URL.

## Items

### GET /items

Returns a paginated list of FLEXIcontent items.

| Parameter | Meaning |
| --- | --- |
| `filter[search]` | Search in item titles. |
| `filter[state]` | Publication state. Managers may use `-5`, `-2`, `0` and `1`. Forced to `1` for non-managers. |
| `filter[category]` | Main FLEXIcontent category id. The filter is exact: child categories are not included. |
| `filter[type]` | FLEXIcontent content type id. |
| `filter[language]` | Language tag, for example `fr-FR`. |
| `filter[author]` | Joomla author id. |
| `filter[access]` | Joomla access level. Ignored or intersected with the user levels for non-managers. |
| `filter[featured]` | Featured flag. |
| `filter[tag]` | FLEXIcontent tag id. |
| `filter[field]` | Custom field name or numeric id. |
| `filter[field_value]` | Value to compare. Ignored without `filter[field]`. |
| `filter[field_match]` | `exact` (default) or `like` / `contains`. |

The custom field filter compares the stored value. `like` is useful for serialized or partial values; `exact` is intended for simple numeric, radio or text values. An unknown or unauthorized field returns an empty list rather than an error.

Allowed `list[ordering]` values are `id`, `title`, `alias`, `catid`, `state`, `access`, `created`, `modified`, `ordering`, `language` and `type_id`, with their SQL aliases.

### GET /items/:id

Returns one item. The detail representation adds `introtext`, `fulltext`, `metakey`, `metadesc`, `images`, `urls`, `attribs`, `metadata`, `version`, `note` and `flexi_fields`.

`flexi_fields` is a map keyed by field name. It is only present on the detail endpoint, never in lists.

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

Relationships exposed on items are `category`, `categories`, `created_by`, `modified_by` and `tags`. Attributes `category_ids` and `tag_ids` contain FLEXIcontent ids; the `tags` relationship uses Joomla tag ids from `jtag_id`.

### POST /items

Creates an item. `title`, `catid` and `type_id` are required. If `catid` is omitted, the first id in `categories` or `category_ids` is used.

| Attribute | Notes |
| --- | --- |
| `title` | Required. |
| `catid` | Required unless derivable from `categories`. Main category id. |
| `type_id` | Required. FLEXIcontent content type id. |
| `alias` | URL alias. |
| `state` | Publication state. Changing it requires state-edit permission. |
| `access`, `language` | Joomla access level and language tag. |
| `created_by`, `created_by_alias` | Author information. Legacy permissions may override these values. |
| `text` | Canonical body text; FLEXIcontent splits it at the readmore marker. |
| `introtext`, `fulltext` | Accepted instead of `text`; a partial patch keeps the stored counterpart. |
| `tags`, `tag_ids` | FLEXIcontent tag ids, not Joomla `jtag_id`. |
| `categories`, `category_ids` | Additional FLEXIcontent category ids. |
| `fields`, `custom`, `flexi_fields` | Custom values keyed by field name. `fields` is recommended. |
| `metakey`, `metadesc`, `note` | Metadata and administrator note. |
| `publish_up`, `publish_down`, `featured`, `ordering` | Publishing and ordering data. Protected by legacy permissions. |

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

A successful call returns `201` and the created representation when it is visible to the token user.

### PATCH /items/:id

Partially updates an item. The same attributes as POST are accepted; none is mandatory. State changes require the state-edit permission. A successful call returns `200` and the updated representation.

### DELETE /items/:id

Deletes an item through the legacy FLEXIcontent model. Returns `204` with an empty body on success.

## Categories

Categories are stored in `#__categories` under the extension configured in the component parameters. The default extension is `com_content`.

### GET /categories

| Parameter | Meaning |
| --- | --- |
| `filter[search]` | Search in title, alias or path. |
| `filter[state]` | Publication state. Managers only; forced to `1` otherwise. |
| `filter[parent_id]` | Direct parent category id. |
| `filter[level]` | Category nesting level. |
| `filter[language]` | Language tag. |
| `filter[access]` | Joomla access level. Managers only. |

List attributes: `id`, `title`, `alias`, `extension`, `published`, `access`, `parent_id`, `level`, `path`, `language`, `item_count`. Detail responses add `note`, `description`, `metadesc`, `metakey`, `metadata`, creation and modification fields, `hits` and `item_count`.

### POST /categories

`title` is required on creation.

| Attribute | Notes |
| --- | --- |
| `title` | Required. |
| `alias`, `note`, `description` | Optional. |
| `parent_id`, `published`, `access`, `language` | Optional; defaults are `1`, `1`, `1` and `*`. |
| `metadesc`, `metakey`, `metadata`, `params`, `layouts` | Optional. |

The response includes the computed `extension` attribute.

### PATCH /categories/:id

Accepts the same attributes as POST. Omitted attributes keep their stored values.

### DELETE /categories/:id

Returns `204` on success.

## Tags

FLEXIcontent tags are exposed with their optional Joomla bridge. Attribute `tag_ids` on items uses FLEXIcontent ids; the `tags` relationship uses Joomla `jtag_id`.

### GET /tags

| Parameter | Meaning |
| --- | --- |
| `filter[search]` | Search in name or alias. |
| `filter[state]` | Publication state. Managers only; forced to `1` otherwise. |
| `filter[jtag]` | `1` returns only bridged tags, `0` only unbridged tags. |

List attributes: `id`, `name`, `alias`, `published`, `jtag_id`, `jtag_title`, `item_count`. Detail responses add `checked_out`, `checked_out_time`, `jtag_alias`, `jtag_published` and `jtag_access`.

### POST /tags

`name` is required.

| Attribute | Notes |
| --- | --- |
| `name` | Required. |
| `alias`, `published` | Optional. |
| `jtag_id` | Optional Joomla tag id; it must exist. The legacy model manages the bridge. |

### PATCH /tags/:id

Accepts the same attributes as POST. Omitted attributes keep their stored values.

### DELETE /tags/:id

Returns `204` on success.

## Content types

### GET /types

| Parameter | Meaning |
| --- | --- |
| `filter[search]` | Search in name or alias. |
| `filter[state]` | Publication state. Managers only; forced to `1` otherwise. |
| `filter[access]` | Joomla access level. Managers only. |

List attributes: `id`, `name`, `alias`, `published`, `access`, `itemscreatable`, `item_count`. Detail responses add `description`, `checked_out` and `checked_out_time`.

### POST /types

`name` is required.

| Attribute | Notes |
| --- | --- |
| `name` | Required. |
| `alias`, `description` | Optional. |
| `published`, `access`, `itemscreatable` | Optional; defaults are `1`, `1` and `0`. |
| `attribs`, `layouts`, `iflayout` | Optional configuration values. |

### PATCH /types/:id

Accepts the same attributes as POST. Omitted attributes keep their stored values.

### DELETE /types/:id

Returns `204` on success.

## Custom fields

### GET /fields

| Parameter | Meaning |
| --- | --- |
| `filter[search]` | Search in name, label or alias. |
| `filter[state]` | Publication state. Managers only; forced to `1` otherwise. |
| `filter[core]` | `0` returns custom fields only, `1` core fields only. |
| `filter[form]` | `1` includes `form_*` configuration pseudo-fields. They are hidden by default. |
| `filter[type]` | Fields attached to this content type id. |
| `filter[access]` | Joomla access level. Managers only. |

List attributes: `id`, `name`, `label`, `field_type`, `iscore`, `published`, `access`, `ordering`. Detail responses add `description`.

### POST /fields

`label` is required. Creating core fields through the API is refused.

| Attribute | Notes |
| --- | --- |
| `label` | Required. |
| `field_type` | Optional; defaults to `text`. |
| `name`, `description` | Optional. |
| `published`, `access`, `ordering` | Optional; defaults are `1`, `1` and `999`. |
| `issearch`, `isadvsearch`, `isfilter`, `isadvfilter` | Search and filter flags. |
| `untranslatable`, `formhidden`, `valueseditable`, `edithelp`, `positions` | Field behaviour settings. |
| `attribs` | Field parameters. |
| `tid`, `type_ids`, `types` | Attached content type ids. The legacy model rebuilds the relations on save. |
| `layouts`, `iflayout` | Optional layout configuration copied into `attribs`. |

### PATCH /fields/:id

Accepts the same attributes as POST. Omitted attributes keep their stored values.

### DELETE /fields/:id

Returns `204` on success.

## Media uploads

### POST /media

Uploads a file into FLEXIcontent storage. Only POST is registered for this resource.

The endpoint accepts either a JSON body or a multipart form with a `file` part.

| JSON attribute | Notes |
| --- | --- |
| `filename` | Required in JSON mode. Must include an extension. |
| `content_base64` | Base64-encoded file content. |
| `content` | Raw file content, accepted as an alternative to `content_base64`. |
| `tmp_name`, `error` | Used internally for multipart uploads; send the `file` part instead. |
| `field_id` | Optional FLEXIcontent field id. Applies the field extension and size limits and selects the storage area. |
| `item_id` | Required for folder-mode image fields. |
| `secure` | Store in secure uploads (`1`) or public medias (`0`) for DB-mode fields. |
| `alt`, `description` | Image alternative text and file description. |

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

The response returns a `media` resource with `id`, `filename`, `original_name`, `extension`, `size`, `mime_type`, `secure`, `storage`, `url`, `path`, `field_id`, `field_type` and `field_value`.

- DB-mode files are stored in the FLEXIcontent uploads or medias directory and registered in `#__flexicontent_files`. `field_value` is the file id.
- Folder-mode image fields store the original in the field item folder. `field_value` is an image value array and can be passed directly to `POST /items` or `PATCH /items/:id` through the `fields` object.
- Image fields using the Joomla media/intro-full source mode cannot be uploaded to through the API.

Uploads require `flexicontent.uploadfiles`, `flexicontent.managefiles` or `core.manage` on `com_flexicontent`.

## Status codes

| Status | Meaning |
| --- | --- |
| `200` | Read or partial update succeeded. |
| `201` | Item, taxonomy record or upload was created. |
| `204` | Delete succeeded; the response body is empty. |
| `400` | The request body is not valid JSON. |
| `401` | Missing, invalid, disabled or regenerated token. |
| `403` | The Joomla account lacks the required permission. |
| `404` | Unknown route, invisible record, unknown id, or offset past the end of the list. |
| `422` | Validation failure, missing required attribute, or invalid upload. |
| `500` | Server or legacy model error. Internal details are not exposed for delete failures. |

## Related tools

The [MCP server](./mcp.md) is a thin client over these endpoints. Each `flexi_*` tool maps to one or more calls described here; the same Joomla account permissions apply.
