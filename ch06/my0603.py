import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QItemSelectionModel, pyqtSlot, QStringListModel, pyqtSignal
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5.QtWidgets import QAbstractItemView, QLabel, QMainWindow, QDialog


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(567, 367)
        self.qWidget = QtWidgets.QWidget(qMainWindow)
        self.qMenuBar = QtWidgets.QMenuBar(qMainWindow)
        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        qMainWindow.setCentralWidget(self.qWidget)
        qMainWindow.setMenuBar(self.qMenuBar)
        qMainWindow.addToolBar(self.qToolBar)
        qMainWindow.setStatusBar(self.qStatusBar)

        self.qTabWidget = QtWidgets.QTabWidget(self.qWidget)
        self.qAction1 = QtWidgets.QAction(self.qToolBar)
        self.qAction2 = QtWidgets.QAction(self.qToolBar)
        self.qAction3 = QtWidgets.QAction(self.qToolBar)
        self.qAction4 = QtWidgets.QAction(self.qToolBar)
        self.qAction5 = QtWidgets.QAction(self.qToolBar)







class QmyMainWindow(QMainWindow):
    cellIndexChange = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )