import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QPainter, QPen, QBrush, QPixmap, QLinearGradient, QRadialGradient
from PyQt5.QtWidgets import QWidget, QApplication


class QmyWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setPalette(QPalette(Qt.white))
        self.setAutoFillBackground(True)
        self.resize(400, 280)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen()
        pen.setStyle(Qt.NoPen)
        painter.setPen(pen)
        W = self.width()
        H = self.height()
        radialGrad = QRadialGradient(W/2, H/2, W/3, W/2, H/2)
        radialGrad.setColorAt(0, Qt.white)
        radialGrad.setColorAt(1, Qt.blue)
        painter.setBrush(radialGrad)
        rect = QRect(W/4, H/4, W/2, H/2)
        painter.drawRect(rect)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())