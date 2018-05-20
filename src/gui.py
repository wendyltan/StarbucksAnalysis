from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
from PyQt5.QtWidgets import *

from src.util import genAllChart as g


class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('星巴克数据分析')
        # 设置窗口图标
        self.setWindowIcon(QIcon('icons/star.png'))
        # 设置窗口大小
        self.resize(1200, 800)
        self.gen = g.Gen()
        # default mode
        self.mode = 'k'
        self.first = True

        # 设置浏览器
        self.browser = QWebEngineView()
        url = os.path.abspath('icons/foobar.html')
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl.fromLocalFile(url))
        # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)

        # adding menu...
        menubar = self.menuBar()
        # 添加导航栏
        navigation_bar = QToolBar('Navigation')
        # 设定图标的大小
        navigation_bar.setIconSize(QSize(32, 32))
        # 添加导航栏到窗口中
        self.addToolBar(navigation_bar)
        self.fileMenu = menubar.addMenu('显示图表')
        self.modeMenu = menubar.addMenu('选择模式')

        # 添加URL地址栏
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        # self.urlbar.setText("在此输入经度、纬度和k值，用半角逗号分隔：")
        # 让地址栏能响应回车按键信号

        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)
        if (not os.path.exists(os.path.curdir + '\\chartHtml\\')):
            os.mkdir(os.path.curdir + '\\chartHtml\\')

        Action1 = QAction('top-k', self)
        Action1.setCheckable(True)
        Action1.triggered.connect(self.handleMode)
        self.modeMenu.addAction(Action1)
        Action2 = QAction('top-r', self)
        Action2.setCheckable(True)
        Action2.triggered.connect(self.handleMode)
        self.modeMenu.addAction(Action2)
        Action3 = QAction('key-match-k', self)
        Action3.setCheckable(True)
        Action3.triggered.connect(self.handleMode)
        self.modeMenu.addAction(Action3)

        self.show()

    def handleMode(self):
        for action in self.modeMenu.actions():
            if action.isChecked():
                str = action.text()
                if (str == 'top-k'):
                    action.setChecked(False)
                    self.mode = 'k'
                    self.urlbar.setText("Enter lat,lon and k")
                    break
                elif (str == 'top-r'):
                    action.setChecked(False)
                    self.mode = 'r'
                    self.urlbar.setText("Enter lat,lon and r")
                    break
                elif (str == 'key-match-k'):
                    action.setChecked(False)
                    self.mode = 'm'
                    self.urlbar.setText("Enter lat,lon ,keyword and k")
                    break

    def showDataChart(self):
        # get actions
        for action in self.fileMenu.actions():
            if action.isChecked():
                url = os.path.abspath("chartHtml/" + action.text() + '.html')
                # remember to unchecked !
                action.setChecked(False)
                self.browser.load(QUrl.fromLocalFile(url))
                self.setCentralWidget(self.browser)

    def navigate_to_url(self):
        q = self.urlbar.text()
        gen2 = g.Gen()
        if (self.mode == 'k'):
            lon = float(q.split(',')[0])
            lat = float(q.split(',')[1])
            k = int(q.split(',')[2])
            if (lon >= -180 and lon <= 180 and lat >= -90 and lat <= 90):
                gen2.run(lon, lat, k, keyword=None, mode=self.mode)
                if(self.first):
                    self.addChartMenu()
                self.first = False
            else:
                self.urlbar.setText("不合法的输入！")
        elif (self.mode == 'r'):
            print("Enter r mode!")
            lon = float(q.split(',')[0])
            lat = float(q.split(',')[1])
            r = int(q.split(',')[2])
            if (lon >= -180 and lon <= 180 and lat >= -90 and lat <= 90):
                gen2.run(lon, lat, r, keyword=None, mode=self.mode)
                if (self.first):
                    self.addChartMenu()
                self.first = False
            else:
                self.urlbar.setText("不合法的输入！")
        elif (self.mode == 'm'):
            print("Enter m mode!")
            lon = float(q.split(',')[0])
            lat = float(q.split(',')[1])
            keyword = q.split(',')[2]
            k = int(q.split(',')[3])
            if (lon >= -180 and lon <= 180 and lat >= -90 and lat <= 90):
                gen2.run(lon, lat, k,keyword,  mode=self.mode)
                if (self.first):
                    self.addChartMenu()
                self.first = False
            else:
                self.urlbar.setText("不合法的输入！")

    def addChartMenu(self):
        self.urlList = os.listdir(os.path.curdir + '/chartHtml')
        for item in self.urlList:
            itemAction = QAction(item.title().replace('.Html', ''), self)
            itemAction.setCheckable(True)
            itemAction.triggered.connect(self.showDataChart)
            self.fileMenu.addAction(itemAction)




