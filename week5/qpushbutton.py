
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class ButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button demo")

        layout = QVBoxLayout()

        # Button 1: checkable & toggled
        self.b1 = QPushButton("Button1")
        self.b1.setCheckable(True)
        self.b1.setChecked(True)
        self.b1.pressed.connect(lambda: print("button pressed"))
        self.b1.released.connect(lambda: print("button released"))
        self.b1.clicked.connect(lambda: print(f"clicked button is {self.b1.text()}"))
        layout.addWidget(self.b1)

        # Button 2: no label
        self.b2 = QPushButton("")
        self.b2.clicked.connect(lambda: print("clicked button is "))
        layout.addWidget(self.b2)

        # Button 3: disabled
        self.b3 = QPushButton("Disabled")
        self.b3.setEnabled(False)
        layout.addWidget(self.b3)

        # Button 4: default button
        self.b4 = QPushButton("&Default")
        self.b4.setDefault(True)
        self.b4.clicked.connect(lambda: print(f"clicked button is {self.b4.text()}"))
        layout.addWidget(self.b4)

        self.setLayout(layout)

def create_window():
    return ButtonDemo()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = create_window()
    window.show()
    sys.exit(app.exec_())

