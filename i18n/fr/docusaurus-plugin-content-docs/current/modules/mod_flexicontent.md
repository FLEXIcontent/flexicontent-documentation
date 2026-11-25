---
sidebar_position: 3
---

# Contenus FLEXIcontent

FLEXIcontent fournit six modules frontend pour afficher des contenus, des catégories, des formulaires de recherche, des filtres, des cartes et des nuages d’étiquettes. Configurez un module depuis **Extensions → Modules**.

> Liste de contenu et plus, dans une position module

:::info Source
Cette page est générée depuis `modules/mod_flexicontent/mod_flexicontent.xml` et les fichiers de langue officiels de FLEXIcontent 5.x.
:::

L’option **Template** sélectionne un thème de module. Voir [Créer un thème de module](./create-a-module-theme.md) pour en ajouter un.

## Basique

#### Onglets d’affichage

### De base

### Template du module

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Template**<br />`layout` | Choisir la mise en page de votre module | `fclayout` | — | `news` |

:::note
Veuillez définir les paramètres de disposition dans l’onglet **Disposition : ...**. Les développeurs CSS/HTML doivent consulter : ** Guide des modèles personnalisés **
:::

#### Contenu en vedette/standard

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Total des contenus**<br />`count` | Le nombre total de contenu à afficher (par défaut 5) | `text` | — | `5` |
| **Contenus en vedette**<br />`count_feat` | Remarque : « Contenus en vedette » sont que les éléments NN hors Total les « Contenus en vedette » peuvent avoir des affichages différent affichage « des Contenus standard ». cela dépend des modèles, par exemple, ils peuvent être pleine largeur | `text` | — | `1` |
| **Contenus standard**<br />`count_std` | # Standard = Total # - # Vedette | `text` | — | `Total - Featured` |
| **Décalage des contenus Umod**<br />`offset_items` | Description du décalage des contenus Umod | `text` | — | `0` |

:::note
REMARQUE : pour lister les contenus avec le drapeau « en vedette », ouvrez l’onglet **Sélectionner les contenus** et choisissez la portée **Drapeau Joomla en vedette**
:::

### ItemID à utiliser

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Forcer l'ItemID du menu**<br />`itemid_force` | Cette option permet de forcer pour l'ensemble des liens des contenus. Vous pouvez utiliser celui de la page active, un celui d'un menu spécifique | `multilist` | `0` = Non<br />`1` = Actif<br />`2` = Spécifique | `0` (Non) |
| **ItemID spécifique**<br />`itemid_force_value` | Entrer l'id du lien vers le contenu dans le menu Remarque : il doit pointé vers un vue FLEXIcontent, sinon les liens SEF ne fonctionneront pas ou ils seront ignoré. | `fcmenuitem` | `—` = Cliquez pour sélectionner | — |

### Masquer/afficher le module

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Combinaison des règles**<br />`combine_show_rules` | En fonction des VUES ET/OU des règles d'expression PHP, afin de déterminer si le si le module doit s'afficher ou non. | `radio` | `OR` = OU<br />`AND` = ET | `AND` (ET) |

#### Clients

:::note
Veuillez noter que si la **mise en cache de Joomla** est activée dans **la Configuration globale de Joomla** puis - que l'option '**cache en fonction de la plateforme **' (Notez que 'la tablette' est détecté comme un 'mobile') - ou que la mise en cache de ce module est désactivée à l’intérieur de l'onglet 'Réglage avancé' alors ce paramètre sera ignoré
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher pour les clients**<br />`show_in_clients` | Sélectionner pour afficher sur les ordinateurs de bureau, tablettes, mobiles | `fccheckbox` | — | — |

#### Règles des vues (catégorie, article, etc.)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher dans les vues**<br />`show_in_views` | Sélectionner les vues dans lesquelles vous souhaitez afficher ce module. | `fccheckbox` | — | — |

#### Règles PHP

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer la règle**<br />`enable_php_rule` | Vous pouvez désactiver cette règle sans supprimer les règles saisies ci-dessous. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Code régle PHP**<br />`php_rule` | Ce code PHP sera exécuté à la fin. Il doit retourner un booléen par le biais d'un 'return'. Cela determinera si le module doit être affiché ou non. | `textarea` | — | — |

### Liste des contenus

#### Onglets de la liste des contenus

### Liste de contenu : Entête

:::note
Ici, vous pouvez activer la création d’un en-tête pour la liste des contenus. Il s’agit généralement des informations de catégorie. REMARQUE : la liste de catégorie affichera les contenus de la catégorie juste sous les informations de catégorie. REMARQUE : pour créer une liste de catégorie sans contenus, définissez le nombre de contenus affichés à ZÉRO
:::

### Statistiques

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le nombre total d'éléments**<br />`show_found_items` | Affiche le nombre total d'élément à afficher. Si la configuration par catégorie est activée, alors ce sera calculés par catégorie | `multilist` | `0` = Non<br />`1` = Ligne de séparation<br />`2` = À côté du titre | `0` (Non) |

### Catégories

:::note
-La liste catégorie affiche une liste des contenus de la catégorie juste en dessous des informations de la catégorie - Pour créer une liste de catégorie sans contenu, définissez le nombre de contenu affichés à zéro
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Appliquer la configuration par catégorie**<br />`apply_config_per_category` | Créer une liste de catégories. **a. Pour créer une liste de catégories sans contenus**, définissez le nombre de contenus à 0. **b. Pour afficher 5 contenus pour chaque catégorie** définissez le nombre de contenus à 5. **Remarque :** L'affichage des données des catégories est possible seulement si vous avez défini dans les critères de sélection des contenus par catégorie soit : (a) **Inclure une liste de catégories statiques** ou soit (b) la catégorie **active** | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Passer les catégories si elles sont vides**<br />`skip_category_if_noitems` | Permettre d'ignorer les informations d'une catégorie si elle ne contient aucun contenu | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Ordre de la liste de catégorie**<br />`cats_orderby` | Ordre la liste des catégories, les options disponibles dépendent des propriétés de l'ensemble des catégories ex le nom, l'ordre configuré dans l'administration, etc | `list` | `—` = Paramètres globaux<br />`date` = Les plus anciens<br />`rdate` = Plus récents en premier<br />`modified` = Derniers modifiés en premier<br />`alpha` = Titre par ordre alphabétique<br />`ralpha` = Titre par ordre anti-alphabétique<br />`author` = Nom des auteurs<br />`rauthor` = Nom des auteurs (inversé)<br />`hits` = Les plus consultés<br />`rhits` = Les moins consultés<br />`order` = Attribut d'ordre des catégories | `order` (Attribut d'ordre des catégories) |

#### Affichage des informations des catégories

#### Titre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Titre**<br />`cats_showtitle` | Afficher/Masquer le titre de la catégorie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Ajouter un lien sur le titre**<br />`cats_link_title` | Ajouter un lien sur le titre de la catégorie permettant d'accéder à la vue complète de cette catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Longueur Max du titre**<br />`cats_cuttitle` | Longueur Max du titre.0 pour illimité | `text` | — | `40` |

#### Description

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la description**<br />`cats_showdescr` | Afficher la description de la catégorie | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Supprimer HTML & tronquer le texte**<br />`cats_do_cutdescr` | Supprimer toutes les balises HTML du texte et tronquer le texte en fonction du nombre de caractère maximum. | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Longueur maximum du texte**<br />`cats_cutdescr` | Tronquer automatiquement le texte après x caractères. Remarque : Le code HTML sera automatiquement supprimé du texte. | `text` | — | `100` |
| **Ajouter un lien 'Voir tous'**<br />`cats_readmore` | Activer pour afficher un lien 'Voir tous' pour afficher la vue complète de la catégorie. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'image**<br />`cats_show_image` | Extraire la première image de la description de la catégorie ou bien utiliser l'image des paramètres de la catégorie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Source de l'image de la catégorie**<br />`cats_image_source` | Sélectionner la source de l'image. Vous pouvez choisir l'image définie dans les paramètres de la catégorie (si elle est disponible) ou bien extraire automatiquement la première image trouvée dans la description. | `radio` | `0` = Extraire de la description<br />`1` = Utiliser l'image des paramètres<br />`2` = Essayer les paramètres, puis extraire de la description | `0` (Extraire de la description) |
| **Ajouter un lien sur l'image**<br />`cats_link_image` | Ajouter un lien sur l'image de la catégorie. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Méthode de traitement**<br />`cats_image_method` | Méthode de traitement | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |
| **Largeur de l'image**<br />`cats_image_width` | Largeur de l'image | `text` | — | `110` |
| **Hauteur de l'image**<br />`cats_image_height` | Hauteur de l'image | `text` | — | `110` |

### Catégorie active (vue contenu uniquement)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Affichage personnalisée pour catégorie active**<br />`currcat_custom_display` | Quand activé, L'affichage de la catégorie de l'élément affiché pourra être **différent** des autres catégories. L'apparence peut être personnalisée par les paramètres suivants | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **La catégorie actuelle est**<br />`currcat_source` | Sélectionner la catégorie considérée comme actuelle | `radio` | `0` = Catégorie du contenu dans la vue contenu<br />`1` = Catégorie active dans la vue catégorie<br />`2` = Les deux | `0` (Catégorie du contenu dans la vue contenu) |
| **Catégorie principale par défaut**<br />`currcat_fallback_maincat` | Si un id de catégorie courante n'est pas initialisé dans l'URL, alors la catégorie principale de l'élément courant sera utilisée | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Affichage des informations de la catégorie

#### Titre

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Titre**<br />`currcat_showtitle` | Afficher/Masquer le titre de la catégorie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Ajouter un lien sur le titre**<br />`currcat_link_title` | Ajouter un lien sur le titre de la catégorie permettant d'accéder à la vue complète de cette catégorie | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Longueur Max du titre**<br />`currcat_cuttitle` | Longueur Max du titre.0 pour illimité | `text` | — | `20` |

#### Description

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la description**<br />`currcat_showdescr` | Afficher la description de la catégorie | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Supprimer HTML & tronquer le texte**<br />`currcat_do_cutdescr` | Supprimer toutes les balises HTML du texte et tronquer le texte en fonction du nombre de caractère maximum. | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Longueur maximum du texte**<br />`currcat_cutdescr` | Tronquer automatiquement le texte après x caractères. Remarque : Le code HTML sera automatiquement supprimé du texte. | `text` | — | `100` |
| **Ajouter un lien 'Voir tous'**<br />`currcat_readmore` | Activer pour afficher un lien 'Voir tous' pour afficher la vue complète de la catégorie. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |

#### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l'image**<br />`currcat_show_image` | Extraire la première image de la description de la catégorie ou bien utiliser l'image des paramètres de la catégorie. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Source de l'image**<br />`currcat_image_source` | Sélectionner la source de l'image. Vous pouvez aussi choisir un champ image (s'il y en a au moins un de disponible) ou automatiquement extraire l'image de la description. | `list` | `0` = Extraire de la description<br />`1` = Utiliser l'image des paramètres<br />`2` = Essayer les paramètres, puis extraire de la description | `0` (Extraire de la description) |
| **Ajouter un lien sur l'image**<br />`currcat_link_image` | Ajouter un lien sur l'image de la catégorie. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Méthode de traitement**<br />`currcat_image_method` | Méthode de traitement | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |
| **Largeur de l'image**<br />`currcat_image_width` | Largeur de l'image | `text` | — | `110` |
| **Hauteur de l'image**<br />`currcat_image_height` | Hauteur de l'image | `text` | — | `110` |

### Liste de contenus : basique (ordre, ignoré, etc.)

:::note
Les options standart de la liste de contenus (qui sont pris en charge par tous les modèles), comme: le nombre d'articles, l'ordre, sauter les contenus indésirables qui ont une valeur vide sur des champs spécifiques, etc
:::

### Classer par

#### Ordre du contenu (niveau 1)

:::note
Pour utiliser les tris par contenus programmés / expirés, activez l’option d’ignorance des dates de programmation / d’expiration dans l’onglet **Sélectionner les contenus**
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Groupes de tri (*)**<br />`ordering` | Sélectionner dans quel ordre les contenus doivent apparaitre. * Vous pouvez sélectionner plusieurs ordres, une liste de contenu sera créé pour chaque ordre, mais attention un contenu pourra alors apparaitre plusieurs fois. | `fcordering` | — | `added` |
| **Afficher le titre pour chaque groupe de tri.**<br />`ordering_addtitle` | Cette option permet d'ajouter un titre pour chaque groupe de tri, cette option est recommandé si vous avez sélectionné plusieurs critères de tri. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

#### Tri par champ personnalisé

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Champ personnalisé**<br />`orderbycustomfieldid` | Sélectionnez un champ personnalisé à utiliser pour l'ordre, **REMARQUE** : vous devez sélectionner/activer l'ordonnancement du champ personnalisé. **REMARQUE :** : certains types de champs ne peuvent pas être ordonnés (champs fichiers et images par exemple). | `fields` | — | `0` |
| **Sens du tri**<br />`orderbycustomfielddir` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `radio` | `ASC` = Croissant<br />`DESC` = Décroissant | `ASC` (Croissant) |
| **Méthode de tri**<br />`orderbycustomfieldint` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `radio` | `0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date<br />`4` = Nombre de téléchargement | `0` (Texte) |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

#### Ordre du contenu (niveau 2)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Trier par champ/propriétés du noyau**<br />`ordering_2nd` | Trier les éléments par des champs/propriétés du noyau | `fcordering` | — | `alpha` |

#### Classement personnalisé des champs

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Activer *** surcharge l'ordre du noyau****<br />`orderbycustomfield_2nd` | Force l'ordre de tri avec le champ choisi. Remarque : paramètre ignoré si aucun champ personnalisé n'est sélectionné | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Champ personnalisé**<br />`orderbycustomfieldid_2nd` | Sélectionnez un champ personnalisé à utiliser pour l'ordre, **REMARQUE** : vous devez sélectionner/activer l'ordonnancement du champ personnalisé. **REMARQUE :** : certains types de champs ne peuvent pas être ordonnés (champs fichiers et images par exemple). | `fields` | — | `0` |
| **Sens du tri**<br />`orderbycustomfielddir_2nd` | Sélectionner si vous souhaiter afficher les contenus dans un ordre croissant ou décroissant. | `radio` | `ASC` = Croissant<br />`DESC` = Décroissant | `ASC` (Croissant) |
| **Méthode de tri**<br />`orderbycustomfieldint_2nd` | Sélectionner pour classer en fonction d'un texte alphanumérique (ordre du dictionnaire) ou numérique ('1000 articles' est placé après '200 années') | `radio` | `0` = Texte<br />`1` = Entier<br />`2` = Virgule flottante<br />`3` = Date<br />`4` = Nombre de téléchargement | `0` (Texte) |

:::note
Veillez noter que: l'ordre **'Nombre de téléchargement'** à besoin d'un champ **fichier**
:::

### Gestion des contenus avec champs vides

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ignorer les contenus**<br />`skip_items` | Ignorer les contenus avec des champs vides. **Remarque :** En fonction de vos données, cette fonction peut avoir un léger impact sur les performances. | `multilist` | `0` = Non<br />`1` = Oui, vérifie les valeurs manquantes (plus rapide)<br />`2` = Oui, vérifie les valeurs nulles (plus lent) | `0` (Non) |
| **Liste des champs à vérifier**<br />`skiponempty_fields` | Champs pour interroger si vide en sautant des contenus. Remarque 1 : les champs ne doivent produire AUCUNE SORTIE HTML pour que cela fonctionne | `fields` | — | — |
| **Nb. maximum de contenus à ignorer**<br />`maxskipcount` | Nombre maximum de contenus à ignorer, pour des raisons de performance les valeurs au dessus de 100 seront ignorées. | `text` | — | `50` |
| **Combinaison des champs vides**<br />`onempty_fields_combination` | Ignorer les contenus sur n'importe quel champ vide, ou bien si tous les champs sont vides. | `radio` | `any` = Au moins un champ<br />`all` = Tous les champs | `any` (Au moins un champ) |
| **Supprimer HTML pour les champs vides**<br />`striptags_onempty_fields` | Cette option permet de supprimer les tags HTML afin d'épurer le champ et le considérer comme vide. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Liste des articles : Sélection

:::note
--TOUT-- les filtrages sont nécessaires Remarque : (a) le comportement STATIQUE affichera LES MEMES ELEMENTS INDEPENDAMMENT de l'élément courant/ la page courante, (b) le comportement DYNAMIQUE affichera LES ELEMENTS QUI DEPENDENT de la vue courante (ex ELEMENT COURANT) ou autre donnée dynamique (ex date serveur)
:::

### Filtrage simple

#### Portée du contenu en cours

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode**<br />`method_curitem` | Tout: Afficher tous les éléments incluant l'élément courant. Exclus: Afficher tous les éléments excepté l'élément courant, Inclus (seulement le courant): Afficher les champs uniquement pour l'élément courant. **Veuillez utiliser la mise en page « actualités » ou une équivalente.** | `multilist` | `0` = Tous<br />`1` = Exclure<br />`2` = Inclure (actif uniquement) | `0` (Tous) |

#### Langue active

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode**<br />`method_curlang` | Tous: Affiche tous les contenus peu importe la langue. Exlure: Affiche les contenus qui ne correspondent pas à la langue active. Inclure (active uniquement): Affiche les contenus de langue active uniquement. | `multilist` | `0` = Tous<br />`1` = Exclure<br />`2` = Inclure (actif uniquement) | `0` (Tous) |

#### Favoris (en fonction de l'utilisateur connecté)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode**<br />`method_curuserfavs` | Tous : Afficher tous les article (s) quel que soit en favori ou pas. Exclure : Affichage les article (s) sauf les favoris. Inclure : Affichage article (s) favoris de l’utilisateur actuellement connecté | `multilist` | `0` = Tous<br />`1` = Exclure<br />`2` = Inclure | `0` (Tous) |

#### Contenus en vedette

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode**<br />`method_featured` | Tous: Affiche tous les contenus. Exclure : Affiche tous les contenus sauf deux en vedette. Inclure : Affiche uniquement les contenus en vedette. | `multilist` | `0` = Tous<br />`1` = Exclure<br />`2` = Inclure | `0` (Tous) |

#### Etat de publication

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode**<br />`method_states` | Normal : Tous les contenus publiés. Exclure : afficher tous les contenus sauf ceux qui ont un des états de publication sélectionnés. Inclure : Affiche uniquement les contenus qui ont un des états de publication sélectionnés. | `multilist` | `0` = Normal (Publié)<br />`1` = Exclure<br />`2` = Inclure | `0` (Normal (Publié)) |
| **Etats de publication**<br />`item_states` | Sélectionner les états de publication que vous souhaitez inclure ou exclure. | `fcitemstate` | — | — |
| **Lister tout (via les ACL)**<br />`use_list_items_in_any_state_acl` | Activer cette option permet d'élever les privilèges utilisateurs (Privilège ACL : 'Afficher la liste des contenus avec tous les statuts) ainsi que le super admin pour qu'ils puissent afficher tous les articles quelque soit leur statuts et aussi quelque soit leur date d'expiration ou de programmation. Note les utilisateurs sans le privilège ACL 'Afficher la liste des contenus avec tous les status', ne pourront pas voir ces contenus. Néanmoins, vous voudrez peut-être attribuer à ce module un niveau d’accès spécial | `multilist` | `—` = Paramètres globaux<br />`0` = Non<br />`1` = Oui | `0` (Non) |

#### Contenu programmé ou expiré

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ignorer les dates expirées/programmées**<br />`ignore_up_down_dates` | Vous pouvez choisir d'ignorer les dates de publication début / fin, y compris les contenus dont la publication est programmée (date de publication dans le futur) et / ou les contenus arrivés à expiration (date de publication antérieure passée). Ceci peut être combiné avec le filtrage de type DATE pour donner un résultat plus pertinent. REMARQUE : vous pouvez ne pas ajouter de liens à ces contenus, car ils ne seront pas visibles ou qu’ils ont expiré ou sont planifiés. Pratique pour montrer des informations sur les contenus à venir (planifiés) ou sur les contenus passés (expirés) | `multilist` | `0` = Non<br />`1` = Programmé (publication programmée)<br />`2` = Expiré (fin de publication)<br />`3` = Les deux | `0` (Non) |

#### Tags

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode**<br />`method_tags` | Vous pouvez définir ici si vous souhaitez inclure ou exclure des catégories. Seuls les tags des contenus associés à ces catégories seront donc afficher ou masquer. | `multilist` | `1` = Tous<br />`2` = Exclure<br />`3` = Inclure | `1` (Tous) |
| **Sélectionner les tags**<br />`tag_ids` | Sélectionner les tags que vous souhaitez inclure ou exclure. | `tags` | — | — |
| **Requiert TOUS les tags**<br />`tag_combine` | Sélectionnez si les contenus listés doivent être affectés à TOUTES les mots clés sélectionnés | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Filtrage avancé

#### Catégories

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comportement (**)**<br />`behaviour_cat` | Comportement statique : **ignore le contenu actuellement visualisé** et utilise seulement les paramètres pour **afficher les données dans toutes les vues**. Comportement dynamique : compare les contenus à **le contenu actuellement affiché** et donc **cela affiche uniquement les données dans les vues de contenus**, cela peut ou non utiliser certains paramètres | `multilist` | `0` = STATIQUE :: Ignorer la page actuellement affichée, et utiliser des choix spécifiques<br />**Comportement dynamique (comparer à l'élément courant)**<br />`1` = Contenus de la même catégorie<br />`2` = Contenus d'une catégorie différente<br />**Comportement dynamique (comparer à la catégorie courante(s))**<br />`3` = Contenus de la catégorie(s) active<br />`4` = Contenus de la catégorie(s) inactive | `0` (STATIQUE :: Ignorer la page actuellement affichée, et utiliser des choix spécifiques) |
| **Méthode statique**<br />`method_cat` | Ceci est utilisé par les comportements statiques et ignoré par les comportements dynamiques. **REMARQUE :** ces comportements dynamiques sont toujours actifs ! | `multilist` | `1` = Tous<br />`2` = Exclure<br />`3` = Inclure | `1` (Tous) |
| **Catégories**<br />`catids` | Veuillez sélectionner les catégories à inclure ou à exclure en fonction du paramètre ci-dessus. | `flexicategories` | — | — |
| **Necessite toutes les catégories**<br />`cat_combine` | Sélectionnez si les contenus listés doivent être affectés à TOUTES les catégories sélectionnées | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Catégories supplémentaires**<br />`treeinclude` | Inclure les parents/enfants des catégories sélectionnées. **NOTE**: 'autre catégories du contenu' est utilisé uniquement sur le site (frontend) pour l'affichage d'un contenu | `list` | `0` = Aucun<br />`1` = Catégories enfants<br />`5` = Catégories enfants, mais exclure les catégories sélectionnées<br />`2` = Catégories parentes<br />`3` = Catégories parentes & enfants<br />`4` = Autre catégories du contenu | `0` (Aucun) |
| **Lien de contenu via la catégorie principale**<br />`link_via_main` | Les liens vers les contenus seront construits via la catégorie principale, en utilisant l'alias de la catégorie ou l'alias de lien vers le contenu dans un menu | `radio` | `0` = Aucun élément sélectionné<br />`1` = Oui | `0` (Aucun élément sélectionné) |

#### Types

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comportement (**)**<br />`behaviour_types` | Comportement statique : **ignore le contenu actuellement visualisé** et utilise seulement les paramètres pour **afficher les données dans toutes les vues**. Comportement dynamique : compare les contenus à **le contenu actuellement affiché** et donc **cela affiche uniquement les données dans les vues de contenus**, cela peut ou non utiliser certains paramètres | `multilist` | `0` = STATIQUE :: Ignorer la page actuellement affichée, et utiliser des choix spécifiques<br />**Comportement dynamique (comparer à l'élément courant)**<br />`1` = Contenus du même type<br />`2` = Contenus d'un type différent | `0` (STATIQUE :: Ignorer la page actuellement affichée, et utiliser des choix spécifiques) |
| **Méthode statique**<br />`method_types` | Ceci est utilisé par les comportements statiques et ignoré par les comportements dynamiques. **REMARQUE :** ces comportements dynamiques sont toujours actifs ! | `multilist` | `1` = Tous<br />`2` = Exclure<br />`3` = Inclure | `1` (Tous) |
| **Types**<br />`types` | Sélectionner ici les types à inclure ou à exclure. | `types` | — | — |

#### Auteur / Mes contenus

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comportement (**)**<br />`behaviour_auth` | Comportement statique : **ignore le contenu actuellement visualisé** et utilise seulement les paramètres pour **afficher les données dans toutes les vues**. Comportement dynamique : compare les contenus à **le contenu actuellement affiché** et donc **cela affiche uniquement les données dans les vues de contenus**, cela peut ou non utiliser certains paramètres | `multilist` | `0` = STATIQUE :: Ignorer la page actuellement affichée, et utiliser des choix spécifiques<br />**Comportement dynamique (comparer à l'élément courant)**<br />`1` = Contenus du même auteur<br />`2` = Contenus d'auteurs différents<br />`3` = Contenus de l'utilisateur connecté (=Mes contenus) | `0` (STATIQUE :: Ignorer la page actuellement affichée, et utiliser des choix spécifiques) |
| **Méthode statique**<br />`method_auth` | Ceci est utilisé par les comportements statiques et ignoré par les comportements dynamiques. **REMARQUE :** ces comportements dynamiques sont toujours actifs ! | `multilist` | `1` = Tous<br />`2` = Exclure<br />`3` = Inclure | `1` (Tous) |
| **Auteurs**<br />`authors` | Vous pouvez saisir ici les auteurs que vous souhaitez inclure ou exclure. Saisir les id des auteurs séparés par une virgule. | `text` | — | — |

#### Contenus

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comportement (**)**<br />`behaviour_items` | Comportement statique : **ignore le contenu actuellement visualisé** et utilise seulement les paramètres pour **afficher les données dans toutes les vues**. Comportement dynamique : compare les contenus à **le contenu actuellement affiché** et donc **cela affiche uniquement les données dans les vues de contenus**, cela peut ou non utiliser certains paramètres | `multilist` | `0` = STATIQUE :: Ignorer la page actuellement affichée, et utiliser des choix spécifiques<br />**Comportement dynamique (comparer à l'élément courant)**<br />`1` = Contenus avec des étiquettes en commun<br />`2` = Eléments connexe (champ de relation)<br />`3` = Eléments connexes inversés (champ de relation) | `0` (STATIQUE :: Ignorer la page actuellement affichée, et utiliser des choix spécifiques) |
| **Tags à exclure**<br />`excluded_tags` | Sélectionner les tags que vous ne souhaitez pas utiliser via l'option 'Contenus avec des étiquettes en commun' | `tags` | — | — |
| **Champ(s) de relation**<br />`relitems_fields` | Sélectionnez le(s) champ(s) de relation (utilisé pour le comportement: Eléments connexes inversés / Eléments connexes via le champ de relation) | `fields` | — | — |
| **Méthode statique**<br />`method_items` | Ceci est utilisé par les comportements statiques et ignoré par les comportements dynamiques. **REMARQUE :** ces comportements dynamiques sont toujours actifs ! | `multilist` | `1` = Tous<br />`2` = Exclure<br />`3` = Inclure | `1` (Tous) |
| **Contenus**<br />`items` | Vous pouvez saisir ici les contenus que vous souhaitez inclure ou exclure. Saisir les id des contenus séparés par une virgule. | `text` | — | — |
| **Utiliser l'ordre ci-dessus**<br />`items_use_order` | Au lieu de l'ordre configuré, vous pouvez utiliser l’ordre des contenus spécifié ci-dessus | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |

### Filtrage expert

### Dates

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comportement (***) veuillez lire la description**<br />`behaviour_dates` | Comportement statique: compare les dates des articles DE/A à la date choisie dans les paramètres et **affiche une liste de contenus**. Comportement dynamique : compare les **dates de l’élément actuellement visualisé** ou ** la date actuelle du serveur** (par exemple la date du contenu actuellement visualisé -2 semaines, ou par exemple la semaine précédente de l’heure actuelle du serveur) - Si on utilise la comparaison avec la date de l'article actuellement visualisé, il **n'affichera des données que sur la vue contenu unique** - Si on utilise la comparaison avec le temp du serveur il **affichera les données dans toutes les vues,** | `multilist` | `0` = Statique: dates spécifiques De/A expressions de date<br />**Comportement dynamique (...)**<br />`1` = DE/A décalage personnalisé (modifie 'Comparer avec une date DYNAMIQUE')<br />**Comportement dynamique (même ...)**<br />`8` = même jour<br />`2` = Même mois<br />`3` = Même année<br />**Comportement dynamique (... précédent)**<br />`9` = Jour précédent<br />`4` = Mois précédent<br />`5` = Année précédente<br />**Comportement dynamique (... suivant)**<br />`10` = Jour suivant<br />`6` = Mois suivant<br />`7` = Année suivante<br />**Comportement dynamique (ignore l'année)**<br />`11` = Même jour du mois (1-31)<br />`12` = [-3,+4] jours du mois<br />`13` = Même semaine du mois (1,4)<br />`14` = Même semaine de l'année (1-53)<br />`15` = Même mois de l'année (1-12)<br />**Comportement dynamique (ignore le mois / l'année)**<br />`16` = Même jour du mois (1-31)<br />`17` = [-3,+4] jours du mois<br />`18` = Même semaine du mois (1,4) | `0` (Statique: dates spécifiques De/A expressions de date) |

#### Comportements dynamiques: Comparer à la date serveur ou à l'élément courant

#### Comportement statique: Dates spécifiques ... ou décalage personnalisé pour les comportements dynamiques

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Méthode**<br />`method_date_dyn_ignored` | Description de la méthode dynamique | `multilist` | `1` = Inclure | `1` (Inclure) |
| **Méthode statique**<br />`method_dates` | Ceci est utilisé par les comportements statiques et ignoré par les comportements dynamiques. **REMARQUE :** ces comportements dynamiques sont toujours actifs ! | `multilist` | `1` = Tous<br />`2` = Exclure<br />`3` = Inclure | `1` (Tous) |
| **DONNÉES de date à utiliser dans la comparaison**<br />`date_type` | Les éléments listés seront comparés en utilisant ces DONNÉES de date. **NOTE**: Elles sont utilisées à la fois dans le comportement statique et les comportements dynamiques | `multilist` | `0` = Création<br />`1` = Modification<br />`2` = Publier<br />`4` = Dépublier<br />`3` = Champ date | `0` (Création) |
| **Champ date**<br />`datecomp_field` | Pour activer, initialisez le paramètre 'DONNÉES de date' ci-dessus à 'Champ date'. **Remarque :** Si le champ a des valeurs multiples, seule la première valeur du champ date sera utilisée | `fields` | — | — |
| **Nul / dates vides**<br />`nulldates` | Sélectionner pour inclure/exclure les dates dont les valeurs sont vides ou nules | `radio` | `0` = Exclure<br />`1` = Inclure | `0` (Exclure) |
| **Premier jour de la semaine**<br />`week_start` | Sélectionnez le premier jour de la semaine | `radio` | `0` = Dimanche<br />`5` = Lundi | `0` (Dimanche) |

:::note
Décalages personnalisés appliqués à la date dynamique, ex. -5 j (moins 5 jours) - pour saisir la **date actuelle (maintenant)**, utilisez : 0 j
:::

:::note
Comparer à des dates précises (AAAA-MM-JJ), ex. 2015-01-23 - pour saisir la **date actuelle (maintenant)**, utilisez : CURDATE() &gt; , et définissez le type de date sur « expression SQL de date »
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **De**<br />`bdate` | Si vous souhaitez un comportement avec une chaine statique, saisir une date au format MySQL (YYYY-MM-DD). Si vous souhaitez un comportement avec une chaine dynamique, vous pouvez utiliser les paramètres suivants : 'd' pour les jours, 'm' pour les mois et 'Y' pour les années. P. ex : -5 d (5 jours avant aujourd'hui) | `fcdate` | — | — |
| **À**<br />`edate` | Si vous souhaitez un comportement avec une chaine statique, saisir une date au format MySQL (YYYY-MM-DD). Si vous souhaitez un comportement avec une chaine dynamique, vous pouvez utiliser les paramètres suivants : 'd' pour les jours, 'm' pour les mois et 'Y' pour les années. P. ex. : 3 d (3 jours après aujourd'hui) | `fcdate` | — | — |
| **Date de début**<br />`raw_bdate` | Détail de la fonctionnalité et des possibilités: (a) **Chaîne :** ex statique : 2012-04-23 ex dynamique: maintenant moins 3 heures = -3 h (b) **Expression** ex : la journée précédente à 20h00 = ADDTIME( CAST(ADDDATE(CURDATE(), -1) AS DATETIME) , '0 20:00:00') ex : aujourd'hui à 20h00 = ADDTIME( CAST(CURDATE() AS DATETIME),'0 20:00:00') | `radio` | `0` = Date spécifiques<br />`1` = Expression SQL date | `0` (Date spécifiques) |
| **Date de fin**<br />`raw_edate` | Détail de la fonctionnalité et des possibilités: (a) **Chaîne :** ex statique : 2012-04-23 ex dynamique: maintenant moins 3 heures = -3 h (b) **Expression** ex : la journée précédente à 20h00 = ADDTIME( CAST(ADDDATE(CURDATE(), -1) AS DATETIME) , '0 20:00:00') ex : aujourd'hui à 20h00 = ADDTIME( CAST(CURDATE() AS DATETIME),'0 20:00:00') | `radio` | `0` = Date spécifiques<br />`1` = Expression SQL date | `0` (Date spécifiques) |
| **Comparer avec une date DYNAMIQUE**<br />`date_compare` | Choisissez si vous voulez comparer les DONNÉES de date dynamique soit avec (a) la date courante du serveur ou (b) la date de l'élément courant | `radio` | `0` = Date serveur courante<br />`1` = Données de la date du contenu courant | `0` (Date serveur courante) |

### Champs personnalisés (non-Core)

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Comportement (**)**<br />`behaviour_filt` | Comportement statique : **ignore le contenu actuellement visualisé** et utilise seulement les paramètres pour **afficher les données dans toutes les vues**. Comportement dynamique : compare les contenus à **le contenu actuellement affiché** et donc **cela affiche uniquement les données dans les vues de contenus**, cela peut ou non utiliser certains paramètres | `multilist` | `0` = Statique: Filtrer en utilisant les valeurs de champs spécifiques<br />`1` = Dynamique: Filtrer en utilisant les valeurs des champs de l'élément courant<br />`2` = Dynamique + Statique: Filtrer par les 2 | `0` (Statique: Filtrer en utilisant les valeurs de champs spécifiques) |
| **Filtres dynamiques (vue élément uniquement)**<br />`dynamic_filters` | Ces filtres appliquent un filtre DYNAMIC qui compare à l'élément courant et donc la liste d'éléments contient des éléments qui ont des valeurs de champ identiques à l'élément courant. ** Remplir ainsi: ** id_champ1,id_champ2,id_champ3 | `textarea` | — | — |
| **Méthode statique**<br />`method_filt` | Ceci est utilisé par les comportements statiques et ignoré par les comportements dynamiques. **REMARQUE :** ces comportements dynamiques sont toujours actifs ! | `multilist` | `1` = Tous<br />`2` = Exclure<br />`3` = Inclure | `1` (Tous) |
| **Filtres statiques (toutes les vues)**<br />`static_filters` | Ces filtres appliquent un filtrage STATIC, quel que soit l'élément en cours d'affichage. Entrez : field_id##value %% field_id##value Exemple : 22##14 %% 47##some field value %% 19##someword - **Valeurs uniques**: field_id##value1 **Ranges**: field_id##value1---valeur2 - **Valeurs multiples**: field_id##value1++++++++valeur3 - **Relation / Reverse-relation**: REL_field_id##REL_field_id~~value1 | `textarea` | — | — |

### Pied de page

:::note
Normalement ce module génère une liste de contenus/catégories. Vous pouvez ici sélectionner quelques options supplémentaires pour le pied de page.
:::

### Favoris récement ajoutés

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Liste des favoris récents**<br />`display_favlist` | Afficher une liste des favoris (titre + lien) récemment ajoutés (dans la session active). Remarque : Cette option peut être combiné avec les critères de sélection 'Favoris' afin d'afficher tous les favoris de l'utilisateur (avec une présentation plus détaillée) | `radio` | `0` = Cacher<br />`1` = Afficher | `0` (Cacher) |

### Lire lire la suite en pide de page

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher 'Plus d'informations'**<br />`show_more` | Afficher un lien en bas du module vers une URL spécifique. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Titre**<br />`more_title` | Texte utilisé pour 'Plus d'informations'. ** Laisser vide pour utiliser la valeur par défaut:** | `text` | — | — |
| **Lien**<br />`more_link` | Lien | `text` | — | `index.php` |
| **Ouvrir dans une nouvelle fenêtre in new window**<br />`more_blank` | Ouvrir le lien dans une nouvelle fenêtre/onglet. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **CSS personnalisé**<br />`more_css` | Code CSS à utiliser pour le lien 'Plus d'informations' au bas du module. | `textarea` | — | — |

#### Onglets de la liste des contenus

### Mise en page : Options de la mise en page selectionnée

### Gestion du contenu via paramètres

:::note
Il s’agit de la configuration d'un affichage qui va répété **chaque contenu répertorié**. Il est disponible à tous les modèles, mais tous les modèles n'en feront pas usage
:::

### Titre

#### Standard

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le titre**<br />`display_title` | Permet d'afficher ou de masquer le titre | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Ajouter un lien sur le titre**<br />`link_title` | Ouvre le contenu lorsqu'on clique sur le titre | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Longueur Max du titre**<br />`cuttitle` | Longueur Max du titre.0 pour illimité | `text` | — | `40` |

#### En vedette

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher le titre**<br />`display_title_feat` | Permet d'afficher ou de masquer le titre | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Ajouter un lien sur le titre**<br />`link_title_feat` | Ouvre le contenu lorsqu'on clique sur le titre | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Longueur Max du titre**<br />`cuttitle_feat` | Longueur Max du titre.0 pour illimité | `text` | — | `40` |

### Description

#### Standard

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la description**<br />`display_text` | Afficher le texte de description | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Supprimer HTML & tronquer le texte**<br />`mod_do_stripcat` | Supprimer toutes les balises HTML du texte et tronquer le texte en fonction du nombre de caractère maximum. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Longueur maximum du texte**<br />`mod_cut_text` | Tronquer automatiquement le texte après x caractères. Remarque : Le code HTML sera automatiquement supprimé du texte. | `text` | — | `100` |
| **Afficher 'lire la suite'**<br />`mod_readmore` | Afficher/masquer le boutton 'lire la suite' | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Readmore align**<br />`readmore_align_std` | Nombre de colonnes pour le contenu. NOTE : c'est la valeur maximale, le nombre de colonne affichées dépendra de la largeur de la fenêtre du navigateur | `radio` | `left` = A gauche<br />`center` = Centre<br />`right` = A droite | `center` (Centre) |
| **Classe du bouton**<br />`readmore_class_std` | Ajoutez votre classe CSS ; readon btn feat par défaut _readon btn std_ | `text` | — | — |

#### En vedette

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la description**<br />`display_text_feat` | Afficher le texte de description | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Supprimer HTML & tronquer le texte**<br />`mod_do_stripcat_feat` | Supprimer HTML & tronquer le texte | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Longueur maximum du texte**<br />`mod_cut_text_feat` | Tronquer automatiquement le texte après x caractères. Remarque : Le code HTML sera automatiquement supprimé du texte. | `text` | — | `200` |
| **Afficher 'lire la suite'**<br />`mod_readmore_feat` | Afficher/masquer le boutton 'lire la suite' | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Readmore align**<br />`readmore_align_feat` | Nombre de colonnes pour le contenu. NOTE : c'est la valeur maximale, le nombre de colonne affichées dépendra de la largeur de la fenêtre du navigateur | `radio` | `left` = A gauche<br />`center` = Centre<br />`right` = A droite | `center` (Centre) |
| **Classe du bouton**<br />`readmore_class_feat` | Ajoutez votre classe CSS ; readon btn feat par défaut _readon btn feat_ | `text` | — | — |

### Image

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Source de l'image**<br />`mod_image` | Sélectionner la source de l'image. Vous pouvez aussi choisir un champ image (s'il y en a au moins un de disponible) ou automatiquement extraire l'image de la description. | `fcimage` | — | — |
| **HTML de champ comme image**<br />`mod_image_custom_display` | Vous pouvez utiliser le HTML produit par n’importe quel champ personnalisé à la place de l’image. -- Laissez vide pour utiliser la valeur de la liste déroulante ci-dessus. -- **Remarque : la taille de l’image et les autres paramètres ne sont pas utilisés**. -- Écrivez sous la forme nomchamp##nomvariable, par exemple pour les champs image : imgfieldname##display_small, imgfieldname##display_medium, imgfieldname##display_large | `text` | — | — |
| **URL de champ comme image**<br />`mod_image_custom_url` | Vous pouvez utiliser l’URL produite par n’importe quel champ personnalisé à la place de l’image. -- Laissez vide pour utiliser la valeur de la liste déroulante ci-dessus. -- **Remarque : la taille de l’image et les autres paramètres sont appliqués à l’URL fournie**. -- Écrivez sous la forme nomchamp##nomvariable, par exemple pour les champs image : imgfieldname##display_small_src, imgfieldname##display_medium_src, imgfieldname##display_large_src | `text` | — | — |
| **Image par défaut (lorsque l'image est manquante)**<br />`mod_image_fallback_img` | Quand l'image est manquante, vous pouvez sélectionner une autre image par défaut. ex: l'image du texte d'introduction quand il n'y pas de valeur dans le champs image, même si le champ image possède une image par défaut. | `list` | `0` = Aucune image par défaut<br />`1` = Utiliser l'image du texte d'introduction<br />`2` = Utiliser l'image du texte d'introduction (ignorer l'image par défaut du champ)<br />`3` = Champ de repli personnalisé | — |

:::note
Pensez à activer cette option ci-dessus
:::

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Champ de repli personnalisé**<br />`mod_image_fallback_field` | — | `fcimage` | — | — |

#### Standard

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser l'image**<br />`mod_use_image` | Extraire la première image du texte principale | `multilist` | `0` = Non<br />`1` = Oui, rédimensionner<br />`small` = Oui, petite miniature (champ image)<br />`medium` = Oui, moyenne miniature (champ image)<br />`large` = Oui, grande miniature (champ image)<br />`original` = Oui, l'image originale (champ image obligatoire) | `medium` (Oui, moyenne miniature (champ image)) |
| **Lien sur l'image**<br />`mod_link_image` | Actif un lien sur l'image affichée. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Méthode de traitement**<br />`mod_method` | Méthode de traitement | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |
| **Largeur de l'image**<br />`mod_width` | Largeur de l'image | `text` | — | `80` |
| **Hauteur de l'image**<br />`mod_height` | Hauteur de l'image | `text` | — | `80` |

#### En vedette

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Utiliser l'image**<br />`mod_use_image_feat` | Extraire la première image du texte principale | `multilist` | `0` = Non<br />`1` = Oui, rédimensionner<br />`small` = Oui, petite miniature (champ image)<br />`medium` = Oui, moyenne miniature (champ image)<br />`large` = Oui, grande miniature (champ image)<br />`original` = Oui, l'image originale (champ image obligatoire) | `medium` (Oui, moyenne miniature (champ image)) |
| **Lien sur l'image**<br />`mod_link_image_feat` | Actif un lien sur l'image affichée. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Méthode de traitement**<br />`mod_method_feat` | Méthode de traitement | `radio` | `0` = A l'échelle<br />`1` = Découper | `1` (Découper) |
| **Largeur de l'image**<br />`mod_width_feat` | Largeur de l'image | `text` | — | `110` |
| **Hauteur de l'image**<br />`mod_height_feat` | Hauteur de l'image | `text` | — | `110` |

#### Image par défaut

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher l’image par défaut**<br />`mod_default_img_show` | Sélectionner pour afficher une image par défaut pour les contenus sans image | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Image par défaut**<br />`mod_default_img_path` | Image à afficher si le contenu n’a pas d’image | `text` | — | `components/com_flexicontent/assets/images/image.png` |

### Dates

#### Standard

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la date**<br />`display_date` | Afficher les dates | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Afficher le libellé**<br />`date_label` | Afficher ou masquer le libellé de la date | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Type de date**<br />`date_fields` | Type de date à afficher | `fccheckbox` | — | — |
| **Format de la date**<br />`date_format` | — | `multilist` | `DATE_FORMAT_LC` = Date format lc<br />`DATE_FORMAT_LC1` = Date format lc1<br />`DATE_FORMAT_LC2` = Date format lc2<br />`DATE_FORMAT_LC3` = Date format lc3<br />`DATE_FORMAT_LC4` = Date format lc4<br />`custom` = Personnalisé | `DATE_FORMAT_LC3` (Date format lc3) |
| **Format personnalisé**<br />`custom_date_format` | Format personnalisé de la date si vous avez sélectionner l'option ci-dessus. | `text` | — | — |

#### En vedette

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher la date**<br />`display_date_feat` | Afficher les dates | `multilist` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Afficher le libellé**<br />`date_label_feat` | Afficher ou masquer le libellé de la date | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Type de date**<br />`date_fields_feat` | Type de date à afficher | `fccheckbox` | — | — |
| **Format de la date**<br />`date_format_feat` | — | `multilist` | `DATE_FORMAT_LC` = Date format lc<br />`DATE_FORMAT_LC1` = Date format lc1<br />`DATE_FORMAT_LC2` = Date format lc2<br />`DATE_FORMAT_LC3` = Date format lc3<br />`DATE_FORMAT_LC4` = Date format lc4<br />`custom` = Personnalisé | `DATE_FORMAT_LC3` (Date format lc3) |
| **Format personnalisé**<br />`custom_date_format_feat` | Format personnalisé de la date si vous avez sélectionner l'option ci-dessus. | `text` | — | — |

### Clics

#### Standard

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les visites**<br />`display_hits` | Afficher le nombre de visites pour chaque contenu | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher le libellé**<br />`hits_label` | Afficher ou masquer le libellé de la date | `radio` | `2` = Non<br />`1` = Oui<br />`0` = Oui, après le compteur | `0` (Oui, après le compteur) |

#### En vedette

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les visites**<br />`display_hits_feat` | Afficher le nombre de visites pour chaque contenu | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher le libellé**<br />`hits_label_feat` | Afficher ou masquer le libellé de la date | `radio` | `2` = Non<br />`1` = Oui<br />`0` = Oui, après le compteur | `0` (Oui, après le compteur) |

### Vote

#### Standard

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les votes**<br />`display_voting` | Affiche les votes du contenu | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher le libellé**<br />`voting_label` | Afficher ou masquer le libellé de la date | `radio` | `2` = Non<br />`1` = Oui<br />`0` = Oui, après le compteur | `0` (Oui, après le compteur) |
| **Afficher le compteur**<br />`vote_counter` | Afficher le nombre de votes que chaque contenu a reçu. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Nombre d'étoiles**<br />`vote_stars` | Afin de rendre l'affichage plus compatible, vous pouvez afficher une seule étoile ou bien laisser les 5 étoiles. | `radio` | `1` = 1 étoile (recommandé)<br />`5` = 5 étoiles | `1` (1 étoile (recommandé)) |
| **Autoriser le vote**<br />`allow_vote` | Étant donné que le peu d’informations sur chaque élément affiché, il est recommandé de désactiver un nouveau vote | `radio` | `0` = Non (recommandé)<br />`1` = Oui | `0` (Non (recommandé)) |

#### En vedette

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les votes**<br />`display_voting_feat` | Affiche les votes du contenu | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher le libellé**<br />`voting_label_feat` | Afficher ou masquer le libellé de la date | `radio` | `2` = Non<br />`1` = Oui<br />`0` = Oui, après le compteur | `0` (Oui, après le compteur) |
| **Afficher le compteur**<br />`vote_counter_feat` | Afficher le nombre de votes que chaque contenu a reçu. | `radio` | `0` = Non<br />`1` = Oui | `1` (Oui) |
| **Nombre d'étoiles**<br />`vote_stars_feat` | Afin de rendre l'affichage plus compatible, vous pouvez afficher une seule étoile ou bien laisser les 5 étoiles. | `radio` | `1` = 1 étoile (recommandé)<br />`5` = 5 étoiles<br />`0` = Etoiles par défaut | `1` (1 étoile (recommandé)) |
| **Autoriser le vote**<br />`allow_vote_feat` | Étant donné que le peu d’informations sur chaque élément affiché, il est recommandé de désactiver un nouveau vote | `radio` | `0` = Non (recommandé)<br />`1` = Oui | `0` (Non (recommandé)) |

### Commentaires

#### Standard

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les commentaires**<br />`display_comments` | Afficher le nombre de commentaires pour chaque contenu. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher le libellé**<br />`comments_label` | Afficher ou masquer le libellé de la date | `radio` | `2` = Non<br />`1` = Oui<br />`0` = Oui, après le compteur | `0` (Oui, après le compteur) |

#### En vedette

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **FLEXI_DISPLAY_comments**<br />`display_comments_feat` | Afficher le nombre de commentaires pour chaque contenu. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher le libellé**<br />`comments_label_feat` | Afficher ou masquer le libellé de la date | `radio` | `2` = Non<br />`1` = Oui<br />`0` = Oui, après le compteur | `0` (Oui, après le compteur) |

### Champs personnalisés

#### Standard

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les champs**<br />`use_fields` | Sélectionner afin d'afficher n'importe quel champ du contenu. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher le libellé**<br />`display_label` | Afficher ou masquer le libellé de la date | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Cacher le libellé quand vide**<br />`hide_label_onempty` | Activer cette option pour cacher automatiquement le libellé du champ quand celui ci n'affiche aucune valeur. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte après le libellé**<br />`text_after_label` | Texte à afficher immédiatement après le libellé du champ | `text` | — | — |
| **Veuillez sélectionner des champs**<br />`fields` | Sélectionner les champs que vous souhaitez afficher dans ce module. | `fields` | — | — |

#### En vedette

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Afficher les champs**<br />`use_fields_feat` | Sélectionner afin d'afficher n'importe quel champ du contenu. | `multilist` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Afficher le libellé**<br />`display_label_feat` | Afficher ou masquer le libellé de la date | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Cacher le libellé quand vide**<br />`hide_label_onempty_feat` | Activer cette option pour cacher automatiquement le libellé du champ quand celui ci n'affiche aucune valeur. | `radio` | `0` = Non<br />`1` = Oui | `0` (Non) |
| **Texte après le libellé**<br />`text_after_label_feat` | Texte à afficher immédiatement après le libellé du champ | `text` | — | — |
| **Veuillez sélectionner des champs**<br />`fields_feat` | Sélectionner les champs que vous souhaitez afficher dans ce module. | `fields` | — | — |

### Contenu via Page Builder

:::note
Il s’agit de la configuration d'un affichage qui va répété **chaque contenu répertorié**. Il est disponible à tous les modèles, mais tous les modèles n'en feront pas usage
:::

### Disposition 1

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Constructeur de disposition**<br />`builder_layout1` | — | `fclayoutbuilder` | — | — |
| **HTML**<br />`builder_layout1_html` | — | `textarea` | — | — |
| **JS**<br />`builder_layout1_js` | — | `hidden` | — | — |
| **CSS**<br />`builder_layout1_css` | — | `textarea` | — | — |
| **Styles**<br />`builder_layout1_styles` | — | `hidden` | — | — |
| **Composants**<br />`builder_layout1_components` | — | `hidden` | — | — |
| **Ressources**<br />`builder_layout1_assets` | — | `hidden` | — | — |
| **Hash**<br />`builder_layout1_hash` | — | `hidden` | — | — |
| **Less**<br />`builder_layout1_less` | — | `hidden` | — | `/modules/mod_flexicontent/builder/less/builder_layout1_&#123;&#123;id&#125;&#125;` |

### Disposition 2

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Constructeur de disposition**<br />`builder_layout2` | — | `fclayoutbuilder` | — | — |
| **HTML**<br />`builder_layout2_html` | — | `textarea` | — | — |
| **JS**<br />`builder_layout2_js` | — | `hidden` | — | — |
| **CSS**<br />`builder_layout2_css` | — | `textarea` | — | — |
| **Styles**<br />`builder_layout2_styles` | — | `hidden` | — | — |
| **Composants**<br />`builder_layout2_components` | — | `hidden` | — | — |
| **Ressources**<br />`builder_layout2_assets` | — | `hidden` | — | — |
| **Hash**<br />`builder_layout2_hash` | — | `hidden` | — | — |
| **Less**<br />`builder_layout2_less` | — | `hidden` | — | `/modules/mod_flexicontent/builder/less/builder_layout2_&#123;&#123;id&#125;&#125;` |

#### Onglets d’affichage

## Avancé

### Mis en cache

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Mis en cache**<br />`cache` | Sélectionnez si vous souhaitez mettre en cache le contenu de ce module. | `list` | `1` = Paramètres globaux<br />`0` = Pas de mise en cache | `1` (Paramètres globaux) |
| **Temps de mise en cache**<br />`cache_time` | Temps avant que le module soit remis en cache. | `text` | — | `900` |

### CSS / JS

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Ajouter css**<br />`add_ccs` | Ajouter le fichier CSS par défaut du module | `radio` | `—` = Utiliser le paramètre du composant<br />`0` = Non<br />`1` = Oui<br />`2` = Liens CSS dans le HTML (permet la capture) | — |
| **Charger le JS Tooltips**<br />`add_tooltips` | Ajouter le script d'infobulles afin d'afficher des informations supplémentaires dans des tooltips en front. | `radio` | `—` = Utiliser le paramètre du composant<br />`0` = Non<br />`1` = Oui | — |

### Conteneur du module

| Option | Description | Type | Valeurs | Défaut |
| --- | --- | --- | --- | --- |
| **Suffixe de class CSS**<br />`moduleclass_sfx` | Le suffixe sera ajouté à la classe CSS du module, cela permet d'appliquer un style particulier pour le module. | `text` | — | — |
