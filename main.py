import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class YellowEllipses(QMainWindow):
    def __init__(self):
        super().__init__()
        self.painter = QPainter(self)
        uic.loadUi('UI.ui', self)
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
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(self.ellipse_label.x(), self.ellipse_label.y(), x, y)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowEllipses()
    ex.show()
    sys.exit(app.exec())
