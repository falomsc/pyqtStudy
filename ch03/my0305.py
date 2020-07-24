'''
目前问题：

总结：
1，注意功能，LCD显示屏每隔固定周期显示当前时间

'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime, QTimer
from PyQt5.QtWidgets import QLCDNumber


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(296, 223)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(qWidget)
        self.qGrounpBox1 = QtWidgets.QGroupBox(qWidget)
        self.qGrounpBox1.setTitle("定时器")
        self.qGrounpBox2 = QtWidgets.QGroupBox(qWidget)
        self.qGrounpBox2.setTitle("当前时间（小时：分：秒）")
        self.qLabel = QtWidgets.QLabel(qWidget)
        self.qLabel.setText("流逝的时间")
        self.qLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.qGridLayout = QtWidgets.QGridLayout(self.qGrounpBox1)
        self.qHBoxLayout = QtWidgets.QHBoxLayout(self.qGrounpBox2)
        self.qPushButton1 = QtWidgets.QPushButton(self.qGrounpBox1)
        self.qPushButton1.setText("开始")
        self.qPushButton2 = QtWidgets.QPushButton(self.qGrounpBox1)
        self.qPushButton2.setText("停止")
        self.qPushButton2.setEnabled(False)
        self.qPushButton3 = QtWidgets.QPushButton(self.qGrounpBox1)
        self.qPushButton3.setText("设置周期")
        self.qSpinBox = QtWidgets.QSpinBox(self.qGrounpBox1)
        self.qSpinBox.setSuffix(" ms")
        self.qSpinBox.setMaximum(999999)
        self.qLCDNumber1 = QtWidgets.QLCDNumber(self.qGrounpBox2)
        self.qLCDNumber1.setDigitCount(2)
        self.qLCDNumber1.setSegmentStyle(QLCDNumber.Filled)
        self.qLCDNumber2 = QtWidgets.QLCDNumber(self.qGrounpBox2)
        self.qLCDNumber2.setDigitCount(2)
        self.qLCDNumber2.setSegmentStyle(QLCDNumber.Filled)
        self.qLCDNumber3 = QtWidgets.QLCDNumber(self.qGrounpBox2)
        self.qLCDNumber3.setDigitCount(2)
        self.qLCDNumber3.setSegmentStyle(QLCDNumber.Filled)

        self.qVBoxLayout.addWidget(self.qGrounpBox1)
        self.qVBoxLayout.addWidget(self.qGrounpBox2)
        self.qVBoxLayout.addWidget(self.qLabel)
        self.qGridLayout.addWidget(self.qPushButton1, 0, 0, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton2, 0, 1, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton3, 1, 0, 1, 1)
        self.qGridLayout.addWidget(self.qSpinBox, 1, 1, 1, 1)
        self.qHBoxLayout.addWidget(self.qLCDNumber1)
        self.qHBoxLayout.addWidget(self.qLCDNumber2)
        self.qHBoxLayout.addWidget(self.qLCDNumber3)

        self.qPushButton1.setObjectName("qPushButton1")
        self.qPushButton2.setObjectName("qPushButton2")
        self.qPushButton3.setObjectName("qPushButton3")
        self.qSpinBox.setObjectName("qSpinBox")
        QtCore.QMetaObject.connectSlotsByName(qWidget)

        ############################  Init  ##################################
        self.qSpinBox.setValue(1000)
        self.qLCDNumber1.setProperty("value", 10)
        self.qLCDNumber2.setProperty("value", 26)
        self.qLCDNumber3.setProperty("value", 35)


class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.stop()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.do_timer_timeout)
        self.count = QTime()

    def on_qPushButton1_clicked(self):
        self.timer.start()
        self.count.start()
        self.ui.qPushButton1.setEnabled(False)
        self.ui.qPushButton2.setEnabled(True)
        self.ui.qPushButton3.setEnabled(False)

    def on_qPushButton2_clicked(self):
        self.timer.stop()
        tm = self.count.elapsed()
        ms = tm % 1000
        s = tm // 1000
        self.ui.qLabel.setText("流逝的时间：%d秒 %d毫秒" % (s, ms))
        self.ui.qPushButton1.setEnabled(True)
        self.ui.qPushButton2.setEnabled(False)
        self.ui.qPushButton3.setEnabled(True)

    def on_qPushButton3_clicked(self):
        self.timer.setInterval(self.ui.qSpinBox.value())

    def do_timer_timeout(self):
        curTime = QTime.currentTime()
        self.ui.qLCDNumber1.display(curTime.hour())
        self.ui.qLCDNumber2.display(curTime.minute())
        self.ui.qLCDNumber3.display(curTime.second())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())