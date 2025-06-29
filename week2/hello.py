import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def create_window():
    """Create and return the main window without blocking execution."""
    app = QApplication.instance() or QApplication(sys.argv)  # Cegah aplikasi ganda

    w = QWidget()
    b = QLabel(w)

    w.setGeometry(100, 100, 500, 300)
    w.setWindowTitle('Hello PyQt5')

    b.setText('Hello World!')
    b.setGeometry(200, 50, 100, 100)
    b.move(50, 50)
    b.setToolTip('Tes Tooltips')

    w.show()
    return w, b, app  # Kembalikan objek untuk pengujian

def main():
    """Main function to run the application normally."""
    w, _, app = create_window()
    sys.exit(app.exec_())  # Menjalankan aplikasi secara penuh

# Perbaikan di sini:
if __name__ == '_main':  # Seharusnya __name_ (bukan name)
    main()