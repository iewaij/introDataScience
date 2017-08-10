# 数据收集与整理
## 数据收集
尽管互联网上已经有很多数据集，但有时候我们需要的数据不是现成的，需要收集数据。收集这些数据通常有两种方法：爬虫和 API。

爬虫就是写程序把网页上的内容抓取下来，理论上，任何你能在网上看到的数据都是可以用爬虫抓取的，但要遵守法律、网站条款和隐私权，控制爬虫的抓取速度，不要把别人服务器搞垮了。

API 可以理解为网站给程序用的接口，API 给出的数据更友好，但每个网站的 API 格式都不同，需要查阅文档。有些网站不提供 API 接口，不妨去 GitHub 搜一搜，通常能找到开源的非官方 API，这些 API 其实就是打包好的爬虫，你只要调用命令就能获得数据了。

### 爬虫
爬虫首先需要发送请求给服务器，然后服务器会发回网页内容。这个过程有多个库可以使用，例如 [requests](http://docs.python-requests.org/en/master/)。

```Python
import requests
r = requests.get('http://httpbin.org'))
content = r.text
```

发回网页内容后，你就能得到 HTML 代码，HTML 代码构成的就是网页的内容，它们通常长这样：

```HTML
<!DOCTYPE html>
<html>
  <head>
    <title>This is a title</title>
  </head>
  <body>
    <h2> Test </h2>
    <p>Hello world!</p>
  </body>
</html>
```

HTML 代码的特点有：
1. 标签通常成对出现
2. 标题 `<h1></h1> ... <h6></h6>`
3. 段落 `<p></p>`
4. 换行 `<br>`
5. href 内容是链接 `<a href="http://www.example.com/">An example link</a>`

在 Chrome 或者 Safari 浏览器里，你只要右键网页-检查就能找到你需要的数据对应的 HTML 代码。

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fica17mz53j31kw19ch22.jpg)

你可以硬着头皮用正则表达式筛选出你要的数据，更好的方法是用现成的分析 HTML 的工具，例如 BeautifulSoup、[Selenium](http://selenium-python.readthedocs.org/en/latest/index.html)。

```Python
from bs4 import BeautifulSoup

# 把 Requsests 得到的内容传给 BeautifulSoup，得到 bs4 对象
soup = BeautifulSoup(source)

# 查找所有的 <a>...</a> 标签
aTag = soup.findAll('a')

# 得到链接
atag.get('href')

# 得到链接并生成列表
link_list = [l.get('href') for l in aTag]
for l in link_list:
    if l is not None and l[:4] == 'http':
        external_links.append(l)
```

爬取的数据可以用词典保存，Python 还有个很重要的模块叫 [collections](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431953239820157155d21c494e5786fce303f3018c86000)，为数据科学家提供了很多工具，例如加强型词典 defaultdict 和频率计算 Counter。

限于篇幅，爬虫部分就在这里结束。如果你想深入了解，这里有一些爬虫实例：

[使用 urllib2 和 BeautifulSoup 爬取数据科学家所需技能](https://jessesw.com/Data-Science-Skills/)  
[使用 LXML 和 Selenium 爬取洛杉矶 Happy Hour (PyCon 2014 Tutorial)](https://www.youtube.com/watch?v=p1iX0uxM1w8)

### API
网站为了防止 API 被滥用，通常会要求你注册账号，访问 API 的时候要加上你的账号密钥。有些 API 能控制你的账户行为，例如用 Twitter API 可以发推，所以不要让你的密钥出现在你的代码里，而是让代码访问密钥文件得到密钥。

这里有一些有意思的 API：

[Twitter](https://dev.twitter.com/rest/public)  
[烂番茄电影评分](http://developer.rottentomatoes.com/member/register)  
[老司机影视库](https://avgle.github.io/doc/)


#### JSON
有时候 API 发回的是 JSON 格式的数据，JSON 的全称是 JavaScript Object Notation，格式和 Python 中的词典很像，但不好直接处理，需要转换成词典。

```Python
import json
dataDict = json.loads(data)
```

#### 第三方库
有些 API 非常复杂，例如 [Twitter](https://dev.twitter.com/rest/public)，用第三方库会省力很多，例如 [tweepy](http://tweepy.readthedocs.io/)。

## 数据整理
收集数据后，我们先要探索数据 (data discovery， data unboxing)，以对数据有基本的认识。数据可能是「脏」的，或者对我们的工作是无用的，所以还需要整理数据 (data wrangling, data prep, data munging, data transformation)，让数据更好地为分析师服务。

[Kandel et al.](http://db.cs.berkeley.edu/papers/vast12-interview.pdf) (2012) 采访了35位分析师后发现，许多分析师都把大部分时间花在整理数据上，而整理数据的过程，让分析师更了解数据并能提出好的猜想。

> I spend more than half of my time integrating, cleansing and transforming data without doing any actual analysis. Most of time I’m lucky if I get to do any ‘analysis’ at all…  
>   
> … Most of the time once you transform the data ... the insights can be scarily obvious.  

贝尔实验室数学家、R 语言之父 John Tukey 在 1965 年就提出了[类似的见解](https://books.google.com.hk/books?id=C1guHWTlVVoC&lpg=PA554&ots=Gyad7RQzzG&dq=tukey%201965%20the%20flexibility%20of%20the%20informed%20human%20mind&hl=zh-CN&pg=PA554#v=onepage&q=tukey%201965%20the%20flexibility%20of%20the%20informed%20human%20mind&f=false)。Tukey 指出，统计学家要想灵活地分析数据，就必须让数据对使用者更友好，这个过程如此重要，以致于是数学、统计模型、计算机不能比拟的。 

> at all stages of data analysis, the nature and detail of output, both actual and potential, need to be matched to the capabilities of the people who use it and want it … Nothing - not the careful logic of mathematics, not statistical models and theories, not the awesome arithmetic power of modern computers - nothing can substitute here for **the flexibility of the informed human mind**.  

Hoaglin(2003) 有一篇[论文](https://projecteuclid.org/euclid.ss/1076102418)讨论了 John Tukey 的事迹和他对统计学的贡献。

### 整理要点
这里提供一个通用的整理要点，但是整理数据是个主观过程。没有一成不变的规则

#### 结构 (Structure)：数据的形状
* 数据是矩形结构（Rectangular Data）吗？
矩形结构包含表格（用关系代数处理）和矩阵（用线性代数处理）。如果不是这两者，例如 JSON、XML，需要转换成矩形结构（Rectangular Data）。
* 有没有超出定义的数据？例如在日期里出现了 ￥120。
* 数据内有嵌套吗？例如在支出里出现了￥180（住宿）。
* 数据是什么类型？定类数据（nominal）、定序数据（ordinal）还是定量数据（quantitative）？
* 相同类型的数据格式一样吗？例如日期里出现了 4th May 和 04-05-2017

#### 粒度 (Granularity): 主键的精细程度
主键（primary key）指赋予每条数据独特性的指标，例如 `user_id`、`transaction_id`、`(City, State)`。主键的值最多出现一次，主键决定了数据的粒度。根据主键，可以把不同的数据拼合起来。

#### 可信度 (Faithfulness): 数据的真实程度
可信度只能在上下文（context）中检验，如果出现了偏离数据分布太多的异常值（outlier），有三者方法处理：  
1. 删掉
2. 改为最接近的非异常值（non-outlier）
3. 保持数据原样，并添加一栏注明是否为异常值，添加一栏注明修改后的结果。

#### 时间契合度 (Temporality): 数据记录的时间解决问题的有效程度

#### 完整性 (Scope): 数据的完整程度
是否有缺失的数据或者条目？可以利用数字排序推测，比如数据中房间号有101、103、104，那么我们可以认为 102 缺失。

限于篇幅，数据整理要点就说到这，如果你想更深入的阅读，可以试试以下链接：

[The Quartz guide to bad data](https://github.com/Quartz/bad-data-guide)    
中文翻译：[The Quartz 坏数据手册](http://djchina.org/2016/07/12/bad_data_guide/)    
[Research Directions in Data Wrangling, Heer et al. 2011](http://vis.stanford.edu/papers/data-wrangling)  

### 工具
数据科学家使用大量的工具来提高整理和分析数据的效率。

文本编辑器，例如 Atom、Sublime Text，文本编辑器轻量、小地图（mini-map）便于定位、丰富的快捷键，可以方便地对数据进行简单修改、查找替换。

[Trifacta](http://trifacta.com) 是免费的可视化数据整理工具，诞生于斯坦福和伯克利，支持编程操作和智能预测。

UNIX 命令行，可以向操作系统内核直接发送操作指令，省去进入编程环境的步骤，[内核恐慌第28期](https://ipn.li/kernelpanic/28/)回顾了 command line/shell 的历史，有兴趣的可以听一听。 macOS 上可以安装 iTerm2 和 zsh 进行命令行操作。命令行操作也可以在 Jupyter Notebook 中完成，在命令前加上 `!` 即可。

Pandas 是 Wes McKinney 开发的专门用于数据操作的 Python 第三方库，设计参考了 R 语言。

下面我们使用 [movielens](https://grouplens.org/datasets/movielens/latest/) 的数据，演示 UNIX 命令行和 Pandas 的使用。写代码之前，有几个建议：

1. 有问题就 Google。
2. 某种程度上，程序员就是复制粘贴 Stack Overflow 上的代码然后跑通的人。 
3. 使用快捷键。Jupyter Notebook 中，按 `Tab` 自动补全命令；在命令后加上 `?` 可以弹出手册界面，`esc` 退出；写代码时按 `Shift + Tab` 可以更快地显示手册，如下图所示。

![](https://ws1.sinaimg.cn/large/006tNc79gy1fielnrof6zj31120tjafe.jpg)

3. 取有意义的变量名，可以通过变量名判断变量是什么。


### UNIX 命令行
`man something` 手册（manual）的缩写，可以查看任何 UNIX 命令的指引。

`ls -lh movieLens/` 查看 `movieLens/` 文件夹下的文件目录。

```
total 6136
-rw-r--r--@ 1 Jiawei  staff   8.2K Oct 17  2016 README.txt
-rw-r--r--@ 1 Jiawei  staff   179K Oct 17  2016 links.csv
-rw-r--r--@ 1 Jiawei  staff   448K Oct 17  2016 movies.csv
-rw-r--r--@ 1 Jiawei  staff   2.3M Oct 17  2016 ratings.csv
-rw-r--r--@ 1 Jiawei  staff    41K Oct 17  2016 tags.csv
```

`cat movieLens/README.txt` 查看 `README.txt` 文件全文。

`wc movieLens/movies.csv movieLens/ratings.csv movieLens/tags.csv` wc 是 word count 的缩写，查看 `movieLens/movies.csv`、 `movieLens/ratings.csv` 、`movieLens/tags.csv` 文件的行数、词数、字节数。

```
    9126   39127  458390 movieLens/movies.csv
  100005  100005 2438266 movieLens/ratings.csv
    1297    1887   41902 movieLens/tags.csv
  110428  141019 2938558 total
```

`head movieLens/movies.csv movieLens/ratings.csv movieLens/tags.csv` 查看 `movieLens/movies.csv`、 `movieLens/ratings.csv` 、`movieLens/tags.csv` 文件的前10行。

```
==> movieLens/movies.csv <==
movieId,title,genres
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
2,Jumanji (1995),Adventure|Children|Fantasy
3,Grumpier Old Men (1995),Comedy|Romance
4,Waiting to Exhale (1995),Comedy|Drama|Romance
5,Father of the Bride Part II (1995),Comedy
6,Heat (1995),Action|Crime|Thriller
7,Sabrina (1995),Comedy|Romance
8,Tom and Huck (1995),Adventure|Children
9,Sudden Death (1995),Action

==> movieLens/ratings.csv <==
userId,movieId,rating,timestamp
1,31,2.5,1260759144
1,1029,3.0,1260759179
1,1061,3.0,1260759182
1,1129,2.0,1260759185
1,1172,4.0,1260759205
1,1263,2.0,1260759151
1,1287,2.0,1260759187
1,1293,2.0,1260759148
1,1339,3.5,1260759125

==> movieLens/tags.csv <==
userId,movieId,tag,timestamp
15,339,sandra 'boring' bullock,1138537770
15,1955,dentist,1193435061
15,7478,Cambodia,1170560997
15,32892,Russian,1170626366
15,34162,forgettable,1141391765
15,35957,short,1141391873
15,37729,dull story,1141391806
15,45950,powerpoint,1169616291
15,100365,activist,1425876220
```

### Pandas
我们可以用 Pandas 做一些简单的数据操作来整理数据，在后续的章节里我们会更深入地了解 Pandas。

```Python
import pandas as pd # 导入 pandas 模块，缩写为 pd
pd.set_option('display.max_rows', 8) # 设置最多显示 8 行表格
```

#### 导入操作
这里有必要介绍一下索引 (Index) 的概念，索引就像是门牌号，通过索引可以找到索引对应的数据。例如 Python 的列表，可以用 `aList[n]` 来表示 aList 位置 n 上的数据，这个 `[n]` 就是列表的索引。Pandas 有两种数据结构，一维的 Series 和二维的 DataFrame，这两个数据结构都有 Index 对象作为索引，用 Numpy 保存索引外的数据，Series 有 index，DataFrame 有两个，分别是 index 和 columns，index 是纵向的，columns 是横向的。

```Python
# 导入 csv 文件，并把第 0 列设为 index
movies = pd.read_csv('movieLens/movies.csv', index_col=0)
# 导入 csv 文件，不设置 index
ratings = pd.read_csv('movieLens/ratings.csv')
tags = pd.read_csv('movieLens/tags.csv')
```

#### 数据属性

```Python
# 使用 describe() 描述数据，输出结果视情况而定
movies.describe()
```

```Python
movies.dtypes # 查看数据类型
movies.shape # 查看数据形状
movies.index # 查看 index
movies.columns # 查看 columns
```

#### 选择条目
标签 (label) 就是 index 和 column 上不同索引的名字，这些索引可以用整数表示，也可以用 label 表示。

```Python
# 选择前 5 行，两者等价
movies[:5] 
movies.iloc[:5, :]
# 依据 label 选择对应条目，两者等价
movies.title
movies['title']
```

```Python
# 选择前五行的 genres 条目，loc 接受 label，iloc 接受整数
movies.loc[:5, 'genres']
movies.iloc[:5, 1]
# 传入多个列表选择数据，注意传入嵌套列表的列表
movies[['title', 'genres']]
# 与上一条命令等价
showList = ['title', 'genres']
movies[showList]
```

```Python
# 输出一系列布尔值列表
movies['genres'] == 'Comedy' 
# 依据布尔值选择 genres 为 Comedy 的条目
movies[movies['genres'] == 'Comedy'] 
# 选择多个布尔值条件（类型是 Comedy 且标题中含 Gay 的电影）
movies[(movies['genres'] == 'Comedy') 
       & (movies['title'].str.contains('Gay'))]
```

#### Split-apply-combine
[Split-apply-combine](https://pandas.pydata.org/pandas-docs/stable/groupby.html)过程会频繁出现在你的数据科学项目里，简而言之，该过程包括3个步骤:

1. 把数据分组
2. 对每个组应用函数
3. 整合结果

如下图所示，我们把数据分成3组，然后对每个组求均值，最后整合在一块就是一次 split-apply-combine。

![](https://ws3.sinaimg.cn/large/006tNc79gy1fidfd575x7j30dw09ddgu.jpg)

我现在想知道：

- 每部电影的平均得分是多少？
- 平均得分最高多少？哪几部电影得分最高？
- 每位用户的平均打分是多少？

这就需要我把所有评分以 `movieId` 区分，相同 `movieId` 的取平均值后，得到新的表格。用户的平均打分的过程亦是如此，读者可自己尝试。

```Python
groupedRatingPerMovie = ratings['rating'].groupby(ratings['movieId'])
# 注意不是 ratings.groupby('movieId')
groupedRatingPerMovie.describe()
```

```Python
ratingPerMovie = groupedRatingPerMovie.mean() # 计算平均值
maxRating = ratingPerMovie.max() # 得到电影平均分的最高值
maxRating 

# 输出
5.0
```

```Python
# 用布尔值选择数据
maxRatedMovieId = ratingPerMovie[ratingPerMovie == maxRating] 
maxRatedMovieTitle = movies[movies.index.isin(maxRatedMovieId.index)] 
# 得到最高分的电影名称
maxRatedMovieTitle['title']

# 输出
movieId
53                                          Lamerica (1994)
183                                     Mute Witness (1994)
301                       Picture Bride (Bijo photo) (1994)
309       Red Firecracker, Green Firecracker (Pao Da Shu...
                                ...                        
160590                           Survive and Advance (2013)
161944                The Last Brickmaker in America (2001)
162542                                        Rustom (2016)
163949    The Beatles: Eight Days a Week - The Touring Y...
Name: title, Length: 315, dtype: object
```

```Python
# 得到最高分的电影有几次评分？
countPerMovie = groupedRatingPerMovie.count()
maxRatedMovieCount = countPerMovie[countPerMovie.index.isin(maxRatedMovieId.index)]
maxRatedMovieCount

# 输出
movieId
53        1
183       1
301       1
309       3
         ..
160590    1
161944    1
162542    1
163949    1
Name: rating, Length: 315, dtype: int64
```

#### 函数
有些操作比较复杂，可以用 `apply()` 传入函数来操作数据。我想把 movies.csv 里的 genres 变成列表。

```Python
genreSplited = movies['genres'].apply(lambda x: x.split('|'))

# 输出
movieId
1         [Adventure, Animation, Children, Comedy, Fantasy]
2                            [Adventure, Children, Fantasy]
3                                         [Comedy, Romance]
4                                  [Comedy, Drama, Romance]
                                ...                        
163056                 [Action, Adventure, Fantasy, Sci-Fi]
163949                                        [Documentary]
164977                                             [Comedy]
164979                                        [Documentary]
Name: genres, Length: 9125, dtype: object
```

这里使用的 `lambda x: x.split('|')` 是个 lambda 表达式，lambda 表达式就是不取名字、不可重复使用的函数，它等价于：

```Python
def someName(x):
    return x.split('|')
```

以上就是 Pandas 的简单操作，第一次上手必然不熟悉，就像小学你刚接触乘法和乘法表一样，多多练习、熟能生巧。很多操作只要知道即可，用到的时候可以 Google 嘛。

以下是一些深入 Pandas 和其他数据科学工具的好书：

[Python for Data Analysis](https://book.douban.com/subject/25779298/)  
作者就是创造 Pandas 的 Wes McKinney，介绍得非常仔细，但 2012 年出版，有点久远。

[Python Data Science Handbook](https://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb)  
与 Python for Data Analysis  内容差不多，但出版时间是 2016 年 11 月，非常新且作者把内容开源了。

## 作业
[CS109 Lecture Notes: DataScraping](https://github.com/cs109/2015/blob/master/Lectures/02-DataScraping.ipynb)  
[DS100 Homework: Language in the 2016 Presidential Election](https://github.com/DS-100/sp17/blob/master/materials/hw/hw2/hw2.ipynb)

## 致谢
数据科学导论笔记基于加州大学伯克利校区 [DS100](http://www.ds100.org/sp17/syllabus) 与哈佛大学 [CS109](http://cs109.github.io/2015/pages/videos.html) 的课程主页改写，参考了课件、笔记、阅读材料及作业，感谢制作这两门课程的 Joe Blitzstein、Hanspeter Pfister、Verena Kaynig-Fittkau、Joseph E. Gonzalez、Joseph Hellerstein、Deborah Nolan 和 Bin Yu。本文基于 DS100  Week 2 - Data Wrangling，及 CS 109 的 Lecture 2 - Web Scraping, Regular Expressions, Data Reshaping, Data Cleanup, Pandas。

#卡片/Datascience
