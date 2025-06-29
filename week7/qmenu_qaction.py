from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu
import sys

class menudemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Menu bar
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_triggered)
        file_menu.addAction(save_action)

        edit_menu = QMenu("Edit", self)
        file_menu.addMenu(edit_menu)

        paste_menu = QMenu("paste", self)
        edit_menu.addMenu(paste_menu)

        paste_value_action = QAction("by value", self)
        paste_value_action.triggered.connect(self.paste_value_triggered)
        paste_menu.addAction(paste_value_action)

        menubar.addMenu("Help")
        menubar.addMenu("Run")

        self.setWindowTitle("Menu Demo")
        self.setGeometry(300, 300, 300, 200)

    def save_triggered(self):
        print("save triggered")

    def paste_value_triggered(self):
        print("edit paste value triggered")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = menudemo()
    demo.show()
    sys.exit(app.exec_())
