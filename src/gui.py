from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
from PyQt5.QtWidgets import *

import src.model.MyDF
import src.util.no_frameobj_helper
from src.guiHelper import scoreTable as st
from src.util import genAllChart as g
from src import query as qr
from src.util import frameobj_helper as hp
from src import table
from src.model.MyDF import MyDataFrame
class MainWindow(QMainWindow):
    """
    Main gui class of the program.
    """

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
        # default starbucks and related query parameters
        dataframe = qr.get_dataFrame(table)
        self.starbucks = MyDataFrame()
        self.starbucks.setDataFrame(dataframe)
        self.starbucks.setTable(table)
        #default value
        self.aimlat = 22.3
        self.aimlng = 113.71
        self.k = 5
        self.r = 15
        self.keyword = "珠海"

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
        self.normalMenu = menubar.addMenu('常规图表')
        self.fileMenu = menubar.addMenu('模式图表')
        self.modeMenu = menubar.addMenu('选择模式')
        self.scoreMenu = menubar.addMenu('进入评分')



        # 添加URL地址栏
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        # self.urlbar.setText("在此输入经度、纬度和k值，用半角逗号分隔：")
        # 让地址栏能响应回车按键信号

        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)
        if (not os.path.exists(os.path.curdir + '\\modeHtml\\')):
            os.mkdir(os.path.curdir + '\\modeHtml\\')

        #modeMenu options
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

        #scoreMenu options
        Action4 = QAction('top-k-score', self)
        Action4.setCheckable(True)
        Action4.triggered.connect(self.handleScore)
        self.scoreMenu.addAction(Action4)
        Action5 = QAction('top-r-score', self)
        Action5.setCheckable(True)
        Action5.triggered.connect(self.handleScore)
        self.scoreMenu.addAction(Action5)
        Action6 = QAction('key-match-k-score', self)
        Action6.setCheckable(True)
        Action6.triggered.connect(self.handleScore)
        self.scoreMenu.addAction(Action6)

        self.normalUrls = os.listdir(os.path.curdir + '/chartHtml')
        for item in self.normalUrls:
            itemAction = QAction(item.title().replace('.Html', ''), self)
            itemAction.setCheckable(True)
            itemAction.triggered.connect(self.showNormalChart)
            self.normalMenu.addAction(itemAction)

        gen1 =  g.Gen()
        gen1.run(0, 0, 0, None, '')
        self.show()
    def handleScore(self):

        # 读取评分记录
        save_log = self.starbucks.grade_read()
        d_dict = hp.count_all_distance(self.aimlat, self.aimlng, self.starbucks)
        for action in self.scoreMenu.actions():
            if action.isChecked():
                str = action.text()
                if (str == 'top-k-score'):
                    action.setChecked(False)
                    # top-k查询结果进行店铺评分
                    title = str
                    k_list = src.util.no_frameobj_helper.top_k(d_dict, self.k, isReturnList=True)
                    match_topk = hp.change_to_matchdict(k_list, self.starbucks, save_log)
                    self.table = st.MyTable(title,match_topk,save_log)
                    break
                elif (str == 'top-r-score'):
                    action.setChecked(False)
                    # range查询结果进行店铺评分
                    title = str
                    r_list = src.util.no_frameobj_helper.top_r(d_dict, self.r, isReturnList=True)
                    match_range = hp.change_to_matchdict(r_list, self.starbucks,save_log)
                    self.table = st.MyTable(title, match_range, save_log)
                    break
                elif (str == 'key-match-k-score'):
                    action.setChecked(False)
                    # 关键词查询结果进行店铺评分
                    title = str
                    keyword_list = hp.keyword_select(self.keyword, self.k, self.aimlat, self.aimlng, self.starbucks, isReturnList=True, isOpen=False)
                    match_keyword = hp.change_to_matchdict(keyword_list,self.starbucks,save_log)
                    self.table = st.MyTable(title, match_keyword, save_log)
                    break



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
                url = os.path.abspath("modeHtml/" + action.text() + '.html')
                # remember to unchecked !
                action.setChecked(False)
                self.browser.load(QUrl.fromLocalFile(url))
                self.setCentralWidget(self.browser)

    def showNormalChart(self):
        for action in self.normalMenu.actions():
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
            self.aimlng = float(q.split(',')[0])
            self.aimlat = float(q.split(',')[1])
            self.k = int(q.split(',')[2])
            if (self.aimlng >= -180 and self.aimlng <= 180 and self.aimlat >= -90 and self.aimlat <= 90):
                gen2.run(self.aimlng, self.aimlat, self.k, keyword=None, mode=self.mode)
                if(self.first):
                    self.addChartMenu()
                self.first = False
            else:
                self.urlbar.setText("不合法的输入！")
        elif (self.mode == 'r'):
            print("Enter r mode!")
            self.aimlng = float(q.split(',')[0])
            self.aimlat = float(q.split(',')[1])
            self.r = int(q.split(',')[2])
            if (self.aimlng >= -180 and self.aimlng <= 180 and self.aimlat >= -90 and self.aimlat <= 90):
                gen2.run(self.aimlng, self.aimlat, self.r, keyword=None, mode=self.mode)
                if (self.first):
                    self.addChartMenu()
                self.first = False
            else:
                self.urlbar.setText("不合法的输入！")
        elif (self.mode == 'm'):
            print("Enter m mode!")
            self.aimlng = float(q.split(',')[0])
            self.aimlat = float(q.split(',')[1])
            self.keyword = q.split(',')[2]
            self.k = int(q.split(',')[3])
            if (self.aimlng >= -180 and self.aimlng <= 180 and self.aimlat >= -90 and self.aimlat <= 90):
                gen2.run(self.aimlng, self.aimlat, self.k,self.keyword,mode=self.mode)
                if (self.first):
                    self.addChartMenu()
                self.first = False
            else:
                self.urlbar.setText("不合法的输入！")

    def addChartMenu(self):
        self.urlList = os.listdir(os.path.curdir + '/modeHtml')
        for item in self.urlList:
            itemAction = QAction(item.title().replace('.Html', ''), self)
            itemAction.setCheckable(True)
            itemAction.triggered.connect(self.showDataChart)
            self.fileMenu.addAction(itemAction)






