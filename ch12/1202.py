import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QColorDialog
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPen, QPalette, QColor


class Ui_QWDialogPen(object):
    def setupUi(self, QWDialogPen):
        QWDialogPen.setObjectName("QWDialogPen")
        QWDialogPen.resize(319, 139)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        QWDialogPen.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(QWDialogPen)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(QWDialogPen)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.spinWidth = QtWidgets.QSpinBox(self.groupBox)
        self.spinWidth.setMinimumSize(QtCore.QSize(100, 0))
        self.spinWidth.setMinimum(1)
        self.spinWidth.setMaximum(100)
        self.spinWidth.setObjectName("spinWidth")
        self.gridLayout.addWidget(self.spinWidth, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboPenStyle = QtWidgets.QComboBox(self.groupBox)
        self.comboPenStyle.setObjectName("comboPenStyle")
        self.gridLayout.addWidget(self.comboPenStyle, 0, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.btnColor = QtWidgets.QPushButton(self.groupBox)
        self.btnColor.setAutoFillBackground(False)
        self.btnColor.setStyleSheet("background-color: rgb(255, 0, 255);")
        self.btnColor.setText("")
        self.btnColor.setFlat(False)
        self.btnColor.setObjectName("btnColor")
        self.gridLayout.addWidget(self.btnColor, 4, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.btnOK = QtWidgets.QPushButton(QWDialogPen)
        self.btnOK.setObjectName("btnOK")
        self.verticalLayout.addWidget(self.btnOK)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.btnCancel = QtWidgets.QPushButton(QWDialogPen)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout.addWidget(self.btnCancel)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(QWDialogPen)
        self.btnOK.clicked.connect(QWDialogPen.accept)
        self.btnCancel.clicked.connect(QWDialogPen.reject)
        QtCore.QMetaObject.connectSlotsByName(QWDialogPen)

    def retranslateUi(self, QWDialogPen):
        _translate = QtCore.QCoreApplication.translate
        QWDialogPen.setWindowTitle(_translate("QWDialogPen", "QPen属性设置对话框"))
        self.groupBox.setTitle(_translate("QWDialogPen", "Pen属性设置"))
        self.label.setText(_translate("QWDialogPen", "线 型"))
        self.label_3.setText(_translate("QWDialogPen", "颜 色"))
        self.label_2.setText(_translate("QWDialogPen", "线 宽"))
        self.btnOK.setText(_translate("QWDialogPen", "确 定"))
        self.btnCancel.setText(_translate("QWDialogPen", "取 消"))


class QmyDialogPen(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWDialogPen()
        self.ui.setupUi(self)  # 构造UI界面

        self.__pen = QPen()

        ##“线型”ComboBox的选择项设置
        self.ui.comboPenStyle.clear()
        self.ui.comboPenStyle.addItem("NoPen", 0)
        self.ui.comboPenStyle.addItem("SolidLine", 1)
        self.ui.comboPenStyle.addItem("DashLine", 2)
        self.ui.comboPenStyle.addItem("DotLine", 3)
        self.ui.comboPenStyle.addItem("DashDotLine", 4)
        self.ui.comboPenStyle.addItem("DashDotDotLine", 5)
        self.ui.comboPenStyle.addItem("CustomDashLine", 6)

        self.ui.comboPenStyle.setCurrentIndex(1)

    ##=================自定义接口函数====================
    def setPen(self, pen):  ##设置pen
        self.__pen = pen

        self.ui.spinWidth.setValue(pen.width())  # 线宽
        i = int(pen.style())  # 枚举类型转换为整型
        self.ui.comboPenStyle.setCurrentIndex(i)

        color = pen.color()  # QColor
        ##      self.ui.btnColor.setAutoFillBackground(True)
        qss = "background-color: rgb(%d, %d, %d)" % (
            color.red(), color.green(), color.blue())
        self.ui.btnColor.setStyleSheet(qss)  # 使用样式表设置按钮背景色

    def getPen(self):  ##返回pen
        index = self.ui.comboPenStyle.currentIndex()
        self.__pen.setStyle(Qt.PenStyle(index))  # 线型
        self.__pen.setWidth(self.ui.spinWidth.value())  # 线宽

        color = self.ui.btnColor.palette().color(QPalette.Button)
        self.__pen.setColor(color)  # 颜色
        return self.__pen

    @staticmethod  ##类函数，或静态函数
    def staticGetPen(iniPen):
        # 不能有参数self,不能与类的成员函数同名，也就是不能命名为getPen()
        Dlg = QmyDialogPen()  # 创建一个对话框
        Dlg.setPen(iniPen)  # 设置初始化QPen

        pen = iniPen
        ok = False

        ret = Dlg.exec()  # 模态显示对话框
        if ret == QDialog.Accepted:
            pen = Dlg.getPen()  # 获取pen
            ok = True

        return pen, ok  # 返回设置的QPen对象

    ##  ==========由connectSlotsByName()自动连接的槽函数============
    @pyqtSlot()  ##选择颜色
    def on_btnColor_clicked(self):
        color = QColorDialog.getColor()
        if color.isValid():  # 用样式表设置QPushButton的背景色
            qss = "background-color: rgb(%d, %d, %d);" % (
                color.red(), color.green(), color.blue())
            self.ui.btnColor.setStyleSheet(qss)


##  ============窗体测试程序 ================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    iniPen = QPen(Qt.blue)
    pen = QmyDialogPen.staticGetPen(iniPen)  # 测试类函数调用
    sys.exit(app.exec_())