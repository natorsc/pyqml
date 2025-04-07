# -*- coding: utf-8 -*-
"""."""

import pathlib
import subprocess

APP_ID = 'com.github.natorsc.Pyqml'

BASE_DIR = pathlib.Path(__file__).resolve().parent

LOC_DIR = BASE_DIR / 'locales'
QML_DIR = BASE_DIR / 'ui'
APP_DIR = BASE_DIR.parent / 'src' / 'app_name'

QRC_FILE = BASE_DIR / 'resources.qrc'

SRC_LANG = 'en_US'
TGT_LANG = ['pt_BR']


def main() -> None:
    format_qml_files()
    create_or_update_translations()
    compile_translations()
    create_resources()


def format_qml_files() -> None:
    print('[!] Formatting *.qml files, please wait... [!]')
    for file in QML_DIR.rglob('*.qml'):
        if file.is_file() and file.suffix == '.qml':
            subprocess.run(
                args=[
                    'pyside6-qmlformat',
                    '-i',
                    '-n',
                    '--objects-spacing',
                    '--functions-spacing',
                    file,
                ],
                check=False,
            )
    print('[!] Done [!]\n')


def create_or_update_translations() -> None:
    print('[!] Updating the translations (*.ts), please wait... [!]')
    for lang in TGT_LANG:
        output = LOC_DIR.joinpath(f'{APP_ID}.{lang}.ts')
        output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            args=[
                'pyside6-lupdate',
                '-silent',
                # '-no-obsolete',
                '-extensions',
                'py,qml',
                '-source-language',
                SRC_LANG,
                '-target-language',
                lang,
                BASE_DIR,
                APP_DIR,
                '-ts',
                output,
            ],
            check=False,
        )
    print('[!] Done [!]\n')


def compile_translations() -> None:
    print('[!] Compiling the translations (*.qm), please wait... [!]')
    for file in LOC_DIR.rglob('*.ts'):
        if file.is_file() and file.suffix == '.ts':
            output = file.parent.joinpath(f'{file.stem}.qm')
            subprocess.run(
                args=['pyside6-lrelease', '-silent', file, output],
                check=False,
            )
    print('[!] Done [!]\n')


def create_resources() -> None:
    print('[!] Creating resources, please wait... [!]')
    output = APP_DIR / 'resources_rc.py'
    subprocess.run(
        args=['pyside6-rcc', QRC_FILE, '-o', output],
        check=False,
    )
    print('[!] Done [!]')


if __name__ == '__main__':
    main()
