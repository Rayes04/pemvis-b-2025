from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QTextEdit, QMdiArea, QMdiSubWindow, QMenu
)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MDI Example")
        self.setGeometry(100, 100, 800, 600)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        new_action = QAction("New", self)
        new_action.triggered.connect(lambda: self.windowaction(new_action))
        file_menu.addAction(new_action)

        cascade_action = QAction("cascade", self)
        cascade_action.triggered.connect(self.mdi.cascadeSubWindows)
        file_menu.addAction(cascade_action)

        tile_action = QAction("Tiled", self)
        tile_action.triggered.connect(self.mdi.tileSubWindows)
        file_menu.addAction(tile_action)

    def windowaction(self, action):
        if action.text() == "New":
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("SubWindow")
            self.mdi.addSubWindow(sub)
            sub.show()

# jalankan GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
