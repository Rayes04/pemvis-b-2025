from PyQt5.QtWidgets import QMainWindow, QTextEdit, QListWidget, QDockWidget, QAction, QApplication, QMenuBar
import sys

class dockdemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dock Demo")
        self.setGeometry(100, 100, 600, 400)

        # Central Widget
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # Dock Widget
        self.items = QDockWidget("Dockable", self)
        self.listWidget = QListWidget()
        self.listWidget.addItems(["item1", "item2", "item3"])
        self.items.setWidget(self.listWidget)
        self.addDockWidget(0x1, self.items)  # Left dock area

        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        new_action = QAction("New", self)
        save_action = QAction("save", self)
        quit_action = QAction("quit", self)

        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        file_menu.addAction(quit_action)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = dockdemo()
    window.show()
    sys.exit(app.exec_())
