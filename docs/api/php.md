---
title: PHP developer API
sidebar_position: 5
---

# PHP developer API

Use the PHP API when your code runs **inside Joomla!**: a custom extension, a plugin, a module, a template or a command-line script. For external HTTP clients, use the [JSON:API](./webservices.md) instead.

The examples below are adapted from the official FLEXIcontent tutorials. Treat them as a starting point and validate them on your Joomla!/FLEXIcontent version.

## Load the Joomla! framework

When the code is not already inside a Joomla! extension, bootstrap the application first. This example assumes the script is in the site root; adjust `JPATH_BASE` if it lives in a subfolder.

```php
define('_JEXEC', 1);
define('JPATH_BASE', realpath(__DIR__));
define('DS', DIRECTORY_SEPARATOR);

require_once JPATH_BASE . '/includes/defines.php';
require_once JPATH_BASE . '/includes/framework.php';

$app = Joomla\CMS\Factory::getApplication('site');
$app->initialise();
```

Older official examples use `JFactory::getApplication()`. With Joomla! 4-6, prefer `Joomla\CMS\Factory`.

## Load FLEXIcontent classes and languages

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

## Create or update an item

The item model handles core data, categories, tags and custom field values.

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

## Create or update a type, field or tag

The backend models use the same `store()` pattern.

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

See the DB table for additional properties.

## Retrieve field definitions and check access

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

## Plugin events

FLEXIcontent triggers events that plugins of type `flexicontent` can implement:

- `onBeforeSaveItem`
- `onAfterSaveItem`
- `onCompleteSaveItem`

A working example is in `plugins/flexicontent/flexinotify/flexinotify.php`. Field plugins of type `flexicontent_fields` have their own API methods; see the official tutorial linked below.

## Render content and generate URLs

For more advanced use cases, the official tutorials provide ready-to-adapt code:

- [Render item view in custom code](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/294-how-to-render-item-view-in-custom-code.html)
- [Retrieve the HTML display of fields inside third-party code](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/247-retrieving-the-html-display-of-fc-fields-inside-3rd-party-code.html)
- [Generate FLEXIcontent SEF URLs in custom code](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/323-how-to-generate-flexicontent-sef-urls-in-custom-code.html)
- [Call field functions as controller tasks](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/575-calling-flexicontent-field-functions-as-controller-tasks.html)
- [API methods of FLEXIcontent fields](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/301-api-methods-of-flexicontent-fields.html)

## Official sources

- [Create/update an item with the item model](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/580-how-to-create-a-flexicontent-item-by-calling-the-flexicontent-item-model-in-custom-code.html)
- [Use type / field / tag DB models](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/654-how-to-use-type-field-tag-db-models-of-flexicontent-to-create-edit-records.html)
- [Sample code to retrieve field data and check access](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/500-sample-code-to-retrieve-field-data-also-creating-parameters-and-checking-access.html)
- [API methods for plugins of type "flexicontent"](https://www.flexicontent.org/documentation/tutorials-english/70-developer-api-field-plugins/632-api-methods-triggered-events-for-plugins-of-type-flexicontent.html)
