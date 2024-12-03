import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
import random


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.ellipses = []
        self.ellipse_rect = None
        self.re_rect = None
        self.pushButton.clicked.connect(self.run)
        self.r = 0
        self.count = random.randrange(1, 10)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Улучшение качества рисования
        painter.setBrush(QColor(255, 255, 0))  # Цвет заливки эллипса
        for i in self.ellipses:
            painter.drawEllipse(i[0], i[1], i[2], i[2])

    def run(self):
        self.ellipses.clear()
        self.count = random.randrange(1, 10)
        self.re_rect = (0, 0, 0, 0)
        for i in range(self.count):
            print(8)
            self.r = random.randint(0, 100)
            self.ellipses.append((random.randrange(0, 450), random.randrange(0, 350), self.r))
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())