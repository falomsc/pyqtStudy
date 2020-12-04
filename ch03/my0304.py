'''
目前问题：

总结：

'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime, QSize
from PyQt5.QtWidgets import QDateTimeEdit


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(600, 300)
        self.qHBoxLayout = QtWidgets.QHBoxLayout(qWidget)
        self.qGrounpBox1 = QtWidgets.QGroupBox(qWidget)
        self.qGrounpBox1.setTitle("日期时间")
        self.qGrounpBox2 = QtWidgets.QGroupBox(qWidget)
        self.qGrounpBox2.setTitle("日历选择")
        self.qGridLayout1 = QtWidgets.QGridLayout(self.qGrounpBox1)
        self.qGridLayout2 = QtWidgets.QGridLayout(self.qGrounpBox2)
        self.qPushButton1 = QtWidgets.QPushButton(self.qGrounpBox1)
        self.qPushButton1.setText("读取当前日期时间")
        self.qPushButton2 = QtWidgets.QPushButton(self.qGrounpBox1)
        self.qPushButton2.setText("设置时间")
        self.qPushButton3 = QtWidgets.QPushButton(self.qGrounpBox1)
        self.qPushButton3.setText("设置日期")
        self.qPushButton4 = QtWidgets.QPushButton(self.qGrounpBox1)
        self.qPushButton4.setText("设置日期时间")
        self.qLabel1 = QtWidgets.QLabel(self.qGrounpBox1)
        self.qLabel1.setText("字符串显示")
        self.qLabel1.setAlignment(Qt.AlignCenter)
        self.qLabel2 = QtWidgets.QLabel(self.qGrounpBox1)
        self.qLabel2.setText("时 间")
        self.qLabel3 = QtWidgets.QLabel(self.qGrounpBox1)
        self.qLabel3.setText("日 期")
        self.qLabel4 = QtWidgets.QLabel(self.qGrounpBox1)
        self.qLabel4.setText("日期时间")
        self.qLineEdit1 = QtWidgets.QLineEdit(self.qGrounpBox1)
        self.qLineEdit1.setInputMask("99:99:99;_")
        self.qLineEdit2 = QtWidgets.QLineEdit(self.qGrounpBox1)
        self.qLineEdit2.setInputMask("9999-99-99")
        self.qLineEdit2.setMinimumSize(QSize(150, 0))
        self.qLineEdit3 = QtWidgets.QLineEdit(self.qGrounpBox1)
        self.qLineEdit3.setInputMask("9999-99-99 99:99:99")
        self.qTimeEdit = QtWidgets.QTimeEdit(self.qGrounpBox1)
        self.qTimeEdit.setDisplayFormat("hh:mm:ss")
        self.qDateEdit = QtWidgets.QDateEdit(self.qGrounpBox1)
        self.qDateEdit.setDisplayFormat("yyyy年MM月dd日")
        self.qDateEdit.setCalendarPopup(True)
        self.qDateTimeEdit = QtWidgets.QDateTimeEdit(self.qGrounpBox1)
        self.qDateTimeEdit.setMinimumDateTime(QDateTime(1763, 9, 14, 0, 0, 0))
        self.qDateTimeEdit.setMaximumDateTime(QDateTime(3000, 12, 31, 23, 59, 59))
        self.qDateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.qDateTimeEdit.setCurrentSection(QDateTimeEdit.YearSection)
        self.qLabel5 = QtWidgets.QLabel(self.qGrounpBox2)
        self.qLabel5.setText("选择的日期：")
        self.qLineEdit4 = QtWidgets.QLineEdit(self.qGrounpBox2)
        self.qCalendarWidget = QtWidgets.QCalendarWidget(self.qGrounpBox2)

        self.qHBoxLayout.addWidget(self.qGrounpBox1)
        self.qHBoxLayout.addWidget(self.qGrounpBox2)
        self.qGridLayout1.addWidget(self.qPushButton1, 0, 1, 1, 1)
        self.qGridLayout1.addWidget(self.qLabel1, 0, 2, 1, 1)
        self.qGridLayout1.addWidget(self.qLabel2, 1, 0, 1, 1)
        self.qGridLayout1.addWidget(self.qTimeEdit, 1, 1, 1, 1)
        self.qGridLayout1.addWidget(self.qLineEdit1, 1, 2, 1, 1)
        self.qGridLayout1.addWidget(self.qPushButton2, 2, 2, 1, 1)
        self.qGridLayout1.addWidget(self.qLabel3, 3, 0, 1, 1)
        self.qGridLayout1.addWidget(self.qDateEdit, 3, 1, 1, 1)
        self.qGridLayout1.addWidget(self.qLineEdit2, 3, 2, 1, 1)
        self.qGridLayout1.addWidget(self.qPushButton3, 4, 2, 1, 1)
        self.qGridLayout1.addWidget(self.qLabel4, 5, 0, 1, 1)
        self.qGridLayout1.addWidget(self.qDateTimeEdit, 5, 1, 1, 1)
        self.qGridLayout1.addWidget(self.qLineEdit3, 5, 2, 1, 1)
        self.qGridLayout1.addWidget(self.qPushButton4, 6, 2, 1, 1)
        self.qGridLayout2.addWidget(self.qLabel5, 0, 0, 1, 1)
        self.qGridLayout2.addWidget(self.qLineEdit4, 0, 1, 1, 1)
        self.qGridLayout2.addWidget(self.qCalendarWidget, 1, 0, 1, 2)

        self.qLineEdit1.setObjectName("qLineEdit1")
        self.qLineEdit2.setObjectName("qLineEdit2")
        self.qLineEdit3.setObjectName("qLineEdit3")
        self.qLineEdit4.setObjectName("qLineEdit4")
        self.qPushButton1.setObjectName("qPushButton1")
        self.qPushButton2.setObjectName("qPushButton2")
        self.qPushButton3.setObjectName("qPushButton3")
        self.qPushButton4.setObjectName("qPushButton4")
        self.qTimeEdit.setObjectName("qTimeEdit")
        self.qDateEdit.setObjectName("qDateEdit")
        self.qDateTimeEdit.setObjectName("qDateTimeEdit")
        self.qCalendarWidget.setObjectName("qCalendarWidget")
        QtCore.QMetaObject.connectSlotsByName(qWidget)

        ############################  Init  ##################################
        self.qTimeEdit.setTime(QTime(15, 30, 55))
        self.qDateEdit.setDate(QDate(2016, 11, 21))
        self.qDateTimeEdit.setDateTime(QDateTime(2018, 10, 9, 8, 21, 28))


class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def on_qPushButton1_clicked(self):
        curDateTime = QDateTime.currentDateTime()
        self.ui.qTimeEdit.setTime(curDateTime.time())
        self.ui.qDateEdit.setDate(curDateTime.date())
        self.ui.qDateTimeEdit.setDateTime(curDateTime)

    def on_qPushButton2_clicked(self):
        time = QTime.fromString(self.ui.qLineEdit1.text(), "hh:mm:ss")
        self.ui.qTimeEdit.setTime(time)

    def on_qPushButton3_clicked(self):
        date = QDate.fromString(self.ui.qLineEdit2.text(), "yyyy-MM-dd")
        self.ui.qDateEdit.setDate(date)

    def on_qPushButton4_clicked(self):
        datetime = QDateTime.fromString(self.ui.qLineEdit3.text(), "yyyy-MM-dd hh:mm:ss")
        self.ui.qDateTimeEdit.setDateTime(datetime)

    def on_qCalendarWidget_selectionChanged(self):
        date = self.ui.qCalendarWidget.selectedDate()
        self.ui.qLineEdit4.setText(date.toString("yyyy年M月d日"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())
