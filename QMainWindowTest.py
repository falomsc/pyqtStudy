import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabWidget, QFrame


class Ui_MainWindow(object):
    def setupUi(self, qMainWindow):
        qMainWindow.resize(805, 512)
        self.qCenterWidget = QtWidgets.QWidget(qMainWindow)
        self.qFrame = QtWidgets.QFrame(qMainWindow)
        self.qFrame.setFrameShape(QFrame.Panel)
        self.qFrame.setFrameShadow(QFrame.Raised)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(self.qCenterWidget)
        self.qVBoxLayout.addWidget(self.qFrame)
        qMainWindow.setCentralWidget(self.qCenterWidget)


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_())