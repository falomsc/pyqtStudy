import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QDir, QSize
from PyQt5.QtWidgets import QFrame, QFileSystemModel


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(876, 513)
        self.qWidget = QtWidgets.QWidget(qMainWindow)
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(self.qWidget)
        self.qGroupBox1 = QtWidgets.QGroupBox(self.qWidget)
        self.qGroupBox1.setMaximumSize(QSize(16777215, 75))
        self.qVBoxLayout2 = QtWidgets.QVBoxLayout(self.qGroupBox1)
        self.qSplitter1 = QtWidgets.QSplitter(self.qWidget)
        self.qSplitter1.setOrientation(Qt.Horizontal)
        self.qVBoxLayout1.addWidget(self.qSplitter1)
        self.qVBoxLayout1.addWidget(self.qGroupBox1)

        self.qHBoxLayout = QtWidgets.QHBoxLayout(self.qGroupBox1)
        self.qFrame = QtWidgets.QFrame(self.qGroupBox1)
        self.qLabel1 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel1.setText("路径名：")
        self.qFrame.setFrameShape(QFrame.HLine)
        self.qFrame.setFrameShadow(QFrame.Sunken)
        self.qVBoxLayout2.addLayout(self.qHBoxLayout)
        self.qVBoxLayout2.addWidget(self.qFrame)
        self.qVBoxLayout2.addWidget(self.qLabel1)

        self.qLabel2 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel2.setText("文件名：")
        self.qLabel3 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel3.setText("文件大小：")
        self.qLabel4 = QtWidgets.QLabel(self.qGroupBox1)
        self.qLabel4.setText("节点类型：")
        self.qCheckBox = QtWidgets.QCheckBox(self.qGroupBox1)
        self.qCheckBox.setText("节点是目录")
        self.qHBoxLayout.addWidget(self.qLabel2)
        self.qHBoxLayout.addWidget(self.qLabel3)
        self.qHBoxLayout.addWidget(self.qLabel4)
        self.qHBoxLayout.addWidget(self.qCheckBox)

        self.qGroupBox2 = QtWidgets.QGroupBox(self.qSplitter1)
        self.qGroupBox2.setTitle("TreeView")
        self.qSplitter2 = QtWidgets.QSplitter(self.qSplitter1)
        self.qSplitter2.setOrientation(Qt.Vertical)
        self.qVBoxLayout3 = QtWidgets.QVBoxLayout(self.qGroupBox2)
        self.qTreeView = QtWidgets.QTreeView(self.qGroupBox2)
        self.qVBoxLayout3.addWidget(self.qTreeView)
        self.qGroupBox3 = QtWidgets.QGroupBox(self.qSplitter2)
        self.qGroupBox3.setTitle("ListView")
        self.qVBoxLayout4 = QtWidgets.QVBoxLayout(self.qGroupBox3)
        self.qListView = QtWidgets.QListView(self.qGroupBox3)
        self.qListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.qVBoxLayout4.addWidget(self.qListView)
        self.qGroupBox4 = QtWidgets.QGroupBox(self.qSplitter2)
        self.qGroupBox4.setTitle("TableView")
        self.qVBoxLayout5 = QtWidgets.QVBoxLayout(self.qGroupBox4)
        self.qTableView = QtWidgets.QTableView(self.qGroupBox4)
        self.qVBoxLayout5.addWidget(self.qTableView)

        self.qTreeView.setObjectName("qTreeView")
        qMainWindow.setCentralWidget(self.qWidget)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)



class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = QFileSystemModel(self)
        self.model.setRootPath(QDir.currentPath())
        self.ui.qTreeView.setModel(self.model)
        self.ui.qListView.setModel(self.model)
        self.ui.qTableView.setModel(self.model)

        self.ui.qTreeView.clicked.connect(self.ui.qListView.setRootIndex)
        self.ui.qTreeView.clicked.connect(self.ui.qTableView.setRootIndex)

    def on_qTreeView_clicked(self, index):
        self.ui.qCheckBox.setChecked(self.model.isDir(index))
        self.ui.qLabel1.setText(self.model.filePath(index))
        self.ui.qLabel4.setText(self.model.type(index))
        self.ui.qLabel2.setText(self.model.fileName(index))
        fileSize = self.model.size(index)/1024
        if(fileSize<1024):
            self.ui.qLabel3.setText("%d KB" % fileSize)
        else:
            self.ui.qLabel3.setText("%.2f MB" % (fileSize/1024))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )
