import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow90(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 800, 600) # X, Y, Width, Height

        label = QLabel("Hello, World!", self) # self in behind is the parent
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 800, 100) # X, Y, Width, Height
        label.setStyleSheet("color: #292929;" 
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # AlignCenter, AlignRight, AlignLeft, AlignTop, etc.
        # Vertical Alignment
        # label.setAlignment(Qt.AlignCenter)
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)

        # Horizontal Alignment
        # label.setAlignment(Qt.AlignLeft)
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)

        # Both Vertical and Horizontal Alignment
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

def main():
    app = QApplication(sys.argv) # argv = argument variable
    window = MainWindow90()
    window.show()
    sys.exit(app.exec_()) # FOR USER INPUT

if __name__ == "__main__":
    main()