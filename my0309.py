'''
结构图：
qMainWindow
|--qWidget1
|   |--qScrollArea
|       |--qWidget2(qVBoxLayout1)
|           |--qLabel
|--qMenuBar
|   |--qMenu1
|   |   |--qAction1
|   |   |--qAction2
|   |   |--qAction3
|   |   |--qAction4
|   |   |--Separator
|   |   |--qAction5
|   |--qMenu2
|       |--qAction6
|       |--qAction7
|       |--qAction8
|       |--qAction9
|       |--qAction10
|--qToolBar
|   |--qAction1
|   |--qAction2
|   |--qAction3
|   |--qAction4
|   |--Separator
|   |--qAction6
|   |--qAction7
|   |--qAction8
|   |--qAction9
|   |--qAction10
|   |--Separator
|   |--qAction11
|   |--qAction12
|   |--Separator
|   |--qAction15
|--qStatusBar
|--qDockWidget
    |--qWidget3(qVBoxLayout2)
        |--qTreeWidget
            |--qTreeWidgetItem1
                |--qTreeWidgetItem2
                |   |--qTreeWidgetItem3
                |--qTreeWidgetItem4
                    |--qTreeWidgetItem5

问题：

总结：
1，注意qTreeWidget
（1）先设置列setColumnCount，headerItem即为表头
（2）然后根据树关系生成qTreeWidgetItem
（3）设置text的时候根据qTreeWidget.topLevelItem(n).child(n)
2，注意self.setCentralWidget(self.ui.qScrollArea)改变布局
3，添加图片功能好像有问题
4，代码分析


'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt, QSize, pyqtSlot, QDir, QFileInfo
from PyQt5.QtGui import QIcon, QCursor, QPixmap
from PyQt5.QtWidgets import QListView, QFileDialog


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(860, 506)
        self.qWidget1 = QtWidgets.QWidget(qMainWindow)
        self.qScrollArea = QtWidgets.QScrollArea(self.qWidget1)
        self.qScrollArea.setGeometry(QRect(20, 20, 541, 361))
        self.qScrollArea.setMinimumSize(QSize(200, 0))
        self.qScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.qScrollArea.setWidgetResizable(True)
        self.qScrollArea.setAlignment(Qt.AlignCenter)
        self.qWidget2 = QtWidgets.QWidget(self.qScrollArea)
        self.qWidget2.setGeometry(QRect(0, 0, 539, 359))
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(self.qWidget2)
        self.qLabel = QtWidgets.QLabel(self.qWidget2)
        self.qLabel.setAlignment(Qt.AlignCenter)
        self.qLabel.setText("待显示图片")
        self.qVBoxLayout1.addWidget(self.qLabel)
        self.qScrollArea.setWidget(self.qWidget2)
        qMainWindow.setCentralWidget(self.qWidget1)

        self.qMenuBar = QtWidgets.QMenuBar(qMainWindow)
        self.qMenuBar.setGeometry(QRect(0, 0, 860, 23))
        self.qMenu1 = QtWidgets.QMenu(self.qMenuBar)
        self.qMenu1.setTitle("目录树")
        self.qMenu2 = QtWidgets.QMenu(self.qMenuBar)
        self.qMenu2.setTitle("视图")
        self.qAction1 = QtWidgets.QAction(qMainWindow)
        self.qAction1.setText("添加目录")
        self.qAction1.setIcon(QIcon("./image/folder1.bmp"))
        self.qAction2 = QtWidgets.QAction(qMainWindow)
        self.qAction2.setText("添加文件")
        self.qAction2.setIcon(QIcon("./image/824.bmp"))
        self.qAction3 = QtWidgets.QAction(qMainWindow)
        self.qAction3.setText("删除节点")
        self.qAction3.setIcon(QIcon("./image/delete1.bmp"))
        self.qAction3.setEnabled(False)
        self.qAction4 = QtWidgets.QAction(qMainWindow)
        self.qAction4.setText("遍历节点")
        self.qAction4.setIcon(QIcon("./image/fold.bmp"))
        self.qAction5 = QtWidgets.QAction(qMainWindow)
        self.qAction5.setText("退出")
        self.qAction5.setIcon(QIcon("./image/exit.bmp"))
        self.qAction6 = QtWidgets.QAction(qMainWindow)
        self.qAction6.setText("放大")
        self.qAction6.setIcon(QIcon("./image/418.bmp"))
        self.qAction6.setEnabled(False)
        self.qAction7 = QtWidgets.QAction(qMainWindow)
        self.qAction7.setText("缩小")
        self.qAction7.setIcon(QIcon("./image/416.bmp"))
        self.qAction7.setEnabled(False)
        self.qAction8 = QtWidgets.QAction(qMainWindow)
        self.qAction8.setText("实际大小")
        self.qAction8.setIcon(QIcon("./image/414.bmp"))
        self.qAction8.setEnabled(False)
        self.qAction9 = QtWidgets.QAction(qMainWindow)
        self.qAction9.setText("适合宽度")
        self.qAction9.setIcon(QIcon("./image/424.bmp"))
        self.qAction9.setEnabled(False)
        self.qAction10 = QtWidgets.QAction(qMainWindow)
        self.qAction10.setText("适合高度")
        self.qAction10.setIcon(QIcon("./image/426.bmp"))
        self.qAction10.setEnabled(False)
        self.qMenu1.addAction(self.qAction1)
        self.qMenu1.addAction(self.qAction2)
        self.qMenu1.addAction(self.qAction3)
        self.qMenu1.addAction(self.qAction4)
        self.qMenu1.addSeparator()
        self.qMenu1.addAction(self.qAction5)
        self.qMenu2.addAction(self.qAction6)
        self.qMenu2.addAction(self.qAction7)
        self.qMenu2.addAction(self.qAction8)
        self.qMenu2.addAction(self.qAction9)
        self.qMenu2.addAction(self.qAction10)
        self.qMenuBar.addMenu(self.qMenu1)
        self.qMenuBar.addMenu(self.qMenu2)
        qMainWindow.setMenuBar(self.qMenuBar)

        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.qAction11 = QtWidgets.QAction(qMainWindow)
        self.qAction11.setText("窗体浮动")
        self.qAction11.setIcon(QIcon("./image/814.bmp"))
        self.qAction11.setCheckable(True)
        self.qAction11.setChecked(False)
        self.qAction12 = QtWidgets.QAction(qMainWindow)
        self.qAction12.setText("窗体可见")
        self.qAction12.setIcon(QIcon("./image/414.bmp"))
        self.qAction12.setCheckable(True)
        self.qAction12.setChecked(True)
        self.qToolBar.addAction(self.qAction1)
        self.qToolBar.addAction(self.qAction2)
        self.qToolBar.addAction(self.qAction3)
        self.qToolBar.addAction(self.qAction4)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction6)
        self.qToolBar.addAction(self.qAction7)
        self.qToolBar.addAction(self.qAction8)
        self.qToolBar.addAction(self.qAction9)
        self.qToolBar.addAction(self.qAction10)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction11)
        self.qToolBar.addAction(self.qAction12)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction5)
        qMainWindow.addToolBar(Qt.TopToolBarArea, self.qToolBar)

        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        qMainWindow.setStatusBar(self.qStatusBar)

        self.qDockWidget = QtWidgets.QDockWidget(qMainWindow)
        self.qDockWidget.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.qDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.qDockWidget.setWindowTitle("图片目录树")
        self.qWidget3 = QtWidgets.QWidget(self.qDockWidget)
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qWidget3)
        self.qTreeWidget = QtWidgets.QTreeWidget(self.qWidget3)
        self.qTreeWidget.setColumnCount(2)
        self.qTreeWidget.headerItem().setTextAlignment(0, Qt.AlignCenter)
        self.qTreeWidget.headerItem().setTextAlignment(1, Qt.AlignCenter)
        self.qTreeWidget.header().setDefaultSectionSize(150)
        self.qTreeWidget.headerItem().setText(0, "节点")
        self.qTreeWidget.headerItem().setText(1, "节点类型")
        qTreeWidgetItem1 = QtWidgets.QTreeWidgetItem(self.qTreeWidget)
        qTreeWidgetItem1.setIcon(0, QIcon("./image/15.ico"))
        qTreeWidgetItem2 = QtWidgets.QTreeWidgetItem(qTreeWidgetItem1)
        qTreeWidgetItem2.setIcon(0, QIcon("./image/open3.bmp"))
        qTreeWidgetItem3 = QtWidgets.QTreeWidgetItem(qTreeWidgetItem2)
        qTreeWidgetItem3.setIcon(0, QIcon("./image/31.ico"))
        qTreeWidgetItem3.setFlags(Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        qTreeWidgetItem4 = QtWidgets.QTreeWidgetItem(qTreeWidgetItem1)
        qTreeWidgetItem4.setIcon(0, QIcon("./image/open3.bmp"))
        qTreeWidgetItem5 = QtWidgets.QTreeWidgetItem(qTreeWidgetItem4)
        qTreeWidgetItem5.setIcon(0, QIcon("./image/31.ico"))
        self.qTreeWidget.topLevelItem(0).setText(0, "图片文件")
        self.qTreeWidget.topLevelItem(0).child(0).setText(0, "分组节点")
        self.qTreeWidget.topLevelItem(0).child(0).child(0).setText(0, "图片节点")
        self.qTreeWidget.topLevelItem(0).child(1).setText(0, "分组2")
        self.qTreeWidget.topLevelItem(0).child(1).child(0).setText(0, "图片2")
        self.qVBoxLayout2.addWidget(self.qTreeWidget)
        self.qDockWidget.setWidget(self.qWidget3)
        qMainWindow.addDockWidget(Qt.DockWidgetArea(1), self.qDockWidget)

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
        self.qAction12.setObjectName("qAction12")
        self.qTreeWidget.setObjectName("qTreeWidget")
        self.qDockWidget.setObjectName("qDockWidget")

        self.qAction5.triggered.connect(qMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.curPixmap = QPixmap()
        self.pixRatio = 1
        self.itemFlags = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsAutoTristate)
        self.setCentralWidget(self.ui.qScrollArea)

        self.ui.qTreeWidget.clear()
        item = QtWidgets.QTreeWidgetItem(1001)
        item.setIcon(0, QIcon("./image/15.ico"))
        item.setText(0, "图片文件")
        item.setFlags(self.itemFlags)
        item.setCheckState(0, Qt.Checked)
        item.setData(0, Qt.UserRole, "")
        self.ui.qTreeWidget.addTopLevelItem(item)

    @pyqtSlot()
    def on_qAction1_triggered(self):    # 添加目录
        dirStr = QFileDialog.getExistingDirectory()
        # if dirStr == "":
        #     return
        parItem = self.ui.qTreeWidget.currentItem()
        if parItem == None:
            parItem = self.ui.qTreeWidget.topLevelItem(0)

        dirObj = QDir(dirStr)
        nodeText = dirObj.dirName()

        item = QtWidgets.QTreeWidgetItem(1002)
        item.setIcon(0, QIcon("./image/open3.bmp"))
        item.setText(0, nodeText)
        item.setText(1, "Group")
        item.setFlags(self.itemFlags)
        item.setData(0, Qt.UserRole, dirStr)
        parItem.addChild(item)
        parItem.setExpanded(True)

    @pyqtSlot()
    def on_qAction2_triggered(self):    # 添加文件
        fileList, flt = QFileDialog.getOpenFileNames(self, "选择一个或多个文件", "", "Images(*.jpg)")
        if (len(fileList)<1):
            return
        item = self.ui.qTreeWidget.currentItem()
        if (item.type() == 1003):
            parItem = item.parent()
        else:
            parItem = item
        for i in range(len(fileList)):
            fullFileName = fileList[i]
            fileinfo = QFileInfo(fullFileName)
            nodeText = fileinfo.fileName()

            item = QtWidgets.QTreeWidgetItem(1003)
            item.setIcon(0, QIcon("./image/31.ico"))
            item.setText(0, nodeText)
            item.setText(1, "Image")
            item.setFlags(self.itemFlags)
            item.setCheckState(0, Qt.Checked)
            item.setData(0, Qt.UserRole, fullFileName)
            parItem.addChild(item)
        parItem.setExpanded(True)

    @pyqtSlot()
    def on_qAction3_triggered(self):    # 删除节点
        item = self.ui.qTreeWidget.currentItem()
        parItem = item.parent()
        parItem.removeChild(item)

    def __changeItemCaption(self, item):
        title = "*" + item.text(0)
        item.setText(0, title)
        if item.childCount() > 0:
            for i in range(item.childCount()):
                self.__changeItemCaption(item.child(i))

    def __displayImage(self, item):
        filename = item.data(0, Qt.UserRole)
        self.ui.qStatusBar.showMessage(filename)
        self.curPixmap.load(filename)
        self.on_qAction10_triggered()
        self.ui.qAction6.setEnabled(True)
        self.ui.qAction7.setEnabled(True)
        self.ui.qAction8.setEnabled(True)
        self.ui.qAction9.setEnabled(True)
        self.ui.qAction10.setEnabled(True)


    @pyqtSlot()
    def on_qAction4_triggered(self):    # 遍历节点
        count = self.ui.qTreeWidget.topLevelItemCount()
        for i in range(count):
            item = self.ui.qTreeWidget.topLevelItem(i)
            self.__changeItemCaption(item)

    def on_qTreeWidget_currentItemChanged(self, current, previous):
        if current == None:
            return
        nodeType = current.type()
        if nodeType == 1001:
            self.ui.qAction1.setEnabled(True)
            self.ui.qAction2.setEnabled(True)
            self.ui.qAction3.setEnabled(False)
        elif nodeType == 1002:
            self.ui.qAction1.setEnabled(True)
            self.ui.qAction2.setEnabled(True)
            self.ui.qAction3.setEnabled(True)
        elif nodeType == 1003:
            self.ui.qAction1.setEnabled(False)
            self.ui.qAction2.setEnabled(True)
            self.ui.qAction3.setEnabled(True)
            self.__displayImage(current)

    @pyqtSlot()
    def on_qAction10_triggered(self):   # 适合高度
        H = self.ui.qScrollArea.height()
        realH = self.curPixmap.height()
        self.pixRatio = float(H)/realH
        pix = self.curPixmap.scaledToHeight(H-30)
        self.ui.qLabel.setPixmap(pix)

    @pyqtSlot()
    def on_qAction9_triggered(self):    # 适合宽度
        W = self.ui.qScrollArea.width()-20
        realW = self.curPixmap.width()
        self.pixRatio = float(W)/realW
        pix = self.curPixmap.scaledToWidth(W-30)
        self.ui.qLabel.setPixmap(pix)

    @pyqtSlot()
    def on_qAction8_triggered(self):    # 实际大小
        self.pixRatio = 1
        self.ui.qLabel.setPixmap(self.curPixmap)

    @pyqtSlot()
    def on_qAction6_triggered(self):    # 放大
        self.pixRatio *= 1.2
        W = self.pixRatio * self.curPixmap.width()
        H = self.pixRatio * self.curPixmap.height()
        pix = self.curPixmap.scaled(W, H)
        self.ui.qLabel.setPixmap(pix)

    @pyqtSlot()
    def on_qAction7_triggered(self):    # 缩小
        self.pixRatio *= 0.8
        W = self.pixRatio * self.curPixmap.width()
        H = self.pixRatio * self.curPixmap.height()
        pix = self.curPixmap.scaled(W, H)
        self.ui.qLabel.setPixmap(pix)

    @pyqtSlot(bool)
    def on_qAction11_triggered(self, checked):  # 窗体浮动
        self.ui.qDockWidget.setFloating(checked)

    @pyqtSlot(bool)
    def on_qDockWidget_topLevelChanged(self, topLevel):
        self.ui.qAction11.setChecked(topLevel)

    @pyqtSlot(bool)
    def on_qAction12_triggered(self, checked):  # 窗口可见
        self.ui.qDockWidget.setVisible(checked)

    @pyqtSlot(bool)
    def on_qDockWidget_visibilityChanged(self, visible):
        self.ui.qAction12.setChecked(visible)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )
