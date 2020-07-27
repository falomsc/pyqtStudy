import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDateTimeEdit, QToolButton


class Ui_MainWindow(object):
    def setupUi(self, qWidget):
        qWidget.resize(805, 512)
        self.qToolButton = QtWidgets.QToolButton(qWidget)
        self.qToolButton.setGeometry(QRect(100, 100, 100, 100))
        self.qToolButton.setText("caidan")
        self.qAction = QtWidgets.QAction(qWidget)
        self.qAction.setText("haha")
        self.qAction.setIcon(QIcon("./image/15.ico"))

        self.qMenu = QtWidgets.QMenu(qWidget)
        self.qMenu.addAction(self.qAction)
        self.qToolButton.setMenu(self.qMenu)
        self.qToolButton.setPopupMode(QToolButton.MenuButtonPopup)




class QmyMainWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_())