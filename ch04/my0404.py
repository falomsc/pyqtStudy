import os
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QRect, QItemSelectionModel, pyqtSlot
from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QAbstractItemView, QLabel, QFileDialog, QStyledItemDelegate, QDoubleSpinBox, QComboBox


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(753, 400)
        font = QFont()
        font.setPointSize(10)
        qMainWindow.setFont(font)
        self.qWidget = QtWidgets.QWidget(qMainWindow)
        self.qMenuBar = QtWidgets.QMenuBar(qMainWindow)
        self.qMenuBar.setGeometry(QRect(0, 0, 753, 23))
        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        qMainWindow.setCentralWidget(self.qWidget)

        self.qSplitter = QtWidgets.QSplitter(self.qWidget)
        self.qSplitter.setOrientation(Qt.Horizontal)
        self.qSplitter.setGeometry(QRect(100, 40, 532, 261))
        self.qGroupBox1 = QtWidgets.QGroupBox(self.qSplitter)
        self.qGroupBox1.setTitle("tableView")
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(self.qGroupBox1)
        self.qGroupBox2 = QtWidgets.QGroupBox(self.qSplitter)
        self.qGroupBox2.setTitle("plainTextEdit")
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qGroupBox2)
        self.qTableView = QtWidgets.QTableView(self.qGroupBox1)
        self.qTableView.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.qPlainTextEdit = QtWidgets.QPlainTextEdit(self.qGroupBox2)
        self.qVBoxLayout1.addWidget(self.qTableView)
        self.qVBoxLayout2.addWidget(self.qPlainTextEdit)

        self.qAction1 = QtWidgets.QAction(self.qToolBar)
        self.qAction1.setIcon(QIcon("../image/122.bmp"))
        self.qAction1.setText("打开文件")
        self.qAction2 = QtWidgets.QAction(self.qToolBar)
        self.qAction2.setEnabled(False)
        self.qAction2.setIcon(QIcon("../image/104.bmp"))
        self.qAction2.setText("另存文件")
        self.qAction3 = QtWidgets.QAction(self.qToolBar)
        self.qAction3.setEnabled(False)
        self.qAction3.setIcon(QIcon("../image/export1.bmp"))
        self.qAction3.setText("模型数据")
        self.qAction4 = QtWidgets.QAction(self.qToolBar)
        self.qAction4.setEnabled(False)
        self.qAction4.setIcon(QIcon("../image/append.bmp"))
        self.qAction4.setText("添加行")
        self.qAction5 = QtWidgets.QAction(self.qToolBar)
        self.qAction5.setEnabled(False)
        self.qAction5.setIcon(QIcon("../image/306.bmp"))
        self.qAction5.setText("插入行")
        self.qAction6 = QtWidgets.QAction(self.qToolBar)
        self.qAction6.setEnabled(False)
        self.qAction6.setIcon(QIcon("../image/delete.bmp"))
        self.qAction6.setText("删除行")
        self.qAction7 = QtWidgets.QAction(self.qToolBar)
        self.qAction7.setIcon(QIcon("../image/508.bmp"))
        self.qAction7.setText("居左")
        self.qAction8 = QtWidgets.QAction(self.qToolBar)
        self.qAction8.setIcon(QIcon("../image/510.bmp"))
        self.qAction8.setText("居中")
        self.qAction9 = QtWidgets.QAction(self.qToolBar)
        self.qAction9.setIcon(QIcon("../image/512.bmp"))
        self.qAction9.setText("居右")
        self.qAction10 = QtWidgets.QAction(self.qToolBar)
        self.qAction10.setIcon(QIcon("../image/500.bmp"))
        self.qAction10.setCheckable(True)
        self.qAction10.setText("粗体")
        self.qAction11 = QtWidgets.QAction(self.qToolBar)
        self.qAction11.setIcon(QIcon("../image/exit.bmp"))
        self.qAction11.setText("退出")
        self.qToolBar.addAction(self.qAction1)
        self.qToolBar.addAction(self.qAction2)
        self.qToolBar.addAction(self.qAction3)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction4)
        self.qToolBar.addAction(self.qAction5)
        self.qToolBar.addAction(self.qAction6)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction7)
        self.qToolBar.addAction(self.qAction8)
        self.qToolBar.addAction(self.qAction9)
        self.qToolBar.addAction(self.qAction10)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction11)
        qMainWindow.addToolBar(Qt.TopToolBarArea, self.qToolBar)
        qMainWindow.setMenuBar(self.qMenuBar)
        qMainWindow.setStatusBar(self.qStatusBar)

        self.qAction1.setObjectName("qAction1")
        self.qAction2.setObjectName("qAction2")
        self.qAction3.setObjectName("qAction3")
        self.qAction4.setObjectName("qAction4")
        self.qAction5.setObjectName("qAction5")
        self.qAction6.setObjectName("qAction6")
        self.qAction7.setObjectName("qAction7")
        self.qAction8.setObjectName("qAction8")
        self.qAction9.setObjectName("qAction9")
        self.qAction10.setObjectName("qAction10")
        self.qAction11.setObjectName("qAction11")

        self.qAction11.triggered.connect(qMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setCentralWidget(self.ui.qSplitter)
        self.__ColCount = 6
        self.itemModel = QStandardItemModel(5, self.__ColCount, self)
        self.selectionModel = QItemSelectionModel(self.itemModel)
        self.selectionModel.currentChanged.connect(self.do_curChanged)

        self.__lastColumnTitle = "测井取样"
        self.__lastColumnFlags = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

        self.ui.qTableView.setModel(self.itemModel)
        self.ui.qTableView.setSelectionModel(self.selectionModel)

        oneOrMore = QAbstractItemView.ExtendedSelection
        self.ui.qTableView.setSelectionMode(oneOrMore)

        itemOrRow = QAbstractItemView.SelectItems
        self.ui.qTableView.setSelectionBehavior(itemOrRow)

        self.ui.qTableView.verticalHeader().setDefaultSectionSize(22)
        self.ui.qTableView.setAlternatingRowColors(True)

        self.ui.qTableView.setEnabled(False)

        self.qLabel1 = QLabel("当前单元格：", self)
        self.qLabel1.setMinimumWidth(180)
        self.qLabel2 = QLabel("单元格内容：", self)
        self.qLabel2.setMinimumWidth(150)
        self.qLabel3 = QLabel("当前文件：", self)
        self.ui.qStatusBar.addWidget(self.qLabel1)
        self.ui.qStatusBar.addWidget(self.qLabel2)
        self.ui.qStatusBar.addPermanentWidget(self.qLabel3)

        self.spinCeshen = QmyFloatSpinDelegate(0, 10000, 0, self)
        self.spinLength = QmyFloatSpinDelegate(0, 6000, 2, self)
        self.spinDegree = QmyFloatSpinDelegate(0, 360, 1, self)

        self.ui.qTableView.setItemDelegateForColumn(0, self.spinCeshen)
        self.ui.qTableView.setItemDelegateForColumn(1, self.spinLength)
        self.ui.qTableView.setItemDelegateForColumn(3, self.spinLength)
        self.ui.qTableView.setItemDelegateForColumn(2, self.spinDegree)

        qualities = ["优", "良", "合格", "不合格"]
        self.comboDelegate = QmyComboBoxDelegate(self)
        self.comboDelegate.setItems(qualities, False)
        self.ui.qTableView.setItemDelegateForColumn(4, self.comboDelegate)

    def __iniModelFromStringList(self, allLines):
        rowCnt = len(allLines)
        self.itemModel.setRowCount(rowCnt - 1)
        headerText = allLines[0].strip()
        headerList = headerText.split("\t")
        self.itemModel.setHorizontalHeaderLabels(headerList)
        self.__lastColumnTitle = headerList[len(headerList) - 1]
        lastColNo = self.__ColCount - 1
        for i in range(rowCnt - 1):
            lineText = allLines[i + 1].strip()
            strList = lineText.split("\t")
            for j in range(self.__ColCount - 1):
                item = QStandardItem(strList[j])
                self.itemModel.setItem(i, j, item)

            item = QStandardItem(self.__lastColumnTitle)
            item.setFlags(self.__lastColumnFlags)
            item.setCheckable(True)
            if (strList[lastColNo] == "0"):
                item.setCheckState(Qt.Unchecked)
            else:
                item.setCheckState(Qt.Checked)
            self.itemModel.setItem(i, lastColNo, item)

    def __setCellAlignment(self, align=Qt.AlignHCenter):
        if (not self.selectionModel.hasSelection()):
            return
        selectedIndex = self.selectionModel.selectedIndexes()
        count = len(selectedIndex)
        for i in range(count):
            index = selectedIndex[i]
            item = self.itemModel.itemFromIndex(index)
            item.setTextAlignment(align)

    @pyqtSlot()
    def on_qAction1_triggered(self):  # 打开文件
        curPath = os.getcwd()
        filename, flt = QFileDialog.getOpenFileName(self, "打开一个文件", curPath, "井斜数据文件(*.txt);;所有文件(*.*)")
        if (filename == ""):
            return
        self.qLabel3.setText("当前文件：" + filename)
        self.ui.qPlainTextEdit.clear()
        aFile = open(filename, 'r')
        allLines = aFile.readlines()
        aFile.close()

        for strLine in allLines:
            self.ui.qPlainTextEdit.appendPlainText(strLine.strip())

        self.__iniModelFromStringList(allLines)
        self.ui.qTableView.setEnabled(True)
        self.ui.qAction2.setEnabled(True)
        self.ui.qAction3.setEnabled(True)
        self.ui.qAction4.setEnabled(True)
        self.ui.qAction5.setEnabled(True)
        self.ui.qAction6.setEnabled(True)

    @pyqtSlot()
    def on_qAction2_triggered(self):  # 另存文件
        curPath = os.getcwd()
        filename, flt = QFileDialog.getSaveFileName(self, "保存文件", curPath, "井斜数据文件(*.txt);;所有文件(*.*)")
        if (filename == ""):
            return
        self.on_qAction3_triggered()
        aFile = open(filename, "w")
        aFile.write(self.ui.qPlainTextEdit.toPlainText())
        aFile.close()

    @pyqtSlot()
    def on_qAction4_triggered(self):  # 添加行
        itemList = []
        for i in range(self.__ColCount - 1):
            item = QStandardItem("0")
            itemList.append(item)

        item = QStandardItem(self.__lastColumnTitle)
        item.setCheckable(True)
        item.setFlags(self.__lastColumnFlags)
        itemList.append(item)

        self.itemModel.appendRow(itemList)
        curIndex = self.itemModel.index(self.itemModel.rowCount() - 1, 0)
        self.selectionModel.clearSelection()
        self.selectionModel.setCurrentIndex(curIndex, QItemSelectionModel.Select)

    @pyqtSlot()
    def on_qAction5_triggered(self):  # 插入行
        itemlist = []
        for i in range(self.__ColCount - 1):
            item = QStandardItem("0")
            itemlist.append(item)

        item = QStandardItem(self.__lastColumnTitle)
        item.setFlags(self.__lastColumnFlags)
        item.setCheckable(True)
        item.setCheckState(Qt.Checked)
        itemlist.append(item)

        curIndex = self.selectionModel.currentIndex()
        self.itemModel.insertRow(curIndex.row(), itemlist)
        self.selectionModel.clearSelection()
        self.selectionModel.setCurrentIndex(curIndex, QItemSelectionModel.Select)

    @pyqtSlot()
    def on_qAction6_triggered(self):  # 删除行
        curIndex = self.selectionModel.currentIndex()
        self.itemModel.removeRow(curIndex.row())

    @pyqtSlot()
    def on_qAction7_triggered(self):  # 居左
        self.__setCellAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    @pyqtSlot()
    def on_qAction8_triggered(self):  # 居中
        self.__setCellAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    @pyqtSlot()
    def on_qAction9_triggered(self):  # 居右
        self.__setCellAlignment(Qt.AlignRight | Qt.AlignVCenter)

    @pyqtSlot(bool)
    def on_qAction10_triggered(self, checked):  # 粗体
        if (not self.selectionModel.hasSelection()):
            return
        selectedIndex = self.selectionModel.selectedIndexes()
        count = len(selectedIndex)
        for i in range(count):
            index = selectedIndex[i]
            item = self.itemModel.itemFromIndex(index)
            font = item.font()
            font.setBold(checked)
            item.setFont(font)

    @pyqtSlot()
    def on_qAction3_triggered(self):  # 模型数据
        self.ui.qPlainTextEdit.clear()
        lineStr = ""
        for i in range(self.itemModel.columnCount() - 1):
            item = self.itemModel.horizontalHeaderItem(i)
            lineStr = lineStr + item.text() + "\t"
        item = self.itemModel.horizontalHeaderItem(self.__ColCount - 1)
        lineStr = lineStr + item.text()
        self.ui.qPlainTextEdit.appendPlainText(lineStr)

        for i in range(self.itemModel.rowCount()):
            lineStr = ""
            for j in range(self.itemModel.columnCount() - 1):
                item = self.itemModel.item(i, j)
                lineStr = lineStr + item.text() + "\t"
            item = self.itemModel.item(i, self.__ColCount - 1)
            if (item.checkState() == Qt.Checked):
                lineStr = lineStr + "1"
            else:
                lineStr = lineStr + "0"
            self.ui.qPlainTextEdit.appendPlainText(lineStr)

    def do_curChanged(self, current, previous):
        if (current != None):
            text = "当前单元格：%d行，%d列" % (current.row(), current.column())
            self.qLabel1.setText(text)
            item = self.itemModel.itemFromIndex(current)
            self.qLabel2.setText("单元格内容：" + item.text())
            font = item.font()
            self.ui.qAction10.setChecked(font.bold())


class QmyFloatSpinDelegate(QStyledItemDelegate):
    def __init__(self, minV=0, maxV=1000, digi=2, parent=None):
        super().__init__(parent)
        self.__min = minV
        self.__max = maxV
        self.__decimals = digi

    def createEditor(self, parent, option, index):
        editor = QDoubleSpinBox(parent)
        editor.setFrame(False)
        editor.setRange(self.__min, self.__max)
        editor.setDecimals(self.__decimals)
        return editor

    def setEditorData(self, editor, index):
        model = index.model()
        text = model.data(index, Qt.EditRole)
        editor.setValue(float(text))

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class QmyComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__itemList = []
        self.__isEditable = False

    def setItems(self, itemList, isEditable=False):
        self.__itemList = itemList
        self.__isEditable = isEditable

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setFrame = False
        editor.setEditable(self.__isEditable)
        editor.addItems(self.__itemList)
        return editor

    def setEditorData(self, editor, index):
        model = index.model()
        text = model.data(index, Qt.EditRole)
        editor.setCurrentText(text)

    def setModelData(self, editor, model, index):
        text = editor.currentText()
        model.setData(index, text, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )
