---
sidebar_position: 37
---

# Texte avec liste

Plugin de champ 'Liste de textes' pour FLEXIcontent

*Plugin : `textselect` — Sélection de texte*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/textselect/textselect.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Édition

#### Édition

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le champ dans un groupe**<br />`use_ingroup` | Activer pour permettre d'utiliser ce champ dans un groupe, qui sera configuré via champ 'Groupe de champ'. REMARQUE: Vous devez alors sélectionner ce champ UNIQUEMENT dans un groupe de champs | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Nombre de valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage conditionnel**<br />`showon` | Affiché en fonction de conditions. Utilisez le format Joomla 'fieldname:value' comme par exemple album_type:2 REMARQUE: ne pas définir ce champ en obligatoire. Également DÉSACTIVER les scripts prettyCheckable / Select2 JS dans tous les champs référencés de type select*, checkbox*, radio* | `text` | — | — |
| **Obligatoire**<br />`required` | Définit si le champ doit être obligatoire dans le formulaire de saisie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Autoriser les valeurs multiples**<br />`allow_multiple` | Autoriser plus d'1 valeur pour ce champs | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Nb maximum de valeurs**<br />`max_values` | Définissez ici le nombre maximum de valeurs que l'utilisateur pourra saisir. 0 pour illimité. | `text` | — | `0` |
| **Valeurs par colonne**<br />`fields_box_placing` | Économiser de l'espace en autorisant l'affichage par ligne de valeurs multiples | `radio` | `0` = 1<br />`1` = Multiple | `0` (1) |
| **Position Ajouter**<br />`add_position` | Sélectionnez pour ajouter le bouton en ligne (bouton d'ajout de valeur à chaque ligne) ou afficher le bouton d'ajout au fond de la liste de valeurs | `multilist` | `0` = Bouton Ajouter en bas<br />`1` = Bouton ajouter avant<br />`2` = Bouton Ajouter après<br />`3` = Les deux (avant - après) | `3` (Les deux (avant - après)) |

#### Texte saisi

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Par défaut**<br />`default_value` | Définir la valeur par défaut qui sera utilisé lors du chargement durant l'édition du champ dans le formulaire de saisie et/ou lors de l'affichage du champ dans la vue élément/catégorie/etc. | `text` | — | — |
| **Utilisation par défaut**<br />`default_value_use` | Sélectionner lorsque cette propriété par défaut sera utilisée. | `list` | `0` = Afficher pour les nouveaux contenus(nécessite une sauvegarde)<br />`1` = Afficher pour tous les contenus (nécessite une sauvegarde)<br />`2` = Toujours afficher plutôt qu'une valeur vierge | `0` (Afficher pour les nouveaux contenus(nécessite une sauvegarde)) |

#### Masque de saisie des valeurs & Validation

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Masque de validation de valeur (Réglage prédéfini)**<br />`inputmask` | Choisir un masque de validation de donnée depuis une liste prédéfinie, utilisé durant le renseignement du champ par l'utilisateur | `multilist` | `—` = Pas de masque<br />`__regex__` = - EXPRESSION RÉGULIÈRE (regex) -<br />`__custom__` = - MASQUE PERSONNALISÉ (liste de propriétés)<br />**Divers (enregistrement inchangé)**<br />`url` = URL<br />`email` = Email<br />`ip` = IP (i.i.i.i)<br />`mac` = Adresse MAC (#:#:#:#:#:#)<br />**DECIMAL (enregister sous la forme n.n)**<br />`currency` = Devise ($)<br />`currency_euro` = Devise (€)<br />`decimal` = Décimal (base : .)<br />`decimal_comma` = Décimal (base : ,)<br />`percentage` = Pourcentage (0,00 % - 100 %)<br />`percentage_zero_nolimit` = Pourcentage (0,00 % - sans limite)<br />`percentage_nolimit_nolimit` = Pourcentage (sans limites)<br />**ENTIER (enregistrer sous la forme nnn)**<br />`integer` = Entier<br />`unsigned` = Entier non signé (positif)<br />`mobile` = Mobile (9999 999 999)<br />**DATE-TIME (Enregistrement inchangé)**<br />`dd/mm/yyyy` = Date (dd/mm/yyyy)<br />`mm/dd/yyyy` = Date (mm/dd/yyyy)<br />`yyyy/mm/dd` = Date (yyyy/mm/dd)<br />`dd.mm.yyyy` = Date (dd.mm.yyyy)<br />`dd-mm-yyyy` = Date (dd-mm-yyyy)<br />`mm.dd.yyyy` = Date (mm.dd.yyyy)<br />`mm-dd-yyyy` = Date (mm-dd-yyyy)<br />`yyyy.mm.dd` = Date (yyyy.mm.dd)<br />`yyyy-mm-dd` = Date (yyyy-mm-dd)<br />`datetime` = Date et heure 24 h (jj/mm/aaaa hh:mm)<br />`datetime12` = Date et heure 12 h (jj/mm/aaaa hh:mm xm)<br />`hh:mm t` = Time (hh:mm t)<br />`h:s t` = Time (h:s t)<br />`hh:mm:ss` = Time (hh:mm:ss)<br />`hh:mm` = Time (hh:mm)<br />`mm/yyyy` = Mois/Année (mm/aaaa) | — |
| **Validation coté serveur**<br />`validation` | Autoriser l'entrée de balises HTML sûres, OU de texte brut, OU utiliser les filtres texte de Joomla (paramètré par groupe d'utilisateurs dans la configuration globale de Joomla), etc ..., n'autorisez jamais le HTML NON-SÉCURISÉ pour les formulaires publics, mais uniquement pour activer le paramètre'**d'encodage à l'affichage**' | `groupedlist` | **Par utilisateur**<br />`2` = Filtrage de texte Joomla (par groupe d'utilisateur)<br />**HTML / Texte**<br />`1` = HTML SÉCURITÉ: retirer tags / attributs dangereux<br />`RAW` = HTML Non sécurisé (HTML brut): ... peut-être: à encoder à l'affichage<br />`STRING` = TEXTE: décoder les entités HTML, enlever les balises HTML<br />`HTML` = TEXTE ou ENCODEAGE HTML : autorisés les entités HTML, enlever les balises<br />**Divers**<br />`URL` = URL<br />`EMAIL` = Email<br />`PATH` = Chemin de fichier<br />**Nombres**<br />`INT` = Entier<br />`UINT` = Entier non signé<br />`DOUBLE` = Decimal<br />**Chaîne**<br />`WORD` = A-Za-z_<br />`ALNUM` = A-Za-z0-9<br />`CMD` = A-Za-z0-9_.-<br />`BASE64` = BASE64 | `HTML` (TEXTE ou ENCODEAGE HTML : autorisés les entités HTML, enlever les balises) |
| **Expression régulière**<br />`regexmask` | Voir l’expression régulière PERL par ex. [0-9]&#123;0-10&#125; | `text` | — | — |
| **Masque personnalisé**<br />`custommask` | Veuillez entrer un masque de validation personnalisé à utiliser lors de l'entrée de l'utilisateur. Ce doit être la valeur RAW du paramètre TAG du champ de saisie HTML. Veuillez lire la documentation et le code source de la bibliothèque JS jquery.inputmask avant de l'utiliser, p. ex. alias : 'numerique', regex: &#123;...&#125; masque:'9&#123;1,24&#125;', avidité : faux, préfixe : '$ ', suffixe : '', placeholder: '0', autoGroup: true, groupSize: 3, groupSeparator: ',', radixPoint : '. , chiffres : 2, chiffres: false, allowPlus: false, allowMinus: true, clearMaskOnLostFocus: true, removeMaskOnSubmit: true, unmaskAsNumber: true Remarque : utilisez les alias : 'existingalias' pour hériter d'un alias existant. | `textarea` | — | — |

#### Création automatique de valeur

:::note
Version Flexicontent PRO uniquement
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Valeur automatique**<br />`auto_value` | Activer pour créer automatiquement la valeur de ce champ lors de l'enregistrement du formulaire d'élément. Dans certains cas, vous pouvez activer l'option de masquer ce champ dans le frontend ou backend ou dans les deux formulaires d'élément | `multilist` | `0` = Non<br />`2` = Utiliser du code personnalisé | `0` (Non) |
| **Code personnalisé**<br />`auto_value_code` | Entrez le code PHP à utiliser pour créer la valeur personnalisée, veuillez vider ce champs et enregistrez pour charger l'exemple par défaut, puis personnaliser | `editor` | — | `fields; if ( !isset($F['fieldname01']) ) return array('fieldname01 field not found'); $vals = array(); foreach($F['fieldname01']-&gt;postdata as $i =&gt; $v) &#123; $vals[$i] = 'Auto : ' . $v; &#125; return $vals;` |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `multilist` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne<br />`-1` = Comme espace réservé | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Texte saisi

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Espaces réservés**<br />`placeholder` | Ce sera le Texte affiché dans le champ saisie avant que le texte soit tapé. ** Note **: Cela peut être une chaîne de langue | `text` | — | — |
| **Longueur maximum du texte**<br />`maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | — |
| **Taille du champ**<br />`size` | Taille du champ dans le formulaire de saisie | `text` | — | `30` |
| **Attributs du champ**<br />`extra_attributes` | Saisir ici quelques attributs supplémentaires (paramètres de balises HTML) pour le champ de formulaire comme par exemple onkeypress="" onmouseover="..." somename="somevalue". Veillez à ne pas briser la syntaxe HTML du champ de formulaire | `text` | — | — |

#### Préfixe / Suffixe

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_form` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_form` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

#### Liste déroulante

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Disposition**<br />`select_field_placement` | — | `radio` | `0` = Avant<br />`1` = Après | `0` (Avant) |
| **Mode de la liste des valeurs**<br />`select_field_mode` | Configurer les valeurs que vous souhaitez faire apparaitre dans la zone de liste. | `multilist` | `1` = Eléments personnalisés<br />`2` = Requête SQL<br />`0` = Tous les valeurs existantes<br />`-1` = Toutes les valeurs existantes + éléments personnalisés<br />`-2` = Toutes les valeurs existantes + requête SQL | `0` (Tous les valeurs existantes) |
| **Liste des valeurs**<br />`select_field_elements` | Éléments personnalisés ou une requête SQL. Pour les **éléments personnalisés**, la syntaxe est la suivante : valeur1 : :label1%% value2: :label2%% Pour une**requête SQL**, entrez : SELECT value, value as text FROM #__flexicontent_fields_item_relations WHERE field_id='&#123;field_id&#125;' AND value != '' GROUP BY value **Vous pouvez utiliser des valeurs de remplacement** : pour des données du champ actuel : &#123;field-&gt;id&#125; &#123;field-&gt;field_type&#125; et pour des données du contenu : &#123;item-&gt;created_by&#125; &#123;item-&gt;catid&#125; etc. **NOTE** : Les noms seront transmises par le biais de JText... pour permettre la prise en charge multilingue (vous pouvez les ajouter à vos fichiers de langue) | `fcsortablelist` | — | `SELECT value, value as text FROM #__flexicontent_fields_item_relations WHERE field_id='&#123;field-&gt;id&#125;' AND value != '' GROUP BY value` |
| **Texte pour la première option (message d'information)**<br />`select_field_prompt` | Le texte de la première option de la liste déroulante, ex. 'Sélectionner une valeur existante' etc. **NOTE**: Cette option n'est associée à aucune valeur **NOTE**: Ce texte est filtre par langue, vous pouvez donc utiliser une chaine de remplacement dans vos fichiers langues | `text` | — | — |

### Importation

#### Manipuler les valeurs lors de l'importation

:::note
Version Flexicontent PRO uniquement
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Remapper les valeurs**<br />`import_fv_remap_mode` | Activer pour changer certaines valeurs importées en d'autres valeurs. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Remappages de valeur**<br />`import_fv_remap` | Format des données importValue1::realValue1%% importValue2::realValue2%% importValue3::realValue3%% | `textarea` | — | — |
| **Manipulation des valeurs**<br />`import_fv_ccode_mode` | Exécuter des méthodes personnalisées pour manipuler les valeurs de champ | `multilist` | `0` = Non<br />`2` = Utiliser du code personnalisé | `0` (Non) |
| **Code personnalisé**<br />`import_fv_ccode` | Entrez le code PHP à utiliser pour créer la valeur personnalisée, veuillez vider ce champs et enregistrez pour charger l'exemple par défaut, puis personnaliser | `editor` | — | `parameters-&gt;get('some_param'); foreach($values as $i =&gt; $v) &#123; $values[$i] = 'Example ' . $i . ' : ' . $v; &#125; return $values;` |

#### Édition

## Apparence

#### Apparence

### Basique

#### Affichage

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher pour les clients**<br />`show_in_clients` | Sélectionner si le champ sera créé et affiché à des clients spécifiques | `fccheckbox` | — | — |
| **Afficher dans les vues**<br />`show_in_views` | Sélectionner si le champ sera créé et affiché en fonction d'une vue spécifique | `fccheckbox` | — | — |

#### Libellé et accès

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Montrer un message d'**accès interdit****<br />`show_acc_msg` | Si le champ est inaccessible, une message de non-accès s'affichera. **NOTE : ** SI ce paramètre est désactivé, le champ sera invisible aux utilisateurs sans accès, sans aucun message ou avertissement indiquant son existance | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Message **accès interdit****<br />`no_acc_msg` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Exporter

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Inclure l'export CSV**<br />`include_in_csv_export` | Sélectionnez pour inclure le champ dans l'export CSV. Assurez-vous que tous les champs supportent bien l'exportation CSV. Veuillez vérifier si ce champ est correctement inclus, car une méthode spéciale est nécessaire mais n'est pas encore implémentée par tous les champs | `multilist` | `0` = Non<br />`1` = Valeurs brutes<br />`2` = Valeurs de rendu | `0` (Non) |
| **Supprimer html**<br />`csv_strip_html` | — | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### FLEXI_BACKEND_VIEW

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_BACKEND_VIEW_APPEARANCE**<br />`backend_view_appearance` | FLEXI_BACKEND_VIEW_APPEARANCE_DESC | `multilist` | `0` = Par défaut<br />`1` = FLEXI_CHECK_MARK<br />`2` = FLEXI_CLEAN_HTML_AND_TRIM | `0` (Par défaut) |
| **FLEXI_TRIM_LENGTH**<br />`backend_view_trim_chars` | FLEXI_TRIM_LENGTH_DESC | `text` | — | `100` |

### Mise en Page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mise en page des valeurs**<br />`viewlayout` | Veuillez noter : - ne pas modifier les mises en page par défaut, - Des mises en page personnalisées peuvent nécessiter une mise à jour à l'avenir pour respecter la nouvelle configuration et fonctionner correctement - pour créer une nouvelle copie (même dossier) : plugins/flexicontent_fields/FIELD_TYPE/tmpl/value_*. hp comme value_mytemplate. hp - ou vers le dossier : /templates/SOME_NAME/html/flexicontent_fields/FIELD_TYPE/ puis modifiez | `fcfilelist` | — | — |

#### Valeurs affichées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Valeurs du filtre de langue**<br />`lang_filter_values` | Applique le filtre de langue JText::_() aux libellés ; ces libellés doivent être des chaînes de langue, ajoutées dans un fichier de langue ou via le gestionnaire de surcharges de langue Joomla | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Encoder les valeurs (sécurisation XSS, HTML/JS visible)**<br />`encode_output` | Encoder n'importe quel HTML/JS à l'intérieur des valeurs rendra visible n'importe quel code HTML/JS, donc les valeurs deviennent XSS en sécurité (cross site scripting). NOTE : activez ceci, - si vous soupçonnez que les valeurs dangereuses XSS ont été ajoutées au champ par des configurations de champs plus anciennes, - ou si vous voulez afficher le code HTML qui n'est pas déjà encodé en tant qu'entités HTML | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Nettoyer valeurs (par ex. enlever HTML / JS)**<br />`clean_output` | Vous pouvez faire une étape supplémentaire pour nettoyer tout HTML non sûr ou non désiré dans les valeurs, NOTE : activez ceci, - si vous soupçonnez que le html peut être dangereux via une faille XSS, ou que du formatage du HTML non désiré pourrait être ajouté au champ par des configurations de champs plus anciennes | `radio` | `0` = Non<br />`1` = HTML non-sécurisé<br />`2` = TOUT HTML | `0` (Non) |

#### Rendu personnalisé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Format comme**<br />`format_output` | Format d'affichage personnalisé , par exemple format décimal | `multilist` | `0` = Non formaté<br />`-1` = Fonction personnalisée<br />`1` = Décimale<br />`2` = Entier | `0` (Non formaté) |
| **Combien de décimale**<br />`decimal_digits_displayed` | Nombre de décimales à afficher | `text` | — | `2` |
| **Point de séparateur décimal**<br />`decimal_digits_sep` | Caractère ou chaîne à indiquer pour le début de décimales | `text` | — | `.` |
| **Séparateur de milliers**<br />`decimal_thousands_sep` | Caractère pour séparer les milliers , des millions , des milliards , etc. | `text` | — | `,` |
| **Préfixe**<br />`output_prefix` | — | `text` | — | — |
| **Suffixe**<br />`output_suffix` | — | `text` | — | — |
| **Fonction personnalisée**<br />`output_custom_func` | Utiliser une fonction personnalisée pour formater la valeur, Remarque : - Utiliser $value en référence à la valeur - Utiliser une instruction return pour renvoyer la valeur formatée | `editor` | — | `$value_length = mb_strlen($value, 'UTF-8'); return 'Value length is: '. $value_length;` |

### Liste Valeurs

#### Préfixe - Suffixe - Séparateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pré-configuration**<br />`prx_sfx_open_close_configs` | Il s'agit d'une liste de configurations prédéfinies, après les avoir charger, vous pouvez les personnaliser | `multilist` | `—` = Personnalisé<br />`1` = List: numbered<br />`2` = List (bullets)<br />`3` = List (circle)<br />`4` = List (square)<br />`5` = Liste (sans marquage)<br />`6` = Badge<br />`7` = Badge success<br />`8` = Badge info<br />`9` = Badge warning<br />`10` = Badge important | — |
| **Supprimer les espaces**<br />`remove_space` | Supprimer les espaces en début et fin de chaîne. Cette option est recommandé pour l'utilisation des plugins, par exemple &#123;play&#125;machanson.mp3&#123;/play&#125; | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Préfixe pour chaque valeur**<br />`pretext` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |

:::note
Remarque : Les textes d'ouvertures et de fermetures ainsi que les texte de séparations de valeurs ne seront pas utiliser dans champ de type groupe
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Séparateur de valeurs (vues frontend)**<br />`separatorf` | Choisir le séparateur pour séparer l'ensemble des valeurs dans l'affichage frontend (placé entre les valeurs) | `multilist` | `0` = Espace<br />`1` = Saut de ligne<br />`6` = Ligne Horizontale<br />`2` = Barre<br />`3` = Virgule<br />`4` = Textes: Fermeture + Ouverture<br />`5` = Vide (aucun caractère)<br />`7` = Séparateur personnalisé | `1` (Saut de ligne) |
| **Séparateur personnalisé**<br />`separatorf_custom` | — | `text` | — | — |
| **Texte d'ouverture**<br />`opentag` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

### Plugins de contenu

#### Plugins de Contenu -- Vous en aurez besoin pour le champ description, pour les autres champs, à activer seulement si nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Exécuter les plugins de contenu**<br />`trigger_onprepare_content` | Activez cette option si vous voulez déclencher l'événement du plugin de contenu : onPrepareContent. Un nombre réduit de plugins pourraient ne pas fonctionner en dehors de com_content. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Exécuter dans la catégorie**<br />`trigger_plgs_incatview` | Exécuter les plugins de contenu de ce champ quand le contenu est affiché dans une vue catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Plugins spécifiques seulement**<br />`plugins` | Vous pouvez choisir des plugins spécifiques dans cette liste ou laisser vide pour tout déclencher. Cette fonctionnalité est utile dans certains cas pour éviter les conflits, les affichages multiples ou réduire la charge. Gardez à l'esprit qu'une fois le plugin importé pour un champ, il sera automatiquement exécuté sur tous les champs suivants dans la boucle. | `pluginlist` | — | — |

#### Apparence

## Référencement

### Prise en charge des microdonnées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Propriété des microdonnées**<br />`microdata_itemprop` | Sélectionnez une propriété de microdonnées pour caractériser toutes les valeurs de ce champ. Cela permettra aux moteurs de recherche de classer les valeurs de ce champ de manière appropriée, améliorant ainsi le référencement de vos pages | `microdataprops` | — | — |

## Réseaux sociaux

### Prise en charge des réseaux sociaux (ex. Facebook)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Suggérer le champ aux listes**<br />`useogp` | Intégrer le champ texte dans l'Open Graph (og:description ou og:title) | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Utiliser le champ comme**<br />`ogpusage` | Sélectionner comment utiliser le champ dans l'Open Graph (og:title ou og:description) | `radio` | `1` = Titre<br />`2` = Description | `1` (Titre) |
| **Longueur maximum du texte**<br />`ogpmaxlen` | Saisir le nombre maximum de caractères à utiliser avant d'être tronqué. | `text` | — | `300` |

## Filtrer

Paramètres utilisés pour la recherche/filtre dans (a)la vue catégorie, (b)la vue recherche

#### Filtrer

### Valeurs

#### Créer les options de filtre

:::note
Veuillez faire attention à bien construire votre requête SQL ou la liste d'éléments -- Remarque : la partie 'valeur' pour la requête SQL/la liste d'éléments doit correspondre aux valeurs existantes du champ
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Récupération personnalisé des valeurs du filtre**<br />`filter_customize_options` | Définissez si vous souhaitez utiliser toutes les valeurs pour le filtre, ou construire une liste de valeurs spécifiques à partir d'une requête SQL/ liste d'éléments | `multilist` | `0` = Non, utiliser toutes les valeurs (par défaut)<br />`1` = Utiliser une requête personnalisée<br />`2` = Utiliser des valeurs personnalisées | `0` (Non, utiliser toutes les valeurs (par défaut)) |
| **Liste d'éléments ou requête SQL personnalisée**<br />`filter_custom_options` | Éléments personnalisés ou une requête SQL. Pour les **éléments personnalisés**, la syntaxe est la suivante : valeur1 : :label1%% value2: :label2%% Pour une**requête SQL**, entrez : SELECT value, value as text FROM #__flexicontent_fields_item_relations WHERE field_id='&#123;field_id&#125;' AND value != '' GROUP BY value **Vous pouvez utiliser des valeurs de remplacement** : pour des données du champ actuel : &#123;field-&gt;id&#125; &#123;field-&gt;field_type&#125; et pour des données du contenu : &#123;item-&gt;created_by&#125; &#123;item-&gt;catid&#125; etc. **NOTE** : Les noms seront transmises par le biais de JText... pour permettre la prise en charge multilingue (vous pouvez les ajouter à vos fichiers de langue) _SELECT value, value as text FROM #__flexicontent_fields_item_relations WHERE field_id='&#123;field-&gt;id&#125;' AND value != '' GROUP BY value_ | `textarea` | — | — |
| **Ordre des valeurs de filtrage**<br />`reverse_filter_order` | Activer pour afficher les valeurs de filtre dans l'ordre inverse. NOTE : dans le cas de l'affichage de la plage du slider, la poignée de gauche sera le maximum, et la poignée de droite sera le minimum | `radio` | `0` = Normal<br />`1` = Inverse | `0` (Normal) |

#### Comparaison des valeurs de filtre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comparaison des valeurs de filtre**<br />`filter_compare_type` | Valeurs de filtrage qui peuvent être comparées de manière alphanumérique ou numérique (entier / à virgule flottante) | `radio` | `0` = Alphanumérique<br />`1` = Entier<br />`2` = Virgule flottante | `0` (Alphanumérique) |

:::note
... si le champ est multiple (Formulaire de contenu) ... et a une apparence de filtre multiple
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Requérir TOUTES les valeurs sélectionnées**<br />`filter_values_require_all` | Habituellement, vous allez inclure des éléments trouvés ayant une des valeurs sélectionnées. -- Vous pouvez sélectionner **pour que toutes les valeurs de filtre** sélectionnées soient correspondantes pour les éléments trouvés. -- **AVERTISSEMENT** aux développeurs de nouveaux types de champs : cela ne fonctionnera pas correctement si votre champ enregistre la valeur du champ SAME plus d'une fois pour le même élément. Donc, dans un tel cas, n'ajoutez pas cette option à votre champ ! | `radio` | `0` = Non<br />`1` = Oui, plus lentement | `0` (Non) |
| **Information pour Requérir AU MOINS UNE / TOUTES**<br />`filter_values_require_all_tip` | choisir de montrer l'information si aucune ou toutes les valeurs de filtre sélectionnées sont requises | `radio` | `0` = Cacher<br />`1` = Montrer | `0` (Cacher) |

### Vue Catégorie

#### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Recherche texte (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Sélecteur liste déroulante

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Option par défaut personnalisé (pour toutes les valeurs)**<br />`filter_usefirstoption` | Activer pour personnaliser la première option du filtre (=toutes les valeurs) . NOTE : ceci n'est utilisé que dans le cas de la sélection déroulante, et aussi si l'étiquette du champ n'est pas placée à l'intérieur du sélecteur | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'option par défaut (ex. Toutes les couleurs)**<br />`filter_firstoptiontext` | Texte de la première option de la sélection déroulante, par exemple « Toutes les couleurs » ou « FLEXI_ALL » etc. **NOTE**: Cette option n'a aucune valeur **NOTE**: Ce texte est filtré dans la langue de sorte que vous pouvez entrer une chaîne de langue remplaçable | `text` | — | `FLEXI_ALL` (Tous) |

#### Curseur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Données du slider**<br />`slider_display_config` | Utiliser les valeurs existantes dans le champ, ou spécifier vos propre valeurs d'échelle | `multilist` | `1` = Valeurs trouvées<br />`2` = Valeurs personnalisées | `1` (Valeurs trouvées) |
| **Valeurs personnalisées**<br />`slider_custom_range` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': '50', '50%': '150', '75%': '600', 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_50 ## label_150 ## label_600 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Préfixe / Suffixe

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_filter` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_filter` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Texte d'ouverture**<br />`opentag_filter` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_filter` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

### Vue recherche avancée

#### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette du filtre**<br />`display_label_filter_s` | Vous pouvez désactiver l'étiquette de filtre ou le régler pour apparaître avant (à gauche) le filtre ou à l'intérieur du filtre. **NOTE :** Ce paramètre peut être écrasé dans les paramètres de filtrage de catégorie pour TOUS les filtres de catégorie à la fois | `radio` | `0` = Non<br />`1` = En dehors du filtre<br />`2` = Dans le filtre | `2` (Dans le filtre) |
| **Type d'affichage du filtre**<br />`display_filter_as_s` | Sélectionner l'apparence du filtre | `multilist` | `0` = Sélecteur liste déroulante<br />`1` = Texte à Rechercher<br />`7` = Slider<br />`2` = Liste déroulante (intervalle)<br />`3` = Recherche texte (intervalle)<br />`8` = Slider (écart)<br />`4` = Option bouton radio<br />`5` = Case à Cocher (multiple)<br />`6` = Sélecteur par mot clé (multiple) | `0` (Sélecteur liste déroulante) |
| **Filtre personnalisable valeurs en fonction de ...**<br />`faceted_filter_s` | Calculez les valeurs de filtre affichées selon la **configuration de la page** ou selon les **filtres actifs**. OPTION: **Désactivez ceci** pour afficher toutes les valeurs et atteindre de hautes performances sur les grands sites (plus de 10, 00 articles par catégorie ou plus de 10 000 articles dans l'index de recherche). OPTION: **La configuration de la page** est mise en cache et aura un impact sur les performances de la première page (pour les grands sites) -- cette option affiche les valeurs de filtre en ne tenant compte que de la configuration de la catégorie et/ou de la configuration de l'élément de menu (catégorie/recherche). OPTION: **Filtres actifs** n'est pas mis en cache et aura un impact modéré sur chaque chargement de page (grands sites) lorsque (et if) l'utilisateur active certains filtres. -- cette option affiche les valeurs de filtre en tenant compte de tout : l'index alpha, recherche de texte, filtres de champs, etc, offrant ainsi **meilleures expériences utilisateur**. | `multilist` | `0` = Non, afficher toutes les valeurs (haute performance)<br />`1` = Configuration par page (Rapide & cache utilisable)<br />`2` = Filtres activés (meilleure expérience utilisateur) | `2` (Filtres activés (meilleure expérience utilisateur)) |

#### Filtre personnalisable des 'Filtres actifs' (configuré ci-dessus)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nb. de contenu pour chaque valeur filtrée**<br />`show_matching_items_s` | Activez pour ajouter le nombre de contenus correspondants après chaque valeur de filtre. **NOTE** : Cela n'ayant aucun sens quand le filtre est affiché en tant que gamme ou champ texte, il n'est donc pas utilisé dans ces scénarios | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Valeurs non disponibles for le filtre personnalisante utilisant les filtres actifs**<br />`hide_disabled_values_s` | Sélectionnez pour EITHER **désactiver** OU **cacher** les valeurs non disponibles. **AVIS**: Ceci affecte les valeurs qui ne sont pas disponibles en raison des filtres actifs. **NOTE**: Cela ne fonctionne que si vous affichez les valeurs de filtre en fonction des filtres actifs (ci-dessus) | `radio` | `0` = Désactiver<br />`1` = Cacher | `0` (Désactiver) |

#### Sélecteur liste déroulante

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Option par défaut personnalisé (pour toutes les valeurs)**<br />`filter_usefirstoption_s` | Activer pour personnaliser la première option du filtre (=toutes les valeurs) . NOTE : ceci n'est utilisé que dans le cas de la sélection déroulante, et aussi si l'étiquette du champ n'est pas placée à l'intérieur du sélecteur | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte d'option par défaut (ex. Toutes les couleurs)**<br />`filter_firstoptiontext_s` | Texte de la première option de la sélection déroulante, par exemple « Toutes les couleurs » ou « FLEXI_ALL » etc. **NOTE**: Cette option n'a aucune valeur **NOTE**: Ce texte est filtré dans la langue de sorte que vous pouvez entrer une chaîne de langue remplaçable | `text` | — | `FLEXI_ALL` (Tous) |

#### Curseur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Données du slider**<br />`slider_display_config_s` | Utiliser les valeurs existantes dans le champ, ou spécifier vos propre valeurs d'échelle | `multilist` | `1` = Valeurs trouvées<br />`2` = Valeurs personnalisées | `1` (Valeurs trouvées) |
| **Valeurs personnalisées**<br />`slider_custom_range_s` | Plage de valeurs personnalisée, veuillez utiliser des valeurs qui existent dans le champ ! pour le format, voir le format d'exemple, entrez des valeurs séparées par des virgules : pourcentage%: 'valeur', et au lieu de 0% ou 100%, vous devez utiliser 'min': 'valeur' et 'max':'min': 'valeur' | `textarea` | — | `'min': '', '25%': 500, '50%': 2000, '75%': 10000, 'max': ''` |
| **Etiquettes personnalisées**<br />`slider_custom_labels_s` | Étiquettes personnalisées pour correspondre aux valeurs, veuillez entrer un ## libellé séparé sans guillemets de début ou de fin | `textarea` | — | `label_any ## label_500 ## label_2000 ## label_10000 ## label_any` |
| **Les libellés sont des chaînes de langue**<br />`slider_custom_labels_jtext_s` | Définir comme oui pour traiter les libellés comme des chaînes de langue, n'oubliez pas de les ajouter à votre gestionnaire de langue Joomla ou dans d'autres fichiers de langue chargés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Préfixe / Suffixe

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Préfixe pour chaque valeur**<br />`pretext_filter_s` | Ce texte sera placé **avant** chaque valeur du champ | `text` | — | — |
| **Suffixe pour chaque valeur**<br />`posttext_filter_s` | Ce texte sera placé **après** chaque valeur du champ | `text` | — | — |
| **Texte d'ouverture**<br />`opentag_filter_s` | Ceci sera appliqué une seule fois au DEBUT du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |
| **Texte de fermeture**<br />`closetag_filter_s` | Ceci sera appliqué une seule fois à la FIN du champ. Il est censé créé la fin du champ HTML, mais vous pouvez choisir de le placer comme SEPARATEUR du texte et des valeurs aussi. Il est préférable d'utiliser ces paramètres: **Préfixe/Suffixe texte des valeurs** si elles existent pour ce type de champ. | `text` | — | — |

#### Filtrer
