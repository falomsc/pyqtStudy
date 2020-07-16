'''
结构图：
qMainWindow
|--qWidget1
|   |--qSplitter
|       |--qToolBox
|       |   |--qWidget2(qGridLayout)
|       |   |   |--qToolButton1
|       |   |   |--qToolButton2
|       |   |   |--qToolButton3
|       |   |   |--qToolButton4
|       |   |   |--qToolButton5
|       |   |--qWidget3
|       |   |--qWidget4
|       |--qTabWidget
|           |--qWidget5(qVBoxLayout1)
|           |   |--qFrame(qVBoxLayout2)
|           |       |--qGroupBox1(qHBoxLayout1)
|           |       |   |--qLabel
|           |       |   |--qLineEdit
|           |       |   |--qCheckBox
|           |       |--qGroupBox2(qHBoxLayout2)
|           |       |   |--qToolButton6
|           |       |   |--qToolButton7
|           |       |   |--qToolButton8
|           |       |   |--qToolButton9
|           |       |--qListWidget
|           |           |--item
|           |           |--item
|           |--qWidget6
|           |--qWidget7
|--qToolBar
    |--qAction1
    |--qAction2
    |--qAction3
    |--qAction4
    |--qAction5
主程序中把CentralWidget改成了QSplitter

问题：
1，QFrame有什么用
2，删除命令必须加@pyqtSlot()，否则一次删除两个，具体原因未知
3，反选命令必须加@pyqtSlot()，否则无效，具体原因未知
4，增加和插入项必须加@pyqtSlot()，否则一次操作两次，具体原因未知
5，customContextMenuRequested(pos)中pos不知道是什么的位置坐标，鼠标坐标用QCursor.pos()

总结：
1，self.qWidget2.setGeometry(QRect(0, 0, 148, 299))这句话貌似没用
2，为QToolButton设置下拉菜单步骤：（1）setPopupMode（2）setToolButtonStyle（3）setMenu
3，貌似QToolButton可以加QAction，QPushButton不能加QAction
4，QListWidgetItem状态需要通过setFlags方法修改


'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt, QSize, pyqtSlot
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QListView


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(805, 512)
        self.qWidget1 = QtWidgets.QWidget(qMainWindow)
        self.qSplitter = QtWidgets.QSplitter(self.qWidget1)
        self.qSplitter.setGeometry(QRect(6, 6, 636, 391))
        self.qSplitter.setOrientation(Qt.Horizontal)

        self.qToolBox = QtWidgets.QToolBox(self.qSplitter)
        self.qToolBox.setMinimumSize(QSize(150, 0))
        self.qToolBox.setMaximumSize(QSize(220, 16777215))
        self.qToolBox.setFrameShape(QtWidgets.QFrame.Panel)
        self.qWidget2 = QtWidgets.QWidget(self.qToolBox)
        # self.qWidget2.setGeometry(QRect(0, 0, 148, 299))
        self.qToolBox.addItem(self.qWidget2,  QIcon("./image/408.bmp"), "QListWidget操作")
        self.qGridLayout = QtWidgets.QGridLayout(self.qWidget2)
        self.qToolButton1 = QtWidgets.QToolButton(self.qToolBox)
        self.qToolButton1.setMinimumSize(QSize(120, 25))
        self.qToolButton1.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.qToolButton1.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.qToolButton1.setText("btnList_Ini")
        self.qToolButton2 = QtWidgets.QToolButton(self.qToolBox)
        self.qToolButton2.setMinimumSize(QSize(120, 25))
        self.qToolButton2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.qToolButton2.setText("btnList_Clear")
        self.qToolButton3 = QtWidgets.QToolButton(self.qToolBox)
        self.qToolButton3.setMinimumSize(QSize(120, 25))
        self.qToolButton3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.qToolButton3.setText("btnList_Insert")
        self.qToolButton4 = QtWidgets.QToolButton(self.qToolBox)
        self.qToolButton4.setMinimumSize(QSize(120, 25))
        self.qToolButton4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.qToolButton4.setText("btnList_Append")
        self.qToolButton5 = QtWidgets.QToolButton(self.qToolBox)
        self.qToolButton5.setMinimumSize(QSize(120, 25))
        self.qToolButton5.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.qToolButton5.setText("btnList_Delete")
        self.qGridLayout.addWidget(self.qToolButton1, 0, 0, 1, 1)
        self.qGridLayout.addWidget(self.qToolButton2, 1, 0, 1, 1)
        self.qGridLayout.addWidget(self.qToolButton3, 2, 0, 1, 1)
        self.qGridLayout.addWidget(self.qToolButton4, 3, 0, 1, 1)
        self.qGridLayout.addWidget(self.qToolButton5, 4, 0, 1, 1)
        self.qWidget3 = QtWidgets.QWidget(self.qToolBox)
        self.qToolBox.addItem(self.qWidget3, QIcon("./image/410.bmp"), "QTreeWidget[空]")
        self.qWidget4 = QtWidgets.QWidget(self.qToolBox)
        self.qToolBox.addItem(self.qWidget4, QIcon("./image/412.bmp"), "QTableWidget[空]")

        self.qTabWidget = QtWidgets.QTabWidget(self.qSplitter)
        self.qTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.qTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.qTabWidget.setDocumentMode(True)
        self.qWidget5 = QtWidgets.QWidget(self.qTabWidget)
        self.qTabWidget.addTab(self.qWidget5, "QListWidget")
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(self.qWidget5)
        self.qFrame = QtWidgets.QFrame(self.qWidget5)
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qFrame)
        self.qVBoxLayout1.addWidget(self.qFrame)
        self.qGroupBox1 = QtWidgets.QGroupBox(self.qFrame)
        self.qHBoxLayout1 = QtWidgets.QHBoxLayout(self.qGroupBox1)
        self.qLabel = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel.setText("当前项变化")
        self.qLineEdit = QtWidgets.QLineEdit(self.qGroupBox1)
        self.qCheckBox = QtWidgets.QCheckBox(self.qGroupBox1)
        self.qCheckBox.setText("可编辑")
        self.qHBoxLayout1.addWidget(self.qLabel)
        self.qHBoxLayout1.addWidget(self.qLineEdit)
        self.qHBoxLayout1.addWidget(self.qCheckBox)
        self.qGroupBox2 = QtWidgets.QGroupBox(self.qFrame)
        self.qHBoxLayout2 = QtWidgets.QHBoxLayout(self.qGroupBox2)
        self.qToolButton6 = QtWidgets.QToolButton(self.qGroupBox2)
        self.qToolButton6.setMinimumSize(QSize(100,25))
        self.qToolButton6.setText("btnSelectItem")
        self.qToolButton6.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.qToolButton7 = QtWidgets.QToolButton(self.qGroupBox2)
        self.qToolButton7.setMinimumSize(QSize(70, 25))
        self.qToolButton7.setText("btnSel_ALL")
        self.qToolButton8 = QtWidgets.QToolButton(self.qGroupBox2)
        self.qToolButton8.setMinimumSize(QSize(70, 25))
        self.qToolButton8.setText("btnSel_None")
        self.qToolButton9 = QtWidgets.QToolButton(self.qGroupBox2)
        self.qToolButton9.setMinimumSize(QSize(70, 25))
        self.qToolButton9.setText("btnSel_Invs")
        self.qHBoxLayout2.addWidget(self.qToolButton6)
        self.qHBoxLayout2.addWidget(self.qToolButton7)
        self.qHBoxLayout2.addWidget(self.qToolButton8)
        self.qHBoxLayout2.addWidget(self.qToolButton9)
        self.qListWidget = QtWidgets.QListWidget(self.qFrame)
        self.qListWidget.setLayoutMode(QListView.SinglePass)
        self.qListWidget.setViewMode(QListView.ListMode)
        self.qListWidget.setSelectionRectVisible(False)
        self.qListWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.qListWidget.setSortingEnabled(False)
        item = QtWidgets.QListWidgetItem(self.qListWidget)
        item.setIcon(QIcon("./image/724.bmp"))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setText("New item")
        item.setCheckState(Qt.Checked)
        self.qListWidget.addItem(item)
        item = QtWidgets.QListWidgetItem(self.qListWidget)
        item.setIcon(QIcon("./image/724.bmp"))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setText("New item2")
        item.setCheckState(Qt.Unchecked)
        self.qListWidget.addItem(item)
        self.qVBoxLayout2.addWidget(self.qGroupBox1)
        self.qVBoxLayout2.addWidget(self.qGroupBox2)
        self.qVBoxLayout2.addWidget(self.qListWidget)
        self.qWidget6 = QtWidgets.QWidget(self.qTabWidget)
        self.qTabWidget.addTab(self.qWidget6, "QTreeWidget[空]")
        self.qWidget7 = QtWidgets.QWidget(self.qTabWidget)
        self.qTabWidget.addTab(self.qWidget7, "QTableWidget[空]")

        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.qAction1 = QtWidgets.QAction(qMainWindow)
        self.qAction1.setText("初始化列表")
        self.qAction1.setIcon(QIcon("./image/128.bmp"))
        self.qAction2 = QtWidgets.QAction(qMainWindow)
        self.qAction2.setText("清除列表")
        self.qAction2.setIcon(QIcon("./image/delete1.bmp"))
        self.qAction3 = QtWidgets.QAction(qMainWindow)
        self.qAction3.setText("插入项")
        self.qAction3.setIcon(QIcon("./image/424.bmp"))
        self.qAction4 = QtWidgets.QAction(qMainWindow)
        self.qAction4.setText("添加项")
        self.qAction4.setIcon(QIcon("./image/316.bmp"))
        self.qAction5 = QtWidgets.QAction(qMainWindow)
        self.qAction5.setText("删除当前项")
        self.qAction5.setIcon(QIcon("./image/324.bmp"))
        self.qToolBar.addAction(self.qAction1)
        self.qToolBar.addAction(self.qAction2)
        self.qToolBar.addAction(self.qAction3)
        self.qToolBar.addAction(self.qAction4)
        self.qToolBar.addAction(self.qAction5)

        qMainWindow.setCentralWidget(self.qWidget1)
        qMainWindow.addToolBar(self.qToolBar)
        self.qAction6 = QtWidgets.QAction(qMainWindow)
        self.qAction6.setText("项选择")
        self.qAction6.setIcon(QIcon("./image/124.bmp"))
        self.qAction7 = QtWidgets.QAction(qMainWindow)
        self.qAction7.setText("全选")
        self.qAction8 = QtWidgets.QAction(qMainWindow)
        self.qAction8.setText("全不选")
        self.qAction9 = QtWidgets.QAction(qMainWindow)
        self.qAction9.setText("反选")
        self.qAction10 = QtWidgets.QAction(qMainWindow)
        self.qAction10.setText("退出")
        self.qAction10.setIcon(QIcon("./image/132.bmp"))

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
        self.qListWidget.setObjectName("qListWidget")
        self.qToolButton1.setObjectName("qToolButton1")
        self.qToolButton2.setObjectName("qToolButton2")
        self.qToolButton3.setObjectName("qToolButton3")
        self.qToolButton4.setObjectName("qToolButton4")
        self.qToolButton5.setObjectName("qToolButton5")
        self.qToolButton6.setObjectName("qToolButton6")
        self.qToolButton7.setObjectName("qToolButton7")
        self.qToolButton8.setObjectName("qToolButton8")
        self.qToolButton9.setObjectName("qToolButton9")
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)

        self.qAction10.triggered.connect(qMainWindow.close)
        self.qAction6.triggered.connect(self.qAction9.trigger)


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setCentralWidget(self.ui.qSplitter)
        self.ui.qToolButton1.setDefaultAction(self.ui.qAction1)
        self.ui.qToolButton2.setDefaultAction(self.ui.qAction2)
        self.ui.qToolButton3.setDefaultAction(self.ui.qAction3)
        self.ui.qToolButton4.setDefaultAction(self.ui.qAction4)
        self.ui.qToolButton5.setDefaultAction(self.ui.qAction5)
        self.ui.qToolButton7.setDefaultAction(self.ui.qAction7)
        self.ui.qToolButton8.setDefaultAction(self.ui.qAction8)
        self.ui.qToolButton9.setDefaultAction(self.ui.qAction9)

        qMenu = QtWidgets.QMenu(self)
        qMenu.addAction(self.ui.qAction6)
        qMenu.addAction(self.ui.qAction7)
        qMenu.addAction(self.ui.qAction8)
        self.ui.qToolButton6.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ui.qToolButton6.setDefaultAction(self.ui.qAction6)
        self.ui.qToolButton6.setMenu(qMenu)

        qToolButton = QtWidgets.QToolButton(self)
        qToolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        qToolButton.setDefaultAction(self.ui.qAction6)
        qToolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        qToolButton.setMenu(qMenu)
        self.ui.qToolBar.addWidget(qToolButton)
        self.ui.qToolBar.addSeparator()
        self.ui.qToolBar.addAction(self.ui.qAction10)

        self.__FlagEditable = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
        self.__FlagNotEditable = (Qt.ItemIsSelectable | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled )

    def on_qAction1_triggered(self):    # 初始化列表
        icon = QIcon("./image/724.bmp")
        editable = self.ui.qCheckBox.isChecked()
        if editable:
            Flag = self.__FlagEditable
        else:
            Flag = self.__FlagNotEditable
        self.ui.qListWidget.clear()
        for i in range(10):
            itemStr = "item %d" % i
            aItem = QtWidgets.QListWidgetItem()
            aItem.setText(itemStr)
            aItem.setIcon(icon)
            aItem.setCheckState(Qt.Checked)
            aItem.setFlags(Flag)
            self.ui.qListWidget.addItem(aItem)

    @pyqtSlot()
    def on_qAction5_triggered(self):    # 删除当前项目
        row = self.ui.qListWidget.currentRow()
        self.ui.qListWidget.takeItem(row)

    def on_qAction2_triggered(self):    # 清除列表
        self.ui.qListWidget.clear()

    @pyqtSlot()
    def on_qAction3_triggered(self):    # 插入项
        icon = QIcon("./image/724.bmp")
        editable = self.ui.qCheckBox.isChecked()
        if editable:
            Flag = self.__FlagEditable
        else:
            Flag = self.__FlagNotEditable
        aItem = QtWidgets.QListWidgetItem()
        aItem.setIcon(icon)
        aItem.setCheckState(Qt.Checked)
        aItem.setFlags(Flag)
        aItem.setText("Inserted Item")
        curRow = self.ui.qListWidget.currentRow()
        self.ui.qListWidget.insertItem(curRow, aItem)

    @pyqtSlot()
    def on_qAction4_triggered(self):    # 添加项
        icon = QIcon("./image/724.bmp")
        editable = self.ui.qCheckBox.isChecked()
        if editable:
            Flag = self.__FlagEditable
        else:
            Flag = self.__FlagNotEditable
        aItem = QtWidgets.QListWidgetItem()
        aItem.setIcon(icon)
        aItem.setCheckState(Qt.Checked)
        aItem.setFlags(Flag)
        aItem.setText("Appended Item")
        self.ui.qListWidget.addItem(aItem)

    def on_qAction7_triggered(self):    # 全选
        for i in range(self.ui.qListWidget.count()):
            qListWidgetItem = self.ui.qListWidget.item(i)
            qListWidgetItem.setCheckState(Qt.Checked)

    def on_qAction8_triggered(self):    # 全不选
        for i in range(self.ui.qListWidget.count()):
            qListWidgetItem = self.ui.qListWidget.item(i)
            qListWidgetItem.setCheckState(Qt.Unchecked)

    @pyqtSlot()
    def on_qAction9_triggered(self):    # 反选
        for i in range(self.ui.qListWidget.count()):
            qListWidgetItem = self.ui.qListWidget.item(i)
            if(qListWidgetItem.checkState() == Qt.Checked):
                qListWidgetItem.setCheckState(Qt.Unchecked)
            else:
                qListWidgetItem.setCheckState(Qt.Checked)

    @pyqtSlot(bool)
    def on_qCheckBox_clicked(self, checked):    # 可编辑
        if checked:
            Flag = self.__FlagEditable
        else:
            Flag = self.__FlagNotEditable
        for i in range(self.ui.qListWidget.count()):
            qListWidgetItem = self.ui.qListWidget.item(i)
            qListWidgetItem.setFlags(Flag)

    def on_qListWidget_currentItemChanged(self, current, previous): # 显示框
        strInfo = ""
        if(current != None):
            if(previous==None):
                strInfo = "当前："+current.text()
            else:
                strInfo = "前一项："+previous.text()+"；当前项：" + current.text()
        self.ui.qLineEdit.setText(strInfo)

    def on_qListWidget_customContextMenuRequested(self, pos):
        menu = QtWidgets.QMenu()
        menu.addAction(self.ui.qAction1)
        menu.addAction(self.ui.qAction2)
        menu.addAction(self.ui.qAction3)
        menu.addAction(self.ui.qAction4)
        menu.addAction(self.ui.qAction5)
        menu.addSeparator()
        menu.addAction(self.ui.qAction7)
        menu.addAction(self.ui.qAction8)
        menu.addAction(self.ui.qAction9)
        menu.exec_(QCursor.pos())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )