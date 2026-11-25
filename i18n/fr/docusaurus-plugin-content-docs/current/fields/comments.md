---
sidebar_position: 11
---

# Commentaires

FLEXIcontent - Commentaires, un plugin de commentaire via les apps Disqus et Facebook pour la vue contenu

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/comments/comments.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Application commentaire

### Application commentaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **API pour les commentaires**<br />`comment_api` | Choisissez Disqus ou Facebook pour gérer vos commentaires | `multilist` | `disqus` = Disqus<br />`facebook` = Facebook | `0` |
| **Catégorie**<br />`method_category` | Inclure ou exclure les commentaires dans les contenus pour les-la catégorie(s) | `multilist` | `0` = Tout autoriser<br />`1` = Inclure<br />`-1` = Exclure | `0` (Tout autoriser) |
| **Catégorie**<br />`catid` | Choisissez votre catégorie dans la liste | `flexicategories` | — | — |

### Disqus

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nom du forum**<br />`pforum_shortname` | Créer le nom du forum déclaré dans l'admin Disqus | `text` | — | — |

:::note
Pour obtenir votre clé de domaine Disqus veillez cliquer:Obtenir ma clé de domaine
:::

### API Facebook

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **ID de l'appli**<br />`fappId` | Définir votre ID d'application | `text` | — | — |
| **ID de l'administrateur**<br />`fadminID` | Définir votre ID d'application | `text` | — | — |

:::note
PLG_FLEXICONTENT_FIELDS_COMMENTS_GET__FBAPI_KEY_INFO
:::

### Forcer la langue

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Langue automatique**<br />`autolanguage` | Si cette option est mise sur auto, l'api de commentaire sélectionnée utilisera le système de détection automatique pour la langue | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Forcer la langue**<br />`comment_language` | Sélectionnez une langue dans la liste de sélection | `list` | `af_ZA` = Afrikaans<br />`gn_PY` = Guaraní<br />`ay_BO` = Aymara<br />`az_AZ` = Azéri<br />`id_ID` = Indonésien<br />`ms_MY` = Malais<br />`jv_ID` = Javanais<br />`bs_BA` = Bosnien<br />`ca_ES` = Catalan<br />`cs_CZ` = Tchèque<br />`ck_US` = Cherokee<br />`cy_GB` = Gallois<br />`da_DK` = Danois<br />`se_NO` = Same du Nord<br />`de_DE` = Allemand<br />`et_EE` = Estonien<br />`ثn_IN` = Anglais (Inde)<br />`en_PI` = Anglais (pirate)<br />`en_GB` = Anglais (Royaume-Uni)<br />`en_UD` = Anglais (à l’envers)<br />`en_US` = Anglais (États-Unis)<br />`es_LA` = Espagnol<br />`es_CL` = Espagnol (Chili)<br />`es_CO` = Espagnol (Colombie)<br />`es_ES` = Espagnol (Espagne)<br />`es_MX` = Espagnol (Mexique)<br />`es_VE` = Espagnol (Venezuela)<br />`eo_EO` = Espéranto<br />`eu_ES` = Basque<br />`tl_PH` = Filipino<br />`fo_FO` = Féroïen<br />`fr_FR` = Français (France)<br />`fr_CA` = Français (Canada)<br />`fy_NL` = Frison<br />`ga_IE` = Irlandais<br />`gl_ES` = Galicien<br />`ko_KR` = Coréen<br />`hr_HR` = Croate<br />`xh_ZA` = Xhosa<br />`zu_ZA` = Zoulou<br />`is_IS` = Islandais<br />`it_IT` = Italien<br />`ka_GE` = Géorgien<br />`sw_KE` = Swahili<br />`tl_ST` = Klingon<br />`ku_TR` = Kurde<br />`lv_LV` = Letton<br />`fb_LT` = Langue « leet »<br />`lt_LT` = Lituanien<br />`li_NL` = Limbourgeois<br />`la_VA` = Latin<br />`hu_HU` = Hongrois<br />`mg_MG` = Malgache<br />`mt_MT` = Maltais<br />`nl_NL` = Néerlandais<br />`nl_BE` = Néerlandais (Belgique)<br />`ja_JP` = Japonais<br />`nb_NO` = Norvégien (bokmål)<br />`nn_NO` = Norvégien (nynorsk)<br />`uz_UZ` = Ouzbek<br />`pl_PL` = Polonais<br />`pt_BR` = Portugais (Brésil)<br />`pt_PT` = Portugais (Portugal)<br />`qu_PE` = Quechua<br />`ro_RO` = Roumain<br />`rm_CH` = Romanche<br />`ru_RU` = Russe<br />`sq_AL` = Albanais<br />`sk_SK` = Slovaque<br />`sl_SI` = Slovène<br />`so_SO` = Somali<br />`fi_FI` = Finnois<br />`sv_SE` = Suédois<br />`th_TH` = Thaï<br />`vi_VN` = Vietnamien<br />`tr_TR` = Turc<br />`zh_CN` = Chinois simplifié (Chine)<br />`zh_TW` = Chinois traditionnel (Taïwan)<br />`zh_HK` = Chinois traditionnel (Hong Kong)<br />`el_GR` = Grec<br />`gx_GR` = Grec ancien<br />`be_BY` = Biélorusse<br />`bg_BG` = Bulgare<br />`kk_KZ` = Kazakh<br />`mk_MK` = Macédonien<br />`mn_MN` = Mongol<br />`sr_RS` = Serbe<br />`tt_RU` = Tatar<br />`tg_TJ` = Tadjik<br />`uk_UA` = Ukrainien<br />`hy_AM` = Arménien<br />`yi_DE` = Yiddish<br />`he_IL` = Hébreu<br />`ur_PK` = Ourdou<br />`ar_AR` = Arabe<br />`ps_AF` = Pachto<br />`fa_IR` = Persan<br />`sy_SY` = Syriaque<br />`ne_NP` = Népalais<br />`mr_IN` = Marathe<br />`sa_IN` = Sanscrit<br />`hi_IN` = Hindi<br />`bn_IN` = Bengali<br />`pa_IN` = Pendjabi<br />`gu_IN` = Gujarati<br />`ta_IN` = Tamoul<br />`te_IN` = Télougou<br />`kn_IN` = Kannada<br />`ml_IN` = Malayalam<br />`km_KH` = Khmer | `en_GB` (Anglais (Royaume-Uni)) |

## PLG_FLEXICONTENT_FIELDS_VIEWING

### Option d'affichage Facebook

### Aucune option d'apparence pour Disqus

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nombre de commentaire**<br />`fdata-num-posts` | Définir le nombre de commentairedans la liste | `text` | — | `4` |
| **Largeur des commentaires**<br />`fdata-width` | Largeur de la liste des commentaires | `text` | — | `500` |
| **Thème**<br />`fdata-colorscheme` | Choisissez l'affichage, clair ou foncé | `list` | `—` = Light<br />`dark` = Dark | — |
