# -*- coding: utf-8 -*-
"""."""

import sys

from PySide6 import QtCore, QtGui, QtQml

try:
    import resources_rc
    from settings import conf
    from ui.MainWindow import MainWindow
    from ui.MenuBar import MenuBar
except ImportError:
    from app_name import resources_rc
    from app_name.settings import conf
    from app_name.ui.MainWindow import MainWindow
    from app_name.ui.MenuBar import MenuBar

RESOURCES_RC = resources_rc


def main() -> None:
    application = QtGui.QGuiApplication(sys.argv)
    application.setApplicationDisplayName(conf.APP_ID)
    application.setApplicationName(conf.APP_ID)
    application.setDesktopFileName(conf.APP_ID)
    application.setOrganizationName(conf.ORGANIZATION_NAME)
    application.setOrganizationDomain(conf.ORGANIZATION_DOMAIN)

    loc = QtCore.QLocale.system()
    translator = QtCore.QTranslator(application)
    if translator.load(QtCore.QLocale(loc), conf.APP_ID, '.', ':/locales'):
        application.installTranslator(translator)

    if QtCore.QSysInfo.productType() == 'windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(conf.APP_ID)

    mainWindow = MainWindow()
    menubar = MenuBar()

    engine = QtQml.QQmlApplicationEngine()
    engine.rootContext().setContextProperty('mainWindow', mainWindow)
    engine.rootContext().setContextProperty('menubar', menubar)
    engine.load(QtCore.QUrl('qrc:/ui/MainWindow.qml'))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(application.exec())


if __name__ == '__main__':
    main()
