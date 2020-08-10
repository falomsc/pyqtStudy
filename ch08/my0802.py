import math
import sys

from PyQt5.QtCore import Qt, QPoint
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
        painter.setRenderHint(QPainter.TextAntialiasing)
        R = 100
        Pi = 3.14159
        deg = Pi*72/180
        points = [QPoint(R,0),
                  QPoint(R*math.cos(deg), -R*math.sin(deg)),
                  QPoint(R*math.cos(2*deg), -R*math.sin(2*deg)),
                  QPoint(R*math.cos(3*deg), -R*math.sin(3*deg)),
                  QPoint(R*math.cos(4*deg), -R*math.sin(4*deg))]
        font = painter.font()
        font.setPointSize(12)
        font.setBold(False)
        painter.setFont(font)

        pen = QPen()
        pen.setWidth(2)
        pen.setColor(Qt.blue)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.FlatCap)
        pen.setJoinStyle(Qt.BevelJoin)
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(Qt.yellow)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        starPath = QPainterPath()
        starPath.moveTo(points[0])
        starPath.lineTo(points[2])
        starPath.lineTo(points[4])
        starPath.lineTo(points[1])
        starPath.lineTo(points[3])
        starPath.closeSubpath()

        starPath.addText(points[0], font, "0")
        starPath.addText(points[1], font, "1")
        starPath.addText(points[2], font, "2")
        starPath.addText(points[3], font, "3")
        starPath.addText(points[4], font, "4")

        painter.save()
        painter.translate(100, 120)
        painter.drawPath(starPath)
        painter.drawText(0, 0, "S1")
        painter.restore()

        painter.translate(300, 120)
        painter.scale(0.8, 0.8)
        painter.rotate(90)
        painter.drawPath(starPath)
        painter.drawText(0, 0, "S2")

        painter.resetTransform()
        painter.translate(500, 120)
        painter.rotate(-145)
        painter.drawPath(starPath)
        painter.drawText(0, 0, "S3")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())