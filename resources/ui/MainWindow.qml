import QtQuick
import QtQuick.Layouts
import QtQuick.Controls as Controls

Controls.ApplicationWindow {
    id: root

    height: 720
    minimumHeight: 640
    minimumWidth: 360
    title: 'PySide'
    visible: true
    width: 1280

    menuBar: Controls.MenuBar {
        Controls.Menu {
            title: qsTr("&File")

            Controls.Action {
                icon.name: "application-exit-symbolic"
                shortcut: "Ctrl+q"
                text: qsTr("Quit")

                onTriggered: Qt.exit(0)
            }
        }

        Controls.Menu {
            title: "Linux"

            Controls.Action {
                text: qsTr("Create desktop entry")

                onTriggered: menubar.create_desktop_entry()
            }
        }
    }

    ColumnLayout {
        anchors.fill: parent

        Controls.Label {
            id: label

            Layout.fillHeight: true
            Layout.fillWidth: true
            horizontalAlignment: Qt.AlignHCenter
            text: qsTr("Type something in the text field!")
            verticalAlignment: Qt.AlignVCenter
        }

        Controls.TextField {
            id: textField

            Layout.fillWidth: true
            Layout.leftMargin: 12
            Layout.rightMargin: 12
            placeholderText: qsTr("Type something.")
        }

        Controls.Button {
            id: button

            Layout.bottomMargin: 12
            Layout.fillWidth: true
            Layout.leftMargin: 12
            Layout.rightMargin: 12
            text: qsTr("Click here")

            onClicked: {
                let text = textField.text;
                if (text.len === 0 || text.trim() === "") {
                    label.text = qsTr("The text field is empty.");
                } else {
                    let pythonText = mainWindow.to_upper(text);
                    text += pythonText;
                    label.text = `QML: ${text}`;
                }
            }
        }
    }
}
