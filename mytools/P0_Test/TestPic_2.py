'''
qMainWindow(qSplitter)
|--qTreeWidget
|--qTabWidget
    |--qScrollArea
        |--qWidget(qVBoxLayout)
            |--qLabel

'''
import sys
import xlrd

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QTreeWidgetItem

# ./pic/B66/B66_5+10+gap25+20+10_H_1.png

class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(800, 600)
        qMainWindow.setWindowTitle("PA Test Report")
        self.qSplitter = QtWidgets.QSplitter(qMainWindow)
        self.qSplitter.setOrientation(Qt.Horizontal)
        self.qTreeWidget = QtWidgets.QTreeWidget(self.qSplitter)
        self.qTreeWidget.setMaximumSize(300, 16777215)
        self.qTabWidget = QtWidgets.QTabWidget(self.qSplitter)
        self.qTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.qTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.qTabWidget.setDocumentMode(True)
        font = QFont()
        font.setPointSize(10)
        self.qTabWidget.setFont(font)
        qMainWindow.setCentralWidget(self.qSplitter)
        qMainWindow.setWindowIcon(QIcon("./Pic/icon.png"))

        ####################  QTreeWidget  ####################
        self.qTreeWidget.setColumnCount(1)
        self.qTreeWidget.headerItem().setText(0, "测试报告")

        detail = {"B66": ("Overview", "20", "20+20", "20+10+5+10", "5+10+gap25+20+10"),
                  "B7": ("Overview", "20", "20+20", "20+gap30+20"),
                  "N78_TX0_without_filter": ("Overview", "100", "100+100", "50+gap90+60"),
                  "N78_TX0_with_filter": ("Overview", "100", "100+100", "50+gap90+60"),
                  "N78_TX1_without_filter": ("Overview", "100", "100+100", "50+gap90+60"),
                  "N78_TX1_with_filter": ("Overview", "100", "100+100", "50+gap90+60")
                  }

        n = 1
        for key in detail.keys():
            exec("item%d = QtWidgets.QTreeWidgetItem(self.qTreeWidget)" % n)
            exec("item%d.setText(0, '%s')" % (n, key))
            m = 1
            for i in detail[key]:
                exec("item%d_%d = QtWidgets.QTreeWidgetItem(item%d)" % (n, m, n))
                exec("item%d_%d.setText(0, '%s')" % (n, m, i))
                if (i != "Overview"):
                    if (i in ("20", "20+20", "100", "5+10+gap25+20+10", "20+10+5+10")):
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

        ####################  Overview  ####################
        self.qWidget1 = QtWidgets.QWidget()
        self.qGroupBox = QtWidgets.QGroupBox(self.qWidget1)
        self.qGroupBox.setGeometry(0, 0, 250, 300)
        self.qVboxLayout1 = QtWidgets.QVBoxLayout(self.qGroupBox)
        self.qLabel1 = QtWidgets.QLabel(self.qGroupBox)
        self.qLabel2 = QtWidgets.QLabel(self.qGroupBox)
        self.qLabel3 = QtWidgets.QLabel(self.qGroupBox)
        self.qLabel4 = QtWidgets.QLabel(self.qGroupBox)
        self.qVboxLayout1.addWidget(self.qLabel1)
        self.qVboxLayout1.addWidget(self.qLabel2)
        self.qVboxLayout1.addWidget(self.qLabel3)
        self.qVboxLayout1.addWidget(self.qLabel4)

        ####################  Settings  ####################
        self.qWidget2 = QtWidgets.QWidget()
        self.qVboxLayoutS = QtWidgets.QVBoxLayout(self.qWidget2)

        self.qTableWidget = QtWidgets.QTableWidget(self.qWidget2)
        self.qTableWidget.setAlternatingRowColors(True)
        self.qTableWidget.setRowCount(12)
        self.qTableWidget.setColumnCount(2)
        self.qTableWidget.setColumnWidth(0, 200)
        self.qTableWidget.setColumnWidth(1, 200)
        self.qTableWidget.horizontalHeader().setVisible(False)

        self.qVboxLayoutS.addWidget(self.qTableWidget)

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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.qPixmap = QPixmap()
        self.setWindowState(Qt.WindowMaximized)

    def setPic(self, picNum, basePath):
        self.qPixmap.load(basePath + "_1.png")
        self.ui.qLabelPic1.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab1, "Before DPD")

        self.qPixmap.load(basePath + "_2.png")
        self.ui.qLabelPic2.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab2, "After DPD")

        self.qPixmap.load(basePath + "_3.png")
        self.ui.qLabelPic3.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab3, "Spu1")

        self.qPixmap.load(basePath + "_4.png")
        self.ui.qLabelPic4.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab4, "Spu2")

        self.qPixmap.load(basePath + "_5.png")
        self.ui.qLabelPic5.setPixmap(self.qPixmap)
        self.ui.qTabWidget.addTab(self.ui.qWidgetTab5, "Spu3")

        if (picNum == 6):
            self.qPixmap.load(basePath + "_6.png")
            self.ui.qLabelPic6.setPixmap(self.qPixmap)
            self.ui.qTabWidget.addTab(self.ui.qWidgetTab6, "Spu4")

    def setOverview(self, band):
        self.ui.qTabWidget.clear()
        dict = {"B66": 0, "B7": 1, "N78": 2}
        data = xlrd.open_workbook("TestReport.xlsx")
        table = data.sheet_by_name("Overview")
        self.ui.qLabel1.setText(table.cell_value(dict[band], 1))
        self.ui.qLabel2.setText(table.cell_value(dict[band], 2))
        self.ui.qLabel3.setText(table.cell_value(dict[band], 3))
        self.ui.qLabel4.setText(table.cell_value(dict[band], 4))
        self.ui.qTabWidget.addTab(self.ui.qWidget1, band + " Overview")

    def setSettings(self, band, row, picNum, basePath):
        self.ui.qTabWidget.clear()
        data = xlrd.open_workbook("TestReport.xlsx")
        table = data.sheet_by_name(band)
        self.ui.qTableWidget.clear()
        for i in range(12):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(table.cell_value(0, i + 2)))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.qTableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(table.cell_value(row, i + 2)))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.qTableWidget.setItem(i, 1, item)
        self.ui.qTabWidget.addTab(self.ui.qWidget2, "Settings")
        self.setPic(picNum, basePath)

    def on_qTreeWidget_itemClicked(self, item: QTreeWidgetItem, column: int):

        ####################  Set Overview  ####################
        if (item is self.ui.qTreeWidget.topLevelItem(0).child(0)):  # B66 Overview
            self.setOverview("B66")

        elif (item is self.ui.qTreeWidget.topLevelItem(1).child(0)):  # B7 Overview
            self.setOverview("B7")

        elif (item is self.ui.qTreeWidget.topLevelItem(2).child(0)):  # N78_TX0_without_filter Overview
            self.setOverview("N78")

        elif (item is self.ui.qTreeWidget.topLevelItem(3).child(0)):  # N78_TX0_with_filter Overview
            self.setOverview("N78")

        elif (item is self.ui.qTreeWidget.topLevelItem(4).child(0)):  # N78_TX1_without_filter Overview
            self.setOverview("N78")

        elif (item is self.ui.qTreeWidget.topLevelItem(5).child(0)):  # N78_TX1_with_filter Overview
            self.setOverview("N78")

        ####################  Set B66  ####################
        if (item is self.ui.qTreeWidget.topLevelItem(0).child(1).child(0)):  # B66_20_L
            self.setSettings("B66", 1, 6, "./pic/B66/B66_20_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(1).child(1)):  # B66_20_M
            self.setSettings("B66", 2, 6, "./pic/B66/B66_20_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(1).child(2)):  # B66_20_H
            self.setSettings("B66", 3, 6, "./pic/B66/B66_20_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(2).child(0)):  # B66_20+20_L
            self.setSettings("B66", 4, 5, "./pic/B66/B66_20+20_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(2).child(1)):  # B66_20+20_M
            self.setSettings("B66", 5, 5, "./pic/B66/B66_20+20_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(2).child(2)):  # B66_20+20_H
            self.setSettings("B66", 6, 5, "./pic/B66/B66_20+20_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(3).child(0)):  # B66_20+10+5+10_L
            self.setSettings("B66", 7, 6, "./pic/B66/B66_20+10+5+10_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(3).child(1)):  # B66_20+10+5+10_M
            self.setSettings("B66", 8, 6, "./pic/B66/B66_20+10+5+10_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(3).child(2)):  # B66_20+10+5+10_H
            self.setSettings("B66", 9, 6, "./pic/B66/B66_20+10+5+10_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(4).child(0)):  # B66_5+10+gap25+20+10_L
            self.setSettings("B66", 10, 5, "./pic/B66/B66_5+10+gap25+20+10_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(4).child(1)):  # B66_5+10+gap25+20+10_M
            self.setSettings("B66", 11, 5, "./pic/B66/B66_5+10+gap25+20+10_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(0).child(4).child(2)):  # B66_5+10+gap25+20+10_H
            self.setSettings("B66", 12, 5, "./pic/B66/B66_5+10+gap25+20+10_H")

        ####################  Set B7  ####################
        if (item is self.ui.qTreeWidget.topLevelItem(1).child(1).child(0)):  # B7_20_L
            self.setSettings("B7", 1, 6, "./pic/B7/B7_20_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(1).child(1).child(1)):  # B7_20_M
            self.setSettings("B7", 2, 6, "./pic/B7/B7_20_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(1).child(1).child(2)):  # B7_20_H
            self.setSettings("B7", 3, 6, "./pic/B7/B7_20_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(1).child(2).child(0)):  # B7_20+20_L
            self.setSettings("B7", 4, 6, "./pic/B7/B7_20+20_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(1).child(2).child(1)):  # B7_20+20_M
            self.setSettings("B7", 5, 6, ":/pic/B7/B7_20+20_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(1).child(2).child(2)):  # B7_20+20_H
            self.setSettings("B7", 6, 6, "./pic/B7/B7_20+20_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(1).child(3).child(0)):  # B7_20+gap30+20_C
            self.setSettings("B7", 7, 6, "./pic/B7/B7_20+gap30+20_C")

        ####################  Set N78_TX0_without_filter  ####################
        if (item is self.ui.qTreeWidget.topLevelItem(2).child(1).child(0)):  # N78_TX0_without_filter_100_L
            self.setSettings("N78_TX0_without_filter", 1, 5,
                             "./pic/N78_TX0_without_filter/N78_TX0_without_filter_100_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(2).child(1).child(1)):  # N78_TX0_without_filter_100_M
            self.setSettings("N78_TX0_without_filter", 2, 5,
                             "./pic/N78_TX0_without_filter/N78_TX0_without_filter_100_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(2).child(1).child(2)):  # N78_TX0_without_filter_100_H
            self.setSettings("N78_TX0_without_filter", 3, 5,
                             "./pic/N78_TX0_without_filter/N78_TX0_without_filter_100_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(2).child(2).child(0)):  # N78_TX0_without_filter_100+100_L
            self.setSettings("N78_TX0_without_filter", 4, 5,
                             "./pic/N78_TX0_without_filter/N78_TX0_without_filter_100+100_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(2).child(2).child(1)):  # N78_TX0_without_filter_100+100_H
            self.setSettings("N78_TX0_without_filter", 5, 5,
                             "./pic/N78_TX0_without_filter/N78_TX0_without_filter_100+100_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(2).child(3).child(0)):  # N78_TX0_without_filter_50+gap90+60_L
            self.setSettings("N78_TX0_without_filter", 6, 5,
                             "./pic/N78_TX0_without_filter/N78_TX0_without_filter_50+gap90+60_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(2).child(3).child(1)):  # N78_TX0_without_filter_50+gap90+60_H
            self.setSettings("N78_TX0_without_filter", 7, 5,
                             "./pic/N78_TX0_without_filter/N78_TX0_without_filter_50+gap90+60_H")

        ####################  Set N78_TX0_with_filter  ####################
        if (item is self.ui.qTreeWidget.topLevelItem(3).child(1).child(0)):  # N78_TX0_with_filter_100_L
            self.setSettings("N78_TX0_with_filter", 1, 5, "./pic/N78_TX0_with_filter/N78_TX0_with_filter_100_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(3).child(1).child(1)):  # N78_TX0_with_filter_100_M
            self.setSettings("N78_TX0_with_filter", 2, 5, "./pic/N78_TX0_with_filter/N78_TX0_with_filter_100_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(3).child(1).child(2)):  # N78_TX0_with_filter_100_H
            self.setSettings("N78_TX0_with_filter", 3, 5, "./pic/N78_TX0_with_filter/N78_TX0_with_filter_100_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(3).child(2).child(0)):  # N78_TX0_with_filter_100+100_L
            self.setSettings("N78_TX0_with_filter", 4, 5, "./pic/N78_TX0_with_filter/N78_TX0_with_filter_100+100_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(3).child(2).child(1)):  # N78_TX0_with_filter_100+100_H
            self.setSettings("N78_TX0_with_filter", 5, 5, "./pic/N78_TX0_with_filter/N78_TX0_with_filter_100+100_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(3).child(3).child(0)):  # N78_TX0_with_filter_50+gap90+60_L
            self.setSettings("N78_TX0_with_filter", 6, 5, "./pic/N78_TX0_with_filter/N78_TX0_with_filter_50+gap90+60_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(3).child(3).child(1)):  # N78_TX0_with_filter_50+gap90+60_H
            self.setSettings("N78_TX0_with_filter", 7, 5, "./pic/N78_TX0_with_filter/N78_TX0_with_filter_50+gap90+60_H")

            ####################  Set N78_TX1_without_filter  ####################
        if (item is self.ui.qTreeWidget.topLevelItem(4).child(1).child(0)):  # N78_TX1_without_filter_100_L
            self.setSettings("N78_TX1_without_filter", 1, 5,
                             "./pic/N78_TX1_without_filter/N78_TX1_without_filter_100_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(4).child(1).child(1)):  # N78_TX1_without_filter_100_M
            self.setSettings("N78_TX1_without_filter", 2, 5,
                             "./pic/N78_TX1_without_filter/N78_TX1_without_filter_100_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(4).child(1).child(2)):  # N78_TX1_without_filter_100_H
            self.setSettings("N78_TX1_without_filter", 3, 5,
                             "./pic/N78_TX1_without_filter/N78_TX1_without_filter_100_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(4).child(2).child(0)):  # N78_TX1_without_filter_100+100_L
            self.setSettings("N78_TX1_without_filter", 4, 5,
                             "./pic/N78_TX1_without_filter/N78_TX1_without_filter_100+100_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(4).child(2).child(1)):  # N78_TX1_without_filter_100+100_H
            self.setSettings("N78_TX1_without_filter", 5, 5,
                             "./pic/N78_TX1_without_filter/N78_TX1_without_filter_100+100_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(4).child(3).child(0)):  # N78_TX1_without_filter_50+gap90+60_L
            self.setSettings("N78_TX1_without_filter", 6, 5,
                             "./pic/N78_TX1_without_filter/N78_TX1_without_filter_50+gap90+60_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(4).child(3).child(1)):  # N78_TX1_without_filter_50+gap90+60_H
            self.setSettings("N78_TX1_without_filter", 7, 5,
                             "./pic/N78_TX1_without_filter/N78_TX1_without_filter_50+gap90+60_H")

            ####################  Set N78_TX1_with_filter  ####################
        if (item is self.ui.qTreeWidget.topLevelItem(5).child(1).child(0)):  # N78_TX1_with_filter_100_L
            self.setSettings("N78_TX1_with_filter", 1, 5, "./pic/N78_TX1_with_filter/N78_TX1_with_filter_100_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(5).child(1).child(1)):  # N78_TX1_with_filter_100_M
            self.setSettings("N78_TX1_with_filter", 2, 5, "./pic/N78_TX1_with_filter/N78_TX1_with_filter_100_M")

        elif (item is self.ui.qTreeWidget.topLevelItem(5).child(1).child(2)):  # N78_TX1_with_filter_100_H
            self.setSettings("N78_TX1_with_filter", 3, 5, "./pic/N78_TX1_with_filter/N78_TX1_with_filter_100_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(5).child(2).child(0)):  # N78_TX1_with_filter_100+100_L
            self.setSettings("N78_TX1_with_filter", 4, 5, "./pic/N78_TX1_with_filter/N78_TX1_with_filter_100+100_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(5).child(2).child(1)):  # N78_TX1_with_filter_100+100_H
            self.setSettings("N78_TX1_with_filter", 5, 5, "./pic/N78_TX1_with_filter/N78_TX1_with_filter_100+100_H")

        elif (item is self.ui.qTreeWidget.topLevelItem(5).child(3).child(0)):  # N78_TX1_with_filter_50+gap90+60_L
            self.setSettings("N78_TX1_with_filter", 6, 5, "./pic/N78_TX1_with_filter/N78_TX1_with_filter_50+gap90+60_L")

        elif (item is self.ui.qTreeWidget.topLevelItem(5).child(3).child(1)):  # N78_TX1_with_filter_50+gap90+60_H
            self.setSettings("N78_TX1_with_filter", 7, 5, "./pic/N78_TX1_with_filter/N78_TX1_with_filter_50+gap90+60_H")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )