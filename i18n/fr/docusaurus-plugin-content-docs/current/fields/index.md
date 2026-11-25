---
sidebar_position: 1
---

# Champs

Les champs sont les types de contenus personnalisés de FLEXIcontent. Chaque type est fourni par un plugin et propose ses propres options d’édition, d’affichage, de référencement et de filtrage.

Ajoutez un champ depuis **Composants → FLEXIcontent → Champs**, puis choisissez son type. Les options disponibles dépendent du type sélectionné.

:::info Source
Ces pages sont générées depuis les manifests XML des plugins de champs et les fichiers de langue officiels anglais et français de FLEXIcontent 5.x.
:::

## Guides

- [Créer un champ](./create-a-field.md) — ajouter un champ personnalisé, choisir son type, l’associer aux types de contenu et le placer dans les formulaires et les vues.
- [Créer un type de champ](./create-a-field-type.md) — écrire un nouveau plugin `flexicontent_fields` lorsque les types existants ne peuvent pas stocker ou traiter la donnée.
- [Créer un layout de champ](./field-layouts.md) — personnaliser l’affichage de la valeur (`viewlayout`), le champ du formulaire (`formlayout`) ou une galerie d’images.

## Texte et basique

| Type | Description | Options |
| --- | --- | --- |
| [Adresse internationale / Google Maps](./addressint.md) | Ce champ ajoute les informations d'adresse aux éléments. Inclut des champs détaillés pour adresse rue, ville, état/province, code postal/… | 135 |
| [Couleur](./color.md) | Champ couleur pour Flexicontent | 129 |
| [Date / horodatage](./date.md) | Plugin de champ 'Date' pour FLEXIcontent | 137 |
| [E-mail](./email.md) | Plugin de champ 'Email' pour FLEXIcontent | 85 |
| [Liste de liens](./linkslist.md) | Plugin de champ 'Lien list' pour FLEXIcontent | 50 |
| [Numéros de téléphone internationaux](./phonenumbers.md) | Ce champ ajoute des numéros de téléphone aux contenus. Pour chaque numéro, vous pouvez ajouter un nom (ex : Bureau, Fax, etc.), un code inte… | 84 |
| [Texte](./text.md) | Plugin de champ « Texte » pour FLEXIcontent | 153 |
| [Zone de texte](./textarea.md) | Plugin de champ 'Textarea' pour FLEXIcontent | 124 |
| [Texte avec liste](./textselect.md) | Plugin de champ 'Liste de textes' pour FLEXIcontent | 154 |
| [Lien web](./weblink.md) | Plugin de champ 'Weblink' pour FLEXIcontent | 123 |

## Choix et étiquettes

| Type | Description | Options |
| --- | --- | --- |
| [Case à cocher](./checkbox.md) | Plugin de champ 'Checkbox' pour FLEXIcontent | 153 |
| [Case à cocher avec image](./checkboximage.md) | Plugin de champ 'Checkbox Image' pour FLEXIcontent | 164 |
| [Bouton radio](./radio.md) | Plugin de champ 'Radio' pour FLEXIcontent | 153 |
| [Bouton radio avec image](./radioimage.md) | Plugin de champ 'Radio Image' pour FLEXIcontent | 164 |
| [Liste déroulante](./select.md) | Plugin de champ 'Liste de sélection' pour FLEXIcontent | 150 |
| [Liste à choix multiples](./selectmultiple.md) | Plugin de champ 'Liste de sélection multiple' pour FLEXIcontent | 150 |
| [Liste de termes](./termlist.md) | FLEXI_FIELD_TERMLIST | 93 |

## Fichiers et médias

| Type | Description | Options |
| --- | --- | --- |
| [Fichier](./file.md) | Plugin de champ 'fichier' pour FLEXIcontent | 230 |
| [Image / galerie](./image.md) | Plugin de champ 'Image' pour FLEXIcontent | 193 |
| [Fichier multimédia](./mediafile.md) | FLEXI_FIELD_MEDIAFILE | 231 |
| [Vidéo / audio partagé](./sharedmedia.md) | Ce champ intègre dans les articles , un lecteur (vidéo/audio) à partir de sites de partage vidéo comme YouTube, Vimeo, Dailymotion, Vevo,… | 84 |

## Relations et utilisateurs

| Type | Description | Options |
| --- | --- | --- |
| [Compte utilisateur via le formulaire](./account_via_submit.md) | Plugin de champ 'Email' pour FLEXIcontent | 34 |
| [Contenus de l’auteur](./authoritems.md) | Plugin pour FLEXIcontent - Article de l'auteur | 17 |
| [Profil utilisateur](./jprofile.md) | Plugin de champ 'Utilisateur Joomla' pour FLEXIcontent | 60 |
| [Relation](./relation.md) | Plugin de champ pour FLEXIcontent - Relation | 185 |
| [Relation inverse](./relation_reverse.md) | Plugin de champ 'Relation Reverse' pour FLEXIcontent | 106 |

## Mise en page et structure

| Type | Description | Options |
| --- | --- | --- |
| [Commentaires](./comments.md) | FLEXIcontent - Commentaires, un plugin de commentaire via les apps Disqus et Facebook pour la vue contenu | 19 |
| [Champs cœur (Joomla)](./core.md) | Plugin des champ systèmes pour FLEXIcontent | 610 |
| [Propriété cœur](./coreprops.md) | Plugin de placement des propriétés cœur du formulaire de contenu pour FLEXIcontent. Ce champ définit l’emplacement de la propriété cœur dans le formulaire… | 85 |
| [HTML personnalisé / onglet de formulaire](./custom_form_html.md) | Plugin de marquage de groupe de champs pour FLEXIcontent. Ce champ marque le début/la fin des groupes de champs dans le formulaire de modification… | 9 |
| [Charger un module](./fcloadmodule.md) | Charger un module ou une position de module dans un contenu | 19 |
| [Navigation entre contenus](./fcpagenav.md) | Plugin de champ Navigation entre contenus pour FLEXIcontent | 38 |
| [Groupe de champs (répétable)](./fieldgroup.md) | Champs de groupe pour les plugin champ de FLEXIContent | 66 |
| [Sous-formulaire](./subform.md) | Plugin de champ de sous-formulaire pour FLEXIcontent | 125 |
| [Barre d’outils](./toolbar.md) | Plugin de champ Barre d’outils pour FLEXIcontent | 32 |
