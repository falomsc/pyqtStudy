'''
qMainWindow(qSplitter)
|--qTreeWidget
|--qTabWidget
    |--qScrollArea
        |--qWidget(qVBoxLayout)
            |--qLabel

'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt, QSize, pyqtSlot
from PyQt5.QtGui import QIcon, QCursor, QFont, QPixmap, QImage
from PyQt5.QtWidgets import QListView, QTreeWidgetItem
import rec.res
# :/pic/B66/B66_5+10+gap25+20+10_H_1.png

class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(800, 600)
        self.qSplitter = QtWidgets.QSplitter(qMainWindow)
        self.qSplitter.setOrientation(Qt.Horizontal)
        self.qTreeWidget = QtWidgets.QTreeWidget(self.qSplitter)
        self.qTreeWidget.setMaximumSize(200, 16777215)
        self.qTabWidget = QtWidgets.QTabWidget(self.qSplitter)
        self.qTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.qTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.qTabWidget.setDocumentMode(True)
        qMainWindow.setCentralWidget(self.qSplitter)

        ####################  QTreeWidget  ####################
        self.qTreeWidget.setColumnCount(1)
        self.qTreeWidget.headerItem().setText(0, "测试报告")

        detail = {"B66": ("Overview", "20", "20+20", "5+10+gap25+20+10"),
                  "B7": ("Overview", "20", "20+20", "20+gap30+20"),
                  "N78_TX0": ("Overview", "100", "100+100", "50+gap90+60"),
                  "N78_TX1": ("Overview", "100", "100+100", "50+gap90+60")}
        n = 1
        for key in detail.keys():
            exec("item%d = QtWidgets.QTreeWidgetItem(self.qTreeWidget)" % n)
            exec("item%d.setText(0, '%s')" % (n, key))
            m = 1
            for i in detail[key]:
                exec("item%d_%d = QtWidgets.QTreeWidgetItem(item%d)" % (n, m, n))
                exec("item%d_%d.setText(0, '%s')" % (n, m, i))
                if (i != "Overview"):
                    if (i in ("20", "20+20", "100", "5+10+gap25+20+10")):
                        k = 1
                        for j in ("L", "M", "H"):
                            exec("item%d_%d_%d = QtWidgets.QTreeWidgetItem(item%d_%d)" % (n, m, k, n, m))
                            exec("item%d_%d_%d.setText(0, '%s')" % (n, m, k, j))
                            k += 1
                    elif (i in ("100+100", "50+gap90+60")):
                        k = 1
                        for j in ("L", "H"):
                            exec("item%d_%d_%d = QtWidgets.QTreeWidgetItem(item%d_%d)" % (n, m, k, n, m))
                            exec("item%d_%d_%d.setText(0, '%s')" % (n, m, k, j))
                            k += 1
                    elif (i == "20+gap30+20"):
                        exec("item%d_%d_1 = QtWidgets.QTreeWidgetItem(item%d_%d)" % (n, m, n, m))
                        exec("item%d_%d_1.setText(0, 'C')" % (n, m,))
                m += 1
            n += 1

        ####################  QTabWidget  ####################


        ####################  Overview  ####################

        self.qWidget1 = QtWidgets.QWidget()


        ####################  Basic Information  ####################

        self.qWidget2 = QtWidgets.QWidget()

        ####################  Pic1~6  ####################

        # self.qWidgetTab1 = QtWidgets.QWidget()
        # # self.qTabWidget.addTab(self.qWidgetTab1, "pic")
        #
        # self.qScrollArea1 = QtWidgets.QScrollArea(self.qWidgetTab1)
        # self.qScrollArea1.setWidgetResizable(True)
        #
        # self.qVboxLayoutTab1 = QtWidgets.QVBoxLayout(self.qWidgetTab1)
        # self.qVboxLayoutTab1.addWidget(self.qScrollArea1)
        #
        # self.qWidgetPic1 = QtWidgets.QWidget()
        # self.qScrollArea1.setWidget(self.qWidgetPic1)
        # self.qVboxLayoutPic1 = QtWidgets.QVBoxLayout(self.qWidgetPic1)
        #
        # self.qLabelPic1 = QtWidgets.QLabel(self.qWidgetPic1)
        # self.qLabelPic1.setAlignment(Qt.AlignCenter)
        # # self.qLabelPic1.setPixmap(QPixmap(":/pic/B66/B66_5+10+gap25+20+10_H_1.png"))
        # self.qVboxLayoutPic1.addWidget(self.qLabelPic1)


        for i in range(1, 7):
            exec("self.qWidgetTab%d = QtWidgets.QWidget()" % i)
            exec("self.qScrollArea%d = QtWidgets.QScrollArea(self.qWidgetTab%d)" % (i, i))
            exec("self.qScrollArea%d.setWidgetResizable(True)" % i)
            exec("self.qVboxLayoutTab%d = QtWidgets.QVBoxLayout(self.qWidgetTab%d)" % (i, i))
            exec("self.qVboxLayoutTab%d.addWidget(self.qScrollArea%d)" % (i, i))
            exec("self.qWidgetPic%d = QtWidgets.QWidget()" % i)
            exec("self.qScrollArea%d.setWidget(self.qWidgetPic%d)" % (i, i))
            exec("self.qVboxLayoutPic%d = QtWidgets.QVBoxLayout(self.qWidgetPic%d)" % (i, i))
            exec("self.qLabelPic%d = QtWidgets.QLabel(self.qWidgetPic%d)" % (i, i))
            exec("self.qLabelPic%d.setAlignment(Qt.AlignCenter)" % i)
            exec("self.qVboxLayoutPic%d.addWidget(self.qLabelPic%d)" % (i, i))

        self.qTreeWidget.setObjectName("qTreeWidget")
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def on_qTreeWidget_itemClicked(self, item: QTreeWidgetItem, column: int):

        ####################  Set Overview  ####################
        if(item is self.ui.qTreeWidget.topLevelItem(0).child(0)):   # B66 Overview
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget1, "B66 Overview")

        elif(item is self.ui.qTreeWidget.topLevelItem(1).child(0)): # B7 Overview
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget1, "B7 Overview")

        elif(item is self.ui.qTreeWidget.topLevelItem(2).child(0)): # N78_TX0 Overview
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget1, "N78_TX0 Overview")

        elif(item is self.ui.qTreeWidget.topLevelItem(3).child(0)): # N78_TX1 Overview
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget1, "N78_TX1 Overview")

        ####################  Set B66  ####################
        if(item is self.ui.qTreeWidget.topLevelItem(0).child(1).child(0)):  # B66_20_L Overview
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            qPixmap = QPixmap()

            qPixmap.load(":/pic/B66/B66_20_L_1.png")
            self.ui.qLabelPic1.setPixmap(qPixmap)
            self.ui.qTabWidget.addTab(self.ui.qWidgetTab1, "Before DPD")

            qPixmap.load(":/pic/B66/B66_20_L_2.png")
            self.ui.qLabelPic2.setPixmap(qPixmap)
            self.ui.qTabWidget.addTab(self.ui.qWidgetTab2, "After DPD")

            qPixmap.load(":/pic/B66/B66_20_L_3.png")
            self.ui.qLabelPic3.setPixmap(qPixmap)
            self.ui.qTabWidget.addTab(self.ui.qWidgetTab3, "Spu1")

            qPixmap.load(":/pic/B66/B66_20_L_4.png")
            self.ui.qLabelPic4.setPixmap(qPixmap)
            self.ui.qTabWidget.addTab(self.ui.qWidgetTab4, "Spu2")

            qPixmap.load(":/pic/B66/B66_20_L_5.png")
            self.ui.qLabelPic5.setPixmap(qPixmap)
            self.ui.qTabWidget.addTab(self.ui.qWidgetTab5, "Spu3")

            qPixmap.load(":/pic/B66/B66_20_L_6.png")
            self.ui.qLabelPic6.setPixmap(qPixmap)
            self.ui.qTabWidget.addTab(self.ui.qWidgetTab6, "Spu4")




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )