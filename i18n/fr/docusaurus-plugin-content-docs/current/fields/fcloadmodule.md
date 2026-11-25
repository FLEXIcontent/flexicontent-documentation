---
sidebar_position: 17
---

# Charger un module

Charger un module ou une position de module dans un contenu

*Plugin : `fcloadmodule` — Charger un module / une position de module*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/fcloadmodule/fcloadmodule.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Sélectionner un module

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode**<br />`module_method` | Choisir la méthode de chargement. Tous les modules d'une position, ou bien l'instance unique de module. | `multilist` | `1` = Module<br />`2` = Position | `1` (Module) |
| **Module**<br />`modules` | Sélectionner un module à charger | `fcmodules` | — | — |
| **Position**<br />`position` | Sélectionner une position de module à charger | `fcpositions` | — | — |
| **Style**<br />`style` | Sélectionner le style pour le rendu de votre module, laisser vide pour utiliser le rendu basique 'none' | `text` | — | — |

## Édition

#### Édition

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Personnaliser les paramètres du module par contenu (pas pour le mode position)**<br />`mod_params` | Vous pouvez - essayer de - personnaliser certains paramètres du module en autorisant l'utilisateur modifier ses valeurs depuis le formulaire du contenu. **NOTE : **Vous devez examiner le fichier XML du module cible pour trouver le nom des paramètres. Par exemple : etiquette_param1!!nom_param1 %% etiquette_param2!!nom_param2 %% etiquette_param3!!nom_param3 | `textarea` | — | — |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Édition

## Apparence

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
