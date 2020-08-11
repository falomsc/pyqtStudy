import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, Qt, QRect, QSize
from PyQt5.QtGui import QPainter, QPen, QBrush, QFontMetrics
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(239, 166)
        self.qWidget = QtWidgets.QWidget(MainWindow)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(self.qWidget)
        self.qmyBattery = QmyBattery(self.qWidget)
        self.qSlider = QtWidgets.QSlider(self.qWidget)
        self.qSlider.setOrientation(Qt.Horizontal)
        self.qLabel = QtWidgets.QLabel(self.qWidget)
        self.qLabel.setMaximumSize(QSize(16777215, 20))
        self.qLabel.setText("电池电量：")
        self.qVBoxLayout.addWidget(self.qmyBattery)
        self.qVBoxLayout.addWidget(self.qSlider)
        self.qVBoxLayout.addWidget(self.qLabel)
        MainWindow.setCentralWidget(self.qWidget)

        self.qLabel.setObjectName("qLabel")
        self.qSlider.setObjectName("qSlider")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class QmyBattery(QWidget):
    powerLevelChanged = pyqtSignal(int)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.colorBack = Qt.white
        self.colorBorder = Qt.black
        self.colorPower = Qt.green
        self.colorWarning = Qt.red
        self.__powerLevel = 65
        self.__warnLevel = 20

    def setPowerLevel(self, power):
        self.__powerLevel = power
        self.powerLevelChanged.emit(power)
        self.repaint()

    def powerLevel(self):
        return self.__powerLevel

    def setWarnLevel(self, warn):
        self.__warnLevel = warn
        self.repaint()

    def warnLevel(self):
        return self.__warnLevel

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        rect = QRect(0, 0, self.width(), self.height())
        painter.setViewport(rect)
        painter.setWindow(0, 0, 120, 50)

        pen = QPen()
        pen.setWidth(2)
        pen.setColor(self.colorBorder)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.FlatCap)
        pen.setJoinStyle(Qt.BevelJoin)
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(self.colorBack)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        rect.setRect(1, 1, 109, 48)
        painter.drawRect(rect)
        brush.setColor(self.colorBorder)
        painter.setBrush(brush)
        rect.setRect(110, 15, 10, 20)
        painter.drawRect(rect)

        if self.__powerLevel>self.__warnLevel:
            brush.setColor(self.colorPower)
            pen.setColor(self.colorPower)
        else:
            brush.setColor(self.colorWarning)
            pen.setColor(self.colorWarning)

        painter.setBrush(brush)
        painter.setPen(pen)
        if self.__powerLevel>0:
            rect.setRect(5, 5, self.__powerLevel, 40)
            painter.drawRect(rect)

        textSize = QFontMetrics(self.font())
        powStr = "%d%%" %self.__powerLevel
        textRect = QRect(textSize.boundingRect(powStr))
        painter.setFont(self.font())
        pen.setColor(self.colorBorder)
        painter.setPen(pen)
        painter.drawText(55 - textRect.width(), 23 + textRect.height()/2, powStr)

class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.qSlider.setRange(0, 100)
        self.ui.qLabel.setMaximumHeight(20)
        self.ui.qmyBattery.powerLevelChanged.connect(self.do_battery_changed)
        self.ui.qSlider.setValue(60)

    def on_qSlider_valueChanged(self, value):
        self.ui.qmyBattery.setPowerLevel(value)

    def do_battery_changed(self, power):
        powStr = "当前电量：%d %%" % power
        self.ui.qLabel.setText(powStr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
