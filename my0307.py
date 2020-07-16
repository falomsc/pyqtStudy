'''
目前问题：
1，on_qPlainTextEdit_customContextMenuRequested不知道如何触发
2，为什么是qActionGroup而不是self.qActionGroup

总结：
1，QMenuBar增加QMenu用addMenu方法即可，原代码用addAction方法
2，注意on_qPlainTextEdit_copyAvailable方法，设置剪切复制粘贴三个按钮的enabled状态
3，注意on_qPlainTextEdit_selectionChanged方法，设置选中字体时粗体斜体下划线按钮的checked状态
4，信号connect槽函数，[bool]也可以写成["bool"]
5，注意__init__函数中self.setCentralWidget(self.ui.qPlainTextEdit)，改变了布局


'''
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime, QTimer, QSize, QRect, pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap, QImage, QFont


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(743, 379)
        self.centralWidget = QtWidgets.QWidget(qMainWindow)
        self.qPlainTextEdit = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.qPlainTextEdit.setGeometry(QRect(45, 25, 476, 221))
        font = QFont()
        font.setPointSize(12)
        self.qPlainTextEdit.setFont(font)
        self.qMenuBar = QtWidgets.QMenuBar(qMainWindow)
        self.qMenuBar.setGeometry(QRect(0, 0, 743, 23))
        self.qToolBar = QtWidgets.QToolBar(qMainWindow)
        self.qToolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        self.qMenu1 = QtWidgets.QMenu(self.qMenuBar)
        self.qMenu1.setTitle("文件(&F)")
        self.qMenu2 = QtWidgets.QMenu(self.qMenuBar)
        self.qMenu2.setTitle("编辑(&E)")
        self.qMenu3 = QtWidgets.QMenu(self.qMenuBar)
        self.qMenu3.setTitle("格式(&M)")
        self.qMenu4 = QtWidgets.QMenu(self.qMenuBar)
        self.qMenu4.setTitle("界面语言")

        self.qAction1 = QtWidgets.QAction(qMainWindow)
        self.qAction1.setIcon(QIcon("./image/100.bmp"))
        self.qAction1.setText("新建")
        self.qAction1.setShortcut("Ctrl+N")
        self.qAction1.setToolTip("新建文件")
        self.qAction2 = QtWidgets.QAction(qMainWindow)
        self.qAction2.setIcon(QIcon("./image/122.bmp"))
        self.qAction2.setText("打开...")
        self.qAction2.setShortcut("Ctrl+O")
        self.qAction2.setToolTip("打开文件")
        self.qAction3 = QtWidgets.QAction(qMainWindow)
        self.qAction3.setIcon(QIcon("./image/104.bmp"))
        self.qAction3.setText("保存")
        self.qAction3.setShortcut("Ctrl+S")
        self.qAction3.setToolTip("保存修改")
        self.qAction4 = QtWidgets.QAction(qMainWindow)
        self.qAction4.setIcon(QIcon("./image/132.bmp"))
        self.qAction4.setText("关闭")
        self.qAction4.setToolTip("关闭本窗口")
        self.qAction5 = QtWidgets.QAction(qMainWindow)
        self.qAction5.setIcon(QIcon("./image/200.bmp"))
        self.qAction5.setText("剪切")
        self.qAction5.setShortcut("Ctrl+X")
        self.qAction5.setToolTip("剪切到粘贴板")
        self.qAction5.setEnabled(False)
        self.qAction6 = QtWidgets.QAction(qMainWindow)
        self.qAction6.setIcon(QIcon("./image/202.bmp"))
        self.qAction6.setText("复制")
        self.qAction6.setShortcut("Ctrl+C")
        self.qAction6.setToolTip("复制到粘贴板")
        self.qAction6.setEnabled(False)
        self.qAction7 = QtWidgets.QAction(qMainWindow)
        self.qAction7.setIcon(QIcon("./image/204.bmp"))
        self.qAction7.setText("粘贴")
        self.qAction7.setShortcut("Ctrl+V")
        self.qAction7.setToolTip("从粘贴板粘贴")
        self.qAction7.setEnabled(False)
        self.qAction8 = QtWidgets.QAction(qMainWindow)
        self.qAction8.setIcon(QIcon("./image/206.bmp"))
        self.qAction8.setText("撤销")
        self.qAction8.setShortcut("Ctrl+Z")
        self.qAction8.setToolTip("撤销上次编辑操作")
        self.qAction8.setEnabled(False)
        self.qAction9 = QtWidgets.QAction(qMainWindow)
        self.qAction9.setIcon(QIcon("./image/208.bmp"))
        self.qAction9.setText("重做")
        self.qAction9.setShortcut("Ctrl+Y")
        self.qAction9.setToolTip("重做上次操作")
        self.qAction9.setEnabled(False)
        self.qAction10 = QtWidgets.QAction(qMainWindow)
        self.qAction10.setText("全选")
        self.qAction10.setShortcut("Ctrl+A")
        self.qAction10.setToolTip("全选")
        self.qAction11 = QtWidgets.QAction(qMainWindow)
        self.qAction11.setIcon(QIcon("./image/212.bmp"))
        self.qAction11.setText("清空")
        self.qAction11.setToolTip("清空")
        self.qAction12 = QtWidgets.QAction(qMainWindow)
        self.qAction12.setIcon(QIcon("./image/500.bmp"))
        self.qAction12.setText("粗体")
        self.qAction12.setToolTip("粗体")
        self.qAction12.setCheckable(True)
        self.qAction13 = QtWidgets.QAction(qMainWindow)
        self.qAction13.setIcon(QIcon("./image/502.bmp"))
        self.qAction13.setText("斜体")
        self.qAction13.setToolTip("斜体")
        self.qAction13.setCheckable(True)
        self.qAction14 = QtWidgets.QAction(qMainWindow)
        self.qAction14.setIcon(QIcon("./image/504.bmp"))
        self.qAction14.setText("下划线")
        self.qAction14.setToolTip("下划线")
        self.qAction14.setCheckable(True)
        self.qAction15 = QtWidgets.QAction(qMainWindow)
        self.qAction15.setText("显示工具栏文字")
        self.qAction15.setToolTip("显示工具栏文字")
        self.qAction15.setCheckable(True)
        self.qAction15.setChecked(True)
        self.qAction16 = QtWidgets.QAction(qMainWindow)
        self.qAction16.setIcon(QIcon("./image/CN.jpg"))
        self.qAction16.setText("汉语")
        self.qAction16.setToolTip("汉语界面")
        self.qAction16.setCheckable(True)
        self.qAction16.setChecked(True)
        self.qAction17 = QtWidgets.QAction(qMainWindow)
        self.qAction17.setIcon(QIcon("./image/timg2.jpg"))
        self.qAction17.setText("英语")
        self.qAction17.setToolTip("英语")
        self.qAction17.setCheckable(True)

        qMainWindow.setCentralWidget(self.centralWidget)
        qMainWindow.setMenuBar(self.qMenuBar)
        qMainWindow.addToolBar(self.qToolBar)
        qMainWindow.setStatusBar(self.qStatusBar)
        self.qMenuBar.addMenu(self.qMenu1)
        self.qMenuBar.addMenu(self.qMenu2)
        self.qMenuBar.addMenu(self.qMenu3)
        # self.qMenuBar.addAction(self.qMenu1.menuAction())
        # self.qMenuBar.addAction(self.qMenu2.menuAction())
        # self.qMenuBar.addAction(self.qMenu3.menuAction())
        self.qMenu1.addAction(self.qAction1)
        self.qMenu1.addAction(self.qAction2)
        self.qMenu1.addAction(self.qAction3)
        self.qMenu1.addSeparator()
        self.qMenu1.addAction(self.qAction4)
        self.qMenu2.addAction(self.qAction5)
        self.qMenu2.addAction(self.qAction6)
        self.qMenu2.addAction(self.qAction7)
        self.qMenu2.addSeparator()
        self.qMenu2.addAction(self.qAction8)
        self.qMenu2.addAction(self.qAction9)
        self.qMenu2.addSeparator()
        self.qMenu2.addAction(self.qAction10)
        self.qMenu2.addAction(self.qAction11)
        self.qMenu3.addAction(self.qAction12)
        self.qMenu3.addAction(self.qAction13)
        self.qMenu3.addAction(self.qAction14)
        self.qMenu3.addSeparator()
        self.qMenu3.addAction(self.qAction15)
        self.qMenu3.addMenu(self.qMenu4)
        self.qMenu4.addAction(self.qAction16)
        self.qMenu4.addAction(self.qAction17)
        self.qToolBar.addAction(self.qAction1)
        self.qToolBar.addAction(self.qAction2)
        self.qToolBar.addAction(self.qAction3)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction5)
        self.qToolBar.addAction(self.qAction6)
        self.qToolBar.addAction(self.qAction7)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction8)
        self.qToolBar.addAction(self.qAction9)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction12)
        self.qToolBar.addAction(self.qAction13)
        self.qToolBar.addAction(self.qAction14)
        self.qToolBar.addSeparator()
        self.qToolBar.addAction(self.qAction16)
        self.qToolBar.addAction(self.qAction17)
        self.qToolBar.addSeparator()

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
        self.qAction12.setObjectName("qAction12")
        self.qAction13.setObjectName("qAction13")
        self.qAction14.setObjectName("qAction14")
        self.qAction15.setObjectName("qAction15")
        self.qAction16.setObjectName("qAction16")
        self.qAction17.setObjectName("qAction17")
        self.qPlainTextEdit.setObjectName("qPlainTextEdit")
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)

        ############################  Init  ##################################
        self.qPlainTextEdit.setPlainText("你好世界")
        self.qAction4.triggered.connect(qMainWindow.close)
        self.qAction5.triggered.connect(self.qPlainTextEdit.cut)
        self.qAction6.triggered.connect(self.qPlainTextEdit.copy)
        self.qAction7.triggered.connect(self.qPlainTextEdit.paste)
        self.qAction8.triggered.connect(self.qPlainTextEdit.undo)
        self.qAction9.triggered.connect(self.qPlainTextEdit.redo)
        self.qAction10.triggered.connect(self.qPlainTextEdit.selectAll)
        self.qAction11.triggered.connect(self.qPlainTextEdit.clear)
        self.qPlainTextEdit.undoAvailable[bool].connect(self.qAction8.setEnabled)
        self.qPlainTextEdit.redoAvailable[bool].connect(self.qAction9.setEnabled)


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__qLabel1 = QtWidgets.QLabel(self)
        self.__qLabel1.setText("文件名：")
        self.__qLabel1.setMinimumWidth(150)
        self.ui.qStatusBar.addWidget(self.__qLabel1)
        self.__qProgressBar = QtWidgets.QProgressBar(self)
        self.__qProgressBar.setMaximumWidth(200)
        self.__qProgressBar.setMaximum(50)
        self.__qProgressBar.setMinimum(5)
        self.ui.qStatusBar.addWidget(self.__qProgressBar)
        sz = self.ui.qPlainTextEdit.font().pointSize()
        self.__qProgressBar.setValue(sz)
        self.__qLabel2 = QtWidgets.QLabel(self)
        self.__qLabel2.setText("选择字体名称")
        self.ui.qStatusBar.addPermanentWidget(self.__qLabel2)
        qActionGroup = QtWidgets.QActionGroup(self)
        qActionGroup.addAction(self.ui.qAction16)
        qActionGroup.addAction(self.ui.qAction17)
        qActionGroup.setExclusive(True)
        self.__qSpinBox = QtWidgets.QSpinBox(self)
        self.__qSpinBox.setMinimum(5)
        self.__qSpinBox.setMaximum(50)
        self.__qSpinBox.setValue(sz)
        self.__qSpinBox.setMinimumWidth(50)
        self.ui.qToolBar.addWidget(self.__qSpinBox)
        self.__qFontComboBox = QtWidgets.QFontComboBox(self)
        self.__qFontComboBox.setMinimumWidth(100)
        self.ui.qToolBar.addWidget(self.__qFontComboBox)
        self.ui.qToolBar.addSeparator()
        self.ui.qToolBar.addAction(self.ui.qAction4)
        self.setCentralWidget(self.ui.qPlainTextEdit)

        self.__qSpinBox.valueChanged[int].connect(self.do_fontSize_Changed)
        self.__qFontComboBox.currentIndexChanged[str].connect(self.do_fontName_Changed)

    @pyqtSlot(bool)
    def on_qAction12_triggered(self, checked):
        font = self.ui.qPlainTextEdit.currentCharFormat()
        if checked == True:
            font.setFontWeight(QFont.Bold)
        else:
            font.setFontWeight(QFont.Normal)
        self.ui.qPlainTextEdit.mergeCurrentCharFormat(font)

    @pyqtSlot(bool)
    def on_qAction13_triggered(self, checked):
        font = self.ui.qPlainTextEdit.currentCharFormat()
        font.setFontItalic(checked)
        self.ui.qPlainTextEdit.mergeCurrentCharFormat(font)

    @pyqtSlot(bool)
    def on_qAction14_triggered(self, checked):
        font = self.ui.qPlainTextEdit.currentCharFormat()
        font.setFontUnderline(checked)
        self.ui.qPlainTextEdit.mergeCurrentCharFormat(font)

    def on_qPlainTextEdit_copyAvailable(self, yes):
        self.ui.qAction5.setEnabled(yes)
        self.ui.qAction6.setEnabled(yes)
        self.ui.qAction7.setEnabled(self.ui.qPlainTextEdit.canPaste())

    def on_qPlainTextEdit_selectionChanged(self):
        font = self.ui.qPlainTextEdit.currentCharFormat()
        self.ui.qAction12.setChecked(font.font().bold())
        self.ui.qAction13.setChecked(font.fontItalic())
        self.ui.qAction14.setChecked(font.fontUnderline())

    def on_qPlainTextEdit_customContextMenuRequested(self, pos):
        popmenu = self.ui.qPlainTextEdit.createStandardContextMenu()
        popmenu.exec(pos)

    @pyqtSlot(bool)
    def on_qAction15_triggered(self, checked):
        if checked:
            st = Qt.ToolButtonTextUnderIcon
        else:
            st = Qt.ToolButtonIconOnly
        self.ui.qToolBar.setToolButtonStyle(st)

    def on_qAction1_triggered(self):
        self.__qLabel1.setText("新建文件")

    def on_qAction2_triggered(self):
        self.__qLabel1.setText("打开的文件")

    def on_qAction3_triggered(self):
        self.__qLabel1.setText("文件已保存")

    @pyqtSlot(int)
    def do_fontSize_Changed(self, fontSize):
        font = self.ui.qPlainTextEdit.currentCharFormat()
        font.setFontPointSize(fontSize)
        self.ui.qPlainTextEdit.mergeCurrentCharFormat(font)
        self.__qProgressBar.setValue(fontSize)

    @pyqtSlot(str)
    def do_fontName_Changed(self, fontName):
        font = self.ui.qPlainTextEdit.currentCharFormat()
        font.setFontFamily(fontName)
        self.ui.qPlainTextEdit.mergeCurrentCharFormat(font)
        self.__qLabel2.setText("字体名称：%s" % fontName)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_())