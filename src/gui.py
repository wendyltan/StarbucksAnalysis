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

        # 设置浏览器
        self.browser = QWebEngineView()
        url = os.path.abspath('icons/foobar.html')
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl.fromLocalFile(url))
        # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)

        #adding menu...
        menubar = self.menuBar()
        self.fileMenu = menubar.addMenu('显示图表')
        gen = g.Gen()
        if gen.run():
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





