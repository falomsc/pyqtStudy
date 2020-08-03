import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QItemSelectionModel, pyqtSlot, QStringListModel, pyqtSignal
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5.QtWidgets import QAbstractItemView, QLabel, QMainWindow, QDialog


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(567, 367)
        self.qWidget = QtWidgets.QWidget(qMainWindow)
        self.qMenuBar = QtWidgets.QMenuBar(qMainWindow)
        self.qMenuBar.setGeometry(QRect(0, 0, 567, 23))
        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        qMainWindow.setCentralWidget(self.qWidget)
        qMainWindow.setMenuBar(self.qMenuBar)
        qMainWindow.addToolBar(self.qToolBar)
        qMainWindow.setStatusBar(self.qStatusBar)

        self.qTableView = QtWidgets.QTableView(self.qWidget)
        self.qTableView.setGeometry(QRect(20, 15, 506, 236))
        self.qTableView.setAlternatingRowColors(True)
        self.qTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.qTableView.verticalHeader().setDefaultSectionSize(25)
        self.qAction1 = QtWidgets.QAction(self.qToolBar)
        self.qAction1.setText("设置行数列数")
        self.qAction1.setIcon(QIcon("../image/230.bmp"))
        self.qAction2 = QtWidgets.QAction(self.qToolBar)
        self.qAction2.setText("设置表头标题")
        self.qAction2.setIcon(QIcon("../image/516.bmp"))
        self.qAction3 = QtWidgets.QAction(self.qToolBar)
        self.qAction3.setText("定位单元格")
        self.qAction3.setIcon(QIcon("../image/132.bmp"))
        self.qAction4 = QtWidgets.QAction(self.qToolBar)
        self.qAction4.setText("退出")
        self.qAction4.setIcon(QIcon("../image/304.bmp"))
        self.qToolBar.addAction(self.qAction1)
        self.qToolBar.addAction(self.qAction2)
        self.qToolBar.addAction(self.qAction3)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction4)

        self.qAction1.setObjectName("qAction1")
        self.qAction2.setObjectName("qAction2")
        self.qAction3.setObjectName("qAction3")
        self.qAction4.setObjectName("qAction4")

        self.qAction4.triggered.connect(qMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)

class Ui_QWDialogHeaders():
    def setupUi(self, QWDialogHeaders):
        QWDialogHeaders.resize(289, 318)
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(QWDialogHeaders)
        self.qHBoxLayout = QtWidgets.QHBoxLayout(QWDialogHeaders)
        self.qVBoxLayout1.addLayout(self.qHBoxLayout)
        self.qGroupBox = QtWidgets.QGroupBox(QWDialogHeaders)
        self.qGroupBox.setTitle("表头标题")
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qGroupBox)
        self.qFrame = QtWidgets.QFrame(QWDialogHeaders)
        self.qVBoxLayout3 = QtWidgets.QVBoxLayout(self.qFrame)
        self.qHBoxLayout.addWidget(self.qGroupBox)
        self.qHBoxLayout.addWidget(self.qFrame)
        self.qListView = QtWidgets.QListView(self.qGroupBox)
        self.qPushButton1 = QtWidgets.QPushButton(self.qFrame)
        self.qPushButton1.setIcon(QIcon("../image/704.bmp"))
        self.qPushButton1.setText("确定")
        self.qPushButton2 = QtWidgets.QPushButton(self.qFrame)
        self.qPushButton2.setIcon(QIcon("../image/706.bmp"))
        self.qPushButton2.setText("取消")
        QSpacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        QSpacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        QSpacerItem3 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        QSpacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        QSpacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        QSpacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.qVBoxLayout2.addWidget(self.qListView)
        self.qVBoxLayout3.addSpacerItem(QSpacerItem1)
        self.qVBoxLayout3.addWidget(self.qPushButton1)
        self.qVBoxLayout3.addSpacerItem(QSpacerItem2)
        self.qVBoxLayout3.addWidget(self.qPushButton2)
        self.qVBoxLayout3.addSpacerItem(QSpacerItem3)
        self.qVBoxLayout3.addSpacerItem(QSpacerItem4)
        self.qVBoxLayout3.addSpacerItem(QSpacerItem5)
        self.qVBoxLayout3.addSpacerItem(QSpacerItem6)

        self.qPushButton1.setObjectName("qPushButton1")
        self.qPushButton2.setObjectName("qPushButton2")
        self.qPushButton1.clicked.connect(QWDialogHeaders.accept)
        self.qPushButton2.clicked.connect(QWDialogHeaders.reject)
        QtCore.QMetaObject.connectSlotsByName(QWDialogHeaders)

class Ui_QWDialogLocate():
    def setupUi(self, QWDialogLocate):
        QWDialogLocate.resize(313, 148)
        self.qHBoxLayout = QtWidgets.QHBoxLayout(QWDialogLocate)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(QWDialogLocate)
        self.qGroupBox = QtWidgets.QGroupBox(QWDialogLocate)
        self.qGridLayout = QtWidgets.QGridLayout(self.qGroupBox)
        self.qHBoxLayout.addWidget(self.qGroupBox)
        self.qHBoxLayout.addLayout(self.qVBoxLayout)

        self.qCheckBox1 = QtWidgets.QCheckBox(self.qGroupBox)
        self.qCheckBox1.setText("列增")
        self.qCheckBox2 = QtWidgets.QCheckBox(self.qGroupBox)
        self.qCheckBox2.setText("行增")
        self.qLabel1 = QtWidgets.QLabel(self.qGroupBox)
        self.qLabel1.setText("列号")
        self.qLabel2 = QtWidgets.QLabel(self.qGroupBox)
        self.qLabel2.setText("行号")
        self.qLabel3 = QtWidgets.QLabel(self.qGroupBox)
        self.qLabel3.setText("设定文字")
        self.qSpinBox1 = QtWidgets.QSpinBox(self.qGroupBox)
        self.qSpinBox2 = QtWidgets.QSpinBox(self.qGroupBox)
        self.qLineEdit = QtWidgets.QLineEdit(self.qGroupBox)
        self.qGridLayout.addWidget(self.qLabel1, 0, 0)
        self.qGridLayout.addWidget(self.qSpinBox1, 0, 1)
        self.qGridLayout.addWidget(self.qCheckBox1, 0, 2)
        self.qGridLayout.addWidget(self.qLabel2, 1, 0)
        self.qGridLayout.addWidget(self.qSpinBox2, 1, 1)
        self.qGridLayout.addWidget(self.qCheckBox2, 1, 2)
        self.qGridLayout.addWidget(self.qLabel3, 2, 0)
        self.qGridLayout.addWidget(self.qLineEdit, 2, 1, 1, 2)

        self.qPushButton1 = QtWidgets.QPushButton(QWDialogLocate)
        self.qPushButton1.setText("设定文字")
        self.qPushButton1.setIcon(QIcon("../image/322.bmp"))
        self.qPushButton2 = QtWidgets.QPushButton(QWDialogLocate)
        self.qPushButton2.setText("关闭")
        self.qPushButton2.setIcon(QIcon("../image/132.bmp"))
        self.qVBoxLayout.addWidget(self.qPushButton1)
        self.qVBoxLayout.addWidget(self.qPushButton2)

        self.qPushButton1.setObjectName("qPushButton1")
        self.qPushButton2.setObjectName("qPushButton2")

        self.qPushButton2.clicked.connect(QWDialogLocate.close)
        QtCore.QMetaObject.connectSlotsByName(QWDialogLocate)


class Ui_QWDialogSize():
    def setupUi(self, QWDialogSize):
        QWDialogSize.resize(266, 132)
        self.qHBoxLayout = QtWidgets.QHBoxLayout(QWDialogSize)
        self.qFrame = QtWidgets.QFrame(QWDialogSize)
        self.qGroupBox = QtWidgets.QGroupBox("设置表格行数和列数", QWDialogSize)
        self.qHBoxLayout.addWidget(self.qGroupBox)
        self.qHBoxLayout.addWidget(self.qFrame)

        self.qGridLayout = QtWidgets.QGridLayout(self.qGroupBox)
        self.qLabel1 = QtWidgets.QLabel("列数", self.qGroupBox)
        self.qLabel2 = QtWidgets.QLabel("行数", self.qGroupBox)
        self.qSpinBox1 = QtWidgets.QSpinBox(self.qGroupBox)
        self.qSpinBox2 = QtWidgets.QSpinBox(self.qGroupBox)
        self.qGridLayout.addWidget(self.qLabel1, 0, 0)
        self.qGridLayout.addWidget(self.qLabel2, 1, 0)
        self.qGridLayout.addWidget(self.qSpinBox1, 0, 1)
        self.qGridLayout.addWidget(self.qSpinBox2, 1, 1)

        self.qVBoxLayout = QtWidgets.QVBoxLayout(self.qFrame)
        self.qPushButton1 = QtWidgets.QPushButton(QIcon("../image/704.bmp"), "确定", self.qFrame)
        self.qPushButton2 = QtWidgets.QPushButton(QIcon("../image/706.bmp"), "取消", self.qFrame)
        self.qVBoxLayout.addWidget(self.qPushButton1)
        self.qVBoxLayout.addWidget(self.qPushButton2)

        self.qPushButton1.clicked.connect(QWDialogSize.accept)
        self.qPushButton2.clicked.connect(QWDialogSize.reject)
        QtCore.QMetaObject.connectSlotsByName(QWDialogSize)


class QmyMainWindow(QMainWindow):
    cellIndexChange = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__dlgSetHeaders = None
        self.setCentralWidget(self.ui.qTableView)
        self.qLabel1 = QLabel("当前单元格：", self)
        self.qLabel1.setMinimumWidth(180)
        self.ui.qStatusBar.addWidget(self.qLabel1)

        self.qLabel2 = QLabel("单元格内容：", self)
        self.qLabel2.setMinimumWidth(200)
        self.ui.qStatusBar.addWidget(self.qLabel2)

        self.itemModel = QStandardItemModel(10, 5, self)
        self.selectionModel = QItemSelectionModel(self.itemModel)
        self.selectionModel.currentChanged.connect(self.do_currentChanged)  # 显示状态栏信息

        self.ui.qTableView.setModel(self.itemModel)
        self.ui.qTableView.setSelectionModel(self.selectionModel)

    @pyqtSlot()
    def on_qAction1_triggered(self):    # 设置行数列数
        dlgTableSize = QmyDialogSize(self.itemModel.rowCount(), self.itemModel.columnCount())
        ret = dlgTableSize.exec()
        if(ret == QDialog.Accepted):
            rows, cols = dlgTableSize.getTableSize()
            self.itemModel.setRowCount(rows)
            self.itemModel.setColumnCount(cols)

    @pyqtSlot()
    def on_qAction2_triggered(self):    # 设置表头标题
        if (self.__dlgSetHeaders == None):
            self.__dlgSetHeaders = QmyDialogHeaders(self)

        count = len(self.__dlgSetHeaders.headerList())
        if(count != self.itemModel.columnCount()):  # 逻辑感人。首先表头标题不允许在表格内部直接改，因此如果发现标题与设置界面不一致，肯定是列数发生变化
            strList = []
            for i in range(self.itemModel.columnCount()):
                text = str(self.itemModel.headerData(i, Qt.Horizontal, Qt.DisplayRole))
                strList.append(text)
            self.__dlgSetHeaders.setHeaderList(strList)
        ret = self.__dlgSetHeaders.exec()
        if (ret == QDialog.Accepted):
            strList2 =self.__dlgSetHeaders.headerList()
            self.itemModel.setHorizontalHeaderLabels(strList2)

    @pyqtSlot()
    def on_qAction3_triggered(self):    # 定位单元格
        dlgLocate = QmyDialogLocate(self)
        dlgLocate.setSpinRange(self.itemModel.rowCount(), self.itemModel.columnCount())
        dlgLocate.changeActionEnable.connect(self.do_setActLocateEnable)
        dlgLocate.changeCellText.connect(self.do_setACellText)
        self.cellIndexChange.connect(dlgLocate.do_setSpinValue)
        dlgLocate.setAttribute(Qt.WA_DeleteOnClose)
        dlgLocate.show()

    def do_setActLocateEnable(self, enable):
        self.ui.qAction3.setEnabled(enable)

    def do_setACellText(self, row, column, text):
        index = self.itemModel.index(row, column)
        self.selectionModel.clearSelection()
        self.selectionModel.setCurrentIndex(index, QItemSelectionModel.Select)
        self.itemModel.setData(index, text, Qt.DisplayRole)

    def do_currentChanged(self, current, previous):
        if(current != None):
            self.qLabel1.setText("当前单元格：%d行，%d列" % (current.row(), current.column()))
            item = self.itemModel.itemFromIndex(current)
            self.qLabel2.setText("单元格内容："+item.text())
            self.cellIndexChange.emit(current.row(),current.column())


class QmyDialogHeaders(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_QWDialogHeaders()
        self.ui.setupUi(self)

        self.__model = QStringListModel()
        self.ui.qListView.setModel(self.__model)
        self.ui.qListView.setAlternatingRowColors(True)
        self.ui.qListView.setDragDropMode(QAbstractItemView.InternalMove)
        self.ui.qListView.setDefaultDropAction(Qt.MoveAction)

    def __del__(self):
        print("QmyDialogHeaders 对象被删除了")

    def setHeaderList(self, headerStrList):
        self.__model.setStringList(headerStrList)

    def headerList(self):
        return self.__model.stringList()

class QmyDialogLocate(QDialog):
    changeActionEnable = pyqtSignal(bool)   # 当定位单元格窗口出现时，不能再点击定位单元格按钮
    changeCellText = pyqtSignal(int, int, str)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui=Ui_QWDialogLocate()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def __del__(self):
        print("QmyDialogLocate 对象被删除了")

    def setSpinRange(self, rowCount, colCount):
        self.ui.qSpinBox1.setMaximum(colCount-1)
        self.ui.qSpinBox2.setMaximum(rowCount-1)

    def showEvent(self, event):
        self.changeActionEnable.emit(False)
        super().showEvent(event)

    def closeEvent(self, event):
        self.changeActionEnable.emit(True)
        super().closeEvent(event)

    @pyqtSlot()
    def on_qPushButton1_clicked(self):
        row = self.ui.qSpinBox2.value()
        col = self.ui.qSpinBox1.value()
        text = self.ui.qLineEdit.text()
        self.changeCellText.emit(row, col, text)
        if(self.ui.qCheckBox2.isChecked()):
            self.ui.qSpinBox2.setValue(1+self.ui.qSpinBox2.value())
        if(self.ui.qCheckBox1.isChecked()):
            self.ui.qSpinBox1.setValue(1+self.ui.qSpinBox2.value())

    @pyqtSlot(int, int)
    def do_setSpinValue(self, rowNo, colNo):
        self.ui.qSpinBox2.setValue(rowNo)
        self.ui.qSpinBox1.setValue(colNo)

class QmyDialogSize(QDialog):
    def __init__(self, rowCount=3,colCount=5,parent=None):
        super().__init__(parent)
        self.ui=Ui_QWDialogSize()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.ui.qSpinBox2.setValue(rowCount)
        self.ui.qSpinBox1.setValue(colCount)

    def __del__(self):
        print("QmyDialogSize 对象被删除了")

    def getTableSize(self):
        rows = self.ui.qSpinBox2.value()
        cols = self.ui.qSpinBox1.value()
        return rows, cols

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )