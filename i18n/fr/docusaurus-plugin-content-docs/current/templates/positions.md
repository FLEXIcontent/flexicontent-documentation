---
title: Positions de champs et glisser-déposer
sidebar_position: 4
---

# Positions de champs et glisser-déposer

Les modèles FLEXIcontent exposent des **positions de champs**. Dans l’éditeur de modèle de l’administration, les champs core et personnalisés peuvent être glissés dans ces positions. L’ordre enregistré est ensuite affiché par le modèle.

:::info Source
Basé sur FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`) : `admin/views/template/tmpl/default.php`, `admin/views/template/view.html.php`, `admin/assets/js/layout_editor.js`, `admin/controllers/templates.php`, `admin/models/template.php`, `site/classes/helpers/tmpl.php` et `site/classes/flexicontent.fields.php`.
:::

:::caution Les positions de champs ne sont pas des positions de modules Joomla
Ce mécanisme assigne des **champs** FLEXIcontent à des emplacements du modèle. Les positions de modules Joomla sont un concept distinct. Voir [Positions de modules](#positions-de-modules) ci-dessous.
:::

## 1. Déclarer une position dans le XML

Ouvrez `item.xml`, `category.xml` ou les deux, puis ajoutez un `<group>` dans `<fieldgroups>`.

```xml
<fieldgroups>
    <group>myposition</group>
    <group title="My Position" tcolor="darkcyan">another_position</group>
    <group posrow="image" tcolor="#3A2459" title="Image">image</group>
    <group tcolor="gray" readonly="true">subcategory_title</group>
    <group tcolor="darkgray" title="Render only, no display">renderonly</group>
</fieldgroups>
```

| Attribut | Effet |
| --- | --- |
| (contenu texte) | Nom technique de la position. Utilisez-le dans la boucle PHP. |
| `title` | Libellé lisible dans l’éditeur de modèle. |
| `tcolor` | Couleur de fond dans l’éditeur. |
| `posrow` | Regroupe les positions en ligne/colonne dans l’éditeur. |
| `readonly` | Affiche un message et désactive le glisser-déposer pour la position. |

L’éditeur demande de placer la nouvelle position dans `<fieldgroups>` et de retenir son nom pour `item.php` ou `category_items.php`. Utilisez un nom simple : pas d’espace ni de caractère accentué.

`renderonly` est une convention, pas un mode de rendu spécial. Les champs qui y sont assignés sont rendus dans `$item->fields` mais ne sont pas affichés automatiquement. Voir [Champs render-only](#champs-render-only).

## 2. Ajouter la boucle PHP correspondante

Pour `item.php` :

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

Pour `category_items.php`, la même boucle se place dans la boucle des contenus :

```php
<?php foreach ($this->items as $item) : ?>
    <?php if (isset($item->positions['myposition'])) : ?>
        <?php foreach ($item->positions['myposition'] as $field) : ?>
            <div class="flexi value field_<?php echo $field->name; ?>">
                <?php echo $field->display; ?>
            </div>
        <?php endforeach; ?>
    <?php endif; ?>
<?php endforeach; ?>
```

Le nom XML et `$_position_name` doivent correspondre exactement. Voir [Boucles de contenus et rendu des champs](./loops-fields.md) pour la boucle complète et la forme de `$item->positions`.

## 3. Assigner les champs dans l’éditeur de modèle

Dans l’administration, ouvrez la configuration du modèle et l’onglet **Field's placement**. L’éditeur construit trois types de listes triables :

```text
#sortablecorefields      champs core disponibles
#sortableuserfields      champs personnalisés disponibles
#sortable-myposition     champs actuellement assignés à "myposition"
```

Chaque champ est un élément de liste avec un identifiant tel que `field_myfield`. Les champs personnalisés sont affichés avec leur identifiant, par exemple `City #47`.

L’éditeur stocke l’ordre dans des champs cachés : un par position et un champ global `positions` au format CSV. Le JavaScript de `admin/assets/js/layout_editor.js` utilise Sortable :

```js
Sortable.create(list, {
    group: 'flexicontent-layout-fields',
    draggable: 'li[id^="field_"]',
    onEnd(event) {
        storeOrder(event.from);
        if (event.to !== event.from) storeOrder(event.to);
    }
});
```

`storeOrder()` écrit les noms de champs séparés par des virgules, par exemple `image,introtext,city`.

## 4. Enregistrer le modèle

Le contrôleur lit l’entrée `positions` et appelle le modèle :

```php
$positions = $this->input->getString('positions', '');
$positions = explode(',', $positions);
$model->setConfig($positions, $attribs);
$model->store($post);
```

Le modèle stocke ensuite les positions des champs, les paramètres de mise en page, les variables LESS générées et actualise le cache des modèles :

```php
$this->storeFieldPositions($this->_folder, $this->_cfgname, $this->_type, $this->_config['positions'], $data);
$this->storeLayoutConf($this->_folder, $this->_cfgname, $this->_type, $this->_config['attribs']);
$this->check_less_files($this->_folder);
$this->storeLessConf($this->_folder, $this->_cfgname, $this->_type, $this->_config['attribs']);
flexicontent_tmpl::getTemplates($this->_folder, false);
```

:::warning
Après avoir modifié directement le XML ou le PHP sur le serveur, enregistrez à nouveau le modèle dans l’administration. Sinon les assignations de la nouvelle balise `<group>` ne sont pas stockées et la définition en cache du modèle peut rester inchangée. Videz le cache Joomla si nécessaire.
:::

## Stockage des positions

Les positions sont enregistrées par modèle, configuration de mise en page (`cfgname`) et vue dans `#__flexicontent_templates` :

```sql
CREATE TABLE IF NOT EXISTS `#__flexicontent_templates` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `template` varchar(50) NOT NULL default '',
  `cfgname` varchar(50) NOT NULL default '',
  `layout` varchar(20) NOT NULL default '',
  `position` varchar(100) NOT NULL default '',
  `fields` text NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `configuration` (`template`,`cfgname`,`layout`,`position`)
);
```

La colonne `fields` contient les noms de champs séparés par des virgules. Côté frontend, `flexicontent_tmpl::getFieldsByPositions()` charge les lignes du modèle et de la mise en page actifs, en convertissant le nom de vue `item` en clé interne `items`.

Au rendu, `FlexicontentFields::renderPositions()` remplit chaque position :

```php
$item->positions['position_name']->{$field_name}->id;
$item->positions['position_name']->{$field_name}->name;
$item->positions['position_name']->{$field_name}->label;
$item->positions['position_name']->{$field_name}->display;
```

Les champs dont le rendu est vide sont ignorés.

## Champs render-only

Utilisez `renderonly` lorsqu’un champ doit être affiché manuellement, par exemple deux fois dans un même modèle ou dans une autre structure HTML :

```xml
<fieldgroups>
    <group tcolor="darkgray" title="Render only, no display">renderonly</group>
</fieldgroups>
```

```php
<?php echo $item->fields["fieldname"]->display; ?>
```

L’éditeur de modèle joint cette note à l’extrait :

> You need to add this field to the renderonly position, in the "Field's placement" TAB

Certains plugins de champ génèrent des identifiants HTML. Afficher plusieurs fois le même champ peut donc produire des identifiants dupliqués invalides.

## Positions de modules

Les positions de modules Joomla sont gérées par Joomla, pas par `item.xml` ni `category.xml`. Le champ `fcloadmodule` expose une liste des positions de modules publiques du site via `type="fcpositions"` :

```xml
<field
    name="position"
    type="fcpositions"
    default=""
    label="FLEXI_FIELD_MODULE_POSITIONS_LIST"
    description="FLEXI_FIELD_MODULE_POSITIONS_LIST_DESC"
/>
```

Cet élément de formulaire interroge `#__modules` pour obtenir les positions distinctes publiées avec `client_id = 0`. Il n’existe pas de définition de glisser-déposer pour les modules Joomla dans un manifeste de modèle FLEXIcontent.

## Checklist des positions

1. Copiez un modèle fourni avant de le modifier.
2. Ajoutez le `<group>` dans `item.xml`, `category.xml` ou les deux.
3. Ajoutez la boucle PHP avec le nom identique.
4. Enregistrez le modèle pour mettre à jour `#__flexicontent_templates`.
5. Glissez les champs core/personnalisés dans la position dans l’éditeur de modèle.
6. Enregistrez à nouveau après avoir changé l’ordre d’assignation.
7. Vérifiez le frontend avec le paramètre `ilayout` ou `clayout` concerné.
8. Pour un affichage manuel, assignez le champ à `renderonly` et affichez `$item->fields['name']->display`.

## Références officielles

- [Ajouter une position dans la vue contenu](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/661-adding-position-in-item-view.html)
- [Créer une position de champ supplémentaire dans un modèle personnalisé](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/255-creating-an-extra-field-position-in-a-custom-template.html)
- [Afficher un champ à plusieurs endroits](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/635-how-to-display-a-field-in-multiple-places.html)
- [Modifier les paramètres des modèles](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/305-editing-template-parameters-to-customize-template-appearance.html)
- [Source : éditeur de modèle](https://github.com/FLEXIcontent/flexicontent-cck/blob/master/admin/views/template/tmpl/default.php)
