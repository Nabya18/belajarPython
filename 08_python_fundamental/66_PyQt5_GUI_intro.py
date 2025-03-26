import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow90(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(700, 300, 800, 600) # X, Y, Width, Height
        self.setWindowIcon(QIcon("Byad.jpeg"))

def main():
    app = QApplication(sys.argv) # argv = argument variable
    window = MainWindow90()
    window.show()
    sys.exit(app.exec_()) # FOR USER INPUT

if __name__ == "__main__":
    main()