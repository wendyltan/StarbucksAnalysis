

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):
    # noinspection PyUnresolvedReferences
    def tiaoxing(self):
        url = 'file:///C:/Users/J/PycharmProjects/sad/World.html'
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl(url))
        # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)
    def sandian(self):
        url = 'http:///www.ichacha.net'
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl(url))
        # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('星巴克数据分析')
        # 设置窗口图标
        self.setWindowIcon(QIcon('/icons/star.png'))
        # 设置窗口大小
        self.resize(1200, 800)
        self.show()

        # 设置浏览器
        self.browser = QWebEngineView()
        url = 'file:///C:/Users/J/PycharmProjects/sad/icons/foobar.html'
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl(url))
        # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)



        ###使用QToolBar创建导航栏，并使用QAction创建按钮
        # 添加导航栏
        navigation_bar = QToolBar('Navigation')
        # 设定图标的大小
        navigation_bar.setIconSize(QSize(16, 16))
        #添加导航栏到窗口中
        self.addToolBar(navigation_bar)

        #QAction类提供了抽象的用户界面action，这些action可以被放置在窗口部件中
        tiaoxing_btn = QAction('条形图',self)
        sandian_btn = QAction('散点图',self)
        back_button = QAction( '后退', self)

        back_button.triggered.connect(self.browser.back)
        tiaoxing_btn.triggered.connect(self.tiaoxing)
        sandian_btn.triggered.connect(self.sandian)

        # 将按钮添加到导航栏上
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(tiaoxing_btn)
        navigation_bar.addAction(sandian_btn)




# 创建应用
app = QApplication(sys.argv)
# 创建主窗口
window = MainWindow()
# 显示窗口
window.show()
# 运行应用，并监听事件
app.exec_()
