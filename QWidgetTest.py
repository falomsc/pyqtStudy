import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QRect, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDateTimeEdit, QToolButton, QAbstractScrollArea


class Ui_MainWindow(object):
    def setupUi(self, qWidget):
        qWidget.resize(805, 512)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(qWidget)
        self.qTableWidget = QtWidgets.QTableWidget(qWidget)
        self.qVBoxLayout.addWidget(self.qTableWidget)

        self.qTableWidget.headerItem().setText(0, "cpu")
        self.qTableWidget.headerItem().setText(1, "displaycard")






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