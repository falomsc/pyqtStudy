import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication


class QmyWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setPalette(QPalette(Qt.white))
        self.setAutoFillBackground(True)
        self.resize(400, 280)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        pen = QPen()
        pen.setWidth(3)
        pen.setColor(Qt.red)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.FlatCap)
        pen.setJoinStyle(Qt.BevelJoin)
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(Qt.yellow)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        W = self.width()
        H = self.height()
        rect = QRect(W/4, H/4, W/2, H/2)
        painter.drawRect(rect)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())