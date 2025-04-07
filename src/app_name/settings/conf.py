# -*- coding: utf-8 -*-
"""."""

import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent
APP_DIR = BASE_DIR.parent

HOME = pathlib.Path.home()

APP_ID = 'com.github.natorsc.Pyqml'
ORGANIZATION_NAME = APP_ID.split('.')[2]
ORGANIZATION_DOMAIN = '.'.join(APP_ID.split('.')[0:3])
