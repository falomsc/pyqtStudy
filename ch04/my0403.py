import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QRect, QItemSelectionModel
from PyQt5.QtGui import QIcon, QFont, QStandardItemModel
from PyQt5.QtWidgets import QAbstractItemView


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
        self.qTableView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
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

        self.qAction11.triggered.connect(qMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)



class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setCentralWidget(self.ui.qSplitter)
        self.__column = 6
        self.itemModel = QStandardItemModel(5, self.__column, self)
        self.selectionModel = QItemSelectionModel(self.itemModel)
        self.selectionModel.currentChanged.connect(self.do_curChanged)

        self.__lastColumnTitle = "测井取样"
        self.__lastColumnFlags = (Qt.ItemIsSelectable| Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)

        self.ui.qTableView.setModel(self.itemModel)
        self.ui.qTableView.setSelectionModel(self.selectionModel)

        oneOrMore = QAbstractItemView.ExtendedSelection
        self.ui.qTableView.setSelectionMode(oneOrMore)

        itemOrRow = QAbstractItemView.SelectItems
        self.ui.qTableView.setSelectionBehavior(itemOrRow)

        self.ui.qTableView.verticalHeader().setDefaultSectionSize(22)
        self.ui.qTableView.setAlternatingRowColors(True)

        self.ui.qTableView.setEnabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )