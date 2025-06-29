
from PyQt5.QtWidgets import QWidget, QRadioButton, QVBoxLayout

class RadioButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RadioButton demo")

        self.b1 = QRadioButton("B1")
        self.b2 = QRadioButton("B2")

        self.b1.setChecked(True)
        self.b2.setChecked(False)

        self.b1.toggled.connect(self.handle_toggle)
        self.b2.toggled.connect(self.handle_toggle)

        layout = QVBoxLayout()
        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        self.setLayout(layout)

    def handle_toggle(self):
        if self.b1.isChecked():
            print("B1 is selected")
            print("B2 is deselected")
        elif self.b2.isChecked():
            print("B2 is selected")
            print("B1 is deselected")

def create_window():
    return RadioButtonDemo()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = create_window()
    window.show()
    sys.exit(app.exec_())

