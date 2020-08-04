import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QItemSelectionModel, pyqtSlot, QStringListModel, pyqtSignal
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5.QtWidgets import QAbstractItemView, QLabel, QMainWindow, QDialog


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(827, 520)
        self.qWidget = QtWidgets.QWidget(qMainWindow)
        self.qMenuBar = QtWidgets.QMenuBar(qMainWindow)
        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        qMainWindow.setCentralWidget(self.qWidget)
        qMainWindow.setMenuBar(self.qMenuBar)
        qMainWindow.addToolBar(self.qToolBar)
        qMainWindow.setStatusBar(self.qStatusBar)

        self.qTabWidget = QtWidgets.QTabWidget(self.qWidget)
        self.qTabWidget.setGeometry(QRect(70, 30, 336, 196))
        self.qTabWidget.setTabsClosable(True)
        self.tab = QtWidgets.QWidget()
        self.qTabWidget.addTab(self.tab, "Page")
        self.qAction1 = QtWidgets.QAction(QIcon("../image/430.bmp"), "嵌入式Widget", self.qToolBar)
        self.qAction2 = QtWidgets.QAction(QIcon("../image/806.bmp"), "独立Widget窗口", self.qToolBar)
        self.qAction3 = QtWidgets.QAction(QIcon("../image/808.bmp"), "嵌入式MainWindow", self.qToolBar)
        self.qAction4 = QtWidgets.QAction(QIcon("../image/804.bmp"), "独立MainWindow窗口", self.qToolBar)
        self.qAction5 = QtWidgets.QAction(QIcon("../image/132.bmp"), "退出", self.qToolBar)
        self.qToolBar.addAction(self.qAction1)
        self.qToolBar.addAction(self.qAction2)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction3)
        self.qToolBar.addAction(self.qAction4)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction5)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.qAction1.setObjectName("qAction1")
        self.qAction2.setObjectName("qAction2")
        self.qAction3.setObjectName("qAction3")
        self.qAction4.setObjectName("qAction4")
        self.qAction5.setObjectName("qAction5")
        self.qAction5.triggered.connect(qMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)






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