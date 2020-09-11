import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QDir, QFile, QIODevice, QTextStream
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 445)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(125, 55, 391, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 685, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actQFile_Open = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/122.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQFile_Open.setIcon(icon)
        self.actQFile_Open.setObjectName("actQFile_Open")
        self.actStream_Open = QtWidgets.QAction(MainWindow)
        self.actStream_Open.setIcon(icon)
        self.actStream_Open.setObjectName("actStream_Open")
        self.actQuit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuit.setIcon(icon1)
        self.actQuit.setObjectName("actQuit")
        self.actQFile_Save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/104.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQFile_Save.setIcon(icon2)
        self.actQFile_Save.setObjectName("actQFile_Save")
        self.actStream_Save = QtWidgets.QAction(MainWindow)
        self.actStream_Save.setIcon(icon2)
        self.actStream_Save.setObjectName("actStream_Save")
        self.actPY_Open = QtWidgets.QAction(MainWindow)
        self.actPY_Open.setIcon(icon)
        self.actPY_Open.setObjectName("actPY_Open")
        self.actPY_Save = QtWidgets.QAction(MainWindow)
        self.actPY_Save.setIcon(icon2)
        self.actPY_Save.setObjectName("actPY_Save")
        self.mainToolBar.addAction(self.actQFile_Open)
        self.mainToolBar.addAction(self.actQFile_Save)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actStream_Open)
        self.mainToolBar.addAction(self.actStream_Save)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actPY_Open)
        self.mainToolBar.addAction(self.actPY_Save)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo9_1，文本文件读写"))
        self.actQFile_Open.setText(_translate("MainWindow", "QFile打开"))
        self.actQFile_Open.setToolTip(_translate("MainWindow", "用QFile打开文本文件"))
        self.actStream_Open.setText(_translate("MainWindow", "Stream打开"))
        self.actStream_Open.setToolTip(_translate("MainWindow", "用QtextStream打开文本文件"))
        self.actQuit.setText(_translate("MainWindow", "退出"))
        self.actQuit.setToolTip(_translate("MainWindow", "退出"))
        self.actQFile_Save.setText(_translate("MainWindow", "QFile另存"))
        self.actQFile_Save.setToolTip(_translate("MainWindow", "用QFile直接另存文件"))
        self.actStream_Save.setText(_translate("MainWindow", "Stream另存"))
        self.actStream_Save.setToolTip(_translate("MainWindow", "用QTextStream另存文件"))
        self.actPY_Open.setText(_translate("MainWindow", "Python打开"))
        self.actPY_Open.setToolTip(_translate("MainWindow", "使用Python内置功能打开"))
        self.actPY_Save.setText(_translate("MainWindow", "Python另存"))
        self.actPY_Save.setToolTip(_translate("MainWindow", "采用Python内置功能另存"))


import rec.res_rc_0901

class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setCentralWidget(self.ui.textEdit)

    def __openByIODevice(self, fileName):
        fileDevice = QFile(fileName)
        if not fileDevice.exists():
            return False
        if not fileDevice.open(QIODevice.ReadOnly | QIODevice.Text):
            return False

        try:
            self.ui.textEdit.clear()
            while not fileDevice.atEnd():
                qtBytes = fileDevice.readLine()
                pyBytes = bytes(qtBytes.data())
                lineStr = pyBytes.decode("utf-8")
                lineStr = lineStr.strip()
                self.ui.textEdit.appendPlainText(lineStr)
        finally:
            fileDevice.close()

        return True


    def __saveByIODevice(self, fileName):
        fileDevice = QFile(fileName)
        if not fileDevice.open(QIODevice.ReadOnly | QIODevice.Text):
            return False

        try:
            text = self.ui.textEdit.toPlainText()
            strBytes = text.encode("utf-8")
            fileDevice.write(strBytes)
        finally:
            fileDevice.close()

        return True

    def __openByStream(self, fileName):
        fileDevice = QFile(fileName)
        if not fileDevice.exists():
            return False

        if not fileDevice.open(QIODevice.ReadOnly | QIODevice.Text):
            return False

        try:
            fileStream = QTextStream(fileDevice)
            fileStream.setAutoDetectUnicode(True)
            fileStream.setCodec("utf-8")

            self.ui.textEdit.clear()
            while not fileStream.atEnd():
                lineStr = fileStream.readLine()
                self.ui.textEdit.appendPlainText(lineStr)

        finally:
            fileDevice.close()
        return True

    def __saveByStream(self, fileName):
        fileDevice = QFile(fileName)
        if not fileDevice.exists():
            return False

        if not fileDevice.open(QIODevice.ReadOnly | QIODevice.Text):
            return False

        try:
            fileStream = QTextStream(fileDevice)
            fileStream.setAutoDetectUnicode(True)
            fileStream.setCodec("utf-8")

            text = self.ui.textEdit.toPlainText()
            fileStream << text

        finally:
            fileDevice.close()
        return True

    @pyqtSlot()
    def on_actQFile_Open_triggered(self):
        curPath = QDir.currentPath()
        title = "打开一个文件"
        filt = "程序文件(*.h *.cpp *.py);;文本文件(*.txt);;所有文件(*.*)"
        fileName,flt = QFileDialog.getOpenFileName(self, title, curPath, filt)
        if(fileName == ""):
            return
        if self.__openByIODevice(fileName):
            self.ui.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self,"错误","打开文件失败")

    @pyqtSlot()
    def on_actQFile_Save_triggered(self):
        curPath = QDir.currentPath()
        title = "另存为一个文件"
        filt = "Python程序(*.py);;C++程序(*.h *.cpp);;文本文件(*.txt);;所有文件(*.*)"
        fileName , flt = QFileDialog.getSaveFileName(self, title, curPath, filt)
        if(fileName == ""):
            return
        if self.__saveByIODevice(fileName):
            self.ui.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self, "错误", "保存文件失败")

    @pyqtSlot()
    def on_actStream_Open_triggered(self):
        curPath = QDir.currentPath()
        title = "打开一个文件"
        filt = "程序文件(*.h *.cpp *.py);;文本文件(*.txt);;所有文件(*.*)"
        fileName, flt = QFileDialog.getOpenFileName(self, title, curPath, filt)
        if(fileName==""):
            return

        if self.__openByStream(fileName):
            self.ui.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self, "错误", "打开文件失败")

    @pyqtSlot()
    def on_actStream_Save_triggered(self):
        curPath = QDir.currentPath()
        title = "另存为一个文件"
        filt = "Python程序(*.py);;C++程序(*.h *.cpp);;文本文件(*.txt);;所有文件(*.*)"
        fileName, flt = QFileDialog.getSaveFileName(self, title, curPath, filt)
        if (fileName == ""):
            return
        if self.__saveByStream(fileName):
            self.ui.statusBar.showMessage(fileName)
        else:
            QMessageBox.critical(self, "错误", "保存文件失败")

    @pyqtSlot()
    def on_actPY_Open_triggered(self):
        curPath = QDir.currentPath()
        title = "打开一个文件"
        filt = "程序文件(*.h *.cpp *.py);;文本文件(*.txt);;所有文件(*.*)"
        fileName, flt = QFileDialog.getOpenFileName(self, title, curPath, filt)
        if (fileName == ""):
            return

        self.ui.textEdit.clear()
        fileDevice = open(fileName, mode='r', encoding='utf-8')
        try:
            for eachLine in fileDevice:
                lineStr = eachLine.strip()
                self.ui.textEdit.appendPlainText(lineStr)
            self.ui.statusBar.showMessage(fileName)
        finally:
            fileDevice.close()

    @pyqtSlot()
    def on_actPY_Save_triggered(self):
        curPath = QDir.currentPath()
        title = "另存为一个文件"
        filt = "Python程序(*.py);;C++程序(*.h *.cpp);;文本文件(*.txt);;所有文件(*.*)"
        fileName, flt = QFileDialog.getSaveFileName(self, title, curPath, filt)
        if (fileName == ""):
            return

        text = self.ui.textEdit.toPlainText()
        fileDevice = open(fileName, mode='w', encoding='utf-8')
        try:
            fileDevice.write(text)
            self.ui.statusBar.showMessage(fileName)
        finally:
            fileDevice.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )