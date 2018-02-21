
# 数据科学导论

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
<br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可。

去年暑假我开始写一些数据科学入门的笔记，现在回头看惨不忍睹，不至于误人子弟（所以我就赖着不删了），但没达到我现在的期望，决定重写。

我用朴素的厨房观看待人类思想：知识的生产就像炒菜，先要有炊具，然后有原材料，加上心灵手巧就能做一盘好菜。数据科学也一样，说来说去核心工具有三大件：数理统计、机器学习、数据编程，带上工具、数据和脑子，你就可以自称数据科学家去解决问题了。数理统计是用数理逻辑分析数据，机器学习从数据里提炼关键信息用于预测，数据编程做数据的维护工作，怎么存储、怎么读取、怎么可视化、怎么高效压榨计算机的性能。

说一下我对数理统计和机器学习的理解。数理统计讲求严格的证明推导，是从空地起高楼；机器学习归纳从数据里寻找规律的方法（就是 SICP 说的「抽象」），然后反复调用这些方法用来预测。谈不上高低，数理统计是演绎，对结论的解释和因果推断更到位，令人信服，但预测效果不怎么样；机器学习是归纳，预测得准，但说不清预测是怎么来的。同时了解这两门学科是有必要的，而且很多学者在努力结合这两者。

这个专栏是涉及数理统计、机器学习和数据编程三个方面的学习笔记，主要关注数理统计和机器学习。为什么要有笔记？笔记通常比教科书更简洁，比视频和课件更方便阅读，适合读者按图索骥、复习和总结。很多人讲数据科学这么多东西要学怎么学得完，我的看法是，做不到样样精通，因此更需要有一个地图，这样遇到问题了能知道是哪里出了问题、要去哪里找答案。那我写得完吗？当然写不完... ~~拖延症最擅长的就是做完成不了的承诺了，~~ 所以欢迎大家投稿和指责。

由于 Github 不渲染数学公式，我把大致梳理的数理统计和机器学习思路放在了 [preface.ipynb](/preface.ipynb) 里。

虽然我不喜欢列书单这种营造焦虑感的事情，但考虑到这份笔记的涵盖范围，有必要列出参考书目和课程：

[Practical Data Science](http://www.datasciencecourse.org/lectures/)  
这门课是 CMU 面向本科生和硕士生的数据科学导论课程，今年第一次把课程视频公开，同时附有详细的笔记和作业。

[Statistics 110: Probability](https://projects.iq.harvard.edu/stat110/youtube)  
这是 Harvard 面向本科生的数理统计课程。

[Learning From Data](https://work.caltech.edu/telecourse.html)  
这门课是 Caltech 面向本科生的机器学习线上公开课程，相比于 Cousera 上 Ng 的课程，理论性更强。

[Statistical Learning](https://lagunita.stanford.edu/courses/HumanitiesSciences/StatLearning/Winter2016/info)  
这门课是 Stanford 面向无统计背景学生的统计学习线上公开课程，统计学习和机器学习非常相似，但数理统计的味道更浓。

Rice, J. A. (2007) Mathematical statistics and data analysis. 3rd ed.  
Wackerly, D. D., Mendenhall, W. and Scheaffer, R. L. (2008) Mathematical statistics with applications. 7. ed.  
Wasserman, L. (2013) All of statistics: a concise course in statistical inference.  
这三本都可用作学习数理统计的参考书。

笔记更新时间不定，也不会按顺序写，有空就零星地想怎么写就怎么写，还会有一些数据分析。最好的跟踪方式是 [RSS](https://rss.lilydjwg.me/zhihuzhuanlan/introdatascience)，[知乎专栏](https://zhuanlan.zhihu.com/introdatascience)和我的[ Github 仓库](https://github.com/iewaij/introDataScience)。

对了，我目前感觉最好的数据科学 IDE 是 [Jupyter Lab](https://github.com/jupyterlab/jupyterlab)，无论是写作还是写代码都好用。

## 目录
- [ ] [前言](/preface.ipynb)
- [ ] 数理统计笔记
    - 概率
    - 离散随机变量及其概率分布
    - 连续随机变量及其概率分布
    - 随机变量函数
    - 联合概率分布
    - 期望
    - 大数定理及中心极限定理
    - 估计
    - [最小二乘法线性回归](http://lijiawei.cc/introDataScience/OLS.html)

- [ ] 机器学习笔记

- [ ] 数据编程笔记

- [ ] 数据分析

## Changelog, Corrections and Updates
2018-02-21 添加 CC BY-NC-SA 4.0 条款
2018-02-21 最小二乘法线性回归
2018-02-01 前言
