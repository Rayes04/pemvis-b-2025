from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QTextEdit
from PyQt5.QtGui import QPixmap
import os

class filedialogdemo(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Label untuk menampilkan gambar
        self.le = QLabel("Gambar akan muncul di sini")
        self.le.setScaledContents(True)
        self.le.setFixedSize(300, 200)

        # Tombol untuk membuka file gambar
        btn1 = QPushButton("Open Image")
        btn1.clicked.connect(self.getfile)

        # TextEdit untuk menampilkan isi file teks
        self.contents = QTextEdit()
        self.contents.setReadOnly(True)

        # Tombol untuk membuka file teks
        btn2 = QPushButton("Open Text File")
        btn2.clicked.connect(self.getfiles)

        layout = QVBoxLayout()
        layout.addWidget(self.le)
        layout.addWidget(btn1)
        layout.addWidget(self.contents)
        layout.addWidget(btn2)
        self.setLayout(layout)

        self.setWindowTitle("File Dialog Demo")
        self.resize(400, 400)

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), "Image files (*.jpg *.png)")
        if fname:
            self.le.setPixmap(QPixmap(fname))

    def getfiles(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        if dialog.exec_():
            selected = dialog.selectedFiles()
            if selected:
                with open(selected[0], 'r') as f:
                    text = f.read()
                    self.contents.setPlainText(text)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    demo = filedialogdemo()
    demo.show()
    sys.exit(app.exec_())
