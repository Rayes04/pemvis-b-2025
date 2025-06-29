from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction
import sys

class tooldemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toolbar Demo")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()

    def init_ui(self):
        # File Toolbar
        file_toolbar = QToolBar("File", self)
        file_toolbar.setObjectName("File")
        self.addToolBar(file_toolbar)

        new_action = QAction("membuat file baru", self)
        new_action.triggered.connect(lambda: print("pressed tool button is membuat file baru"))
        file_toolbar.addAction(new_action)

        open_action = QAction("open", self)
        open_action.triggered.connect(lambda: print("pressed tool button is open"))
        file_toolbar.addAction(open_action)

        save_action = QAction("save", self)
        save_action.triggered.connect(lambda: print("pressed tool button is save"))
        file_toolbar.addAction(save_action)

        # Edit Toolbar
        edit_toolbar = QToolBar("Edit", self)
        edit_toolbar.setObjectName("Edit")
        self.addToolBar(edit_toolbar)

        cut_action = QAction("cut", self)
        cut_action.triggered.connect(lambda: print("pressed tool button is cut"))
        edit_toolbar.addAction(cut_action)

        copy_action = QAction("copy", self)
        copy_action.triggered.connect(lambda: print("pressed tool button is copy"))
        edit_toolbar.addAction(copy_action)

        paste_action = QAction("paste", self)
        paste_action.triggered.connect(lambda: print("pressed tool button is paste"))
        edit_toolbar.addAction(paste_action)

def main():
    app = QApplication(sys.argv)
    window = tooldemo()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()