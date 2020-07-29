'''
总结：
1，installEventFilter将其他对象作为时间检测者
2，eventFilter进行监测
'''
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, qApp


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(265, 154)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(qWidget)
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.qLabel1 = QtWidgets.QLabel(qWidget)
        self.qLabel1.setText("靠近我，点击我")
        self.qLabel1.setFont(font)
        self.qLabel1.setAutoFillBackground(False)
        self.qLabel1.setStyleSheet("")
        self.qLabel1.setAlignment(Qt.AlignCenter)
        self.qLabel2 = QtWidgets.QLabel(qWidget)
        self.qLabel2.setText("可双击的标签")
        self.qLabel2.setFont(font)
        self.qLabel2.setAutoFillBackground(False)
        self.qLabel2.setStyleSheet("")
        self.qLabel2.setAlignment(Qt.AlignCenter)
        self.qVBoxLayout.addWidget(self.qLabel1)
        self.qVBoxLayout.addWidget(self.qLabel2)
        QtCore.QMetaObject.connectSlotsByName(qWidget)

class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.qLabel1.installEventFilter(self)
        self.ui.qLabel2.installEventFilter(self)
        # qApp.processEvents()

    def eventFilter(self, watched, event):
        if(watched == self.ui.qLabel1):
            if(event.type() == QEvent.Enter):
                self.ui.qLabel1.setStyleSheet("background: rgb(170, 255, 255);")
            elif(event.type() == QEvent.Leave):
                self.ui.qLabel1.setStyleSheet("")
                self.ui.qLabel1.setText("靠近我，点击我")
            elif(event.type() == QEvent.MouseButtonPress):
                self.ui.qLabel1.setText("button pressed")
            elif(event.type() == QEvent.MouseButtonRelease):
                self.ui.qLabel1.setText("button released")

        if(watched == self.ui.qLabel2):
            if(event.type() == QEvent.Enter):
                self.ui.qLabel2.setStyleSheet("background: rgb(85, 255, 127);")
            elif(event.type() == QEvent.Leave):
                self.ui.qLabel2.setStyleSheet("")
                self.ui.qLabel2.setText("可双击的标签")
            elif(event.type() == QEvent.MouseButtonDblClick):
                self.ui.qLabel2.setText("double clicked")

        return super().eventFilter(watched, event)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())