---
sidebar_position: 3
---

# Types de contenu — options

Un type de contenu définit les champs, les règles de rédaction et les paramètres d’affichage disponibles pour une catégorie de contenus. Ouvrez un type depuis **Composants → FLEXIcontent → Types de contenu**.

:::info Source
Cette page est générée depuis `admin/models/forms/type.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Titre

### Texte du titre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`title_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`title_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |
| **Titre automatique**<br />`auto_title` | Vous pouvez configurer le titre comme une valeur automatique | `multilist` | `0` = Non<br />`1` = Indiquer l'id<br />`2` = Utiliser du code personnalisé | `0` (Non) |
| **Code personnalisé**<br />`auto_title_code` | Entrez le code PHP à utiliser pour créer la valeur personnalisée, veuillez vider ce champs et enregistrez pour charger l'exemple par défaut, puis personnaliser | `textarea` | — | `$F = & $item-&gt;fields; $txt = isset( $F['fieldname01'] ) ? $F['fieldname01']-&gt;postdata[0] : 'fieldname01 field not found'; return $txt;` |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`title_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`title_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Description

### Description

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Etiquette Description**<br />`maintext_label` | L'étiquette du champ de description principal dans le formulaire de saisie. La valeur par défaut est 'Description'. | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`maintext_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |
| **Editeur**<br />`maintext_hide_html` | Utilser un éditeur html (WYSIWYG) ou un simple textarea | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Editeur HTML<br />`1` = Simple Zone de texte | — |
| **Largeur de l'éditeur**<br />`maintext_width` | Largeur de l'éditeur html | `text` | — | — |
| **Hauteur de l'éditeur**<br />`maintext_height` | Définit la hauteur de l'éditeur HTML | `text` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`maintext_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`maintext_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Catégories

### Catégories

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`categories_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`categories_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`categories_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`categories_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Liens

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter des liens**<br />`categories_link_to_view` | Lier chaque valeur à sa vue par liste d'articles | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |

## Créé

### Créé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`created_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`created_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`created_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`created_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Créé par

### Créé par

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`created_by_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`created_by_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`created_by_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`created_by_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Modification

### Modification

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`modified_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`modified_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`modified_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`modified_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Modifié par

### Modifié par

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`modified_by_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`modified_by_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`modified_by_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`modified_by_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Type du document

### Type du document

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`document_type_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`document_type_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`document_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`document_type_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Vues

### Vues

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`hits_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`hits_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`hits_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`hits_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Version

### Version

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`version_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`version_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`version_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`version_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Etat

### Etat

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`state_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`state_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`state_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`state_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Vote

### Vote

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`voting_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`voting_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`voting_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`voting_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |
| **Afficher le nombre total de votes**<br />`voting_main_counter` | Afficher le nombre total de votes | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Désactiver<br />`1` = Activer | — |
| **Afficher l'étiquette du compteur**<br />`voting_main_counter_show_label` | Cela va ajouter une étiquette « votes » après le compteur de vote | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Désactiver<br />`1` = Activer | — |
| **Affiche le pourcentage**<br />`voting_main_counter_show_percentage` | Ceci affichera le pourcentage à côté de chaque étiquette de notation | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Désactiver<br />`1` = Activer | — |

#### Note moyenne

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`voting_main_label` | Libellé de la note moyenne | `text` | — | — |
| **Texte pour l'Échelle de notation**<br />`voting_rating_texts` | Représentation textuelle de l'échelle de notation. Entrez une liste de chaînes de langue séparée par des virgules. par exemple JVERYPOOR, JPOOR, JFAIR, JBON, JEXCELLENT | `textarea` | — | — |

#### Vote composé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer**<br />`voting_enable_extra_votes` | Activer/désactiver l'affichage des caractéristiques de vote partiel, comme la qualité, la performance, la précision, etc | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Critères de vote**<br />`voting_extra_votes` | Ici, vous pouvez définir les caractéristiques de vote comme par exemple Qualité, Vitesse, Précision, etc ... **Écrire comme**: 1##Quality##Description%% 2##Speed##Description%% 3##Accuracy##Description%% 4##Apparence##Description%% . **NOTE 1**: Les noms seront passés par JText . . pour permettre la prise en charge multilingue (vous pouvez les ajouter à vos fichiers de langue) | `textarea` | — | — |
| **Afficher le nombre total de votes**<br />`voting_extra_counter` | Afficher le nombre total de votes | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Désactiver<br />`1` = Activer | — |
| **Afficher l'étiquette du compteur**<br />`voting_extra_counter_show_label` | Cela va ajouter une étiquette « votes » après le compteur de vote | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Désactiver<br />`1` = Activer | — |
| **Affiche le pourcentage**<br />`voting_extra_counter_show_percentage` | Ceci affichera le pourcentage à côté de chaque étiquette de notation | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Désactiver<br />`1` = Activer | — |

## Favoris

### Favoris

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`favourites_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`favourites_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`favourites_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`favourites_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

## Mots-clés

### Mots-clés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Étiquette**<br />`tags_label` | Défini un nom personnalisé pour ce **champ cœur** Pour utilisation par langue, utilisez [shortlang]= Par exemple : [fr]=Libellé français [en]=Libellé anglais [default]=Libellé par défaut ... **SANS** retour à la ligne | `text` | — | — |

#### Édition

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Description**<br />`tags_desc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Apparence

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`tags_display_label` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |
| **Description**<br />`tags_viewdesc` | Définir une description de l'info-bulle personnalisée pour ce champ CORE, lorsque qu'il est visualisé pour chaque langue d'utilisation [shortlang]= par ex. [fr]=Description du champ en français [en]=Description du champ en français [default]=Description par défaut du champ ... SANS caractères pour un saut de ligne | `textarea` | — | — |

#### Liens

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter des liens**<br />`tags_link_to_view` | Lier chaque valeur à sa vue par liste d'articles | `radio` | `—` = Utiliser les paramètres du champ<br />`0` = Non<br />`1` = Oui | — |

## Rédaction

### Catégorie principale

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Sous-arborescence autorisée -- vide = tout autoriser --**<br />`catid_allowed_parent` | Sélectionner la sous-arborescence de catégories utilisée pour sélectionner la catégorie principale | `flexicategories` | — | — |
| **Désactiver le parent de la sous-arborescence**<br />`catid_allowed_parent_disable` | Il est généralement souhaitable d’empêcher la sélection de la catégorie racine de la sous-arborescence | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Catégorie par défaut**<br />`catid_default` | Sélectionner la catégorie principale par défaut pour ce type (pré-sélectionnée au chargement du formulaire) | `flexicategories` | — | — |

### Catégories secondaires

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Sous-arborescence autorisée -- vide = tout autoriser --**<br />`cid_allowed_parent` | Sélectionner la sous-arborescence de catégories autorisée pour sélectionner les catégories secondaires | `flexicategories` | — | — |
| **Désactiver le parent de la sous-arborescence**<br />`cid_allowed_parent_disable` | Il est généralement souhaitable d’empêcher la sélection de la catégorie racine de la sous-arborescence | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Catégories par défaut**<br />`cid_default` | Sélectionner les catégories secondaires par défaut | `flexicategories` | — | — |

### Template vue contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Templates de contenu autorisés -- aucun autorise tout --**<br />`allowed_ilayouts` | Sélectionner les templates autorisés pour ce type **Remarque :** C'est utilie si vous souhaitez autoriser la sélection des templates pour les utilisateurs frontend ayant des droits de saisie de contenu, surtout pour réduire la sélection dans la liste des templates. | `ilayoutlist` | — | — |

### Balises courantes (sélectionnables via cases à cocher)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mots clés**<br />`quick_tags` | Étiquettes sélectionnables par cases à cocher dans le formulaire (pour une sélection plus rapide/facile) | `tag` | — | — |

## Référencement

### Prise en charge des microdonnées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Type microdata**<br />`microdata_itemtype` | Sélectionnez un type de microdonnées qui caractérisera tous les éléments du type. MICRODATA permet aux moteurs de recherche de catégoriser votre contenu de manière appropriée, améliorant le référencement de vos pages | `microdatatype` | — | — |

### Balise HTML « title »

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Surcharger**<br />`override_title` | Défini à oui, cela permet d'utiliser le titre du contenu (ou bien le titre personnalisé si il est défini) comme titre de la page (tag TITLE HTML) à la place du titre défini dans le menu. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Catégorie vers**<br />`addcat_title` | Ajoutez le nom de la catégorie dans la balise de titre à gauche ou à droite du nom de l'article | `radio` | `0` = Non<br />`1` = Gauche<br />`2` = Droite | `1` (Gauche) |

### Autres paramètres de référencement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Tag canonique**<br />`add_canonical` | Ajouter une balise meta canonique dans le code source de vos pages, cela aide les moteurs de recherche à identifier une page visualisée via des URL différentes et lui donner meilleur rang, en ne l'indexant pas plusieurs fois | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Robots des moteurs de recherche**<br />`robots` | Indiquer si les robots des moteurs de recherche vont ajouter ce contenu dans leur base de données et s'ils doivent suivre (respectivement indexer) les liens qui y figurent | `radio` | `—` = Par défaut de Joomla!<br />`index, follow` = index, follow<br />`noindex, follow` = noindex, follow<br />`index, nofollow` = index, nofollow<br />`noindex, nofollow` = noindex, nofollow | — |

### Élément de menu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **L'élément de menu par défaut pour les URLs de contenu**<br />`type_menu_itemid` | L'élément de menu qui sera utilisé dans les URL d'élément quand un lien de menu plus approprié n'a pas pu être trouvé. un élément de menu plus approprié est celui qui pointe directement vers un élément de contenu. **REMARQUE :** L'élément de menu effets quels modules sont actifs. | `fcmenuitem` | — | — |
| **Utilisation de l'élément de menu par défaut**<br />`type_menu_itemid_usage` | L'élément de menu qui sera utilisé dans les éléments de ce type quand un élément de menu plus approprié n'a pas pu être trouvé. un élément de menu plus approprié est celui qui pointe directement vers un élément de contenu. **REMARQUE :** L'élément de menu effets quels modules sont actifs. | `radio` | `0` = Aucun<br />`1` = Essayer avant les contenus de la catégorie<br />`2` = Essayer après les contenus de la catégorie<br />`3` = Élément de menu actif | `0` (Aucun) |

## Vue contenu

### Affichage Article Joomla

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser**<br />`allow_jview` | Par défaut, la vue de l'article joomla sera redirigée vers la vue de l'élément FLEXIcontent. Si la redirection est désactivée, alors il permettra à l'élément d'être consulté à la fois par la vue article de Joomla et la vue d'éléments de FLEXIcontent , donc par ex. les liens de l'article dans la vue catégorie Joomla ne seront pas redirigés NOTE : 'Autorisé' et 'Rerouté' affichera les modules assignés aux éléments du menu Joomla, 'redirect' changera l'URL pour être l'URL de l'affichage de l'élément FLEXIcontent et affichera le module assigné aux éléments du menu FLEXIcontent Remarque : (compatibilité) ceci est par défaut autorisé pour le 'article' de type **type**, mais vous pouvez aussi autoriser d'autres types NOTE : si activé, les liens de la vue de recherche sont activés, lien vers la vue de l'article JOOMLA et les URL peuvent contenir /component/content/article/ | `multilist` | `0` = Redirection vers la vue FLEXIcontent<br />`2` = Redirection vers une vue FLEXIcontent<br />`1` = Oui | `0` (Redirection vers la vue FLEXIcontent) |
| **Lien vers la vue Recherche avancée**<br />`search_jlinks` | Les éléments de ce type dans la vue de recherche peuvent être liés à la vue d'article Joomla ou à la vue d'éléments de FLEXIcontent | `radio` | `0` = Lien du Contenu FC<br />`1` = Lien article Joomla | `1` (Lien article Joomla) |
| **Ajouter un champ personnalisé**<br />`jview_fields_placement` | Sélectionnez cette option pour ajouter des champs personnalisés FLEXIcontent à la vue d'article Joomla. NOTE : tous les champs personnalisés seront ajoutés selon les niveaux ACCESS autorisés à l'utilisateur actuel de la partie publique | `radio` | `0` = Désactiver<br />`1` = Afficher Avant le contenu<br />`2` = Afficher Après le contenu | `0` (Désactiver) |

### Contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le titre**<br />`show_title` | Montrer/Masquer le titre du contenu | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Montrer le texte d'introduction**<br />`show_intro` | Permet de montrer le texte d'introduction même dans la vue contenu, en plus de la description complète. | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Activer l'intégration des commentaires**<br />`comments` | Autorise l'intégration d'un système de commentaires. **REMARQUE:** Ce paramètre peut être surchargé dans les types, les catégories, les éléments uniques ou les éléments de menu. **REMARQUE:** Si vous désactivez cette option, vous pourrez activer manuellement (le champ de description activera tout par défaut) le plug-in de contenu Joomla approprié de votre système de commentaires pour insérer des commentaires via un événement de contenu Joomla. Si vous ajoutez des commentaires de cette manière, vous ne pourrez pas utiliser le paramètre \"Désactiver les commentaires\" dans le formulaire, mais vous devrez le faire comme le recommande votre système de commentaires, par exemple. en insérant un texte spécial dans la description | `radio` | `—` = Paramètres globaux<br />`0` = Désactiver ou intégrer manuellement<br />`1` = JComments | — |
| **Créer le fil de navigation automatiquement**<br />`automatic_pathways` | Le chemin de catégories et de contenus (affiché dans le module de fil de navigation) sera généré automatiquement (a) en supprimant toutes les entrées du menu du fil de navigation et en ajoutant l'arborescence de catégories puis le titre de l'article. NOTE : vous pouvez surcharger ces paramètres pour chaque catégorie, type et contenu. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

### Icônes

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Icône imprimer**<br />`show_print_icon` | Affiche l'icône d'impression. | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Icône email**<br />`show_email_icon` | Activer le partage de la page via e-mail | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Bouton Modifier**<br />`show_editbutton` | Affiche un bouton de modification pour tous les utilisateurs qui sont connectés et qui ont les droits nécessaires pour effectuer l'édition du contenu | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Lien vers la partie publique<br />`2` = Lien vers l'administration | — |
| **Bouton Supprimer (permanent)**<br />`show_deletebutton` | Actif l'affichage du bouton Supprimer pour tous les éléments que l'utilisateur connecté peut supprimer. REMARQUE, ce n'est pas un bouton de corbeille, cette action va supprimé définitivement l'élément. | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Bouton Statut**<br />`show_state_icon` | Activer le changement de statut rapide via AJAX | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |

### Style et comportement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajoute des css à la vue contenu**<br />`view_extra_css_fe` | Ajoute des règles CSS supplémentaires à la vue de l'élément. - Généralement vous devriez le définir par type d'élément. | `editor` | — | — |
| **Ajouter du code JS dans le formulaire d'édition pour développeur seulement***<br />`view_extra_js_fe` | Ajoute un code JS supplémentaire à la vue de l'élément. - Généralement vous devriez le définir par type d'élément. | `editor` | — | — |

## Vue rechercher

### Vue rechercher

:::note
La vue de recherche peut effectuer une **recherche textuelle** et un **filtrage**, différemment selon le type de contenu ; vous pouvez définir ici le comportement de la recherche. **REMARQUE :** ces paramètres ne sont pas utilisés dans les vues de type catégorie (listes de contenus), où la configuration se fait dans le composant / la catégorie / les éléments de menu
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Texte utilisable pour la recherche**<br />`searchable` | La recherche de texte se produira dans les champs sélectionnés (si l'utilisation d'un champ spécifique est activée dans la configuration de l'élément de menu de recherche) | `filters` | — | — |
| **Filtres**<br />`filters` | NOTE : Vous devez activer son utilisation dans la configuration de la vue **recherche** (par exemple via l'élément de menu) NOTE : Vous pouvez definir l'apparence du filtre et son comportement en éditant la configuration de chaque champ individuel | `filters` | — | — |
| **Priorité de recherche du type**<br />`search_priority` | Description de la priorité de recherche du type | `number` | — | `0` |

#### Affichage des résultats de recherche du type

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Image de recherche du type**<br />`search_image` | Description de l’image de recherche du type | `fcimage` | — | — |
| **Afficher la date dans la recherche du type**<br />`search_show_date` | Description de l’affichage de la date dans la recherche du type | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Champs d’information de recherche du type**<br />`search_infoflds` | Description des champs d’information de recherche du type | `textarea` | — | — |

## Formulaire de saisie

#### Début du formulaire de contenu

### Formulaire de contenu (Public)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Apparence du formulaire de saisie**<br />`form_ilayout_fe` | — | `fclayout` | **Dispositions intégrées**<br />`tabs` = onglets (par défaut)<br />`flat` = plat | — |

#### Formulaire de contenu (Public)

### Paramétrage du formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Boutons optionnels**<br />`allowbuttons_fe` | Sélectionner les boutons que vous souhaitez faire apparaitre dans le formulaire de saisie en frontend. | `fccheckbox` | — | — |
| **Placement des boutons**<br />`buttons_placement_fe` | Selectionner pour afficher des boutons de formulaire en haut ou en bas du formulaire | `radio` | `—` = Paramètres globaux<br />`0` = En haut<br />`1` = En bas<br />`2` = A gauche<br />`3` = A droite | — |

#### Affiche un message du type approbation nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Dans le formulaire**<br />`approval_warning_inform_fe` | Activez ceci, pour afficher un message dans le formulaire de l'élément, si l'utilisateur actuel peut publier de nouveaux éléments ou s'il peut auto-approuver les modifications aux éléments existants | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Après la soumission du formulaire**<br />`approval_warning_aftersubmit_fe` | Activez ceci, pour afficher un avertissement après l'envoi du formulaire, en disant si l'approbation est nécessaire pour que le nouvel élément soit publié ou pour que les modifications de l'élément existant deviennent actives | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Nécessite une révision de cette version**<br />`version_reviewal_msg_fe` | _Veuillez noter que la **version** de votre document devra être validée par un administrateur_ | `textarea` | — | — |
| **Nécessite l'approbation du contenu**<br />`document_approval_msg_fe` | _Veuillez noter que votre **nouvel article** devra être relu et accepté par un administrateur_ | `textarea` | — | — |
| **Peut nécessiter une révision de cette version**<br />`mr_version_revial_msg_fe` | _Veuillez noter que la nouvelle **version** de ce document a peut-être besoin d'être vérifiée et approuvée avant publication. Cela peut dépendre de la catégorie du contenu et / ou du type du contenu. Si l'approbation est nécessaire, vous serez avisé après avoir enregistré ce contenu._ | `textarea` | — | — |
| **Peut nécessiter l'approbation du contenu**<br />`mr_document_approval_msg_fe` | _Veuillez noter que votre nouveau contenu peut nécessiter une approbation avant d'être accepté. Cela peut dépendre de catégorie du contenu et/ou de type de contenu. Vous serez avisé si l'approbation est nécessaire, après avoir enregistré ce contenu._ | `textarea` | — | — |
| **Modifications appliquées immédiatement**<br />`changes_applied_immediately_msg_fe` | _Veuillez noter que la gestion des versions de document est désactivée, donc toute modification que vous apportez à ce contenu sera accepté/activé immédiatement et la version précédente sera perdue_ | `textarea` | — | — |

#### Instructions / redirections d'URL / etc

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Instructions pour la saisie**<br />`submit_message` | Ces instructions seront placées en haut du formulaire, après les boutons **NOTE **: Cela peut être une chaîne de langue (à ajouter à vos fichiers de langue) | `textarea` | — | — |
| **Redirection URL après la soumission cache le bouton Aperçu**<br />`submit_redirect_url_fe` | Vous pouvez définir une URL personnalisée vers laquelle l'utilisateur sera redirigé après avoir soumis un nouveau contenu. **NOTE :** Cela fonctionnera même si vous cliquez sur les boutons 'Ajouter' ou 'Appliquer' avant de fermer l'élément **Remarque :** Définir ceci masquera le bouton d'aperçu lors de l'envoi de nouveaux éléments | `text` | — | — |
| **Page d'accès non autorisé (saisir un contenu)**<br />`notauthurl` | Spécifiez l'URL / ID du lien de menu de la page vers laquelle vous souhaitez que vos visiteurs / utilisateurs soient dirigés s'ils n'ont pas les droits suffisants pour créer plus de contenu (ou aucun). Cela pourrait être (par exemple) la page des plans d'abonnement si vous vendez votre espace de publication. **NOTE :** Si vous ne définissez rien ici, la page générale non autorisé sera utilisée. | `menuitem` | — | — |

#### Formulaire de sécurité critères d'affichage pour CAPTCHA

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser les captcha**<br />`use_captcha` | Choisir à quel moment afficher un champ captcha pour protéger le formulaire des robots | `multilist` | `—` = Paramètres globaux<br />`0` = Désactiver<br />`1` = Invités (Recommandé)<br />`2` = Tous les utilisateurs | — |
| **Plugin de Captcha**<br />`captcha` | Choisir un plugin spécifique de captcha pour surcharger le paramètre par défaut | `plugins` | `—` = Paramètres globaux<br />`0` = Désactiver | — |
| **Type d'opération**<br />`captcha_formop` | Lorsque l'opération est sur le type sélectionné | `radio` | `—` = Paramètres globaux<br />`0` = Envoyer (recommander)<br />`1` = Envoyer/Editer | — |

### Compatibilité Joomla

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Éditer les liens**<br />`create_jarticle_form_links_fe` | Créer des liens d'édition vers le formulaire d'article Joomla ou le formulaire d'élément Flexicontent | `multilist` | `0` = FC Formulaire de contenu | `0` (FC Formulaire de contenu) |
| **Images intro / complètes**<br />`use_jimages_fe` | Afficher les images intro/complètes | `radio` | `—` = Paramètres globaux<br />`0` = Désactiver<br />`1` = Activer | — |
| **URL**<br />`use_jurls_fe` | Afficher les URL | `radio` | `—` = Paramètres globaux<br />`0` = Désactiver<br />`1` = Activer | — |

### Édition de base

#### Nouveaux / existants contenus

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le titre**<br />`usetitle_fe` | Sélectionnez pour afficher ou masquer le titre de l'élément - vous pouvez définir automatiquement dans les paramètres de type | `radio` | `—` = Paramètres globaux<br />`0` = Cacher si automatique<br />`1` = Oui | — |
| **Utiliser les Alias**<br />`usealias_fe` | Autoriser l'utilisateur à saisir les alias. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser le type**<br />`usetype_fe` | Afficher le sélecteur de type pour permettre le changement de type d'élément | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser l'état**<br />`usestate_fe` | Afficher le sélecteur d'état pour permettre le changement d'état de publication du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser l'accès**<br />`useaccess_fe` | Afficher le sélecteur d'accès pour permettre de changer le niveau d'accès du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser les vedettes**<br />`usefeatured_fe` | Afficher le sélecteur de vedette pour permettre le changement d'état du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser les tags**<br />`usetags_fe` | Autoriser les tags a être cachés, pour les groupes qui possèdent le droit sur les tags, cela n'empêche pas après de gérer les tags | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui<br />`2` = Afficher seulement | — |
| **Autoriser la désactivation des commentaires**<br />`allowdisablingcomments_fe` | Vous pouvez préciser ici si les auteurs ou les éditeurs peuvent désactiver les commentaires pour le contenu qu'ils modifient ou ajoutent. Si vous autorisez ce paramètre, il est recommandé de ne pas afficher les paramètres avancés du contenu. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

#### Catégories

:::note
Remarque : Vous avez toujours besoin des **ACL** pour éviter les changements de catégories multiples. Cacher ces dernières, n'empêche pas les utilisateurs de les modifier ...
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser la catégorie**<br />`usemaincat_fe` | Si vous désactivez cette option, vous devez également définir une catégorie par défaut dans la configuration de chaque type (généralement vous allez créer une catégorie avec le même nom que le type et la définir comme par défaut) | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Catégories secondaires**<br />`show_seccats_fe` | — | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Cacher si non modifiable<br />`2` = Montrer | — |
| **Catégories en vedette**<br />`show_featcats_fe` | — | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Cacher si non modifiable<br />`2` = Montrer | — |

:::note
Filtrer
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pas dans la langue de l'élément**<br />`iform_cats_not_in_itemlang_fe` | Masquer les catégories dans des langues différentes de la langue de l'élément ou ajouter une langue au titre de la catégorie | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Saisir un nom de langue | — |
| **États autorisés**<br />`iform_catstates_allowed_fe` | Les catégories avec des états non autorisés seront masquées, sauf si l'élément est déjà affecté à une telle catégorie | `fccheckbox` | — | — |

#### Langue

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le langage**<br />`uselang_fe` | Autoriser l'utilisateur à choisir sa langue. NOTE : Sélectionnez une langue par défaut avant de désactiver ce paramètre | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui<br />`3` = Oui, sans associations<br />`2` = Afficher seulement | — |
| **Langue par défaut**<br />`default_language_fe` | C'est la langue qui sera pré-sélectionnée, particulièrement utile si vous cachez la langue | `fclanguage` | `_author_lang_` = Utiliser la langue de l'éditeur<br />`_site_default_` = Utiliser la langue par défaut du site | — |
| **Désactiver les langues**<br />`disable_languages_fe` | Par exemple, vous pourriez choisir de désactiver la langue 'ALL' | `fclanguage` | — | — |

#### Sélecteur de langue

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher comme**<br />`langdisplay_fe` | Vous pouvez l'afficher ex comme une liste déroulante ou des boutons radios | `radio` | `—` = Paramètres globaux<br />`2` = Sélecteur liste déroulante<br />`3` = Bouton radio | — |
| **Afficher drapeaux (radio)**<br />`langdisplay_flags_fe` | Afficher les icônes drapeaux | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Montrer le texte (radio)**<br />`langdisplay_texts_fe` | Activer pour afficher le texte comme un code langue | `radio` | `—` = Paramètres globaux<br />`0` = Pas de texte<br />`1` = Code de la langue<br />`2` = Titre<br />`3` = Titre natif<br />`4` = Titre + Titre natif | — |

#### Contenus existants

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser les modifications de langue**<br />`allowlangmods_fe` | Permettre à l'utilisateur de modifier les propriétés de la langue pour des éléments -existant-. Habituellement, vous devriez interdire aux utilisateurs de modifier les propriétés de langue existantes comme la langue de l'élément et le contenu original de la traduction | `fccheckbox` | — | — |

:::note
Vous avez accès à plus d'option de configuration ici: Plugin de Notifications
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser la notification du propriétaire**<br />`allow_owner_notify_fe` | Permettre à l'éditeur d'envoyer une notification de mise à jour (email) au propriétaire du contenu courant | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui, un par session | — |
| **Autoriser la notification des inscrits (contenus favoris des utilisateurs)**<br />`allow_subscribers_notify_fe` | Permettre à l'éditeur d'envoyer des notifications de mise à jour (emails) aux utilisateurs qui ont en favori le contenu courant | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui, un par session | — |

### Options avancées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser les détails de publication**<br />`usepublicationdetails_fe` | Sélectionnez ici pour autoriser : -Basic- Publication Details: (début & date de fin de publication & alias d'auteur) aux personnes qui peuvent -EDITER- l'élément. ou - Tous les détails de la publication : (auteur de l'élément & date de création) sont disponibles UNIQUEMENT aux utilisateurs de Super Admin. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Basique (recommandé)<br />`2` = Tous * | — |
| **Utiliser les métadonnées**<br />`usemetadata_fe` | Recommandé pour masquer ou uniquement autoriser -basic- META données (description et mots-clés), le reste sera inutile pour les utilisateurs | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Basique (recommandé)<br />`2` = Tous * | — |
| **Configuration SEO**<br />`useseoconf_fe` | Permettre à l'utilisateur de modifier les paramètres SEO, comme balise de titre personnalisée | `radio` | `—` = Paramètres globaux<br />`0` = Non (recommandé)<br />`1` = Oui | — |
| **Options d'affichage**<br />`usedisplaydetails_fe` | Sélectionnez les groupes de paramètres que vous souhaitez rendre modifiables dans le frontend | `radio` | `—` = Paramètres globaux<br />`0` = Non (recommandé)<br />`1` = Basique<br />`2` = Avancé | — |
| **Options d'affichage d'un composant tiers**<br />`use3rdpartyparams_fe` | Sélectionner pour afficher les options d'affichage des extensions tierces | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Sélection du modèle**<br />`selecttheme_fe` | Activer la sélection et la configuration du modèle pour les groupes d'utilisateur de l'interface publique ayant le privilège de gestion des modèles. | `radio` | `—` = Paramètres globaux<br />`0` = Non (recommandé)<br />`1` = Sélectionner<br />`2` = Sélectionner et configurer | — |
| **Autorisations (ACL)**<br />`permsplacement_fe` | Sélectionnez ici pour afficher les permissions pour l'utilisateur si celles-ci sont modifiables | `radio` | `—` = Paramètres globaux<br />`0` = Toujours masquer (même si modifiable)<br />`1` = En ligne<br />`2` = Carrousel | — |
| **Versions**<br />`versionsplacement_fe` | Sélectionnez ici pour afficher la version en ligne dans une fenêtre pop-up | `radio` | `—` = Paramètres globaux<br />`0` = Toujours masquer (même si modifiable)<br />`1` = Pop-up<br />`2` = En ligne | — |

### Mise en Page

:::note
Utiliser les paramètres par défaut
:::

### Style et comportement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Classe du libellé**<br />`form_lbl_class_fe` | Classe pour stylé le libellé de ce champ | `text` | — | — |
| **Classe CSS du conteneur**<br />`form_container_class_fe` | Une liste de noms de classes à ajouter au conteneur de formulaire externe | `text` | — | — |
| **CSS du formulaire**<br />`form_container_css_fe` | Vous pouvez définir quelques règles CSS qui seront appliqués au formulaire de saisie. ex: 'width:800px;'pour éviter d'avoir des problèmes de dimension en frontend. | `textarea` | — | — |
| **Ajouter du code CSS**<br />`form_extra_css_fe` | Ajouter des règles CSS supplémentaires au formulaire de soumission/modification. - Ceci peut être écrasé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | `editor` | — | — |
| **Ajouter du code JS dans le formulaire d'édition pour développeur seulement***<br />`form_extra_js_fe` | Ajouter un code JS supplémentaire au formulaire de soumission/édition. - Généralement, vous ajoutez un code JS exécuté sur l'événement DOM Ready. - N'oubliez pas de casser l'exécution JS de votre formulaire. - Cela peut être surchargé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | `editor` | — | — |

#### Formulaire de contenu (Public)

### Formulaire de contenu (Administration)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Apparence du formulaire de saisie**<br />`form_ilayout_be` | — | `fclayout` | **Dispositions intégrées**<br />`tabs` = onglets (par défaut)<br />`flat` = plat | — |

#### Formulaire de contenu (Administration)

### Paramétrage du formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Boutons optionnels**<br />`allowbuttons_be` | Sélectionner les boutons que vous souhaitez faire apparaitre dans le formulaire de saisie en frontend. | `fccheckbox` | — | — |
| **Placement des boutons**<br />`buttons_placement_be` | Selectionner pour afficher des boutons de formulaire en haut ou en bas du formulaire | `radio` | `—` = Paramètres globaux<br />`-1` = Jtoolbar<br />`0` = En haut<br />`1` = En bas<br />`2` = A gauche<br />`3` = A droite | — |

#### Affiche un message du type approbation nécessaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Dans le formulaire**<br />`approval_warning_inform_be` | Activez ceci, pour afficher un message dans le formulaire de l'élément, si l'utilisateur actuel peut publier de nouveaux éléments ou s'il peut auto-approuver les modifications aux éléments existants | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Après la soumission du formulaire**<br />`approval_warning_aftersubmit_be` | Activez ceci, pour afficher un avertissement après l'envoi du formulaire, en disant si l'approbation est nécessaire pour que le nouvel élément soit publié ou pour que les modifications de l'élément existant deviennent actives | `radio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Montrer | — |
| **Nécessite une révision de cette version**<br />`version_reviewal_msg_be` | _Veuillez noter que la **version** de votre document devra être validée par un administrateur_ | `textarea` | — | — |
| **Nécessite l'approbation du contenu**<br />`document_approval_msg_be` | _Veuillez noter que votre **nouvel article** devra être relu et accepté par un administrateur_ | `textarea` | — | — |
| **Peut nécessiter une révision de cette version**<br />`mr_version_revial_msg_be` | _Veuillez noter que la nouvelle **version** de ce document a peut-être besoin d'être vérifiée et approuvée avant publication. Cela peut dépendre de la catégorie du contenu et / ou du type du contenu. Si l'approbation est nécessaire, vous serez avisé après avoir enregistré ce contenu._ | `textarea` | — | — |
| **Peut nécessiter l'approbation du contenu**<br />`mr_document_approval_msg_be` | _Veuillez noter que votre nouveau contenu peut nécessiter une approbation avant d'être accepté. Cela peut dépendre de catégorie du contenu et/ou de type de contenu. Vous serez avisé si l'approbation est nécessaire, après avoir enregistré ce contenu._ | `textarea` | — | — |
| **Modifications appliquées immédiatement**<br />`changes_applied_immediately_msg_be` | _Veuillez noter que la gestion des versions de document est désactivée, donc toute modification que vous apportez à ce contenu sera accepté/activé immédiatement et la version précédente sera perdue_ | `textarea` | — | — |

#### Instructions / redirections d'URL / etc

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Instructions pour la saisie**<br />`submit_message_be` | Ces instructions seront placées en haut du formulaire, après les boutons **NOTE **: Cela peut être une chaîne de langue (à ajouter à vos fichiers de langue) | `textarea` | — | — |

### Compatibilité Joomla

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Éditer les liens**<br />`create_jarticle_form_links` | Créer des liens d'édition vers le formulaire d'article Joomla ou le formulaire d'élément Flexicontent | `multilist` | `0` = FC Formulaire de contenu<br />`1` = Formulaire d’article Joomla | `0` (FC Formulaire de contenu) |
| **Images intro / complètes**<br />`use_jimages_be` | Afficher les images intro/complètes | `radio` | `—` = Paramètres globaux<br />`0` = Désactiver<br />`1` = Activer | — |
| **URL**<br />`use_jurls_be` | Afficher les URL | `radio` | `—` = Paramètres globaux<br />`0` = Désactiver<br />`1` = Activer | — |

### Édition de base

#### Nouveaux / existants contenus

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le titre**<br />`usetitle_be` | Sélectionnez pour afficher ou masquer le titre de l'élément - vous pouvez définir automatiquement dans les paramètres de type | `radio` | `—` = Paramètres globaux<br />`0` = Cacher si automatique<br />`1` = Oui | — |
| **Utiliser les Alias**<br />`usealias_be` | Autoriser l'utilisateur à saisir les alias. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser le type**<br />`usetype_be` | Afficher le sélecteur de type pour permettre le changement de type d'élément | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser l'état**<br />`usestate_be` | Afficher le sélecteur d'état pour permettre le changement d'état de publication du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser l'accès**<br />`useaccess_be` | Afficher le sélecteur d'accès pour permettre de changer le niveau d'accès du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser les vedettes**<br />`usefeatured_be` | Afficher le sélecteur de vedette pour permettre le changement d'état du contenu | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Utiliser les tags**<br />`usetags_be` | Autoriser les tags a être cachés, pour les groupes qui possèdent le droit sur les tags, cela n'empêche pas après de gérer les tags | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui<br />`2` = Afficher seulement | — |
| **Autoriser la désactivation des commentaires**<br />`allowdisablingcomments_be` | Vous pouvez préciser ici si les auteurs ou les éditeurs peuvent désactiver les commentaires pour le contenu qu'ils modifient ou ajoutent. Si vous autorisez ce paramètre, il est recommandé de ne pas afficher les paramètres avancés du contenu. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

#### Catégories

:::note
Remarque : Vous avez toujours besoin des **ACL** pour éviter les changements de catégories multiples. Cacher ces dernières, n'empêche pas les utilisateurs de les modifier ...
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser la catégorie**<br />`usemaincat_be` | Si vous désactivez cette option, vous devez également définir une catégorie par défaut dans la configuration de chaque type (généralement vous allez créer une catégorie avec le même nom que le type et la définir comme par défaut) | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Catégories secondaires**<br />`show_seccats_be` | — | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Cacher si non modifiable<br />`2` = Montrer | — |
| **Catégories en vedette**<br />`show_featcats_be` | — | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Cacher si non modifiable<br />`2` = Montrer | — |

:::note
Filtrer
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Pas dans la langue de l'élément**<br />`iform_cats_not_in_itemlang_be` | Masquer les catégories dans des langues différentes de la langue de l'élément ou ajouter une langue au titre de la catégorie | `fcradio` | `—` = Paramètres globaux<br />`0` = Cacher<br />`1` = Saisir un nom de langue | — |
| **États autorisés**<br />`iform_catstates_allowed_be` | Les catégories avec des états non autorisés seront masquées, sauf si l'élément est déjà affecté à une telle catégorie | `fccheckbox` | — | — |

#### Langue

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser le langage**<br />`uselang_be` | Autoriser l'utilisateur à choisir sa langue. NOTE : Sélectionnez une langue par défaut avant de désactiver ce paramètre | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui<br />`3` = Oui, sans associations<br />`2` = Afficher seulement | — |
| **Langue par défaut**<br />`default_language_be` | C'est la langue qui sera pré-sélectionnée, particulièrement utile si vous cachez la langue | `fclanguage` | `_author_lang_` = Utiliser la langue de l'éditeur<br />`_site_default_` = Utiliser la langue par défaut du site | — |
| **Désactiver les langues**<br />`disable_languages_be` | Par exemple, vous pourriez choisir de désactiver la langue 'ALL' | `fclanguage` | — | — |

#### Sélecteur de langue

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher comme**<br />`langdisplay_be` | Vous pouvez l'afficher ex comme une liste déroulante ou des boutons radios | `radio` | `—` = Paramètres globaux<br />`2` = Sélecteur liste déroulante<br />`3` = Bouton radio | — |
| **Afficher drapeaux (radio)**<br />`langdisplay_flags_be` | Afficher les icônes drapeaux | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Montrer le texte (radio)**<br />`langdisplay_texts_be` | Activer pour afficher le texte comme un code langue | `radio` | `—` = Paramètres globaux<br />`0` = Pas de texte<br />`1` = Code de la langue<br />`2` = Titre<br />`3` = Titre natif<br />`4` = Titre + Titre natif | — |

#### Contenus existants

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser les modifications de langue**<br />`allowlangmods_be` | Permettre à l'utilisateur de modifier les propriétés de la langue pour des éléments -existant-. Habituellement, vous devriez interdire aux utilisateurs de modifier les propriétés de langue existantes comme la langue de l'élément et le contenu original de la traduction | `fccheckbox` | — | — |

:::note
Vous avez accès à plus d'option de configuration ici: Plugin de Notifications
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Autoriser la notification du propriétaire**<br />`allow_owner_notify_be` | Permettre à l'éditeur d'envoyer une notification de mise à jour (email) au propriétaire du contenu courant | `fcradio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui, un par session | — |
| **Autoriser la notification des inscrits (contenus favoris des utilisateurs)**<br />`allow_subscribers_notify_be` | Permettre à l'éditeur d'envoyer des notifications de mise à jour (emails) aux utilisateurs qui ont en favori le contenu courant | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui, un par session | — |

### Options avancées

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser les détails de publication**<br />`usepublicationdetails_be` | Sélectionnez ici pour autoriser : -Basic- Publication Details: (début & date de fin de publication & alias d'auteur) aux personnes qui peuvent -EDITER- l'élément. ou - Tous les détails de la publication : (auteur de l'élément & date de création) sont disponibles UNIQUEMENT aux utilisateurs de Super Admin. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Basique (recommandé)<br />`2` = Tous * | — |
| **Utiliser les métadonnées**<br />`usemetadata_be` | Recommandé pour masquer ou uniquement autoriser -basic- META données (description et mots-clés), le reste sera inutile pour les utilisateurs | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Basique (recommandé)<br />`2` = Tous * | — |
| **Configuration SEO**<br />`useseoconf_be` | Permettre à l'utilisateur de modifier les paramètres SEO, comme balise de titre personnalisée | `radio` | `—` = Paramètres globaux<br />`0` = Non (recommandé)<br />`1` = Oui | — |
| **Options d'affichage**<br />`usedisplaydetails_be` | Sélectionnez les groupes de paramètres que vous souhaitez rendre modifiables dans le frontend | `radio` | `—` = Paramètres globaux<br />`0` = Non (recommandé)<br />`1` = Basique<br />`2` = Avancé | — |
| **Options d'affichage d'un composant tiers**<br />`use3rdpartyparams_be` | Sélectionner pour afficher les options d'affichage des extensions tierces | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Sélection du modèle**<br />`selecttheme_be` | Activer la sélection et la configuration du modèle pour les groupes d'utilisateur de l'interface publique ayant le privilège de gestion des modèles. | `radio` | `—` = Paramètres globaux<br />`0` = Non (recommandé)<br />`1` = Sélectionner<br />`2` = Sélectionner et configurer | — |
| **Autorisations (ACL)**<br />`permsplacement_be` | Sélectionnez ici pour afficher les permissions pour l'utilisateur si celles-ci sont modifiables | `radio` | `—` = Paramètres globaux<br />`0` = Toujours masquer (même si modifiable)<br />`1` = En ligne<br />`2` = Carrousel | — |
| **Versions**<br />`versionsplacement_be` | Sélectionnez ici pour afficher la version en ligne dans une fenêtre pop-up | `radio` | `—` = Paramètres globaux<br />`0` = Toujours masquer (même si modifiable)<br />`1` = Pop-up<br />`2` = En ligne | — |

### Mise en Page

:::note
Utiliser les paramètres par défaut
:::

### Style et comportement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Classe du libellé**<br />`form_lbl_class_be` | Classe pour stylé le libellé de ce champ | `text` | — | — |
| **Classe CSS du conteneur**<br />`form_container_class_be` | Une liste de noms de classes à ajouter au conteneur de formulaire externe | `text` | — | — |
| **CSS du formulaire**<br />`form_container_css_be` | Vous pouvez définir quelques règles CSS qui seront appliqués au formulaire de saisie. ex: 'width:800px;'pour éviter d'avoir des problèmes de dimension en frontend. | `textarea` | — | — |
| **Ajouter du code CSS**<br />`form_extra_css_be` | Ajouter des règles CSS supplémentaires au formulaire de soumission/modification. - Ceci peut être écrasé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | `editor` | — | — |
| **Ajouter du code JS dans le formulaire d'édition pour développeur seulement***<br />`form_extra_js_be` | Ajouter un code JS supplémentaire au formulaire de soumission/édition. - Généralement, vous ajoutez un code JS exécuté sur l'événement DOM Ready. - N'oubliez pas de casser l'exécution JS de votre formulaire. - Cela peut être surchargé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | `editor` | — | — |

#### Formulaire de contenu (Administration)

### Formulaire de contenu (Public et administration)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Cacher la description**<br />`hide_maintext` | Masquer le champ description (texte principal) du formulaire du contenu (pas recommandé !!!). FAITES ATTENTION, vous perdrez la rétro-compatibilité avec le composants com_content pour les contenus concerés !!! | `multilist` | `0` = Montrer<br />`1` = Les deux<br />`2` = Chargement automatique dans la partie publique<br />`3` = Administration | `0` (Montrer) |

### Style et comportement

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter du code CSS**<br />`form_extra_css` | Ajouter des règles CSS supplémentaires au formulaire de soumission/modification. - Ceci peut être écrasé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | `editor` | — | — |
| **Ajouter du code JS dans le formulaire d'édition pour développeur seulement***<br />`form_extra_js` | Ajouter un code JS supplémentaire au formulaire de soumission/édition. - Généralement, vous ajoutez un code JS exécuté sur l'événement DOM Ready. - N'oubliez pas de casser l'exécution JS de votre formulaire. - Cela peut être surchargé par type de contenu (avec les autres paramètres) et permettre ainsi une personnalisation différente pour chaque type de contenu. | `editor` | — | — |

#### Fin du formulaire de contenu

## Notifications

### Notifications suite à la soumission ou au changement d’un contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer les notifications**<br />`enable_notifications` | Cette option permet d'activer l'envoi de notification automatique par email suite à la soumission ou la modification d'un contenu. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Envoyer les emails en copie cachée**<br />`nf_send_as_bcc` | Activez cette option pour empêcher les destinataires de recevoir des e-mails et de voir d'autres destinataires. **NOTE**: cela obligera l'administrateur du site à être le principal destinataire de l'e-mail de notification | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |
| **Debug des notifications**<br />`nf_enable_debug` | -- Activer ceci pour: (a) afficher les informations de débogage et aussi (b) **forcer l'envoi de notifications par e-mail sur chaque opération de sauvegarde**, -- Normalement, les notifications seront envoyées SEULEMENT (a) une fois par session pour chaque élément de contenu ou (b)**lorsque ses catégories sont modifiées**. | `radio` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | — |

#### Nouveau Contenu : Peu importe le statut (à partir des auteurs qui peuvent publier)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **États des contenus**<br />`states_notify_new` | L'email de notification sera envoyé quand le contenu aura un des états sélectionnés. | `fccheckbox` | — | — |
| **Groupes d'utilisateurs**<br />`usergrps_notify_new` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | `flexiusergroup` | — | — |
| **Id Utilisateur/liste de noms**<br />`userlist_notify_new` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | `text` | — | — |
| **Texte personnalisé**<br />`text_notify_new` | Entrez un texte supplémentaire personnalisé à inclure dans l'e-mail de notification. **NOTE**: Ceci sera filtré comme une chaîne de langue (via JText) | `textarea` | — | — |

#### Nouveau Contenu: En attente de publication (pour les auteurs qui n'ont pas le droit de publication)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Groupes d'utilisateurs**<br />`usergrps_notify_new_pending` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | `flexiusergroup` | — | — |
| **Id Utilisateur/liste de noms**<br />`userlist_notify_new_pending` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | `text` | — | — |
| **Texte personnalisé**<br />`text_notify_new_pending` | Entrez un texte supplémentaire personnalisé à inclure dans l'e-mail de notification. **NOTE**: Ceci sera filtré comme une chaîne de langue (via JText) | `textarea` | — | — |

#### Mise à jour d'un contenu: PAS BESOIN D'APPROBATION DE LA VERSION (pour les auteurs qui peuvent publier )

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **États des contenus**<br />`states_notify_existing` | L'email de notification sera envoyé quand le contenu aura un des états sélectionnés. | `fccheckbox` | — | — |
| **Groupes d'utilisateurs**<br />`usergrps_notify_existing` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | `flexiusergroup` | — | — |
| **Id Utilisateur/liste de noms**<br />`userlist_notify_existing` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | `text` | — | — |
| **Texte personnalisé**<br />`text_notify_existing` | Entrez un texte supplémentaire personnalisé à inclure dans l'e-mail de notification. **NOTE**: Ceci sera filtré comme une chaîne de langue (via JText) | `textarea` | — | — |

#### Mise à jour d'un contenu: BESOIN DE L'APPROBATION DE LA VERSION (pour les auteurs qui ne peuvent pas publier, la gestion des versions doit être activé)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Groupes d'utilisateurs**<br />`usergrps_notify_existing_reviewal` | L'email de notification sera envoyé quand l'auteur fera partie de l'un des groupes sélectionnés. | `flexiusergroup` | — | — |
| **Id Utilisateur/liste de noms**<br />`userlist_notify_existing_reviewal` | Entrez les identifiants d'utilisateur ou les noms (les noms d'utilisateur pas de noms complets) et séparez les valeurs avec des virgules | `text` | — | — |
| **Texte personnalisé**<br />`text_notify_existing_reviewal` | Entrez un texte supplémentaire personnalisé à inclure dans l'e-mail de notification. **NOTE**: Ceci sera filtré comme une chaîne de langue (via JText) | `textarea` | — | — |

## Gestionnaire de contenu

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Sous-type de contenu**<br />`is_subtype` | Les contenus de ce type ne sont pas destinés à être visibles. Au lieu de cela, ils sont destinés à être affichés à l'intérieur d'autres contenus, cela masquera le bouton de prévisualisation dans le gestionnaire d'éléments | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Désactiver les colonnes**<br />`iman_skip_cols` | Cacher définitivement les colonnes. L'utilisateur ne sera pas en mesure de les activer. Remarque : 'Type unique', signifie masquer la colonne si le filtrage par type est unique | `fccheckbox` | — | — |
| **Colonnes personnalisées**<br />`items_manager_extra_fields` | En option inclure des colonnes de champs personnalisés dans la liste des contenus. ** Remarque : ** Ne pas inclure de champs personnalisés qui ne rentre pas ou qui désorganise la liste, ** Remarque : ** Certains champs peuvent poser problème lors de l'affichage dans le backend, dans ce cas essayer d'utiliser une autre variable d'affichage (par défaut c'est 'display') OU les enlever de la liste, ** Remarque : ** Vous pouvez personnaliser cela dans toutes les configurations de type de contenu. Par contenu les types de champs seront affichés quand vous filtrez la liste du gestionnaire de contenus grâce au filtre de type de contenu. ** FORMAT : ** fieldname1, fieldname2, fieldname3:dispname3, fieldname4:dispname4, fieldname5 | `fields` | — | — |
| **Filtrage personnalisé**<br />`items_manager_custom_filters` | Sélectionnez les champs personnalisés à ajouter en tant que filtres du gestionnaire d'éléments. NOTE : le sélecteur déroulant affiche les types de champs pris en charge | `filters` | — | — |

## Modèles

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Modèle par défaut des contenus**<br />`ilayout` | Choisir un template par défaut pour tous les contenus de ce type (recommandé) **NOTE :**Chaque template a une vue contenu, donc cette liste montre le nom de chaque template. **NOTE :** Il est possible de surcharger le template du contenu dans les paramètres de chaque contenu. | `itemlayout` | — | `grid` |
| **Modèle mobile**<br />`ilayout_mobile` | Définit si un modèle mobile doit être utilisé quand le visiteur utilise un support mobile pour afficher le site, le modèle « normal » sera utilisé par défaut. Cette option permet de résoudre des problèmes de résolution | `itemlayout` | — | — |
