# -*- coding: utf-8 -*-
"""."""

from PySide6.QtCore import QObject, Slot


class MainWindow(QObject):
    def __init__(self):
        super().__init__()

    @Slot(str, result=str)
    def to_upper(self, text):
        return f'\nPython: {text.upper()}!'


if __name__ == '__main__':
    print('[X]Run the app.py file[X]')
