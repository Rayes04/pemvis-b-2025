from PyQt5.QtWidgets import (
    QApplication, QWidget, QFormLayout, QLineEdit, QLabel, 
    QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout
)

def create_window():
    window = QWidget()
    window.setWindowTitle("PyQt")

    form_layout = QFormLayout()

    name_label = QLabel("Name")
    name_field = QLineEdit()
    form_layout.addRow(name_label, name_field)

    address_label = QLabel("Address")
    address_layout = QVBoxLayout()
    address_layout.addWidget(QLineEdit()) 
    address_layout.addWidget(QLineEdit())  
    form_layout.addRow(address_label, address_layout)

    gender_label = QLabel("Gender")
    gender_layout = QHBoxLayout()
    male_radio = QRadioButton("Male")
    female_radio = QRadioButton("Female")
    gender_layout.addWidget(male_radio)
    gender_layout.addWidget(female_radio)
    form_layout.addRow(gender_label, gender_layout)

    submit_button = QPushButton("Submit")
    cancel_button = QPushButton("Cancel")
    form_layout.addRow(submit_button, cancel_button)

    window.setLayout(form_layout)

    return window

if __name__ == "__main__":
    app = QApplication([])
    win = create_window()
    win.show()
    app.exec_()
