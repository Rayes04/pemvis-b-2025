import sys
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Signal and slot")  
        self.setGeometry(100, 100, 250, 150)  
        
        self.lcd = QLCDNumber(self)
        self.lcd.setGeometry(50, 20, 150, 50)  
        
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(50, 80, 150, 20) 
        self.slider.setRange(0, 100)
        
        self.slider.valueChanged.connect(self.lcd.display)
        
        self.show()  

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
