from PyQt5.QtWidgets import QWidget, QComboBox, QVBoxLayout, QApplication
import sys

_nim = "F1D022008"  

class ComboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cb = QComboBox(self)
        
        # Tambahkan karakter dari _nim ke combo box
        for char in _nim:
            self.cb.addItem(char)

        # Hubungkan sinyal
        self.cb.highlighted.connect(self._on_highlight)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.cb)
        self.setLayout(layout)

        self.setWindowTitle("ComboBox Demo")
        self.setGeometry(100, 100, 300, 100)

    def _on_highlight(self, index):
        self.cb.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ComboBox()
    demo.show()
    sys.exit(app.exec_())
