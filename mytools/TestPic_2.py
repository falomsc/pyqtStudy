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
        self.qTreeWidget.setMaximumSize(300, 16777215)
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


        ####################  Settings  ####################

        self.qWidget2 = QtWidgets.QWidget()
        self.qVboxLayoutS = QtWidgets.QVBoxLayout(self.qWidget2)
        font = QFont()
        font.setPixelSize(22)
        for i in range(1, 12):
            exec("self.qLabelS%d = QtWidgets.QLabel(self.qWidget2)" % i)
            exec("self.qVboxLayoutS.addWidget(self.qLabelS%d)" % i)
            exec("self.qLabelS%d.setFont(font)" % i)

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
        self.qPixmap = QPixmap()
        self.setWindowState(Qt.WindowMaximized)

    def setPic(self, picNum, basePath):
        self.qPixmap.load(basePath+"_1.png")
        self.ui.qLabelPic1.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab1, "Before DPD")

        self.qPixmap.load(basePath+"_2.png")
        self.ui.qLabelPic2.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab2, "After DPD")

        self.qPixmap.load(basePath+"_3.png")
        self.ui.qLabelPic3.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab3, "Spu1")

        self.qPixmap.load(basePath+"_4.png")
        self.ui.qLabelPic4.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab4, "Spu2")

        self.qPixmap.load(basePath+"_5.png")
        self.ui.qLabelPic5.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab5, "Spu3")

        if(picNum == 6):
            self.qPixmap.load(basePath + "_6.png")
            self.ui.qLabelPic6.setPixmap(self.qPixmap)
            self.ui.qTabWidget.addTab(self.ui.qWidgetTab6, "Spu4")


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
        if(item is self.ui.qTreeWidget.topLevelItem(0).child(1).child(0)):  # B66_20_L
            self.ui.qTabWidget.clear()
            self.ui.qLabelS1.setText("lo = 2110")
            self.ui.qLabelS2.setText("txnco = 10")
            self.ui.qLabelS3.setText("freq = 2120")
            self.ui.qLabelS4.setText("atten = 9.7")
            self.ui.qLabelS5.setText("cfr = 0.41")
            self.ui.qLabelS6.setText("orxgain = 225")
            self.ui.qLabelS7.setText("dpd = Mudra95Coe.txt")
            self.ui.qLabelS8.setText("peak = 655350")
            self.ui.qLabelS9.setText("Regularization_D = 20")
            self.ui.qLabelS10.setText("Regularization_D = 25")
            self.ui.qLabelS11.setText("Damping = 25")
            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            self.setPic(6, ":/pic/B66/B66_20_L")

        elif(item is self.ui.qTreeWidget.topLevelItem(0).child(1).child(1)):    # B66_20_M
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            self.setPic(6, ":/pic/B66/B66_20_M")

        elif(item is self.ui.qTreeWidget.topLevelItem(0).child(1).child(2)):    # B66_20_H
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            self.setPic(6, ":/pic/B66/B66_20_H")

        if(item is self.ui.qTreeWidget.topLevelItem(0).child(2).child(0)):  # B66_20+20_L
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            self.setPic(5, ":/pic/B66/B66_20+20_L")

        elif(item is self.ui.qTreeWidget.topLevelItem(0).child(2).child(1)):    # B66_20+20_M
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            self.setPic(5, ":/pic/B66/B66_20+20_M")

        elif(item is self.ui.qTreeWidget.topLevelItem(0).child(2).child(2)):    # B66_20+20_H
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            self.setPic(5, ":/pic/B66/B66_20+20_H")

        if(item is self.ui.qTreeWidget.topLevelItem(0).child(3).child(0)):  # B66_5+10+gap25+20+10_L
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            self.setPic(5, ":/pic/B66/B66_5+10+gap25+20+10_L")

        elif(item is self.ui.qTreeWidget.topLevelItem(0).child(3).child(1)):    # B66_5+10+gap25+20+10_M
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            self.setPic(5, ":/pic/B66/B66_5+10+gap25+20+10_M")

        elif(item is self.ui.qTreeWidget.topLevelItem(0).child(3).child(2)):    # B66_5+10+gap25+20+10_H
            self.ui.qTabWidget.clear()

            self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
            self.setPic(5, ":/pic/B66/B66_5+10+gap25+20+10_H")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )