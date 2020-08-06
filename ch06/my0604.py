import codecs
import sys, os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QItemSelectionModel, pyqtSlot, QStringListModel, pyqtSignal
from PyQt5.QtGui import QIcon, QStandardItemModel, QPixmap, QPainter
from PyQt5.QtWidgets import QAbstractItemView, QLabel, QMainWindow, QDialog, QWidget, QToolBar, QVBoxLayout, \
    QFileDialog, QFontDialog, QMdiArea


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(678, 454)
        self.qWidget = QtWidgets.QWidget(qMainWindow)
        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        qMainWindow.setCentralWidget(self.qWidget)
        qMainWindow.addToolBar(self.qToolBar)
        qMainWindow.setStatusBar(self.qStatusBar)
        self.qMdiArea = QtWidgets.QMdiArea(self.qWidget)
        self.qAction1 = QtWidgets.QAction(QIcon("../image/100.bmp"), "新建文档", self.qToolBar)
        self.qAction2 = QtWidgets.QAction(QIcon("../image/132.bmp"), "退出", self.qToolBar)
        self.qAction3 = QtWidgets.QAction(QIcon("../image/122.bmp"), "打开文档", self.qToolBar)
        self.qAction4 = QtWidgets.QAction(QIcon("../image/506.bmp"), "字体设置", self.qToolBar)
        self.qAction4.setEnabled(False)
        self.qAction5 = QtWidgets.QAction(QIcon("../image/200.bmp"), "剪切", self.qToolBar)
        self.qAction5.setEnabled(False)
        self.qAction6 = QtWidgets.QAction(QIcon("../image/202.bmp"), "复制", self.qToolBar)
        self.qAction6.setEnabled(False)
        self.qAction7 = QtWidgets.QAction(QIcon("../image/204.bmp"), "粘贴", self.qToolBar)
        self.qAction7.setEnabled(False)
        self.qAction8 = QtWidgets.QAction(QIcon("../image/230.bmp"), "MDI模式", self.qToolBar)
        self.qAction8.setCheckable(True)
        self.qAction9 = QtWidgets.QAction(QIcon("../image/400.bmp"), "级联展开", self.qToolBar)
        self.qAction10 = QtWidgets.QAction(QIcon("../image/406.bmp"), "平铺展开", self.qToolBar)
        self.qAction11 = QtWidgets.QAction(QIcon("../image/128.bmp"), "关闭所有窗口", self.qToolBar)
        self.qToolBar.addAction(self.qAction1)
        self.qToolBar.addAction(self.qAction3)
        self.qToolBar.addAction(self.qAction11)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction5)
        self.qToolBar.addAction(self.qAction6)
        self.qToolBar.addAction(self.qAction7)
        self.qToolBar.addAction(self.qAction4)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction8)
        self.qToolBar.addAction(self.qAction9)
        self.qToolBar.addAction(self.qAction10)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction2)

        self.qAction1.setObjectName("qAction1")
        self.qAction2.setObjectName("qAction2")
        self.qAction3.setObjectName("qAction3")
        self.qAction4.setObjectName("qAction4")
        self.qAction5.setObjectName("qAction5")
        self.qAction6.setObjectName("qAction6")
        self.qAction7.setObjectName("qAction7")
        self.qAction8.setObjectName("qAction8")
        self.qAction9.setObjectName("qAction9")
        self.qAction10.setObjectName("qAction10")
        self.qAction11.setObjectName("qAction11")
        self.qMdiArea.setObjectName("qMdiArea")
        self.qAction2.triggered.connect(qMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)

class Ui_QWFormDoc():
    def setupUi(self, QWFormDoc):
        QWFormDoc.resize(666, 401)
        self.qVBoxLayout = QtWidgets.QVBoxLayout(QWFormDoc)
        self.qPlainTextEdit = QtWidgets.QPlainTextEdit(QWFormDoc)
        self.qPlainTextEdit.setObjectName("qPlainTextEdit")
        self.qVBoxLayout.addWidget(self.qPlainTextEdit)
        QtCore.QMetaObject.connectSlotsByName(QWFormDoc)




class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setCentralWidget(self.ui.qMdiArea)
        self.ui.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

    def closeEvent(self, event):
        self.ui.qMdiArea.closeAllSubWindows()
        event.accept()

    def __enableEditActions(self, enabled):
        self.ui.qAction4.setEnabled(enabled)
        self.ui.qAction5.setEnabled(enabled)
        self.ui.qAction6.setEnabled(enabled)
        self.ui.qAction7.setEnabled(enabled)

    @pyqtSlot()
    def on_qAction1_triggered(self):
        formDoc = QmyFormDoc(self)
        self.ui.qMdiArea.addSubWindow(formDoc)
        formDoc.show()
        self.__enableEditActions(True)

    @pyqtSlot()
    def on_qAction3_triggered(self):
        needNew = False
        if(len(self.ui.qMdiArea.subWindowList())>0):
            formDoc = self.ui.qMdiArea.activeSubWindow().widget()
            needNew = formDoc.isFileOpened()
        else:
            needNew = True
        curPath = os.getcwd()
        filename, flt = QFileDialog.getOpenFileName(self, "打开一个文件", curPath, "文本文件(*.cpp *.h *.py);;所有文件(*.*)")
        if(filename == ""):
            return
        if(needNew):
            formDoc = QmyFormDoc(self)
            self.ui.qMdiArea.addSubWindow(formDoc)

        formDoc.loadFromFile(filename)
        formDoc.show()
        self.__enableEditActions(True)

    @pyqtSlot()
    def on_qAction11_triggered(self):
        self.ui.qMdiArea.closeAllSubWindows()

    @pyqtSlot(bool)
    def on_qAction8_triggered(self, checked):
        if checked:
            self.ui.qMdiArea.setViewMode(QMdiArea.TabbedView)
            self.ui.qMdiArea.setTabsClosable(True)
            self.ui.qAction9.setEnabled(True)
            self.ui.qAction10.setEnabled(True)
        else:
            self.ui.qMdiArea.setViewMode(QMdiArea.SubWindowView)
            self.ui.qAction9.setEnabled(True)
            self.ui.qAction10.setEnabled(True)

    @pyqtSlot()
    def on_qAction9_triggered(self):
        self.ui.qMdiArea.cascadeSubWindows()

    @pyqtSlot()
    def on_qAction10_triggered(self):
        self.ui.qMdiArea.tileSubWindows()

    @pyqtSlot()
    def on_qAction5_triggered(self):
        formDoc = self.ui.qMdiArea.activeSubWindow().widget()
        formDoc.textCut()

    @pyqtSlot()
    def on_qAction6_triggered(self):
        formDoc = self.ui.qMdiArea.activeSubWindow().widget()
        formDoc.textCopy()

    @pyqtSlot()
    def on_qAction7_triggered(self):
        formDoc = self.ui.qMdiArea.activeSubWindow().widget()
        formDoc.textPaste()

    @pyqtSlot()
    def on_qAction4_triggered(self):
        formDoc = self.ui.qMdiArea.activeSubWindow().widget()
        formDoc.textSetFont()


    def on_qMdiArea_subWindowActivated(self, arg1):
        cnt = len(self.ui.qMdiArea.subWindowList())
        if(cnt == 0):
            self.__enableEditActions(False)
            self.ui.qStatusBar.clearMessage()
        else:
            formDoc = self.ui.qMdiArea.activeSubWindow().widget()
            self.ui.qStatusBar.showMessage(formDoc.currentFileName())



class QmyFormDoc(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormDoc()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.__currentFile = ""
        self.__fileOpened = False

    def __del__(self):
        print("QmyFormDoc 对象被删除了")

    def loadFromFile(self, aFileName):
        aFile = codecs.open(aFileName, encoding="utf-8")
        try:
            for eachLine in aFile:
                self.ui.qPlainTextEdit.appendPlainText(eachLine.strip())
        finally:
            aFile.close()

        self.__currentFile = aFileName
        self.__fileOpened = True

        baseFilename = os.path.basename(aFileName)
        self.setWindowTitle(baseFilename)

    def currentFileName(self):
        return self.__currentFile

    def isFileOpened(self):
        return self.__fileOpened

    def textCut(self):
        self.ui.qPlainTextEdit.cut()

    def textCopy(self):
        self.ui.qPlainTextEdit.copy()

    def textPaste(self):
        self.ui.qPlainTextEdit.paste()

    def textSetFont(self):
        iniFont = self.ui.qPlainTextEdit.font()
        font, OK = QFontDialog.getFont(iniFont)
        if(OK):
            self.ui.qPlainTextEdit.setFont(font)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    # mw = QmyFormDoc()
    mw.show()
    sys.exit(app.exec_(), )