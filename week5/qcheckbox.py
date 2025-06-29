
from PyQt5.QtWidgets import QWidget, QCheckBox, QVBoxLayout
from PyQt5.QtCore import Qt

class CheckboxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("checkbox demo")
        
        self.b1 = QCheckBox("Button1")
        self.b2 = QCheckBox("Button2")
        
        self.b1.setChecked(True)
        self.b2.setChecked(False)
        
        self.b1.stateChanged.connect(self.on_state_change)
        self.b2.stateChanged.connect(self.on_state_change)
        
        layout = QVBoxLayout()
        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        self.setLayout(layout)

    def on_state_change(self, state):
        checkbox = self.sender()
        if checkbox.isChecked():
            print(f"{checkbox.text()} is selected")
        else:
            print(f"{checkbox.text()} is deselected")

def create_window():
    return CheckboxDemo()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = create_window()
    window.show()
    sys.exit(app.exec_())

