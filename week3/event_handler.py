import sys
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Event handler")  
        self.setGeometry(100, 100, 250, 150)  

        self.label = QLabel("Press 'E' to close the window", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(25, 60, 200, 30) 
        
        self.show()  
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_E:
            self.close()  # Menutup window jika tombol 'E' ditekan

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
