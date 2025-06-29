from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QFontDialog
from PyQt5.QtGui import QFont

class fontdialogdemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Label dengan teks awal
        self.le = QLabel("Hello")
        self.le.setFont(QFont("Times", 12))

        # Tombol untuk membuka font dialog
        self.btn = QPushButton("choose font")
        self.btn.clicked.connect(self.getfont)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.le)
        layout.addWidget(self.btn)
        self.setLayout(layout)

        self.setWindowTitle("Font Dialog Demo")
        self.resize(300, 100)

    def getfont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.le.setFont(font)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    demo = fontdialogdemo()
    demo.show()
    sys.exit(app.exec_())
