import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(876, 513)
        self.qWidget = QtWidgets.QWidget(qMainWindow)
        self.qVBoxLayout1 = QtWidgets.QVBoxLayout(self.qWidget)
        self.qGroupBox1 = QtWidgets.QGroupBox(self.qWidget)
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


        qMainWindow.setCentralWidget(self.qWidget)



class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )
