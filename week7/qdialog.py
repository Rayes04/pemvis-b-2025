from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog
from PyQt5.QtCore import Qt
import sys

def showdialog():
    dialog = QDialog()
    dialog.setWindowTitle("Dialog")
    dialog.setWindowModality(Qt.ApplicationModal)

    b1 = QPushButton("ok", dialog)
    b1.move(50, 50)

    dialog.exec_()

def main():
    app = QApplication(sys.argv)

    # Buat jendela utama
    main_window = QWidget()
    main_window.setWindowTitle("Main Window")
    main_window.setGeometry(100, 100, 300, 200)

    # Tambahkan tombol
    button = QPushButton("Hello World!", main_window)
    button.move(50, 50)
    button.clicked.connect(showdialog)

    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()