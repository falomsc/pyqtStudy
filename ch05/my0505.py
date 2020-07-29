import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QEvent, QRect, QSize
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, qApp


class Ui_Widget():
    def setupUi(self, qWidget):
        qWidget.resize(468, 462)
        self.qPlainTextEdit = QtWidgets.QPlainTextEdit(qWidget)
        self.qPlainTextEdit.setGeometry(QRect(9, 9, 450, 140))
        self.qPlainTextEdit.setMinimumSize(QSize(0, 140))
        self.qLabel = QtWidgets.QLabel(qWidget)
        self.qLabel.setGeometry(QRect(9, 155, 450, 298))
        self.qLabel.setAcceptDrops(True)
        self.qLabel.setText("")
        self.qLabel.setPixmap(QPixmap("../image/sea1.jpg"))
        self.qLabel.setScaledContents(True)
        self.qLabel.setAlignment(Qt.AlignCenter)
        QtCore.QMetaObject.connectSlotsByName(qWidget)

class QmyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.ui.qPlainTextEdit.setAcceptDrops(False)
        self.ui.qLabel.setAcceptDrops(False)
        self.ui.qLabel.setScaledContents(True)

    def dragEnterEvent(self, event):
        self.ui.qPlainTextEdit.clear()
        self.ui.qPlainTextEdit.appendPlainText("dragEnterEvent事件 mimeData()->formats()")
        for strLine in event.mimeData().formats():
            self.ui.qPlainTextEdit.appendPlainText(strLine)

        self.ui.qPlainTextEdit.appendPlainText("\ndragEnterEvent事件 mimeData()->urls()")
        for url in event.mimeData().urls():
            self.ui.qPlainTextEdit.appendPlainText(url.path())

        if(event.mimeData().hasUrls()):
            filename = event.mimeData().urls()[0].fileName()
            basename, ext = os.path.splitext(filename)
            ext = ext.upper()
            if(ext == ".JPG"):
                event.acceptProposedAction()
            else:
                event.ignore()
        else:
            event.ignore()

    def dropEvent(self, event):
        filename = event.mimeData().urls()[0].path()
        cnt = len(filename)

        realname = filename[1:cnt]
        pixmap = QPixmap(realname)
        self.ui.qLabel.setPixmap(pixmap)
        event.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyWidget()
    mw.show()
    sys.exit(app.exec_())