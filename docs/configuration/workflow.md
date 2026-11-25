---
sidebar_position: 10
---

# Workflow

Publication states, permissions and the editorial workflow.

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

#### Workflow

## Basic Workflow

#### Default state for new items

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Backend**<br />`new_item_state` | Preselected (default) state for newly created items | — | `1` |
| **Frontend**<br />`new_item_state_fe` | Preselected (default) state for newly created items | — | `1` |

#### Forced state for new items (for non-publishers)

:::note
- Pending Approval (Produces immediate Notification Emails) - Draft (user will manually set state to Pending Approval by a Request Publication Approval button)
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Backend**<br />`non_publishers_item_state` | The state that will be forced on new items created by authors that cannot publish | — | `-4` |
| **Frontend**<br />`non_publishers_item_state_fe` | The state that will be forced on new items created by authors that cannot publish | — | `-3` |

## Versioning Configuration

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable versioning**<br />`use_versioning` | Enable the versioning feature for the FLEXIcontent component. | — | `1` |
| **Version comparing**<br />`allow_versioncomparing` | Disable version comparing. NOTE: We noticed that version comparing sometimes produces unexpected results depending on the editor. This parameter allows you to disable it to avoid confusing your clients. | — | `1` |
| **Versions kept**<br />`nr_versions` | Choose the number of version you want to keep for each item. The higher this number is the bigger your database size will increase. Take care when choosing a big value like 50 or 100. | — | `10` |
| **# versions per page**<br />`versionsperpage` | The number of versions you wish to display per page | — | `5` |
| **Publish changes (new version)**<br />`auto_approve` | Select to allow user to publish changes (new version) at later time. This can be useful to preview changes before making them public | — | `1` |

## Notifications

:::note
Content submit/change notifications
:::

:::note
Notification emails use Joomla's mail templates. Edit the subject and body of each notification in **System → Mail Templates**, filtering on the **FLEXIcontent** extension. Available tags include: **&#123;TITLE&#125;**, **&#123;STATE&#125;**, **&#123;CREATOR&#125;**, **&#123;MODIFIER&#125;**, **&#123;EDITOR_NAME&#125;**, **&#123;CREATED&#125;**, **&#123;MODIFIED&#125;**, **&#123;CATEGORIES&#125;**, **&#123;VIEW_URL&#125;**, **&#123;EDIT_URL_FE&#125;**, **&#123;EDIT_URL_BE&#125;**, **&#123;NOTIFY_TEXT&#125;**, **&#123;CATEGORY_TEXT&#125;**. FlexiContent custom fields are available as **&#123;FIELD_FIELDNAME&#125;** or directly as **&#123;FIELDNAME&#125;** (field name in uppercase, non alphanumeric characters replaced by underscores, e.g. **&#123;FIELD_FLOORS&#125;** or **&#123;FLOORS&#125;**), and all non-core fields together as **&#123;FIELDS&#125;**. A field name never overrides a core tag such as **&#123;TITLE&#125;**. **Conditional blocks:** the template subject, text body and HTML body can contain **&#123;if ...&#125;...&#123;elseif ...&#125;...&#123;else&#125;...&#123;/if&#125;** blocks. Context variables: **catid**, **incat**, **state_id**, **lang**, **type_id**, **item_id**, **author_id**, **editor_id**. Custom fields are tested with **field_name** (e.g. **&#123;if field_floors&#125;Floor: &#123;FIELD_FLOORS&#125;&#123;/if&#125;**). Operators: **=**, **!=**, **in**, **not in**, **contains**, **not contains**, **&gt;**, **&gt;=**, **=100000&#125;Premium&#123;/if&#125;**. Keywords and string comparisons are case-insensitive. Conditions only affect the text, not the recipients. They are evaluated on the template content stored in Mail Templates; the shipped defaults use language keys and must be edited and saved once to contain conditional text. Invalid conditions keep the content and never block the email.
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Enable notifications**<br />`enable_notifications` | Select to enable sending notification emails about content submits / updates | — | `0` |
| **Debug notifications**<br />`nf_enable_debug` | Enable this to display debugging information (selected mail template, recipients, subject and body) after saving. This option does **not** control whether notifications are sent: notification emails are evaluated and sent on **every save operation**, according to the recipients and states configured above. | — | `0` |

### Email creation

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Send emails as BCC**<br />`nf_send_as_bcc` | Enable this to prevent email recipients from seeing other email recipients. **NOTE**: this will force the administrator email of the website to be the main recipient of the notification email | — | `1` |

### Email Recipients

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Select**<br />`nf_allow_cat_specific` | Select to allow notifications that depend on the category the items are assigned to. This will show recipients selection in every category configuration form too | — | `1` |

#### New Content: IN ANY STATE (from authors that can publish)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Item in states**<br />`states_notify_new` | Email will be sent when item is any of the selected states | — | — |
| **User groups**<br />`usergrps_notify_new` | Select usergroups using ctrl-click to select multiple | — | — |
| **User id/names list**<br />`userlist_notify_new` | Enter user ids or names (usernames not full names) and separate the list with comma | — | — |
| **Extra custom text**<br />`text_notify_new` | Enter an extra custom text to include in the notification email. **NOTE**: This will be filtered as a language string (via JText) | — | — |

#### New Content: PENDING PUBLICATION (from authors that cannot publish)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **User groups**<br />`usergrps_notify_new_pending` | Select usergroups using ctrl-click to select multiple | — | — |
| **User id/names list**<br />`userlist_notify_new_pending` | Enter user ids or names (usernames not full names) and separate the list with comma | — | — |
| **Extra custom text**<br />`text_notify_new_pending` | Enter an extra custom text to include in the notification email. **NOTE**: This will be filtered as a language string (via JText) | — | — |

#### Updated Content: NOT NEEDING VERSION APPROVAL (author can publish)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Item in states**<br />`states_notify_existing` | Email will be sent when item is any of the selected states | — | — |
| **User groups**<br />`usergrps_notify_existing` | Select usergroups using ctrl-click to select multiple | — | — |
| **User id/names list**<br />`userlist_notify_existing` | Enter user ids or names (usernames not full names) and separate the list with comma | — | — |
| **Extra custom text**<br />`text_notify_existing` | Enter an extra custom text to include in the notification email. **NOTE**: This will be filtered as a language string (via JText) | — | — |

#### Updated Content: NEEDING VERSION APPROVAL (author cannot publish, versioning is enabled)

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **User groups**<br />`usergrps_notify_existing_reviewal` | Select usergroups using ctrl-click to select multiple | — | — |
| **User id/names list**<br />`userlist_notify_existing_reviewal` | Enter user ids or names (usernames not full names) and separate the list with comma | — | — |
| **Extra custom text**<br />`text_notify_existing_reviewal` | Enter an extra custom text to include in the notification email. **NOTE**: This will be filtered as a language string (via JText) | — | — |

#### Workflow
