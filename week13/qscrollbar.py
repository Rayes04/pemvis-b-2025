# qscrollbar.py

from PyQt5.QtWidgets import QWidget, QLabel, QScrollBar, QVBoxLayout, QApplication
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('ScrollBar Example')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Label
        self.l1 = QLabel("Test Text", self)
        layout.addWidget(self.l1)

        # ScrollBars for R, G, B, A
        self.s1 = QScrollBar(Qt.Horizontal, self)
        self.s2 = QScrollBar(Qt.Horizontal, self)
        self.s3 = QScrollBar(Qt.Horizontal, self)
        self.s4 = QScrollBar(Qt.Horizontal, self)

        for s in [self.s1, self.s2, self.s3, self.s4]:
            s.setMaximum(255)
            s.valueChanged.connect(self.sliderval)
            layout.addWidget(s)

        self.setLayout(layout)

    def sliderval(self):
        r = self.s1.value()
        g = self.s2.value()
        b = self.s3.value()
        a = self.s4.value()

        color = QColor(r, g, b, a)
        palette = self.l1.palette()
        palette.setColor(QPalette.Foreground, color)
        self.l1.setPalette(palette)

# Untuk menjalankan GUI-nya langsung
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Example()
    demo.show()
    sys.exit(app.exec_())
