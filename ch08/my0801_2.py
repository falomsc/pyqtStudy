import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QPainter, QPen, QBrush, QPixmap
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
        pen.setWidth(2)
        pen.setColor(Qt.red)
        painter.setPen(pen)

        texturePixmap = QPixmap("../image/texture2.jpg")
        brush = QBrush()
        brush.setStyle(Qt.TexturePattern)
        brush.setTexture(texturePixmap)
        painter.setBrush(brush)

        W = self.width()
        H = self.height()
        rect = QRect(W/5, H/5, 3*W/5, 3*H/5)
        painter.drawRect(rect)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())