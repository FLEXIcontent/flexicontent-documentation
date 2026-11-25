---
sidebar_position: 5
---

# Compte utilisateur via le formulaire

Plugin de champ 'Email' pour FLEXIcontent

*Plugin : `account_via_submit` — User account via submit*

:::info Source
Cette page est générée depuis `plugins/flexicontent_fields/account_via_submit/account_via_submit.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

## Édition

### Valeurs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage conditionnel**<br />`showon` | Affiché en fonction de conditions. Utilisez le format Joomla 'fieldname:value' comme par exemple album_type:2 REMARQUE: ne pas définir ce champ en obligatoire. Également DÉSACTIVER les scripts prettyCheckable / Select2 JS dans tous les champs référencés de type select*, checkbox*, radio* | `text` | — | — |
| **Obligatoire**<br />`required` | Définit si le champ doit être obligatoire dans le formulaire de saisie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Champ formulaire

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'étiquette**<br />`display_label_form` | Afficher ou masquer l'étiquette pour ce champ | `radio` | `0` = Non<br />`1` = Aligner à gauche<br />`2` = En colonne | `1` (Aligner à gauche) |
| **Etiquette**<br />`label_form` | Saisir un libellé à utiliser dans le formulaire de contenu, différent du libellé du champ utilisé en affichage | `text` | — | — |
| **Message **accès interdit****<br />`no_acc_msg_form` | Laissez vide pour utiliser le message d'**accès refusé** par défaut du système, ou saisissez un message personnalisé pour ce champ | `text` | — | — |

#### Adresse e-mail

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Longueur maximum du texte**<br />`maxlength` | Nombre maximum de caractères autorisés lors de la saisie de l'utilisateur | `text` | — | — |
| **Taille du champ**<br />`size` | Taille du champ dans le formulaire de saisie | `text` | — | `30` |
| **Attributs du champ**<br />`extra_attributes` | Saisir ici quelques attributs supplémentaires (paramètres de balises HTML) pour le champ de formulaire comme par exemple onkeypress="" onmouseover="..." somename="somevalue". Veillez à ne pas briser la syntaxe HTML du champ de formulaire | `text` | — | — |
| **Masque de saisie des valeurs & Validation**<br />`inputmask` | Paramètres à la fois pour le masque et la validation des entrées utilisateur | `multilist` | `0` = Non<br />`email` = Oui | `email` (Oui) |
| **Confirmer l’adresse e-mail**<br />`email_confirm` | Exiger que l’adresse e-mail soit saisie deux fois | `radio` | `0` = Non | `0` (Non) |

#### Propriétés optionnelles

#### Activer

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Nom complet**<br />`use_full` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Fist name**<br />`use_first` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Last name**<br />`use_last` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Gender**<br />`use_gender` | Si vous activer cette option, alors l'utilisateur aura la possibilité d'surcharger la valeur par défaut quand il modifiera les valeurs du champ dans le formulaire de saisie. | `radio` | `0` = Non | `0` (Non) |

## Création d’utilisateur / Coupons de modification

... créer de nouveaux utilisateurs et/ou leur permettre de modifier des contenus en tant qu’invités

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **L’e-mail existe**<br />`handle_existing_email` | — | `radio` | `0` = Annuler la création du contenu<br />`1` = Attribuer un nouveau contenu | `0` (Annuler la création du contenu) |

#### Contenu existant ou utilisateur connecté

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Contenus existants**<br />`display_item_owner` | — | `radio` | `0` = Non<br />`1` = Afficher les informations du propriétaire du contenu | `0` (Non) |
| **Nouveaux contenus**<br />`display_when_logged` | — | `radio` | `0` = Non<br />`1` = Afficher les informations de l’utilisateur connecté | `0` (Non) |

### Création de compte

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Créer de nouveaux comptes**<br />`create_accounts` | Créer un nouveau compte à utiliser comme propriétaire du contenu | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Groupe utilisateur (ID)**<br />`new_usertype` | — | `usergrouplist` | `—` = Par défaut de Joomla! | — |
| **Activation de l'utilisateur**<br />`useractivation` | — | `list` | `—` = Par défaut de Joomla!<br />`0` = JNONE<br />`1` = Auto-activation (lien e-mail)<br />`2` = Activation par l'administrateur | — |

#### Notifications administrateur

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Envoyer un e-mail à l'administrateur**<br />`mail_to_admin` | — | `radio` | `—` = Par défaut de Joomla!<br />`0` = Non<br />`1` = Oui | — |
| **Envoyer les emails en copie cachée**<br />`admin_send_as_bcc` | Activez cette option pour empêcher les destinataires de recevoir des e-mails et de voir d'autres destinataires. **NOTE**: cela obligera l'administrateur du site à être le principal destinataire de l'e-mail de notification | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

### Coupons de modification

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Créer / envoyer des coupons de modification**<br />`create_coupons` | Créer un coupon de modification par nouveau contenu et envoyer un e-mail avec un lien de modification direct utilisant ce coupon | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Texte de l’e-mail du coupon de modification**<br />`coupon_desc` | Texte utilisé comme corps de l’e-mail lors de l’envoi du lien de modification du contenu | `textarea` | — | `Add a custom message here` |
| **Initialisé**<br />`initialized` | Tables SQL initialisées | `hidden` | — | `0` |
