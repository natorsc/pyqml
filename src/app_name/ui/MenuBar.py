# -*- coding: utf-8 -*-
"""."""

import shutil

from PySide6.QtCore import QObject, Slot

try:
    from settings import conf
except ImportError:
    from app_name.settings import conf


APPLICATIONS_DIR = conf.HOME / '.local' / 'share' / 'applications'

ICONS_DIR = conf.HOME / '.icons'
APP_ICON = conf.APP_DIR / 'data' / 'icons' / f'{conf.APP_ID}.png'

DESKTOP_ENTRY = APPLICATIONS_DIR / f'{conf.APP_ID}.desktop'
DESKTOP_ENTRY_TEMPLATE = f"""[Desktop Entry]
Categories=Development;
Comment=Graphical interface with Python and Kirigami.
Exec=python3 app.py
Icon={ICONS_DIR / f'{conf.APP_ID}.png'}
Name=PyQML
Path={conf.APP_DIR}
StartupNotify=true
Terminal=false
Type=Application
Version=1.0
"""


class MenuBar(QObject):
    def __init__(self):
        super().__init__()

    @Slot()
    def create_desktop_entry(self):
        if not APPLICATIONS_DIR.exists():
            APPLICATIONS_DIR.mkdir(parents=True, exist_ok=True)
        with open(file=DESKTOP_ENTRY, mode='w', encoding='utf-8') as f:
            f.write(DESKTOP_ENTRY_TEMPLATE)
            f.close()
        if not ICONS_DIR.exists():
            ICONS_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copy2(APP_ICON, ICONS_DIR)


if __name__ == '__main__':
    print('[X]Run the app.py file[X]')
