import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt, QSize, pyqtSlot
from PyQt5.QtGui import QIcon, QCursor, QFont, QPixmap
from PyQt5.QtWidgets import QListView, QTreeWidgetItem


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(800, 600)
        self.CqWidget = QtWidgets.QWidget(qMainWindow)
        self.qSplitter = QtWidgets.QSplitter(self.CqWidget)
        self.qSplitter.setOrientation(Qt.Horizontal)
        self.qSplitter.setGeometry(QRect(0, 0, 800, 600))
        self.qTreeWidget = QtWidgets.QTreeWidget(self.qSplitter)
        self.qTreeWidget.setMaximumSize(QSize(220, 16777215))
        self.qTabWidget = QtWidgets.QTabWidget(self.qSplitter)
        qMainWindow.setCentralWidget(self.CqWidget)

        self.qTreeWidget.setColumnCount(1)
        self.qTreeWidget.headerItem().setText(0, "测试报告")
        item1 = QtWidgets.QTreeWidgetItem(self.qTreeWidget)
        item1.setText(0, "B66")
        item1_1 = QtWidgets.QTreeWidgetItem(item1)
        item1_1.setText(0, "Overview")
        item1_2 = QtWidgets.QTreeWidgetItem(item1)
        item1_2.setText(0, "20")
        item1_2_1 = QtWidgets.QTreeWidgetItem(item1_2)
        item1_2_1.setText(0, "L")
        item1_2_2 = QtWidgets.QTreeWidgetItem(item1_2)
        item1_2_2.setText(0, "M")
        item1_2_3 = QtWidgets.QTreeWidgetItem(item1_2)
        item1_2_3.setText(0, "H")
        item1_3 = QtWidgets.QTreeWidgetItem(item1)
        item1_3.setText(0, "20+20")
        item1_3_1 = QtWidgets.QTreeWidgetItem(item1_3)
        item1_3_1.setText(0, "L")
        item1_3_2 = QtWidgets.QTreeWidgetItem(item1_3)
        item1_3_2.setText(0, "M")
        item1_3_3 = QtWidgets.QTreeWidgetItem(item1_3)
        item1_3_3.setText(0, "H")
        item1_4 = QtWidgets.QTreeWidgetItem(item1)
        item1_4.setText(0, "5+10+gap25+20+10")
        item1_4_1 = QtWidgets.QTreeWidgetItem(item1_4)
        item1_4_1.setText(0, "L")
        item1_4_2 = QtWidgets.QTreeWidgetItem(item1_4)
        item1_4_2.setText(0, "M")
        item1_4_3 = QtWidgets.QTreeWidgetItem(item1_4)
        item1_4_3.setText(0, "H")

        item2 = QtWidgets.QTreeWidgetItem(self.qTreeWidget)
        item2.setText(0, "B7")
        item2_1 = QtWidgets.QTreeWidgetItem(item2)
        item2_1.setText(0, "Overview")
        item2_2 = QtWidgets.QTreeWidgetItem(item2)
        item2_2.setText(0, "20")
        item2_2_1 = QtWidgets.QTreeWidgetItem(item2_2)
        item2_2_1.setText(0, "L")
        item2_2_2 = QtWidgets.QTreeWidgetItem(item2_2)
        item2_2_2.setText(0, "M")
        item2_2_3 = QtWidgets.QTreeWidgetItem(item2_2)
        item2_2_3.setText(0, "H")
        item2_3 = QtWidgets.QTreeWidgetItem(item2)
        item2_3.setText(0, "20+20")
        item2_3_1 = QtWidgets.QTreeWidgetItem(item2_3)
        item2_3_1.setText(0, "L")
        item2_3_2 = QtWidgets.QTreeWidgetItem(item2_3)
        item2_3_2.setText(0, "M")
        item2_3_3 = QtWidgets.QTreeWidgetItem(item2_3)
        item2_3_3.setText(0, "H")
        item2_4 = QtWidgets.QTreeWidgetItem(item2)
        item2_4.setText(0, "5+10+gap25+20+10")
        item2_4_1 = QtWidgets.QTreeWidgetItem(item2_4)
        item2_4_1.setText(0, "C")
        
        item3 = QtWidgets.QTreeWidgetItem(self.qTreeWidget)
        item3.setText(0, "N78")
        item3_1 = QtWidgets.QTreeWidgetItem(item3)
        item3_1.setText(0, "Overview")
        item3_2 = QtWidgets.QTreeWidgetItem(item3)
        item3_2.setText(0, "100")
        item3_2_1 = QtWidgets.QTreeWidgetItem(item3_2)
        item3_2_1.setText(0, "L")
        item3_2_2 = QtWidgets.QTreeWidgetItem(item3_2)
        item3_2_2.setText(0, "M")
        item3_2_3 = QtWidgets.QTreeWidgetItem(item3_2)
        item3_2_3.setText(0, "H")
        item3_3 = QtWidgets.QTreeWidgetItem(item3)
        item3_3.setText(0, "200")
        item3_3_1 = QtWidgets.QTreeWidgetItem(item3_3)
        item3_3_1.setText(0, "L")
        item3_3_2 = QtWidgets.QTreeWidgetItem(item3_3)
        item3_3_2.setText(0, "M")
        item3_3_3 = QtWidgets.QTreeWidgetItem(item3_3)
        item3_3_3.setText(0, "H")
        item3_4 = QtWidgets.QTreeWidgetItem(item3)
        item3_4.setText(0, "300")
        item3_4_1 = QtWidgets.QTreeWidgetItem(item3_4)
        item3_4_1.setText(0, "C")

        self.qTreeWidget.setObjectName("qTreeWidget")
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

############################# Pic1 #############################
        self.qWidget3 = QtWidgets.QWidget()
        self.qLabel3_1 = QtWidgets.QLabel(self.qWidget3)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(self.qWidget3)
        self.qPixmap = QPixmap()
        self.qLabel3_1.setPixmap(self.qPixmap)
        self.qVBoxLayout.addWidget(self.qLabel3_1)


############################# Pic2 #############################


############################# Pic3 #############################


    def on_qTreeWidget_itemClicked(self, item: QTreeWidgetItem, column: int):
        if(item.text(0) == "Overview"):
            if(item.parent().text(0) == "B66"):
                self.ui.qTabWidget.clear()
                self.ui.qTabWidget.addTab(self.qWidget1, "B66 Overview")
            elif (item.parent().text(0) == "B7"):
                self.ui.qTabWidget.clear()
                self.ui.qTabWidget.addTab(self.qWidget1, "B7 Overview")
            elif (item.parent().text(0) == "N78"):
                self.ui.qTabWidget.clear()
                self.ui.qTabWidget.addTab(self.qWidget1, "N78 Overview")
        elif(item.text(0) == "L"):
            if(item.parent().text(0) == "20"):
                if(item.parent().parent().text(0) == "B66"):
                    self.ui.qTabWidget.clear()
                    self.ui.qTabWidget.addTab(self.qWidget2, "Basic Information")
                    self.qPixmap.load("../image/scenery.jpg")
                    self.ui.qTabWidget.addTab(self.qWidget3, "Basic Information")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )