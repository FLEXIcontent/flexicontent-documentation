---
sidebar_position: 10
---

# Item submission form



:::info Source
This page is generated from `site/views/item/tmpl/form.xml` and the official FLEXIcontent 5.x language files.
:::

## Required parameters

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Form Type**<br />`typeid` | Either set a specific Form Type that you wish to display, OR let your submitting user to select out of the Content Types that are allowed to him/her via ACL 'create items' privilege (please set this in Content Type manager) | `types` | — | — |

:::note
**NOTE**: in order to configure submit/edit item form, these are used: -- Form Configuration in component and content type, -- 'Create' / 'Edit' ACL for Category and Types, etc -- Author/User group limitations, etc Enable/use parameters in this menu item only if needed, -- the above mentioned configuration and **ACL** should be checked and configured **anyway**
:::

## General Form Behavior

(effects only initial submission)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Item form layout**<br />`form_ilayout_fe` | — | `fclayout` | **Built-in layouts**<br />`tabs` = tabs (Default)<br />`flat` = flat | — |

### General Form Behavior

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Optional buttons**<br />`allowbuttons_fe` | Select the optional buttons that you want to appear in frontend form | `fccheckbox` | — | — |
| **Placement of buttons**<br />`buttons_placement_fe` | Select to display form buttons at the top or bottom of the form | `radio` | `—` = Use Global<br />`0` = Top<br />`1` = Bottom<br />`2` = Left<br />`3` = Right | — |

#### Display approval needed warnings

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Inside form**<br />`approval_warning_inform_fe` | Enable this, to show a message inside item form, whether current user can publish new items or if they can self-approve changes to existing items | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |
| **After form submit**<br />`approval_warning_aftersubmit_fe` | Enable this, to show an after form submit warning, saying if approval is needed for new item being published or for the changes to existing item becoming active | `radio` | `—` = Use Global<br />`0` = Hide<br />`1` = Show | — |

:::note
If you leave these blank, then please check default values at item configuration type type
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Requires version reviewal**<br />`version_reviewal_msg_fe` | _Please note that your new document **version** will be reviewed and approved by a site administrator_ | `textarea` | — | — |
| **Requires document approval**<br />`document_approval_msg_fe` | _Please note that your **new content** will be reviewed and accepted by a site administrator_ | `textarea` | — | — |
| **May require version reviewal**<br />`mr_version_revial_msg_fe` | _Please note, your new document **version** might need to be reviewed and approved. This may depend on the content's category AND/OR the content's type. You will be notified whether approval is needed, after you save this content._ | `textarea` | — | — |
| **May require document approval**<br />`mr_document_approval_msg_fe` | _Please note, that your new content might require approval before being accepted. This may depend on the content's category AND/OR the content's type. You will be notified whether approval is needed, after you save this content._ | `textarea` | — | — |
| **Changes applied immediately**<br />`changes_applied_immediately_msg_fe` | _Please note, that document versioning is disabled, thus any changes that you make to this content will be accepted/activated immediately and the previous version will be permanently overwritten_ | `textarea` | — | — |

#### Instructions / URL redirections / etc

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Submit Instructions**<br />`submit_message` | These instructions will be placed at the top of the form, after the form buttons **NOTE:** This can be a language string (add it to your language files) | `textarea` | — | — |
| **Submit Redirect URL hides preview button**<br />`submit_redirect_url_fe` | You can set a custom URL that the user will be redirected after submitting new content. **NOTE:** This will work with even if you click 'Add' or 'Apply' buttons before closing the item **NOTE:** Setting this will hide the preview button while submitting new items | `text` | — | — |
| **Unauthorized Page User can not submit MORE or ANY content**<br />`notauthurl` | Specify the URL / Menu Item ID of the page you wish your registered users to land if they don't have enough rights to create more (or any) content. This could be (for example) the subscriptions plans page if you sell your published content. **NOTE:** If you don't set anything here they the general unauthorized page will be used. | `menuitem` | — | — |

#### Form Security Field Display criteria for CAPTCHA

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use captcha**<br />`use_captcha` | Select when to display a captcha security field, to protect the form from robots | `multilist` | `—` = Use Global<br />`0` = Disable<br />`1` = Guests (Recommended)<br />`2` = Any user | — |
| **Captcha plugin**<br />`captcha` | Select a specific captcha plugin, to override the default setting | `plugins` | `—` = Use Global<br />`0` = Disable | — |

## Optional Form Data

(effects only initial submission)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Intro / Full Images**<br />`use_jimages_fe` | Show intro/full images | `radio` | `—` = Joomla's default<br />`0` = Disable<br />`1` = Enable | — |
| **Urls**<br />`use_jurls_fe` | Show urls | `radio` | `—` = Joomla's default<br />`0` = Disable<br />`1` = Enable | — |

### Basic Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use title**<br />`usetitle_fe` | Select to display or hide item title - you can set to automatic in type parameters | `radio` | `—` = Use Global<br />`0` = Hide if automatic<br />`1` = Yes | — |
| **Use Alias**<br />`usealias_fe` | Allow the user to enter the Alias field | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use type**<br />`usetype_fe` | Display type selector to allow changing type of item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use state**<br />`usestate_fe` | Display state selector to allow changing publication state of the item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use access**<br />`useaccess_fe` | Display access selector to allow changing access level of the item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use featured**<br />`usefeatured_fe` | Display featured selector to allow changing featured flag of the item | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Use tags**<br />`usetags_fe` | Allow tags to be hidden, for user groups that have the Can-Tags Privilege, note the item can still have tags managed | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes<br />`2` = Display only | — |
| **Allow disabling comments**<br />`allowdisablingcomments_fe` | Here you can give the ability to authors/editors to disable comments on Content Items they can edit. If you allow this it is recommended not to show item advanced parameters | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |

#### Categories

:::note
Note: You still need **ACL** to prevent multi-category changes. Just hiding them, does not prevent users from changing them ...
:::

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use category**<br />`usemaincat_fe` | If you disable this you need to also set a default category in the type configuration (typically you will create a category with the same name as the type and set it as default) | `fcradio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Secondary categories**<br />`show_seccats_fe` | — | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Hide if non-editable<br />`2` = Show | — |
| **Featured Categories**<br />`show_featcats_fe` | — | `fcradio` | `—` = Use Global<br />`0` = Hide<br />`1` = Hide if non-editable<br />`2` = Show | — |

#### Language

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Use language**<br />`uselang_fe` | Allow the user to select language. NOTE: select a default language before disabling this | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes<br />`3` = Yes, without associations<br />`2` = Display only | — |
| **Default language**<br />`default_language_fe` | This is the language that will be pre-selected, particularly useful if you hide the language | `fclanguage` | `_author_lang_` = Use editor's Language<br />`_site_default_` = Use site default Language | — |
| **Disable languages**<br />`disable_languages_fe` | For example you may want to disable language 'ALL' | `fclanguage` | — | — |

#### Language selector

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Display as**<br />`langdisplay_fe` | You can display it e.g. as drop-down select or radio buttons | `radio` | `—` = Use Global<br />`2` = Drop-down select<br />`3` = Radio buttons | — |
| **Show flags (radio)**<br />`langdisplay_flags_fe` | Show flag icons | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Show text (radio)**<br />`langdisplay_texts_fe` | Enable to show text such language code | `radio` | `—` = Use Global<br />`0` = No Text<br />`1` = Language code<br />`2` = Title<br />`3` = Native title<br />`4` = Title + Native title | — |

### Advanced Editing

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Publication Details**<br />`usepublicationdetails_fe` | Select here to allow either: -Basic- Publication Details: (start & finish publishing dates & author alias) to people that can -EDIT- the item. or -All- publication details: (item author & creation date) are available ONLY to Super Admin users. | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Basic (recommended)<br />`2` = All * | — |
| **Metadata Details**<br />`usemetadata_fe` | Recommended to hide or only allow -basic- META data (description and keywords), the rest will be unnecessary & confusing to the users | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Basic (recommended)<br />`2` = All * | — |
| **SEO Configuration**<br />`useseoconf_fe` | Select here to allow user to edit SEO parameters, like custom page title tag | `radio` | `—` = Use Global<br />`0` = No (Recommended)<br />`1` = Yes | — |
| **Display options**<br />`usedisplaydetails_fe` | Select which item display parameters groups you want to be editable in the frontend | `radio` | `—` = Use Global<br />`0` = No (Recommended)<br />`1` = Basic<br />`2` = Advanced | — |
| **3rd party display options**<br />`use3rdpartyparams_fe` | Select to show the display options from 3rd party extensions | `radio` | `—` = Use Global<br />`0` = No<br />`1` = Yes | — |
| **Template Selection**<br />`selecttheme_fe` | Enable selection and configuration of template for frontend user groups with the Templates-Manage Privilege. | `radio` | `—` = Use Global<br />`0` = No (Recommended)<br />`1` = Select<br />`2` = Select and Configure | — |
| **Permissions (ACL)**<br />`permsplacement_fe` | Select here to show permissions to user if these are editable | `radio` | `—` = Use Global<br />`0` = Hide always (even if editable)<br />`1` = Inline<br />`2` = Slider | — |
| **Versions**<br />`versionsplacement_fe` | Inline: open the version comparison in a new browser tab. Popup: open the version comparison in a modal window. The version history table is always shown in the Versions tab. | `radio` | `—` = Use Global<br />`0` = Hide always (even if editable)<br />`1` = Popup<br />`2` = Inline | — |

#### Styling and behaviour

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Label class**<br />`form_lbl_class_fe` | A class to style the label of the fields | `text` | — | — |
| **Form Container CSS**<br />`form_container_css_fe` | Set some CSS rules for the form container e.g. 'width:800px;' to avoid fitting problems in the frontend | `text` | — | — |
| **Add CSS to edit form**<br />`form_extra_css_fe` | Add extra CSS rules to the submit/edit form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | `editor` | — | — |
| **Add JS to edit form for developers only ***<br />`form_extra_js_fe` | Add extra JS code to the submit/edit form. - Usually you would add JS code executed on DOM Ready Event. - Take care not break JS execution of your Form. - This can be overridden per Content Type (along with the other parameters) and thus allow different customization for every Type of content. | `editor` | — | — |

## Override: Submit/publish ACL

(effects only initial submission)

### Unauthorized Users

#### - Override 'create' permission (ACL) of TYPES. - CATEGORIES 'create' permission (ACL) is still enforced

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Unauthorized submit Ignores ACL 'create' (**)**<br />`allowunauthorize` | This allows unauthorized users to submit new content items, effectively ignoring the ACL 'create' privilege ! **NOTE:** 1. This effects current menu item only 2. The preferred way is to use ACL 'create' privilege, which: ** - effects submitting everywhere, - can allow even guest users to submit items** | `radio` | `0` = No, use ACL<br />`1` = Yes<br />`2` = Yes, exclude guests (unlogged) | `0` (No, use ACL) |

### Auto publish override

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Auto publish**<br />`autopublished` | Auto publish the submitted items | `multilist` | `0` = No, show state (based on ACL)<br />`1` = Yes, hide state (regardless privilege) | `0` (No, show state (based on ACL)) |
| **Message about Auto-Publishing**<br />`autopublished_message` | The message will be placed at the top of the form, after the form buttons, **NOTE:** This can be a language string (add it to your language files), also you may use 2 replacements: _PUBLISH_UP_DAYS_INTERVAL_ and _PUBLISH_DOWN_DAYS_INTERVAL_ | `textarea` | — | — |
| **Publish UP interval (minutes)**<br />`autopublished_up_interval` | If auto-publishing is enabled, then the publish UP date will be set to current time plus the interval, a value of 0 will publish the content immediately **NOTE:** This is IGNORED for users that can publish **NOTE:** e.g. For 24 hours enter 1440 (that is 24*60) | `text` | — | `0` |
| **Publish DOWN interval (minutes)**<br />`autopublished_down_interval` | If auto-publishing is enabled, then the publish DOWN date will be set to current time plus the interval, a value of 0 will not set a publish down limit **NOTE:** This is IGNORED for users that can publish **NOTE:** e.g. For 30 days enter 43200 (that is 30*24*60) | `text` | — | `0` |

## Override: Category ACL

(effects only initial submission)

### Categories

#### - Override 'create' permission (ACL) of CATEGORIES. - TYPES 'create' permission (ACL) is still enforced

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable override**<br />`overridecatperms` | If this is disabled then the categories that user has 'CREATE' (=add) permission will be displayed. **NOTE** this will not override user's permission for submitting to multiple categories. | `multilist` | `0` = No, use ACL<br />`1` = Yes | `0` (No, use ACL) |
| **Allowed categories**<br />`cid` | You may select multiple categories. If you **LEAVE BLANK** then permissions override will be disabled, and only the categories that the user has 'CREATE' permission will be displayed | `flexicategories` | — | — |

#### Main category

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Default Main Category**<br />`maincatid` | Optionally, you can set the category that will be selected as default main category on form load. - this will be added to the allowed categories | `flexicategories` | — | — |
| **Enable selector**<br />`maincat_show` | Hide / Show main category selector. NOTE: you must select a default value | `radio` | `1` = Hide<br />`2` = Show | `2` (Show) |

#### Secondary categories (= multi-category assignments)

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Enable selector**<br />`postcats` | Enable / disable multi-category submit (enable / disable selector of secondary categories). Or lock the selector and submit in all categories | `multilist` | `1` = Hide<br />`2` = Show<br />`0` = Locked (submit in ALL) | `2` (Show) |

#### Note: Users are not allowed to submit into multiple categories, unless they have ACL (COMPONENT) permission **'Assign multiple categories to items'**

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Allow to ALL users**<br />`override_mulcatsperms` | Select to ignore user's privilege of assigning an item to multiple categories | `radio` | `0` = No, use ACL<br />`1` = Yes | `1` (Yes) |
| **Display category titles**<br />`postcats_show` | Select to display main category or all category titles | `radio` | `1` = Hide<br />`2` = Show | `1` (Hide) |
