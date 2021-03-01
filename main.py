import random
import sys
from PyQt5 import uic
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton


class Nim(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.buttons = [
            [QLabel(self),
             random.randint(10, 300),
             (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]
            for _ in range(3)]
        for i in range(len(self.buttons)):
            itemRad = self.buttons[i][1]
            self.buttons[i][0].move(30 + 620 * i, 300)
            self.buttons[i][0].resize(itemRad * 2, itemRad * 2)


    def run(self):
        for i in range(len(self.buttons)):
            self.buttons[i][0].setStyleSheet(f'background: rgb({self.buttons[i][-1][0]}, {self.buttons[i][-1][1]}, {self.buttons[i][-1][2]}); border-radius:{self.buttons[i][1]}px')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Nim()
    ex.show()
    sys.exit(app.exec())