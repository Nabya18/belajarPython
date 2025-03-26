import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap # to display images

class MainWindow90(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 800, 600) # X, Y, Width, Height

        label = QLabel(self) # self in behind is the parent
        label.setGeometry(0, 0, 100, 100)  # X, Y, Width, Height

        pixmap = QPixmap("Byad.jpeg")
        label.setPixmap(pixmap)

        # set the image to be scaled to the label size
        label.setScaledContents(True)

        label.setGeometry((self.width() - self.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height()) # same as label.setGeometry(0, 0, 800, 600)

def main():
    app = QApplication(sys.argv) # argv = argument variable
    window = MainWindow90()
    window.show()
    sys.exit(app.exec_()) # FOR USER INPUT

if __name__ == "__main__":
    main()