'''
总结：
1，注意标签内触发event必须重新定义标签类

'''
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QWidget, QApplication


class QmyLabel(QLabel):
    doubleClicked = pyqtSignal()

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()

class QmyWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.resize(280, 150)
        LabHello = QmyLabel(self)
        LabHello.setText("双击我啊")
        font = LabHello.font()
        font.setPointSize(14)
        font.setBold(True)
        LabHello.setFont(font)
        size = LabHello.sizeHint()
        LabHello.setGeometry(70, 60, size.width(), size.height())
        LabHello.doubleClicked.connect(self.do_doubledClicked)

    def do_doubledClicked(self):
        print("标签被双击了")

    def mouseDoubleClickEvent(self, event):
        print("窗口双击事件")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())