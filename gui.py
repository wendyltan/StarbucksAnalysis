# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import *
# import os
# from PyQt5.QtWidgets import *

#
# from src.util import genAllChart as g
#
# class MainWindow(QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # 设置窗口标题
#         self.setWindowTitle('星巴克数据分析')
#         # 设置窗口图标
#         self.setWindowIcon(QIcon('icons/star.png'))
#         # 设置窗口大小
#         self.resize(1200, 800)
#
#         # 设置浏览器
#         self.browser = QWebEngineView()
#         url = os.path.abspath('icons/foobar.html')
#         # 指定打开界面的 URL
#         self.browser.setUrl(QUrl.fromLocalFile(url))
#         # 添加浏览器到窗口中
#         self.setCentralWidget(self.browser)
#
#         #adding menu...
#         menubar = self.menuBar()
#         self.fileMenu = menubar.addMenu('显示图表')
#         gen = g.Gen()
#         if gen.run():
#             # success
#             # get gen url name and map it into menu action
#             self.urlList = os.listdir(os.path.curdir + '/chartHtml')
#             for item in self.urlList:
#                 itemAction = QAction(item.title().replace('.Html', ''), self)
#                 itemAction.setCheckable(True)
#                 itemAction.triggered.connect(self.showDataChart)
#                 self.fileMenu.addAction(itemAction)
#         else:
#             print("You haven't generate chart html files yet!")
#
#         self.show()
#
#     def showDataChart(self):
#         #get actions
#         for action in self.fileMenu.actions():
#             if action.isChecked():
#                 url = os.path.abspath("chartHtml/"+action.text()+'.html')
#                 #remember to unchecked !
#                 action.setChecked(False)
#                 self.browser.load(QUrl.fromLocalFile(url))
#                 self.setCentralWidget(self.browser)
#
#
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit,QInputDialog

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("经纬度")
        self.setGeometry(400,400,300,260)
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("选择经纬度")
        self.myButton.clicked.connect(self.msg)

    # def msg(self):
    #      #后面四个数字的作用依次是 初始值 最小值 最大值 小数点后位数
    #     doubleNum,ok1 = QInputDialog.getDouble(self, "标题","计数:", 37.56, -10000, 10000, 2)
    #      #后面四个数字的作用依次是 初始值 最小值 最大值 步幅
    #     intNum,ok2 = QInputDialog.getInt(self, "标题","计数:", 37, -10000, 10000, 2)
    #      #第三个参数可选 有一般显示 （QLineEdit.Normal）、密碼显示（ QLineEdit. Password）与不回应文字输入（ QLineEdit. NoEcho）
    #     stringNum,ok3 = QInputDialog.getText(self, "标题","姓名:",QLineEdit.Normal, "王尼玛")
    #      #1为默认选中选项目，True/False  列表框是否可编辑。
    #     items = ["Spring", "Summer", "Fall", "Winter"]
    #     item, ok4 = QInputDialog.getItem(self, "标题","Season:", items, 1, True)
    #     text, ok5 = QInputDialog.getMultiLineText(self, "标题", "Address:", "John Doe\nFreedom Street")

    def msg(self):
        doubleNum,ok1 = QInputDialog.getDouble(self, "标题","经度:",0, -180, 180, 2)
        doubleNum,ok1 = QInputDialog.getDouble(self, "标题","纬度:", 0, -90, 90, 2)

#
#
