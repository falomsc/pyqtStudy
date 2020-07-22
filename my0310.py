'''
结构图：
qMainWindow
|--qWidget1

'''
import sys
from enum import Enum

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt, QSize, pyqtSlot, QDir, QFileInfo, QDate
from PyQt5.QtGui import QIcon, QCursor, QBrush
from PyQt5.QtWidgets import QListView, QFileDialog, QFrame, QAbstractItemView, QTableWidgetItem, QLabel


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(837, 471)
        self.qWidget1 = QtWidgets.QWidget(qMainWindow)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(self.qWidget1)
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        self.qSplitter1 = QtWidgets.QSplitter(self.qWidget1)
        self.qSplitter1.setOrientation(Qt.Horizontal)
        self.qGroupBox = QtWidgets.QGroupBox(self.qSplitter1)
        self.qGroupBox.setMaximumSize(QSize(300, 16777215))
        self.qGridLayout = QtWidgets.QGridLayout(self.qGroupBox)
        self.qSplitter2 = QtWidgets.QSplitter(self.qSplitter1)
        self.qSplitter2.setOrientation(Qt.Vertical)
        self.qSplitter2.setFrameShape(QFrame.NoFrame)
        self.qSplitter2.setFrameShadow(QFrame.Plain)

        qMainWindow.setCentralWidget(self.qWidget1)
        qMainWindow.setStatusBar(self.qStatusBar)
        self.qVBoxLayout.addWidget(self.qSplitter1)

        self.qPushButton1 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton1.setText("设置表头")
        self.qPushButton2 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton2.setText("设置行数")
        self.qPushButton3 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton3.setText("初始化表格数据")
        self.qPushButton4 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton4.setText("插入行")
        self.qPushButton5 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton5.setText("添加行")
        self.qPushButton6 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton6.setText("删除当前行")
        self.qPushButton7 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton7.setText("清空表格数据")
        self.qPushButton8 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton8.setText("自动调节行高")
        self.qPushButton9 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton9.setText("自动调节列宽")
        self.qPushButton10 = QtWidgets.QPushButton(self.qGroupBox)
        self.qPushButton10.setText("读取表格内容到文本")
        self.qCheckBox1 = QtWidgets.QCheckBox(self.qGroupBox)
        self.qCheckBox1.setText("表格可编辑")
        self.qCheckBox1.setChecked(True)
        self.qCheckBox2 = QtWidgets.QCheckBox(self.qGroupBox)
        self.qCheckBox2.setText("间隔行底色")
        self.qCheckBox2.setChecked(True)
        self.qCheckBox3 = QtWidgets.QCheckBox(self.qGroupBox)
        self.qCheckBox3.setText("显示行表头")
        self.qCheckBox3.setChecked(True)
        self.qCheckBox4 = QtWidgets.QCheckBox(self.qGroupBox)
        self.qCheckBox4.setText("显示列表头")
        self.qCheckBox4.setChecked(True)
        self.qRadioButton1 = QtWidgets.QRadioButton(self.qGroupBox)
        self.qRadioButton1.setText("行选择")
        self.qRadioButton2 = QtWidgets.QRadioButton(self.qGroupBox)
        self.qRadioButton2.setText("单元格选择")
        self.qRadioButton2.setChecked(True)
        self.qSpinBox = QtWidgets.QSpinBox(self.qGroupBox)
        self.qSpinBox.setValue(8)

        self.qGridLayout.addWidget(self.qPushButton1, 0, 0, 1, 2)
        self.qGridLayout.addWidget(self.qPushButton2, 1, 0, 1, 1)
        self.qGridLayout.addWidget(self.qSpinBox, 1, 1, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton3, 2, 0, 1, 2)
        self.qGridLayout.addWidget(self.qPushButton4, 3, 0, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton5, 3, 1, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton6, 4, 0, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton7, 4, 1, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton8, 5, 0, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton9, 5, 1, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton10, 6, 0, 1, 2)
        self.qGridLayout.addWidget(self.qCheckBox1, 7, 0, 1, 1)
        self.qGridLayout.addWidget(self.qCheckBox2, 7, 1, 1, 1)
        self.qGridLayout.addWidget(self.qCheckBox3, 8, 0, 1, 1)
        self.qGridLayout.addWidget(self.qCheckBox4, 8, 1, 1, 1)
        self.qGridLayout.addWidget(self.qRadioButton1, 9, 0, 1, 1)
        self.qGridLayout.addWidget(self.qRadioButton2, 9, 1, 1, 1)

        self.qTableWidget = QtWidgets.QTableWidget(self.qSplitter2)
        self.qPlainTextEdit = QtWidgets.QPlainTextEdit(self.qSplitter2)
        self.qTableWidget.setAlternatingRowColors(True)
        self.qTableWidget.setRowCount(5)
        self.qTableWidget.setColumnCount(4)
        self.qTableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.qTableWidget.verticalHeader().setDefaultSectionSize(30)
        item = QtWidgets.QTableWidgetItem()
        item.setText("列1")
        self.qTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("列2")
        self.qTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("列3")
        self.qTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("0行，0列")
        self.qTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(QIcon("./image/boy.ico"))
        item.setText("0行，1列")
        self.qTableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(Qt.Checked)
        item.setText("0行，2列")
        self.qTableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("0行，3列")
        self.qTableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("1行，0列")
        self.qTableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(QIcon("./image/girl.ico"))
        item.setText("1行，1列")
        self.qTableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(Qt.Checked)
        self.qTableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("2行，0列")
        self.qTableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qTableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.qTableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("3行，0列")
        self.qTableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qTableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("4行，0列")
        self.qTableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qTableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.qTableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("4行，3列")
        self.qTableWidget.setItem(4, 3, item)

        self.qPushButton1.setObjectName("qPushButton1")
        self.qPushButton2.setObjectName("qPushButton2")
        self.qPushButton3.setObjectName("qPushButton3")
        self.qPushButton4.setObjectName("qPushButton4")
        self.qPushButton5.setObjectName("qPushButton5")
        self.qPushButton6.setObjectName("qPushButton6")
        self.qPushButton7.setObjectName("qPushButton7")
        self.qPushButton8.setObjectName("qPushButton8")
        self.qPushButton9.setObjectName("qPushButton9")
        self.qPushButton10.setObjectName("qPushButton10")
        self.qCheckBox1.setObjectName("qCheckBox1")
        self.qCheckBox2.setObjectName("qCheckBox2")
        self.qCheckBox3.setObjectName("qCheckBox3")
        self.qCheckBox4.setObjectName("qCheckBox4")
        self.qRadioButton1.setObjectName("qRadioButton1")
        self.qRadioButton2.setObjectName("qRadioButton2")
        self.qSpinBox.setObjectName("qSpinBox")
        self.qTableWidget.setObjectName("qTableWidget")

        QtCore.QMetaObject.connectSlotsByName(qMainWindow)




class QmyMainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.qLabel1 = QtWidgets.QLabel("当前单元格坐标：", self)
        self.qLabel1.setMinimumWidth(250)
        self.qLabel2 = QtWidgets.QLabel("当前单元格类型：", self)
        self.qLabel2.setMinimumWidth(200)
        self.qLabel3 = QtWidgets.QLabel("学生ID：", self)
        self.qLabel3.setMinimumWidth(200)
        self.ui.qStatusBar.addWidget(self.qLabel1)
        self.ui.qStatusBar.addWidget(self.qLabel2)
        self.ui.qStatusBar.addWidget(self.qLabel3)
        self.__tableInitialized = False

    def __createItemsARow(self, rowNo, name, sex, birth, nation, isParty, score):

        StudID = 201805000 + rowNo
        item = QtWidgets.QTableWidgetItem(name, 1000)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = item.font()
        font.setBold(True)
        item.setFont(font)
        item.setData(Qt.UserRole, StudID)

        self.ui.qTableWidget.setItem(rowNo, 0, item)
        if sex == "男":
            icon = QIcon("./image/boy.ico")
        else:
            icon = QIcon("./image/girl.ico")
        item = QtWidgets.QTableWidgetItem(sex, 1001)
        item.setIcon(icon)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.qTableWidget.setItem(rowNo, 1, item)

        strBirth = birth.toString("yyyy-MM-dd")
        item = QtWidgets.QTableWidgetItem(strBirth, 1002)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.qTableWidget.setItem(rowNo, 2, item)

        item = QtWidgets.QTableWidgetItem(nation, 1003)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        if nation != "汉族":
            item.setForeground(QBrush(Qt.blue))
        self.ui.qTableWidget.setItem(rowNo, 3, item)

        strScore = str(score)
        item = QtWidgets.QTableWidgetItem(strScore, 1004)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.ui.qTableWidget.setItem(rowNo, 4, item)

        item = QtWidgets.QTableWidgetItem("党员", 1005)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        if isParty:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setBackground(QBrush(Qt.yellow))
        self.ui.qTableWidget.setItem(rowNo, 5, item)

    @pyqtSlot()
    def on_qPushButton1_clicked(self):  # 设置表头
        headerText = ["姓 名", "性 别", "出生日期", "民 族", "分数", "是否党员"]
        self.ui.qTableWidget.setColumnCount(len(headerText))
        for i in range(len(headerText)):
            headerItem = QtWidgets.QTableWidgetItem(headerText[i])
            font = headerItem.font()
            font.setPointSize(11)
            headerItem.setFont(font)
            headerItem.setForeground(QBrush(Qt.red))
            self.ui.qTableWidget.setHorizontalHeaderItem(i, headerItem)

    @pyqtSlot()
    def on_qPushButton2_clicked(self):  # 设置行数
        self.ui.qTableWidget.setRowCount(self.ui.qSpinBox.value())
        self.ui.qTableWidget.setAlternatingRowColors(self.ui.qCheckBox2.isChecked())

    @pyqtSlot()
    def on_qPushButton3_clicked(self):  # 初始化表格数据
        self.ui.qTableWidget.clearContents()
        birth = QDate(1998, 6, 23)
        isParty = True
        nation = "汉族"
        score = 70
        rowCount = self.ui.qTableWidget.rowCount()
        for i in range(rowCount):
            strName = "学生%d" % i
            if i % 2 == 0:
                strSex = "男"
            else:
                strSex = "女"
            self.__createItemsARow(i, strName, strSex, birth, nation, isParty, score)
            birth = birth.addDays(20)
            isParty = not isParty
        self.__tableInitialized = True

    @pyqtSlot()
    def on_qPushButton4_clicked(self):  # 插入行
        curRow = self.ui.qTableWidget.currentRow()
        self.ui.qTableWidget.insertRow(curRow)
        birth = QDate.fromString("1998-4-5", "yyyy-M-d")
        self.__createItemsARow(curRow, "新学生", "男", birth, "苗族", True, 65)

    @pyqtSlot()
    def on_qPushButton5_clicked(self):  # 添加行
        curRow = self.ui.qTableWidget.rowCount()
        self.ui.qTableWidget.insertRow(curRow)
        birth = QDate.fromString("1999-1-10", "yyyy-M-d")
        self.__createItemsARow(curRow, "新生", "女", birth, "土家", False, 86)

    @pyqtSlot()
    def on_qPushButton6_clicked(self):  # 删除当前行
        curRow = self.ui.qTableWidget.currentRow()
        self.ui.qTableWidget.removeRow(curRow)

    @pyqtSlot()
    def on_qPushButton7_clicked(self):  # 清空表格内容
        self.ui.qTableWidget.clearContents()

    @pyqtSlot()
    def on_qPushButton8_clicked(self):  # 自动调节行高
        self.ui.qTableWidget.resizeRowsToContents()

    @pyqtSlot()
    def on_qPushButton9_clicked(self):  # 自动调节行高
        self.ui.qTableWidget.resizeColumnsToContents()

    @pyqtSlot()
    def on_qPushButton10_clicked(self):  # 读取表格内容到文本
        self.ui.qPlainTextEdit.clear()
        rowCount = self.ui.qTableWidget.rowCount()
        colCount = self.ui.qTableWidget.columnCount()
        for i in range(rowCount):
            strText = "第 %d 行" % (i + 1)
            for j in range(colCount - 1):
                cellItem = self.ui.qTableWidget.item(i, j)
                strText = strText + cellItem.text() + " "
            cellItem = self.ui.qTableWidget.item(i, colCount - 1)
            if (cellItem.checkState() == Qt.Checked):
                strText = strText + "党员"
            else:
                strText = strText + "群众"
            self.ui.qPlainTextEdit.appendPlainText(strText)

    @pyqtSlot(bool)
    def on_qCheckBox1_clicked(self, checked):  # 表格可编辑
        if checked:
            trig = QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked
        else:
            trig = QAbstractItemView.NoEditTriggers
        self.ui.qTableWidget.setEditTriggers(trig)

    @pyqtSlot(bool)
    def on_qCheckBox2_clicked(self, checked):  # 间隔行底色
        self.ui.qTableWidget.setAlternatingRowColors(checked)

    @pyqtSlot(bool)
    def on_qCheckBox3_clicked(self, checked):  # 显示行表头
        self.ui.qTableWidget.horizontalHeader().setVisible(checked)

    @pyqtSlot(bool)
    def on_qCheckBox4_clicked(self, checked):  # 显示列表头
        self.ui.qTableWidget.verticalHeader().setVisible(checked)

    @pyqtSlot()
    def on_qRadioButton1_clicked(self):  # 行选择
        selMode = QAbstractItemView.SelectRows
        self.ui.qTableWidget.setSelectionBehavior(selMode)

    @pyqtSlot()
    def on_qRadioButton2_clicked(self):  # 单元格选择
        selMode = QAbstractItemView.SelectItems
        self.ui.qTableWidget.setSelectionBehavior(selMode)

    @pyqtSlot(int, int, int, int)
    def on_qTableWidget_currentCellChanged(self, currentRow, currentColumn, previousRow, previousColumn):
        if (self.__tableInitialized == False):
            return
        item = self.ui.qTableWidget.item(currentRow, currentColumn)
        if (item == None):
            return
        self.qLabel1.setText("当前单元格：%d行，%d列" % (currentRow, currentColumn))
        itemCellType = item.type()
        self.qLabel2.setText("当前单元格类型：%d" % itemCellType)

        item2 = self.ui.qTableWidget.item(currentRow, 0)
        studID = item2.data(Qt.UserRole)
        print(studID)
        self.qLabel3.setText("学生ID：%d" % studID)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )
