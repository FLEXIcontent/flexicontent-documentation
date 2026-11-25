---
sidebar_position: 13
---

# Fichiers

Répertoires de téléversement, extensions autorisées et gestion des images.

:::info Source
Cette page est générée depuis `admin/config.xml` et les fichiers de langue officiels `en-GB.com_flexicontent.ini` / `fr-FR.com_flexicontent.ini` de FLEXIcontent 5.x.
:::

### Configuration des fichiers

#### Configuration des fichiers

## Basique

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Afficher le fichier de langue comme**<br />`display_file_lang_as` | Selectionner l'apparence/comportement du fichier de langue | — | `0` |

#### Dossier

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Chemin de fichiers sécurisés**<br />`file_path` | Le répertoire où seront stockés les fichiers sécurisés uploadés sur le site. Vous pouvez changer le répertoire par défaut pour augmenter votre niveau de sécurité. | — | `components/com_flexicontent/uploads` |
| **Chemin de fichiers multimédia**<br />`media_path` | Le répertoire où seront stockés les médias sur le site. Ce répertoire est visible dans le code source et sera utilisé pour la lecture des médias. | — | `components/com_flexicontent/medias` |

#### Index de recherche

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Indexer les fichiers PDF**<br />`index_pdf_files` | Ajouter le contenu des fichiers PDF dans l'index de recherche (seulement le texte) | — | `0` |
| **Chemin de l'indexeur PDF**<br />`pdfparser_path` | Ceci est le chemin vers la bibliothèque nécessaire pour analyser les fichiers PDF, voir https://github.com/smalot/pdfparsers Veuillez télécharger & extraire la bibliothèque à partir de l'URL donnée dans le dossier puis lancer le composer à l'intérieur | — | — |
| **Indexer les fichiers CSV**<br />`index_csv_files` | Ajouter le contenu des fichiers CSV dans l'index de recherche | — | `0` |

## Éditeur de fichiers

:::note
Choisissez les champs affichés lors de la modification d’un fichier. Les champs masqués conservent leurs valeurs enregistrées. Les paramètres avancés nécessitent toujours l’autorisation propriétés de fichier.
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Nom du fichier téléchargé**<br />`file_editor_show_download_filename` | — | — | `1` |
| **Titre**<br />`file_editor_show_title` | — | — | `1` |
| **Description**<br />`file_editor_show_description` | — | — | `1` |
| **Remplacement du fichier**<br />`file_editor_show_replace` | — | — | `1` |
| **Conserver la date d’envoi d’origine**<br />`file_editor_show_keep_uploaded_date` | — | — | `1` |
| **Conserver l’auteur de l’envoi d’origine**<br />`file_editor_show_keep_uploaded_by` | — | — | `1` |
| **Langue**<br />`file_editor_show_language` | — | — | `1` |
| **Accès**<br />`file_editor_show_access` | — | — | `1` |
| **Estampille du téléchargement**<br />`file_editor_show_stamp` | — | — | `1` |
| **Nombre de vues**<br />`file_editor_show_hits` | — | — | `1` |
| **Type de fichier**<br />`file_editor_show_type` | — | — | `1` |
| **Taille du fichier**<br />`file_editor_show_size` | — | — | `1` |
| **Nom de fichier / URL de stockage**<br />`file_editor_show_storage` | — | — | `1` |
| **Chemin serveur**<br />`file_editor_show_path` | — | — | `0` |

:::note
Ces paramètres s’appliquent aux formulaires du gestionnaire de fichiers (ajout / modification de fichiers hors d’un champ Fichier). Si une propriété n’est pas activée ici, les paramètres du premier champ Fichier qui l’active sont utilisés. Chaque champ Fichier possède ses propres paramètres (onglet Champ du formulaire, Modifier les propriétés), utilisés lorsque les fichiers sont modifiés via ce champ
:::

#### Propriété de fichier personnalisée 1 (HTML)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer**<br />`file_custom1_enable` | Activer cette propriété : elle est affichée sous la description dans les formulaires d’ajout/modification et sur le site lorsqu’elle n’est pas vide | — | `0` |
| **Libellé**<br />`file_custom1_label` | Texte du libellé. Vous pouvez saisir une clé de langue (elle sera traduite si elle existe) | — | — |
| **Afficher le libellé**<br />`file_custom1_label_show` | Afficher le libellé dans les formulaires et sur le site | — | `1` |
| **Par défaut**<br />`file_custom1_default` | Valeur par défaut (HTML autorisé). Son utilisation est contrôlée par le paramètre ci-dessous | — | — |
| **Hauteur du champ (lignes)**<br />`file_custom1_rows` | Hauteur de la zone de texte dans les formulaires, en lignes (1 - 30) | — | `2` |
| **Utilisation par défaut**<br />`file_custom1_default_use` | Sélectionner lorsque cette propriété par défaut sera utilisée. | — | `0` |

#### Propriété de fichier personnalisée 2 (HTML)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer**<br />`file_custom2_enable` | Activer cette propriété : elle est affichée sous la description dans les formulaires d’ajout/modification et sur le site lorsqu’elle n’est pas vide | — | `0` |
| **Libellé**<br />`file_custom2_label` | Texte du libellé. Vous pouvez saisir une clé de langue (elle sera traduite si elle existe) | — | — |
| **Afficher le libellé**<br />`file_custom2_label_show` | Afficher le libellé dans les formulaires et sur le site | — | `1` |
| **Par défaut**<br />`file_custom2_default` | Valeur par défaut (HTML autorisé). Son utilisation est contrôlée par le paramètre ci-dessous | — | — |
| **Hauteur du champ (lignes)**<br />`file_custom2_rows` | Hauteur de la zone de texte dans les formulaires, en lignes (1 - 30) | — | `2` |
| **Utilisation par défaut**<br />`file_custom2_default_use` | Sélectionner lorsque cette propriété par défaut sera utilisée. | — | `0` |

## Limites

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Taille maximum**<br />`upload_maxsize` | Spécifie la taille maximum d'un fichier qui peut être uploadé sur le site (en octet). Utiliser 0 pour ne mettre aucune limite. NOTE : la taille maximum dépend également de la configuration de votre serveur. | — | `10000000` |
| **Extensions autorisées**<br />`upload_extensions` | Les extensions (types de fichier) que vous êtes autorisés à envoyer pour une image (séparé par virgule). | — | `bmp,wbmp,csv,doc,docx,webp,gif,ico,jpg,jpeg,odg,odp,ods,odt,pdf,png,ppt,pptx,txt,xcf,xls,xlsx,zip,ics` |

#### Fichiers distants (URL)

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Hôtes distants de confiance**<br />`remote_trusted_hosts` | Noms d’hôte des serveurs de fichiers externes, un par ligne. Un nom d’hôte autorise tous les ports ; host:port n’autorise que ce port. Les hôtes listés peuvent utiliser des adresses réseau privées. Sinon, les vérifications de taille et les téléchargements autorisent les hôtes HTTP(S) publics sur les ports standards, à l’exception de l’hôte vérifié du site. Lorsque cette liste est définie, les téléchargements via le serveur sont limités aux hôtes listés et à l’hôte du site ; les autres téléchargements redirigent le navigateur. La détection automatique de la taille lors de l’ajout ou de l’enregistrement d’une URL nécessite l’option ci-dessous et un hôte explicitement listé. | — | — |
| **Lire automatiquement la taille des fichiers URL de confiance**<br />`remote_probe_size` | Lors de l’ajout ou de l’enregistrement d’un fichier URL sans taille fournie, tentez de lire sa taille depuis un serveur listé dans les hôtes distants de confiance. Chaque redirection doit également correspondre à la liste, y compris vers l’hôte du site. Désactivé par défaut ; une liste vide n’effectue aucune requête HTTP automatique. Une taille fournie est prioritaire. Les recherches échouées ou non prises en charge laissent la taille à 0. Les vérifications utilisent HEAD avec un repli Range GET et partagent un court délai d’attente HTTP lors de l’enregistrement. Les imports par lot et les enregistrements existants ne sont pas recalculés automatiquement. | — | `0` |

#### Redimensionner automatiquement les images

:::note
Redimensionnement se fera au niveau du navigateur de l’utilisateur, ainsi vous obtenez un téléchargement plus rapide et moins de consommation sur l’espace serveur
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Redimensionnement**<br />`resize_on_upload` | Redimensionner une image téléchargée afin d'économiser de l’espace sur le serveur et d'accélérer les téléchargements, cela sera la taille pour le client (tous les modes ne supportes pas cette fonction) | — | `1` |
| **Largeur de l'image**<br />`upload_max_w` | — | — | `4000` |
| **Hauteur de l'image**<br />`upload_max_h` | — | — | `3000` |
| **Méthode de traitement**<br />`upload_method` | Méthode de traitement permettant de générer la miniature à l'échelle: redimensionne image proportionnellement (hauteur largeur). découper: redimensionne l'image et dès que la hauteur ou la largeur maximum est atteinte, l'autre dimension sera automatiquement tronquée. | — | `0` |

## Limites de téléchargement

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Activer les limites de téléchargement**<br />`dl_limit_enable` | Interrupteur principal pour tout le site. Chaque champ Fichier / Fichier média peut utiliser ces paramètres, ses propres paramètres ou aucune limite. | — | `0` |

:::note
Limitez le nombre de fichiers que chaque groupe d’utilisateurs peut télécharger sur une période (minutes, heures ou jours), pour tous les champs utilisant ces limites. Les téléchargements sont comptés par utilisateur connecté, et par visiteur (cookie + IP) pour les invités. Un groupe hérite de la limite de ses groupes parents ; si plusieurs groupes correspondent, la limite la plus élevée s’applique. Les super utilisateurs ne sont jamais limités.
:::

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Mode de comptage**<br />`dl_limit_count_mode` | Tout fichier : chaque téléchargement est compté, même pour le même fichier. Fichier unique : un fichier n’est compté qu’une fois pendant la période, le télécharger à nouveau est gratuit. | — | `0` |
| **Période**<br />`dl_limit_window` | Durée de la période glissante, avec l’unité définie ci-dessous. Par exemple 24 heures, 30 jours ou 5 minutes (avec une limite de 1 fichier : pas plus d’un téléchargement toutes les 5 minutes). Les enregistrements de téléchargement plus anciens que cette période sont supprimés automatiquement. | — | `24` |
| **Unité de la période**<br />`dl_limit_window_unit` | Minutes, heures ou jours. | — | `60` |
| **Limite par groupe d’utilisateurs**<br />`dl_limit_groups` | Nombre de fichiers par période. Utilisez -1 pour une limite illimitée. Les groupes non listés (et qui n’héritent pas d’un groupe parent listé) ne sont pas limités. | — | — |
| **Quota IP invité (multiplicateur)**<br />`dl_limit_guest_ip_factor` | Les invités sont limités par navigateur (cookie). Pour éviter la réinitialisation du quota en effaçant les cookies, ils sont aussi limités par adresse IP, à la limite du groupe multipliée par ce nombre, afin que plusieurs visiteurs derrière une même adresse IP (bureau, école) ne partagent pas un seul quota. | — | `5` |
| **Compter les téléchargements via coupons / panier**<br />`dl_limit_count_special` | Les téléchargements via coupons de lien partagé ou le panier de téléchargements contournent les niveaux d’accès. Sélectionnez Oui pour appliquer également les limites à ces téléchargements. | — | `0` |
| **Limite atteinte : HTML de la fenêtre modale**<br />`dl_limit_modal_html` | HTML affiché dans une fenêtre modale lorsqu’un utilisateur dont le quota est épuisé clique sur un bouton de téléchargement désactivé, par exemple un texte et un bouton Inscription / Abonnement. Laissez vide pour le message par défaut. Espaces réservés : **&#123;reset_in&#125;** temps avant le prochain téléchargement possible (la période est glissante, donc le téléchargement le plus ancien expire en premier), **&#123;reset_full_in&#125;** temps avant que le compteur revienne à zéro, **&#123;reset_seconds&#125;** identique à &#123;reset_in&#125; en secondes, **&#123;limit&#125;** fichiers autorisés, **&#123;used&#125;** fichiers utilisés, **&#123;window&#125;** durée de la période, par exemple 5 min, 24 h, 7 j. | — | — |

## Vérifier le contenus des fichiers

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Restrictions de téléversement**<br />`restrict_uploads` | Vérifie les types de fichiers en examinant le contenu et en empêchant le chargement de types non autorisés | — | `1` |

#### Extensions

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Extensions d'images autorisées**<br />`image_extensions` | Les extensions (types de fichier) que vous êtes autorisés à envoyer pour une image (séparé par virgule). | — | `bmp,wbmp,gif,jpg,jpeg,png,webp,ico` |
| **Extensions non vérifiées**<br />`ignore_extensions` | Ignorer les fichiers pour les fichiers de type MIME et restreindre les envois. | — | — |

#### Type MIME

| Option | Description | Valeurs | Défaut |
| --- | --- | --- | --- |
| **Types MIME bloqués**<br />`upload_mime_illegal` | Liste noire des types MIME séparées par des virgules. | — | `text/html` |
| **Types MIME autorisés**<br />`upload_mime` | Liste des types MIME ,séparés par des virgules, qui sont autorisés pour le téléversement. | — | `image/jpeg,image/gif,image/png,image/bmp,application/msword,application/excel,application/pdf,application/powerpoint,text/plain,application/x-zip` |

#### Configuration des fichiers
