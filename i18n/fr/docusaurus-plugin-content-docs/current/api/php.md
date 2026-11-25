---
title: API PHP pour développeurs
sidebar_position: 5
---

# API PHP pour développeurs

Utilisez l’API PHP lorsque votre code s’exécute **dans Joomla!** : une extension personnalisée, un plugin, un module, un modèle de page ou un script en ligne de commande. Pour un client HTTP externe, utilisez plutôt la [JSON:API](./webservices.md).

Les exemples ci-dessous sont adaptés des tutoriels officiels FLEXIcontent. Considérez-les comme un point de départ et validez-les sur votre version de Joomla!/FLEXIcontent.

## Charger le framework Joomla!

Lorsque le code n’est pas déjà dans une extension Joomla!, initialisez d’abord l’application. Cet exemple suppose que le script se trouve à la racine du site ; ajustez `JPATH_BASE` s’il est dans un sous-dossier.

```php
define('_JEXEC', 1);
define('JPATH_BASE', realpath(__DIR__));
define('DS', DIRECTORY_SEPARATOR);

require_once JPATH_BASE . '/includes/defines.php';
require_once JPATH_BASE . '/includes/framework.php';

$app = Joomla\CMS\Factory::getApplication('site');
$app->initialise();
```

Les anciens exemples officiels utilisent `JFactory::getApplication()`. Avec Joomla! 4-6, préférez `Joomla\CMS\Factory`.

## Charger les classes et les langues de FLEXIcontent

```php
use Joomla\CMS\Factory;
use Joomla\CMS\Log\Log;
use Joomla\CMS\Table\Table;

require_once JPATH_SITE . '/components/com_flexicontent/classes/flexicontent.helper.php';
require_once JPATH_SITE . '/components/com_flexicontent/classes/flexicontent.categories.php';
require_once JPATH_SITE . '/components/com_flexicontent/classes/flexicontent.fields.php';
require_once JPATH_SITE . '/components/com_flexicontent/helpers/permission.php';
require_once JPATH_SITE . '/components/com_flexicontent/helpers/route.php';

Table::addIncludePath(JPATH_ADMINISTRATOR . '/components/com_flexicontent/tables');

$language = Factory::getApplication()->getLanguage();
$language->load('com_content', JPATH_ADMINISTRATOR, 'en-GB', true);
$language->load('com_content', JPATH_ADMINISTRATOR, null, true);
$language->load('com_flexicontent', JPATH_ADMINISTRATOR, 'en-GB', true);
$language->load('com_flexicontent', JPATH_ADMINISTRATOR, null, true);
$language->load('com_content', JPATH_SITE, 'en-GB', true);
$language->load('com_content', JPATH_SITE, null, true);
$language->load('com_flexicontent', JPATH_SITE, 'en-GB', true);
$language->load('com_flexicontent', JPATH_SITE, null, true);
```

## Créer ou modifier un contenu

Le modèle d’élément gère les données principales, les catégories, les étiquettes et les valeurs des champs personnalisés.

```php
use Joomla\CMS\Factory;
use Joomla\CMS\Log\Log;

$modelFile = Factory::getApplication()->isAdmin()
    ? JPATH_ADMINISTRATOR . '/components/com_flexicontent/models/item.php'
    : JPATH_SITE . '/components/com_flexicontent/models/item.php';
require_once $modelFile;

$item_model = new FlexicontentModelItem();
$data = [];

$item_ID = 0; // Use an existing id to update, or 0 to create.

if ($item_ID) {
    $item = $item_model->getItem($item_ID, false, true, 0);
    if (!$item) {
        throw new RuntimeException('Item ' . $item_ID . ' not found');
    }

    // Keep the existing custom field values before saving changes.
    $items = [$item];
    $items_custom_values = FlexicontentFields::getCustomFieldValues($items, 'item');
    $data['custom'] = reset($items_custom_values);
    $data['id'] = $item_ID;
} else {
    $data['id'] = 0;
}

$data['type_id']  = 1;        // Content type id. Do not change it for an existing item.
$data['language'] = 'en-GB';
$data['catid']    = 42;       // Main category id.
$data['cid']      = [55, 117]; // Secondary category ids.
$data['tag']      = [];        // Tag ids.
$data['vstate']   = 2;         // Version approved.
$data['state']    = 1;         // Published.
$data['title']    = 'My item title';
$data['text']     = 'Item description';

// Custom fields, indexed by field name.
$data['custom']['field1']    = 'Single value';
$data['custom']['field2'][0] = 'First value';
$data['custom']['field2'][1] = 'Second value';

if (!$item_model->store($data)) {
    $msg = 'Failed to store item: ' . $item_model->getError();
    Log::add($msg);
    echo $msg . '<br />';
}
```

## Créer ou modifier un type, un champ ou une étiquette

Les modèles de l’administration utilisent le même schéma `store()`.

```php
use Joomla\CMS\Factory;
use Joomla\CMS\Log\Log;

require_once JPATH_ADMINISTRATOR . '/components/com_flexicontent/models/type.php';
// Use field.php or tag.php instead, depending on the record.
// require_once JPATH_ADMINISTRATOR . '/components/com_flexicontent/models/field.php';
// require_once JPATH_ADMINISTRATOR . '/components/com_flexicontent/models/tag.php';

$model = new FlexicontentModelType();
// new FlexicontentModelField();
// new FlexicontentModelTag();

$data = [
    'id'    => 0,       // Existing id to update, 0 to create.
    'title' => 'My type',
    'alias' => 'my-type',
];

if (!$model->store($data)) {
    $msg = 'Failed to store record: ' . $model->getError();
    Log::add($msg);
    echo $msg . '<br />';
}
```

Consultez la table de base de données pour les propriétés supplémentaires.

## Récupérer les définitions de champs et vérifier l’accès

```php
use Joomla\CMS\Factory;
use Joomla\Registry\Registry;

$app  = Factory::getApplication();
$user = $app->getIdentity();
$db   = Factory::getDbo();

$viewLevels = $user->getAuthorisedViewLevels();
$fieldnames = ['field_name1', 'field_name2', 'field_name3'];

$query = $db->getQuery(true)
    ->select('*')
    ->from($db->quoteName('#__flexicontent_fields'))
    ->whereIn($db->quoteName('name'), $fieldnames);

$db->setQuery($query);
$fields = $db->loadObjectList('name');

foreach ($fields as $field) {
    $field->parameters = new Registry($field->attribs);
    $field->has_access = in_array($field->access, $viewLevels, true);
}
```

## Événements des plugins

FLEXIcontent déclenche des événements que peuvent implémenter les plugins de type `flexicontent` :

- `onBeforeSaveItem`
- `onAfterSaveItem`
- `onCompleteSaveItem`

Un exemple fonctionnel se trouve dans `plugins/flexicontent/flexinotify/flexinotify.php`. Les plugins de champs de type `flexicontent_fields` ont leurs propres méthodes API ; voir le tutoriel officiel lié ci-dessous.

## Afficher du contenu et générer des URL

Pour des cas plus avancés, les tutoriels officiels fournissent du code prêt à adapter :

- [Afficher la vue d’un contenu dans un code personnalisé](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/294-how-to-render-item-view-in-custom-code.html)
- [Récupérer l’affichage HTML des champs dans un code tiers](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/247-retrieving-the-html-display-of-fc-fields-inside-3rd-party-code.html)
- [Générer des URL SEF FLEXIcontent dans un code personnalisé](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/323-how-to-generate-flexicontent-sef-urls-in-custom-code.html)
- [Appeler les fonctions de champ comme tâches de contrôleur](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/575-calling-flexicontent-field-functions-as-controller-tasks.html)
- [Méthodes API des champs FLEXIcontent](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/301-api-methods-of-flexicontent-fields.html)

## Sources officielles

- [Créer/modifier un contenu avec le modèle d’élément](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/580-how-to-create-a-flexicontent-item-by-calling-the-flexicontent-item-model-in-custom-code.html)
- [Utiliser les modèles de base de données type / champ / étiquette](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/654-how-to-use-type-field-tag-db-models-of-flexicontent-to-create-edit-records.html)
- [Exemple de code pour récupérer les données de champs et vérifier l’accès](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/500-sample-code-to-retrieve-field-data-also-creating-parameters-and-checking-access.html)
- [Méthodes API pour les plugins de type « flexicontent »](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/632-api-methods-triggered-events-for-plugins-of-type-flexicontent.html)
