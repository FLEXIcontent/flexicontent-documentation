---
sidebar_position: 1
---

# Installation

Cette page décrit l'installation de FLEXIcontent sur un site Joomla! 4, 5 ou 6.

## Prérequis

- Un site Joomla! fonctionnel sur une version supportée par la branche 5.x.
- Une configuration PHP compatible avec votre version de Joomla!.
- La directive `max_input_vars` réglée à **4000 ou plus**. Elle est vérifiable dans l'administration Joomla!, via **Système → Informations sur le site → Informations PHP**. Les formulaires FLEXIcontent pouvant contenir beaucoup de champs, une valeur trop basse peut empêcher l'enregistrement.

:::tip
Si vous devez modifier `max_input_vars`, faites-le dans le `php.ini` de l'hébergement. La modification via `.htaccess` fonctionne sur certains serveurs seulement.
:::

## Installer le composant

1. Téléchargez le package depuis la page [Latest version](https://www.flexicontent.org/downloads/latest-version.html) du site officiel.
2. Dans l'administration Joomla!, allez dans **Système → Installer → Extensions**.
3. Uploadez le fichier ZIP téléchargé.
4. Attendez la confirmation d'installation, puis vérifiez que le composant **FLEXIcontent** apparaît dans le menu des composants.
5. Ouvrez la configuration du composant et enregistrez une première fois les options pour initialiser les paramètres.

## Après l'installation

Pour obtenir un site visible rapidement :

1. Créez un **type de contenu** ou utilisez le type `Article` fourni par défaut.
2. Associez-lui quelques **champs** (texte, date, image, liste de choix…).
3. Créez une **catégorie** et affectez-la au type.
4. Créez un premier **contenu** et renseignez ses champs.
5. Créez un **élément de menu** de type vue catégorie FLEXIcontent pour afficher la liste.

Le détail de ces étapes est décrit dans [Premiers pas](./premiers-pas.md).

## Mise à jour

:::warning
Faites toujours une sauvegarde des fichiers et de la base de données avant une mise à jour.
:::

1. Téléchargez la nouvelle version.
2. Installez le paquet par-dessus l'installation existante via **Système → Installer → Extensions**.
3. Videz le cache Joomla! et le cache FLEXIcontent.
4. Ouvrez les options des modèles, modules et types de contenu, puis enregistrez-les à nouveau si l'interface le demande.

:::caution
Lors du passage à une nouvelle branche majeure, certains réglages de modèles ou de styles peuvent changer. Vérifiez vos vues après la mise à jour et réenregistrez les options concernées.
:::

## Dépannage

- **Erreur pendant l'installation** : vérifiez la mémoire PHP disponible et la taille maximale des fichiers uploadés.
- **La configuration ne reste pas enregistrée** : vérifiez les permissions d'écriture et la directive `max_input_vars`.
- **Aucun champ ne s'affiche** : vérifiez que les champs sont bien associés au type de contenu utilisé.
