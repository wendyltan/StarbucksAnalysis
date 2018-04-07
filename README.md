# StarbucksAnalysis
A analytical project for Starbucks dataset


## Index/src
 - util :工具类所在目录
    - csv2xlsx :csv格式转xlsx格式
    - excel2sql: xlsx转sqlite db格式。
    - helper: 一些在模块中反复使用的函数
 - drawChart :画图模块，大部分画图函数请放在这里
 - models:数据库模型类，使用sqlcodegen 生成的请勿改动
 - query :请在这里编写大部分查询数据的函数
 - main :主模块
 - init :初始化
 - dataset :原始数据excel文件目录

## 历史开发进度
- 18/4/7: **jasonli** 加入`qt_browser.py'文件，尝试pyqt实现浏览图表网页的功能，但是只能打开已保存的本地网页，不能实时生成，与main.py的关联有些问题。这些地图都是可以操作的动态页面，而非静态图片。
<img  src="https://github.com/2015SoftwareAnalysisTeam/StarbucksAnalysis/blob/master/src/icons/test.gif" />

- 18/3/25: **jasonli** 可以通过`tk.py` 文件启动GUI，点击按钮打开地图，接下来将修改为使用combobox下拉列表实现多种地图。同时修改了`main.py`,将部分功能改为可调用函数。**Wendy**将`tk.py`更改为`gui.py`并将启动函数放置到`main.py`保证gui部分的整洁和低耦合。

- 18/3/20-3/21 **huangyep** 完成地图函数编写，**Wendy** 进行优化并抽象部分函数

- 18/3/19前 : **Wendy**粗略对模块分块，编写部分函数


