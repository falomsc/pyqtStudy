import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, pyqtSlot, QFile, QIODevice, Qt, QItemSelectionModel
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlRecord, QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 387)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(50, 25, 431, 241))
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 653, 23))
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
        self.actRecInsert = QtWidgets.QAction(MainWindow)
        self.actRecInsert.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/306.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRecInsert.setIcon(icon2)
        self.actRecInsert.setObjectName("actRecInsert")
        self.actRecDelete = QtWidgets.QAction(MainWindow)
        self.actRecDelete.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/delete1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRecDelete.setIcon(icon3)
        self.actRecDelete.setObjectName("actRecDelete")
        self.actRecEdit = QtWidgets.QAction(MainWindow)
        self.actRecEdit.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/812.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRecEdit.setIcon(icon4)
        self.actRecEdit.setObjectName("actRecEdit")
        self.actScan = QtWidgets.QAction(MainWindow)
        self.actScan.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/up.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actScan.setIcon(icon5)
        self.actScan.setObjectName("actScan")
        self.actTestSQL = QtWidgets.QAction(MainWindow)
        self.actTestSQL.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/828.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actTestSQL.setIcon(icon6)
        self.actTestSQL.setObjectName("actTestSQL")
        self.mainToolBar.addAction(self.actOpenDB)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actRecInsert)
        self.mainToolBar.addAction(self.actRecEdit)
        self.mainToolBar.addAction(self.actRecDelete)
        self.mainToolBar.addAction(self.actScan)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actTestSQL)
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo7_3, QSqlQuery的使用"))
        self.actOpenDB.setText(_translate("MainWindow", "打开数据库"))
        self.actOpenDB.setToolTip(_translate("MainWindow", "打开数据库"))
        self.actQuit.setText(_translate("MainWindow", "退出"))
        self.actQuit.setToolTip(_translate("MainWindow", "退出"))
        self.actRecInsert.setText(_translate("MainWindow", "插入记录"))
        self.actRecInsert.setToolTip(_translate("MainWindow", "插入记录"))
        self.actRecDelete.setText(_translate("MainWindow", "删除记录"))
        self.actRecDelete.setToolTip(_translate("MainWindow", "删除记录"))
        self.actRecEdit.setText(_translate("MainWindow", "编辑记录"))
        self.actRecEdit.setToolTip(_translate("MainWindow", "编辑记录"))
        self.actScan.setText(_translate("MainWindow", "涨工资"))
        self.actScan.setToolTip(_translate("MainWindow", "涨工资"))
        self.actTestSQL.setText(_translate("MainWindow", "SQL测试"))
        self.actTestSQL.setToolTip(_translate("MainWindow", "SQL语句测试"))

import rec.res_rc_0703

class Ui_QWDialogData(object):
    def setupUi(self, QWDialogData):
        QWDialogData.setObjectName("QWDialogData")
        QWDialogData.resize(499, 324)
        font = QtGui.QFont()
        font.setPointSize(10)
        QWDialogData.setFont(font)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(QWDialogData)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(QWDialogData)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.editName = QtWidgets.QLineEdit(self.groupBox_2)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.comboSex = QtWidgets.QComboBox(self.groupBox_2)
        self.comboSex.setObjectName("comboSex")
        self.comboSex.addItem("")
        self.comboSex.addItem("")
        self.gridLayout.addWidget(self.comboSex, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.editBirth = QtWidgets.QDateEdit(self.groupBox_2)
        self.editBirth.setCalendarPopup(True)
        self.editBirth.setDate(QtCore.QDate(2017, 2, 20))
        self.editBirth.setObjectName("editBirth")
        self.gridLayout.addWidget(self.editBirth, 3, 1, 1, 1)
        self.comboProvince = QtWidgets.QComboBox(self.groupBox_2)
        self.comboProvince.setEditable(True)
        self.comboProvince.setObjectName("comboProvince")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.comboProvince.addItem("")
        self.gridLayout.addWidget(self.comboProvince, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.comboDep = QtWidgets.QComboBox(self.groupBox_2)
        self.comboDep.setEditable(True)
        self.comboDep.setObjectName("comboDep")
        self.comboDep.addItem("")
        self.comboDep.addItem("")
        self.comboDep.addItem("")
        self.comboDep.addItem("")
        self.gridLayout.addWidget(self.comboDep, 5, 1, 1, 1)
        self.spinSalary = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinSalary.setPrefix("")
        self.spinSalary.setMinimum(1000)
        self.spinSalary.setMaximum(50000)
        self.spinSalary.setSingleStep(100)
        self.spinSalary.setProperty("value", 1000)
        self.spinSalary.setObjectName("spinSalary")
        self.gridLayout.addWidget(self.spinSalary, 6, 1, 1, 1)
        self.editMemo = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.editMemo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.editMemo.setObjectName("editMemo")
        self.gridLayout.addWidget(self.editMemo, 7, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinEmpNo = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinEmpNo.setMinimum(1)
        self.spinEmpNo.setMaximum(10000)
        self.spinEmpNo.setObjectName("spinEmpNo")
        self.gridLayout.addWidget(self.spinEmpNo, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.LabPhoto = QtWidgets.QLabel(self.groupBox_2)
        self.LabPhoto.setMinimumSize(QtCore.QSize(150, 0))
        self.LabPhoto.setMaximumSize(QtCore.QSize(350, 16777215))
        self.LabPhoto.setObjectName("LabPhoto")
        self.verticalLayout.addWidget(self.LabPhoto)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.frame = QtWidgets.QFrame(QWDialogData)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnSetPhoto = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/00.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetPhoto.setIcon(icon)
        self.btnSetPhoto.setObjectName("btnSetPhoto")
        self.verticalLayout_2.addWidget(self.btnSetPhoto)
        self.btnClearPhoto = QtWidgets.QPushButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/103.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClearPhoto.setIcon(icon1)
        self.btnClearPhoto.setObjectName("btnClearPhoto")
        self.verticalLayout_2.addWidget(self.btnClearPhoto)
        self.btnOK = QtWidgets.QPushButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/322.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOK.setIcon(icon2)
        self.btnOK.setObjectName("btnOK")
        self.verticalLayout_2.addWidget(self.btnOK)
        self.btnClose = QtWidgets.QPushButton(self.frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/324.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon3)
        self.btnClose.setObjectName("btnClose")
        self.verticalLayout_2.addWidget(self.btnClose)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.label_12.setBuddy(self.spinSalary)
        self.label_7.setBuddy(self.comboProvince)
        self.label_5.setBuddy(self.editBirth)
        self.label_6.setBuddy(self.comboDep)
        self.label_9.setBuddy(self.editMemo)
        self.label_2.setBuddy(self.editName)
        self.label.setBuddy(self.spinEmpNo)
        self.label_3.setBuddy(self.comboSex)

        self.retranslateUi(QWDialogData)
        self.btnClose.clicked.connect(QWDialogData.reject)
        self.btnOK.clicked.connect(QWDialogData.accept)
        QtCore.QMetaObject.connectSlotsByName(QWDialogData)

    def retranslateUi(self, QWDialogData):
        _translate = QtCore.QCoreApplication.translate
        QWDialogData.setWindowTitle(_translate("QWDialogData", "编辑记录"))
        self.label_12.setText(_translate("QWDialogData", "工  资"))
        self.label_7.setText(_translate("QWDialogData", "出生省份"))
        self.comboSex.setItemText(0, _translate("QWDialogData", "男"))
        self.comboSex.setItemText(1, _translate("QWDialogData", "女"))
        self.label_5.setText(_translate("QWDialogData", "出生日期"))
        self.editBirth.setDisplayFormat(_translate("QWDialogData", "yyyy-MM-dd"))
        self.comboProvince.setCurrentText(_translate("QWDialogData", "北京"))
        self.comboProvince.setItemText(0, _translate("QWDialogData", "北京"))
        self.comboProvince.setItemText(1, _translate("QWDialogData", "上海"))
        self.comboProvince.setItemText(2, _translate("QWDialogData", "天津"))
        self.comboProvince.setItemText(3, _translate("QWDialogData", "重庆"))
        self.comboProvince.setItemText(4, _translate("QWDialogData", "安徽"))
        self.comboProvince.setItemText(5, _translate("QWDialogData", "河北"))
        self.comboProvince.setItemText(6, _translate("QWDialogData", "河南"))
        self.comboProvince.setItemText(7, _translate("QWDialogData", "湖北"))
        self.comboProvince.setItemText(8, _translate("QWDialogData", "湖南"))
        self.comboProvince.setItemText(9, _translate("QWDialogData", "山西"))
        self.comboProvince.setItemText(10, _translate("QWDialogData", "山东"))
        self.comboProvince.setItemText(11, _translate("QWDialogData", "陕西"))
        self.comboProvince.setItemText(12, _translate("QWDialogData", "江苏"))
        self.comboProvince.setItemText(13, _translate("QWDialogData", "江西"))
        self.label_6.setText(_translate("QWDialogData", "部  门"))
        self.comboDep.setCurrentText(_translate("QWDialogData", "销售部"))
        self.comboDep.setItemText(0, _translate("QWDialogData", "销售部"))
        self.comboDep.setItemText(1, _translate("QWDialogData", "技术部"))
        self.comboDep.setItemText(2, _translate("QWDialogData", "生产部"))
        self.comboDep.setItemText(3, _translate("QWDialogData", "行政部"))
        self.label_9.setText(_translate("QWDialogData", "备   注"))
        self.label_2.setText(_translate("QWDialogData", "姓  名"))
        self.label.setText(_translate("QWDialogData", "工  号"))
        self.label_3.setText(_translate("QWDialogData", "性  别"))
        self.label_13.setText(_translate("QWDialogData", "照  片"))
        self.LabPhoto.setText(_translate("QWDialogData", "LabPhoto"))
        self.btnSetPhoto.setText(_translate("QWDialogData", "导入照片"))
        self.btnClearPhoto.setText(_translate("QWDialogData", "清除照片"))
        self.btnOK.setText(_translate("QWDialogData", "确  定"))
        self.btnClose.setText(_translate("QWDialogData", "取  消"))

class QmyDialogData(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWDialogData()
        self.ui.setupUi(self)

        self.__record = QSqlRecord()

    def setInsertRecord(self, recData):
        self.__record = recData
        self.ui.spinEmpNo.setEnabled(True)
        self.setWindowTitle("插入新记录")
        self.ui.spinEmpNo.setValue(recData.value("empNo"))

    def setUpdateRecord(self, recData):
        self.__record = recData
        self.ui.spinEmpNo.setEnabled(False)
        self.setWindowTitle("更新记录")

        self.ui.spinEmpNo.setValue(recData.value("empNo"))
        self.ui.editName.setText(recData.value("Name"))
        self.ui.comboSex.setCurrentText(recData.value("Gender"))

        birth = recData.value("Birthday")
        birth_date = QDate.fromString(birth, "yyyy-MM-dd")
        self.ui.editBirth.setDate(birth_date)

        self.ui.comboProvince.setCurrentText(recData.value("Province"))
        self.ui.comboDep.setCurrentText(recData.value("Department"))
        self.ui.spinSalary.setValue(recData.value("Salary"))
        self.ui.editMemo.setPlainText(recData.value("Memo"))

        picData = recData.value("Photo")
        if(picData==''):
            self.ui.LabPhoto.clear()
        else:
            pic = QPixmap()
            pic.loadFromData(picData)
            W = self.ui.LabPhoto.size().width()
            self.ui.LabPhoto.setPixmap(pic.scaledToWidth(W))

    def getRecordData(self):
        self.__record.setValue("empNo", self.ui.spinEmpNo.value())
        self.__record.setValue("Name", self.ui.editName.text())
        self.__record.setValue("Gender", self.ui.comboSex.currentText())
        self.__record.setValue("Birthday", self.ui.editBirth.date())
        self.__record.setValue("Province", self.ui.comboProvince.currentText())
        self.__record.setValue("Department", self.ui.comboDep.currentText())
        self.__record.setValue("Salary", self.ui.spinSalary.value())
        self.__record.setValue("Memo", self.ui.editMemo.toPlainText())
        return self.__record

    @pyqtSlot()
    def on_btnSetPhoto_clicked(self):
        fileName, filt = QFileDialog.getOpenFileName(self, "选择图片", "", "照片(*.jpg)")
        if(fileName == ''):
            return
        file = QFile(fileName)
        file.open(QIODevice.ReadOnly)
        data = file.readAll()
        file.close()

        self.__record.setValue("Photo", data)
        pic = QPixmap()
        pic.loadFromData(data)
        W = self.ui.LabPhoto.width()
        self.ui.LabPhoto.setPixmap(pic.scaledToWidth(W))

    @pyqtSlot()
    def on_btnClearPhoto_clicked(self):
        self.ui.LabPhoto.clear()
        self.__record.setNull("Photo")


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setCentralWidget(self.ui.tableView)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(22)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(60)

    def __getFieldNames(self):
        emptyRec = self.qryModel.record()
        self.fldNum = {}
        for i in range(emptyRec.count()):
            fieldName = emptyRec.fieldName(i)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName] = i
        print(self.fldNum)


    def __openTable(self):
        self.qryModel = QSqlQueryModel(self)
        self.qryModel.setQuery('''SELECT empNo, Name, Gender, Birthday, Province, Department, Salary FROM employee ORDER BY empNo''')
        if self.qryModel.lastError().isValid():
            QMessageBox.critical(self, "错误", "数据表查询错误,错误信息\n" + self.qryModel.lastError().text())
            return
        self.__getFieldNames()
        self.qryModel.setHeaderData(0, Qt.Horizontal, "工号")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "姓名")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "性别")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "出生日期")
        self.qryModel.setHeaderData(4, Qt.Horizontal, "省份")
        self.qryModel.setHeaderData(5, Qt.Horizontal, "部门")
        self.qryModel.setHeaderData(6, Qt.Horizontal, "工资")

        self.selModel = QItemSelectionModel(self.qryModel)
        self.selModel.currentRowChanged.connect(self.do_currentRowChanged)
        self.ui.tableView.setModel(self.qryModel)
        self.ui.tableView.setSelectionModel(self.selModel)
        self.ui.actOpenDB.setEnabled(False)
        self.ui.actRecInsert.setEnabled(True)
        self.ui.actRecDelete.setEnabled(True)
        self.ui.actRecEdit.setEnabled(True)
        self.ui.actScan.setEnabled(True)
        self.ui.actTestSQL.setEnabled(True)


    def __updateRecord(self, recNo):
        curRec = self.qryModel.record(recNo)
        empNo = curRec.value("EmpNo")
        query = QSqlQuery(self.DB)
        query.prepare("SELECT * FROM employee WHERE EmpNo = :ID")
        query.bindValue(":ID", empNo)
        query.exec()
        query.first()
        if(not query.isValid()):
            return

        curRec = query.record()
        dlgData = QmyDialogData(self)
        dlgData.setUpdateRecord(curRec)
        ret = dlgData.exec()
        if(ret != QDialog.Accepted):
            return

        recData = dlgData.getRecordData()
        query.prepare('''UPDATE employee SET Name=:Name, Gender=:Gender,
                      Birthday=:Birthday, Province=:Province,
                      Department=:Department, Salary=:Salary,
                      Memo=:Memo, Photo=:Photo WHERE EmpNo = :ID''')

        query.bindValue(":Name", recData.value("Name"))
        query.bindValue(":Gender", recData.value("Gender"))
        query.bindValue(":Birthday", recData.value("Birthday"))
        query.bindValue(":Province", recData.value("Province"))
        query.bindValue(":Department", recData.value("Department"))
        query.bindValue(":Salary", recData.value("Salary"))
        query.bindValue(":Memo", recData.value("Memo"))
        query.bindValue(":Photo", recData.value("Photo"))
        query.bindValue(":ID", empNo)

        if(not query.exec()):
            QMessageBox.critical(self, "错误", "记录更新错误\n" + query.lastError().text())
        else:
            self.qryModel.query().exec()


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
            QMessageBox.warning(self, "错误", "打开数据库失败")


    @pyqtSlot()
    def on_actRecInsert_triggered(self):
        query = QSqlQuery(self.DB)
        query.exec("select * from employee where EmpNo = -1")
        curRec = query.record()
        curRec.setValue("EmpNo", self.qryModel.rowCount() + 3000)
        dlgData = QmyDialogData(self)
        dlgData.setInsertRecord(curRec)

        ret = dlgData.exec()
        if(ret != QDialog.Accepted):
            return

        recData = dlgData.getRecordData()

        query.prepare('''INSERT INTO employee (EmpNo,Name,Gender,Birthday,
                    Province,Department,Salary,Memo,Photo)
                    VALUES(:EmpNo,:Name, :Gender,:Birthday,:Province,
                    :Department,:Salary,:Memo,:Photo)''')
        query.bindValue(":EmpNo", recData.value("EmpNo"))
        query.bindValue(":Name", recData.value("Name"))
        query.bindValue(":Gender", recData.value("Gender"))
        query.bindValue(":Birthday", recData.value("Birthday"))

        query.bindValue(":Province", recData.value("Province"))
        query.bindValue(":Department", recData.value("Department"))

        query.bindValue(":Salary", recData.value("Salary"))
        query.bindValue(":Memo", recData.value("Memo"))
        query.bindValue(":Photo", recData.value("Photo"))

        res = query.exec()
        if(res == False):
            QMessageBox.critical(self, "错误", "插入记录错误\n" + query.lastError().text())
        else:
            sqlStr = self.qryModel.query().executedQuery()
            self.qryModel.setQuery(sqlStr)


    @pyqtSlot()
    def on_actRecDelete_triggered(self):
        curRecNo = self.selModel.currentIndex().row()
        curRec = self.qryModel.record(curRecNo)
        if(curRec.isEmpty()):
            return
        empNo = curRec.value("EmpNo")
        query = QSqlQuery(self.DB)
        query.prepare("DELETE  FROM employee WHERE EmpNo = :ID")
        query.bindValue(":ID", empNo)
        if(query.exec() == False):
            QMessageBox.critical(self, "错误", "删除记录出现错误\n" + query.lastError().text())
        else:
            sqlStr = self.qryModel.query().executedQuery()
            self.qryModel.setQuery(sqlStr)


    @pyqtSlot()
    def on_actRecEdit_triggered(self):
        curRecNo = self.selModel.currentIndex().row()
        self.__updateRecord(curRecNo)

    def on_tableView_doubleClicked(self, index):
        curRecNo = index.row()
        self.__updateRecord(curRecNo)


    @pyqtSlot()
    def on_actScan_triggered(self):
        qryEmpList = QSqlQuery(self.DB)
        qryEmpList.exec("SELECT empNo,Salary FROM employee ORDER BY empNo")
        qryUpdate = QSqlQuery(self.DB)
        qryUpdate.prepare('''UPDATE employee SET Salary=:Salary WHERE EmpNo = :ID''')

        qryEmpList.first()
        while(qryEmpList.isValid()):
            empID = qryEmpList.value("empNo")
            salary = qryEmpList.value("Salary")
            salary = salary + 500

            qryUpdate.bindValue(":ID", empID)
            qryUpdate.bindValue(":Salary", salary)
            qryUpdate.exec()

            if not qryEmpList.next():
                break
        self.qryModel.query().exec()
        QMessageBox.information(self, "提示", "涨工资计算完毕")


    @pyqtSlot()
    def on_actTestSQL_triggered(self):
        query = QSqlQuery(self.DB)
        query.exec('''UPDATE employee SET Salary=500+Salary''')
        sqlStr = self.qryModel.query().executedQuery()
        self.qryModel.setQuery(sqlStr)
        print("SQL OK")


    def do_currentRowChanged(self, current, previous):
        if(current.isValid() == False):
            return
        curRec = self.qryModel.record(current.row())
        empNo = curRec.value("EmpNo")
        self.ui.statusBar.showMessage("当前记录：工号 = %d" %empNo)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )
