'''
注意：
1，保存文件并非真正保存
'''
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QDir, Qt, QTime
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QFileDialog, QColorDialog, QFontDialog, QMessageBox, \
    QLineEdit, QInputDialog, QProgressDialog


class Ui_Dialog():
    def setupUi(self, qDialog):
        qDialog.resize(556, 364)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(qDialog)
        self.qGridLayout1 = QtWidgets.QGridLayout(qDialog)
        self.qPlainTextEdit = QtWidgets.QPlainTextEdit(qDialog)
        self.qVBoxLayout.addLayout(self.qGridLayout1)
        self.qVBoxLayout.addWidget(self.qPlainTextEdit)

        self.qGroupBox1 = QtWidgets.QGroupBox(qDialog)
        self.qGroupBox1.setTitle("标准对话框")
        self.qGridLayout2 = QtWidgets.QGridLayout(self.qGroupBox1)
        self.qGroupBox2 = QtWidgets.QGroupBox(qDialog)
        self.qGroupBox2.setTitle("标准消息对话框 QMessageBox")
        self.qGridLayout3 = QtWidgets.QGridLayout(self.qGroupBox2)
        self.qGroupBox3 = QtWidgets.QGroupBox(qDialog)
        self.qGroupBox3.setTitle("输入标准对话框 QInputDialog")
        self.qGridLayout4 = QtWidgets.QGridLayout(self.qGroupBox3)
        self.qGroupBox4 = QtWidgets.QGroupBox(qDialog)
        self.qHBoxLayout = QtWidgets.QHBoxLayout(self.qGroupBox4)
        self.qGridLayout1.addWidget(self.qGroupBox1, 0, 0)
        self.qGridLayout1.addWidget(self.qGroupBox2, 0, 1)
        self.qGridLayout1.addWidget(self.qGroupBox3, 1, 0)
        self.qGridLayout1.addWidget(self.qGroupBox4, 1, 1)

        self.qPushButton1 = QtWidgets.QPushButton(self.qGroupBox1)
        self.qPushButton1.setText("打开一个文件")
        self.qPushButton2 = QtWidgets.QPushButton(self.qGroupBox1)
        self.qPushButton2.setText("打开多个文件")
        self.qPushButton3 = QtWidgets.QPushButton(self.qGroupBox1)
        self.qPushButton3.setText("选择已有目录")
        self.qPushButton4 = QtWidgets.QPushButton(self.qGroupBox1)
        self.qPushButton4.setText("保存文件")
        self.qPushButton5 = QtWidgets.QPushButton(self.qGroupBox1)
        self.qPushButton5.setText("选择颜色")
        self.qPushButton6 = QtWidgets.QPushButton(self.qGroupBox1)
        self.qPushButton6.setText("选择字体")
        self.qPushButton7 = QtWidgets.QPushButton(self.qGroupBox1)
        self.qPushButton7.setText("进度对话框")
        self.qPushButton8 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton8.setText("question")
        self.qPushButton9 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton9.setText("information")
        self.qPushButton10 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton10.setText("warning")
        self.qPushButton11 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton11.setText("critical")
        self.qPushButton12 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton12.setText("about")
        self.qPushButton13 = QtWidgets.QPushButton(self.qGroupBox2)
        self.qPushButton13.setText("aboutQt")
        self.qPushButton14 = QtWidgets.QPushButton(self.qGroupBox3)
        self.qPushButton14.setText("输入字符串")
        self.qPushButton15 = QtWidgets.QPushButton(self.qGroupBox3)
        self.qPushButton15.setText("输入整数")
        self.qPushButton16 = QtWidgets.QPushButton(self.qGroupBox3)
        self.qPushButton16.setText("输入浮点数")
        self.qPushButton17 = QtWidgets.QPushButton(self.qGroupBox3)
        self.qPushButton17.setText("条目选择输入")
        self.qPushButton18 = QtWidgets.QPushButton(self.qGroupBox4)
        self.qPushButton18.setText("清除文本框内容")
        self.qPushButton18.setIcon(QIcon("../image/212.bmp"))
        self.qPushButton19 = QtWidgets.QPushButton(self.qGroupBox4)
        self.qPushButton19.setText("退出")
        self.qPushButton19.setIcon(QIcon("../image/132.bmp"))
        self.qGridLayout2.addWidget(self.qPushButton1, 0, 0)
        self.qGridLayout2.addWidget(self.qPushButton2, 0, 1)
        self.qGridLayout2.addWidget(self.qPushButton3, 1, 0)
        self.qGridLayout2.addWidget(self.qPushButton4, 1, 1)
        self.qGridLayout2.addWidget(self.qPushButton5, 2, 0)
        self.qGridLayout2.addWidget(self.qPushButton6, 2, 1)
        self.qGridLayout2.addWidget(self.qPushButton7, 3, 0)
        self.qGridLayout3.addWidget(self.qPushButton8, 0, 0)
        self.qGridLayout3.addWidget(self.qPushButton9, 0, 1)
        self.qGridLayout3.addWidget(self.qPushButton10, 1, 0)
        self.qGridLayout3.addWidget(self.qPushButton11, 1, 1)
        self.qGridLayout3.addWidget(self.qPushButton12, 2, 0)
        self.qGridLayout3.addWidget(self.qPushButton13, 2, 1)
        self.qGridLayout4.addWidget(self.qPushButton14, 0, 0)
        self.qGridLayout4.addWidget(self.qPushButton15, 0, 1)
        self.qGridLayout4.addWidget(self.qPushButton16, 1, 0)
        self.qGridLayout4.addWidget(self.qPushButton17, 1, 1)
        self.qHBoxLayout.addWidget(self.qPushButton18)
        self.qHBoxLayout.addWidget(self.qPushButton19)

        self.qPushButton1.setObjectName("qPushButton1")
        self.qPushButton2.setObjectName("qPushButton2")
        self.qPushButton3.setObjectName("qPushButton3")
        self.qPushButton4.setObjectName("qPushButton4")
        self.qPushButton5.setObjectName("qPushButton5")
        self.qPushButton6.setObjectName("qPushButton6")
        self.qPushButton7.setObjectName("qPushButton7")
        self.qPushButton8.setObjectName("qPushButton8")
        self.qPushButton9.setObjectName("qPushButton9")
        self.qPushButton10.setObjectName("qPushButton10")
        self.qPushButton11.setObjectName("qPushButton11")
        self.qPushButton12.setObjectName("qPushButton12")
        self.qPushButton13.setObjectName("qPushButton13")
        self.qPushButton14.setObjectName("qPushButton14")
        self.qPushButton15.setObjectName("qPushButton15")
        self.qPushButton16.setObjectName("qPushButton16")
        self.qPushButton17.setObjectName("qPushButton17")
        self.qPushButton18.setObjectName("qPushButton18")
        self.qPushButton19.setObjectName("qPushButton19")

        self.qPushButton18.clicked.connect(self.qPlainTextEdit.clear)
        self.qPushButton19.clicked.connect(qDialog.close)
        QtCore.QMetaObject.connectSlotsByName(qDialog)


class QmyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_qPushButton1_clicked(self):
        curPath = QDir.currentPath()
        dlgTitle = "选择一个文件"
        filt = "所有文件(*.*);;文本文件(*.txt);;图片文件(*.jpg *.gif *.png)"
        filename, filtUsed = QFileDialog.getOpenFileName(self, dlgTitle, curPath, filt)
        self.ui.qPlainTextEdit.appendPlainText(filename)
        self.ui.qPlainTextEdit.appendPlainText("\n" + filtUsed)

    @pyqtSlot()
    def on_qPushButton2_clicked(self):
        curPath = QDir.currentPath()
        dlgTitle = "选择一个文件"
        filt = "所有文件(*.*);;文本文件(*.txt);;图片文件(*.jpg *.gif *.png)"
        fileList, filtUsed = QFileDialog.getOpenFileNames(self, dlgTitle, curPath, filt)
        for i in fileList:
            self.ui.qPlainTextEdit.appendPlainText(i)
        self.ui.qPlainTextEdit.appendPlainText("\n" + filtUsed)

    @pyqtSlot()
    def on_qPushButton3_clicked(self):
        curPath = QDir.currentPath()
        dlgTitle = "选择一个目录"
        selectedDir = QFileDialog.getExistingDirectory(self, dlgTitle, curPath, QFileDialog.ShowDirsOnly)
        self.ui.qPlainTextEdit.appendPlainText("\n" + selectedDir)

    @pyqtSlot()
    def on_qPushButton4_clicked(self):
        curPath = QDir.currentPath()
        dlgTitle = "保存文件"
        filt = "所有文件(*.*);;文本文件(*.txt);;图片文件(*.jpg *.gif *.png)"
        filename, filtUsed = QFileDialog.getSaveFileName(self, dlgTitle, curPath, filt)
        self.ui.qPlainTextEdit.appendPlainText(filename)
        self.ui.qPlainTextEdit.appendPlainText("\n" + filtUsed)

    @pyqtSlot()
    def on_qPushButton5_clicked(self):
        pal = self.ui.qPlainTextEdit.palette()
        iniColor = pal.color(QPalette.Text)
        color = QColorDialog.getColor(iniColor, self, "选择颜色")
        if color.isValid():
            pal.setColor(QPalette.Text, color)
            self.ui.qPlainTextEdit.setPalette(pal)

    @pyqtSlot()
    def on_qPushButton6_clicked(self):
        iniFont = self.ui.qPlainTextEdit.font()
        font, OK = QFontDialog.getFont(iniFont)
        if OK:
            self.ui.qPlainTextEdit.setFont(font)

    @pyqtSlot()
    def on_qPushButton7_clicked(self):
        labText = "正在复制文件..."
        btnText = "取消"
        minV = 0
        maxV = 200
        dlgProgress = QProgressDialog(labText, btnText, minV, maxV, self)
        dlgProgress.canceled.connect(self.do_progress_cancled)

        dlgProgress.setWindowTitle("复制文件")
        dlgProgress.setWindowModality(Qt.WindowModal)
        dlgProgress.setAutoReset(True)
        dlgProgress.setAutoClose(True)

        msCounter = QTime()
        for i in range(minV, maxV + 1):
            dlgProgress.setValue(i)
            dlgProgress.setLabelText("正在复制文件，第 %d 个" % i)
            msCounter.start()
            while (msCounter.elapsed() < 30):
                None
            if (dlgProgress.wasCanceled()):
                break

    def do_progress_cancled(self):
        self.ui.qPlainTextEdit.appendPlainText("**进度对话框被取消了**")

    @pyqtSlot()
    def on_qPushButton8_clicked(self):
        dlgTitle = "Question消息框"
        strInfo = "文件已被修改，是否保存修改？"
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                      defaultBtn)
        if result == QMessageBox.Yes:
            self.ui.qPlainTextEdit.appendPlainText("Question消息框：Yes 被选择")
        elif result == QMessageBox.No:
            self.ui.qPlainTextEdit.appendPlainText("Question消息框：No 被选择")
        elif result == QMessageBox.Cancel:
            self.ui.qPlainTextEdit.appendPlainText("Question消息框：Cancel 被选择")
        else:
            self.ui.qPlainTextEdit.appendPlainText("Question消息框：无选择")

    @pyqtSlot()
    def on_qPushButton9_clicked(self):
        dlgTitle = "information消息框"
        strInfo = "文件已被正确打开"
        QMessageBox.information(self, dlgTitle, strInfo)

    @pyqtSlot()
    def on_qPushButton10_clicked(self):
        dlgTitle = "warning消息框"
        strInfo = "文件内容已经被修改"
        QMessageBox.warning(self, dlgTitle, strInfo)

    @pyqtSlot()
    def on_qPushButton11_clicked(self):
        dlgTitle = "critical消息框"
        strInfo = "出现严重错误，程序将关闭"
        QMessageBox.critical(self, dlgTitle, strInfo)

    @pyqtSlot()
    def on_qPushButton12_clicked(self):
        dlgTitle = "about消息框"
        strInfo = "Python Qt GUI与数据可视化编程\n保留所有版权"
        QMessageBox.about(self, dlgTitle, strInfo)

    @pyqtSlot()
    def on_qPushButton13_clicked(self):
        dlgTitle = "aboutQt消息框"
        QMessageBox.aboutQt(self, dlgTitle)

    @pyqtSlot()
    def on_qPushButton14_clicked(self):
        dlgTitle = "输入文字对话框"
        txtLabel = "请输入文件名"
        defaultInput = "新建文件.txt"
        echoMode = QLineEdit.Normal

        text, OK = QInputDialog.getText(self, dlgTitle, txtLabel, echoMode, defaultInput)
        if (OK):
            self.ui.qPlainTextEdit.appendPlainText(text)

    @pyqtSlot()
    def on_qPushButton15_clicked(self):
        dlgTitle = "输入整数对话框"
        txtLabel = "设置字体大小"
        defaultValue = self.ui.qPlainTextEdit.font().pointSize()
        minValue = 6
        maxValue = 50
        stepValue = 1
        inputValue, OK = QInputDialog.getInt(self, dlgTitle, txtLabel, defaultValue, minValue, maxValue, stepValue)
        if OK:
            font = self.ui.qPlainTextEdit.font()
            font.setPointSize(inputValue)
            self.ui.qPlainTextEdit.setFont(font)

    @pyqtSlot()
    def on_qPushButton16_clicked(self):
        dlgTitle = "输入浮点数对话框"
        txtLabel = "输入一个浮点数"
        defaultValue = 3.65
        minValue = 0
        maxValue = 10000
        decimals = 2
        inputValue, OK = QInputDialog.getDouble(self, dlgTitle, txtLabel, defaultValue, minValue, maxValue, decimals)
        if OK:
            text = "输入了一个浮点数：%.2f" % inputValue
            self.ui.qPlainTextEdit.appendPlainText(text)

    @pyqtSlot()
    def on_qPushButton17_clicked(self):
        dlgTitle = "条目选择对话框"
        txtLabel = "请选择级别"
        curIndex = 0
        editable = True
        items = ["优秀", "良好", "合格", "不合格"]
        text, OK = QInputDialog.getItem(self, dlgTitle, txtLabel, items, curIndex, editable)
        if OK:
            self.ui.qPlainTextEdit.appendPlainText(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyDialog()
    mw.show()
    sys.exit(app.exec_())
