from PyQt5.QtWidgets import QComboBox, QApplication, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDropEvent, QDragEnterEvent


class combo(QComboBox):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setEditable(True)
        self.setToolTip(title)


    def dragEnterEvent(self, e: QDragEnterEvent):
        if e.mimeData().hasText():
            e.acceptProposedAction()
        else:
            e.ignore()

    def dropEvent(self, e: QDropEvent):
        if e.mimeData().hasText():
            text = e.mimeData().text()
            self.addItem(text)
            e.acceptProposedAction()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Drag and Drop ComboBox Demo")
    layout = QVBoxLayout()

    label = QLabel("Drag text here:")
    drop_box = combo("Drop target")

    layout.addWidget(label)
    layout.addWidget(drop_box)

    window.setLayout(layout)
    window.resize(300, 150)
    window.show()

    sys.exit(app.exec_())
