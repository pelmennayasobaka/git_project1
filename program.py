import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint
import random


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.ellipses = []  # Список для хранения координат эллипсов
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Улучшение качества рисования
        painter.setBrush(QColor(255, 255, 0))  # Цвет заливки эллипса

        # Рисование всех эллипсов из списка
        for point in self.ellipses:
            r = random.randrange(0, 50)
            painter.drawEllipse(point[0] - 20, point[1] - 10, r, r)

    def run(self):
        for i in range(random.randrange(0, 10)):
            self.ellipses.append((random.randrange(0, 200), random.randrange(0, 150)))
            self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())