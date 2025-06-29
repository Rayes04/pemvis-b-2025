from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QVBoxLayout, QApplication
import sys

_nim = "F1D022008"

class SpinBox(QWidget):
    def __init__(self):
        super().__init__()
        self.l1 = QLabel("Nilai: 0")
        self.sp = QSpinBox()
        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        nim_digits = list(_nim)[3:]
        min_val = int(min(nim_digits))
        max_val = int(max(nim_digits))

        self.sp.setMinimum(min_val)
        self.sp.setMaximum(max_val)
        self.sp.setValue(0)

        layout = QVBoxLayout()
        layout.addWidget(self.l1)
        layout.addWidget(self.sp)
        self.setLayout(layout)
        self.setWindowTitle("SpinBox Demo")

    def _connect_signals(self):
        self.sp.valueChanged.connect(self._update_label)

    def _update_label(self, value):
        self.l1.setText(f"Nilai: {value}")

def main():
    app = QApplication(sys.argv)
    window = SpinBox()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()