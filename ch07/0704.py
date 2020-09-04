import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt, QItemSelectionModel, QModelIndex
from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlTableModel, QSqlRelation, QSqlRelationalDelegate
from PyQt5.QtWidgets import QAbstractItemView, QFileDialog, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 417)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(60, 20, 491, 271))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 662, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actOpenDB = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/open3.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actOpenDB.setIcon(icon)
        self.actOpenDB.setObjectName("actOpenDB")
        self.actQuit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/exit.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuit.setIcon(icon1)
        self.actQuit.setObjectName("actQuit")
        self.actRecAppend = QtWidgets.QAction(MainWindow)
        self.actRecAppend.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/316.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRecAppend.setIcon(icon2)
        self.actRecAppend.setObjectName("actRecAppend")
        self.actRecInsert = QtWidgets.QAction(MainWindow)
        self.actRecInsert.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/306.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRecInsert.setIcon(icon3)
        self.actRecInsert.setObjectName("actRecInsert")
        self.actSubmit = QtWidgets.QAction(MainWindow)
        self.actSubmit.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/save1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSubmit.setIcon(icon4)
        self.actSubmit.setObjectName("actSubmit")
        self.actRevert = QtWidgets.QAction(MainWindow)
        self.actRevert.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/ubdo.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRevert.setIcon(icon5)
        self.actRevert.setObjectName("actRevert")
        self.actRecDelete = QtWidgets.QAction(MainWindow)
        self.actRecDelete.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/delete1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRecDelete.setIcon(icon6)
        self.actRecDelete.setObjectName("actRecDelete")
        self.actFields = QtWidgets.QAction(MainWindow)
        self.actFields.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/124.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actFields.setIcon(icon7)
        self.actFields.setObjectName("actFields")
        self.mainToolBar.addAction(self.actOpenDB)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actRecAppend)
        self.mainToolBar.addAction(self.actRecInsert)
        self.mainToolBar.addAction(self.actRecDelete)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actSubmit)
        self.mainToolBar.addAction(self.actRevert)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actFields)
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo7_4, QSqlRelationalTableModel 的使用"))
        self.actOpenDB.setText(_translate("MainWindow", "打开"))
        self.actOpenDB.setToolTip(_translate("MainWindow", "打开数据库"))
        self.actQuit.setText(_translate("MainWindow", "退出"))
        self.actQuit.setToolTip(_translate("MainWindow", "退出"))
        self.actRecAppend.setText(_translate("MainWindow", "添加"))
        self.actRecAppend.setToolTip(_translate("MainWindow", "添加记录"))
        self.actRecInsert.setText(_translate("MainWindow", "插入"))
        self.actRecInsert.setToolTip(_translate("MainWindow", "插入记录"))
        self.actSubmit.setText(_translate("MainWindow", "保存"))
        self.actSubmit.setToolTip(_translate("MainWindow", "保存修改"))
        self.actRevert.setText(_translate("MainWindow", "取消"))
        self.actRevert.setToolTip(_translate("MainWindow", "取消修改"))
        self.actRecDelete.setText(_translate("MainWindow", "删除"))
        self.actRecDelete.setToolTip(_translate("MainWindow", "删除记录"))
        self.actFields.setText(_translate("MainWindow", "字段列表"))
        self.actFields.setToolTip(_translate("MainWindow", "字段列表"))

import rec.res_rc_0704

class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.tableView)

        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)

        self.ui.tableView.verticalHeader().setDefaultSectionSize(22)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(100)

    def __getFieldNames(self):
        emptyRec = self.tabModel.record()
        self.fldNum = {}
        for i in range(emptyRec.count()):
            fieldName = emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName]=i
        print(self.fldNum)

    def __openTable(self):
        self.tabModel = QSqlRelationalTableModel(self, self.DB)
        self.tabModel.setTable("studInfo")
        self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.tabModel.setSort(self.tabModel.fieldIndex("studID"), Qt.AscendingOrder)

        if(self.tabModel.select() == False):
            QMessageBox.critical(self, "错误信息", "打开数据表错误，错误信息\n"+self.tabModel.lastError().text())
            return

        self.__getFieldNames()
        self.tabModel.setHeaderData(self.fldNum["studID"], Qt.Horizontal, "学号")
        self.tabModel.setHeaderData(self.fldNum["name"], Qt.Horizontal, "姓名")
        self.tabModel.setHeaderData(self.fldNum["gender"], Qt.Horizontal, "性别")
        self.tabModel.setHeaderData(self.fldNum["departID"], Qt.Horizontal, "学院")
        self.tabModel.setHeaderData(self.fldNum["majorID"], Qt.Horizontal, "专业")

        self.tabModel.setRelation(self.fldNum["departID"], QSqlRelation("departments", "departID", "department"))
        self.tabModel.setRelation(self.fldNum["majorID"], QSqlRelation("majors", "majorID", "major"))

        self.selModel = QItemSelectionModel(self.tabModel)
        self.selModel.currentChanged.connect(self.do_currentChanged)

        self.ui.tableView.setModel(self.tabModel)
        self.ui.tableView.setSelectionModel(self.selModel)

        delgate = QSqlRelationalDelegate(self.ui.tableView)
        self.ui.tableView.setItemDelegate(delgate)

        self.tabModel.select()

        self.ui.actOpenDB.setEnabled(False)
        self.ui.actRecAppend.setEnabled(True)
        self.ui.actRecInsert.setEnabled(True)
        self.ui.actRecDelete.setEnabled(True)
        self.ui.actFields.setEnabled(True)

    @pyqtSlot()
    def on_actOpenDB_triggered(self):
        dbFilename, flt = QFileDialog.getOpenFileName(self, "选择数据库文件", "", "SQL Lite数据库(*.db *.db3)")
        if(dbFilename == ''):
            return
        self.DB = QSqlDatabase.addDatabase("QSQLITE")
        self.DB.setDatabaseName(dbFilename)
        if self.DB.open():
            self.__openTable()
        else:
            QMessageBox.warning(self, "错误", "打开数据库失败了")

    @pyqtSlot()
    def on_actSubmit_triggered(self):
        res = self.tabModel.submitAll()
        if(res == False):
            QMessageBox.information(self, "消息", "数据保存错误，错误信息\n" + self.tabModel.lastError().text())
        else:
            self.ui.actSubmit.setEnabled(False)
            self.ui.actRevert.setEnabled(False)

    @pyqtSlot()
    def on_actRevert_triggered(self):
        self.tabModel.revertAll()
        self.ui.actSubmit.setEnabled(False)
        self.ui.actRevert.setEnabled(False)

    @pyqtSlot()
    def on_actRecInsert_triggered(self):
        curIndex = self.ui.tableView.currentIndex()
        self.tabModel.insertRow(curIndex.row(), QModelIndex())
        self.selModel.clearSelection()
        self.selModel.setCurrentIndex(curIndex, QItemSelectionModel.Select)

    @pyqtSlot()
    def on_actRecDelete_triggered(self):
        curIndex = self.selModel.currentIndex()
        self.tabModel.removeRow(curIndex.row())

    @pyqtSlot()
    def on_actFields_triggered(self):
        emptyRec = self.tabModel.record()
        str = ''
        for i in range(emptyRec.count()):
            str = str + emptyRec.fieldName(i)+'\n'
        QMessageBox.information(self, "所有字段名", str)

    def do_currentChanged(self, current, previous):
        self.ui.actSubmit.setEnabled(self.tabModel.isDirty())
        self.ui.actRevert.setEnabled(self.tabModel.isDirty())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )