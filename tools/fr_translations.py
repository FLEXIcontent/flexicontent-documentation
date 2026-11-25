""" Traduction française des textes restés en anglais dans les pages générées.

Les chaînes absentes des fichiers de langue officiels FLEXIcontent restent en
anglais. Ce module complète ces traductions pour les pages FR, sans toucher aux
identifiants techniques, aux valeurs de configuration ni au code.
"""
import re

from fr_exact_extra import EXACT as EXTRA_EXACT
from fr_more import (
    EXACT as MORE_EXACT,
    LABELS as MORE_LABELS,
    VALUES as MORE_VALUES,
    PHRASES as MORE_PHRASES,
    LANGUAGES as MORE_LANGUAGES,
)

# Remplacements de ligne entière (titres, notes, descriptions longues).
EXACT = {
    # --- Titres ---
    '## Advanced': '## Avancé',
    '### Advanced': '### Avancé',
    '## Social': '## Réseaux sociaux',
    '## Tabs (RegEx)': '## Onglets (RegEx)',
    '#### Slider': '#### Curseur',
    '#### Meta': '#### Métadonnées',
    '#### SEO': '#### Référencement',
    '### Seo': '### Référencement',
    '#### Seo': '#### Référencement',
    '#### Information': '#### Informations',
    '#### Extra editor areas': '#### Zones supplémentaires de l’éditeur',
    '#### URL / Links': '#### URL / liens',
    '#### Item tabset': '#### Onglets de l’élément',
    '### Module Container': '### Conteneur du module',
    '## Download limits': '## Limites de téléchargement',
    '## File editor': '## Éditeur de fichiers',
    '#### Custom file property 1 (HTML)': '#### Propriété de fichier personnalisée 1 (HTML)',
    '#### Custom file property 2 (HTML)': '#### Propriété de fichier personnalisée 2 (HTML)',
    '#### Remote files (URLs)': '#### Fichiers distants (URL)',
    '## User creation / Edit coupons': '## Création d’utilisateur / Coupons de modification',
    '### Edit coupons': '### Coupons de modification',
    '#### Email address': '#### Adresse e-mail',
    '#### Existing item Or user is logged': '#### Contenu existant ou utilisateur connecté',
    '#### Position, Style': '#### Position, style',
    '## Permission': '## Permissions',
    '## Select Module': '## Sélectionner un module',
    '## Links': '## Liens',
    '### Category image': '### Image de catégorie',
    '### Item images': '### Images du contenu',
    '### Previous / Next items': '### Contenus précédent / suivant',
    '#### Button Text': '#### Texte du bouton',
    '#### Thumbnailing parameters': '#### Paramètres des vignettes',
    '### Form Display': '### Affichage du formulaire',
    '#### Fields WITHOUT value': '#### Champs SANS valeur',
    '### Field filters': '### Filtres de champs',
    '## Playback': '## Lecture',
    '### Media': '### Médias',
    '#### Media Info': '#### Informations sur le média',
    '#### Media player': '#### Lecteur média',
    '#### Native APIs only': '#### API natives uniquement',
    '#### Waveform options': '#### Options du waveform',
    '#### Wavesurfer JS options': '#### Options de Wavesurfer JS',
    '#### Category-like views': '#### Vues de type catégorie',
    '#### Item view': '#### Vue contenu',
    '#### CUSTOM 1': '#### PERSONNALISÉ 1',
    '#### CUSTOM 2': '#### PERSONNALISÉ 2',
    '#### Layout': '#### Disposition',
    '#### Email': '#### E-mail',
    '### Common tags (seleactable via checkboxes)': '### Balises courantes (sélectionnables via cases à cocher)',
    '### Menu Item': '### Élément de menu',
    '#### Item form bof': '#### Début du formulaire de contenu',
    '#### Item form eof': '#### Fin du formulaire de contenu',
    '#### Cats params set': '#### Jeu de paramètres de catégories',
    '### FC Advanced Search plugin: **Override Configuration**': '### Plugin FC Advanced Search : **Surcharger la configuration**',
    '### Results List': '### Liste des résultats',
    '### Search Form': '### Formulaire de recherche',
    '#### Advanced Options': '#### Options avancées',
    '#### Basic Information (used by non-FC results too)': '#### Informations de base (également utilisées pour les résultats non-FC)',
    '#### Category selector': '#### Sélecteur de catégories',
    '#### Content Types': '#### Types de contenu',
    '#### Display Fields (Render their HTML)': '#### Champs affichés (rendu de leur HTML)',
    '#### Text Search': '#### Recherche textuelle',
    '### Featured items': '### Contenus en vedette',
    '### Standard items': '### Contenus standard',
    '#### (sub) Category block, at (sub-)category start': '#### Bloc (sous-)catégorie, au début de la (sous-)catégorie',
    '#### Content / image placement': '#### Placement du contenu / de l’image',
    '#### Item box': '#### Boîte du contenu',
    '#### Items featured tabset': '#### Onglets des contenus en vedette',
    '#### Items list box': '#### Boîte de la liste des contenus',
    '#### Items standard tabset': '#### Onglets des contenus standard',
    '#### Lazy loading image': '#### Image en chargement différé',
    '#### commun Item box style': '#### Style commun de la boîte de contenu',
    '#### Main Content': '#### Contenu principal',
    '#### Field columns': '#### Colonnes de champs',
    '### Items List': '### Liste des contenus',
    '#### Display Tabset': '#### Onglets d’affichage',
    '#### Items List Tabset': '#### Onglets de la liste des contenus',
    '#### Search Form: Advanced Options': '#### Formulaire de recherche : options avancées',
    '#### Search Form: Content Types': '#### Formulaire de recherche : types de contenu',
    '### Marker actions': '### Actions sur les marqueurs',
    '### Markers list': '### Liste des marqueurs',
    '#### Geo Location options': '#### Options de géolocalisation',
    '#### Map basic configuration': '#### Configuration de base de la carte',
    '#### Marker list wrapping': '#### Retour à la ligne de la liste des marqueurs',
    '#### Markers List options': '#### Options de la liste des marqueurs',
    '#### Parameters tags view legacy': '#### Paramètres de l’ancienne vue des étiquettes',
    '#### Table of contents': '#### Table des matières',
    '#### Hide categories': '#### Masquer les catégories',
    '#### URL redirections': '#### Redirections d’URL',

    # --- Descriptions de plugins ---
    '> FLEXIcontent plugin for JSitemap': '> Plugin FLEXIcontent pour JSitemap',
    '> OSMap Plugin for FLEXIcontent Component': '> Plugin OSMap pour le composant FLEXIcontent',
    '> System Plugin for FLEXIcontent Advanced Routing': '> Plugin système pour le routage avancé de FLEXIcontent',
    '*Plugin : `addressint` — International Address / Google Maps*': '*Plugin : `addressint` — Adresse internationale / Google Maps*',
    '*Plugin : `authoritems` — Author Items*': '*Plugin : `authoritems` — Contenus de l’auteur*',
    '*Plugin : `checkboximage` — Checkbox Image*': '*Plugin : `checkboximage` — Case à cocher avec image*',
    '*Plugin : `color` — Color*': '*Plugin : `color` — Couleur*',
    '*Plugin : `core` — Core Fields*': '*Plugin : `core` — Champs cœur*',
    '*Plugin : `coreprops` — CORE property*': '*Plugin : `coreprops` — Propriété cœur*',
    '*Plugin : `custom_form_html` — Custom HTML / Item Form Tab / Fieldset*': '*Plugin : `custom_form_html` — HTML personnalisé / onglet de formulaire / fieldset*',
    '*Plugin : `date` — Date / Timestamp / Publish Up-Down Dates*': '*Plugin : `date` — Date / horodatage / dates de publication*',
    '*Plugin : `fcloadmodule` — Load Module / Module position*': '*Plugin : `fcloadmodule` — Charger un module / une position de module*',
    '*Plugin : `fcpagenav` — Navigation*': '*Plugin : `fcpagenav` — Navigation*',
    '*Plugin : `fieldgroup` — Fieldgroup*': '*Plugin : `fieldgroup` — Groupe de champs*',
    '*Plugin : `file` — File*': '*Plugin : `file` — Fichier*',
    '*Plugin : `image` — Image or Gallery*': '*Plugin : `image` — Image ou galerie*',
    '*Plugin : `jprofile` — User Profile*': '*Plugin : `jprofile` — Profil utilisateur*',
    '*Plugin : `linkslist` — HTML list of URLs/Anchors/JS links*': '*Plugin : `linkslist` — Liste HTML d’URL / ancres / liens JS*',
    '*Plugin : `mediafile` — MediaFile*': '*Plugin : `mediafile` — Fichier média*',
    '*Plugin : `phonenumbers` — International Phone Numbers*': '*Plugin : `phonenumbers` — Numéros de téléphone internationaux*',
    '*Plugin : `radioimage` — Radio Image*': '*Plugin : `radioimage` — Bouton radio avec image*',
    '*Plugin : `relation_reverse` — Relation - Reverse*': '*Plugin : `relation_reverse` — Relation inverse*',
    '*Plugin : `selectmultiple` — Select Multiple*': '*Plugin : `selectmultiple` — Sélection multiple*',
    '*Plugin : `sharedmedia` — Shared Video/Audio*': '*Plugin : `sharedmedia` — Vidéo/audio partagé*',
    '*Plugin : `termlist` — TermList*': '*Plugin : `termlist` — Liste de termes*',
    '*Plugin : `textselect` — Textselect*': '*Plugin : `textselect` — Sélection de texte*',
    '*Plugin : `toolbar` — Toolbar*': '*Plugin : `toolbar` — Barre d’outils*',
    '*Plugin : `weblink` — Weblink*': '*Plugin : `weblink` — Lien web*',

    # --- Notes et textes longs ---
    'Please set layout parameters in **Layout: ... TAB**. CSS/HTML developers please read: ** Custom templates HOW-TO **':
        'Veuillez définir les paramètres de disposition dans l’onglet **Disposition : ...**. Les développeurs CSS/HTML doivent consulter : ** Guide des modèles personnalisés **',
    'Choose which fields appear when editing a file. Hidden fields keep their saved values. Advanced settings still require the file-properties permission.':
        'Choisissez les champs affichés lors de la modification d’un fichier. Les champs masqués conservent leurs valeurs enregistrées. Les paramètres avancés nécessitent toujours l’autorisation propriétés de fichier.',
    'These settings apply to the file manager forms (add / edit files outside of a File field). If a property is not enabled here, the settings of the first File field that enables it are used. Each File field has its own settings (Form field tab, Edit properties), which are used when files are edited via that field':
        'Ces paramètres s’appliquent aux formulaires du gestionnaire de fichiers (ajout / modification de fichiers hors d’un champ Fichier). Si une propriété n’est pas activée ici, les paramètres du premier champ Fichier qui l’active sont utilisés. Chaque champ Fichier possède ses propres paramètres (onglet Champ du formulaire, Modifier les propriétés), utilisés lorsque les fichiers sont modifiés via ce champ',
    'Limit how many files each user group can download in a period (minutes, hours or days), across all fields that use these limits. Downloads are counted per logged-in user, and per visitor (cookie + IP) for guests. A group inherits the limit of its parent groups; if several groups match, the highest limit wins. Super users are never limited.':
        'Limitez le nombre de fichiers que chaque groupe d’utilisateurs peut télécharger sur une période (minutes, heures ou jours), pour tous les champs utilisant ces limites. Les téléchargements sont comptés par utilisateur connecté, et par visiteur (cookie + IP) pour les invités. Un groupe hérite de la limite de ses groupes parents ; si plusieurs groupes correspondent, la limite la plus élevée s’applique. Les super utilisateurs ne sont jamais limités.',
    'Notification emails use Joomla\'s mail templates. Edit the subject and body of each notification in **System → Mail Templates**, filtering on the **FLEXIcontent** extension. Available tags include: **&#123;TITLE&#125;**, **&#123;STATE&#125;**, **&#123;CREATOR&#125;**, **&#123;MODIFIER&#125;**, **&#123;EDITOR_NAME&#125;**, **&#123;CREATED&#125;**, **&#123;MODIFIED&#125;**, **&#123;CATEGORIES&#125;**, **&#123;VIEW_URL&#125;**, **&#123;EDIT_URL_FE&#125;**, **&#123;EDIT_URL_BE&#125;**, **&#123;NOTIFY_TEXT&#125;**, **&#123;CATEGORY_TEXT&#125;**. FlexiContent custom fields are available as **&#123;FIELD_FIELDNAME&#125;** or directly as **&#123;FIELDNAME&#125;** (field name in uppercase, non alphanumeric characters replaced by underscores, e.g. **&#123;FIELD_FLOORS&#125;** or **&#123;FLOORS&#125;**), and all non-core fields together as **&#123;FIELDS&#125;**. A field name never overrides a core tag such as **&#123;TITLE&#125;**. **Conditional blocks:** the template subject, text body and HTML body can contain **&#123;if ...&#125;...&#123;elseif ...&#125;...&#123;else&#125;...&#123;/if&#125;** blocks. Context variables: **catid**, **incat**, **state_id**, **lang**, **type_id**, **item_id**, **author_id**, **editor_id**. Custom fields are tested with **field_name** (e.g. **&#123;if field_floors&#125;Floor: &#123;FIELD_FLOORS&#125;&#123;/if&#125;**). Operators: **=**, **!=**, **in**, **not in**, **contains**, **not contains**, **&gt;**, **&gt;=**, **=100000&#125;Premium&#123;/if&#125;**. Keywords and string comparisons are case-insensitive. Conditions only affect the text, not the recipients. They are evaluated on the template content stored in Mail Templates; the shipped defaults use language keys and must be edited and saved once to contain conditional text. Invalid conditions keep the content and never block the email.':
        'Les e-mails de notification utilisent les modèles de messagerie de Joomla. Modifiez l’objet et le corps de chaque notification dans **Système → Modèles de messagerie**, en filtrant sur l’extension **FLEXIcontent**. Les balises disponibles incluent : **&#123;TITLE&#125;**, **&#123;STATE&#125;**, **&#123;CREATOR&#125;**, **&#123;MODIFIER&#125;**, **&#123;EDITOR_NAME&#125;**, **&#123;CREATED&#125;**, **&#123;MODIFIED&#125;**, **&#123;CATEGORIES&#125;**, **&#123;VIEW_URL&#125;**, **&#123;EDIT_URL_FE&#125;**, **&#123;EDIT_URL_BE&#125;**, **&#123;NOTIFY_TEXT&#125;**, **&#123;CATEGORY_TEXT&#125;**. Les champs personnalisés FLEXIcontent sont disponibles sous **&#123;FIELD_FIELDNAME&#125;** ou directement sous **&#123;FIELDNAME&#125;** (nom du champ en majuscules, caractères non alphanumériques remplacés par des tirets bas, ex. **&#123;FIELD_FLOORS&#125;** ou **&#123;FLOORS&#125;**), et tous les champs non cœur ensemble sous **&#123;FIELDS&#125;**. Un nom de champ ne remplace jamais une balise cœur comme **&#123;TITLE&#125;**. **Blocs conditionnels :** l’objet, le corps texte et le corps HTML du modèle peuvent contenir des blocs **&#123;if ...&#125;...&#123;elseif ...&#125;...&#123;else&#125;...&#123;/if&#125;**. Variables de contexte : **catid**, **incat**, **state_id**, **lang**, **type_id**, **item_id**, **author_id**, **editor_id**. Les champs personnalisés sont testés avec **field_name** (ex. **&#123;if field_floors&#125;Étage : &#123;FIELD_FLOORS&#125;&#123;/if&#125;**). Opérateurs : **=**, **!=**, **in**, **not in**, **contains**, **not contains**, **&gt;**, **&gt;=**, **=100000&#125;Premium&#123;/if&#125;**. Les mots-clés et les comparaisons de chaînes ne sont pas sensibles à la casse. Les conditions n’affectent que le texte, pas les destinataires. Elles sont évaluées sur le contenu du modèle enregistré dans Modèles de messagerie ; les modèles fournis utilisent des clés de langue et doivent être modifiés et enregistrés une fois pour contenir du texte conditionnel. Une condition invalide conserve le contenu et ne bloque jamais l’e-mail.',
    '- **Author\'s Items** and **My Items** always use category view. Usually only 1 menu item is needed. - Using category view allows using \'Templates\' And \'List\' configuration.':
        '- **Contenus de l’auteur** et **Mes contenus** utilisent toujours la vue catégorie. Un seul élément de menu suffit généralement. - La vue catégorie permet d’utiliser la configuration **Modèles** et **Liste**.',
    '- Create these (menu items) inside **Flexicontent hidden menu** - Do not select specific TAG / category / author / etc':
        '- Créez ces éléments de menu dans le **menu caché FLEXIcontent** - Ne sélectionnez pas d’étiquette, catégorie, auteur, etc. précis',
    '- Each menu item will be used as **default configuration** - SEF URLs will use the menu item\'s alias':
        '- Chaque élément de menu servira de **configuration par défaut** - Les URL SEF utiliseront l’alias de l’élément de menu',
    'If using / * needing legacy views. e.g. if search engines / 3rd party web-sites are referencing legacy views, then create 2 legacy menu items and select them as default below':
        'Si vous utilisez / avez besoin des anciennes vues, par exemple si des moteurs de recherche ou des sites tiers référencent ces vues, créez 2 éléments de menu d’ancienne vue et sélectionnez-les comme valeurs par défaut ci-dessous',
    'About template parameters':
        'À propos des paramètres du modèle',
    'Please note you cannot set template parameters here. Template parameters for the choosen template will be retrieved from the template configuration (then inherited from category configuration). For fields shown, please add your fields in layout positions in template configuration management tab':
        'Veuillez noter que vous ne pouvez pas définir les paramètres du modèle ici. Les paramètres du modèle choisi seront récupérés depuis la configuration du modèle (puis hérités de la configuration de la catégorie). Pour les champs affichés, ajoutez vos champs dans les positions de disposition de l’onglet de gestion de la configuration du modèle',
    'To create a menu item for DEFAULT DISPLAY -configuration- (for all authors that do not have a menu item) 1. Select no author here 2. Set a generic title/alias e.g. \'authored\' (as alias will be show in the URLs) and configure menu item parameters 3. Go to component parameters, open TAB \'Lists\' and select this menu item as default menu item for (category-based view) \'Tagged items\'':
        'Pour créer un élément de menu de configuration **d’affichage par défaut** (pour tous les auteurs sans élément de menu) : 1. Ne sélectionnez aucun auteur ici 2. Définissez un titre/alias générique, par exemple « authored » (l’alias apparaîtra dans les URL) et configurez les paramètres de l’élément 3. Ouvrez les paramètres du composant, l’onglet **Listes**, et sélectionnez cet élément comme élément par défaut de la vue catégorie « Contenus étiquetés »',
    'To create a menu item for DEFAULT DISPLAY -configuration- (for all tags that do not have a menu item) 1. Select no tag here 2. Set a generic title/alias e.g. \'tagged\' (as alias will be show in the URLs) and configure menu item parameters 3. Go to component parameters, open TAB \'Lists\' and select this menu item as default menu item for (category-based view) \'Tagged items\'':
        'Pour créer un élément de menu de configuration **d’affichage par défaut** (pour toutes les étiquettes sans élément de menu) : 1. Ne sélectionnez aucune étiquette ici 2. Définissez un titre/alias générique, par exemple « tagged » (l’alias apparaîtra dans les URL) et configurez les paramètres de l’élément 3. Ouvrez les paramètres du composant, l’onglet **Listes**, et sélectionnez cet élément comme élément par défaut de la vue catégorie « Contenus étiquetés »',
    'To create a menu item for DEFAULT DISPLAY -configuration- (for all tags that do not have a menu item) 1. Select no tag here 2. Set a generic title/alias e.g. \'tagged_items\' (as alias will be show in the URLs) and configure menu item parameters 3. Go to component parameters, open TAB \'Lists\' and select this menu item as default menu item for LEGACY VIEW \'Tagged items\'':
        'Pour créer un élément de menu de configuration **d’affichage par défaut** (pour toutes les étiquettes sans élément de menu) : 1. Ne sélectionnez aucune étiquette ici 2. Définissez un titre/alias générique, par exemple « tagged_items » (l’alias apparaîtra dans les URL) et configurez les paramètres de l’élément 3. Ouvrez les paramètres du composant, l’onglet **Listes**, et sélectionnez cet élément comme élément par défaut de l’ancienne vue « Contenus étiquetés »',
    'If you leave these blank, then please check default values at item configuration type type':
        'Si vous laissez ces champs vides, vérifiez les valeurs par défaut dans la configuration du type de contenu',
    'NOTE: single or multiple value allowed, this depends on target view (set below)':
        'REMARQUE : une ou plusieurs valeurs sont autorisées, selon la vue cible (définie ci-dessous)',
    'NOTE: when advanced search options box is hidden, the options configured below will still be used':
        'REMARQUE : même lorsque la boîte des options de recherche avancée est masquée, les options configurées ci-dessous sont utilisées',
    'Please note these reasons for some results not being included: - you have not enabled short word search in component and word is &lt; 4 characters - word is too common e.g. appears in about half of the articles - wrong language or article not publish or article has expired':
        'Voici pourquoi certains résultats peuvent être absents : - la recherche de mots courts n’est pas activée dans le composant et le mot compte moins de 4 caractères - le mot est trop courant, par exemple présent dans environ la moitié des articles - langue incorrecte, article non publié ou article expiré',
    'Please remember to enable this above':
        'Pensez à activer cette option ci-dessus',
    'NOTE: to list items with FEATURED FLAG, please go to TAB \'Select Items\' and find scope \'Joomla Featured FLAG\'':
        'REMARQUE : pour lister les contenus avec le drapeau « en vedette », ouvrez l’onglet **Sélectionner les contenus** et choisissez la portée **Drapeau Joomla en vedette**',
    'To use scheduled / expired items orderings, please enable ignore scheduled / expired dates, inside \'Select Items\' TAB':
        'Pour utiliser les tris par contenus programmés / expirés, activez l’option d’ignorance des dates de programmation / d’expiration dans l’onglet **Sélectionner les contenus**',
    'Compare to specific dates (YYYY-MM-DD) e.g. 2015-01-23 - to enter **CURRENT date (now)** use: CURDATE() &gt; , and set date type to \'SQL date expression\'':
        'Comparer à des dates précises (AAAA-MM-JJ), ex. 2015-01-23 - pour saisir la **date actuelle (maintenant)**, utilisez : CURDATE() &gt; , et définissez le type de date sur « expression SQL de date »',
    'Custom offsets that shift the DYNAMIC date, e.g. -5 d (minus 5 days) - to enter **CURRENT date (now)** use: 0 d':
        'Décalages personnalisés appliqués à la date dynamique, ex. -5 j (moins 5 jours) - pour saisir la **date actuelle (maintenant)**, utilisez : 0 j',
    'This effects if category selector will allow selecting multiple categories':
        'Cette option détermine si le sélecteur de catégories autorise la sélection de plusieurs catégories',
    'Show tags of items in the following categories. **Current category** is - either currently viewed category - or main category of the item currently viewed':
        'Afficher les étiquettes des contenus des catégories suivantes. **Catégorie actuelle** désigne - la catégorie en cours de visualisation - ou la catégorie principale du contenu affiché',
    'Group markers as a total number, to prevent many markers showing very close together':
        'Regrouper les marqueurs en un nombre total, afin d’éviter que de nombreux marqueurs très proches ne s’affichent',
    'Limit at which marker list will be wrapped':
        'Largeur à partir de laquelle la liste des marqueurs passe à la ligne',
    'Hide Categories from Pathway/URLs for Types - These are types that contain content not being a part of structure but rather general information content like site usage instructions or license agreement, etc':
        'Masquer les catégories du fil d’Ariane / des URL pour les types - il s’agit des types dont le contenu ne fait pas partie de la structure mais contient des informations générales, comme les instructions d’utilisation du site ou un contrat de licence, etc.',
    'Hide categories in Content / Content Listings by NOT displaying: a. direct category links b. category title as a content/content list markup - These categories are for special purposes, e.g. contain items **displayed** in frontpage or in a module Slideshow.':
        'Masquer les catégories dans les contenus / listes de contenus en n’affichant pas : a. les liens directs vers les catégories b. le titre de la catégorie comme balisage de contenu / liste - ces catégories ont un usage particulier, par exemple contenir des éléments **affichés** en page d’accueil ou dans un diaporama de module.',
    'NOTE: if you are sending expiration emails, after items have expired, do not change item state, and do not clear publish down date':
        'REMARQUE : si vous envoyez des e-mails d’expiration, ne modifiez pas l’état du contenu après son expiration et n’effacez pas la date de fin de publication',
    'About top folder (J4+ only) - You must add this folder in PLUGIN: \'FileSystem - Local\', e.g. add folder downloads. - For quantum file manager. This is the scope name NOTE: please add an extra custom-named scope for the folder images !! e.g. \'imgs\' DO NOT change folder name \'images\', \'imgs\' will be the name of the custom scope':
        'À propos du dossier racine (Joomla 4+ uniquement) - vous devez ajouter ce dossier dans le plugin **FileSystem - Local**, par exemple le dossier downloads. - Pour le gestionnaire Quantum, il s’agit du nom de portée. REMARQUE : ajoutez une portée personnalisée supplémentaire pour le dossier images, par exemple « imgs ». NE modifiez PAS le nom du dossier « images » ; « imgs » sera le nom de la portée personnalisée',
    'Button configuration for actions such as: download, view, share, add-to-cart':
        'Configuration des boutons pour des actions telles que : télécharger, afficher, partager, ajouter au panier',
    'Currently only FTP is supported, TO-DO more external storage options ...':
        'Actuellement, seul FTP est pris en charge ; d’autres options de stockage externe sont à venir…',
    'Requires manual installation of 2 libraries: tcpdf and fpdi into folder **/components/com_flexicontent/librairies/TCPDF**':
        'Nécessite l’installation manuelle de 2 bibliothèques : tcpdf et fpdi dans le dossier **/components/com_flexicontent/librairies/TCPDF**',
    'Note some of these settings also exist in type configuration form !':
        'Certains de ces paramètres existent également dans le formulaire de configuration du type !',
    'Split textarea into TABs via regular expression':
        'Diviser la zone de texte en onglets à l’aide d’une expression régulière',
    'Note, some core properties only support specific displays, e.g only the text input':
        'Notez que certaines propriétés cœur ne prennent en charge que des affichages spécifiques, par exemple uniquement le champ de texte',
    '#### NOTE: - Fields that can be displayed are: language, alias, main category, access, - for displaying \'publish_up\', \'publish_down\' please use date field in appropriate mode':
        '#### REMARQUE : - les champs affichables sont : langue, alias, catégorie principale, accès, - pour afficher « publish_up » et « publish_down », utilisez un champ Date dans le mode approprié',
    'Item Form CORE property placer Plugin for FLEXIcontent. This field is used to define the place that the CORE property will appear in Item Form. This is done by ordering it in fields manager, while Content Type filter is enabled':
        'Plugin de placement des propriétés cœur du formulaire de contenu pour FLEXIcontent. Ce champ définit l’emplacement de la propriété cœur dans le formulaire, en l’ordonnançant dans le gestionnaire de champs lorsque le filtre par type de contenu est actif',
    'Form Field Group Marker Field Plugin for FLEXIcontent. This field is used to mark the start/end of FLEXIcontent field groups in ITEM edit FORM. Group will appear inside Tabs/Fieldsets/etc. Take care to match all openings with a closing marker appropriately.':
        'Plugin de marquage de groupe de champs pour FLEXIcontent. Ce champ marque le début/la fin des groupes de champs dans le formulaire de modification. Le groupe apparaîtra dans des onglets, fieldsets, etc. Veillez à associer chaque ouverture à un marqueur de fermeture.',
    'Load a module or module position inside a content item':
        'Charger un module ou une position de module dans un contenu',
    'Page Navigation Field Plugin for FLEXIcontent':
        'Plugin de champ de navigation de page pour FLEXIcontent',
    'Toolbar Field for FLEXIcontent':
        'Champ de barre d’outils pour FLEXIcontent',
    'If \'Media URL\' is enabled, the layout is forced to \'fancybox\' except for the \'GLightbox\' layout which supports video URLs natively':
        'Si « URL média » est activé, la disposition est forcée sur « fancybox », sauf pour la disposition « GLightbox » qui prend en charge nativement les URL de vidéo',
    'PLEASE NOTE: If media-URL is enabled then **fancybox** layout will be forced, except when **GLightbox** layout is selected (it supports video URLs natively)':
        'VEUILLEZ NOTER : si l’URL média est activée, la disposition **fancybox** sera forcée, sauf si la disposition **GLightbox** est sélectionnée (elle prend en charge nativement les URL de vidéo)',
    'Not applied in inline (non-popup) galleries like: Elastislide / Galleriffic':
        'Non applicable aux galeries en ligne (sans fenêtre modale) comme Elastislide / Galleriffic',
    'Gallery navigation JS has been disabled in ITEM & CATEGORY view, because parameter \'Link to URL\' was enabled':
        'Le JavaScript de navigation de la galerie a été désactivé dans les vues contenu et catégorie, car le paramètre « Lien vers l’URL » est activé',
    'Gallery navigation JS has been disabled in CATEGORY view, because parameter \'Link to item\' was enabled':
        'Le JavaScript de navigation de la galerie a été désactivé dans la vue catégorie, car le paramètre « Lien vers le contenu » est activé',
    'Samples per peak. E.g. Enter 256, to use 256 input samples to create 1 waveform peak. Note: this is for sounds up to 30 seconds. For longer files we will increase this proportionally. E.g. for 60 seconds we will use 512 samples to create 1 waveform peak.':
        'Échantillons par pic. Par exemple, saisissez 256 pour utiliser 256 échantillons afin de créer 1 pic de waveform. Remarque : cela concerne les sons jusqu’à 30 secondes. Pour les fichiers plus longs, le nombre sera augmenté proportionnellement. Par exemple, pour 60 secondes, 512 échantillons créeront 1 pic.',
    'Media properties Filters. Currently these effect all Media properties in the same way':
        'Filtres des propriétés média. Actuellement, ils affectent toutes les propriétés média de la même manière',
    'Search view can do **text search** and **filtering**, differently per content type, -- you may set search behaviour here. **NOTE:** these are not used in category-like views (content lists), for these views configure in component / category / menu items':
        'La vue de recherche peut effectuer une **recherche textuelle** et un **filtrage**, différemment selon le type de contenu ; vous pouvez définir ici le comportement de la recherche. **REMARQUE :** ces paramètres ne sont pas utilisés dans les vues de type catégorie (listes de contenus), où la configuration se fait dans le composant / la catégorie / les éléments de menu',
    'Warning: this makes sense, if you order your items by their category (1st level order), (2nd level order can be anything e.g. title)':
        'Attention : cela est pertinent si vous triez vos contenus par catégorie (tri de premier niveau), le tri de second niveau pouvant être libre, par exemple le titre',
}

# Longues lignes de tableaux et libellés complémentaires.
EXACT.update(EXTRA_EXACT)
EXACT.update(MORE_EXACT)

# Libellés d’options (gras) à traduire.
LABELS = {
    'Download filename': 'Nom du fichier téléchargé',
    'Download stamping': 'Estampille du téléchargement',
    'Keep old upload date': 'Conserver la date d’envoi d’origine',
    'Keep old uploader': 'Conserver l’auteur de l’envoi d’origine',
    'Language': 'Langue',
    'Access': 'Accès',
    'Hit count': 'Nombre de vues',
    'File type': 'Type de fichier',
    'File size': 'Taille du fichier',
    'Storage filename / URL': 'Nom de fichier / URL de stockage',
    'Server path': 'Chemin serveur',
    'Replacement upload': 'Remplacement du fichier',
    'Label': 'Libellé',
    'Display label': 'Afficher le libellé',
    'Input height (rows)': 'Hauteur du champ (lignes)',
    'Enable download limits': 'Activer les limites de téléchargement',
    'Count coupon / download cart downloads': 'Compter les téléchargements via coupons / panier',
    'Counting mode': 'Mode de comptage',
    'Guest IP allowance (multiplier)': 'Quota IP invité (multiplicateur)',
    'Limit per user group': 'Limite par groupe d’utilisateurs',
    'Limit reached: modal HTML': 'Limite atteinte : HTML de la fenêtre modale',
    'Period unit': 'Unité de la période',
    'Period': 'Période',
    'Trusted remote file hosts': 'Hôtes distants de confiance',
    'Automatically read trusted URL file sizes': 'Lire automatiquement la taille des fichiers URL de confiance',
    'Update channel': 'Canal de mise à jour',
    'Exported fields': 'Champs exportés',
    'Field (Column) separator': 'Séparateur de champs (colonnes)',
    'Multivalue separator': 'Séparateur des valeurs multiples',
    'Column Headers': 'En-têtes de colonnes',
    'Backend list filters': 'Filtres de la liste backend',
    'Apply filters (Modern style)': 'Appliquer les filtres (style moderne)',
    'Category path format': 'Format du chemin des catégories',
    'Content type tabs style': 'Style des onglets des types de contenu',
    'Custom columns appearance': 'Apparence des colonnes personnalisées',
    'Number of parent categories to show': 'Nombre de catégories parentes à afficher',
    'Show category path in category lists': 'Afficher le chemin des catégories dans les listes',
    'Trim length (characters)': 'Longueur de coupure (caractères)',
    'Filter Badge': 'Badge de filtre',
    'Infinit scrolling': 'Défilement infini',
    'List all (via ACL)': 'Tout lister (via ACL)',
    'Use ajax search': 'Utiliser la recherche Ajax',
    'Disable subtree parent': 'Désactiver le parent de la sous-arborescence',
    'Urls': 'URL',
    'Intro / Full Images': 'Images intro / complètes',
    'Edit coupoun email text': 'Texte de l’e-mail du coupon de modification',
    'Email exists': 'L’e-mail existe',
    'Initialized': 'Initialisé',
    'Force language code (e.g. en)': 'Forcer le code de langue (ex. en)',
    'Business or location': 'Entreprise ou lieu',
    'User selection': 'Sélection utilisateur',
    'Tile (Map) Server URL': 'URL du serveur de tuiles (carte)',
    'Address 1': 'Adresse 1', 'Address 2': 'Adresse 2', 'Address 3': 'Adresse 3',
    'City': 'Ville', 'Country': 'Pays', 'Zip': 'Code postal',
    'Latitude': 'Latitude', 'Longitude': 'Longitude', 'Marker': 'Marqueur',
    'Custom colors': 'Couleurs personnalisées',
    'Specific colors': 'Couleurs précises',
    'Toggle Style': 'Style du bouton bascule',
    'Status info': 'Informations sur le statut',
    'Form image height': 'Hauteur de l’image dans le formulaire',
    'Form image width': 'Largeur de l’image dans le formulaire',
    'Border type': 'Type de bordure',
    'Font style': 'Style de police',
    'Font family': 'Famille de police',
    'Font size': 'Taille de police',
    'Align': 'Alignement',
    'Hostname': 'Nom d’hôte',
    'Port': 'Port',
    'Joomla media': 'Médias Joomla',
    'Sub folder path': 'Chemin du sous-dossier',
    'Top folder': 'Dossier racine',
    'View inside': 'Affichage dans',
    'Every N hits': 'Tous les N affichages',
    'Header info': 'Informations d’en-tête',
    'Samples per peak': 'Échantillons par pic',
    'Bit rate (kbps)': 'Débit binaire (kbps)',
    'Media properties': 'Propriétés du média',
    'Profile link': 'Lien vers le profil',
    'Displayed HTML': 'HTML affiché',
    'Embed with': 'Intégrer avec',
    'Specific images': 'Images précises',
    'Field HTML as Image': 'HTML de champ comme image',
    'Field URL as Image': 'URL de champ comme image',
    'Read more class': 'Classe du lien « Lire la suite »',
    'Read more image': 'Image du lien « Lire la suite »',
    'Title background': 'Arrière-plan du titre',
    'Title font size': 'Taille de police du titre',
    'Title text color': 'Couleur du texte du titre',
    'background color': 'couleur d’arrière-plan',
    'border color': 'couleur de bordure',
    'border width': 'largeur de bordure',
    'columns size': 'taille des colonnes',
    'description color': 'couleur de la description',
    'margin bottom': 'marge inférieure',
    'margin left/right': 'marge gauche/droite',
    'margin top': 'marge supérieure',
    'margin top/bottom': 'marge supérieure/inférieure',
    'padding left/right': 'remplissage gauche/droite',
    'padding top/bottom': 'remplissage supérieur/inférieur',
    'Gap': 'Espacement',
    'Top width': 'Largeur du bloc supérieur',
    'Subtitle 1': 'Sous-titre 1', 'Subtitle 2': 'Sous-titre 2', 'Subtitle 3': 'Sous-titre 3',
    'Tab 1': 'Onglet 1', 'Tab 2': 'Onglet 2', 'Tab 3': 'Onglet 3', 'Tab 4': 'Onglet 4',
    'Tab 5': 'Onglet 5', 'Tab 6': 'Onglet 6', 'Tab 7': 'Onglet 7', 'Tab 8': 'Onglet 8',
    'Tab 9': 'Onglet 9', 'Tab 10': 'Onglet 10', 'Tab 11': 'Onglet 11', 'Tab 12': 'Onglet 12',
    'Select a custom field Fallback': 'Champ personnalisé de repli',
    '# Featured': '# Contenus en vedette',
    'Title color': 'Couleur du titre',
    'Components': 'Composants',
    'Assets': 'Ressources',
    'Btn class': 'Classe du bouton',
    'Current category is': 'La catégorie actuelle est',
    'Default image': 'Image par défaut',
    'Custom fallback field': 'Champ de repli personnalisé',
    'Styles': 'Styles',
    'Modules field cache time label': 'Durée du cache du champ Modules',
    'Modules field caching label': 'Cache du champ Modules',
    'Modules field moduleclass sfx label': 'Suffixe de classe du module',
    'Click action': 'Action au clic',
    'Custom display': 'Affichage personnalisé',
    'Marker list container wrap limit (pixels)': 'Limite de retour à la ligne de la liste des marqueurs (pixels)',
    'Near Me zoom default': 'Zoom par défaut pour « Near Me »',
    'Allow user selection': 'Autoriser la sélection par l’utilisateur',
    'Buttons position': 'Position des boutons',
    'Categories': 'Catégories',
    'Column gap': 'Espacement entre colonnes',
    'Column width': 'Largeur de colonne',
    'Search Limit': 'Limite de recherche',
    'Select Field': 'Sélectionner un champ',
    'Selector display': 'Affichage du sélecteur',
    'Show selector': 'Afficher le sélecteur',
    'Word Max Length': 'Longueur maximale des mots',
    'Word Min Length': 'Longueur minimale des mots',
    'Specific task ID': 'Identifiant de tâche précis',
    'Task type': 'Type de tâche',
    'Table of Contents placement': 'Position de la table des matières',
    'Index archived items': 'Indexer les contenus archivés',
    'Select which taxonomies (filters) to create': 'Sélectionner les taxonomies (filtres) à créer',
    'Types to Index (aka searchable)': 'Types à indexer (recherchables)',
    'Browser Navigator': 'Navigation du navigateur',
    'Allow Joomla article manager to': 'Autoriser le gestionnaire d’articles Joomla à',
    'Allow Joomla category manager to': 'Autoriser le gestionnaire de catégories Joomla à',
    'Items with expired dates': 'Contenus avec dates expirées',
    'Max checked out hours': 'Durée maximale de verrouillage (heures)',
}

LABELS.update(MORE_LABELS)

# Phrases génériques, appliquées au texte hors des segments de code.
PHRASES = [
    ('Select sub-folder to be opened', 'Sélectionner le sous-dossier à ouvrir'),
    ('Select which types of autocomplete search will be allowed to the user', 'Sélectionner les types d’autocomplétion autorisés pour l’utilisateur'),
    ('Select which content types they want to include in their search', 'Sélectionner les types de contenu à inclure dans leur recherche'),
    ('Select FLEXIcontent types to be indexed by Finder', 'Sélectionner les types FLEXIcontent à indexer par Finder'),
    ('Select the category subtree', 'Sélectionner la sous-arborescence de catégories'),
    ('Select the default secondary categories', 'Sélectionner les catégories secondaires par défaut'),
    ('Select the default main category', 'Sélectionner la catégorie principale par défaut'),
    ('Select fields that will be show shown as a group', 'Sélectionner les champs affichés comme un groupe'),
    ('Select fields to hide labels if they have no value', 'Sélectionner les champs dont le libellé doit être masqué s’ils n’ont pas de valeur'),
    ('Select properties to show', 'Sélectionner les propriétés à afficher'),
    ('Select image to use instead of read more', 'Sélectionner l’image à utiliser à la place de « Lire la suite »'),
    ('Select class css to use instead of read more', 'Sélectionner la classe CSS à utiliser à la place de « Lire la suite »'),
    ('Select a specific task type to link to', 'Sélectionner un type de tâche précis à lier'),
    ('Select which category is considered current category', 'Sélectionner la catégorie considérée comme actuelle'),
    ('Select to view file in same / new window', 'Choisir d’afficher le fichier dans la même fenêtre ou une nouvelle'),
    ('Select which taxonomies (filters) to create', 'Sélectionner les taxonomies (filtres) à créer'),
    ('Please select one by one fields to add to textarea below.', 'Veuillez sélectionner les champs un par un pour les ajouter à la zone de texte ci-dessous.'),
    ('Please select a Task', 'Veuillez sélectionner une tâche'),
    ('Please enter a custom tile server URL', 'Veuillez saisir une URL de serveur de tuiles personnalisée'),
    ('Enter a custom tile server URL', 'Saisir une URL de serveur de tuiles personnalisée'),
    ('Enter a combination of b i u', 'Saisir une combinaison de b i u'),
    ('Enter Fields (their fieldnames) to render their values', 'Saisir les champs (leurs noms) dont les valeurs doivent être affichées'),
    ('Enter only integers without any suffix', 'Saisir uniquement des entiers sans suffixe'),
    ('Enter 256, to use 256 input samples', 'Saisir 256 pour utiliser 256 échantillons'),
    ('Allow to load more item in categorie view without relaoding page', 'Autoriser le chargement de contenus supplémentaires dans la vue catégorie sans recharger la page'),
    ('Allow users to select content types they want to include in their search', 'Autoriser les utilisateurs à sélectionner les types de contenu à inclure dans leur recherche'),
    ('Allow this to automatically archive or unpublish items', 'Activer cette option pour archiver ou dépublier automatiquement les contenus'),
    ('Enable this to allow privileged users', 'Activer cette option pour autoriser les utilisateurs privilégiés'),
    ('Enable this to automatically archive or unpublish items', 'Activer cette option pour archiver ou dépublier automatiquement les contenus'),
    ('Enable this property', 'Activer cette propriété'),
    ('Enable download limits', 'Activer les limites de téléchargement'),
    ('Disable to also use native APIs', 'Désactiver pour utiliser également les API natives'),
    ('Using the basic search index is faster and is recommended for LARGE SITES', 'L’utilisation de l’index de recherche de base est plus rapide et recommandée pour les GRANDS SITES'),
    ('Set yes to use search and filtering without page reloading', 'Réglage Oui pour utiliser la recherche et le filtrage sans rechargement de page'),
    ('Set gap between image blcok and top block', 'Définir l’espacement entre le bloc image et le bloc supérieur'),
    ('set gapp between colum and results', 'définir l’espacement entre la colonne et les résultats'),
    ('set width of column for left and right position', 'définir la largeur de la colonne pour les positions gauche et droite'),
    ('Show the label in the forms and on the site', 'Afficher le libellé dans les formulaires et sur le site'),
    ('Show intro/full images', 'Afficher les images intro/complètes'),
    ('Show extra text about current subscription status', 'Afficher un texte supplémentaire sur le statut actuel de l’abonnement'),
    ('Display your filter value like a badge', 'Afficher la valeur du filtre sous forme de badge'),
    ('Display content types as', 'Afficher les types de contenu sous forme de'),
    ('Display the path of parent categories', 'Afficher le chemin des catégories parentes'),
    ('Whether to show extra text', 'Indique s’il faut afficher un texte supplémentaire'),
    ('Whether the content is published', 'Indique si le contenu est publié'),
    ('Send email every N hits', 'Envoyer un e-mail tous les N affichages'),
    ('Bitrate will effect the quality of the audio preview', 'Le débit binaire influence la qualité de l’aperçu audio'),
    ('Uploaded files will be moved into this sub folder path', 'Les fichiers téléchargés seront déplacés dans ce sous-dossier'),
    ('For native media file manager, this is the folder inside Joomla ROOT', 'Pour le gestionnaire de médias natif, il s’agit du dossier situé dans la racine Joomla'),
    ('This is the image to show if item has no image', 'Image à afficher si le contenu n’a pas d’image'),
    ('You can use the HTML produced by any custom field in place of image', 'Vous pouvez utiliser le HTML produit par n’importe quel champ personnalisé à la place de l’image'),
    ('You can use the URL produced by any custom field in place of image', 'Vous pouvez utiliser l’URL produite par n’importe quel champ personnalisé à la place de l’image'),
    ('Leave blank: to use the above drop-down select box value', 'Laisser vide : pour utiliser la valeur de la liste déroulante ci-dessus'),
    ('image size and other parameters are not used', 'la taille de l’image et les autres paramètres ne sont pas utilisés'),
    ('image size and other parameters are applied to the given URL', 'la taille de l’image et les autres paramètres sont appliqués à l’URL fournie'),
    ('Number of featured items', 'Nombre de contenus en vedette'),
    ('Number of characters to keep after stripping HTML tags', 'Nombre de caractères à conserver après suppression des balises HTML'),
    ('Number of characters of content text shown of around each found search word', 'Nombre de caractères du texte affichés autour de chaque mot recherché trouvé'),
    ('Number of the last parent categories to show in the path', 'Nombre de dernières catégories parentes à afficher dans le chemin'),
    ('Number of files per period', 'Nombre de fichiers par période'),
    ('Length of the sliding period', 'Durée de la période glissante'),
    ('Length of the text area in the forms, in rows', 'Hauteur de la zone de texte dans les formulaires, en lignes'),
    ('Maximum allowed time an record', 'Durée maximale autorisée pendant laquelle un enregistrement'),
    ('Maximum characters length that search words are allowed to have', 'Longueur maximale autorisée pour les mots recherchés'),
    ('Minimum character length that search words are allowed to have', 'Longueur minimale autorisée pour les mots recherchés'),
    ('Height of the text area in the forms, in rows', 'Hauteur de la zone de texte dans les formulaires, en lignes'),
    ('Size is in points', 'La taille est exprimée en points'),
    ('Color of title background', 'Couleur de l’arrière-plan du titre'),
    ('Color of title text', 'Couleur du texte du titre'),
    ('Color of title', 'Couleur du titre'),
    ('Size of title text', 'Taille du texte du titre'),
    ('Left, right, center alignment of text', 'Alignement du texte à gauche, à droite ou au centre'),
    ('Indicates if borders must be drawn around the cell', 'Indique si des bordures doivent être tracées autour de la cellule'),
    ('Either leave this empty, which means regular font', 'Laissez ce champ vide pour la police normale'),
    ('Select a font-family to for the header text', 'Sélectionner une famille de police pour le texte d’en-tête'),
    ('Default appearance for custom column values', 'Apparence par défaut des valeurs des colonnes personnalisées'),
    ('Appearance of the filters box in the backend items list', 'Apparence de la boîte de filtres dans la liste backend des contenus'),
    ('Appearance of the content type tabs above the backend items list', 'Apparence des onglets des types de contenu au-dessus de la liste backend'),
    ('Used only when **Backend list filters** is **Modern**', 'Utilisé uniquement lorsque **Filtres de la liste backend** est **Moderne**'),
    ('changing a filter does not reload the list', 'la modification d’un filtre ne recharge pas la liste'),
    ('the list reloads on every change', 'la liste se recharge à chaque modification'),
    ('Full path: all parent categories', 'Chemin complet : toutes les catégories parentes'),
    ('Last items: only the last parent categories', 'Derniers éléments : uniquement les dernières catégories parentes'),
    ('Categories can have the same title in different branches', 'Des catégories peuvent porter le même titre dans différentes branches'),
    ('search also matches the words of the path', 'la recherche correspond également aux mots du chemin'),
    ('Use -1 for unlimited', 'Utilisez -1 pour une limite illimitée'),
    ('Groups not listed', 'Les groupes non listés'),
    ('When this list is set', 'Lorsque cette liste est définie'),
    ('one per line', 'un par ligne'),
    ('A hostname allows all ports', 'Un nom d’hôte autorise tous les ports'),
    ('allows only that port', 'n’autorise que ce port'),
    ('private network addresses', 'les adresses réseau privées'),
    ('public HTTP(S) hosts on standard ports', 'les hôtes HTTP(S) publics sur les ports standards'),
    ('with an exception for the verified site host', 'avec une exception pour l’hôte vérifié du site'),
    ('server-proxied downloads are restricted to listed hosts', 'les téléchargements via le serveur sont limités aux hôtes listés'),
    ('other downloads redirect the browser', 'les autres téléchargements redirigent le navigateur'),
    ('An empty list makes no automatic HTTP requests', 'Une liste vide n’effectue aucune requête HTTP automatique'),
    ('A supplied size takes precedence', 'Une taille fournie est prioritaire'),
    ('Checks use HEAD with a small Range GET fallback', 'Les vérifications utilisent HEAD avec un repli Range GET'),
    ('Failed or unsupported lookups leave the size at 0', 'Les recherches échouées ou non prises en charge laissent la taille à 0'),
    ('Batch imports and existing records are not automatically recalculated', 'Les imports par lot et les enregistrements existants ne sont pas recalculés automatiquement'),
    ('Every redirect must also match the list', 'Chaque redirection doit également correspondre à la liste'),
    ('including redirects to this site\'s own host', 'y compris les redirections vers l’hôte du site lui-même'),
    ('Shared-link coupons or the downloads cart bypass access levels', 'Les coupons de lien partagé ou le panier de téléchargements contournent les niveaux d’accès'),
    ('Select Yes to also apply the limits to them', 'Sélectionnez Oui pour appliquer également les limites à ces téléchargements'),
    ('every download counts, even of the same file', 'chaque téléchargement est compté, même pour le même fichier'),
    ('a file counts only once during the period', 'un fichier n’est compté qu’une fois pendant la période'),
    ('downloading it again is free', 'le télécharger à nouveau est gratuit'),
    ('Guests are limited per browser (cookie)', 'Les invités sont limités par navigateur (cookie)'),
    ('To stop quota resets by clearing cookies', 'Pour éviter la réinitialisation du quota en effaçant les cookies'),
    ('they are also limited per IP address', 'ils sont également limités par adresse IP'),
    ('at the group limit multiplied by this number', 'à la limite du groupe multipliée par ce nombre'),
    ('so several visitors behind one IP address', 'afin que plusieurs visiteurs derrière une même adresse IP'),
    ('do not share a single quota', 'ne partagent pas un seul quota'),
    ('Master switch for the whole site', 'Interrupteur principal pour tout le site'),
    ('can use these settings, use its own settings, or have no limits', 'peuvent utiliser ces paramètres, leurs propres paramètres ou aucune limite'),
    ('HTML shown in a modal window', 'HTML affiché dans une fenêtre modale'),
    ('when a user with an exhausted quota clicks a disabled download button', 'lorsqu’un utilisateur dont le quota est épuisé clique sur un bouton de téléchargement désactivé'),
    ('text and a Register / Subscribe button', 'un texte et un bouton Inscription / Abonnement'),
    ('Leave empty for the default message', 'Laissez vide pour le message par défaut'),
    ('time until the next download is possible', 'temps restant avant le prochain téléchargement possible'),
    ('the period is sliding, so the oldest download expires first', 'la période est glissante, donc le téléchargement le plus ancien expire en premier'),
    ('time until the counter is back to zero', 'temps restant avant que le compteur revienne à zéro'),
    ('length of the period', 'durée de la période'),
    ('Minutes, hours or days', 'Minutes, heures ou jours'),
    ('Download records older than this period are deleted automatically', 'Les enregistrements de téléchargement plus anciens que cette période sont supprimés automatiquement'),
    ('with a limit of 1 file', 'avec une limite de 1 fichier'),
    ('not more than one download every 5 minutes', 'pas plus d’un téléchargement toutes les 5 minutes'),
    ('Choose \'Stable\' for production sites', 'Choisissez « Stable » pour les sites de production'),
    ('Choose \'Beta\' to receive pre-release versions for testing', 'Choisissez « Beta » pour recevoir les versions préliminaires de test'),
    ('Beta versions may contain bugs', 'Les versions Beta peuvent contenir des bugs'),
    ('By defaut %%', 'Par défaut %%'),
    ('SQL tables initialized', 'Tables SQL initialisées'),
    ('A text to be used as email body message', 'Texte utilisé comme corps de l’e-mail'),
    ('when sending the item edit link', 'lors de l’envoi du lien de modification du contenu'),
    ('Cancel item creation', 'Annuler la création du contenu'),
    ('Assign new item', 'Attribuer un nouveau contenu'),
    ('Let this be empty to use language of current user', 'Laissez ce champ vide pour utiliser la langue de l’utilisateur actuel'),
    ('Let this be zero for default menu item', 'Laissez cette valeur à zéro pour l’élément de menu par défaut'),
    ('SQL date expression', 'expression SQL de date'),
    ('Filter items list using other fields', 'Filtrer la liste des contenus à l’aide d’autres champs'),
    ('noembed API only', 'API noembed uniquement'),
    ('noembed API and native APIs', 'API noembed et API natives'),
    ('Open New Window', 'Ouvrir dans une nouvelle fenêtre'),
    ('Open Same Window', 'Ouvrir dans la même fenêtre'),
    ('Buttons position after search', 'Boutons après la recherche'),
    ('Buttons position after advsearch', 'Boutons après la recherche avancée'),
    ('Basic Index (faster, fields not selectable)', 'Index de base (plus rapide, champs non sélectionnables)'),
    ('Advanced Index (use configured fields)', 'Index avancé (utilise les champs configurés)'),
    ('Advanced Index (use configured fields, allow user selection)', 'Index avancé (utilise les champs configurés, autorise la sélection utilisateur)'),
    ('Modules field value nocaching', 'Valeur du champ Modules sans cache'),
    ('Download via (file-based) form field', 'Téléchargement via un champ de formulaire (fichier)'),
    ('File links via \'File\' XTD Editor button', 'Liens de fichiers via le bouton éditeur « Fichier »'),
    ('Download mutliple files as a compressed archive', 'Télécharger plusieurs fichiers sous forme d’archive compressée'),
    ('Web-link via a weblink form field', 'Lien web via un champ formulaire Weblink'),
    ('Items container\'s background color', 'Couleur d’arrière-plan du conteneur des contenus'),
    ('This is the background color applied at each item', 'Couleur d’arrière-plan appliquée à chaque contenu'),
    ('This is the border color applied around the items', 'Couleur de bordure appliquée autour des contenus'),
    ('This is the border width applied around the items', 'Largeur de bordure appliquée autour des contenus'),
    ('Items container\'s margin applied at top and bottom of the items', 'Marge du conteneur appliquée en haut et en bas des contenus'),
    ('Items container\'s margin applied at left and right of the items', 'Marge du conteneur appliquée à gauche et à droite des contenus'),
    ('This is the margin applied at left and right of the items', 'Marge appliquée à gauche et à droite des contenus'),
    ('This is the margin applied at top and bottom of the items', 'Marge appliquée en haut et en bas des contenus'),
    ('Items container\'s padding applied at left and right of the items', 'Remplissage du conteneur appliqué à gauche et à droite des contenus'),
    ('Items container\'s padding applied at top and bottom of the items', 'Remplissage du conteneur appliqué en haut et en bas des contenus'),
    ('This is the padding applied at left and right of the items', 'Remplissage appliqué à gauche et à droite des contenus'),
    ('This is the padding applied at top and bottom of the items', 'Remplissage appliqué en haut et en bas des contenus'),
    ('This is span1 to span12 (100% width)', 'La valeur va de span1 à span12 (largeur 100 %)'),
    ('Note \'Top\' position is next to \'Image\' position the sum of them is 12', 'Notez que la position « Top » est adjacente à la position « Image » ; leur somme vaut 12'),
    ('If one position is empty the other is expaned to 100%', 'Si une position est vide, l’autre est étendue à 100 %'),
    ('paddng-top padding-right padding-bottom padding-left in px % rem ect', 'paddng-top padding-right padding-bottom padding-left en px % rem, etc.'),
    ('This is the background color applied at each item', 'Couleur d’arrière-plan appliquée à chaque contenu'),
    ('Select FLEXIcontent types to be indexed by Finder. (Leave empty to index all types)', 'Sélectionner les types FLEXIcontent à indexer par Finder. (Laissez vide pour indexer tous les types)'),
    ('Leave empty to index all types', 'Laissez vide pour indexer tous les types'),
    ('Hide Categories from Pathway/URLs for Types', 'Masquer les catégories du fil d’Ariane / des URL pour les types'),
    ('not being a part of structure but rather general information content', 'ne font pas partie de la structure mais contiennent des informations générales'),
    ('like site usage instructions or license agreement, etc', 'comme les instructions d’utilisation du site ou un contrat de licence, etc.'),
    ('direct category links', 'les liens directs vers les catégories'),
    ('category title as a content/content list markup', 'le titre de la catégorie comme balisage de contenu / liste'),
    ('These categories are for special purposes', 'Ces catégories ont un usage particulier'),
    ('contain items **displayed** in frontpage or in a module Slideshow', 'contiennent des éléments **affichés** en page d’accueil ou dans un diaporama de module'),
    ('if you have trouble with some URLs unwantingly redirecting', 'si certaines URL sont redirigées de manière indésirable'),
    ('you can enter here a sub-string of them', 'vous pouvez saisir ici une sous-chaîne de celles-ci'),
    ('in order to exclude them from redirection', 'afin de les exclure de la redirection'),
    ('Seperate urls with %% DO NOT add new line characters', 'Séparez les URL par %% N’ajoutez pas de caractères de nouvelle ligne'),
    ('All non-selected usergroups will be redirected', 'Tous les groupes d’utilisateurs non sélectionnés seront redirigés'),
    ('after items have expired, do not change item state', 'après expiration des contenus, ne modifiez pas leur état'),
    ('and do not clear publish down date', 'et n’effacez pas la date de fin de publication'),
    ('Action to do when clicking on the marker', 'Action à effectuer lors du clic sur le marqueur'),
    ('This is by default same as the popup windows', 'Par défaut, identique aux fenêtres contextuelles'),
    ('Same display as markers list', 'Même affichage que la liste des marqueurs'),
    ('At this width the marker list will wrap to the bottom of the map', 'À cette largeur, la liste des marqueurs passe sous la carte'),
    ('Default zoom level for near-me locations', 'Niveau de zoom par défaut pour la géolocalisation « Near Me »'),
    ('Group markers as a total number', 'Regrouper les marqueurs en un nombre total'),
    ('to prevent many markers showing very close together', 'afin d’éviter que de nombreux marqueurs très proches ne s’affichent'),
    ('Allow to load more item in categorie view', 'Autoriser le chargement de contenus supplémentaires dans la vue catégorie'),
    ('Load more = display a load more button editable with language string', 'Charger plus = afficher un bouton « Charger plus » modifiable via une clé de langue'),
    ('Scrolling = load item automaticly on scroll down user', 'Défilement = charger les contenus automatiquement lorsque l’utilisateur fait défiler vers le bas'),
    ('Load more and scrolling option disable pagination with number', 'Les options Charger plus et Défilement désactivent la pagination numérotée'),
    ('No = classic pagination', 'Non = pagination classique'),
    ('you have not enabled short word search in component', 'vous n’avez pas activé la recherche de mots courts dans le composant'),
    ('word is &lt; 4 characters', 'le mot compte moins de 4 caractères'),
    ('word is too common', 'le mot est trop courant'),
    ('appears in about half of the articles', 'présent dans environ la moitié des articles'),
    ('wrong language or article not publish or article has expired', 'langue incorrecte, article non publié ou article expiré'),
    ('single or multiple value allowed', 'une ou plusieurs valeurs sont autorisées'),
    ('this depends on target view', 'cela dépend de la vue cible'),
    ('the options configured below will still be used', 'les options configurées ci-dessous sont quand même utilisées'),
    ('when advanced search options box is hidden', 'lorsque la boîte des options de recherche avancée est masquée'),
    ('Fields marked as advanced index filters', 'Champs marqués comme filtres de l’index avancé'),
    ('Fields marked as advanced index text-searchable', 'Champs marqués comme recherchables dans l’index avancé'),
    ('only fields marked as advanced index filters are listed', 'seuls les champs marqués comme filtres de l’index avancé sont listés'),
    ('only fields marked as advanced index text-searchable are listed', 'seuls les champs marqués comme recherchables dans l’index avancé sont listés'),
    ('Limit maximum number of results the plugin can return', 'Limiter le nombre maximal de résultats renvoyés par le plugin'),
    ('The content types the search will include', 'Les types de contenu inclus dans la recherche'),
    ('selecting none will include ALL', 'ne rien sélectionner inclut TOUS les types'),
    ('You can allow user to select Content Types', 'Vous pouvez autoriser l’utilisateur à sélectionner les types de contenu'),
    ('the selection list will be LIMITED to display ONLY the types specified here', 'la liste de sélection sera LIMITÉE aux types indiqués ici'),
    ('You can separate each fieldname by comma(,)', 'Vous pouvez séparer les noms de champs par une virgule (,)'),
    ('Depending on target view', 'Selon la vue cible'),
    ('This plugin indexes FLEXIcontent items', 'Ce plugin indexe les contenus FLEXIcontent'),
    ('Sends notifications to users when favouriting an item', 'Envoie des notifications aux utilisateurs lorsqu’ils ajoutent un contenu aux favoris'),
    ('FLEXIcontent alternative to standard pagebreak plugin', 'Alternative FLEXIcontent au plugin standard de saut de page'),
    ('Displays a button in textarea editor for inserting links', 'Affiche un bouton dans l’éditeur pour insérer des liens'),
    ('Displays a popup allowing you to choose the', 'Affiche une fenêtre permettant de choisir le'),
    ('Content listings and more, in a module position', 'Listes de contenus et plus, dans une position de module'),
    ('This module displays a simple search form that links to FLEXIcontent advanced search view', 'Ce module affiche un formulaire de recherche simple qui renvoie vers la vue de recherche avancée FLEXIcontent'),
    ('This module displays a list of categories from one parent category', 'Ce module affiche une liste de catégories issues d’une catégorie parente'),
    ('This module displays a form that filters the item listing of', 'Ce module affiche un formulaire qui filtre la liste des contenus de'),
    ('Module to display a googlemap with item like marker', 'Module permettant d’afficher une carte Google avec les contenus comme marqueurs'),
    ('Tags Cloud Module for FLEXIcontent', 'Module de nuage d’étiquettes pour FLEXIcontent'),
    ('FLEXIcontent plugin for JSitemap', 'Plugin FLEXIcontent pour JSitemap'),
    ('OSMap Plugin for FLEXIcontent Component', 'Plugin OSMap pour le composant FLEXIcontent'),
    ('System Plugin for FLEXIcontent Advanced Routing', 'Plugin système pour le routage avancé FLEXIcontent'),
]

VALUES = dict(MORE_VALUES)
PHRASES.extend(MORE_PHRASES)

# Les libellés d'options sont remplacés entièrement (sous forme de mots), afin
# de ne pas toucher aux clés techniques placées avant le signe « = ».
_VALUE_PATTERNS = [
    (re.compile(r'(?<!\w)' + re.escape(key) + r'(?!\w)'), value)
    for key, value in sorted(VALUES.items(), key=lambda item: -len(item[0]))
]

# Les noms de langues sont appliqués après la restauration du code, pour
# couvrir les libellés d'options et les valeurs par défaut entre backticks.
_LANGUAGE_PATTERNS = [
    (re.compile(r'(?<!\w)' + re.escape(key) + r'(?!\w)', re.IGNORECASE), value)
    for key, value in sorted(MORE_LANGUAGES.items(), key=lambda item: -len(item[0]))
]


def _protect_code(line):
    """Remplace temporairement les segments de code pour éviter de les traduire."""
    placeholders = {}

    def store(match):
        i = len(placeholders)
        key = f'@@FC{i}@@'
        placeholders[key] = match.group(0)
        return key

    # Les destinations de liens Markdown doivent rester telles quelles : un
    # remplacement de « Categories » par « Catégories » ne doit pas réécrire
    # `../concepts/categories.md` en `../concepts/catégories.md`.
    line = re.sub(r'\]\([^)]*\)', store, line)
    line = re.sub(r'`[^`]*`', store, line)
    line = re.sub(r'&#123;[^&]*?&#125;', store, line)
    line = re.sub(r'__[A-Za-z0-9_]+__|%%[A-Za-z0-9_]+%%', store, line)
    return line, placeholders


def _restore_code(line, placeholders):
    for key, value in placeholders.items():
        line = line.replace(key, value)
    return line


def _apply_phrase(line, english, french):
    """Remplace une phrase en conservant la casse initiale."""
    pattern = re.compile(r'(?<!\w)' + re.escape(english) + r'(?!\w)', re.IGNORECASE)

    def repl(match):
        value = match.group(0)
        if value[:1].isupper():
            return french[:1].upper() + french[1:]
        return french[:1].lower() + french[1:]

    return pattern.sub(repl, line)


def translate_content(text):
    """Traduire les textes anglais restants d’une page française."""
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped in EXACT:
            lines.append(line.replace(stripped, EXACT[stripped], 1))
            continue

        protected, placeholders = _protect_code(line)

        # Libellés en gras.
        for english, french in LABELS.items():
            protected = protected.replace(f'**{english}**', f'**{french}**')

        # Libellés affichés des valeurs d'options (jamais les clés techniques).
        for pattern, french in _VALUE_PATTERNS:
            protected = pattern.sub(french, protected)

        # Phrases génériques, les plus longues d'abord.
        for english, french in sorted(PHRASES, key=lambda item: -len(item[0])):
            if english.lower() in protected.lower():
                protected = _apply_phrase(protected, english, french)

        restored = _restore_code(protected, placeholders)
        for pattern, french in _LANGUAGE_PATTERNS:
            restored = pattern.sub(french, restored)
        lines.append(restored)
    return '\n'.join(lines) + ('\n' if text.endswith('\n') else '')


def translate_file(path):
    content = path.read_text(encoding='utf-8')
    translated = translate_content(content)
    if translated != content:
        path.write_text(translated, encoding='utf-8')
        return True
    return False
