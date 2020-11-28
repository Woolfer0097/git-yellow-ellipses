import sys

from random import randint
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from UI import Ui_MainWindow


class YellowEllipses(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.painter = QPainter(self)
        self.setupUi(self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git и жёлтые окружности')
        self.generate_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.generate(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def generate(self, qp):
        x, y = randint(0, 500), randint(0, 500)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(self.ellipse_label.x(), self.ellipse_label.y(), x, y)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowEllipses()
    ex.show()
    sys.exit(app.exec())
