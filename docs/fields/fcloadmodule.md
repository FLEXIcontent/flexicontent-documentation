---
sidebar_position: 17
---

# Load module

Load a module or module position inside a content item

*Plugin : `fcloadmodule` — Load Module / Module position*

:::info Source
This page is generated from `plugins/flexicontent_fields/fcloadmodule/fcloadmodule.xml` and the official FLEXIcontent 5.x language files.
:::

## Select Module

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Method**<br />`module_method` | Choose the loadind method. Either all the modules from a position or a single module instance | `multilist` | `1` = Module<br />`2` = Position | `1` (Module) |
| **Module**<br />`modules` | Select a modules to load | `fcmodules` | — | — |
| **Position**<br />`position` | Select a module position to load | `fcpositions` | — | — |
| **Style**<br />`style` | Select the style to render your module, let empty to use the basic render 'none' | `text` | — | — |

## Editing

#### Editing

### Values

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Customize module parameters per item (not for position mode)**<br />`mod_params` | You can - try - to customize some module parameters by allowing user to enter values for them in item form. **NOTE** You need to examine XML file of target module to find parameter names **Example** param_label1!!param_name1 %% param_label2!!param_name2 %% param_label3!!param_name3 | `textarea` | — | — |

### Form field

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label_form` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Floated left<br />`2` = Cleared | `1` (Floated left) |
| **Label**<br />`label_form` | Enter a label to use for item form that is different than field label for viewing | `text` | — | — |
| **No access message**<br />`no_acc_msg_form` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |

#### Editing

## Viewing

#### Display

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Show in clients**<br />`show_in_clients` | Select if the field will be created and shown to specific clients | `fccheckbox` | — | — |
| **Show in views**<br />`show_in_views` | Select if the field will be created and shown to specific views | `fccheckbox` | — | — |

#### Label and access

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display label**<br />`display_label` | Display or hide label of this field | `radio` | `0` = No<br />`1` = Yes | `1` (Yes) |
| **Show no access message**<br />`show_acc_msg` | When field is inaccessible a no access message will be shown. **NOTE:** IF this parameter is disabled, the field will be invisible to users with no access, without any message or warning that it exists | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **No access message**<br />`no_acc_msg` | Leave this blank to use system's default no access message, or enter a custom message for this field | `text` | — | — |
