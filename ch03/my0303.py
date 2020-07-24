'''
目前问题：

总结：
1，QtCore.QMetaObject.connectSlotsByName(qWidget)必须放在setObjectName语句后面

'''

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt, pyqtSlot


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(374, 228)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(qWidget)
        self.qGroupBox1 = QtWidgets.QGroupBox(qWidget)
        self.qGroupBox2 = QtWidgets.QGroupBox(qWidget)
        self.qGridLayout1 = QtWidgets.QGridLayout(self.qGroupBox1)
        self.qGridLayout2 = QtWidgets.QGridLayout(self.qGroupBox2)
        self.qGroupBox2.setTitle("ProgressBar设置")
        self.qLabel1 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel1.setText("Slider")
        self.qLabel2 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel2.setText("ScrollBar")
        self.qLabel3 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel3.setText("ProgressBar")
        self.qSlider = QtWidgets.QSlider(self.qGroupBox1)
        self.qSlider.setOrientation(Qt.Horizontal)
        self.qSlider.setMaximum(200)
        self.qScrollBar = QtWidgets.QScrollBar(self.qGroupBox1)
        self.qScrollBar.setOrientation(Qt.Horizontal)
        self.qScrollBar.setMaximum(200)
        self.qProgressBar = QtWidgets.QProgressBar(self.qGroupBox1)
        self.qProgressBar.setOrientation(Qt.Horizontal)
        self.qProgressBar.setMaximum(200)
        self.qProgressBar.setTextVisible(True)
        self.qCheckBox1 = QtWidgets.QCheckBox(self.qGroupBox2)
        self.qCheckBox1.setText("textVisible")
        self.qCheckBox2 = QtWidgets.QCheckBox(self.qGroupBox2)
        self.qCheckBox2.setText("InvertedAppearance")
        self.qRadioButton1 = QtWidgets.QRadioButton(self.qGroupBox2)
        self.qRadioButton1.setText("显示格式——百分比")
        self.qRadioButton1.setAutoExclusive(True)
        self.qRadioButton2 = QtWidgets.QRadioButton(self.qGroupBox2)
        self.qRadioButton2.setText("显示格式——当前值")
        self.qRadioButton2.setAutoExclusive(True)

        self.qVBoxLayout.addWidget(self.qGroupBox1)
        self.qVBoxLayout.addWidget(self.qGroupBox2)
        self.qGridLayout1.addWidget(self.qLabel1, 0, 0, 1, 1)
        self.qGridLayout1.addWidget(self.qLabel2, 1, 0, 1, 1)
        self.qGridLayout1.addWidget(self.qLabel3, 2, 0, 1, 1)
        self.qGridLayout1.addWidget(self.qSlider, 0, 1, 1, 1)
        self.qGridLayout1.addWidget(self.qScrollBar, 1, 1, 1, 1)
        self.qGridLayout1.addWidget(self.qProgressBar, 2, 1, 1, 1)
        self.qGridLayout2.addWidget(self.qCheckBox1, 0, 0, 1, 1)
        self.qGridLayout2.addWidget(self.qCheckBox2, 0, 1, 1, 1)
        self.qGridLayout2.addWidget(self.qRadioButton1, 1, 0, 1, 1)
        self.qGridLayout2.addWidget(self.qRadioButton2, 1, 1, 1, 1)

        self.qLabel1.setObjectName("qLabel1")
        self.qLabel2.setObjectName("qLabel2")
        self.qLabel3.setObjectName("qLabel3")
        self.qSlider.setObjectName("qSlider")
        self.qScrollBar.setObjectName("qScrollBar")
        self.qProgressBar.setObjectName("qProgressBar")
        self.qCheckBox1.setObjectName("qCheckBox1")
        self.qCheckBox2.setObjectName("qCheckBox2")
        self.qRadioButton1.setObjectName("qRadioButton1")
        self.qRadioButton2.setObjectName("qRadioButton2")
        QtCore.QMetaObject.connectSlotsByName(qWidget)

        ############################  Init  ##################################
        self.qSlider.setValue(23)
        self.qScrollBar.setValue(23)
        self.qProgressBar.setValue(24)
        self.qCheckBox1.setChecked(True)
        self.qRadioButton1.setChecked(True)


class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.qSlider.valueChanged.connect(self.do_valueChanged)
        self.ui.qScrollBar.valueChanged.connect(self.do_valueChanged)

    @pyqtSlot(bool)
    def on_qCheckBox1_clicked(self, checked):
        self.ui.qProgressBar.setTextVisible(checked)

    @pyqtSlot(bool)
    def on_qCheckBox2_clicked(self, checked):
        self.ui.qProgressBar.setInvertedAppearance(checked)

    def on_qRadioButton1_clicked(self):
        self.ui.qProgressBar.setFormat("%p%")

    def on_qRadioButton2_clicked(self):
        self.ui.qProgressBar.setFormat("%v")

    def do_valueChanged(self, value):
        self.ui.qProgressBar.setValue(value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())
