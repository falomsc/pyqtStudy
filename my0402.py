'''
目前问题：

总结：
1，注意数据结构
（1）QListView.setModel(QStringListModel)
（2）针对QStringListModel进行操作，比如insertRow、removeRow、setData

'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QSize, QStringListModel, pyqtSlot
from PyQt5.QtWidgets import QAbstractItemView


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(549, 348)
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(qWidget)
        self.qGroupBox1 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox1.setMaximumSize(QSize(16777215, 40))
        self.qHBoxLayout = QtWidgets.QHBoxLayout(self.qGroupBox1)
        self.qSplitter = QtWidgets.QSplitter(qWidget)
        self.qSplitter.setOrientation(Qt.Horizontal)
        self.qVBoxLayout1.addWidget(self.qSplitter)
        self.qVBoxLayout1.addWidget(self.qGroupBox1)

        self.qGroupBox2 = QtWidgets.QGroupBox(self.qSplitter)
        self.qGroupBox2.setTitle("QListView")
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qGroupBox2)
        self.qGroupBox3 = QtWidgets.QGroupBox(self.qSplitter)
        self.qGroupBox3.setTitle("QPlainTextEdit")
        self.qVBoxLayout3 = QtWidgets.QVBoxLayout(self.qGroupBox3)
        self.qGridLayout = QtWidgets.QGridLayout(self.qGroupBox2)
        self.qPushButton1 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton1.setText("恢复列表")
        self.qPushButton2 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton2.setText("添加项")
        self.qPushButton3 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton3.setText("插入项")
        self.qPushButton4 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton4.setText("删除当前项")
        self.qPushButton5 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton5.setText("清空列表")
        self.qGridLayout.addWidget(self.qPushButton1, 0, 0, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton2, 1, 0, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton3, 1, 1, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton4, 2, 0, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton5, 2, 1, 1, 1)
        self.qListView = QtWidgets.QListView(self.qGroupBox2)
        self.qVBoxLayout2.addLayout(self.qGridLayout)
        self.qVBoxLayout2.addWidget(self.qListView)

        self.qVBoxLayout4 = QtWidgets.QVBoxLayout(self.qGroupBox3)
        self.qPushButton6 = QtWidgets.QPushButton(self.qGroupBox3)
        self.qPushButton6.setText("清空文本")
        self.qPushButton7 = QtWidgets.QPushButton(self.qGroupBox3)
        self.qPushButton7.setText("显示数据模型的StringList")
        self.qVBoxLayout4.addWidget(self.qPushButton6)
        self.qVBoxLayout4.addWidget(self.qPushButton7)
        self.qPlainTextEdit = QtWidgets.QPlainTextEdit(self.qGroupBox3)
        self.qVBoxLayout3.addLayout(self.qVBoxLayout4)
        self.qVBoxLayout3.addWidget(self.qPlainTextEdit)

        self.qLabel = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel.setText("当前项的ModelIndex")
        self.qHBoxLayout.addWidget(self.qLabel)

        self.qPushButton1.setObjectName("qPushButton1")
        self.qPushButton2.setObjectName("qPushButton2")
        self.qPushButton3.setObjectName("qPushButton3")
        self.qPushButton4.setObjectName("qPushButton4")
        self.qPushButton5.setObjectName("qPushButton5")
        self.qPushButton6.setObjectName("qPushButton6")
        self.qPushButton7.setObjectName("qPushButton7")
        self.qListView.setObjectName("qListView")
        QtCore.QMetaObject.connectSlotsByName(qWidget)


class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.__provinces = ["北京", "上海", "天津", "河北", "山东", "四川", "重庆", "广东", "河南"]
        self.model = QStringListModel(self)
        self.model.setStringList(self.__provinces)
        self.ui.qListView.setModel(self.model)
        self.ui.qListView.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)

    @pyqtSlot()
    def on_qPushButton1_clicked(self):  # 恢复列表
        self.model.setStringList(self.__provinces)

    @pyqtSlot()
    def on_qPushButton2_clicked(self):  # 添加项
        lastRow = self.model.rowCount()
        self.model.insertRow(lastRow)
        index = self.model.index(lastRow, 0)
        self.model.setData(index, "new item", Qt.DisplayRole)
        self.ui.qListView.setCurrentIndex(index)

    @pyqtSlot()
    def on_qPushButton3_clicked(self):  # 插入项
        index = self.ui.qListView.currentIndex()
        self.model.insertRow(index.row())
        self.model.setData(index, "inserted item", Qt.DisplayRole)
        self.ui.qListView.setCurrentIndex(index)

    @pyqtSlot()
    def on_qPushButton4_clicked(self):  # 删除当前项
        index = self.ui.qListView.currentIndex()
        self.model.removeRow(index.row())

    @pyqtSlot()
    def on_qPushButton5_clicked(self):  # 清空列表
        count = self.model.rowCount()
        self.model.removeRows(0, count)

    @pyqtSlot()
    def on_qPushButton6_clicked(self):  # 清空文本
        self.ui.qPlainTextEdit.clear()

    @pyqtSlot()
    def on_qPushButton7_clicked(self):  # 显示数据模型的StringList
        strList = self.model.stringList()
        self.ui.qPlainTextEdit.clear()
        for strLine in strList:
            self.ui.qPlainTextEdit.appendPlainText(strLine)

    def on_qListView_clicked(self, index):
        self.ui.qLabel.setText("当前项index:row=%d, column=%d" % (index.row(),index.column()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())
