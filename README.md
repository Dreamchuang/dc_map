(https://github.com/Dreamchuang/dc_map/assets/157662406/2de096fa-b4a2-467e-bd3d-da09b0f081f9)本项目为围栏算法通过输入坐标来获取此坐标对应的省市县test2.py为运行代码

地图上每个省市县的围栏都可以在此网站https://datav.aliyun.com/portal/school/atlas/area_selector
获取本项目已经将所有的省市县获取放到文件夹中test.py为爬虫代码。爬取下来的数据结构可能会不一样因此本项目修改了一些围栏的结构

show()和show2()为测试时使用的画图函数不必理会

fk()为围栏算法用一条射线穿过围栏如果穿过的围栏有奇数个交点就在其中有偶数个交点则在其外部
射线法其实就是从判断点开始，向左边或者右边(下面我们讲解的都是围绕向右做射线的情况包括代码和图示)水平的做一条射线，
判断该射线穿过多边形的次数，如果为奇数则认为该点在区域内部，如果为偶数则认为该点在区域外部。该方法对于复合多边形也能正确的判断。

fk2()为判断某个点是否在围栏群中无论是省市还是县都有可能出现多个围栏群比如本海南省福建省有许多的岛屿因此有很多围栏

xbox()为最小外接矩阵大多数应用的地理围栏多边形都比较简单，但有时也会遇到一些特别复杂的多边形，比如单个多边形的边数就超过十几万条，
这时候对此复杂多边形执行一次射线法也非常耗时因此可以算出每个区的最小外接矩阵先通过判断点是否在最小外接矩阵内。如果在在使用围栏算法，
如果不在就没必要使用围栏算法因此可以节省不少的时间
mm()此函数为计算最小外接矩阵的函数将计算好的外接矩阵存储到map1、map2、map3、中目的是为了节省时间

fun1()函数为提取矩阵的函数
get_file()、get_file2()、get_file3()分别是遍历省市县的函数可以返回省市县的名字和子节点的数量。
可以通过判断子节点的数量来判断还需不需要继续遍历。
每次运行在10ms左右更换成go语言或者java会更快
![image](https://github.com/Dreamchuang/dc_map/assets/157662406/8209e21f-43e0-4ef5-9628-27874a336879)
