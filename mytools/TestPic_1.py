import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt, QSize, pyqtSlot
from PyQt5.QtGui import QIcon, QCursor, QFont
from PyQt5.QtWidgets import QListView


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(800, 600)
        self.CqWidget = QtWidgets.QWidget(qMainWindow)
        self.qSplitter = QtWidgets.QSplitter(self.CqWidget)
        self.qSplitter.setOrientation(Qt.Horizontal)
        self.qSplitter.setGeometry(QRect(0, 0, 800, 600))
        self.qToolBox = QtWidgets.QToolBox(self.qSplitter)
        self.qToolBox.setMaximumSize(QSize(220, 16777215))
        self.qTabWidget = QtWidgets.QTabWidget(self.qSplitter)
        qMainWindow.setCentralWidget(self.CqWidget)

        font1 = QFont()
        font1.setPointSize(15)
        self.qToolBox.setFont(font1)
        self.qWidget1 = QtWidgets.QWidget(self.qToolBox)
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(self.qWidget1)
        font2 = QFont()
        font2.setPointSize(10)
        self.qTooButton1_1 = QtWidgets.QToolButton(self.qWidget1)
        self.qTooButton1_1.setText("Overview")
        self.qTooButton1_1.setFont(font2)
        self.qTooButton1_1.setMinimumSize(QSize(200, 25))
        self.qTooButton1_2 = QtWidgets.QToolButton(self.qWidget1)
        self.qTooButton1_2.setText("20M")
        self.qTooButton1_2.setFont(font2)
        self.qTooButton1_2.setMinimumSize(QSize(200, 25))
        self.qTooButton1_3 = QtWidgets.QToolButton(self.qWidget1)
        self.qTooButton1_3.setText("20M+20M")
        self.qTooButton1_3.setFont(font2)
        self.qTooButton1_3.setMinimumSize(QSize(200, 25))
        self.qTooButton1_4 = QtWidgets.QToolButton(self.qWidget1)
        self.qTooButton1_4.setText("5M+10M+gap25M+20M+10M")
        self.qTooButton1_4.setFont(font2)
        self.qTooButton1_4.setMinimumSize(QSize(200, 25))
        self.qVBoxLayout1.addWidget(self.qTooButton1_1)
        self.qVBoxLayout1.addWidget(self.qTooButton1_2)
        self.qVBoxLayout1.addWidget(self.qTooButton1_3)
        self.qVBoxLayout1.addWidget(self.qTooButton1_4)

        self.qWidget2 = QtWidgets.QWidget(self.qToolBox)
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qWidget2)
        self.qTooButton2_1 = QtWidgets.QToolButton(self.qWidget2)
        self.qTooButton2_1.setText("Overview")
        self.qTooButton2_1.setFont(font2)
        self.qTooButton2_1.setMinimumSize(QSize(200, 25))
        self.qTooButton2_2 = QtWidgets.QToolButton(self.qWidget2)
        self.qTooButton2_2.setText("20M")
        self.qTooButton2_2.setFont(font2)
        self.qTooButton2_2.setMinimumSize(QSize(200, 25))
        self.qTooButton2_3 = QtWidgets.QToolButton(self.qWidget2)
        self.qTooButton2_3.setText("20M+20M")
        self.qTooButton2_3.setFont(font2)
        self.qTooButton2_3.setMinimumSize(QSize(200, 25))
        self.qTooButton2_4 = QtWidgets.QToolButton(self.qWidget2)
        self.qTooButton2_4.setText("5M+10M+gap25M+20M+10M")
        self.qTooButton2_4.setFont(font2)
        self.qTooButton2_4.setMinimumSize(QSize(200, 25))
        self.qVBoxLayout2.addWidget(self.qTooButton2_1)
        self.qVBoxLayout2.addWidget(self.qTooButton2_2)
        self.qVBoxLayout2.addWidget(self.qTooButton2_3)
        self.qVBoxLayout2.addWidget(self.qTooButton2_4)

        self.qWidget3 = QtWidgets.QWidget(self.qToolBox)
        self.qVBoxLayout3 = QtWidgets.QVBoxLayout(self.qWidget3)
        self.qTooButton3_1 = QtWidgets.QToolButton(self.qWidget3)
        self.qTooButton3_1.setText("Overview")
        self.qTooButton3_1.setFont(font2)
        self.qTooButton3_1.setMinimumSize(QSize(200, 25))
        self.qTooButton3_2 = QtWidgets.QToolButton(self.qWidget3)
        self.qTooButton3_2.setText("100M")
        self.qTooButton3_2.setFont(font2)
        self.qTooButton3_2.setMinimumSize(QSize(200, 25))
        self.qTooButton3_3 = QtWidgets.QToolButton(self.qWidget3)
        self.qTooButton3_3.setText("200M")
        self.qTooButton3_3.setFont(font2)
        self.qTooButton3_3.setMinimumSize(QSize(200, 25))
        self.qTooButton3_4 = QtWidgets.QToolButton(self.qWidget3)
        self.qTooButton3_4.setText("300M")
        self.qTooButton3_4.setFont(font2)
        self.qTooButton3_4.setMinimumSize(QSize(200, 25))
        self.qVBoxLayout3.addWidget(self.qTooButton3_1)
        self.qVBoxLayout3.addWidget(self.qTooButton3_2)
        self.qVBoxLayout3.addWidget(self.qTooButton3_3)
        self.qVBoxLayout3.addWidget(self.qTooButton3_4)

        self.qToolBox.addItem(self.qWidget1, "B66")
        self.qToolBox.addItem(self.qWidget2, "B7")
        self.qToolBox.addItem(self.qWidget3, "N78")

        self.qTooButton1_1.setObjectName("qTooButton1_1")
        self.qTooButton1_2.setObjectName("qTooButton1_2")
        self.qTooButton1_3.setObjectName("qTooButton1_3")
        self.qTooButton1_4.setObjectName("qTooButton1_4")
        self.qTooButton2_1.setObjectName("qTooButton2_1")
        self.qTooButton2_2.setObjectName("qTooButton2_2")
        self.qTooButton2_3.setObjectName("qTooButton2_3")
        self.qTooButton2_4.setObjectName("qTooButton2_4")
        self.qTooButton3_1.setObjectName("qTooButton3_1")
        self.qTooButton3_2.setObjectName("qTooButton3_2")
        self.qTooButton3_3.setObjectName("qTooButton3_3")
        self.qTooButton3_4.setObjectName("qTooButton3_4")
        self.qToolBox.setObjectName("qToolBox")
        self.qTabWidget.setObjectName("qTabWidget")
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

############################# overview #############################
        self.qWidget1 = QtWidgets.QWidget()
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(self.qWidget1)
        self.qLabel1_1 = QtWidgets.QLabel("TXNCO", self.qWidget1)
        self.qLabel1_2 = QtWidgets.QLabel("RXNCO", self.qWidget1)
        self.qVBoxLayout1.addWidget(self.qLabel1_1)
        self.qVBoxLayout1.addWidget(self.qLabel1_2)


############################# basic information #############################
        self.qWidget2 = QtWidgets.QWidget()
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qWidget2)
        self.qLabel2_1 = QtWidgets.QLabel("TXNCO", self.qWidget2)
        self.qLabel2_2 = QtWidgets.QLabel("TX", self.qWidget2)
        self.qVBoxLayout2.addWidget(self.qLabel2_1)
        self.qVBoxLayout2.addWidget(self.qLabel2_2)

############################# Test1 #############################


############################# Test2 #############################


############################# Test3 #############################


    @pyqtSlot()
    def on_qTooButton1_1_clicked(self):
        self.ui.qTabWidget.clear()
        self.ui.qTabWidget.addTab(self.qWidget1, "B66 Overview")

    @pyqtSlot()
    def on_qTooButton1_2_clicked(self):
        self.ui.qTabWidget.clear()


    @pyqtSlot()
    def on_qTooButton2_1_clicked(self):
        self.ui.qTabWidget.clear()
        self.ui.qTabWidget.addTab(self.qWidget1, "B7 Overview")

    @pyqtSlot()
    def on_qTooButton3_1_clicked(self):
        self.ui.qTabWidget.clear()
        self.ui.qTabWidget.addTab(self.qWidget1, "N78 Overview")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )