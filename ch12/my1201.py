'''
注意：
1，QChartView里有个QChart，QChart里有两个QLineSeries
2，QLineSeries里是一组x和y的对，可以理解为坐标点
'''

import sys, math

from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtWidgets import QMainWindow, QApplication


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Demo12_1, QChart 基本绘图")
        self.resize(580, 420)
        chart = QChart()
        chart.setTitle("简单函数曲线")
        chartView = QChartView(self)
        chartView.setChart(chart)
        self.setCentralWidget(chartView)
        series0 = QLineSeries()
        series1 = QLineSeries()
        series0.setName("sin曲线")
        series1.setName("cos曲线")
        chart.addSeries(series0)
        chart.addSeries(series1)
        t = 0
        intv = 0.1
        pointCount = 100
        for i in range(pointCount):
            y1 = math.cos(t)
            series0.append(t, y1)
            y2 = 1.5 * math.sin(t + 20)
            series1.append(t, y2)
            t = t + intv
        axisX = QValueAxis()
        axisX.setRange(0, 10)
        axisX.setTitleText("time(secs)")
        axisY = QValueAxis()
        axisY.setRange(-2, 2)
        axisY.setTitleText("value")

        chart.setAxisX(axisX, series0)
        chart.setAxisY(axisY, series0)
        chart.setAxisX(axisX, series1)
        chart.setAxisY(axisY, series1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
