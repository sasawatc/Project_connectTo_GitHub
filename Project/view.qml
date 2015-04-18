import QtQuick 1.0

NavigationDrawer {
    id: drawer
    anchors.top: navigationBar.bottom
    anchors.bottom: parent.bottom

    position: Qt.LeftEdge
    visualParent: stackView


}