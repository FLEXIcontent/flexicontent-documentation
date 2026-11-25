---
sidebar_position: 9
---

# Item form

Layout and behaviour of the item creation and edit form.

:::info Source
This page is generated from `admin/config.xml` and the official `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` language files of FLEXIcontent 5.x.
:::

#### Item form

## Item Form - Frontend

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Item form layout**<br />`form_ilayout_fe` | — | — | `tabs` |

#### Item Form - Frontend

## General Form Behavior

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Optional buttons**<br />`allowbuttons_fe` | Select the optional buttons that you want to appear in frontend form | — | — |
| **Placement of buttons**<br />`buttons_placement_fe` | Select to display form buttons at the top or bottom of the form | — | `0` |

#### Display approval needed warnings

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Inside form**<br />`approval_warning_inform_fe` | Enable this, to show a message inside item form, whether current user can publish new items or if they can self-approve changes to existing items | — | `1` |
| **After form submit**<br />`approval_warning_aftersubmit_fe` | Enable this, to show an after form submit warning, saying if approval is needed for new item being published or for the changes to existing item becoming active | — | `1` |
| **Requires version reviewal**<br />`version_reviewal_msg_fe` | — | — | — |
| **Requires document approval**<br />`document_approval_msg_fe` | — | — | — |
| **May require version reviewal**<br />`mr_version_revial_msg_fe` | — | — | — |
| **May require document approval**<br />`mr_document_approval_msg_fe` | — | — | — |
| **Changes applied immediately**<br />`changes_applied_immediately_msg_fe` | — | — | — |

#### Instructions / URL redirections / etc

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Submit Instructions**<br />`submit_message` | These instructions will be placed at the top of the form, after the form buttons **NOTE:** This can be a language string (add it to your language files) | — | — |
| **Submit Redirect URL hides preview button**<br />`submit_redirect_url_fe` | You can set a custom URL that the user will be redirected after submitting new content. **NOTE:** This will work with even if you click 'Add' or 'Apply' buttons before closing the item **NOTE:** Setting this will hide the preview button while submitting new items | — | — |
| **Unauthorized Page User can not submit MORE or ANY content**<br />`notauthurl` | Specify the URL / Menu Item ID of the page you wish your registered users to land if they don't have enough rights to create more (or any) content. This could be (for example) the subscriptions plans page if you sell your published content. **NOTE:** If you don't set anything here they the general unauthorized page will be used. | — | — |

#### Form Security Field Display criteria for CAPTCHA

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use captcha**<br />`use_captcha` | Select when to display a captcha security field, to protect the form from robots | — | `1` |
| **Captcha plugin**<br />`captcha` | Select a specific captcha plugin, to override the default setting | — | — |
| **Operation Type**<br />`captcha_formop` | When operation is of the selected type | — | `0` |

## Compatibility

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Intro / Full Images**<br />`use_jimages_fe` | Show intro/full images | — | — |
| **Urls**<br />`use_jurls_fe` | Show urls | — | — |

## Basic Editing

#### New / Existing Items

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use title**<br />`usetitle_fe` | Select to display or hide item title - you can set to automatic in type parameters | — | `1` |
| **Use Alias**<br />`usealias_fe` | Allow the user to enter the Alias field | — | `1` |
| **Use type**<br />`usetype_fe` | Display type selector to allow changing type of item | — | `1` |
| **Use state**<br />`usestate_fe` | Display state selector to allow changing publication state of the item | — | `1` |
| **Use access**<br />`useaccess_fe` | Display access selector to allow changing access level of the item | — | `1` |
| **Use featured**<br />`usefeatured_fe` | Display featured selector to allow changing featured flag of the item | — | `0` |
| **Use tags**<br />`usetags_fe` | Allow tags to be hidden, for user groups that have the Can-Tags Privilege, note the item can still have tags managed | — | `1` |
| **Allow disabling comments**<br />`allowdisablingcomments_fe` | Here you can give the ability to authors/editors to disable comments on Content Items they can edit. If you allow this it is recommended not to show item advanced parameters | — | `0` |

#### Categories

:::note
Note: You still need **ACL** to prevent multi-category changes. Just hiding them, does not prevent users from changing them ...
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use category**<br />`usemaincat_fe` | If you disable this you need to also set a default category in the type configuration (typically you will create a category with the same name as the type and set it as default) | — | `1` |
| **Secondary categories**<br />`show_seccats_fe` | — | — | `2` |
| **Featured Categories**<br />`show_featcats_fe` | — | — | `2` |

:::note
Filtering
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Not in item language**<br />`iform_cats_not_in_itemlang_fe` | Either hide the categories in languages that are different than item language, or append language to category title | — | `1` |
| **States allowed**<br />`iform_catstates_allowed_fe` | Categories with non allowed states will be hidden, unless the item is already assigned to such a category | — | — |

#### Language

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use language**<br />`uselang_fe` | Allow the user to select language. NOTE: select a default language before disabling this | — | `1` |
| **Default language**<br />`default_language_fe` | This is the language that will be pre-selected, particularly useful if you hide the language | — | `_author_lang_` |
| **Disable languages**<br />`disable_languages_fe` | For example you may want to disable language 'ALL' | — | — |

#### Language selector

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Display as**<br />`langdisplay_fe` | You can display it e.g. as drop-down select or radio buttons | — | `2` |
| **Show flags (radio)**<br />`langdisplay_flags_fe` | Show flag icons | — | `1` |
| **Show text (radio)**<br />`langdisplay_texts_fe` | Enable to show text such language code | — | `1` |

#### Existing items

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Allow language modifications**<br />`allowlangmods_fe` | Allow user to change the language related properties for -existing- items. Usually, you should prohibit users from changing existing language properties like item language and original content of translation | — | — |

:::note
Please edit more configuration here: Notifications plugin
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Allow notifying item owner**<br />`allow_owner_notify_fe` | Allow the editor to send update notification (email) to the owner of the current item | — | `0` |
| **Allow notifying subscribers (favoring the content item)**<br />`allow_subscribers_notify_fe` | Allow the editor to send update notifications (emails) to the users favouroting the current item | — | `0` |

## Advanced Editing

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Publication Details**<br />`usepublicationdetails_fe` | Select here to allow either: -Basic- Publication Details: (start & finish publishing dates & author alias) to people that can -EDIT- the item. or -All- publication details: (item author & creation date) are available ONLY to Super Admin users. | — | `1` |
| **Metadata Details**<br />`usemetadata_fe` | Recommended to hide or only allow -basic- META data (description and keywords), the rest will be unnecessary & confusing to the users | — | `1` |
| **SEO Configuration**<br />`useseoconf_fe` | Select here to allow user to edit SEO parameters, like custom page title tag | — | `0` |
| **Display options**<br />`usedisplaydetails_fe` | Select which item display parameters groups you want to be editable in the frontend | — | `0` |
| **3rd party display options**<br />`use3rdpartyparams_fe` | Select to show the display options from 3rd party extensions | — | `1` |
| **Template Selection**<br />`selecttheme_fe` | Enable selection and configuration of template for frontend user groups with the Templates-Manage Privilege. | — | `0` |
| **Permissions (ACL)**<br />`permsplacement_fe` | Select here to show permissions to user if these are editable | — | `2` |
| **Versions**<br />`versionsplacement_fe` | Inline: open the version comparison in a new browser tab. Popup: open the version comparison in a modal window. The version history table is always shown in the Versions tab. | — | `2` |

## Layout

:::note
Using default settings
:::

## Styling

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Label class**<br />`form_lbl_class_fe` | A class to style the label of the fields | — | — |
| **Form Container CSS class**<br />`form_container_class_fe` | A list of classnames to add to the outer form container | — | — |
| **Form Container CSS**<br />`form_container_css_fe` | Set some CSS rules for the form container e.g. 'width:800px;' to avoid fitting problems in the frontend | — | — |
| **Add CSS to edit form**<br />`form_extra_css_fe` | Add extra CSS rules to the submit/edit form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | — | — |
| **Add JS to edit form for developers only ***<br />`form_extra_js_fe` | Add extra JS code to the submit/edit form. - Usually you would add JS code executed on DOM Ready Event. - Take care not break JS execution of your Form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | — | — |

#### Item Form - Frontend

## Item Form - Backend

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Item form layout**<br />`form_ilayout_be` | — | — | `tabs` |

#### Item Form - Backend

## General Form Behavior

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Optional buttons**<br />`allowbuttons_be` | Select the optional buttons that you want to appear in frontend form | — | — |
| **Placement of buttons**<br />`buttons_placement_be` | Select to display form buttons at the top or bottom of the form | — | `-1` |

#### Display approval needed warnings

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Inside form**<br />`approval_warning_inform_be` | Enable this, to show a message inside item form, whether current user can publish new items or if they can self-approve changes to existing items | — | `1` |
| **After form submit**<br />`approval_warning_aftersubmit_be` | Enable this, to show an after form submit warning, saying if approval is needed for new item being published or for the changes to existing item becoming active | — | `1` |
| **Requires version reviewal**<br />`version_reviewal_msg_be` | — | — | — |
| **Requires document approval**<br />`document_approval_msg_be` | — | — | — |
| **May require version reviewal**<br />`mr_version_revial_msg_be` | — | — | — |
| **May require document approval**<br />`mr_document_approval_msg_be` | — | — | — |
| **Changes applied immediately**<br />`changes_applied_immediately_msg_be` | — | — | — |

#### Instructions / URL redirections / etc

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Submit Instructions**<br />`submit_message_be` | These instructions will be placed at the top of the form, after the form buttons **NOTE:** This can be a language string (add it to your language files) | — | — |

## Compatibility

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Intro / Full Images**<br />`use_jimages_be` | Show intro/full images | — | — |
| **Urls**<br />`use_jurls_be` | Show urls | — | — |

## Basic Editing

#### New / Existing Items

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use title**<br />`usetitle_be` | Select to display or hide item title - you can set to automatic in type parameters | — | `1` |
| **Use Alias**<br />`usealias_be` | Allow the user to enter the Alias field | — | `1` |
| **Use type**<br />`usetype_be` | Display type selector to allow changing type of item | — | `1` |
| **Use state**<br />`usestate_be` | Display state selector to allow changing publication state of the item | — | `1` |
| **Use access**<br />`useaccess_be` | Display access selector to allow changing access level of the item | — | `1` |
| **Use featured**<br />`usefeatured_be` | Display featured selector to allow changing featured flag of the item | — | `1` |
| **Use tags**<br />`usetags_be` | Allow tags to be hidden, for user groups that have the Can-Tags Privilege, note the item can still have tags managed | — | `1` |
| **Allow disabling comments**<br />`allowdisablingcomments_be` | Here you can give the ability to authors/editors to disable comments on Content Items they can edit. If you allow this it is recommended not to show item advanced parameters | — | `0` |

#### Categories

:::note
Note: You still need **ACL** to prevent multi-category changes. Just hiding them, does not prevent users from changing them ...
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use category**<br />`usemaincat_be` | If you disable this you need to also set a default category in the type configuration (typically you will create a category with the same name as the type and set it as default) | — | `1` |
| **Secondary categories**<br />`show_seccats_be` | — | — | `2` |
| **Featured Categories**<br />`show_featcats_be` | — | — | `2` |

:::note
Filtering
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Not in item language**<br />`iform_cats_not_in_itemlang_be` | Either hide the categories in languages that are different than item language, or append language to category title | — | `1` |
| **States allowed**<br />`iform_catstates_allowed_be` | Categories with non allowed states will be hidden, unless the item is already assigned to such a category | — | — |

#### Language

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Use language**<br />`uselang_be` | Allow the user to select language. NOTE: select a default language before disabling this | — | `1` |
| **Default language**<br />`default_language_be` | This is the language that will be pre-selected, particularly useful if you hide the language | — | `_author_lang_` |
| **Disable languages**<br />`disable_languages_be` | For example you may want to disable language 'ALL' | — | — |

#### Language selector

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Display as**<br />`langdisplay_be` | You can display it e.g. as drop-down select or radio buttons | — | `2` |
| **Show flags (radio)**<br />`langdisplay_flags_be` | Show flag icons | — | `1` |
| **Show text (radio)**<br />`langdisplay_texts_be` | Enable to show text such language code | — | `1` |

#### Existing items

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Allow language modifications**<br />`allowlangmods_be` | Allow user to change the language related properties for -existing- items. Usually, you should prohibit users from changing existing language properties like item language and original content of translation | — | — |

:::note
Please edit more configuration here: Notifications plugin
:::

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Allow notifying item owner**<br />`allow_owner_notify_be` | Allow the editor to send update notification (email) to the owner of the current item | — | `1` |
| **Allow notifying subscribers (favoring the content item)**<br />`allow_subscribers_notify_be` | Allow the editor to send update notifications (emails) to the users favouroting the current item | — | `1` |

## Advanced Editing

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Publication Details**<br />`usepublicationdetails_be` | Select here to allow either: -Basic- Publication Details: (start & finish publishing dates & author alias) to people that can -EDIT- the item. or -All- publication details: (item author & creation date) are available ONLY to Super Admin users. | — | `2` |
| **Metadata Details**<br />`usemetadata_be` | Recommended to hide or only allow -basic- META data (description and keywords), the rest will be unnecessary & confusing to the users | — | `2` |
| **SEO Configuration**<br />`useseoconf_be` | Select here to allow user to edit SEO parameters, like custom page title tag | — | `1` |
| **Display options**<br />`usedisplaydetails_be` | Select which item display parameters groups you want to be editable in the frontend | — | `2` |
| **3rd party display options**<br />`use3rdpartyparams_be` | Select to show the display options from 3rd party extensions | — | `1` |
| **Template Selection**<br />`selecttheme_be` | Enable selection and configuration of template for frontend user groups with the Templates-Manage Privilege. | — | `2` |
| **Permissions (ACL)**<br />`permsplacement_be` | Select here to show permissions to user if these are editable | — | `2` |
| **Versions**<br />`versionsplacement_be` | Inline: open the version comparison in a new browser tab. Popup: open the version comparison in a modal window. The version history table is always shown in the Versions tab. | — | `2` |

## Layout

:::note
Using default settings
:::

## Styling

### Styling

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Label class**<br />`form_lbl_class_be` | A class to style the label of the fields | — | — |
| **Form Container CSS class**<br />`form_container_class_be` | A list of classnames to add to the outer form container | — | — |
| **Form Container CSS**<br />`form_container_css_be` | Set some CSS rules for the form container e.g. 'width:800px;' to avoid fitting problems in the frontend | — | — |
| **Add CSS to edit form**<br />`form_extra_css_be` | Add extra CSS rules to the submit/edit form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | — | — |
| **Add JS to edit form for developers only ***<br />`form_extra_js_be` | Add extra JS code to the submit/edit form. - Usually you would add JS code executed on DOM Ready Event. - Take care not break JS execution of your Form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | — | — |

#### Item Form - Backend

## Item Form - Both

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Icon type**<br />`form_font_icons` | You may display icons as images or as using an installed font-based icon set | — | `1` |
| **Hide description field**<br />`hide_maintext` | Hide the description (maintext) field in the item form (not recommended !!!). TAKE CARE, you will loose the com_content backwards compatibility for these items !!! | — | `0` |

### Styling

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Add CSS to edit form**<br />`form_extra_css` | Add extra CSS rules to the submit/edit form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | — | — |
| **Add JS to edit form for developers only ***<br />`form_extra_js` | Add extra JS code to the submit/edit form. - Usually you would add JS code executed on DOM Ready Event. - Take care not break JS execution of your Form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | — | — |

## Joomla article form

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **Default type**<br />`jarticle_form_typeid` | Default type for Joomla article form when an item is new or when it has no type ! | — | — |

#### Frontend

| Option | Description | Values | Default |
| --- | --- | --- | --- |
| **New article form**<br />`jarticle_allow_new_form` | Select to either redirect new Joomla article form to FLEXIContent new item form or allow it | — | `1` |

:::note
**Note**: Existing items can be edited via links to Joomla article form, if their type configuration -- 'Allow Joomla article view' -- setting is enabled
:::

#### Item form
