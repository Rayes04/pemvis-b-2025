from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys

_nim = "022008"

class Slider(QWidget):
    def __init__(self):
        super().__init__()

        self.l1 = QLabel(_nim)

        nim_digits = list(_nim)[3:]
        min_digit = int(min(nim_digits))
        max_digit = int(max(nim_digits))

        slider_min = min_digit * 10 + 1
        slider_max = max_digit * 10 + 1

        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(slider_min)
        self.sl.setMaximum(slider_max)
        self.sl.setValue(slider_min)

        font = QFont()
        font.setPointSize(self.sl.value())
        self.l1.setFont(font)

        self.sl.valueChanged.connect(self.update_font_size)

        layout = QVBoxLayout()
        layout.addWidget(self.l1)
        layout.addWidget(self.sl)
        self.setLayout(layout)

        self.setWindowTitle("QSlider Font Demo")
        self.resize(300, 100)

    def update_font_size(self, value):
        font = self.l1.font()
        font.setPointSize(value)
        self.l1.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Slider()
    window.show()
    sys.exit(app.exec_())
