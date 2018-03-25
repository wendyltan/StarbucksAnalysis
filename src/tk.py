from tkinter import *
from tkinter import ttk
from src import *
import src.main as main
class App:
    def __init__(self, master):
        #构造函数里传入一个父组件(master),创建一个Frame组件并显示
        frame = Frame(master)
        frame.pack()

        # 文本框
        #用于辅助调试下拉列表功能
        name = StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
        nameEntered = ttk.Entry(win, width=12, textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
        #nameEntered.grid(column=0, row=1)       # 设置其在界面中出现的位置  column代表列   row 代表行
        nameEntered.focus()     # 当程序运行时,光标默认会出现在该文本框中
        nameEntered.pack()

        # 创建一个下拉列表
        #todo 使用这个下拉列表选择地图类型
        number = StringVar()
        numberChosen = ttk.Combobox(win, width=12, textvariable=number)
        numberChosen['values'] = ('条形图', '散点图')     # 设置下拉列表的值
       # numberChosen.grid(column=1, row=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        numberChosen.pack()

        #创建两个button，并作为frame的一部分
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack() #此处side为LEFT表示将其放置 到frame剩余空间的最左方
        self.tiao = Button(frame, text="Map", command=main.sandian)
        self.tiao.pack()

    def say_hi(self):
        print( "hi there, this is a class example!")

win = Tk()
win.title("星巴克数据分析")
app = App(win)



win.mainloop()
