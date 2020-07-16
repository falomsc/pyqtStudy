'''



'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt, QSize, pyqtSlot
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QListView


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(860, 506)
        self.qWidget1 = QtWidgets.QWidget(qMainWindow)
        self.qDockWidget = QtWidgets.QDockWidget(qMainWindow)
        self.qDockWidget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.qDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.qMenuBar = QtWidgets.QMenuBar(qMainWindow)
        self.qMenuBar.setGeometry(QRect(0, 0, 860, 23))
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        qMainWindow.setCentralWidget(self.qWidget1)
        qMainWindow.addToolBar(Qt.TopToolBarArea, self.qToolBar)
        qMainWindow.setStatusBar(self.qStatusBar)
        qMainWindow.addDockWidget(Qt.DockWidgetArea(1), self.qDockWidget)




class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )