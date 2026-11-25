---
sidebar_position: 5
---

# User account via submit

Email Field Plugin for FLEXIcontent

:::info Source
This page is generated from `plugins/flexicontent_fields/account_via_submit/account_via_submit.xml` and the official FLEXIcontent 5.x language files.
:::

## Editing

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show On**<br />`showon` | Shown On Conditions. Use Joomla Format 'fieldname:value' e.g album_type:2 NOTE: DO not set this field to required. Also DISABLE prettyCheckable / Select2 JS in any referenced fields of type select*, checkbox*, radio* | `text` | — | — |
| **Required**<br />`required` | Choose yes if the field must be filled | `radio` | `0` = No<br />`1` = Yes | `0` (No) |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Email address

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Maximum Text Length**<br />`maxlength` | Maximum number of characters allowed during user input | `text` | — | — |
| **Field size**<br />`size` | Field size in the HTML form | `text` | — | `30` |
| **Field attributes**<br />`extra_attributes` | Here you can enter some extra attributes (HTML Tag Parameters) for the form field like e.g. onkeypress="..." onmouseover="..." somename="somevalue". Take care not to break the the HTML syntax of the form field | `text` | — | — |
| **Input value Masking & Validation**<br />`inputmask` | Parameters for both masking and validating user input | `multilist` | `0` = No<br />`email` = Yes | `email` (Yes) |
| **Confirm email address**<br />`email_confirm` | Require that email address is entered twice | `radio` | `0` = No | `0` (No) |

#### Optional Properties

#### Enable

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Full name**<br />`use_full` | If you enable this, then user will be able to override default property value when editing the field in item form | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Fist name**<br />`use_first` | If you enable this, then user will be able to override default property value when editing the field in item form | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Last name**<br />`use_last` | If you enable this, then user will be able to override default property value when editing the field in item form | `radio` | `0` = No<br />`1` = Yes | `0` (No) |
| **Gender**<br />`use_gender` | If you enable this, then user will be able to override default property value when editing the field in item form | `radio` | `0` = No | `0` (No) |

## User creation / Edit coupons

... create new users, and/or allow them to edit items as guests

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Email exists**<br />`handle_existing_email` | — | `radio` | `0` = Cancel item creation<br />`1` = Assign new item | `0` (Cancel item creation) |

#### Existing item Or user is logged

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Existing items**<br />`display_item_owner` | — | `radio` | `0` = No<br />`1` = Show item owner info | `0` (No) |
| **New items**<br />`display_when_logged` | — | `radio` | `0` = No<br />`1` = Show logged user info | `0` (No) |

### Account creation

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Create new accounts**<br />`create_accounts` | Create new account to use as item owner | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **User group (ID)**<br />`new_usertype` | — | `usergrouplist` | `—` = Joomla's default | — |
| **User activation**<br />`useractivation` | — | `list` | `—` = Joomla's default<br />`0` = JNONE<br />`1` = Self activation (email link)<br />`2` = Activation by administrator | — |

#### Admin notifications

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Email to Administrator**<br />`mail_to_admin` | — | `radio` | `—` = Joomla's default<br />`0` = No<br />`1` = Yes | — |
| **Send emails as BCC**<br />`admin_send_as_bcc` | Enable this to prevent email recipients from seeing other email recipients. **NOTE**: this will force the administrator email of the website to be the main recipient of the notification email | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |

### Edit coupons

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Create/Send edit coupons**<br />`create_coupons` | Create an edit coupon per new item and send an email with a direct edit link that uses the edit coupon | `multilist` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Edit coupoun email text**<br />`coupon_desc` | A text to be used as email body message when sending the item edit link | `textarea` | — | `Add a custom message here` |
| **Initialized**<br />`initialized` | SQL tables initialized | `hidden` | — | `0` |
