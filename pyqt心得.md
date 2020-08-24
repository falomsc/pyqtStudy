1. QscrollArea的问题，在QTabWidget中嵌套QLabel，尺寸如何随窗口大小动态改变

   注意QScrollArea内部一定要嵌套QWidget，并用setWidget进行设置。一定要执行setWidgetResizable(True)

   成功方案：

   （1）不需要设置setWidgetResizable(True)，应该是默认设置为True了

   QMainWindow

   |----QScrollArea (CentralWidget)

   ​		|----QWidget (QVboxLayout)

   ​				|----QLabel (QPixmap)

   （2）需要设置setWidgetResizable(True)

   QTabWidget

   |----QScrollArea

   ​		|----QScrollArea

   ​				|----QWidget (QVboxLayout)

   ​						|--QLabel (QPixmap)

   （3）需要设置setWidgetResizable(True)

   |----QTabWidget

   ​		|----QWidget1 (QVboxLayout1)

   ​				|----QScrollArea

   ​						|----QWidget2 (QVboxLayout2)

   ​								|--QLabel (QPixmap)

   ```python
   # 方案（1）
   import sys
   from PyQt5 import QtWidgets
   from PyQt5.QtCore import Qt
   from PyQt5.QtGui import QPixmap
   import rec.res
   
   
   class Ui_MainWindow():
       def setupUi(self, qMainWindow):
           qMainWindow.resize(800, 600)
           self.qScrollArea = QtWidgets.QScrollArea(qMainWindow)
           self.qScrollArea.setWidgetResizable(True)
           qMainWindow.setCentralWidget(self.qScrollArea)
   
           self.qWidget = QtWidgets.QWidget()
           self.qScrollArea.setWidget(self.qWidget)
   
           self.qVBoxLayout = QtWidgets.QVBoxLayout(self.qWidget)
           self.qLabel = QtWidgets.QLabel(self.qWidget)
           self.qLabel.setAlignment(Qt.AlignCenter)
           self.qLabel.setPixmap(QPixmap(":/pic/B66/B66_5+10+gap25+20+10_H_1.png"))
           self.qVBoxLayout.addWidget(self.qLabel)
   
   
   class QmyMainWindow(QtWidgets.QMainWindow):
       def __init__(self, parent = None):
           super().__init__(parent)
           self.ui = Ui_MainWindow()
           self.ui.setupUi(self)
   
   
   if __name__ == '__main__':
       app = QtWidgets.QApplication(sys.argv)
       mw = QmyMainWindow()
       mw.show()
       sys.exit(app.exec_(), )
   ```

   ```python
   # 方案（2）
   import sys
   from PyQt5 import QtWidgets
   from PyQt5.QtCore import Qt
   from PyQt5.QtGui import QPixmap
   import rec.res
   
   
   class Ui_MainWindow():
       def setupUi(self, qMainWindow):
           qMainWindow.resize(800, 600)
           self.qSplitter = QtWidgets.QSplitter(qMainWindow)
           qMainWindow.setCentralWidget(self.qSplitter)
   
           self.qTreeWidget = QtWidgets.QTreeWidget(self.qSplitter)
           self.qTreeWidget.setMaximumSize(200, 16777215)
           self.qTabWidget = QtWidgets.QTabWidget(self.qSplitter)
   
           self.qScrollArea = QtWidgets.QScrollArea(self.qTabWidget)
           self.qScrollArea.setWidgetResizable(True)
           self.qTabWidget.addTab(self.qScrollArea, "pic")
   
           self.qWidget = QtWidgets.QWidget()
           self.qScrollArea.setWidget(self.qWidget)
           self.qVboxLayout = QtWidgets.QVBoxLayout(self.qWidget)
   
           self.qLabel = QtWidgets.QLabel(self.qWidget)
           self.qLabel.setAlignment(Qt.AlignCenter)
           self.qLabel.setPixmap(QPixmap(":/pic/B66/B66_5+10+gap25+20+10_H_1.png"))
           self.qVboxLayout.addWidget(self.qLabel)
   
   
   class QmyMainWindow(QtWidgets.QMainWindow):
       def __init__(self, parent = None):
           super().__init__(parent)
           self.ui = Ui_MainWindow()
           self.ui.setupUi(self)
   
   
   if __name__ == '__main__':
       app = QtWidgets.QApplication(sys.argv)
       mw = QmyMainWindow()
       mw.show()
       sys.exit(app.exec_(), )
   ```

   ```python
   # 方案（3）
   import sys
   from PyQt5 import QtWidgets
   from PyQt5.QtCore import Qt
   from PyQt5.QtGui import QPixmap
   import rec.res
   
   
   class Ui_MainWindow():
       def setupUi(self, qMainWindow):
           qMainWindow.resize(800, 600)
           self.qSplitter = QtWidgets.QSplitter(qMainWindow)
           qMainWindow.setCentralWidget(self.qSplitter)
   
           self.qTreeWidget = QtWidgets.QTreeWidget(self.qSplitter)
           self.qTreeWidget.setMaximumSize(200, 16777215)
           self.qTabWidget = QtWidgets.QTabWidget(self.qSplitter)
   
           self.qWidget1 = QtWidgets.QWidget(self.qTabWidget)
           self.qTabWidget.addTab(self.qWidget1, "pic")
   
           self.qScrollArea = QtWidgets.QScrollArea(self.qWidget1)
           self.qScrollArea.setWidgetResizable(True)
   
           self.qVboxLayout1 = QtWidgets.QVBoxLayout(self.qWidget1)
           self.qVboxLayout1.addWidget(self.qScrollArea)
   
           self.qWidget2 = QtWidgets.QWidget()
           self.qScrollArea.setWidget(self.qWidget2)
           self.qVboxLayout2 = QtWidgets.QVBoxLayout(self.qWidget2)
   
           self.qLabel = QtWidgets.QLabel(self.qWidget2)
           self.qLabel.setAlignment(Qt.AlignCenter)
           self.qLabel.setPixmap(QPixmap(":/pic/B66/B66_5+10+gap25+20+10_H_1.png"))
           self.qVboxLayout2.addWidget(self.qLabel)
   
   
   class QmyMainWindow(QtWidgets.QMainWindow):
       def __init__(self, parent = None):
           super().__init__(parent)
           self.ui = Ui_MainWindow()
           self.ui.setupUi(self)
   
   
   if __name__ == '__main__':
       app = QtWidgets.QApplication(sys.argv)
       mw = QmyMainWindow()
       mw.show()
       sys.exit(app.exec_(), )
   ```

   

2. exec多行报错问题