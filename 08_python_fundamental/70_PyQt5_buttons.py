import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow90(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 800, 600) # X, Y, Width, Height
        self.button = QPushButton("Click Me", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self): # prefix self is the parent
        self.button.setGeometry(200, 200, 200, 50) # X, Y, Width, Height
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(200, 300, 200, 50) # X, Y, Width, Height
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        self.label.setText("Goodbye")

if __name__ == "__main__":
    app = QApplication(sys.argv) # argv = argument variable
    window = MainWindow90()
    window.show()
    sys.exit(app.exec_()) # FOR USER INPUT