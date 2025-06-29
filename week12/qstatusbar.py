from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QPushButton, QAction
import sys

class statusdemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Status Bar Demo")
        self.setGeometry(100, 100, 400, 200)

        # Status bar
        self.statusBar = self.statusBar()

        # Tombol yang akan ditambahkan saat 'add'
        self.b = QPushButton("Click Me", self)

        # Menu
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")

        # Actions
        actions = ["show", "add", "remove"]
        for action_name in actions:
            action = QAction(action_name, self)
            action.triggered.connect(lambda checked, a=action: self.processtrigger(a))
            fileMenu.addAction(action)

    def processtrigger(self, action):
        action_text = action.text()
        if action_text == "show":
            self.statusBar.showMessage("show is clicked")
        elif action_text == "add":
            self.statusBar.addPermanentWidget(self.b)
        elif action_text == "remove":
            self.statusBar.removeWidget(self.b)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = statusdemo()
    demo.show()
    sys.exit(app.exec_())
