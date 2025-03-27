import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

class MainWindow90(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 800, 600) # X, Y, Width, Height
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: green;")
        label3.setStyleSheet("background-color: blue;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: orange;")

        # MAKING UNOVERLAPPING LAYOUT = vbox for vertical, hbox for horizontal, grid for grid
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)




def main():
    app = QApplication(sys.argv) # argv = argument variable
    window = MainWindow90()
    window.show()
    sys.exit(app.exec_()) # FOR USER INPUT

if __name__ == "__main__":
    main()