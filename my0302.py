'''
目前问题：
1，源代码为何要用QPixmap转QIcon而不直接用QIcon

总结：
1，母框架增加布局用addLayout
2，使用setMinimumSize扩宽QLineEdit的高度

'''

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QFrame


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(305, 198)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(qWidget)
        self.qHBoxLayout1 = QtWidgets.QHBoxLayout(qWidget)
        self.qHBoxLayout2 = QtWidgets.QHBoxLayout(qWidget)
        self.qHBoxLayout3 = QtWidgets.QHBoxLayout(qWidget)
        self.qPushButton1_1 = QtWidgets.QPushButton(qWidget)
        qIcon1_1 = QIcon("./image/508.bmp")
        self.qPushButton1_1.setText("居左")
        self.qPushButton1_1.setIcon(qIcon1_1)
        self.qPushButton1_1.setAutoExclusive(True)
        self.qPushButton1_1.setFlat(True)
        self.qPushButton1_1.setCheckable(True)
        self.qPushButton1_2 = QtWidgets.QPushButton(qWidget)
        qIcon1_2 = QIcon("./image/510.bmp")
        self.qPushButton1_2.setText("居中")
        self.qPushButton1_2.setIcon(qIcon1_2)
        self.qPushButton1_2.setAutoExclusive(True)
        self.qPushButton1_2.setFlat(True)
        self.qPushButton1_2.setCheckable(True)
        self.qPushButton1_3 = QtWidgets.QPushButton(qWidget)
        qIcon1_3 = QIcon("./image/512.bmp")
        self.qPushButton1_3.setText("居右")
        self.qPushButton1_3.setIcon(qIcon1_3)
        self.qPushButton1_3.setAutoExclusive(True)
        self.qPushButton1_3.setFlat(True)
        self.qPushButton1_3.setCheckable(True)
        self.qPushButton2_1 = QtWidgets.QPushButton(qWidget)
        qIcon2_1 = QIcon("./image/500.bmp")
        self.qPushButton2_1.setIcon(qIcon2_1)
        self.qPushButton2_1.setText("粗体")
        self.qPushButton2_1.setCheckable(True)
        self.qPushButton2_2 = QtWidgets.QPushButton(qWidget)
        qIcon2_2 = QIcon("./image/502.bmp")
        self.qPushButton2_2.setIcon(qIcon2_2)
        self.qPushButton2_2.setText("斜体")
        self.qPushButton2_2.setCheckable(True)
        self.qPushButton2_3 = QtWidgets.QPushButton(qWidget)
        qIcon2_3 = QIcon("./image/504.bmp")
        self.qPushButton2_3.setIcon(qIcon2_3)
        self.qPushButton2_3.setText("下划线")
        self.qPushButton2_3.setCheckable(True)
        self.qCheckBox1 = QtWidgets.QCheckBox(qWidget)
        self.qCheckBox1.setText("Readonly")
        self.qCheckBox2 = QtWidgets.QCheckBox(qWidget)
        self.qCheckBox2.setText("Enabled")
        self.qCheckBox3 = QtWidgets.QCheckBox(qWidget)
        self.qCheckBox3.setText("ClearButtonEnabled")
        self.qLineEdit = QtWidgets.QLineEdit(qWidget)
        self.qLineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.qFrame1 = QtWidgets.QFrame(qWidget)
        self.qFrame1.setFrameShape(QFrame.HLine)
        self.qFrame2 = QtWidgets.QFrame(qWidget)
        self.qFrame2.setFrameShape(QFrame.HLine)

        self.qHBoxLayout1.addWidget(self.qPushButton1_1)
        self.qHBoxLayout1.addWidget(self.qPushButton1_2)
        self.qHBoxLayout1.addWidget(self.qPushButton1_3)
        self.qHBoxLayout2.addWidget(self.qPushButton2_1)
        self.qHBoxLayout2.addWidget(self.qPushButton2_2)
        self.qHBoxLayout2.addWidget(self.qPushButton2_3)
        self.qHBoxLayout3.addWidget(self.qCheckBox1)
        self.qHBoxLayout3.addWidget(self.qCheckBox2)
        self.qHBoxLayout3.addWidget(self.qCheckBox3)
        self.qVBoxLayout.addLayout(self.qHBoxLayout1)
        self.qVBoxLayout.addWidget(self.qFrame1)
        self.qVBoxLayout.addLayout(self.qHBoxLayout2)
        self.qVBoxLayout.addWidget(self.qFrame2)
        self.qVBoxLayout.addLayout(self.qHBoxLayout3)
        self.qVBoxLayout.addWidget(self.qLineEdit)

        self.qPushButton1_1.setObjectName("qPushButton1_1")
        self.qPushButton1_2.setObjectName("qPushButton1_2")
        self.qPushButton1_3.setObjectName("qPushButton1_3")
        self.qPushButton2_1.setObjectName("qPushButton2_1")
        self.qPushButton2_2.setObjectName("qPushButton2_2")
        self.qPushButton2_3.setObjectName("qPushButton2_3")
        self.qCheckBox1.setObjectName("qCheckBox1")
        self.qCheckBox2.setObjectName("qCheckBox2")
        self.qCheckBox3.setObjectName("qCheckBox3")
        self.qLineEdit.setObjectName("qLineEdit")
        QtCore.QMetaObject.connectSlotsByName(qWidget)

        ############################  Init  ##################################
        self.qPushButton1_1.setChecked(True)
        self.qCheckBox2.setChecked(True)
        self.qLineEdit.setText("测试显示文本")
        font = QFont()
        font.setPointSize(14)
        self.qLineEdit.setFont(font)

class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def on_qPushButton1_1_clicked(self):
        self.ui.qLineEdit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    def on_qPushButton1_2_clicked(self):
        self.ui.qLineEdit.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def on_qPushButton1_3_clicked(self):
        self.ui.qLineEdit.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

    @pyqtSlot(bool)
    def on_qPushButton2_1_clicked(self, checked):
        font = self.ui.qLineEdit.font()
        font.setBold(checked)
        self.ui.qLineEdit.setFont(font)

    @pyqtSlot(bool)
    def on_qPushButton2_2_clicked(self, checked):
        font = self.ui.qLineEdit.font()
        font.setItalic(checked)
        self.ui.qLineEdit.setFont(font)

    @pyqtSlot(bool)
    def on_qPushButton2_3_clicked(self, checked):
        font = self.ui.qLineEdit.font()
        font.setUnderline(checked)
        self.ui.qLineEdit.setFont(font)

    @pyqtSlot(bool)
    def on_qCheckBox1_clicked(self, checked):
        self.ui.qLineEdit.setReadOnly(checked)

    @pyqtSlot(bool)
    def on_qCheckBox2_clicked(self, checked):
        self.ui.qLineEdit.setEnabled(checked)

    @pyqtSlot(bool)
    def on_qCheckBox3_clicked(self, checked):
        self.ui.qLineEdit.setClearButtonEnabled(checked)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())