---
sidebar_position: 14
---

# HTML personnalisé / onglet de formulaire

Plugin de marquage de groupe de champs pour FLEXIcontent. Ce champ marque le début/la fin des groupes de champs dans le formulaire de modification. Le groupe apparaîtra dans des onglets, fieldsets, etc. Veillez à associer chaque ouverture à un marqueur de fermeture.

*Plugin : `custom_form_html` — HTML personnalisé / onglet de formulaire / fieldset*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/custom_form_html/custom_form_html.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le champ dans un groupe**<br />`use_ingroup` | Activer pour permettre d'utiliser ce champ dans un groupe, qui sera configuré via champ 'Groupe de champ'. REMARQUE: Vous devez alors sélectionner ce champ UNIQUEMENT dans un groupe de champs | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Affichage conditionnel**<br />`showon` | Affiché en fonction de conditions. Utilisez le format Joomla 'fieldname:value' comme par exemple album_type:2 REMARQUE: ne pas définir ce champ en obligatoire. Également DÉSACTIVER les scripts prettyCheckable / Select2 JS dans tous les champs référencés de type select*, checkbox*, radio* | `text` | — | — |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `multilist` | `0` = Non | `0` (Non) |
| **Type de marqueur**<br />`marker_type` | ATTENTION à bien fermé les marqueurs que vous ouvrez avec le type de fermeture approprié. ATTENTION à quel type de contenu vous avez assigné au champ. | `multilist` | **Onglets**<br />`tabset_start` = Groupe d'onglets : DEBUT<br />`tab_open` = Onglet : ouvert<br />`tab_close` = Onglet : fermé<br />`tabset_end` = Groupe d'onglets : FIN<br />**Groupe de champs**<br />`fieldset_open` = Groupe de champs : ouvert<br />`fieldset_close` = Groupe de champs : fermé<br />**Autre**<br />`custom_html` = HTML personnalisé | `custom_html` (HTML personnalisé) |
| **Classe CSS du conteneur**<br />`cont_cssclass` | Classe CSS de l'onglet / groupe de champs / etc. dans le conteneur. Uniquement pour les marqueurs d'**ouverture** | `text` | — | — |

#### Onglet: Début / fieldset

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nom du groupe d'onglets/champs**<br />`cont_label` | Nom de l'onglet / groupe de champs / etc., uniquement pour les marqueurs d'**ouverture**. | `text` | — | — |

#### HTML personnalisé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **HTML personnalisé**<br />`custom_html_sep` | Entrez le code HTML personnalisé qui sera placé entre les champs | `editor` | — | — |
