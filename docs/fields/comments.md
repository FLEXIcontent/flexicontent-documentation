---
sidebar_position: 11
---

# Comments

FLEXIcontent - Comments, a comment plugin with Discus and Facebook api comments for item view

:::info Source
This page is generated from `plugins/flexicontent_fields/comments/comments.xml` and the official FLEXIcontent 5.x language files.
:::

## Comments Application

### Comments Application

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **API for comments**<br />`comment_api` | Choose Disqus or Facebook to manage your comments | `multilist` | `disqus` = Disqus<br />`facebook` = Facebook | `0` |
| **Category**<br />`method_category` | Inckude or exclude category for all items inside | `multilist` | `0` = Allow all<br />`1` = Include<br />`-1` = Exclude | `0` (Allow all) |
| **Category**<br />`catid` | Choose your category in list | `flexicategories` | — | — |

### Disqus

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Forum name**<br />`pforum_shortname` | Tip forum name create in Disqus admin | `text` | — | — |

:::note
To get your Disqus domaine please click here: Get Domaine
:::

### Facebook API

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **App ID**<br />`fappId` | Set your App ID | `text` | — | — |
| **Admin ID**<br />`fadminID` | Set your admin ID | `text` | — | — |

:::note
PLG_FLEXICONTENT_FIELDS_COMMENTS_GET__FBAPI_KEY_INFO
:::

### Force language

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Auto language**<br />`autolanguage` | If this option is autoselect, comment api use autodetection system | `multilist` | `0` = No<br />`1` = Yes | `0` (No) |
| **Force language**<br />`comment_language` | Select a language in select list | `list` | `af_ZA` = Afrikaans<br />`gn_PY` = Guaraní<br />`ay_BO` = Aymara<br />`az_AZ` = Azeri<br />`id_ID` = Indonesian<br />`ms_MY` = Malay<br />`jv_ID` = Javanese<br />`bs_BA` = Bosnian<br />`ca_ES` = Catalan<br />`cs_CZ` = Czech<br />`ck_US` = Cherokee<br />`cy_GB` = Welsh<br />`da_DK` = Danish<br />`se_NO` = Northern Sámi<br />`de_DE` = German<br />`et_EE` = Estonian<br />`ثn_IN` = English (India)<br />`en_PI` = English (Pirate)<br />`en_GB` = English (UK)<br />`en_UD` = English (Upside Down)<br />`en_US` = English (US)<br />`es_LA` = Spanish<br />`es_CL` = Spanish (Chile)<br />`es_CO` = Spanish (Colombia)<br />`es_ES` = Spanish (Spain)<br />`es_MX` = Spanish (Mexico)<br />`es_VE` = Spanish (Venezuela)<br />`eo_EO` = Esperanto<br />`eu_ES` = Basque<br />`tl_PH` = Filipino<br />`fo_FO` = Faroese<br />`fr_FR` = French (France)<br />`fr_CA` = French (Canada)<br />`fy_NL` = Frisian<br />`ga_IE` = Irish<br />`gl_ES` = Galician<br />`ko_KR` = Korean<br />`hr_HR` = Croatian<br />`xh_ZA` = Xhosa<br />`zu_ZA` = Zulu<br />`is_IS` = Icelandic<br />`it_IT` = Italian<br />`ka_GE` = Georgian<br />`sw_KE` = Swahili<br />`tl_ST` = Klingon<br />`ku_TR` = Kurdish<br />`lv_LV` = Latvian<br />`fb_LT` = Leet Speak<br />`lt_LT` = Lithuanian<br />`li_NL` = Limburgish<br />`la_VA` = Latin<br />`hu_HU` = Hungarian<br />`mg_MG` = Malagasy<br />`mt_MT` = Maltese<br />`nl_NL` = Dutch<br />`nl_BE` = Dutch (België)<br />`ja_JP` = Japanese<br />`nb_NO` = Norwegian (bokmal)<br />`nn_NO` = Norwegian (nynorsk)<br />`uz_UZ` = Uzbek<br />`pl_PL` = Polish<br />`pt_BR` = Portuguese (Brazil)<br />`pt_PT` = Portuguese (Portugal)<br />`qu_PE` = Quechua<br />`ro_RO` = Romanian<br />`rm_CH` = Romansh<br />`ru_RU` = Russian<br />`sq_AL` = Albanian<br />`sk_SK` = Slovak<br />`sl_SI` = Slovenian<br />`so_SO` = Somali<br />`fi_FI` = Finnish<br />`sv_SE` = Swedish<br />`th_TH` = Thai<br />`vi_VN` = Vietnamese<br />`tr_TR` = Turkish<br />`zh_CN` = Simplified Chinese (China)<br />`zh_TW` = Traditional Chinese (Taiwan)<br />`zh_HK` = Traditional Chinese (Hong Kong)<br />`el_GR` = Greek<br />`gx_GR` = Classical Greek<br />`be_BY` = Belarusian<br />`bg_BG` = Bulgarian<br />`kk_KZ` = Kazakh<br />`mk_MK` = Macedonian<br />`mn_MN` = Mongolian<br />`sr_RS` = Serbian<br />`tt_RU` = Tatar<br />`tg_TJ` = Tajik<br />`uk_UA` = Ukrainian<br />`hy_AM` = Armenian<br />`yi_DE` = Yiddish<br />`he_IL` = Hebrew<br />`ur_PK` = Urdu<br />`ar_AR` = Arabic<br />`ps_AF` = Pashto<br />`fa_IR` = Persian<br />`sy_SY` = Syriac<br />`ne_NP` = Nepali<br />`mr_IN` = Marathi<br />`sa_IN` = Sanskrit<br />`hi_IN` = Hindi<br />`bn_IN` = Bengali<br />`pa_IN` = Punjabi<br />`gu_IN` = Gujarati<br />`ta_IN` = Tamil<br />`te_IN` = Telugu<br />`kn_IN` = Kannada<br />`ml_IN` = Malayalam<br />`km_KH` = Khmer | `en_GB` (English (UK)) |

## PLG_FLEXICONTENT_FIELDS_VIEWING

### Facebook display option

### No apparence option for disqus

| Option | Description | Type | Values | Default |
| --- | --- | --- | --- | --- |
| **Number of post**<br />`fdata-num-posts` | Set number of post in list | `text` | — | `4` |
| **Post width**<br />`fdata-width` | Width of comments list | `text` | — | `500` |
| **Theme**<br />`fdata-colorscheme` | Choose output display, light or dark | `list` | `—` = Light<br />`dark` = Dark | — |
