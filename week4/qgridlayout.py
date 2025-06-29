from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QHBoxLayout

def create_window():
    window = QWidget()
    window.setWindowTitle("PyQt")

    # Create a Grid Layout
    grid_layout = QGridLayout()

    # Button B11 at (1,1)
    b11 = QPushButton("B11")
    grid_layout.addWidget(b11, 1, 1)

    # B12 inside HBoxLayout at (1,2)
    hbox_b12 = QHBoxLayout()
    hbox_b12.addStretch()  # Stretch before the button
    b12 = QPushButton("B12")
    hbox_b12.addWidget(b12)  # B12 is second item
    grid_layout.addLayout(hbox_b12, 1, 2)

    # Buttons B22 and B23 at (2,2) and (2,3)
    b22 = QPushButton("B22")
    b23 = QPushButton("B23")
    grid_layout.addWidget(b22, 2, 2)
    grid_layout.addWidget(b23, 2, 3)

    # B31 inside HBoxLayout at (3,1)
    hbox_b31 = QHBoxLayout()
    b31 = QPushButton("B31")
    hbox_b31.addWidget(b31)  # B31 is first item
    grid_layout.addLayout(hbox_b31, 3, 1)

    # Set layout on the window
    window.setLayout(grid_layout)

    return window

if __name__ == "__main__":
    app = QApplication([])
    win = create_window()
    win.show()
    app.exec_()
