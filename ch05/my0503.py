'''
总结：
1，return super().event(event)即调用默认的event处理函数

'''
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QRect, QEvent
from PyQt5.QtGui import QFont, QCursor, QPainter, QPixmap
from PyQt5.QtWidgets import QMessageBox


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(392, 266)
        font = QFont()
        font.setPointSize(10)
        qWidget.setFont(font)
        qWidget.setCursor(QCursor(Qt.CrossCursor))
        self.qLabel = QtWidgets.QLabel(qWidget)
        self.qLabel.setText("点击鼠标左键")
        self.qLabel.setGeometry(QRect(55, 35, 196, 41))
        self.qPushButton1 = QtWidgets.QPushButton(qWidget)
        self.qPushButton1.setText("Button at Center\nresizeEvent事件")
        self.qPushButton1.setGeometry(QRect(200, 70, 146, 51))
        self.qPushButton2 = QtWidgets.QPushButton(qWidget)
        self.qPushButton2.setText("Movable Button\nW,S,A,D键移动")
        self.qPushButton2.setGeometry(QRect(30, 170, 141, 51))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.qLabel.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.qLabel.setFont(font)

        self.qLabel.setObjectName("qLabel")
        self.qPushButton1.setObjectName("qPushButton1")
        self.qPushButton2.setObjectName("qPushButton2")
        QtCore.QMetaObject.connectSlotsByName(qWidget)



class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def event(self, event):
        if(event.type() == QEvent.Paint):
            return True
        elif (event.type() == QEvent.KeyRelease) and (event.key() == Qt.Key_Tab):
            rect = self.ui.qPushButton2.geometry()
            self.ui.qPushButton2.setGeometry(rect.left()+100, rect.top(), rect.width(), rect.height())
        return super().event(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        pic = QPixmap("../image/sea1.jpg")
        painter.drawPixmap(0, 0, self.width(), self.height(), pic)

    def resizeEvent(self, event):   # 自动定位qPushButton1
        w = self.width()
        h = self.height()
        wbtn = self.ui.qPushButton1.width()
        hbtn = self.ui.qPushButton1.height()
        self.ui.qPushButton1.setGeometry((w-wbtn)/2, (h-hbtn)/2, wbtn, hbtn)

    def closeEvent(self, event):    # 关闭窗口事件
        dlgTitle = "Question消息框"
        strInfo = "closeEvent事件触发，确定要退出吗？"
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes | QMessageBox.No, defaultBtn)
        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        rect = self.ui.qPushButton2.geometry()
        if event.key() in set([Qt.Key_A, Qt.Key_Left]):
            self.ui.qPushButton2.setGeometry(rect.left()-20, rect.top(), rect.width(), rect.height())
        elif event.key() in set([Qt.Key_D, Qt.Key_Right]):
            self.ui.qPushButton2.setGeometry(rect.left()+20, rect.top(), rect.width(), rect.height())
        elif event.key() in set([Qt.Key_W, Qt.Key_Up]):
            self.ui.qPushButton2.setGeometry(rect.left(), rect.top()-20, rect.width(), rect.height())
        elif event.key() in set([Qt.Key_S, Qt.Key_Down]):
            self.ui.qPushButton2.setGeometry(rect.left(), rect.top()+20, rect.width(), rect.height())

    def hideEvent(self, event):
        print("hideEvent 事件触发")

    def showEvent(self, event):
        print("showEvent 事件触发")

    def mousePressEvent(self, event):
        pt = event.pos()
        if(event.button() == Qt.LeftButton):
            self.ui.qLabel.setText("(x, y)=(%d, %d)" % (pt.x(), pt.y()))
            rect = self.ui.qLabel.geometry()
            self.ui.qLabel.setGeometry(pt.x(), pt.y(), rect.width(), rect.height())
        super().mousePressEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())