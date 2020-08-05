import sys, os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QItemSelectionModel, pyqtSlot, QStringListModel, pyqtSignal
from PyQt5.QtGui import QIcon, QStandardItemModel, QPixmap, QPainter
from PyQt5.QtWidgets import QAbstractItemView, QLabel, QMainWindow, QDialog, QWidget, QToolBar, QVBoxLayout, \
    QFileDialog, QFontDialog


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(827, 520)
        self.qWidget = QtWidgets.QWidget(qMainWindow)
        self.qMenuBar = QtWidgets.QMenuBar(qMainWindow)
        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        qMainWindow.setCentralWidget(self.qWidget)
        qMainWindow.setMenuBar(self.qMenuBar)
        qMainWindow.addToolBar(self.qToolBar)
        qMainWindow.setStatusBar(self.qStatusBar)

        self.qTabWidget = QtWidgets.QTabWidget(self.qWidget)
        self.qTabWidget.setGeometry(QRect(70, 30, 336, 196))
        self.qTabWidget.setTabsClosable(True)
        self.tab = QtWidgets.QWidget()
        self.qTabWidget.addTab(self.tab, "Page")
        self.qAction1 = QtWidgets.QAction(QIcon("../image/430.bmp"), "嵌入式Widget", self.qToolBar)
        self.qAction2 = QtWidgets.QAction(QIcon("../image/806.bmp"), "独立Widget窗口", self.qToolBar)
        self.qAction3 = QtWidgets.QAction(QIcon("../image/808.bmp"), "嵌入式MainWindow", self.qToolBar)
        self.qAction4 = QtWidgets.QAction(QIcon("../image/804.bmp"), "独立MainWindow窗口", self.qToolBar)
        self.qAction5 = QtWidgets.QAction(QIcon("../image/132.bmp"), "退出", self.qToolBar)
        self.qToolBar.addAction(self.qAction1)
        self.qToolBar.addAction(self.qAction2)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction3)
        self.qToolBar.addAction(self.qAction4)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction5)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.qAction1.setObjectName("qAction1")
        self.qAction2.setObjectName("qAction2")
        self.qAction3.setObjectName("qAction3")
        self.qAction4.setObjectName("qAction4")
        self.qAction5.setObjectName("qAction5")
        self.qTabWidget.setObjectName("qTabWidget")
        self.qAction5.triggered.connect(qMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)

class Ui_QWDialogHeaders(object):
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

class Ui_QWFormDoc():
    def setupUi(self, QWFormDoc):
        QWFormDoc.resize(628, 389)
        self.qPlainTextEdit = QtWidgets.QPlainTextEdit(QWFormDoc)
        self.qPlainTextEdit.setGeometry(QRect(75, 45, 256, 192))
        self.qAction1 = QtWidgets.QAction(QIcon("../image/122.bmp"), "打开", QWFormDoc)
        self.qAction2 = QtWidgets.QAction(QIcon("../image/200.bmp"), "剪切", QWFormDoc)
        self.qAction3 = QtWidgets.QAction(QIcon("../image/202.bmp"), "复制", QWFormDoc)
        self.qAction4 = QtWidgets.QAction(QIcon("../image/204.bmp"), "粘贴", QWFormDoc)
        self.qAction5 = QtWidgets.QAction(QIcon("../image/506.bmp"), "字体", QWFormDoc)
        self.qAction6 = QtWidgets.QAction(QIcon("../image/132.bmp"), "关闭", QWFormDoc)
        self.qAction7 = QtWidgets.QAction(QIcon("../image/206.bmp"), "撤销", QWFormDoc)
        self.qAction8 = QtWidgets.QAction(QIcon("../image/208.bmp"), "重复", QWFormDoc)

        self.qAction1.setObjectName("qAction1")
        self.qAction2.setObjectName("qAction2")
        self.qAction3.setObjectName("qAction3")
        self.qAction4.setObjectName("qAction4")
        self.qAction5.setObjectName("qAction5")
        self.qAction6.setObjectName("qAction6")
        self.qAction7.setObjectName("qAction7")
        self.qAction8.setObjectName("qAction8")

        self.qAction6.triggered.connect(QWFormDoc.close)
        self.qAction2.triggered.connect(self.qPlainTextEdit.cut)
        self.qAction3.triggered.connect(self.qPlainTextEdit.copy)
        self.qAction4.triggered.connect(self.qPlainTextEdit.paste)
        self.qAction7.triggered.connect(self.qPlainTextEdit.undo)
        self.qAction8.triggered.connect(self.qPlainTextEdit.redo)
        QtCore.QMetaObject.connectSlotsByName(QWFormDoc)


class Ui_QWFormTable(object):
    def setupUi(self, QWFormTable):
        QWFormTable.resize(555, 341)
        self.qWidget = QtWidgets.QWidget(QWFormTable)
        self.qToolBar = QtWidgets.QToolBar(QWFormTable)
        QWFormTable.setCentralWidget(self.qWidget)

        self.qAction1 = QtWidgets.QAction(QIcon("../image/230.bmp"), "设置表格大小", self.qToolBar)
        self.qAction2 = QtWidgets.QAction(QIcon("../image/516.bmp"), "设置表头", self.qToolBar)
        self.qAction3 = QtWidgets.QAction(QIcon("../image/132.bmp"), "关闭", self.qToolBar)
        self.qToolBar.addAction(self.qAction1)
        self.qToolBar.addAction(self.qAction2)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction3)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        QWFormTable.addToolBar(self.qToolBar)

        self.qTableView = QtWidgets.QTableView(self.qWidget)
        self.qTableView.setGeometry(QRect(35, 20, 256, 192))
        self.qTableView.setAlternatingRowColors(True)
        self.qTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.qTableView.verticalHeader().setDefaultSectionSize(25)

        self.qAction1.setObjectName("qAction1")
        self.qAction2.setObjectName("qAction2")
        self.qAction3.setObjectName("qAction3")
        self.qAction3.triggered.connect(QWFormTable.close)
        QtCore.QMetaObject.connectSlotsByName(QWFormTable)



class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.qTabWidget.setVisible(False)
        self.ui.qTabWidget.clear()
        self.ui.qTabWidget.setDocumentMode(True)
        self.setCentralWidget(self.ui.qTabWidget)
        self.setWindowState(Qt.WindowMaximized)
        self.setAutoFillBackground(True)
        self.__pic = QPixmap("../image/sea1.jpg")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, self.ui.qToolBar.height(), self.width(), self.height()-self.ui.qToolBar.height()-self.ui.qStatusBar.height(), self.__pic)
        super().paintEvent(event)

    @pyqtSlot()
    def on_qAction1_triggered(self):    # 嵌入式Widget
        formDoc = QmyFormDoc(self)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.docFileChanged.connect(self.do_docFileChanged)
        title = "Doc %d" %self.ui.qTabWidget.count()
        curIndex = self.ui.qTabWidget.addTab(formDoc, title)
        self.ui.qTabWidget.setCurrentIndex(curIndex)
        self.ui.qTabWidget.setVisible(True)

    @pyqtSlot(str)
    def do_docFileChanged(self, shortFilename):
        index = self.ui.qTabWidget.currentIndex()
        self.ui.qTabWidget.setTabText(index, shortFilename)

    @pyqtSlot()
    def on_qAction2_triggered(self):    # 独立Widget窗口
        formDoc = QmyFormDoc(self)
        formDoc.setAttribute(Qt.WA_DeleteOnClose)
        formDoc.setWindowTitle("基于QWidget的窗口，关闭时删除了")
        formDoc.setWindowFlag(Qt.Window, True)
        formDoc.setWindowOpacity(0.9)
        formDoc.show()

    @pyqtSlot()
    def on_qAction3_triggered(self):    # 嵌入式MainWindow
        formTable = QmyFormTable(self)
        formTable.setAttribute(Qt.WA_DeleteOnClose)
        title = "Table %d" %self.ui.qTabWidget.conut()
        curIndex = self.ui.qTabWidget.addTab(formTable, title)
        self.ui.qTabWidget.setCurrentIndex(curIndex)
        self.ui.qTabWidget.setVisible(True)

    @pyqtSlot()
    def on_qAction4_triggered(self):    # 独立MainWindow窗口
        formTable = QmyFormTable(self)
        formTable.setAttribute(Qt.WA_DeleteOnClose)
        formTable.setWindowTitle("基于QMainWindow的窗口，关闭时删除")
        formTable.show()

    def on_qTabWidget_currentChanged(self, index):
        hasTabs = self.ui.qTabWidget.count()>0
        self.ui.qTabWidget.setVisible(hasTabs)

    def on_qTabWidget_tabCloseReuqest(self, index):
        if(index<0):
            return
        aForm = self.ui.qTabWidget.widget(index)
        aForm.close()

class QmyDialogHeaders(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_QWDialogHeaders()
        self.ui.setupUi(self)
        self.__model = QStringListModel()
        self.ui.qListView.setModel(self.__model)

    def __del__(self):
        print("QmyDialogHeaders 对象被删除了")

    def setHeaderList(self, headerStrList):
        self.__model.setStringList(headerStrList)

    def headerList(self):
        return self.__model.stringList()

class QmyDialogLocate(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui=Ui_QWDialogLocate()
        self.ui.setupUi(self)


class QmyDialogSize(QDialog):
    def __init__(self, rowCount=3,colCount=5,parent=None):
        super().__init__(parent)
        self.ui=Ui_QWDialogSize()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.setIniSize(rowCount, colCount)

    def __del__(self):
        print("QmyDialogSize 对象被删除了")

    def setIniSize(self,rowCount,colCount):
        self.ui.qSpinBox1.setValue(colCount)
        self.ui.qSpinBox2.setValue(rowCount)

    def getTableSize(self):
        cols = self.ui.qSpinBox1.value()
        rows = self.ui.qSpinBox2.value()
        return rows, cols


class QmyFormDoc(QWidget):
    docFileChanged = pyqtSignal(str)

    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui=Ui_QWFormDoc()
        self.ui.setupUi(self)

        self.__curFile = ""
        locToolBar = QToolBar("文档", self)
        locToolBar.addAction(self.ui.qAction1)
        locToolBar.addAction(self.ui.qAction5)
        locToolBar.addSeparator()
        locToolBar.addAction(self.ui.qAction2)
        locToolBar.addAction(self.ui.qAction3)
        locToolBar.addAction(self.ui.qAction4)
        locToolBar.addAction(self.ui.qAction7)
        locToolBar.addAction(self.ui.qAction8)
        locToolBar.addSeparator()
        locToolBar.addAction(self.ui.qAction6)
        locToolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        Layout = QVBoxLayout()
        Layout.addWidget(locToolBar)
        Layout.addWidget(self.ui.qPlainTextEdit)
        Layout.setContentsMargins(2, 2, 2, 2)
        Layout.setSpacing(2)
        self.setLayout(Layout)
        self.setAutoFillBackground(True)

    def __del__(self):
        print("QmyFormDoc 对象被删除了")

    @pyqtSlot()
    def on_qAction1_triggered(self):
        curPath = os.getcwd()
        filename, flt = QFileDialog.getOpenFileName(self, "打开一个文件", curPath, "文本文件(*.cpp *.h *.py);;所有文件(*.*)")
        if(filename ==""):
            return
        self.__curFile = filename
        self.ui.qPlainTextEdit.clear()

        aFile = open(filename, 'r', encoding="utf-8")
        try:
            for eachLine in aFile:
                self.ui.qPlainTextEdit.appendPlainText(eachLine.strip())
        finally:
            aFile.close()

        baseFilename = os.path.basename((filename))
        self.setWindowTitle(baseFilename)
        self.docFileChanged.emit(baseFilename)

    @pyqtSlot()
    def on_qAction5_triggered(self):
        iniFont = self.ui.qPlainTextEdit.font()
        font, OK = QFontDialog.getFont(iniFont)
        if(OK):
            self.ui.qPlainTextEdit.setFont(font)


class QmyFormTable(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormTable()
        self.ui.setupUi(self)

        self.__dlgSetHeaders=None
        self.setAutoFillBackground(True)
        self.setCentralWidget(self.ui.qTableView)

        self.itemModel = QStandardItemModel(10, 5, self)
        self.selectionModel = QItemSelectionModel(self.itemModel)
        self.ui.qTableView.setModel(self.itemModel)
        self.ui.qTableView.setSelectionModel(self.selectionModel)

    def __del__(self):
        print("QmyFormTable 对象被删除了")

    @pyqtSlot()
    def on_qAction1_triggered(self):
        dlgTableSize = QmyDialogSize()
        dlgTableSize.setIniSize(self.itemModel.rowCount(), self.itemModel.columnCount())
        ret = dlgTableSize.exec()
        if(ret == QDialog.Accepted):
            rows, cols = dlgTableSize.getTableSize()
            self.itemModel.setRowCount(rows)
            self.itemModel.setColumnCount(cols)

    @pyqtSlot()
    def on_qAction2_triggered(self):
        if(self.__dlgSetHeaders == None):
            self.__dlgSetHeaders = QmyDialogHeaders(self)
        count = len(self.__dlgSetHeaders.headerList())
        if(count!=self.itemModel.columnCount()):
            strList=[]
            for i in range(self.itemModel.columnCount()):
                text = str(self.itemModel.headerData(i, Qt.Horizontal, Qt.DisplayRole))
                strList.append(text)
            self.__dlgSetHeaders.setHeaderList(strList)

        ret = self.__dlgSetHeaders.exec()
        if(ret == QDialog.Accepted):
            strList2 = self.__dlgSetHeaders.headerList()
            self.itemModel.setHorizontalHeaderLabels(strList2)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    # mw = QmyDialogHeaders()
    # mw = QmyDialogLocate()
    # mw = QmyDialogSize()
    # mw = QmyFormDoc()
    # mw = QmyFormTable()
    mw.show()
    sys.exit(app.exec_(), )