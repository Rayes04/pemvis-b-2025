from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QInputDialog
import sys

class inputdialogdemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog Demo")
        self.setGeometry(100, 100, 300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # LineEdit untuk getItem
        self.le = QLineEdit()
        layout.addWidget(self.le)

        # LineEdit untuk getText
        self.le1 = QLineEdit()
        layout.addWidget(self.le1)

        # LineEdit untuk getInt
        self.le2 = QLineEdit()
        layout.addWidget(self.le2)

        # Tombol untuk membuka dialog getItem
        btn_item = QPushButton("get item")
        btn_item.clicked.connect(self.getItem)
        layout.addWidget(btn_item)

        # Tombol untuk membuka dialog getText
        btn_text = QPushButton("get text")
        btn_text.clicked.connect(self.gettext)
        layout.addWidget(btn_text)

        # Tombol untuk membuka dialog getInt
        btn_int = QPushButton("get int")
        btn_int.clicked.connect(self.getint)
        layout.addWidget(btn_int)

        self.setLayout(layout)

    def getItem(self):
        items = ["C++", "Python", "Java", "Go"]
        item, ok = QInputDialog.getItem(self, "Select Language", "Languages:", items, 0, False)
        if ok:
            self.le.setText(item)

    def gettext(self):
        text, ok = QInputDialog.getText(self, "Get Text", "Your name:")
        if ok:
            self.le1.setText(text)

    def getint(self):
        num, ok = QInputDialog.getInt(self, "Get Number", "Enter number:")
        if ok:
            self.le2.setText(str(num))

def main():
    app = QApplication(sys.argv)
    window = inputdialogdemo()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()