'''
结构图：
qMainWindow
|--qWidget1

'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRect, Qt, QSize, pyqtSlot, QDir, QFileInfo
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWidgets import QListView, QFileDialog, QFrame


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(837, 471)
        self.qWidget1 = QtWidgets.QWidget(qMainWindow)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(self.qWidget1)
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        self.qSplitter1 = QtWidgets.QSplitter(self.qWidget1)
        self.qSplitter1.setOrientation(Qt.Horizontal)
        self.qGroupBox = QtWidgets.QGroupBox(self.qSplitter1)
        self.qGroupBox.setMaximumSize(QSize(300,16777215))
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
        self.qCheckBox2 = QtWidgets.QCheckBox(self.qGroupBox)
        self.qCheckBox2.setText("间隔行底色")
        self.qCheckBox3 = QtWidgets.QCheckBox(self.qGroupBox)
        self.qCheckBox3.setText("显示行表头")
        self.qCheckBox4 = QtWidgets.QCheckBox(self.qGroupBox)
        self.qCheckBox4.setText("显示列表头")
        self.qRadioButton1 = QtWidgets.QRadioButton(self.qGroupBox)
        self.qRadioButton1.setText("行选择")
        self.qRadioButton2 = QtWidgets.QRadioButton(self.qGroupBox)
        self.qRadioButton2.setText("单元格选择")
        self.qSpinBox = QtWidgets.QSpinBox(self.qGroupBox)

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
        # item = QtWidgets.QTableWidgetItem()
        # self.qTableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.qTableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.qTableWidget.setHorizontalHeaderItem(2, item)






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
