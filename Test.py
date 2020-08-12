import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, QRect
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 600)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawRect(QRect(100, 100, 100, 100))
        painter.setViewport(QRect(100, 100, 600, 400))
        painter.setWindow(-100, -100, 200, 200)
        painter.drawEllipse(QPoint(0, 0), 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
