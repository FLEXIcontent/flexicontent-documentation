---
title: Boucles de contenus et rendu des champs
sidebar_position: 3
---

# Boucles de contenus et rendu des champs

Les vues FLEXIcontent lient les champs personnalisés aux contenus et rendent les positions configurées avant l’exécution du modèle. Un modèle lit normalement les valeurs préparées au lieu d’interroger les champs lui-même.

:::info Source
Les exemples et les signatures proviennent de FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), principalement `site/classes/flexicontent.fields.php`, `site/views/category/view.html.php`, `admin/views/item/view.html.php` et les fichiers `site/templates/*/category_items.php` fournis.
:::

## API centrale : `FlexicontentFields`

Définie dans `site/classes/flexicontent.fields.php`.

```php
FlexicontentFields::renderFields(
    $item_per_field = true,
    $item_ids = array(),
    $field_names = array(),
    $view = FLEXI_ITEMVIEW,
    $methods = array(),
    $cfparams = array()
);

FlexicontentFields::getFields(
    &$_items,
    $view = FLEXI_ITEMVIEW,
    $params = null,
    $aid = false,
    $use_tmpl = true,
    $reuse_loaded = false
);

FlexicontentFields::getFieldDisplay(
    &$item_arr,
    $fieldname,
    $single_item_vals = null,
    $method = 'display',
    $view = FLEXI_ITEMVIEW,
    $reload_field_params = true,
    $options = null
);

FlexicontentFields::renderField(
    &$_item,
    &$_field,
    &$values,
    $method = 'display',
    $view = FLEXI_ITEMVIEW,
    $skip_trigger_plgs = false,
    $event_row = false,
    $reload_field_params = true
);

FlexicontentFields::renderPositions(
    &$items,
    $view = FLEXI_ITEMVIEW,
    $params = null,
    $use_tmpl = true,
    & $_rendered = array()
);
```

`getFields()` charge les valeurs des champs et, lorsque `$params` est fourni, appelle `renderPositions()`. Passer `null` comme paramètres ne récupère que les valeurs sans rien afficher.

## Ce qui est déjà disponible dans chaque vue

### Vue catégorie

Avant l’exécution de `category_items.php`, la vue catégorie appelle :

```php
$items = FlexicontentFields::getFields($items, 'category', $params, $aid);
```

Le modèle reçoit ces contenus dans `$this->items`. Chaque contenu possède :

| Propriété | Contenu |
| --- | --- |
| `$item->fields['name']->display` | HTML rendu du champ. |
| `$item->fields['name']->label` | Libellé selon les paramètres du champ. |
| `$item->positions['position']` | Objet des champs assignés à une position du modèle. |
| `$item->onDemandFields` | Champs rendus à la demande. |

### Vue contenu

La vue contenu appelle :

```php
$_items = array(&$item);
FlexicontentFields::getFields($_items, FLEXI_ITEMVIEW, $params, $aid);
```

`item.php` peut donc utiliser directement `$item->fields` et `$item->positions`.

## Boucle de contenus de catégorie : référence canonique

Un `category_items.php` minimal conserve le formulaire de filtres, la boucle des contenus et une boucle de position. Ce motif reprend celui des modèles fournis.

```php
<?php
defined('_JEXEC') or die;

// Recherche textuelle, filtres de champs, index alpha, pagination et tri.
ob_start();
file_exists(dirname(__FILE__).DS.'listings_filter_form.php')
    ? include(dirname(__FILE__).DS.'listings_filter_form.php')
    : include(JPATH_SITE.DS.'components'.DS.'com_flexicontent'.DS.'tmpl_common'.DS.'listings_filter_form.php');

$filter_form_html = trim(ob_get_contents());
ob_end_clean();

if ($filter_form_html) {
    echo '<div class="fcclear"></div><aside class="group">' . $filter_form_html . '</aside>';
}

if (!$this->items) {
    echo '<div class="fc-mssg fc-info">' . \Joomla\CMS\Language\Text::_('FLEXI_NO_ITEMS_FOUND') . '</div>';
    return;
}

$items = & $this->items;
$count = count($items);
?>

<div class="fc_category_items">
    <?php foreach ($items as $i => $item) : ?>
        <article class="fc_item flexi item_<?php echo (int) $item->id; ?>">

            <?php if (isset($item->positions['image'])) : ?>
                <div class="flexi lineinfo image group">
                    <?php foreach ($item->positions['image'] as $field) : ?>
                        <div class="flexi element field_<?php echo $field->name; ?>">
                            <?php if ($field->label) : ?>
                                <span class="flexi label field_<?php echo $field->name; ?>">
                                    <?php echo $field->label; ?>
                                </span>
                            <?php endif; ?>
                            <div class="flexi value field_<?php echo $field->name; ?>">
                                <?php echo $field->display; ?>
                            </div>
                        </div>
                    <?php endforeach; ?>
                </div>
            <?php endif; ?>

            <h2 class="fc_item_title">
                <a href="<?php echo $item->link; ?>"><?php echo $item->title; ?></a>
            </h2>

            <?php if (isset($item->fields['text'])) : ?>
                <div class="fcitem_text">
                    <?php echo $item->fields['text']->display; ?>
                </div>
            <?php endif; ?>

        </article>
    <?php endforeach; ?>
</div>
```

La forme de l’objet de position est :

```php
$item->positions['position_name']->{$field_name}->id;
$item->positions['position_name']->{$field_name}->name;
$item->positions['position_name']->{$field_name}->label;
$item->positions['position_name']->{$field_name}->display;
```

`foreach ($item->positions['image'] as $field)` parcourt cet objet : `$field->name`, `$field->label` et `$field->display` sont toujours disponibles.

## Rendu d’un champ pour toute la liste

Le modèle `grid` fourni rend le champ `text` pour tous les contenus en un seul appel avant la boucle :

```php
FlexicontentFields::getFieldDisplay($items, 'text', null, 'display', 'category');
```

La boucle ne fait ensuite que lire la valeur préparée :

```php
$desc_text = $this->params->get('lead_strip_html', 1)
    ? flexicontent_html::striptagsandcut($item->fields['text']->display, $lead_cut_text, $uncut_length)
    : $item->fields['text']->display;

echo strlen($desc_text) ? '<p>' . $desc_text . '</p>' : '';
```

Cela évite de rendre le même champ une fois par contenu. Appelez `getFieldDisplay()` avant `foreach ($items as $item)`, pas à l’intérieur.

## Rendu d’un champ à la demande

`getFieldDisplay()` renvoie une chaîne pour un seul contenu et un tableau indexé par identifiant de contenu pour un tableau de contenus. Il remplit aussi `$item->fields` et `$item->onDemandFields`.

```php
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname');
echo $html;
```

Les méthodes d’affichage disponibles dépendent du plugin de champ :

```php
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display_small', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display_medium', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display_large', 'item');
$html = FlexicontentFields::getFieldDisplay($item, 'fieldname', null, 'display_original', 'item');
```

Une lecture directe telle que `echo $item->fields['fieldname']->display;` suppose que le champ ait déjà été rendu. Placez-le dans une position visible, dans `renderonly`, ou rendez-le explicitement comme ci-dessus. Voir [Positions de champs et glisser-déposer](./positions.md). Pour modifier le HTML produit par le champ lui-même, créez un [layout de champ](../fields/field-layouts.md).

## Modèle contenu : boucle de position

L’éditeur de modèle génère ce squelette lorsqu’une nouvelle position est ajoutée. Il fonctionne dans `item.php` (ou `item_html5.php`).

```php
<!-- BOF myposition block -->
<?php $_position_name = "myposition"; ?>

<?php if (isset($item->positions[$_position_name])) : ?>
<div class="flexi lineinfo <?php echo $_position_name; ?> group">

    <?php foreach ($item->positions[$_position_name] as $field) : ?>
    <div class="flexi element field_<?php echo $field->name; ?>">

        <?php if ($field->label) : ?>
            <span class="flexi label field_<?php echo $field->name; ?>">
                <?php echo $field->label; ?>
            </span>
        <?php endif; ?>

        <div class="flexi value field_<?php echo $field->name; ?>">
            <?php echo $field->display; ?>
        </div>

    </div>
    <?php endforeach; ?>

</div>
<?php endif; ?>
<!-- EOF myposition block -->
```

Le fichier `modular.php` fourni utilise la même structure pour les positions `subtitle1`, `subtitle2`, `subtitle3`, `subtitle_tab1` à `subtitle_tab12`, `image`, `top`, `description`, `bottom_tab1` à `bottom_tab12` et `bottom`.

Les positions dynamiques sont adressées par leur nom :

```php
$tabpos_name  = 'subtitle_tab'.$tc;
$tabpos_label = \Joomla\CMS\Language\Text::_($this->params->get('subtitle_tab'.$tc.'_label', $tabpos_name));

if (isset($item->positions[$tabpos_name])) : ?>
    <?php foreach ($item->positions[$tabpos_name] as $field) : ?>
        <?php echo $field->display; ?>
    <?php endforeach; ?>
<?php endif; ?>
```

## Erreurs courantes

| Symptôme | Cause |
| --- | --- |
| `$item->fields['name']` n’existe pas | Le champ n’a pas été rendu. Ajoutez-le à une position ou appelez `getFieldDisplay()`. |
| Une boucle de position n’affiche rien | Le nom PHP ne correspond pas exactement au nom du `<group>` XML, ou aucun champ n’a été assigné dans l’éditeur de modèle. |
| Les valeurs diffèrent entre la vue catégorie et la vue contenu | Une méthode comme `display_small` n’est utilisée que dans une vue, ou un paramètre de vue remplace le champ. |
| Pages catégorie lentes | `getFieldDisplay()` ou `renderField()` appelé dans la boucle des contenus. Déplacez l’appel avant la boucle. |

## Références officielles

- [Template FLEXIcontent — partie 4 : le modèle de contenu](https://www.flexicontent.org/documentation/tutorials-english/84-advanced-tutorials/338-template-flexicontent-part-4-the-contents-template.html)
- [Utilisation de base : afficher les champs dans la vue contenu](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/261-how-to-displat-fields-in-the-frontend-item-view.html)
- [Utilisation de base : afficher les champs dans la vue catégorie](https://www.flexicontent.org/documentation/tutorials-english/75-basic-usage/262-how-to-display-fields-in-the-frontend-category-view.html)
- [Rendu manuel des champs et `renderonly`](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/248-upgrading-custom-templates-to-work-in-v156.html)
- [Afficher un champ à plusieurs endroits](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/635-how-to-display-a-field-in-multiple-places.html)
- [Source : `flexicontent.fields.php`](https://github.com/FLEXIcontent/flexicontent-cck/blob/master/site/classes/flexicontent.fields.php)
