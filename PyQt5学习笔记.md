#### 一，PyQt5 GUI程序框架

1. 什么是Python Qt？

   ​		Qt是一个跨平台的应用程序C++开发库类。PyQt是Qt C++类库的Python绑定，PyQt5对应于Qt5类库。使用PyQt5可以充分利用Qt应用程序开发框架和功能丰富的类设计GUI程序

   

2. PyQt5安装。

   直接使用下面的命令安装PyQt5

   ```shell
   pip install PyQt5
   ```

   

3. PyQt5 GUI程序的基本框架

   ```python
   import sys
   from PyQt5 import QtWidgets
   
   app = QtWidgets.QApplication(sys.argv)
   w = QtWidgets.QWidget()
   
   w.resize(300, 300)
   w.setWindowTitle("Hello")
   
   w.show()
   sys.exit(app.exec_())
   ```

   

4. 用UI Designer可视化设计窗体

5. 将ui文件编译为py文件

   ```shell
    pyuic5 -o ui_Dialog.py Dialog.ui
   ```

   

6. 界面与逻辑分离的GUI程序框架

   ```python
   import sys
   from PyQt5.QtWidgets import QWidget, QApplication
   
   class Qw(QWidget):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.ui = Ui_xxx()
           self.ui.setupUi(self)
           
   if __name__ == '__main__':
       app = QApplication(sys.argv)
       mw = Qw()
       mw.show()
       sys.exit(app.exec_())
   ```

   

7. 为组建的内建信号编写槽函数

   setupUi()函数最后一行定义了信号自动关槽函数的规则

   ```python
   QtCore.QMetaObject.connectSlotsByName(Widget)
   on_<object name>_<signal name>(<signal parameters>)
   ```

   自动关联槽函数举例

   ```python
   def on_btnClear_clicked(self):
       ...
   def on_chkBoxUnder_clicked(self):
       ...
   ```

   overload型信号的处理

   ```python
   @pyqtSlot(bool)
   def on_chkBoxItalic_clicked(self, checked)
   ```

   

8. 自定义信号

   要自定义信号，类必须是QObject的子类

   ```python
   from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
   
   class Human(QObject):
       ageChanged = pyqtSignal([int], [str])
       def setAge(self, age):
           self._age = age
           self.ageChanged.emit(self._age)
           ageInfo = "age"
           self.ageChanged[str].emit(ageInfo)
   
   class Respomsor(QObject):
       @pyqtSlot(int)
       def do_ageChanged_int(self, age):
           print(age)
       @pyqtSlot(str)
       def do_ageChanged_str(self, ageInfo):
           print(ageInfo)
   
   boy = Human()
   resp = Respomsor()
   boy.ageChanged.connect(resp.do_ageChanged_int)
   boy.ageChanged[str].connect(resp.do_ageChanged_str)
   boy.setAge(10)
   ```
   

   
9. 资源文件的使用

   Qt Creator里新建Qt Resource File

   文件编译，注意不要移动文件路径

   ```shell
   pyrcc5 .\QtApp\res.qrc -o res_rc.py
   ```

