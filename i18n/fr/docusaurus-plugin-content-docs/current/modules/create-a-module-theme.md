---
title: Créer un thème de module
sidebar_position: 2
---

# Créer un thème de module

Dans FLEXIcontent, un **thème** de module s’appelle un **layout**. Il s’agit d’un fichier PHP, éventuellement accompagné d’un fichier XML de paramètres, de CSS et de fragments d’en-tête/pied de page. Le paramètre du module `layout` détermine celui qui est utilisé.

Ce guide présente la méthode sûre lors des mises à jour : placer le layout personnalisé dans le template Joomla actif. Elle s’applique à tous les modules FLEXIcontent ; les exemples utilisent `mod_flexicontent`.

:::info Source
Basé sur FLEXIcontent 5.3 (`master`, commit `5bc85a46712b32fae5845a134d48083f71a55419`), notamment `modules/mod_flexicontent/mod_flexicontent.xml`, `modules/mod_flexicontent/mod_flexicontent.php`, `modules/mod_flexicontent/helper.php`, `admin/elements/fclayout.php` et `admin/controllers/templates.raw.php`.
:::

## Terminologie

| Ce que vous personnalisez | Mécanisme | Documentation |
| --- | --- | --- |
| Sortie d’un module | Paramètre `layout`, `modules/<module>/tmpl/<layout>.php` ou surcharge Joomla | Cette page |
| Page contenu ou catégorie entière | Modèles de contenu FLEXIcontent | [Structure des modèles](../templates/structure.md) |
| Affichage d’un seul champ | Layouts de champ | [Créer un layout de champ](../fields/field-layouts.md) |
| HTML autour d’un module | Module chrome Joomla, `modChrome_*` dans `templates/<template>/html/modules.php` | Documentation Joomla |

Un thème de module ne remplace **pas** le modèle de contenu : les valeurs des champs sont déjà calculées dans `$item->fields[...]->display` avant que le layout du module ne les affiche.

## Avant de commencer

- Installez et activez le module FLEXIcontent à personnaliser.
- Identifiez le style de template Joomla réellement utilisé sur les pages où le module apparaît.
- Utilisez FTP, un gestionnaire de fichiers ou votre outil de déploiement : le layout est un fichier, pas une option du gestionnaire de modules.
- Ne modifiez jamais directement les fichiers fournis dans `modules/<module>/tmpl/`. Une mise à jour de FLEXIcontent peut les écraser.

## Comment le sélecteur trouve les layouts

Dans le gestionnaire de modules, ouvrez le module puis allez dans **Basique → Template du module → Template** (`layout`). Le champ est défini avec `type="fclayout"` et, pour `mod_flexicontent`, analyse :

```xml
<field
    name="layout"
    type="fclayout"
    default="news"
    label="FLEXI_CHOOSE_TMPL"
    directory="/modules/mod_flexicontent/tmpl"
    ext_name="mod_flexicontent"
    hide_default="1"
    hide_none="1"
    stripext="1"
    filter="\.php$"
    exclude="^_"
    params_source="file"
/>
```

Le sélecteur liste les fichiers `.php` directs du répertoire configuré. Les fichiers dont le nom commence par `_` sont ignorés. Il analyse aussi les templates Joomla activés pour trouver :

```text
templates/<active_template>/html/<module>/<layout>.php
```

Une surcharge portant le même nom qu’un layout intégré est appliquée automatiquement et est désactivée dans le sélecteur. Pour forcer un template précis, utilisez la valeur `template:layout`, par exemple `my_template:mynews`.

Un fichier `.xml` du même nom fournit les paramètres du layout. Le libellé du sélecteur peut être traduit avec `TPL_<template>_<module>_LAYOUT_<name>` dans le fichier de langue du template.

## Emplacements des fichiers

Pour `mod_flexicontent` :

| Rôle | Emplacement d’origine | Surcharge sûre |
| --- | --- | --- |
| Layout PHP | `modules/mod_flexicontent/tmpl/news.php` | `templates/<template>/html/mod_flexicontent/mynews.php` |
| Paramètres du layout | `modules/mod_flexicontent/tmpl/news.xml` | `templates/<template>/html/mod_flexicontent/mynews.xml` |
| CSS du layout | `modules/mod_flexicontent/tmpl/news/news.css` | `templates/<template>/html/mod_flexicontent/mynews/mynews.css` |
| Fragment d’en-tête | `modules/mod_flexicontent/tmpl/news/header.php` | `templates/<template>/html/mod_flexicontent/mynews/header.php` |
| Fragment de pied de page | `modules/mod_flexicontent/tmpl/news/footer.php` | `templates/<template>/html/mod_flexicontent/mynews/footer.php` |

Remplacez le nom du module pour les autres : `mod_flexicategories`, `mod_flexifilter`, `mod_flexiadvsearch`, `mod_flexigooglemap`, `mod_flexitagcloud`.

:::caution
Le chemin de surcharge ne contient **pas** de segment `/tmpl/` après `html/<module>/`. Certains anciens fichiers README locaux indiquent `html/mod_flexicontent/tmpl/news.php` ; ne suivez pas ce modèle. `ModuleHelper::getLayoutPath()` de Joomla et le sélecteur FLEXIcontent utilisent `html/mod_flexicontent/news.php`.
:::

Les layouts intégrés de `mod_flexicontent` sont `default.php`, `news.php`, `select.php`, `carousel.php` et `swiper.php`. Les fragments partagés se trouvent dans `modules/mod_flexicontent/tmpl_common/`.

## Procédure : créer un thème par surcharge

### 1. Copier un layout de base

Choisissez le layout intégré le plus proche du résultat souhaité :

```text
modules/mod_flexicontent/tmpl/default.php  → liste simple de titres
modules/mod_flexicontent/tmpl/news.php     → images, dates, champs, onglets, votes, commentaires
modules/mod_flexicontent/tmpl/select.php   → liste déroulante
modules/mod_flexicontent/tmpl/carousel.php → carrousel
modules/mod_flexicontent/tmpl/swiper.php   → carrousel Swiper
```

Copiez le fichier PHP, son fichier XML et son dossier CSS dans le template Joomla :

```text
templates/my_template/html/mod_flexicontent/mynews.php
templates/my_template/html/mod_flexicontent/mynews.xml
templates/my_template/html/mod_flexicontent/mynews/mynews.css
```

Utilisez un nom unique (`mynews`, pas `news`) pour que la surcharge apparaisse clairement dans le sélecteur.

### 2. Renommer les classes CSS et les paramètres

Si vous avez copié `news.php`, renommez sa classe CSS et ses préfixes de paramètres :

```php
class="news mod_flexicontent_wrapper"   → class="mynews mod_flexicontent_wrapper"
```

```xml
name="news_params_layout"               → name="mynews_params_layout"
name="news_item_placement_*"            → name="mynews_item_placement_*"
```

Dans le CSS, remplacez le sélecteur `.news` par `.mynews`. Préfixez les identifiants avec `$module->id` et, pour un affichage par catégorie, avec l’identifiant de catégorie.

### 3. Vérifier le contrat PHP

Partez du fichier copié : les variables diffèrent selon les modules et les layouts. Pour `mod_flexicontent`, le contexte principal contient `$params`, `$module`, `$moduleclass_sfx`, `$layout`, `$ordering`, `$list`, `$list_totals`, `$catdata`, `$catdata_arr`, `$count`, `$featured` et `$wa`.

Une structure minimale ressemble à ceci :

```php
<?php
defined('_JEXEC') or die('Restricted access');

// $list est un tableau de groupes de tri, chacun avec des contenus 'featured' et 'standard'.
?>
<div class="mynews mod_flexicontent_wrapper mod_flexicontent_wrap<?php echo $moduleclass_sfx; ?>"
     id="mod_flexicontent_<?php echo $layout . '_' . $module->id; ?>">

    <?php foreach ($ordering as $ord) : ?>
        <?php if (!isset($list[$ord])) continue; ?>

        <div class="order_group" id="order_<?php echo $ord . $module->id; ?>">
            <?php if (!empty($ordering_addtitle) && isset($ordering[$ord])) : ?>
                <h4><?php echo htmlspecialchars($ordering[$ord], ENT_QUOTES, 'UTF-8'); ?></h4>
            <?php endif; ?>

            <?php foreach (array('featured', 'standard') as $group) : ?>
                <?php if (empty($list[$ord][$group])) continue; ?>

                <ul class="mod_flexicontent mod_flexicontent_<?php echo $group; ?>">
                    <?php foreach ($list[$ord][$group] as $item) : ?>
                        <li class="<?php echo !empty($item->is_active_item) ? 'fcitem_active' : ''; ?>">
                            <a href="<?php echo htmlspecialchars($item->link, ENT_QUOTES, 'UTF-8'); ?>">
                                <?php echo htmlspecialchars($item->title, ENT_QUOTES, 'UTF-8'); ?>
                            </a>

                            <?php if (!empty($item->fields)) : ?>
                                <?php foreach ($item->fields as $name => $field) : ?>
                                    <div class="mynews_field mynews_field_<?php echo $name; ?>">
                                        <span class="mynews_label">
                                            <?php echo htmlspecialchars($field->label, ENT_QUOTES, 'UTF-8'); ?>
                                        </span>
                                        <span class="mynews_value"><?php echo $field->display; ?></span>
                                    </div>
                                <?php endforeach; ?>
                            <?php endif; ?>
                        </li>
                    <?php endforeach; ?>
                </ul>
            <?php endforeach; ?>
        </div>
    <?php endforeach; ?>
</div>
```

`$field->display` est déjà rendu et filtré selon les droits d’accès par FLEXIcontent. Ne réinterrogez pas les valeurs brutes des champs dans le layout sans connaître les implications ACL.

Les propriétés courantes d’un contenu sont `id`, `title`, `fulltitle`, `alias`, `link`, `text`, `image`, `image_rendered`, `date_created`, `date_modified`, `hits_rendered`, `voting`, `comments_rendered`, `fields`, `catid`, `itemcats`, `typename`, `access` et `featured`.

Utilisez `Text::_('CLE')` pour les chaînes traduisibles. Les fragments partagés peuvent être inclus depuis leur chemin absolu :

```php
include(JPATH_SITE . '/modules/mod_flexicontent/tmpl_common/category.php');
include(JPATH_SITE . '/modules/mod_flexicontent/tmpl_common/favlist.php');
include(JPATH_SITE . '/modules/mod_flexicontent/tmpl_common/readon.php');
```

### 4. Ajouter les paramètres du layout

Créez `mynews.xml` à côté de `mynews.php` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<form>
    <name>mod_flexicontent - mynews Layout</name>
    <version>1.0</version>
    <description>Paramètres du thème de module mynews</description>

    <fields name="params">
        <fieldset name="layout" addfieldpath="/administrator/components/com_flexicontent/elements">
            <field
                name="mynews_columns"
                type="list"
                default="2"
                label="Colonnes"
            >
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </field>
        </fieldset>
    </fields>
</form>
```

Lisez la valeur dans le layout avec :

```php
$columns = (int) $params->get('mynews_columns', 2);
```

La structure XML doit être `<fields name="params">` contenant `<fieldset name="layout">`. Si aucun XML n’est trouvé, FLEXIcontent utilise `tmpl/_fallback/_fallback.xml`, qui expose les paramètres génériques `custom1` à `custom5`.

:::note
Les paramètres du layout sont enregistrés via l’événement Joomla `onExtensionBeforeSave`. Certains gestionnaires de modules tiers peuvent ne pas les conserver.
:::

### 5. Enregistrer le CSS dans la surcharge

Le chargement automatique du CSS par le composant ne vérifie que `modules/<module>/tmpl/<layout>/<layout>.css`. Pour une surcharge, enregistrez explicitement la feuille de style :

```php
$wa = $app->getWebAssetManager();
$wa->registerAndUseStyle(
    'mod_flexicontent.mynews',
    'templates/' . $app->getTemplate() . '/html/mod_flexicontent/mynews/mynews.css',
    array('version' => FLEXI_VHASH)
);
```

Si la sortie du module est capturée par une autre extension et que le CSS n’est pas injecté dans `<head>`, réglez l’option du module **Ajouter le CSS** (`add_ccs`) sur `2` pour intégrer la balise `<link>` directement dans le HTML du module.

### 6. Sélectionner le thème dans le module

1. Allez dans **Extensions → Modules** et ouvrez le module FLEXIcontent.
2. Dans l’onglet **Basique**, sous **Template du module**, choisissez le nouveau layout.
3. Si vous avez forcé un template précis, sélectionnez `my_template:mynews` ; sinon choisissez l’entrée simple `mynews`.
4. Enregistrez le module.
5. Videz le cache Joomla et rechargez la page si le layout ou ses paramètres n’apparaissent pas.

## Autre méthode : ajouter un layout dans le dossier du module

Vous pouvez dupliquer les fichiers directement sous `modules/mod_flexicontent/tmpl/` :

```text
modules/mod_flexicontent/tmpl/mynews.php
modules/mod_flexicontent/tmpl/mynews.xml
modules/mod_flexicontent/tmpl/mynews/mynews.css
```

C’est plus simple, mais **non sûr lors des mises à jour**. Préférez la surcharge dans le template Joomla, sauf si vous développez le layout dans un paquet personnalisé versionné.

## Fragments d’en-tête et de pied de page

Certains layouts fournis utilisent des fichiers optionnels `header.php` et `footer.php`. Le code principal du module les capture avec une mise en mémoire tampon et ne les affiche que pour les layouts qui déclarent ces fragments. Pour un thème neuf, placez tout le balisage dans le layout principal, sauf si vous copiez volontairement la structure correspondante du composant.

## Chaînes de langue

Pour donner un libellé lisible au sélecteur, ajoutez une clé dans le fichier de langue du template actif :

```ini
TPL_MY_TEMPLATE_MOD_FLEXICONTENT_LAYOUT_MYNEWS="Mon thème actualités"
```

Motif : `TPL_<template>_<module>_LAYOUT_<name>`. Sans cette clé, le sélecteur affiche le nom brut du fichier.

## Cache et règles d’affichage

- Le module prend en charge le cache Joomla (`cache`, `cache_time`). Videz le cache après avoir modifié les fichiers ou les paramètres du layout.
- **Afficher dans les vues**, **Afficher pour les clients**, **Activer la règle PHP** et **Code de la règle PHP** sont évalués avant l’inclusion du layout. Un thème ne peut pas afficher un module masqué par ces règles.
- La détection du client est ignorée lorsque le cache Joomla est actif, sauf si la mise en cache par plateforme est configurée.
- Il n’y a pas de pagination dans le layout du module. Utilisez `count`, `count_feat` et `offset_items`.
- Les groupes de tri proviennent de `$ordering` ; `$ordering_addtitle` contrôle les titres de groupe.
- Avec **Appliquer la configuration par catégorie**, le layout est inclus une fois par catégorie. `$catdata`, `$list`, `$list_totals` et `$items_exist` sont alors disponibles.

## Dépannage

| Problème | Cause probable |
| --- | --- |
| Layout absent du sélecteur | Le fichier PHP doit être un `.php` direct du répertoire des layouts, ne pas commencer par `_`, et le style de template Joomla doit être activé. Videz le cache. |
| Surcharge non utilisée | Mauvais chemin : utilisez `templates/<template>/html/<module>/<layout>.php`, sans segment `/tmpl/`. Utilisez `template:layout` pour forcer un template. |
| Onglet des paramètres vide | Le nom XML doit correspondre au nom PHP et utiliser `<fields name="params"><fieldset name="layout">`. |
| CSS non appliqué | Enregistrez la feuille de style dans la surcharge ; le chargement automatique ne vérifie que le dossier du module. Essayez `add_ccs=2` si la sortie est capturée. |
| En-tête/pied de page ignorés | Le layout doit déclarer la structure correspondante des fichiers `header.php` / `footer.php`. |
| Identifiants DOM ou JavaScript dupliqués | Préfixez les classes et incluez `$module->id` ainsi que l’identifiant de catégorie dans les identifiants générés. |
| Paramètres non enregistrés | Le gestionnaire de modules doit déclencher `onExtensionBeforeSave`. |

## Références officielles

- [Créer un layout personnalisé pour le module Universal Content et les autres modules FLEXIcontent](https://www.flexicontent.org/documentation/tutorials-english/69-templating-module-plugin-content/274-how-to-create-a-custom-layout-for-universal-content-module-and-other-flexicontent-modules.html)
- [Tutoriels en anglais](https://flexicontent.org/documentation/tutorials-english.html)
- [Notes de documentation officielles](https://flexicontent.org/_documentation_notes/)
- [Code source FLEXIcontent](https://github.com/FLEXIcontent/flexicontent-cck)
