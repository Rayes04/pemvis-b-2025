
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import Qt

class LineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt")

        layout = QVBoxLayout()

        # e1: Integer validator
        self.e1 = QLineEdit()
        self.e1.setValidator(QIntValidator())
        layout.addWidget(self.e1)

        # e2: Double validator
        self.e2 = QLineEdit()
        self.e2.setValidator(QDoubleValidator())
        layout.addWidget(self.e2)

        # e3: Input mask
        self.e3 = QLineEdit()
        self.e3.setInputMask("0000-00-00")  # YYYY-MM-DD
        layout.addWidget(self.e3)

        # e4: Text changed signal
        self.e4 = QLineEdit()
        self.e4.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.e4)

        # e5: Password field with returnPressed
        self.e5 = QLineEdit()
        self.e5.setEchoMode(QLineEdit.Password)
        self.e5.returnPressed.connect(self.on_password_edited)
        layout.addWidget(self.e5)

        # e51: PasswordEchoOnEdit
        self.e51 = QLineEdit()
        self.e51.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        layout.addWidget(self.e51)

        # e6: Read-only field
        self.e6 = QLineEdit()
        self.e6.setReadOnly(True)
        self.e6.setText("Hello Python")
        layout.addWidget(self.e6)

        self.setLayout(layout)

    def on_text_changed(self, text):
        print(f"contents of text box: {text}")

    def on_password_edited(self):
        print("edited")

def create_window():
    return LineEditDemo()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = create_window()
    window.show()
    sys.exit(app.exec_())

