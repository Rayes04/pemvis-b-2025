from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calendar Example')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        layout.addWidget(self.calendar)

        self.label = QLabel(self)
        self.label.setText(self.calendar.selectedDate().toString())
        layout.addWidget(self.label)

        self.calendar.clicked.connect(self.update_label)

        self.setLayout(layout)

    def update_label(self, date: QDate):
        self.label.setText(date.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Example()
    demo.show()
    sys.exit(app.exec_())
