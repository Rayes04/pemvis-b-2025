from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

def create_window():
    window = QWidget()
    window.setWindowTitle("PyQt")

    vbox = QVBoxLayout()
    hbox = QHBoxLayout()    

    b1 = QPushButton("Button1")
    b2 = QPushButton("Button2")

    hbox.addWidget(b1)
    hbox.addWidget(b2)

    vbox.addStretch(1)
    vbox.addLayout(hbox)

    window.setLayout(vbox)

    return window

if __name__ == "__main__":
    app = QApplication([])
    win = create_window()
    win.show()
    app.exec_()
