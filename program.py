import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QPushButton
import random


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 450, 350)
        self.pushButton = QPushButton('', self)
        self.pushButton.move(190, 140)
        self.pushButton.clicked.connect(self.run)
        self.ellipses = []
        self.ellipse_rect = None
        self.re_rect = None
        self.r = 0
        self.count = random.randrange(1, 10)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for i in self.ellipses:
            painter.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
            painter.drawEllipse(i[0], i[1], i[2], i[2])

    def run(self):
        self.ellipses.clear()
        self.count = random.randrange(1, 10)
        self.re_rect = (0, 0, 0, 0)
        for i in range(self.count):
            self.r = random.randint(0, 100)
            self.ellipses.append((random.randrange(0, 450), random.randrange(0, 350), self.r))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())