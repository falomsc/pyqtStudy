'''
目前问题：
1，“自动计算总价”初始默认值不是0

总结：
1，qWidget.setTabOrder设置tab键顺序
2，必须设置伙伴关系Qlabel的快捷键才起作用
3，valueChanged必须加@pyqtSlot，否则报错

'''

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(300, 300)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(qWidget)
        self.qGroupBox1 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox2 = QtWidgets.QGroupBox(qWidget)
        self.qVBoxLayout.addWidget(self.qGroupBox1)
        self.qVBoxLayout.addWidget(self.qGroupBox2)
        self.qGroupBox1.setTitle("QLineEdit输入和显示数值")
        self.qGroupBox2.setTitle("SpinBox输入和显示")
        self.qLabel1_1 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel1_1.setText("数 量(&N)")
        self.qLabel1_2 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel1_2.setText("单 价(&P)")
        self.qLabel1_3 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel1_3.setText("总 价(&T)")
        self.qLineEdit1_1 = QtWidgets.QLineEdit(self.qGroupBox1)
        self.qLineEdit1_2 = QtWidgets.QLineEdit(self.qGroupBox1)
        self.qLineEdit1_3 = QtWidgets.QLineEdit(self.qGroupBox1)
        self.qPushButton1 = QtWidgets.QPushButton(self.qGroupBox1)
        self.qGridLayout1 = QtWidgets.QGridLayout(self.qGroupBox1)
        self.qPushButton1.setText("计算总价")
        self.qGridLayout1.addWidget(self.qLabel1_1, 0, 0, 1, 1)
        self.qGridLayout1.addWidget(self.qLineEdit1_1, 0, 1, 1, 1)
        self.qGridLayout1.addWidget(self.qLabel1_2, 0, 2, 1, 1)
        self.qGridLayout1.addWidget(self.qLineEdit1_2, 0, 3, 1, 1)
        self.qGridLayout1.addWidget(self.qPushButton1, 1, 0, 1, 2)
        self.qGridLayout1.addWidget(self.qLabel1_3, 1, 2, 1, 1)
        self.qGridLayout1.addWidget(self.qLineEdit1_3, 1, 3, 1, 1)

        self.qLabel2_1 = QtWidgets.QLabel(self.qGroupBox2)
        self.qLabel2_1.setText("数 量")
        self.qLabel2_2 = QtWidgets.QLabel(self.qGroupBox2)
        self.qLabel2_2.setText("单 价")
        self.qLabel2_3 = QtWidgets.QLabel(self.qGroupBox2)
        self.qLabel2_3.setText("自动计算总价")
        self.qSpinBox2 = QtWidgets.QSpinBox(self.qGroupBox2)
        self.qSpinBox2.setSuffix(" kg")
        self.qDoubleSpinBox2_1 = QtWidgets.QDoubleSpinBox(self.qGroupBox2)
        self.qDoubleSpinBox2_1.setPrefix("$ ")
        self.qDoubleSpinBox2_1.setDecimals(2)
        self.qDoubleSpinBox2_2 = QtWidgets.QDoubleSpinBox(self.qGroupBox2)
        self.qDoubleSpinBox2_2.setPrefix("$ ")
        self.qDoubleSpinBox2_2.setReadOnly(True)
        self.qDoubleSpinBox2_2.setMaximum(10000.0)
        self.qGridLayout2 = QtWidgets.QGridLayout(self.qGroupBox2)
        self.qGridLayout2.addWidget(self.qLabel2_1, 0, 0, 1, 1)
        self.qGridLayout2.addWidget(self.qSpinBox2, 0, 1, 1, 1)
        self.qGridLayout2.addWidget(self.qLabel2_2, 0, 2, 1, 1)
        self.qGridLayout2.addWidget(self.qDoubleSpinBox2_1, 0, 3, 1, 1)
        self.qGridLayout2.addWidget(self.qLabel2_3, 1, 2, 1, 1)
        self.qGridLayout2.addWidget(self.qDoubleSpinBox2_2, 1, 3, 1, 1)

        self.qLabel1_1.setObjectName("qLabel1_1")
        self.qLabel1_2.setObjectName("qLabel1_2")
        self.qLabel1_3.setObjectName("qLabel1_3")
        self.qLineEdit1_1.setObjectName("qLineEdit1_1")
        self.qLineEdit1_2.setObjectName("qLineEdit1_2")
        self.qLineEdit1_3.setObjectName("qLineEdit1_3")
        self.qPushButton1.setObjectName("qPushButton1")
        self.qLabel2_1.setObjectName("qLabel2_1")
        self.qLabel2_2.setObjectName("qLabel2_2")
        self.qLabel2_3.setObjectName("qLabel2_3")
        self.qSpinBox2.setObjectName("qSpinBox2")
        self.qDoubleSpinBox2_1.setObjectName("qDoubleSpinBox2_1")
        self.qDoubleSpinBox2_2.setObjectName("qDoubleSpinBox2_2")
        qWidget.setTabOrder(self.qLineEdit1_1, self.qLineEdit1_2)
        qWidget.setTabOrder(self.qLineEdit1_2, self.qLineEdit1_3)
        qWidget.setTabOrder(self.qLineEdit1_3, self.qSpinBox2)
        qWidget.setTabOrder(self.qSpinBox2, self.qDoubleSpinBox2_1)
        qWidget.setTabOrder(self.qDoubleSpinBox2_1, self.qDoubleSpinBox2_2)
        self.qLabel1_1.setBuddy(self.qLineEdit1_1)
        self.qLabel1_2.setBuddy(self.qLineEdit1_2)
        self.qLabel1_3.setBuddy(self.qLineEdit1_3)
        QtCore.QMetaObject.connectSlotsByName(qWidget)

        ############################  Init  ##################################
        self.qLineEdit1_1.setText("16")
        self.qLineEdit1_2.setText("12.37")
        self.qSpinBox2.setValue(6)
        self.qDoubleSpinBox2_1.setValue(11.23)


class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def on_qPushButton1_clicked(self):
        num = int(self.ui.qLineEdit1_1.text())
        price = float(self.ui.qLineEdit1_2.text())
        sum = num * price
        self.ui.qLineEdit1_3.setText(str(sum))

    @pyqtSlot(int)
    def on_qSpinBox2_valueChanged(self, num):
        price = self.ui.qDoubleSpinBox2_1.value()
        sum = num * price
        self.ui.qDoubleSpinBox2_2.setValue(sum)

    @pyqtSlot(float)
    def on_qDoubleSpinBox2_1_valueChanged(self, price):
        num = self.ui.qSpinBox2.value()
        sum = num * price
        self.ui.qDoubleSpinBox2_2.setValue(sum)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())
