#!/usr/bin/env python3
"""Applique les traductions FR de secours aux pages françaises existantes.

Utile après une mise à jour des fichiers de langue officiels ou des modèles de
traduction : les pages générées peuvent contenir des chaînes non traduites en
amont. Les générateurs appellent déjà fr_translations.translate_content(), ce
script permet de retoucher uniquement les fichiers FR déjà présents.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import fr_translations  # noqa: E402

FR_DOCS = HERE.parent / 'i18n' / 'fr' / 'docusaurus-plugin-content-docs' / 'current'


def main():
    changed = []
    for path in sorted(FR_DOCS.rglob('*.md')):
        if fr_translations.translate_file(path):
            changed.append(path.relative_to(FR_DOCS))
    print(f'{len(changed)} page(s) FR mise(s) à jour')
    for path in changed:
        print(f'  {path}')


if __name__ == '__main__':
    main()
