# 数据科学导论
数据科学那么火，资源那么多，但找遍中文互联网都找不到系统、稍微过得去的笔记，于是就想着自己做一份。我认知中的优秀笔记是 [CS231n 中文笔记](https://zhuanlan.zhihu.com/p/21930884?refer=intelligentunit)，希望这系列笔记能达到它的质量。欢迎加星、合作、提问题、增改内容。

关于数据科学学科介绍的文章、鸡血颇多，因此不再赘述，简而言之，数据科学是计算机科学、统计学、相关领域的结合，以数据、统计思维和计算思维解决问题。而我相信体验数据科学的最佳方式，就是亲手实践。

笔记基于两门数据科学导论课，分别是加州大学伯克利校区 [DS100](http://www.ds100.org/sp17/syllabus) 与哈佛大学 [CS109](http://cs109.github.io/2015/pages/videos.html)，质量颇高。特别感谢制作这两门课程的 Joe Blitzstein、Hanspeter Pfister、Verena Kaynig-Fittkau、Joseph E. Gonzalez、Joseph Hellerstein、Deborah Nolan 和 Bin Yu。

笔记使用 Python3 和 Jupyter Notebook，于[知乎专栏](https://zhuanlan.zhihu.com/introdatascience)亦有更新。

笔记假定读者是以中文为母语、对数据科学感兴趣的入门者，故以中文为主、英语为注释进行创作，原课件为英文而作者亦无中文相关背景，故必然存在翻译纰漏，还请海涵并指出。  
Given the assumption that readers are Chinese speakers and interested in Data Science, this note will be written primarily in Chinese and using English as captions.

## 知识储备
默认读者具有以下知识：
* 统计学基础：理解方差、平均值、线性回归、概率等基本概念
* Python 基础：理解函数、循环、变量、列表生成式、类等基本概念，知道 pip、Jupyter Notebook、NumPy、Pandas 等工具
* 英语技能： 四级或 IELTS 6 分以上水平，能浏览英语文档及文献
* 知识技能：科学上网并使用 Google 查找解决方案

若不具备以上知识，推荐以下资源：
* [data8](http://data8.org)（Python 与统计入门）
* [Learn Python The Hard Way](https://learnpythonthehardway.org/book/)（Python 入门）
* [CS61A](http://cs61a.org)（Python 进阶）
* [Introduction to Computer Science and Programming Using Python](https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017/course/)（Python 进阶）

## 哲学
使用工具，并明了背后的思想；  
内容自洽（self-contained），并提供深入途径；  
能可视化的就不要用文字；  
开源，协作。

## 笔记目录
- [x] [数据收集与整理 Data Collecting, Unboxing and Wrangling](https://nbviewer.jupyter.org/github/iewaij/introDataScience/blob/master/01.%20Data%20Collecting%2C%20Unboxing%20and%20Wrangling.ipynb)

- [x] [探索性数据分析 Exploratory Data Analysis](https://github.com/iewaij/introDataScience/blob/master/02.%20Exploratory%20Data%20Analysis.md)

- [x] [用数据讲故事 Story Telling](https://github.com/iewaij/introDataScience/blob/master/03.%20Story%20Telling.md)

- [ ] 高效演讲 Effective Presentations

- [x] [统计模型 Statistical Models](https://github.com/iewaij/introDataScience/blob/master/04.%20Statistical%20Models.md)

- [ ] 误差与方差 Bias and Variance

- [ ] 回归 Regression

- [ ] 分类 Classification

- [ ] 支持向量机 SVM

- [ ] 决策树和随机森林 Decision Trees and Random Forests

- [ ] 集成方法 Ensemble Methods

- [ ] 最佳实践 Best Practices

- [ ] 推荐系统和并行计算k  Recommendations and MapReduce

- [ ] 大数据处理 Spark

- [ ] 贝叶斯理论和贝叶斯方法 Bayes Theorem and Bayesian Methods

- [ ] 文本聚类 Text and Clustering

- [ ] 深度神经网络 Deep Networks

- [ ] 实验设计 Experimental Design

## 作业目录

### DS100
- [x] [总统候选人推特分析：助手还是本人？ Language in the 2016 Presidential Election](https://github.com/iewaij/introDataScience/blob/master/material/homework/DS%20100/hw2/hw2.ipynb)
- [ ] [数据清洗与探索性数据分析 Data Wrangling and Exploratory Data Analysis](https://github.com/iewaij/introDataScience/blob/master/material/homework/DS%20100/hw3/hw3.ipynb)
- [ ] [爬虫 Crawling the Web](https://github.com/iewaij/introDataScience/blob/master/material/homework/DS%20100/hw5/hw5.ipynb)
- [ ] [预测房价 Prediction on Housing Prices](https://github.com/iewaij/introDataScience/blob/master/material/homework/DS%20100/hw6/hw6.ipynb)

### CS100
- [ ] [探索性数据分析 Exploratory Data Analysis](https://github.com/iewaij/introDataScience/blob/master/material/homework/CS%20109/HW1.ipynb)
- [ ] [进一步探索性数据分析 More Exploratory Data Analysis](https://github.com/iewaij/introDataScience/blob/master/material/homework/CS%20109/HW2.ipynb)
- [ ] [预测与分类 Prediction and Classification](https://github.com/iewaij/introDataScience/blob/master/material/homework/CS%20109/HW3.ipynb)

## 实验目录
- [ ] [概率、分布与频率统计 Probability, Distributions, and Frequentist Statistics](https://github.com/iewaij/introDataScience/tree/master/material/lab/Probability%2C%20Distributions%2C%20and%20Frequentist%20Statistics)
- [ ] [用 sklearn 和 statsmodels 实现回归与逻辑回归 Regression and Logistic Regression in sklearn and statsmodels](https://github.com/iewaij/introDataScience/tree/master/material/lab/Regression%20and%20Logistic%20Regression%20in%20sklearn%20and%20statsmodels)

## Change Log
2017-09-01 完成推特分析作业  
2017-09-01 完成统计模型  
2017-08-17 完成用数据讲故事  
2017-08-11 完成探索性数据分析  
2017-08-10 完成数据收集与整理  
2017-08-09 初始化
