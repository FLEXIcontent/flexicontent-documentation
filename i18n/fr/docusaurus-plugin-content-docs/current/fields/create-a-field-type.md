---
title: Créer un type de champ
sidebar_position: 4
---

# Créer un type de champ

Un **type de champ** est un plugin Joomla du groupe `flexicontent_fields`. Il fournit le code PHP qui affiche un champ dans le formulaire de contenu, rend sa valeur en frontend, valide les données enregistrées et, si vous le souhaitez, ajoute la prise en charge de la recherche et des filtres.

N’écrivez un nouveau type de champ que lorsqu’un type existant associé à un [layout de champ](./field-layouts.md) ne suffit pas. Si vous voulez simplement ajouter un champ d’un type existant, suivez [Créer un champ](./create-a-field.md).

:::info Source
Basé sur FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), notamment `plugins/flexicontent_fields/text/`, `admin/helpers/fcfield/parentfield.php`, `admin/models/field.php`, `admin/models/parentclassitem.php`, `site/classes/helpers/flexiutilities.php` et `site/classes/helpers/db.php`.
:::

## Ce que vous créez

| Tâche | Où cela se passe | Documentation |
| --- | --- | --- |
| Ajouter un champ d’un type existant | **Composants → FLEXIcontent → Champs** | [Créer un champ](./create-a-field.md) |
| Modifier le HTML d’un champ existant | Layouts `viewlayout` / `formlayout` | [Créer un layout de champ](./field-layouts.md) |
| Ajouter un nouveau comportement de stockage/rendu | Plugin `plugins/flexicontent_fields/<type>/` | Cette page |
| Ajouter un champ Joomla `com_fields` | Plugins de champs Joomla | Documentation Joomla |

Un type de champ FLEXIcontent n’est **pas** un plugin de champ personnalisé Joomla. Il s’enregistre dans `#__extensions` avec `folder = 'flexicontent_fields'` et ses valeurs sont stockées dans `#__flexicontent_fields_item_relations`.

## Structure des fichiers

L’élément du plugin correspond au nom du dossier. Utilisez des lettres minuscules, des chiffres et des tirets bas, sans espace.

```text
plugins/flexicontent_fields/myfield/
├── myfield.php                                  # obligatoire : classe principale
├── myfield.xml                                  # obligatoire : manifeste du plugin Joomla
├── index.html                                   # marqueur de dossier vide
├── en-GB.plg_flexicontent_fields_myfield.ini    # fichier de langue
├── tmpl/
│   ├── field_default.php                        # champ du formulaire de contenu
│   └── value_default.php                        # valeur en frontend
└── js/                                          # facultatif, si utilisé
```

`FLEXIUtilities::call_FC_Field_Func()` exige que le fichier principal soit exactement `plugins/flexicontent_fields/<element>/<element>.php`. Le gestionnaire de champs lève aussi une exception si `<element>.xml` est absent.

### Convention de nommage

Pour l’élément `myfield` :

| Élément | Valeur |
| --- | --- |
| Dossier | `plugins/flexicontent_fields/myfield/` |
| Fichier principal | `myfield.php` |
| Manifeste | `myfield.xml` |
| Classe | `plgFlexicontent_fieldsMyfield` |
| `static $field_types` | `array('myfield')` |
| `<name>` du manifeste | `FLEXIcontent - My Field` |
| `<filename plugin="...">` du manifeste | `myfield` |
| Noms des fieldsets | `group-myfield-editing`, `group-myfield-viewing`, … |
| Fichier de langue | `en-GB.plg_flexicontent_fields_myfield.ini` |

Le constructeur de `FCField` déduit le type de champ du nom de la classe (`strtolower(get_class($this))`) : la casse est donc importante. Le sélecteur retire le préfixe `FLEXIcontent - ` du nom du manifeste et affiche la suite.

## Choisir un plugin de base

Ne partez pas d’un fichier vide. Copiez le plugin fourni le plus proche de votre besoin :

| Plugin de base | À utiliser quand |
| --- | --- |
| `text` | Valeurs textuelles simples ou multiples, validation personnalisée, préfixes/suffixes. Meilleur point de départ général. |
| `textarea` | Textes plus longs avec une gestion des valeurs similaire. |
| `select`, `radio`, `checkbox` | Choix prédéfinis ; ces types étendent `FCIndexedField` pour des valeurs indexées et filtrables. |
| `email` | Validation spécifique aux adresses e-mail. |
| `file`, `image`, `mediafile` | Envois de fichiers, aperçus et nettoyage des fichiers. |

Le tutoriel officiel utilise exactement cette méthode : dupliquer le champ `text` et le renommer.

## Procédure pas à pas : dupliquer `text` en `myfield`

### 1. Copier le dossier

```bash
cp -a plugins/flexicontent_fields/text plugins/flexicontent_fields/myfield
```

Renommez les fichiers :

```text
text.php                                  → myfield.php
text.xml                                  → myfield.xml
en-GB.plg_flexicontent_fields_text.ini    → en-GB.plg_flexicontent_fields_myfield.ini
```

:::caution
Faites un recherche-remplacement **en validant chaque occurrence**. Le mot `text` apparaît aussi dans des noms sans rapport comme `JText`, `text-align` ou des alias SQL tels que `value as text`. Ne modifiez que les références au type de champ.
:::

### 2. Mettre à jour la classe PHP

Dans `myfield.php` :

```php
<?php
defined('_JEXEC') or die('Restricted access');

// Chargement différé de la classe de base FLEXIcontent (style 5.x).
spl_autoload_register(static function ($class) {
    $map = array(
        'FCField' => JPATH_ADMINISTRATOR . '/components/com_flexicontent/helpers/fcfield/parentfield.php',
    );
    if (isset($map[$class]) && is_file($map[$class])) require_once $map[$class];
}, true, true);

class plgFlexicontent_fieldsMyfield extends FCField
{
    static $field_types = array('myfield');

    var $task_callable = null;  // Méthodes appelables via AJAX ; null = aucune.

    public function __construct(&$subject, $params)
    {
        parent::__construct($subject, $params);
    }
}
```

`FCField` étend `\Joomla\CMS\Plugin\CMSPlugin` (`admin/helpers/fcfield/parentfield.php:14`). FLEXIcontent 5.x utilise encore les noms de classes de plugins historiques ; il n’y a pas d’espace de noms. Utilisez des appels pleinement qualifiés `\Joomla\CMS\...`, comme les plugins fournis.

Remplacez chaque garde-fou basé sur l’ancienne valeur littérale :

```php
if (!in_array($field->field_type, static::$field_types)) return;
```

:::note
Ne conservez pas le code 4.x obsolète tel que `jimport()` ou `JLoader::register('FCField', ...)`. En 5.x, le constructeur parent charge automatiquement les fichiers de langue `plg_flexicontent_fields_myfield` ; aucun appel manuel à `JPlugin::loadLanguage()` n’est nécessaire.
:::

### 3. Connaître les événements que vous pouvez implémenter

`FLEXIUtilities::call_FC_Field_Func()` instancie la classe et n’appelle une méthode que si elle existe. Implémenter une méthode active aussi les indicateurs de capacité correspondants dans les options du champ.

| Méthode | Signature exacte | Rôle |
| --- | --- | --- |
| `onDisplayField` | `(&$field, &$item)` | Construire le champ du formulaire de contenu. |
| `onDisplayFieldValue` | `(&$field, $item, $values = null, $prop = 'display')` | Construire la valeur en frontend. |
| `onBeforeSaveField` | `(&$field, &$post, &$file, &$item)` | Valider/nettoyer les valeurs envoyées avant l’écriture en base. Un retour `false` annule l’enregistrement. |
| `onAfterSaveField` | `(&$field, &$post, &$file, &$item)` | Nettoyage après l’écriture en base. |
| `onBeforeDeleteField` | `(&$field, &$item)` | Supprimer des données annexes avant la suppression du champ. |
| `onAllFieldsPostDataValidated` | `(&$field, &$item)` | Validation croisée entre champs. |
| `onDisplayFilter` | `(&$filter, $value = '', $formName = 'adminForm', $isSearchView = 0)` | Filtre de la vue catégorie. |
| `onAdvSearchDisplayFilter` | `(&$filter, $value = '', $formName = 'searchForm')` | Filtre de la recherche avancée. |
| `getFiltered` | `(&$filter, $value, $return_sql = true)` | Identifiants de contenus correspondants pour les filtres de catégorie. |
| `getFilteredSearch` | `(&$filter, $value, $return_sql = true)` | Identifiants de contenus correspondants pour les filtres de recherche. |
| `onIndexAdvSearch` | `(&$field, &$post, &$item)` | Index de la recherche avancée. |
| `onIndexSearch` | `(&$field, &$post, &$item)` | Index de la recherche simple. |

FLEXIcontent 5.x ne contient aucun événement nommé `onDisplay`, `onBeforeStore`, `onAfterStore`, `onSearch` ou `onIndexAdvanced`. N’utilisez pas ces noms.

Pour un champ simple de type texte, `FCField` fournit déjà des implémentations génériques des événements d’affichage et d’indexation. Ne redéfinissez que ce que vous devez modifier.

### 4. Ajouter les méthodes de rendu

Les méthodes d’affichage préparent les variables puis `include()` un layout de `tmpl/`. Le layout écrit dans `$field->html` pour le formulaire et dans `$field->{$prop}` pour la valeur.

Une version allégée des méthodes de `text` ressemble à ceci :

```php
public function onDisplayField(&$field, &$item)
{
    if (!in_array($field->field_type, static::$field_types)) return;

    $field->label = $field->parameters->get('label_form')
        ? \Joomla\CMS\Language\Text::_($field->parameters->get('label_form'))
        : \Joomla\CMS\Language\Text::_($field->label);

    $this->setField($field);
    $this->setItem($item);

    $multiple    = (int) $field->parameters->get('allow_multiple', 0);
    $use_ingroup = (int) $field->parameters->get('use_ingroup', 0);

    if (!$field->value || (count($field->value) === 1 && reset($field->value) === null)) {
        $field->value = $this->getDefaultValues(true);
    }

    $document  = \Joomla\CMS\Factory::getApplication()->getDocument();
    $fieldname = 'custom[' . $field->name . ']';
    $elementid = 'custom_' . $field->name;
    $attribs    = '';
    $classes    = 'fcfield_textval';
    $box_classes = 'fcfield_box';
    $validate_mask = '';
    $pretext_form  = $field->parameters->get('pretext_form', '');
    $posttext_form = $field->parameters->get('posttext_form', '');
    $auto_value    = 0;

    $field->html = array();

    $formlayout = $field->parameters->get('formlayout', '');
    $formlayout = $formlayout ? 'field_' . $formlayout : 'field_default';
    include(self::getFormPath($this->fieldtypes[0], $formlayout));

    $field->html = !count($field->html)
        ? ''
        : '<div class="fcfieldval_container valuebox fcfieldval_container_' . $field->id . '">'
          . implode('', $field->html) . '</div>';
}

public function onDisplayFieldValue(&$field, $item, $values = null, $prop = 'display')
{
    if (!in_array($field->field_type, static::$field_types)) return;

    $field->label = \Joomla\CMS\Language\Text::_($field->label);
    $this->setField($field);
    $this->setItem($item);

    $app  = \Joomla\CMS\Factory::getApplication();
    $view = $app->input->getCmd('flexi_callview', $app->input->getCmd('view', 'item'));
    if (!$this->checkRenderConds($prop, $view)) return;

    $values     = $values !== null ? $values : $field->value;
    $is_ingroup = !empty($field->ingroup);
    $multiple   = (int) $field->parameters->get('allow_multiple', 0);
    extract($this->getCommonParams());

    if ($prop === 'csv_export') {
        $separatorf = ', ';
        $itemprop   = false;
    }

    $field->{$prop} = array();

    $viewlayout = $field->parameters->get('viewlayout', '');
    $viewlayout = $viewlayout ? 'value_' . $viewlayout : 'value_default';
    include(self::getViewPath($field->field_type, $viewlayout));

    if (!$is_ingroup) {
        $field->{$prop} = implode($separatorf, $field->{$prop});

        if ($field->{$prop} !== '') {
            $field->{$prop} = $opentag . $field->{$prop} . $closetag;
            if ($itemprop) {
                $field->{$prop} = '<div style="display:inline" itemprop="' . $itemprop . '">' . $field->{$prop} . '</div>';
            }
        } elseif ($no_value_msg !== '') {
            $field->{$prop} = $no_value_msg;
        }
    }
}
```

Points importants :

- Aucun argument `$form`, `$input` ou `$id` isolé n’est transmis à un layout de champ. Utilisez `$field->parameters`, `$field->id`, `$item->id` et `$app->input`.
- `getFormPath()` et `getViewPath()` résolvent d’abord les surcharges dans `templates/<template>/html/flexicontent_fields/<element>/`, avant le dossier du plugin.
- `$fieldname` doit valoir `custom[<nom du champ>]` et les champs de formulaire doivent être nommés `custom[<nom du champ>][<n>]` ; sinon FLEXIcontent n’enregistre pas les valeurs.
- `getCommonParams()` fournit `$pretext`, `$posttext`, `$opentag`, `$closetag`, `$separatorf`, `$itemprop` et `$no_value_msg`.

### 5. Créer les fichiers de layout

`tmpl/field_default.php` :

```php
<?php
defined('_JEXEC') or die('Restricted access');

$n = 0;
foreach ($field->value as $value)
{
    $value       = $value ?? '';
    $fieldname_n = $fieldname . '[' . $n . ']';
    $elementid_n = $elementid . '_' . $n;

    $field->html[] = $pretext_form .
        '<div class="' . $box_classes . '">' .
            '<input type="text" id="' . htmlspecialchars($elementid_n, ENT_QUOTES, 'UTF-8') . '"' .
            ' name="' . htmlspecialchars($fieldname_n, ENT_QUOTES, 'UTF-8') . '"' .
            ' value="' . htmlspecialchars($value, ENT_COMPAT, 'UTF-8') . '"' .
            ' class="' . $classes . '" ' . $attribs . ' />' .
        '</div>' .
        $posttext_form;

    $n++;
    if (!$multiple && !$use_ingroup) break;
}
```

`tmpl/value_default.php` :

```php
<?php
defined('_JEXEC') or die('Restricted access');

$n = 0;
foreach ($values as $value)
{
    if ($value === null || !strlen($value))
    {
        if ($is_ingroup) $field->{$prop}[$n++] = '';
        continue;
    }

    $field->{$prop}[$n] = $pretext . htmlspecialchars($value, ENT_QUOTES, 'UTF-8') . $posttext;

    if ($is_ingroup && $itemprop)
    {
        $field->{$prop}[$n] = '<div style="display:inline" itemprop="' . $itemprop . '">' . $field->{$prop}[$n] . '</div>';
    }

    $n++;
    if (!$multiple) break;
}
```

Ce sont des exemples minimaux. Les layouts `text` fournis gèrent aussi les contrôles multi-valeurs, les masques de saisie, les microdonnées et les libellés flottants ; copiez-les lorsque vous avez besoin de ces fonctionnalités.

### 6. Valider avant l’enregistrement

Les valeurs des champs personnalisés sont stockées dans `#__flexicontent_fields_item_relations`. FLEXIcontent lit `custom[<nom du champ>]`, le normalise en tableau, désérialise les valeurs existantes et transmet le tableau par référence à `onBeforeSaveField()`.

Retournez `false` pour annuler l’enregistrement du contenu avec une erreur. Une implémentation typique :

```php
public function onBeforeSaveField(&$field, &$post, &$file, &$item)
{
    if (!in_array($field->field_type, static::$field_types)) return;
    if (!is_array($post) && !strlen($post)) return;

    $post      = !is_array($post) ? array($post) : $post;
    $maxlength = (int) $field->parameters->get('maxlength', 0);
    $validation = $field->parameters->get('validation', 'HTML');
    $required  = (int) $field->parameters->get('required', 0);
    $clean     = array();

    foreach ($post as $value)
    {
        $value    = trim((string) $value);
        $filtered = strlen($value) ? flexicontent_html::dataFilter($value, $maxlength, $validation, 0) : '';

        if ($value !== '' && $filtered === '') return false;
        if ($required && $filtered === '') return false;

        if (strlen($filtered)) $clean[] = $filtered;
    }

    $post = $clean;
}
```

Les ACL, l’état de publication et la visibilité par vue/client sont gérés par le cœur de FLEXIcontent. `checkRenderConds()` dans la méthode d’affichage respecte ces règles. Il n’existe pas de contrôle serveur générique `required` ou `unique` dans la chaîne d’enregistrement : implémentez ces règles vous-même.

### 7. Mettre à jour le manifeste XML

Un manifeste minimal pour l’exemple :

```xml
<?xml version="1.0" encoding="utf-8"?>
<extension type="plugin" version="1.6" group="flexicontent_fields" method="upgrade">
    <name>FLEXIcontent - My Field</name>
    <author>Your Name</author>
    <creationDate>2026-11-25</creationDate>
    <copyright>Copyright (C) 2026 Your Name</copyright>
    <license>GNU/GPL v2</license>
    <authorEmail>you@example.com</authorEmail>
    <authorUrl>https://example.com</authorUrl>
    <version>1.0.0</version>
    <description>FLEXI_FIELD_MYFIELD</description>
    <documentation url="https://www.flexicontent.org/documentation/" title="FLEXI_ABOUT" modal="1" icon="info" />

    <files>
        <filename plugin="myfield">myfield.php</filename>
        <filename>index.html</filename>
        <folder>tmpl</folder>
        <folder>js</folder>
    </files>

    <config>
        <fields name="attribs">
            <fieldset name="group-myfield-editing" hidden="true" icon_class="icon-pencil"
                      label="FLEXI_FIELD_EDITING"
                      addfieldpath="/administrator/components/com_flexicontent/elements">
                <field name="required" type="radio" default="0"
                       label="FLEXI_FIELD_REQUIRED" description="FLEXI_FIELD_REQUIRED_DESC"
                       class="btn-group btn-group-yesno">
                    <option value="0">FLEXI_NO</option>
                    <option value="1">FLEXI_YES</option>
                </field>
                <field name="default_value" type="text" filter="raw" default=""
                       label="FLEXI_PROPERTY_DEFAULT" description="FLEXI_PROPERTY_DEFAULT_DESC" />
                <field name="formlayout" type="fcfilelist" default=""
                       label="FLEXI_FIELD_SELECT_FORM_LAYOUT" description="FLEXI_FIELD_SELECT_FORM_LAYOUT_DESC"
                       directory="plugins/flexicontent_fields/myfield/tmpl/"
                       filter="^field_.*\.php$" stripext="1" stripprefix="field_"
                       hide_none="1" hide_default="1" />
                <field name="viewlayout" type="fcfilelist" default=""
                       label="FLEXI_FIELD_SELECT_VIEW_LAYOUT" description="FLEXI_FIELD_SELECT_VIEW_LAYOUT_DESC"
                       directory="plugins/flexicontent_fields/myfield/tmpl/"
                       filter="^value_.*\.php$" stripext="1" stripprefix="value_"
                       hide_none="1" hide_default="1" />
            </fieldset>
        </fields>
    </config>

    <languages>
        <language tag="en-GB">en-GB.plg_flexicontent_fields_myfield.ini</language>
    </languages>
</extension>
```

Règles essentielles :

- `group="flexicontent_fields"` et `type="plugin"` enregistrent l’extension auprès de Joomla. Il n’existe pas d’attribut de métadonnées FLEXIcontent supplémentaire.
- Le conteneur de paramètres est `<fields name="attribs">`, et **pas** `name="params"`.
- Les noms de fieldsets doivent commencer par `group-<type>-` ; sinon les options n’apparaissent pas dans l’éditeur de champ.
- Le `directory` des sélecteurs de layout doit pointer vers le dossier `tmpl/` de votre plugin.
- Ajoutez à `<files>` chaque dossier de ressources réellement livré, et incrémentez `<version>` pour les mises à jour.

### 8. Ajouter les chaînes de langue

`en-GB.plg_flexicontent_fields_myfield.ini` :

```ini
FLEXI_FIELD_MYFIELD="My Field Plugin for FLEXIcontent"
FLEXI_FIELD_MYFIELD_NOTE="Enter a value"
```

Le constructeur parent charge d’abord le fichier `en-GB`, puis la langue courante. Réutilisez les clés `FLEXI_*` existantes pour les libellés courants comme `FLEXI_FIELD_REQUIRED` ; ne définissez dans le fichier du plugin que vos propres clés.

### 9. Empaqueter, installer et activer

1. ZIPpez le dossier `myfield/`. Le XML doit être à la racine de ce dossier.
2. Allez dans **Extensions → Installer** et installez le paquet.
3. Allez dans **Extensions → Plugins** et activez **My Field** dans le groupe `flexicontent_fields`. Seuls les plugins activés apparaissent dans le sélecteur de type de champ.
4. Videz le cache Joomla.
5. Allez dans **Composants → FLEXIcontent → Champs** et [créez un champ](./create-a-field.md) de type `My Field`.
6. Associez-le à un type de contenu, puis placez-le dans le formulaire et dans une position de modèle de contenu/catégorie.
7. Testez l’enregistrement, l’affichage en frontend et les options de recherche/filtre que vous avez implémentées.

:::caution
Ne modifiez jamais directement `plugins/flexicontent_fields/text/` ni un autre plugin fourni. Une mise à jour de FLEXIcontent écrase les fichiers du cœur. Conservez votre type dans son propre dossier et versionnez-le comme un paquet installable distinct.
:::

## CSS, JavaScript et surcharges

Chargez les ressources depuis la méthode du plugin ou du layout avec le Web Asset Manager du document :

```php
$wa = $document->getWebAssetManager();
$wa->registerAndUseScript(
    'plg.flexicontent_fields.myfield.form',
    \Joomla\CMS\Uri\Uri::root(true) . '/plugins/flexicontent_fields/myfield/js/form.js',
    array('version' => 'auto')
);
```

Déclarez `js/`, `css/` ou tout autre dossier dans `<files>`, sinon ils ne seront pas installés. Pour personnaliser plus tard uniquement le HTML d’un type personnalisé, placez un layout dans `templates/<template>/html/flexicontent_fields/myfield/field_mylayout.php` ou `value_mylayout.php` ; ces surcharges priment sur les fichiers `tmpl/` du plugin.

## Recherche et filtrage

Les indicateurs de capacité de recherche/filtre sont détectés en vérifiant les méthodes présentes sur la classe du plugin. Si vous omettez `onIndexSearch()` et `onIndexAdvSearch()`, les options correspondantes sont désactivées dans l’éditeur de champ.

Les implémentations les plus simples délèguent aux helpers de FLEXIcontent :

```php
public function onIndexSearch(&$field, &$post, &$item)
{
    if (!in_array($field->field_type, static::$field_types)) return;
    if (!$field->issearch) return;

    FlexicontentFields::onIndexSearch($field, $post, $item, array(), array(), ' ', 'strip_tags');
    return true;
}

public function onIndexAdvSearch(&$field, &$post, &$item)
{
    if (!in_array($field->field_type, static::$field_types)) return;
    if (!$field->isadvsearch && !$field->isadvfilter) return;

    FlexicontentFields::onIndexAdvSearch($field, $post, $item, array(), array(), ' ', 'strip_tags');
    return true;
}
```

Pour des choix prédéfinis nécessitant un filtrage indexé correct, partez de `select` ou `radio`, qui étendent `FCIndexedField` et gèrent les colonnes de valeurs indexées. Reconstruisez l’index de recherche après avoir modifié la logique d’indexation.

## Dépannage

| Problème | Cause probable |
| --- | --- |
| Type absent du sélecteur | Plugin non installé ou non activé, mauvais dossier/groupe, ou XML manquant. Vérifiez `#__extensions`. |
| `cann't find field type` / `seems to have been uninstalled` | Le fichier principal n’est pas à `<element>/<element>.php`. |
| `Could not find class: plgFlexicontent_fieldsMyfield` | Casse ou préfixe du nom de classe incorrect. |
| `Error field XML file for field type ... was not found` | `<element>.xml` est absent du dossier du plugin. |
| Onglet des réglages spécifiques vide | Le fieldset n’est pas nommé `group-myfield-*`, ou le XML utilise `name="params"` au lieu de `name="attribs"`. |
| Chaînes `FLEXI_FIELD_...` affichées littéralement | Nom de fichier de langue ou clé incorrect. |
| Aucun champ dans le formulaire | `tmpl/field_default.php` absent, `formlayout` incorrect, ou nom de champ non conforme à `custom[<name>][<n>]`. |
| Aucun affichage en frontend | `tmpl/value_default.php` absent, `viewlayout` incorrect, ou `$field->{$prop}` jamais rempli. |
| Options de recherche/filtre désactivées | Méthodes d’indexation/filtrage absentes de la classe. |
| Valeurs non enregistrées | Nom du champ incorrect, valeur vide, ou `onBeforeSaveField()` a retourné `false`. |
| Valeurs sérialisées affichées en texte | La valeur stockée est un tableau/objet ; utilisez `parseValues()` / `unserialize_array()`. |
| Layout ou paramètres obsolètes | Les chemins de layout et les paramètres sont mis en cache ; videz le cache Joomla. |

## Références officielles

- [Comment dupliquer un champ FLEXIcontent pour créer un nouveau type de champ](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/245-how-to-duplicate-a-flexicontent-field-to-create-a-new-field-type.html)
- [Méthodes API des champs FLEXIcontent](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/301-api-methods-of-flexicontent-fields.html)
- [Index de l’API développeur / plugins de champs](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins.html)
- [Utiliser la valeur brute d’un champ dans un modèle ou dans un nouveau type de champ personnalisé](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/312-using-the-raw-value-of-a-field-inside-a-template-file-or-inside-a-new-custom-field-type.html)
- [Code source FLEXIcontent](https://github.com/FLEXIcontent/flexicontent-cck)
