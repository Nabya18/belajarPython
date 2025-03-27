import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 800, 600)
        self.checkBox = QCheckBox("Do you like food?", self) # self is parents wadget
        self.initUI()

    def initUI(self):
        self.checkBox.setGeometry(10, 0, 400, 100)
        self.checkBox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You don't like food")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())