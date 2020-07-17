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

'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt, QSize, pyqtSlot
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QListView


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
        self.qAction4 = QtWidgets.QAction(qMainWindow)
        self.qAction4.setText("遍历节点")
        self.qAction4.setIcon(QIcon("./image/fold.bmp"))
        self.qAction5 = QtWidgets.QAction(qMainWindow)
        self.qAction5.setText("退出")
        self.qAction5.setIcon(QIcon("./image/exit.bmp"))
        self.qAction6 = QtWidgets.QAction(qMainWindow)
        self.qAction6.setText("放大")
        self.qAction6.setIcon(QIcon("./image/418.bmp"))
        self.qAction7 = QtWidgets.QAction(qMainWindow)
        self.qAction7.setText("缩小")
        self.qAction7.setIcon(QIcon("./image/416.bmp"))
        self.qAction8 = QtWidgets.QAction(qMainWindow)
        self.qAction8.setText("实际大小")
        self.qAction8.setIcon(QIcon("./image/414.bmp"))
        self.qAction9 = QtWidgets.QAction(qMainWindow)
        self.qAction9.setText("适合宽度")
        self.qAction9.setIcon(QIcon("./image/424.bmp"))
        self.qAction10 = QtWidgets.QAction(qMainWindow)
        self.qAction10.setText("适合高度")
        self.qAction10.setIcon(QIcon("./image/426.bmp"))
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
        self.qAction12 = QtWidgets.QAction(qMainWindow)
        self.qAction12.setText("窗体可见")
        self.qAction12.setIcon(QIcon("./image/414.bmp"))
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


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )
