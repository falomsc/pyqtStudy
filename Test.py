import sys

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal, QPoint, Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QGraphicsView, QMainWindow, QApplication, QWidget, QVBoxLayout, QGroupBox, QLabel, \
    QStatusBar, QGraphicsScene, QGraphicsRectItem, QGraphicsItem, QGraphicsEllipseItem


class QmyGraphicsView(QGraphicsView):
    mouseMove = pyqtSignal(QPoint)
    mouseClicked = pyqtSignal(QPoint)

    # def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
    #     point = event.pos()
    #     self.mouseMove.emit(point)
    #     super().mouseMoveEvent(event)
    #
    # def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
    #     if event.button() == Qt.LeftButton:
    #         point = event.pos()
    #         self.mouseclicked.emit(point)
    #     super().mousePressEvent(event)

    def mouseMoveEvent(self, event):  ##鼠标移动事件
        point = event.pos()
        self.mouseMove.emit(point)  # 发射信号
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event):  ##鼠标单击事件
        if event.button() == Qt.LeftButton:
            point = event.pos()
            self.mouseClicked.emit(point)  # 发射信号
        super().mousePressEvent(event)

class QmyMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.__buildUI()
        self.__iniGraphicsSystem()
        self.view.mouseMove.connect(self.do_mouseMovePoint)
        self.view.mouseClicked.connect(self.do_mouseClicked)

    # def __buildUI(self):
    #     self.resize(600,450)
    #     font = self.font()
    #     font.setPointSize(11)
    #     self.setFont(font)
    #
    #     centralWidget = QWidget(self)
    #     vLayoutMain = QVBoxLayout(centralWidget)
    #
    #     groupBox = QGroupBox(centralWidget)
    #     vLayoutGroup = QVBoxLayout(groupBox)
    #     self.__labViewSize = QLabel(groupBox)
    #     self.__labViewSize.setText("view坐标，左上角(0,0)，宽度=，长度=")
    #     vLayoutGroup.addWidget(self.__labViewSize)
    #     self.__labSceneRect = QLabel(groupBox)
    #     self.__labSceneRect.setText("view.sceneRect=()")
    #     vLayoutGroup.addWidget(self.__labSceneRect)
    #     vLayoutMain.addWidget(groupBox)
    #
    #     self.view = QmyGraphicsView(centralWidget)
    #     self.view.setCursor(Qt.CrossCursor)
    #     self.view.setMouseTracking(True)
    #     vLayoutMain.addWidget(self.view)
    #     self.setCentralWidget(centralWidget)
    #
    #     statusBar = QStatusBar(self)
    #     self.setStatusBar(statusBar)
    #     self.__labViewCord = QLabel("View 坐标：")
    #     self.__labViewCord.setMinimumWidth(150)
    #     statusBar.addWidget(self.__labViewCord)
    #     self.__labSceneCord = QLabel("Scene 坐标：")
    #     self.__labSceneCord.setMinimumWidth(150)
    #     statusBar.addWidget(self.__labSceneCord)
    #     self.__labItemCord = QLabel("Item 坐标：")
    #     self.__labItemCord.setMinimumWidth(150)
    #     statusBar.addWidget(self.__labItemCord)

    def __buildUI(self):  ##构造界面
        self.resize(600, 450)
        self.setWindowTitle("Demo8_5, View/Scene/Item关系和坐标变换")

        font = self.font()
        font.setPointSize(11)
        self.setFont(font)

        centralWidget = QWidget(self)  # 中间工作区组件
        vLayoutMain = QVBoxLayout(centralWidget)  # 垂直布局

        groupBox = QGroupBox(centralWidget)  # 显示两个Label的groupBox
        vLayoutGroup = QVBoxLayout(groupBox)
        self.__labViewSize = QLabel(groupBox)
        self.__labViewSize.setText("view坐标，左上角(0,0)，宽度=，长度=")

        vLayoutGroup.addWidget(self.__labViewSize)
        self.__labSceneRect = QLabel(groupBox)
        self.__labSceneRect.setText("view.sceneRect=()")
        vLayoutGroup.addWidget(self.__labSceneRect)

        vLayoutMain.addWidget(groupBox)  # 主布局添加groupBox

        self.view = QmyGraphicsView(centralWidget)  # 绘图视图
        self.view.setCursor(Qt.CrossCursor)
        self.view.setMouseTracking(True)
        ##      self.view.setDragMode(QGraphicsView.RubberBandDrag)
        vLayoutMain.addWidget(self.view)  # 添加到主布局

        self.setCentralWidget(centralWidget)  # 设置工作区中间组件

        statusBar = QStatusBar(self)  # 状态栏
        self.setStatusBar(statusBar)

        self.__labViewCord = QLabel("View 坐标：")
        self.__labViewCord.setMinimumWidth(150)
        statusBar.addWidget(self.__labViewCord)

        self.__labSceneCord = QLabel("Scene 坐标：")
        self.__labSceneCord.setMinimumWidth(150)
        statusBar.addWidget(self.__labSceneCord)

        self.__labItemCord = QLabel("Item 坐标：")
        self.__labItemCord.setMinimumWidth(150)
        statusBar.addWidget(self.__labItemCord)

    # def __iniGraphicsSystem(self):
    #     rect = QRectF(-200, -100, 400, 200)
    #     self.scene = QGraphicsScene(rect)
    #     self.view.setScene(self.scene)
    #     item = QGraphicsRectItem(rect)
    #     item.setFlag(QGraphicsItem.ItemIsSelectable)
    #     item.setFlag(QGraphicsItem.ItemIsFocusable)
    #     pen = QPen()
    #     pen.setWidth(2)
    #     item.setPen(pen)
    #     self.scene.addItem(item)
    #
    #     item2 = QGraphicsEllipseItem(-100, -50, 200, 100)
    #     item2.setPos(0, 0)
    #     item2.setBrush(QBrush(Qt.blue))
    #     item2.setFlag(QGraphicsItem.ItemIsSelectable)
    #     item2.setFlag(QGraphicsItem.ItemIsFocusable)
    #     item2.setFlag(QGraphicsItem.ItemIsMovable)
    #     self.scene.addItem(item2)
    #
    #     item3 = QGraphicsEllipseItem(-50, -50, 100, 100)
    #     item3.setPos(rect.right(), rect.bottom())
    #     item3.setBrush(QBrush(Qt.red))
    #     item3.setFlag(QGraphicsItem.ItemIsSelectable)
    #     item3.setFlag(QGraphicsItem.ItemIsFocusable)
    #     item3.setFlag(QGraphicsItem.ItemIsMovable)
    #     self.scene.addItem(item3)
    #
    #     self.scene.clearSelection()

    def __iniGraphicsSystem(self):  ##初始化 graphics View系统
        rect = QRectF(-200, -100, 400, 200)
        self.scene = QGraphicsScene(rect)  # scene逻辑坐标系定义
        self.view.setScene(self.scene)

        ## 画一个矩形框，大小等于scene
        item = QGraphicsRectItem(rect)  # 矩形框正好等于scene的大小
        item.setFlag(QGraphicsItem.ItemIsSelectable)  # 可选，
        item.setFlag(QGraphicsItem.ItemIsFocusable)  # 可以有焦点
        pen = QPen()
        pen.setWidth(2)
        item.setPen(pen)
        self.scene.addItem(item)

        ##一个位于scene中心的椭圆，测试局部坐标
        # 矩形框内创建椭圆,绘图项的局部坐标，左上角(-100,-50)，宽200，高100
        item2 = QGraphicsEllipseItem(-100, -50, 200, 100)
        item2.setPos(0, 0)
        item2.setBrush(QBrush(Qt.blue))
        item2.setFlag(QGraphicsItem.ItemIsSelectable)  # 可选，
        item2.setFlag(QGraphicsItem.ItemIsFocusable)  # 可以有焦点
        item2.setFlag(QGraphicsItem.ItemIsMovable)  # 可移动

        self.scene.addItem(item2)

        ##一个圆，中心位于scene的边缘
        item3 = QGraphicsEllipseItem(-50, -50, 100, 100)  # 矩形框内创建椭圆,绘图项的局部坐标
        item3.setPos(rect.right(), rect.bottom())
        item3.setBrush(QBrush(Qt.red))
        item3.setFlag(QGraphicsItem.ItemIsSelectable)  # 可选，
        item3.setFlag(QGraphicsItem.ItemIsFocusable)  # 可以有焦点
        item3.setFlag(QGraphicsItem.ItemIsMovable)  # 可移动
        self.scene.addItem(item3)

        self.scene.clearSelection()

    # def do_mouseMovePoint(self, point):
    #     self.__labViewCord.setText("View 坐标：%d,%d" %(point.x(), point.y()))
    #     pt = self.view.mapToScene(point)
    #     self.__labSceneCord.setText("Scene 坐标：%.0f,%.0f" %(pt.x(), pt.y()))
    #
    # def do_mouseClicked(self, point):
    #     pt = self.view.mapToScene(point)
    #     item = None
    #     item = self.scene.itemAt(pt, self.view.transform())
    #     if(item!=None):
    #         pm = item.mapFromScene(pt)
    #         self.__labItemCord.setText("Item 坐标：%.0f,%.0f" %(pm.x(), pm.y()))

    def do_mouseMovePoint(self, point):
        ##鼠标移动事件，point是 GraphicsView的坐标,物理坐标
        self.__labViewCord.setText("View坐标：%d,%d" % (point.x(), point.y()))
        pt = self.view.mapToScene(point)  # 转换到Scene坐标
        self.__labSceneCord.setText("Scene坐标：%.0f,%.0f" % (pt.x(), pt.y()))

    def do_mouseClicked(self, point):
        pt = self.view.mapToScene(point)  # 转换到Scene坐标
        item = None
        item = self.scene.itemAt(pt, self.view.transform())  # 获取光标下的绘图项
        if (item != None):  # 有绘图项
            pm = item.mapFromScene(pt)  # 转换为绘图项的局部坐标
            self.__labItemCord.setText("Item坐标：%.0f,%.0f" % (pm.x(), pm.y()))

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.__labViewSize.setText('View 坐标，左上角(0,0)，宽度=%d，高度=%d' % (self.view.width(), self.view.height()))
        rectF = self.view.sceneRect()
        self.__labSceneRect.setText('view.sceneRect = (%.0f,%.0f,%.0f,%.0f)' %(rectF.left(),rectF.top(),rectF.width(),rectF.height()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())