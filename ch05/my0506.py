import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QEvent, QRect, QSize, pyqtSlot
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, qApp, QFrame, QAbstractItemView


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(712, 502)
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(qWidget)
        self.qFrame = QtWidgets.QFrame(qWidget)
        self.qFrame.setFrameShape(QFrame.Panel)
        self.qFrame.setFrameShadow(QFrame.Raised)
        self.qHBoxLayout2 = QtWidgets.QHBoxLayout(self.qFrame)
        self.qHBoxLayout1 = QtWidgets.QHBoxLayout(qWidget)
        self.qVBoxLayout1.addWidget(self.qFrame)
        self.qVBoxLayout1.addLayout(self.qHBoxLayout1)

        self.qGroupBox1 = QtWidgets.QGroupBox(self.qFrame)
        self.qGroupBox1.setTitle("设置对象")
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qGroupBox1)
        self.qRadioButton1 = QtWidgets.QRadioButton(self.qGroupBox1)
        self.qRadioButton1.setText("listSource")
        self.qRadioButton2 = QtWidgets.QRadioButton(self.qGroupBox1)
        self.qRadioButton2.setText("listWidget")
        self.qRadioButton3 = QtWidgets.QRadioButton(self.qGroupBox1)
        self.qRadioButton3.setText("treeWidget")
        self.qRadioButton4 = QtWidgets.QRadioButton(self.qGroupBox1)
        self.qRadioButton4.setText("tableWidget")
        self.qVBoxLayout2.addWidget(self.qRadioButton1)
        self.qVBoxLayout2.addWidget(self.qRadioButton2)
        self.qVBoxLayout2.addWidget(self.qRadioButton3)
        self.qVBoxLayout2.addWidget(self.qRadioButton4)

        self.qGroupBox2 = QtWidgets.QGroupBox(self.qFrame)
        self.qGroupBox2.setTitle("拖放参数设置")
        self.qGridLayout = QtWidgets.QGridLayout(self.qGroupBox2)
        self.qCheckBox1 = QtWidgets.QCheckBox(self.qGroupBox2)
        self.qCheckBox1.setText("acceptDrops")
        self.qCheckBox2 = QtWidgets.QCheckBox(self.qGroupBox2)
        self.qCheckBox2.setText("dragEnabled")
        self.qComboBox1 = QtWidgets.QComboBox(self.qGroupBox2)
        self.qComboBox1.addItem("NoDragDrop")
        self.qComboBox1.addItem("DragOnly")
        self.qComboBox1.addItem("DropOnly")
        self.qComboBox1.addItem("DragDrop")
        self.qComboBox1.addItem("InternalMove")
        self.qComboBox2 = QtWidgets.QComboBox(self.qGroupBox2)
        self.qComboBox2.addItem("CopyAction")
        self.qComboBox2.addItem("MoveAction")
        self.qComboBox2.addItem("LinkAction")
        self.qComboBox2.addItem("IgnoreAction")
        self.qLabel1 = QtWidgets.QLabel(self.qGroupBox2)
        self.qLabel1.setText("dragDropMode")
        self.qLabel2 = QtWidgets.QLabel(self.qGroupBox2)
        self.qLabel2.setText("defaultDropAction")
        self.qGridLayout.addWidget(self.qCheckBox1, 0, 0, 1, 1)
        self.qGridLayout.addWidget(self.qCheckBox2, 0, 1, 1, 1)
        self.qGridLayout.addWidget(self.qLabel1, 1, 0, 1, 1)
        self.qGridLayout.addWidget(self.qLabel2, 2, 0, 1, 1)
        self.qGridLayout.addWidget(self.qComboBox1, 1, 1, 1, 1)
        self.qGridLayout.addWidget(self.qComboBox2, 2, 1, 1, 1)

        self.qSpacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.qHBoxLayout2.addWidget(self.qGroupBox1)
        self.qHBoxLayout2.addWidget(self.qGroupBox2)
        self.qHBoxLayout2.addItem(self.qSpacerItem)

        self.qGroupBox3 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox3.setTitle("ListSource")
        self.qVBoxLayout3 = QtWidgets.QVBoxLayout(self.qGroupBox3)
        self.qGroupBox4 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox4.setTitle("listWidget")
        self.qVBoxLayout4 = QtWidgets.QVBoxLayout(self.qGroupBox4)
        self.qGroupBox5 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox5.setTitle("treeWidget")
        self.qVBoxLayout5 = QtWidgets.QVBoxLayout(self.qGroupBox5)
        self.qGroupBox6 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox6.setTitle("tableWidget")
        self.qVBoxLayout6 = QtWidgets.QVBoxLayout(self.qGroupBox6)
        self.qListWidget1 = QtWidgets.QListWidget(self.qGroupBox3)
        self.qListWidget2 = QtWidgets.QListWidget(self.qGroupBox4)
        self.qTreeWidget = QtWidgets.QTreeWidget(self.qGroupBox5)
        self.qTreeWidget.header().setVisible(False)
        self.qTableWidget = QtWidgets.QTableWidget(self.qGroupBox6)
        self.qTableWidget.setMinimumSize(QSize(180, 0))
        self.qTableWidget.setAlternatingRowColors(True)
        self.qTableWidget.setRowCount(6)
        self.qTableWidget.setColumnCount(2)
        self.qVBoxLayout3.addWidget(self.qListWidget1)
        self.qVBoxLayout4.addWidget(self.qListWidget2)
        self.qVBoxLayout5.addWidget(self.qTreeWidget)
        self.qVBoxLayout6.addWidget(self.qTableWidget)
        self.qHBoxLayout1.addWidget(self.qGroupBox3)
        self.qHBoxLayout1.addWidget(self.qGroupBox4)
        self.qHBoxLayout1.addWidget(self.qGroupBox5)
        self.qHBoxLayout1.addWidget(self.qGroupBox6)

        qListWidgetItem1 = QtWidgets.QListWidgetItem(QIcon("../image/200.bmp"), "剪切", self.qListWidget1)
        qListWidgetItem2 = QtWidgets.QListWidgetItem(QIcon("../image/202.bmp"), "复制", self.qListWidget1)
        qListWidgetItem3 = QtWidgets.QListWidgetItem(QIcon("../image/204.bmp"), "粘贴", self.qListWidget1)
        qListWidgetItem4 = QtWidgets.QListWidgetItem(QIcon("../image/500.bmp"), "粗体", self.qListWidget1)
        qListWidgetItem5 = QtWidgets.QListWidgetItem(QIcon("../image/502.bmp"), "斜体", self.qListWidget1)
        qListWidgetItem6 = QtWidgets.QListWidgetItem(QIcon("../image/504.bmp"), "下划线", self.qListWidget1)
        qListWidgetItem7 = QtWidgets.QListWidgetItem(QIcon("../image/508.bmp"), "左对齐", self.qListWidget1)
        qListWidgetItem8 = QtWidgets.QListWidgetItem(QIcon("../image/510.bmp"), "中间对齐", self.qListWidget1)
        qListWidgetItem9 = QtWidgets.QListWidgetItem(QIcon("../image/512.bmp"), "右对齐", self.qListWidget1)
        qListWidgetItem10 = QtWidgets.QListWidgetItem(QIcon("../image/718.bmp"), "红色", self.qListWidget1)
        qListWidgetItem11 = QtWidgets.QListWidgetItem(QIcon("../image/724.bmp"), "绿色", self.qListWidget1)
        qListWidgetItem12 = QtWidgets.QListWidgetItem(QIcon("../image/728.bmp"), "蓝色", self.qListWidget1)

        qTreeWidgetItem1 = QtWidgets.QTreeWidgetItem(self.qTreeWidget)
        qTreeWidgetItem2 = QtWidgets.QTreeWidgetItem(self.qTreeWidget)
        self.qTreeWidget.topLevelItem(0).setText(0, "编辑")
        self.qTreeWidget.topLevelItem(1).setText(0, "格式")

        self.qRadioButton1.setObjectName("qRadioButton1")
        self.qRadioButton2.setObjectName("qRadioButton2")
        self.qRadioButton3.setObjectName("qRadioButton3")
        self.qRadioButton4.setObjectName("qRadioButton4")
        self.qCheckBox1.setObjectName("qCheckBox1")
        self.qCheckBox2.setObjectName("qCheckBox2")
        self.qComboBox1.setObjectName("qComboBox1")
        self.qComboBox2.setObjectName("qComboBox2")
        self.qRadioButton1.setChecked(True)
        QtCore.QMetaObject.connectSlotsByName(qWidget)




class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.qListWidget1.installEventFilter(self)
        self.ui.qListWidget2.installEventFilter(self)
        self.ui.qTreeWidget.installEventFilter(self)
        self.ui.qTableWidget.installEventFilter(self)

        self.ui.qListWidget1.setAcceptDrops(True)
        self.ui.qListWidget1.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui.qListWidget1.setDragEnabled(True)
        self.ui.qListWidget1.setDefaultDropAction(Qt.CopyAction)

        self.ui.qListWidget2.setAcceptDrops(True)
        self.ui.qListWidget2.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui.qListWidget2.setDragEnabled(True)
        self.ui.qListWidget2.setDefaultDropAction(Qt.MoveAction)

        self.ui.qTreeWidget.setAcceptDrops(True)
        self.ui.qTreeWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui.qTreeWidget.setDragEnabled(True)
        self.ui.qTreeWidget.setDefaultDropAction(Qt.MoveAction)

        self.ui.qTableWidget.setAcceptDrops(True)
        self.ui.qTableWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.ui.qTableWidget.setDragEnabled(True)
        self.ui.qTableWidget.setDefaultDropAction(Qt.MoveAction)

        self.__itemView = None

    # def __refreshToUI(self):
    #     self.ui.qCheckBox1.setChecked(self.__itemView.acceptDrops())
    #     self.ui.qCheckBox2.setChecked(self.__itemView.dragEnabled())
    #     self.ui.qComboBox1.setCurrentIndex(self.__itemView.dragDropMode())
    #     index = self.__getDropActionIndex(self.__itemView.defaultDropAction())
    #     self.ui.qComboBox2.setCurrentIndex(index)
    def __refreshToUI(self):
        self.ui.qCheckBox1.setChecked(self.__itemView.acceptDrops())
        self.ui.qCheckBox2.setChecked(self.__itemView.dragEnabled())
        # self.ui.qComboBox1.setCurrentIndex(self.__itemView.dragDropMode())
        # index = self.__getDropActionIndex(self.__itemView.defaultDropAction())
        # self.ui.qComboBox2.setCurrentIndex(index)

    # def __getDropActionType(self, index):
    #     if index == 0:
    #         return Qt.CopyAction
    #     elif index == 1:
    #         return Qt.MoveAction
    #     elif index == 2:
    #         return Qt.LinkAction
    #     elif index == 3:
    #         return Qt.IgnoreAction
    #     else:
    #         return Qt.CopyAction

    # def eventFilter(self, watched, event):
    #     if(event.type()==QEvent.KeyPress) and (event.key()==Qt.Key_Delete):
    #         if(watched == self.ui.qListWidget1):
    #             self.ui.qListWidget1.takeItem(self.ui.qListWidget1.currentRow())
    #         elif(watched == self.ui.qListWidget2):
    #             self.ui.qListWidget2.takeItem(self.ui.qListWidget2.currentRow())
    #         elif(watched==self.ui.qTreeWidget):
    #             curItem = self.ui.qTreeWidget.currentItem()
    #             if(curItem.parent()!=None):
    #                 parItem = curItem.parent()
    #                 parItem.removeChild(curItem)
    #             else:
    #                 index = self.ui.qTreeWidget.indexOfTopLevelItem(curItem)
    #                 self.ui.qTreeWidget.takeTopLevelItem(index)
    #         elif(watched == self.ui.qTableWidget):
    #             self.ui.qTableWidget.takeItem(self.ui.qTableWidget.currentRow(),self.ui.qTableWidget.currentColumn())
    #     return super().eventFilter(watched, event)

    @pyqtSlot()
    def on_qRadioButton1_clicked(self):
        self.__itemView = self.ui.qListWidget1
        self.__refreshToUI()

    # @pyqtSlot()
    # def on_qRadioButton2_clicked(self):
    #     self.__itemView = self.ui.qListWidget2
    #     self.__refreshToUI()
    #
    # @pyqtSlot()
    # def on_qRadioButton3_clicked(self):
    #     self.__itemView = self.ui.qTreeWidget
    #     self.__refreshToUI()
    #
    # @pyqtSlot()
    # def on_qRadioButton4_clicked(self):
    #     self.__itemView = self.ui.qTableWidget
    #     self.__refreshToUI()
    #
    # @pyqtSlot(bool)
    # def on_qCheckBox1_clicked(self, checked):
    #     self.__itemView.setAcceptDrops(checked)
    #
    # @pyqtSlot(bool)
    # def on_qCheckBox2_clicked(self, checked):
    #     self.__itemView.setDragEnabled(checked)
    #
    # @pyqtSlot(int)
    # def on_qComboBox1_currentIndexChanged(self, index):
    #     mode = (QAbstractItemView.DragDropMode)(index)
    #     self.__itemView.setDragDropMode(mode)
    #
    # @pyqtSlot(int)
    # def on_qComboBox2_currentIndexChanged(self, index):
    #     actionType = self.__getDropActionType(index)
    #     self.__itemView.setDefaultDropAction(actionType)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())