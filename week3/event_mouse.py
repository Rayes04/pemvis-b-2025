import sys
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Event object") 
        self.setGeometry(100, 100, 450, 300)  
    
        self.setMouseTracking(True)  
    
        self.label = QLabel("Move the mouse", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(150, 250, 150, 30)  
        
        self.show()
    
    def mouseMoveEvent(self, event: QMouseEvent):
        self.label.setText(f"Mouse at ({event.x()}, {event.y()})")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
