import sys
import random

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QDir, QSize, pyqtSignal, QPoint, pyqtSlot, QPointF
from PyQt5.QtGui import QIcon, QKeyEvent, QBrush, QPolygonF, QPen
from PyQt5.QtWidgets import QFrame, QFileSystemModel, QGraphicsView, QLabel, QGraphicsScene, QGraphicsItem, \
    QColorDialog, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsPolygonItem, QGraphicsLineItem, QInputDialog, \
    QGraphicsTextItem, QGraphicsItemGroup, QFontDialog


class Ui_MainWindow():
    def setupUi(self, qMainWindow):
        qMainWindow.resize(568, 380)
        self.qWidget = QtWidgets.QWidget(qMainWindow)
        self.qToolBar1 = QtWidgets.QToolBar(qMainWindow)
        self.qToolBar1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.qToolBar1.setIconSize(QSize(16, 16))
        self.qToolBar2 = QtWidgets.QToolBar(qMainWindow)
        self.qToolBar2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.qToolBar2.setIconSize(QSize(16, 16))
        self.qStatusBar = QtWidgets.QStatusBar(qMainWindow)
        qMainWindow.setStatusBar(self.qStatusBar)
        # self.qMenBar = QtWidgets.QMenuBar(qMainWindow)

        self.qAction1 = QtWidgets.QAction(QIcon("../image/zoomin.png"), "放大", self.qToolBar1)
        self.qAction2 = QtWidgets.QAction(QIcon("../image/zoomout.png"), "缩小", self.qToolBar1)
        self.qAction3 = QtWidgets.QAction(QIcon("../image/420.bmp"), "恢复", self.qToolBar1)
        self.qAction4 = QtWidgets.QAction(QIcon("../image/rotateleft.png"), "左旋转", self.qToolBar1)
        self.qAction5 = QtWidgets.QAction(QIcon("../image/rotateright.png"), "右旋转", self.qToolBar1)
        self.qAction6 = QtWidgets.QAction(QIcon("../image/528.bmp"), "前置", self.qToolBar1)
        self.qAction7 = QtWidgets.QAction(QIcon("../image/526.bmp"), "后置", self.qToolBar1)
        self.qAction8 = QtWidgets.QAction(QIcon("../image/UNGROUP.BMP"), "组合", self.qToolBar1)
        self.qAction9 = QtWidgets.QAction(QIcon("../image/128_1.bmp"), "打散", self.qToolBar1)
        self.qAction10 = QtWidgets.QAction(QIcon("../image/108.bmp"), "删除", self.qToolBar1)
        self.qAction11 = QtWidgets.QAction(QIcon("../image/132.bmp"), "退出", self.qToolBar1)
        self.qToolBar1.addAction(self.qAction1)
        self.qToolBar1.addAction(self.qAction2)
        self.qToolBar1.addAction(self.qAction3)
        self.qToolBar1.addSeparator()
        self.qToolBar1.addAction(self.qAction4)
        self.qToolBar1.addAction(self.qAction5)
        self.qToolBar1.addAction(self.qAction6)
        self.qToolBar1.addAction(self.qAction7)
        self.qToolBar1.addAction(self.qAction8)
        self.qToolBar1.addAction(self.qAction9)
        self.qToolBar1.addSeparator()
        self.qToolBar1.addAction(self.qAction10)
        self.qToolBar1.addSeparator()
        self.qToolBar1.addAction(self.qAction11)

        self.qAction12 = QtWidgets.QAction(QIcon("../image/RECTANGL.BMP"), "矩形", self.qToolBar2)
        self.qAction13 = QtWidgets.QAction(QIcon("../image/ELLIPSE.BMP"), "椭圆", self.qToolBar2)
        self.qAction14 = QtWidgets.QAction(QIcon("../image/08.JPG"), "圆形", self.qToolBar2)
        self.qAction15 = QtWidgets.QAction(QIcon("../image/Icon1242.ico"), "三角形", self.qToolBar2)
        self.qAction16 = QtWidgets.QAction(QIcon("../image/FREEFORM.BMP"), "梯形", self.qToolBar2)
        self.qAction17 = QtWidgets.QAction(QIcon("../image/LINE.BMP"), "直线", self.qToolBar2)
        self.qAction18 = QtWidgets.QAction(QIcon("../image/800.bmp"), "文字", self.qToolBar2)
        self.qToolBar2.addAction(self.qAction12)
        self.qToolBar2.addAction(self.qAction13)
        self.qToolBar2.addAction(self.qAction14)
        self.qToolBar2.addAction(self.qAction15)
        self.qToolBar2.addAction(self.qAction16)
        self.qToolBar2.addAction(self.qAction17)
        self.qToolBar2.addAction(self.qAction18)

        qMainWindow.addToolBar(Qt.TopToolBarArea, self.qToolBar1)
        qMainWindow.addToolBar(Qt.LeftToolBarArea, self.qToolBar2)
        qMainWindow.setCentralWidget(self.qWidget)

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
        self.qAction18.setObjectName("qAction18")

        self.qAction11.triggered.connect(qMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(qMainWindow)


class QmyGraphicsView(QGraphicsView):
    mouseMove = pyqtSignal(QPoint)
    mouseClicked = pyqtSignal(QPoint)
    mouseDoubleClick = pyqtSignal(QPoint)
    keyPress = pyqtSignal(QKeyEvent)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        point = event.pos()
        self.mouseMove.emit(point)
        super().mouseMoveEvent(event)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            point = event.pos()
            self.mouseClicked.emit(point)
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            point = event.pos()
            self.mouseDoubleClick.emit(point)
        super().mouseDoubleClickEvent(event)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        self.keyPress.emit(event)
        super().keyPressEvent(event)


class QmyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__buildStatusBar()
        self.__iniGraphicsSystem()

        self.__ItemId = 1
        self.__ItemDesc = 2
        self.__seqNum = 0
        self.__backZ = 0
        self.__frontZ = 0

    def __buildStatusBar(self):
        self.__labViewCord = QLabel("View 坐标：")
        self.__labViewCord.setMinimumWidth(150)
        self.ui.qStatusBar.addWidget(self.__labViewCord)

        self.__labSceneCord = QLabel("Scene 坐标：")
        self.__labSceneCord.setMinimumWidth(150)
        self.ui.qStatusBar.addWidget(self.__labSceneCord)

        self.__labItemCord = QLabel("Item 坐标：")
        self.__labItemCord.setMinimumWidth(150)
        self.ui.qStatusBar.addWidget(self.__labItemCord)

        self.__labItemInfo = QLabel("ItemInfo: ")
        self.ui.qStatusBar.addWidget(self.__labItemInfo)

    def __iniGraphicsSystem(self):
        self.view = QmyGraphicsView(self)
        self.setCentralWidget(self.view)

        self.scene = QGraphicsScene(-300, -200, 600, 200)
        self.view.setScene(self.scene)
        self.view.setCursor(Qt.CrossCursor)
        self.view.setMouseTracking(True)
        self.view.setDragMode(QGraphicsView.RubberBandDrag)

        self.view.mouseMove.connect(self.do_mouseMove)
        self.view.mouseClicked.connect(self.do_mouseClicked)
        self.view.mouseDoubleClick.connect(self.do_mouseDoubleClick)
        self.view.keyPress.connect(self.do_keyPress)

    def __setItemProperties(self, item, desc):
        item.setFlag(QGraphicsItem.ItemIsFocusable)
        item.setFlag(QGraphicsItem.ItemIsMovable)
        item.setFlag(QGraphicsItem.ItemIsSelectable)

        self.__frontZ += 1
        item.setZValue(self.__frontZ)
        item.setPos(-150 + random.randint(1, 200), -200 + random.randint(1, 200))

        self.__seqNum += 1
        item.setData(self.__ItemId, self.__seqNum)
        item.setData(self.__ItemDesc, desc)

        self.scene.addItem(item)
        self.scene.clearSelection()
        item.setSelected(True)


    def __setBrushColor(self, item):
        color = item.brush().color()
        color = QColorDialog.getColor(color, self, "选择填充颜色")
        if color.isValid():
            item.setBrush(QBrush(color))

    @pyqtSlot()
    def on_qAction12_triggered(self):
        item = QGraphicsRectItem(-50, -25, 100, 50)
        item.setBrush(QBrush(Qt.yellow))
        self.__setItemProperties(item, "矩形")

    @pyqtSlot()
    def on_qAction13_triggered(self):
        item = QGraphicsEllipseItem(-50, -30, 100, 60)
        item.setBrush(QBrush(Qt.blue))
        self.__setItemProperties(item, "椭圆")

    @pyqtSlot()
    def on_qAction14_triggered(self):
        item = QGraphicsEllipseItem(-50, -50, 100, 100)
        item.setBrush(QBrush(Qt.cyan))
        self.__setItemProperties(item, "圆形")

    @pyqtSlot()
    def on_qAction15_triggered(self):
        item = QGraphicsPolygonItem()
        points = [QPointF(0, -40), QPointF(60, 40), QPointF(-60, 40)]
        item.setPolygon(QPolygonF(points))
        item.setBrush(QBrush(Qt.magenta))
        self.__setItemProperties(item, "三角形")

    @pyqtSlot()
    def on_qAction16_triggered(self):
        item = QGraphicsPolygonItem()
        points = [QPointF(-40, -40), QPointF(40, -40), QPointF(100, 40), QPointF(-100, 40)]
        item.setPolygon(QPolygonF(points))
        item.setBrush(QBrush(Qt.green))
        self.__setItemProperties(item, "梯形")

    @pyqtSlot()
    def on_qAction17_triggered(self):
        item = QGraphicsLineItem(-100, 0, 100, 0)
        pen = QPen(Qt.red)
        pen.setWidth(4)
        item.setPen(pen)
        self.__setItemProperties(item, "直线")

    @pyqtSlot()
    def on_qAction18_triggered(self):
        strText, OK = QInputDialog.getText(self, "输入", "请输入文字")
        if (not OK):
            return
        item = QGraphicsTextItem(strText)
        font = self.font()
        font.setPointSize(20)
        font.setBold(True)
        item.setFont(font)
        item.setDefaultTextColor(Qt.black)
        self.__setItemProperties(item, "文字")

    @pyqtSlot()
    def on_qAction1_triggered(self):
        items = self.scene.selectedItems()
        cnt = len(items)
        if cnt == 1:
            item = items[0]
            item.setScale(0.1 + item.scale())
        else:
            self.view.scale(1.1, 1.1)

    @pyqtSlot()
    def on_qAction2_triggered(self):
        items = self.scene.selectedItems()
        cnt = len(items)
        if cnt == 1:
            item = items[0]
            item.setScale(item.scale() - 0.1)
        else:
            self.view.scale(0.9, 0.9)

    @pyqtSlot()
    def on_qAction3_triggered(self):
        items = self.scene.selectedItems()
        cnt = len(items)
        if cnt == 1:
            item = items[0]
            item.setScale(1)
            item.setRotation(0)
        else:
            self.view.resetTransform()

    @pyqtSlot()
    def on_qAction4_triggered(self):
        items = self.scene.selectedItems()
        cnt = len(items)
        if cnt == 1:
            item = items[0]
            item.setRotation(-30 + item.rotation())
        else:
            self.view.rotate(-30)

    @pyqtSlot()
    def on_qAction5_triggered(self):
        items = self.scene.selectedItems()
        cnt = len(items)
        if cnt == 1:
            item = items[0]
            item.setRotation(30 + item.rotation())
        else:
            self.view.rotate(30)

    @pyqtSlot()
    def on_qAction6_triggered(self):    # 前置
        items = self.scene.selectedItems()
        cnt = len(items)
        if cnt > 0:
            item = items[0]
            self.__frontZ += 1
            item.setZValue(self.__frontZ)

    @pyqtSlot()
    def on_qAction7_triggered(self):    # 后置
        items = self.scene.selectedItems()
        cnt = len(items)
        if cnt > 0:
            item = items[0]
            self.__backZ -= 1
            item.setZValue(self.__backZ)

    @pyqtSlot()
    def on_qAction8_triggered(self):    # 组合
        items = self.scene.selectedItems()
        cnt = len(items)
        if cnt <= 1:
            return
        group = QGraphicsItemGroup()
        self.scene.addItem(group)
        for i in range(cnt):
            item = items[i]
            item.setSelected(False)
            item.clearFocus()
            group.addToGroup(item)

        group.setFlag(QGraphicsItem.ItemIsFocusable)
        group.setFlag(QGraphicsItem.ItemIsMovable)
        group.setFlag(QGraphicsItem.ItemIsSelectable)

        self.__frontZ += 1
        group.setZValue(self.__frontZ)
        self.scene.clearSelection()
        group.setSelected(True)

    @pyqtSlot()
    def on_qAction9_triggered(self):
        items = self.scene.selectedItems()
        cnt = len(items)
        if (cnt == 1):
            group = items[0]
            self.scene.destroyItemGroup(group)

    @pyqtSlot()
    def on_qAction10_triggered(self):
        items = self.scene.selectedItems()
        cnt = len(items)
        for i in range(cnt):
            item = items[i]
            self.scene.removeItem(item)

    def do_mouseMove(self, point):
        self.__labViewCord.setText("View 坐标：%d, %d" % (point.x(), point.y()))
        pt = self.view.mapToScene(point)
        self.__labSceneCord.setText("Scene 坐标：%.0f, %.0f" % (pt.x(), pt.y()))

    def do_mouseClicked(self, point):
        pt = self.view.mapToScene(point)
        item = self.scene.itemAt(pt, self.view.transform())
        if (item == None):
            return
        pm = item.mapFromScene(pt)
        self.__labItemCord.setText("item 坐标：%.0f, %.0f" % (pm.x(), pm.y()))
        self.__labItemInfo.setText(str(item.data(self.__ItemDesc)) + ", ItemId=" + str(item.data(self.__ItemId)))

    def do_mouseDoubleClick(self, point):
        pt = self.view.mapToScene(point)
        item = self.scene.itemAt(pt, self.view.transform())
        if (item == None):
            return
        className = str(type(item))
        if (className.find("QGraphicsRectItem") >= 0):
            self.__setBrushColor(item)
        elif (className.find("QGraphicsEllipseItem") >= 0):
            self.__setBrushColor(item)
        elif (className.find("QGraphicsEllipseItem") >= 0):
            self.__setBrushColor(item)
        elif (className.find("QGraphicsLineItem") >= 0):
            pen = item.pen()
            color = item.pen().color()
            color = QColorDialog.getColor(color, self, "选择线条颜色")
            if color.isValid():
                pen.setColor(color)
                item.setPen(pen)
        elif (className.find("QGraphicsTextItem") >= 0):
            font = item.font()
            font, OK = QFontDialog.getFont(font)
            if OK:
                item.setfont(font)

    def do_keyPress(self, event):
        items = self.scene.selectedItems()
        cnt = len(items)
        if (cnt != 1):
            return
        item = items[0]
        key = event.key()
        if (key == Qt.Key_Delete):
            self.scene.removeItem(item)
        elif (key == Qt.Key_Space):
            item.setRotation(90 + item.rotation())
        elif (key == Qt.Key_PageUp):
            item.setScale(0.1 + item.scale())
        elif (key == Qt.Key_PageDown):
            item.setScale(-0.1 + item.scale())
        elif (key == Qt.Key_Left):
            item.setX(-1 + item.x())
        elif (key == Qt.Key_Right):
            item.setX(1 + item.x())
        elif (key == Qt.Key_Up):
            item.setY(-1 + item.y())
        elif (key == Qt.Key_Down):
            item.setY(1 + item.y())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QmyMainWindow()
    mw.show()
    sys.exit(app.exec_(), )
