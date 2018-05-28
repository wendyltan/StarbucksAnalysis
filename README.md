# StarbucksAnalysis
An analytical project for Starbucks dataset

## Require package
update latter...

## Usage
Just run `main.py`

## 历史开发进度
- 18/5/28:
    + **huangyep and Wendy**基本完成查询评分标记需求（但是仍然无法标记颜色）
- 18/5/20:
    + **jasonli**修改一些错误，增加弹窗显示查询信息
- 18/5/19:
    + **Wendy**基本完成迭代四的显示处理
    + **huangyep**基本完成迭代四需求
- 18/4/27:
    + **Wendy**将`helper`部分函数抽象，删掉不必要的注释以及py文件，消减程序赘余
    
- 18/4/26:
    + **jasonli**修改了`gui.py`，给界面加入输入框以获取地址和k值，输入框同时有显示错误信息作用。将需求2.2整合进`genAllChart.py`，修改了该类的run()函数。
    + **huangyep**完成了第三次迭代三个绘图的代码。
    + **jasonli**和**huangyep**对界面和绘图的代码进行整合，程序可用，但代码风格不统一，修改困难。
- 18/4/7: 
    + **huangyep** 添加了新的图表函数，基本完成需求
    + **jasonli** 加入`qt_browser.py`文件，尝试pyqt实现浏览图表网页的功能，但是只能打开已保存的本地网页，不能实时生成，与main.py的关联有些问题。这些地图都是可以操作的动态页面，而非静态图片。
    + **Wendy**修改界面，用菜单action的方式显示图表。更新了图片html静默生成，不会自动弹出。思路是先生成再用qt去load，但是*非常卡顿*,使用pyinstaller打包失败
    
- 18/3/25: 
    + **jasonli** 可以通过`tk.py` 文件启动GUI，点击按钮打开地图，接下来将修改为使用combobox下拉列表实现多种地图。同时修改了`main.py`,将部分功能改为可调用函数。
    + **Wendy**将`tk.py`更改为`gui.py`并将启动函数放置到`main.py`保证gui部分的整洁和低耦合。

- 18/3/20-3/21 **huangyep** 完成地图函数编写，**Wendy** 进行优化并抽象部分函数

- 18/3/19前 : **Wendy**粗略对模块分块，编写部分函数

## Noted

Happy pair programming！Though lack of testing in this project,I find
it really helpful to code beautiful code and easier to debug through pair-programming.


