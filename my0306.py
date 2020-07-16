'''
目前问题：

总结：
1，addItems方法无法传入icon
2，currentIndexChanged(str)信号帮助文档里没有
3，向QComboBox传入字典时，addItem方法要多加一个参数，读取的时候currentText是key，currentData是value

'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime, QTimer, QSize, pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap, QImage


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(469, 163)
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(qWidget)
        self.qGroupBox1 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox1.setTitle("选择的内容")
        self.qGroupBox2 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox2.setTitle("简单的ComboBox")
        self.qGroupBox3 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox3.setTitle("有用户数据的ComboBox")
        self.qHBoxLayout = QtWidgets.QHBoxLayout(qWidget)
        self.qPushButton1 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton1.setText("初始化列表")
        self.qPushButton2 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton2.setText("清除列表")
        self.qPushButton3 = QtWidgets.QPushButton(self.qGroupBox3)
        self.qPushButton3.setText("初始化城市+区号")
        self.qLineEdit = QtWidgets.QLineEdit(self.qGroupBox1)
        self.qLineEdit.setClearButtonEnabled(True)
        self.qCheckBox = QtWidgets.QCheckBox(self.qGroupBox2)
        self.qCheckBox.setText("可编辑")
        self.qComboBox1 = QtWidgets.QComboBox(self.qGroupBox2)
        self.qComboBox2 = QtWidgets.QComboBox(self.qGroupBox3)
        self.qGridLayout = QtWidgets.QGridLayout(self.qGroupBox2)
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qGroupBox1)
        self.qVBoxLayout3 = QtWidgets.QVBoxLayout(self.qGroupBox3)

        self.qVBoxLayout1.addWidget(self.qGroupBox1)
        self.qVBoxLayout1.addLayout(self.qHBoxLayout)
        self.qVBoxLayout2.addWidget(self.qLineEdit)
        self.qHBoxLayout.addWidget(self.qGroupBox2)
        self.qHBoxLayout.addWidget(self.qGroupBox3)
        self.qGridLayout.addWidget(self.qPushButton1, 0, 0, 1, 1)
        self.qGridLayout.addWidget(self.qPushButton2, 0, 1, 1, 1)
        self.qGridLayout.addWidget(self.qCheckBox, 0, 2, 1, 1)
        self.qGridLayout.addWidget(self.qComboBox1, 1, 0, 1, 3)
        self.qVBoxLayout3.addWidget(self.qPushButton3)
        self.qVBoxLayout3.addWidget(self.qComboBox2)

        self.qPushButton1.setObjectName("qPushButton1")
        self.qPushButton2.setObjectName("qPushButton2")
        self.qPushButton3.setObjectName("qPushButton3")
        self.qCheckBox.setObjectName("qCheckBox")
        self.qComboBox1.setObjectName("qComboBox1")
        self.qComboBox2.setObjectName("qComboBox2")
        QtCore.QMetaObject.connectSlotsByName(qWidget)

        ############################  Init  ##################################
        self.qComboBox1.addItem(QIcon("./image/aim.ico"), "北京市")
        self.qComboBox1.addItem("上海市")

class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def on_qPushButton1_clicked(self):
        self.ui.qComboBox1.clear()
        provinces = ["山东", "河北", "河南", "湖北", "湖南", "广东"]
        for i in provinces:
            self.ui.qComboBox1.addItem(QIcon("./image/unit.ico"), i)

    def on_qPushButton2_clicked(self):
        self.ui.qComboBox2.clear()

    @pyqtSlot(bool)
    def on_qCheckBox_clicked(self, checked):
        self.ui.qComboBox1.setEditable(checked)

    @pyqtSlot(str)
    def on_qComboBox1_currentIndexChanged(self, text):
        self.ui.qLineEdit.setText(text)

    def on_qPushButton3_clicked(self):
        cities = {"北京": 10, "上海": 21, "天津": 22, "徐州": 516, "福州": 591, "青岛": 532}
        for k in cities:
            self.ui.qComboBox2.addItem(QIcon("./image/unit.ico"), k, cities[k])

    @pyqtSlot(str)
    def on_qComboBox2_currentIndexChanged(self, text):
        zone = self.ui.qComboBox2.currentData()
        if(zone != None):
            self.ui.qLineEdit.setText(text + ":区号=%d" % zone)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())