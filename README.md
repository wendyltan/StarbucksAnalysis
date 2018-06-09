# StarbucksAnalysis
An analytical project for Starbucks dataset

## Requirement
 
### Iteration 1
- RQ1

    1.在世界地图上显示所有店铺的位置
    当选中某个店铺时，可以看到店铺的详细信息，如编号、名称、地址、邮编、电话等
    
    2.在将属于不同时区的店铺用不同颜色的点显示，统计每个时区中店铺的数量或密度，并可视化的展示统计结果
    
    3.根据国家和经纬度将地图划分成不同的区域，用渐变色标识每个区域店铺数量
    举例：区域涂为深红色表示店铺数量/密度最高、正红色表示表示店铺数量/密度中等、浅红色表示表示店铺数量/密度较低、白色表示该区域没有店铺
    
    4.统计每个国家拥有店铺的数量/密度，并可视化地给出统计结果

### Iteration 2
- RQ1——不同时区店铺数量渐变图：

    + 是第2轮迭代中“在将属于不同时区的店铺用不同颜色的点显示”的修改版
    
    + 用渐变色标识每个时区的店铺数量

    + 举例：店铺数量多的时区中的点用深红色、数量中等用正红色、数量少用浅红色
- RQ2——距离top-k查询：
    + 用户输入经纬度和一个参数k，展示距离其最近的k个星巴克
        
        1.直接根据经纬度计算距离即可，无需考虑建筑物、道路等因素的影响
        
        2.如果用户输入的经纬度不合法，需要提示用户。
        
        3.对用户的每一次输入，展示查询时延（即从查询发出，到结果返回所需要的时间）
    + 用户输入经纬度，可视化展示随着k的增长查询时延的变化

### Iteration 3
- RQ1—— 如果第3轮的查询执行较慢，则需要显示查询执行的进度条
- RQ2——距离range查询：
    
    1.用户输入经纬度（la,lo）和距离半径r，展示以（la,lo）为中心，r为半径内的所有店铺
    
    2.用户输入经纬度，可视化展示随着k的增长查询时延的变化
- RQ3—— 关键字+距离top-k查询
    
    1.用户输入关键词和经纬度（la,lo），展示与（la,lo）最近的k个匹配关键词的店铺
    
    2.如果不存在完全匹配关键词的店铺，则需要想办法找到与关键词相似的店铺（先按相似度排序，相似度相同时按距离排序）
### Iteration 4
- RQ1——店铺评分和展示评分功能

    1.用户可以点击某个查询结果里的店铺，输入对该店铺的评分（0到10分）
    
    2.如果某个店铺曾经被输入评分，则下次查询时展示该评分；
    
    3.如果某店铺被多次输入评分，则展示评分的平均值

    4.评分高于8分的店铺在top-k、range、top-k+关键词的查询结果里用特殊标记标明

- RQ2——完善功能+重构

    之前迭代中可能存在了很多遗留问题没有解决，在本轮迭代中解决它们

- RQ3——将整个项目打包成一个exe文件

    无需安装环境就可以执行
## Require package
- `fuzzywuzzy` at least `0.16.0`
- `pandas` at least `0.22.0`
- `ploty` at least `2.5.0`
- `pycountry` at least `18.2.23`
- `PyQt5` at least `5.10.1`
- `python-Levenshtein` at least `0.12.0`

## Usage
Just run `main.py`

## Project Structure
- Folder:
    + *chartHtml* : Store the generated html files
    
    + *dataset*: Store the orginal dataset(xlsx and csv file)
    
    + *guiHelper* : Extra gui ,like table or dialog,etc..
    
    + *icons* : icons for main gui
    
    + *test*: simple test files
    
    + *util*: most of the `.py` deal with requirements go in here
- Scripts:
    + **drawChart.py**: use to draw Map.All drawing method place here.
    
    + **gui.py** : main user interface
    
    + **main.py** : run this to exec the program
    
    + ~~**models.py**~~ : deprecated after getDataframe() is invoked
    
    + ~~**query.py**~~ : deprecated after getDataframe() is invoked

## 历史开发进度
- 18/6/9:
    + 全员进行了一次目录结构的重构，并且抽象出一些类运用了三种设计模式
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


