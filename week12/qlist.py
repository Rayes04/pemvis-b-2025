from PyQt5.QtWidgets import QApplication, QListWidget, QMessageBox
import sys

class myListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List Demo")
        self.resize(300, 200)

        self.itemClicked.connect(self.Clicked)

    def Clicked(self, item):
        QMessageBox.warning(self, "Item Clicked", f"You clicked: {item.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = myListWidget()
    demo.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])
    demo.show()
    sys.exit(app.exec_())
