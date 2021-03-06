import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSlot, QItemSelectionModel, QModelIndex, QFile, QIODevice
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QStyledItemDelegate, QWidget, QDoubleSpinBox, QAbstractItemView, QFileDialog, QMessageBox, \
    QDataWidgetMapper, QComboBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 610)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setGeometry(QtCore.QRect(0, 40, 881, 445))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.groupBox_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBoxSort = QtWidgets.QGroupBox(self.frame)
        self.groupBoxSort.setEnabled(False)
        self.groupBoxSort.setObjectName("groupBoxSort")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxSort)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.groupBoxSort)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)
        self.comboFields = QtWidgets.QComboBox(self.groupBoxSort)
        self.comboFields.setObjectName("comboFields")
        self.gridLayout_3.addWidget(self.comboFields, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.radioBtnAscend = QtWidgets.QRadioButton(self.groupBoxSort)
        self.radioBtnAscend.setChecked(True)
        self.radioBtnAscend.setObjectName("radioBtnAscend")
        self.gridLayout_3.addWidget(self.radioBtnAscend, 1, 1, 1, 1)
        self.radioBtnDescend = QtWidgets.QRadioButton(self.groupBoxSort)
        self.radioBtnDescend.setObjectName("radioBtnDescend")
        self.gridLayout_3.addWidget(self.radioBtnDescend, 1, 2, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBoxSort)
        self.groupBoxFilter = QtWidgets.QGroupBox(self.frame)
        self.groupBoxFilter.setEnabled(False)
        self.groupBoxFilter.setObjectName("groupBoxFilter")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxFilter)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioBtnMan = QtWidgets.QRadioButton(self.groupBoxFilter)
        self.radioBtnMan.setObjectName("radioBtnMan")
        self.gridLayout_2.addWidget(self.radioBtnMan, 0, 0, 1, 1)
        self.radioBtnWoman = QtWidgets.QRadioButton(self.groupBoxFilter)
        self.radioBtnWoman.setObjectName("radioBtnWoman")
        self.gridLayout_2.addWidget(self.radioBtnWoman, 0, 1, 1, 1)
        self.radioBtnBoth = QtWidgets.QRadioButton(self.groupBoxFilter)
        self.radioBtnBoth.setChecked(True)
        self.radioBtnBoth.setObjectName("radioBtnBoth")
        self.gridLayout_2.addWidget(self.radioBtnBoth, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBoxFilter)
        spacerItem2 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame)
        self.tableView = QtWidgets.QTableView(self.groupBox_3)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(50)
        self.verticalLayout_2.addWidget(self.tableView)
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dbComboSex = QtWidgets.QComboBox(self.groupBox)
        self.dbComboSex.setObjectName("dbComboSex")
        self.dbComboSex.addItem("")
        self.dbComboSex.addItem("")
        self.gridLayout.addWidget(self.dbComboSex, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.dbEditName = QtWidgets.QLineEdit(self.groupBox)
        self.dbEditName.setObjectName("dbEditName")
        self.gridLayout.addWidget(self.dbEditName, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.dbSpinSalary = QtWidgets.QSpinBox(self.groupBox)
        self.dbSpinSalary.setPrefix("")
        self.dbSpinSalary.setMinimum(1000)
        self.dbSpinSalary.setMaximum(50000)
        self.dbSpinSalary.setSingleStep(100)
        self.dbSpinSalary.setProperty("value", 1000)
        self.dbSpinSalary.setObjectName("dbSpinSalary")
        self.gridLayout.addWidget(self.dbSpinSalary, 6, 1, 1, 1)
        self.dbEditMemo = QtWidgets.QPlainTextEdit(self.groupBox)
        self.dbEditMemo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dbEditMemo.setObjectName("dbEditMemo")
        self.gridLayout.addWidget(self.dbEditMemo, 7, 1, 1, 1)
        self.dbComboDep = QtWidgets.QComboBox(self.groupBox)
        self.dbComboDep.setEditable(True)
        self.dbComboDep.setObjectName("dbComboDep")
        self.dbComboDep.addItem("")
        self.dbComboDep.addItem("")
        self.dbComboDep.addItem("")
        self.dbComboDep.addItem("")
        self.gridLayout.addWidget(self.dbComboDep, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.dbSpinEmpNo = QtWidgets.QSpinBox(self.groupBox)
        self.dbSpinEmpNo.setMinimum(1)
        self.dbSpinEmpNo.setMaximum(10000)
        self.dbSpinEmpNo.setObjectName("dbSpinEmpNo")
        self.gridLayout.addWidget(self.dbSpinEmpNo, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.dbComboProvince = QtWidgets.QComboBox(self.groupBox)
        self.dbComboProvince.setEditable(True)
        self.dbComboProvince.setObjectName("dbComboProvince")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.dbComboProvince.addItem("")
        self.gridLayout.addWidget(self.dbComboProvince, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.dbEditBirth = QtWidgets.QDateEdit(self.groupBox)
        self.dbEditBirth.setCalendarPopup(True)
        self.dbEditBirth.setDate(QtCore.QDate(2017, 2, 20))
        self.dbEditBirth.setObjectName("dbEditBirth")
        self.gridLayout.addWidget(self.dbEditBirth, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.dbLabPhoto = QtWidgets.QLabel(self.groupBox)
        self.dbLabPhoto.setMinimumSize(QtCore.QSize(150, 0))
        self.dbLabPhoto.setMaximumSize(QtCore.QSize(400, 16777215))
        self.dbLabPhoto.setObjectName("dbLabPhoto")
        self.verticalLayout.addWidget(self.dbLabPhoto)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 949, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setIconSize(QtCore.QSize(16, 16))
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
        self.actPhoto = QtWidgets.QAction(MainWindow)
        self.actPhoto.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/00.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actPhoto.setIcon(icon7)
        self.actPhoto.setObjectName("actPhoto")
        self.actPhotoClear = QtWidgets.QAction(MainWindow)
        self.actPhotoClear.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/images/103.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actPhotoClear.setIcon(icon8)
        self.actPhotoClear.setObjectName("actPhotoClear")
        self.actScan = QtWidgets.QAction(MainWindow)
        self.actScan.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/images/up.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actScan.setIcon(icon9)
        self.actScan.setObjectName("actScan")
        self.mainToolBar.addAction(self.actOpenDB)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actRecAppend)
        self.mainToolBar.addAction(self.actRecInsert)
        self.mainToolBar.addAction(self.actRecDelete)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actPhoto)
        self.mainToolBar.addAction(self.actPhotoClear)
        self.mainToolBar.addAction(self.actScan)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actSubmit)
        self.mainToolBar.addAction(self.actRevert)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actQuit)
        self.label_2.setBuddy(self.dbEditName)
        self.label_3.setBuddy(self.dbComboSex)
        self.label_9.setBuddy(self.dbEditMemo)
        self.label_12.setBuddy(self.dbSpinSalary)
        self.label_6.setBuddy(self.dbComboDep)
        self.label.setBuddy(self.dbSpinEmpNo)
        self.label_7.setBuddy(self.dbComboProvince)
        self.label_5.setBuddy(self.dbEditBirth)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo7_1, QSqlTableModel的使用"))
        self.groupBoxSort.setTitle(_translate("MainWindow", "排序"))
        self.label_14.setText(_translate("MainWindow", "排序字段"))
        self.radioBtnAscend.setText(_translate("MainWindow", "升序"))
        self.radioBtnDescend.setText(_translate("MainWindow", "降序"))
        self.groupBoxFilter.setTitle(_translate("MainWindow", "数据过滤"))
        self.radioBtnMan.setText(_translate("MainWindow", "男"))
        self.radioBtnWoman.setText(_translate("MainWindow", "女"))
        self.radioBtnBoth.setText(_translate("MainWindow", "全显示"))
        self.label_2.setText(_translate("MainWindow", "姓  名"))
        self.dbComboSex.setItemText(0, _translate("MainWindow", "男"))
        self.dbComboSex.setItemText(1, _translate("MainWindow", "女"))
        self.label_3.setText(_translate("MainWindow", "性  别"))
        self.label_9.setText(_translate("MainWindow", "备   注"))
        self.label_12.setText(_translate("MainWindow", "工  资"))
        self.dbComboDep.setItemText(0, _translate("MainWindow", "销售部"))
        self.dbComboDep.setItemText(1, _translate("MainWindow", "技术部"))
        self.dbComboDep.setItemText(2, _translate("MainWindow", "生产部"))
        self.dbComboDep.setItemText(3, _translate("MainWindow", "行政部"))
        self.label_6.setText(_translate("MainWindow", "部  门"))
        self.label.setText(_translate("MainWindow", "工  号"))
        self.label_7.setText(_translate("MainWindow", "出生省份"))
        self.dbComboProvince.setItemText(0, _translate("MainWindow", "北京"))
        self.dbComboProvince.setItemText(1, _translate("MainWindow", "上海"))
        self.dbComboProvince.setItemText(2, _translate("MainWindow", "天津"))
        self.dbComboProvince.setItemText(3, _translate("MainWindow", "重庆"))
        self.dbComboProvince.setItemText(4, _translate("MainWindow", "安徽"))
        self.dbComboProvince.setItemText(5, _translate("MainWindow", "河北"))
        self.dbComboProvince.setItemText(6, _translate("MainWindow", "河南"))
        self.dbComboProvince.setItemText(7, _translate("MainWindow", "湖北"))
        self.dbComboProvince.setItemText(8, _translate("MainWindow", "湖南"))
        self.dbComboProvince.setItemText(9, _translate("MainWindow", "山西"))
        self.dbComboProvince.setItemText(10, _translate("MainWindow", "山东"))
        self.dbComboProvince.setItemText(11, _translate("MainWindow", "陕西"))
        self.dbComboProvince.setItemText(12, _translate("MainWindow", "江苏"))
        self.dbComboProvince.setItemText(13, _translate("MainWindow", "江西"))
        self.label_5.setText(_translate("MainWindow", "出生日期"))
        self.dbEditBirth.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.label_13.setText(_translate("MainWindow", "照  片"))
        self.dbLabPhoto.setText(_translate("MainWindow", "dbLabPhoto"))
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
        self.actPhoto.setText(_translate("MainWindow", "设置照片"))
        self.actPhoto.setToolTip(_translate("MainWindow", "设置照片"))
        self.actPhotoClear.setText(_translate("MainWindow", "清除照片"))
        self.actPhotoClear.setToolTip(_translate("MainWindow", "清除照片"))
        self.actScan.setText(_translate("MainWindow", "涨工资"))
        self.actScan.setToolTip(_translate("MainWindow", "涨工资"))

import rec.res_rc_0701

class QmyFloatSpinDelegate(QStyledItemDelegate):
    def __init__(self, minV=0, maxV=10000, digi=2, parent=None):
        super().__init__(parent)
        self.__min=minV
        self.__max=maxV
        self.__decimals=digi

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        editor = QDoubleSpinBox(parent)
        editor.setFrame(False)
        editor.setRange(self.__min, self.__max)
        editor.setDecimals(self.__decimals)
        return editor

    def setEditorData(self, editor: QWidget, index: QtCore.QModelIndex) -> None:
        model=index.model()
        text=model.data(index, Qt.EditRole)
        editor.setValue(float(text))

    def setModelData(self, editor: QWidget, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        value = editor.value()
        model.setDate(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> None:
        editor.setGeometry(option.rect)


class QmyComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__itemList = []
        self.__isEditable = False

    def setItems(self, itemList, isEditable=False):
        self.__itemList=itemList
        self.__isEditable=isEditable

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        editor = QComboBox(parent)
        editor.setFrame(False)
        editor.setEditable(self.__isEditable)
        editor.addItems(self.__itemList)
        return editor

    def setEditorData(self, editor: QWidget, index: QtCore.QModelIndex) -> None:
        model = index.model()
        text = model.data(index, Qt.EditRole)
        editor.setCurrentText(text)

    def setModelData(self, editor: QWidget, model: QtCore.QAbstractItemModel, index: QtCore.QModelIndex) -> None:
        text = editor.currentText()
        model.setData(index, text, Qt.EditRole)

    def updateEditorGeometry(self, editor: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> None:
        editor.setGeometry(option.rect)


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.splitter)

        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.verticalHeader().setDefaultSectionSize(22)
        self.ui.tableView.horizontalHeader().setDefaultSectionSize(60)

    def __openTable(self):
        self.tabModel = QSqlTableModel(self, self.DB)
        self.tabModel.setTable("employee")
        self.tabModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.tabModel.setSort(self.tabModel.fieldIndex("empNo"), Qt.AscendingOrder)
        if(self.tabModel.select()==False):
            QMessageBox.critical(self, "错误信息", "打开数据表错误，错误信息\n"+self.tabModel.lastError().text())
            return
        self.__getFieldNames()

        self.tabModel.setHeaderData(self.fldNum["empNo"], Qt.Horizontal, "工号")
        self.tabModel.setHeaderData(self.fldNum["Name"], Qt.Horizontal, "姓名")
        self.tabModel.setHeaderData(self.fldNum["Gender"], Qt.Horizontal, "性别")
        self.tabModel.setHeaderData(self.fldNum["Birthday"], Qt.Horizontal, "出生日期")
        self.tabModel.setHeaderData(self.fldNum["Province"], Qt.Horizontal, "省份")
        self.tabModel.setHeaderData(self.fldNum["Department"], Qt.Horizontal, "部门")
        self.tabModel.setHeaderData(self.fldNum["Salary"], Qt.Horizontal, "工资")
        self.tabModel.setHeaderData(self.fldNum["Memo"], Qt.Horizontal, "备注")
        self.tabModel.setHeaderData(self.fldNum["Photo"], Qt.Horizontal, "照片")

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.tabModel)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
        self.mapper.addMapping(self.ui.dbSpinEmpNo, self.fldNum["empNo"])
        self.mapper.addMapping(self.ui.dbEditName, self.fldNum["Name"])
        self.mapper.addMapping(self.ui.dbComboSex, self.fldNum["Gender"])
        self.mapper.addMapping(self.ui.dbEditBirth, self.fldNum["Birthday"])
        self.mapper.addMapping(self.ui.dbComboProvince, self.fldNum["Province"])
        self.mapper.addMapping(self.ui.dbComboDep, self.fldNum["Department"])
        self.mapper.addMapping(self.ui.dbSpinSalary, self.fldNum["Salary"])
        self.mapper.addMapping(self.ui.dbEditMemo, self.fldNum["Memo"])
        self.mapper.toFirst()

        self.selModel = QItemSelectionModel(self.tabModel)
        self.selModel.currentChanged.connect(self.do_currentChanged)
        self.selModel.currentRowChanged.connect(self.do_currentRowChanged)

        self.ui.tableView.setModel(self.tabModel)
        self.ui.tableView.setSelectionModel(self.selModel)

        self.ui.tableView.setColumnHidden(self.fldNum["Memo"], True)
        self.ui.tableView.setColumnHidden(self.fldNum["Photo"], True)


        strList = ("男", "女")
        self.__delegatesex = QmyComboBoxDelegate()
        self.__delegatesex.setItems(strList, False)
        self.ui.tableView.setItemDelegateForColumn(self.fldNum["Gender"], self.__delegatesex)

        strList = ("销售部", "技术部", "生产部", "行政部")
        self.__delegateDepart = QmyComboBoxDelegate()
        self.__delegateDepart.setItems(strList, True)
        self.ui.tableView.setItemDelegateForColumn(self.fldNum["Department"], self.__delegateDepart)

        self.ui.actOpenDB.setEnabled(False)
        self.ui.actOpenDB.setEnabled(False)

        self.ui.actRecAppend.setEnabled(True)
        self.ui.actRecInsert.setEnabled(True)
        self.ui.actRecDelete.setEnabled(True)
        self.ui.actScan.setEnabled(True)

        self.ui.groupBoxSort.setEnabled(True)
        self.ui.groupBoxFilter.setEnabled(True)


    def __getFieldNames(self):
        emptyRec = self.tabModel.record()
        self.fldNum = {}
        for i in range(emptyRec.count()):
            fieldName = emptyRec.fieldName(i)
            self.ui.comboFields.addItem(fieldName)
            self.fldNum.setdefault(fieldName)
            self.fldNum[fieldName]=i
        print(self.fldNum)

    def do_currentChanged(self, current, previous):
        self.ui.actSubmit.setEnabled(self.tabModel.isDirty())
        self.ui.actRevert.setEnabled(self.tabModel.isDirty())

    def do_currentRowChanged(self, current, previous):
        self.ui.actRecDelete.setEnabled(current.isValid())
        self.ui.actPhoto.setEnabled(current.isValid())
        self.ui.actPhotoClear.setEnabled(current.isValid())

        if(current.isValid() == False):
            self.ui.dbLabPhoto.clear()
            return

        self.mapper.setCurrentIndex(current.row())
        curRec = self.tabModel.record(current.row())

        if(curRec.isNull("Photo")):
            self.ui.dbLabPhoto.clear()
        else:
            data = curRec.value("Photo")
            pic = QPixmap()
            pic.loadFromData(data)
            w = self.ui.dbLabPhoto.size().width()
            self.ui.dbLabPhoto.setPixmap(pic.scaledToWidth(w))

    @pyqtSlot()
    def on_actOpenDB_triggered(self):
        dbFilename ,flt = QFileDialog.getOpenFileName(self, "选择数据库文件", "", "SQL Lite数据库(*.db *.db3)")
        if (dbFilename == ''):
            return
        self.DB = QSqlDatabase.addDatabase("QSQLITE")
        self.DB.setDatabaseName(dbFilename)
        if self.DB.open():
            self.__openTable()
        else:
            QMessageBox.warning(self, "错误", "打开数据库失败")

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
    def on_actRecAppend_triggered(self):
        self.tabModel.insertRow(self.tabModel.rowCount(), QModelIndex())
        curIndex = self.tabModel.index(self.tabModel.rowCount()-1, 1)
        self.selModel.clearSelection()
        self.selModel.setCurrentIndex(curIndex, QItemSelectionModel.Select)
        currow = curIndex.row()
        self.tabModel.setData(self.tabModel.index(currow, self.fldNum["empNo"]), 2000+self.tabModel.rowCount())
        self.tabModel.setData(self.tabModel.index(currow, self.fldNum["Gender"]), "男")

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
    def on_actPhotoClear_triggered(self):
        curRecNo = self.selModel.currentIndex().row()
        curRec = self.tabModel.record(curRecNo)
        curRec.setNull("Photo")
        self.tabModel.setRecord(curRecNo, curRec)
        self.ui.dbLabPhoto.clear()

    @pyqtSlot()
    def on_actPhoto_triggered(self):
        fileName, filt = QFileDialog.getOpenFileName(self, "选择图片文件", "", "照片(*.jpg")
        if(fileName==''):
            return
        file=QFile(fileName)
        file.open(QIODevice.ReadOnly)
        try:
            data = file.readAll()
        finally:
            file.close()

        curRecNo = self.selModel.currentIndex().row()
        curRec = self.tabModel.record(curRecNo)
        curRec.setValue("Photo", data)
        self.tabModel.setRecord(curRecNo, curRec)

        pic = QPixmap()
        pic.loadFromData(data)
        w = self.ui.dbLabPhoto.width()
        self.ui.dbLabPhoto.setPixmap(pic.scaledToWidth(w))

    @pyqtSlot()
    def on_actScan_triggered(self):
        if(self.tabModel.rowCount()==0):
            return
        for i in range(self.tabModel.rowCount()):
            aRec = self.tabModel.record(i)
            salary = aRec.value("Salary")
            salary = salary*1.1
            aRec.setValue("Salary", salary)
            self.tabModel.setRecord(i, aRec)

        if(self.tabModel.submitAll()):
            QMessageBox.information(self, "消息", "涨工资计算完毕了")

    @pyqtSlot()
    def on_comboFields_currentIndexChanged(self, index):
        if self.ui.radioBtnAscend.isChecked():
            self.tabModel.setSort(index, Qt.AscendingOrder)
        else:
            self.tabModel.setSort(index, Qt.DescendingOrder)
        self.tabModel.select()

    @pyqtSlot()
    def on_radioBtnAscend_clicked(self):
        self.tabModel.setSort(self.ui.comboFields.currentIndex(), Qt.AscendingOrder)
        self.tabModel.select()

    @pyqtSlot()
    def on_radioBtnDescend_clicked(self):
        self.tabModel.setSort(self.ui.comboFields.currentIndex(), Qt.DescendingOrder)
        self.tabModel.select()

    @pyqtSlot()
    def on_radioBtnMan_clicked(self):
        self.tabModel.setFilter("Gender='男'")

    @pyqtSlot()
    def on_radioBtnWoman_clicked(self):
        self.tabModel.setFilter("Gender='女'")

    @pyqtSlot()
    def on_radioBtnBoth_clicked(self):
        self.tabModel.setFilter("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )
