from PyQt5.QtWidgets import QWidget, QSplitter, QTextEdit, QFrame, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QTextEdit dan QFrame
        text_edit1 = QTextEdit()
        text_edit2 = QTextEdit()
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)

        # Splitter horizontal
        splitter_horizontal = QSplitter(Qt.Horizontal)
        splitter_horizontal.addWidget(text_edit1)
        splitter_horizontal.addWidget(text_edit2)
        splitter_horizontal.addWidget(frame)
        splitter_horizontal.setSizes([100, 200, 100])  # memastikan text_edit2 > text_edit1

        # Splitter vertikal
        splitter_vertical = QSplitter(Qt.Vertical)
        splitter_vertical.addWidget(splitter_horizontal)

        # Layout utama
        vbox = QVBoxLayout(self)
        vbox.addWidget(splitter_vertical)
        self.setLayout(vbox)

        self.setWindowTitle("Splitter Example")
        self.setGeometry(100, 100, 600, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
