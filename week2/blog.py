import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class BlogApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Blog Layout")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #333333;")  

        layout = QVBoxLayout()

        title = QLabel("Welcome to My Blog!")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setStyleSheet("color: white;")
        layout.addWidget(title)

        content_texts = [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Proin nec lectus in odio feugiat faucibus. "
            "Mauris nec leo nec nibh tempus aliquet vitae at nisi.",

            "Integer sit amet metus sem. Aliquam nec odio id orci ultrices ullamcorper. "
            "Ut viverra est sed ante malesuada, a tristique purus posuere.",

            "Praesent laoreet ex sed nunc consectetur, non fringilla nisi commodo. "
            "Duis ut placerat velit, eget tincidunt arcu. "
            "Morbi non enim non libero malesuada eleifend ut a dolor."
        ]

        for text in content_texts:
            label = QLabel(text)
            label.setFont(QFont("Arial", 11))
            label.setStyleSheet("color: white;")
            label.setWordWrap(True)
            layout.addWidget(label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BlogApp()
    window.show()
    sys.exit(app.exec_())
