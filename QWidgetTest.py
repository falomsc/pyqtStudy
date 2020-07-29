import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QRect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDateTimeEdit, QToolButton, QAbstractScrollArea


class Ui_MainWindow(object):
    def setupUi(self, qWidget):
        qWidget.resize(805, 512)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(qWidget)
        self.qScrollArea = QtWidgets.QScrollArea(qWidget)
        self.qScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.qLabel = QtWidgets.QLabel(self.qScrollArea)
        self.qLabel.setPixmap(QPixmap("./image/scenery.jpg"))
        self.qScrollArea.setWidget(self.qLabel)
        self.qVBoxLayout.addWidget(self.qScrollArea)





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