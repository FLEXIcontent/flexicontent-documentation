---
title: Créer un layout de champ
sidebar_position: 3
---

# Créer un layout de champ

Un **layout de champ** contrôle le HTML d’un seul champ. Ce n’est pas la même chose qu’un modèle de contenu ou de catégorie : le modèle de contenu décide *où* un champ est affiché ; le layout de champ décide *comment sa valeur ou son champ de formulaire est rendu*.

:::info Source
Basé sur FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), notamment `admin/helpers/fcfield/parentfield.php`, `admin/elements/fcfilelist.php`, `admin/elements/fclayout.php` et les layouts fournis dans `plugins/flexicontent_fields/*/tmpl/`.
:::

:::tip
Un layout ne modifie que le rendu. Si vous avez besoin d’un nouveau moyen de stocker, valider ou traiter une valeur, créez plutôt un [plugin de type de champ](./create-a-field-type.md).
:::

## Terminologie

| Ce que vous personnalisez | Paramètre | Motif de fichier |
| --- | --- | --- |
| Affichage de la valeur en frontend | `viewlayout` | `value_<name>.php` |
| Champ du formulaire de contenu | `formlayout` | `field_<name>.php` |
| Galerie d’images | `popuptype`, `popuptype_mobile` | `value_gallery_<name>.php` ou `value_<name>.php` |
| Page contenu complète | `ilayout` | `components/com_flexicontent/templates/<layout>/item.php` |
| Page catégorie complète | `clayout` | `components/com_flexicontent/templates/<layout>/category.php` |

Le sélecteur de layout ne stocke que le suffixe. `value_MyLayout.php` est sélectionné sous le nom `MyLayout`.

## Où se trouvent les fichiers de layout

Pour un type de champ personnalisé :

```text
plugins/flexicontent_fields/<field_type>/tmpl/value_MyLayout.php
plugins/flexicontent_fields/<field_type>/tmpl/value_MyLayout.xml   # paramètres facultatifs
plugins/flexicontent_fields/<field_type>/tmpl/field_MyForm.php
```

Pour un champ core, un dossier de sous-type est ajouté :

```text
plugins/flexicontent_fields/core/tmpl/<subtype>/value_MyTitle.php
```

Exemples de sous-types : `title`, `created`, `createdby`, `modified`, `modifiedby`, `voting`, `favourites`, `categories`, `tags`.

Une surcharge de modèle Joomla peut également fournir le fichier :

```text
templates/<active_template>/html/flexicontent_fields/<field_type>/value_MyLayout.php
templates/<active_template>/html/flexicontent_fields/core/<subtype>/value_MyTitle.php
```

À l’exécution, la surcharge Joomla est prioritaire sur le fichier du plugin. Cependant, la liste des layouts explore généralement les dossiers des **plugins**. Conservez un fichier découvrable dans `tmpl/` si vous voulez que le layout apparaisse dans le sélecteur.

:::caution
Ne modifiez jamais un layout fourni par défaut. Copiez-le d’abord sous un autre nom. Les layouts personnalisés peuvent nécessiter une révision après une mise à jour de FLEXIcontent.
:::

## Comment le sélecteur trouve les layouts

La plupart des types de champs utilisent le sélecteur classique `fcfilelist` :

```xml
<field
    name="viewlayout"
    type="fcfilelist"
    directory="plugins/flexicontent_fields/text/tmpl/"
    filter="^value_.*\.php$"
    stripext="1"
    stripprefix="value_"
    hide_none="1"
    hide_default="1"
/>
```

`fcfilelist` liste les fichiers correspondant au filtre, retire le préfixe `value_` et l’extension `.php`, puis stocke le suffixe restant.

Certains types de champs utilisent `fclayout`, qui peut regrouper les layouts intégrés et charger les paramètres d’un fichier XML du même nom via AJAX. Le champ image est un cas particulier : il utilise `popuptype` pour la galerie desktop et `popuptype_mobile` pour une surcharge mobile.

## Procédure : créer un layout d’affichage

### 1. Choisir un layout de base

Copiez le layout par défaut du **même type de champ**, car chaque plugin expose des variables différentes.

```text
text       → plugins/flexicontent_fields/text/tmpl/value_default.php
file       → plugins/flexicontent_fields/file/tmpl/value_InlineBoxes.php
image      → plugins/flexicontent_fields/image/tmpl/value_gallery_fancybox.php
core/title → plugins/flexicontent_fields/core/tmpl/title/value_default.php
```

Un paramètre vide ne résout pas toujours vers `value_default.php`. Par exemple, `file` et `mediafile` utilisent par défaut `value_InlineBoxes.php`, et `toolbar` utilise `value_sharing_button.php`.

### 2. Copier et renommer le fichier

```text
plugins/flexicontent_fields/text/tmpl/value_default.php
→
plugins/flexicontent_fields/text/tmpl/value_MyLayout.php
```

Le suffixe doit respecter les règles du sélecteur. Avec le filtre habituel `value_*.php`, utilisez des lettres, des chiffres et des tirets bas. `MyLayout.php` ou `valueMyLayout.php` ne seront pas trouvés.

### 3. Modifier le layout PHP

Un layout de type texte respecte ce contrat :

```php
<?php
/**
 * value_MyLayout.php
 *
 * Variables supplied by the field plugin include:
 * $field, $item, $values, $prop, $view, $sfx,
 * $is_ingroup, $use_ingroup, $multiple,
 * $pretext, $posttext, $opentag, $closetag,
 * $separatorf, $itemprop, $no_value_msg, $remove_space
 */

$n = 0;

foreach ($values as $value)
{
    if ($value === null || !strlen($value))
    {
        if ($is_ingroup)
        {
            $field->{$prop}[$n++] = '';
        }
        continue;
    }

    // Escape values unless trusted HTML is intentional.
    $html = htmlspecialchars((string) $value, ENT_QUOTES, 'UTF-8');
    $html = '<span class="my-field-value">' . $html . '</span>';

    // Prefix and suffix are configured in the field parameters.
    $field->{$prop}[$n] = $pretext . $html . $posttext;

    // Per-value microdata is needed for fields inside a field group.
    if ($is_ingroup && $itemprop)
    {
        $field->{$prop}[$n] =
            '<div style="display:inline" itemprop="' . $itemprop . '">'
            . $field->{$prop}[$n]
            . '</div>';
    }

    $n++;

    if (!$multiple)
    {
        break;
    }
}
```

Un layout **écrit normalement dans** `$field->{$prop}` ; il ne renvoie pas la valeur finale avec `echo`. Le plugin de champ applique ensuite `$separatorf`, `$opentag`, `$closetag`, les microdonnées et le message « sans valeur » après l’inclusion du layout.

| Variable | Signification |
| --- | --- |
| `$field` | Objet champ, avec `$field->parameters`, `$field->id`, `$field->name`, `$field->label`. |
| `$item` | Contenu courant. |
| `$values` | Valeurs brutes du champ. |
| `$prop` | Propriété à remplir, généralement `display` ou un suffixe de méthode d’affichage. |
| `$view` | Vue courante, par exemple `item` ou `category`. |
| `$multiple` | Indique si le champ accepte plusieurs valeurs. |
| `$is_ingroup` | Indique si le champ est rendu dans un groupe de champs répétable. |
| `$pretext`, `$posttext` | Préfixe et suffixe configurés. |
| `$separatorf` | Séparateur entre plusieurs valeurs rendues. |
| `$opentag`, `$closetag` | Balises englobant la liste complète des valeurs. |
| `$itemprop` | Propriété de microdonnées. |
| `$no_value_msg` | Message affiché quand le champ est vide. |

Les champs complexes exposent davantage de variables. Lisez les commentaires en tête du layout de base avant de le modifier.

### 4. Ajouter facultativement des paramètres au layout

Un fichier XML de même nom peut définir les paramètres du layout :

```text
plugins/flexicontent_fields/text/tmpl/value_MyLayout.xml
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<form>
    <name>My custom layout -- Text</name>
    <author>Your Name</author>
    <version>1.0</version>
    <description>Custom parameters for value_MyLayout.php</description>

    <fields name="attribs">
        <fieldset name="layout" addfieldpath="/administrator/components/com_flexicontent/elements">
            <field
                name="PPFX_my_option"
                type="radio"
                default="0"
                label="MY_EXTENSION_MY_OPTION"
                description="MY_EXTENSION_MY_OPTION_DESC"
                class="btn-group btn-group-yesno">
                <option value="0">FLEXI_NO</option>
                <option value="1">FLEXI_YES</option>
            </field>
        </fieldset>
    </fields>
</form>
```

Lisez la valeur dans le layout PHP avec le préfixe du layout :

```php
$LP = 'viewlayout_';
$my_option = $field->parameters->get($LP . 'my_option', 0);
```

Utilisez `popuptype_` ou `popuptype_mobile_` au lieu de `viewlayout_` pour les galeries d’images. `PPFX_` est un espace réservé que FLEXIcontent remplace par le préfixe réel du paramètre de layout.

:::note
Les paramètres XML par layout sont chargés par le sélecteur amélioré `fclayout` avec `params_source="file"`. Avec le sélecteur classique `fcfilelist`, le layout fonctionne, mais ses paramètres XML ne sont pas affichés automatiquement dans le formulaire du champ.
:::

### 5. Sélectionner le layout dans la configuration du champ

1. Ouvrez le champ dans **Composants → FLEXIcontent → Champs**.
2. Dans la section **Viewing**, ouvrez **Layout**.
3. Définissez **Values layout** (`viewlayout`) sur `MyLayout`.
4. Enregistrez le champ.

Pour une galerie d’images, définissez plutôt **Gallery Layout** (`popuptype`). Pour le formulaire d’édition, utilisez **Fields layout** (`formlayout`) et choisissez le suffixe d’un fichier `field_*.php`.

### 6. Afficher le champ

Choisir un layout ne place pas le champ sur la page. Ajoutez le champ à une position de modèle de contenu ou de catégorie dans l’éditeur de modèles FLEXIcontent, ou affichez-le manuellement :

```php
$html = FlexicontentFields::getFieldDisplay($item, 'myfield');
echo $html;
```

Les méthodes d’affichage peuvent être sélectionnées explicitement :

```php
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display_small', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display_medium', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display_large', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'myfield', null, 'display_original', 'item');
```

Voir [Boucles de contenus et rendu des champs](../templates/loops-fields.md) et [Positions de champs et glisser-déposer](../templates/positions.md).

## Layouts de formulaire

Les layouts de formulaire utilisent le préfixe `field_<name>.php` et sont sélectionnés avec `formlayout`.

```text
plugins/flexicontent_fields/text/tmpl/field_MyForm.php
```

Copiez le fichier `field_default.php` du même type de champ, conservez les noms des champs du formulaire et l’intégration JavaScript, puis modifiez uniquement le balisage. Un nom incorrect ou un attribut de champ manquant peut empêcher l’enregistrement de la valeur dans le formulaire de contenu.

## Différence avec les modèles de contenu et de catégorie

| | Layout de champ | Modèle contenu/catégorie |
| --- | --- | --- |
| Portée | Une valeur ou un champ de saisie. | Page complète et positions de champs. |
| Fichiers | `value_*.php`, `field_*.php`. | `item.php`, `category_items.php`, manifestes XML. |
| Sélection | `viewlayout`, `formlayout`, `popuptype`. | `ilayout`, `clayout`. |
| Stockage | Paramètres du champ. | Configuration du contenu, de la catégorie ou de la mise en page. |
| Surcharge Joomla | `html/flexicontent_fields/<type>/`. | `html/com_flexicontent/...`. |

Les surcharges de vue de composant Joomla (`templates/<template>/html/com_flexicontent/<view>/default.php`) sont un troisième mécanisme et ne remplacent pas les layouts de champ.

## Points d’attention

- **Ne modifiez pas les layouts par défaut.** Copiez-les.
- **Respectez le préfixe exact.** `value_MyLayout.php`, pas `MyLayout.php`.
- **Copiez depuis le même type de champ.** Les variables diffèrent entre texte, fichier, image, relation et champs core.
- **Ne renvoyez pas la sortie avec `echo`.** Remplissez `$field->{$prop}` pour conserver séparateurs et balises.
- **Respectez les groupes et les valeurs multiples.** Conservez des emplacements vides quand `$is_ingroup` vaut true.
- **Échappez les valeurs et les URL.** Si votre layout contourne `clean_output` ou `encode_output`, utilisez `htmlspecialchars()` et validez les URL.
- **Utilisez des identifiants HTML uniques.** Le même champ peut être rendu pour plusieurs contenus. Basez les identifiants sur `$field->id` et `$item->id`.
- **Testez toutes les vues.** Contenu, catégorie, module, administration, mobile et groupes de champs peuvent différer.
- **Videz le cache si nécessaire.** Les chemins de layout et les définitions de modèles sont mis en cache pendant la requête et par Joomla.
- **Les plugins de contenu peuvent transformer la sortie.** Vérifiez `trigger_onprepare_content` et `trigger_plgs_incatview` si le résultat change de façon inattendue.
- **Administrateurs de confiance uniquement.** Les layouts de champ sont du PHP exécutable et leurs paramètres sont stockés avec des privilèges élevés.

## Références officielles

- [Créer un layout d’affichage pour le champ File](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/711-create-a-outout-layout-for-file-field.html)
- [Surcharger le rendu d’un champ](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/772-override-field-render.html)
- [Utiliser la valeur brute d’un champ dans un modèle ou dans le layout d’un autre champ](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/312-using-the-raw-value-of-a-field-inside-a-template-file-or-inside-a-new-custom-field-type.html)
- [Exemple de layout de champ pour le profil auteur](https://www.flexicontent.org/documentation/tutorials-english/71-fields-usages-tips-joomla-plugin/304-how-to-create-a-field-that-links-to-author-listing-view-of-current-item-author.html)
- [Index de l’API développeur / plugins de champs](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins.html)
- [Rendu manuel des champs avec `getFieldDisplay()`](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/248-upgrading-custom-templates-to-work-in-v156.html)
