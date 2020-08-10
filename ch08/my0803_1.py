import math
import sys

from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPalette, QPainter, QPen, QBrush, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication


class QmyWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setPalette(QPalette(Qt.white))
        self.setAutoFillBackground(True)
        self.resize(600, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        W = self.width()
        H = self.height()
        side = min(W, H)
        rect = QRect((W-side)/2, (H-side)/2, side, side)
        painter.drawRect((rect))
        painter.setViewport(rect)
        painter.setWindow(-100, -100, 200, 200)

        pen = QPen()
        pen.setWidth(1)
        pen.setColor(Qt.blue)
        pen.setStyle(Qt.SolidLine)
        painter.setPen(pen)

        for i in range(36):
            painter.drawEllipse(QPoint(50, 0), 50, 50)
            painter.rotate(10)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())