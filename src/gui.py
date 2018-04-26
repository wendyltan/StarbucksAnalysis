from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
from PyQt5.QtWidgets import *

from src.util import genAllChart as g


class MainWindow(QMainWindow):
    gen = g.Gen()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('星巴克数据分析')
        # 设置窗口图标
        self.setWindowIcon(QIcon('icons/star.png'))
        # 设置窗口大小
        self.resize(1200, 800)

        # 设置浏览器
        self.browser = QWebEngineView()
        url = os.path.abspath('icons/foobar.html')
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl.fromLocalFile(url))
        # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)

        #adding menu...
        menubar = self.menuBar()
        # 添加导航栏
        navigation_bar = QToolBar('Navigation')
        # 设定图标的大小
        navigation_bar.setIconSize(QSize(32, 32))
        #添加导航栏到窗口中
        self.addToolBar(navigation_bar)
        self.fileMenu = menubar.addMenu('显示图表')
        self.btn = QPushButton('top_k', self)
        self.btn.setGeometry(70, 0, 60, 25)

        self.btn2 = QPushButton('k变化', self)
        self.btn2.setGeometry(130, 0, 60, 25)
        self.btn2.clicked.connect(self.showChange)

         #添加URL地址栏
        self.urlbar = QLineEdit()
        self.urlbar.setText("在此输入经度、纬度和k值，用半角逗号分隔：")
        #让地址栏能响应回车按键信号
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addSeparator()
        navigation_bar.addWidget(self.urlbar)
        if(not os.path.exists(os.path.curdir + '\\chartHtml\\')):
            os.mkdir(os.path.curdir + '\\chartHtml\\')
        if self.gen.run(0,0,0):
            # success
            # get gen url name and map it into menu action
            self.urlList = os.listdir(os.path.curdir + '/chartHtml')
            for item in self.urlList:
                itemAction = QAction(item.title().replace('.Html', ''), self)
                itemAction.setCheckable(True)
                itemAction.triggered.connect(self.showDataChart)
                self.fileMenu.addAction(itemAction)
        else:
            print("You haven't generate chart html files yet!")

        self.show()

    def showDataChart(self):
        #get actions
        for action in self.fileMenu.actions():
            if action.isChecked():
                url = os.path.abspath("chartHtml/"+action.text()+'.html')
                #remember to unchecked !
                action.setChecked(False)
                self.browser.load(QUrl.fromLocalFile(url))
                self.setCentralWidget(self.browser)
    def showChange(self):
        url = os.path.abspath("chartHtml/随着K值得增长查询时延的变化.html")
        #remember to unchecked !
        #action.setChecked(False)
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)

    def navigate_to_url(self):
        gen2 = g.Gen()
        q = self.urlbar.text()
        a = int(q.split(',')[0])
        b = int(q.split(',')[1])
        c = int(q.split(',')[2])
        if(a>=-180 and a<=180 and b>=-90 and b <= 90):
             gen2.run(a, b, c)
        else:self.urlbar.setText("不合法的输入！")
        #self.gen.run(q.split(',')[0],q.split(',')[1],q.split(',')[2])
    def renew_urlbar(self, q):
        ## 更新输入框内容
        self.urlbar.setText("已输入经度："+q.split(',')[0]+", 纬度："+q.split(',')[1]+", k值："+q.split(',')[2])
        self.urlbar.setCursorPosition(0)
