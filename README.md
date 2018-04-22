# Count Lines In a Cube

大佬提出的问题, 来源又双叒叕是[oeis:](http://oeis.org/A222267)   
> x,y,z三个坐标都在0到 n(原题是16)的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？  

---
<p style="font-size:em;text-align:center"> "我要向锤雷世界通话"</p>

## 雪地工程 ( Version 1 )  
寒假的时候试着写了一下, 期望以python的集合来搞定这个问题, 于是有了代码的第一个版本  

于我来说问题的瓶颈在于直线查重是困难的, 需要一种方式把每一个直线唯一的标示出来以供查重,
我的想法是这个直线一定会在最外层的六个平面中的两个或者更多平面上有交点, 不妨以这些交点来唯一的标示每一个直线,(比较像三体里的雪地工程) 即每个直线由一个六个交点坐标的六元组来表示, 
若不存在交点或直线在某一平面上(无数个交点), 则计为None, 
若交点在正方体棱或顶点, 则此交点算入相关的每一个平面上  

譬如n=4的时候, (1,1,1)和(2,2,2)所确定的直线可表示为((0,0),(0,0),(0,0),(1,1),(1,1),(1,1))  

结果并不如愿, n=1~3时答案都对, n=4时算得ans=6025, 多了, 我猜也许是浮点数精度问题  
n=16时,数据太大跑不出来, 内存没炸也真是神奇

## 航迹 ( Version 2 )   
这个灵感是返校后想到的, 为了这个还特地去复习直线在空间中的表示方法.  
一个空间直线可以由直线上某一点及方向向量确定, 但不是唯一确定, 因为点只要在直线上即符合要求, 方向向量也可以倍增或者倍减   
想要唯一确定直线, 需要怎么做呢  

对于方向向量而言, 由于直线都是由整点两两连线确定, 所有每个方向向量都可以化为一组互质的正整数, 我们可以通过一个三重循环生成(0,0,0)出发终点且在正方体内(及其表面,下同)所有互质的向量, 之后遍历这些向量, 对每一个向量遍历一遍所有的点  

既然直线是由立方体内及其表面上的整点确定的, 那么直线一定经过正方体内或其表面的整点, 这样一来, 我们可以对于每个向量维护一个对应此正方体且初值皆为0的数组, 对于每一个为0的点, 若通过当前向量可达正方体内别的点, 则该点置1, 经此点达到的其他点置-1, 点的遍历完成后统计数组里1的个数即可  

因为互质求起来遇到0比较麻烦,故将向量分类如下(名字乱起的, 勿深究):  

- 原则: 不互质则平凡, 有0则降维  
- 三维非平凡向量: xyz皆不为0, 且xyz没有公因子(这里并不是两两互质)  
- 二维非平凡向量: xyz有且只有一个为0, 且其余二者互质  
- 一维向量: (0,0,1) or (0,1,0) or (1,0,0)  
- 平凡向量: 在其所在维度下不满足互质要求   

其中一维向量可生成直线3(n+1)<sup>2</sup>个  

**三维非平凡向量**所生成直线的总数(记作sum1,后改为cnt)需要乘**4**  
因为一个顶点生成的所有向量都可以被其体被对角线连接的另一顶点对应表示, 譬如(0,0,0)指向(x,y,z)的向量与(n,n,n)指向(n-x,n-y,n-z)的向量   
立方体共有4对顶点, 分为4组, 每一个顶点生成的三维向量不可被组外的顶点生成(而生成的二维向量可以,这也是为什么把二维三维的分开考虑)   

**二维非平凡向量**在平面上生成的直线总数(记作sum2,后改为pcnt)要乘 6(n+1)  
正方形内顶点可分为**两组**  
而后正方体内可以找到平行于xoy,yoz,zox的平面各**(n+1)**个  

answer=3(n+1)<sup>2</sup>+4\*sum1+2\*3\*(n+1)\*sum2

在写代码的时候,由于觉得三个数调用好多遍求公因子的函数太麻烦, 所以写了个o(n)的四不像来判断是否互质
``` python
def gcd(x,y,z,n):
	for i in range(2,n):
		if not any((x%i,y%i,z%i)):
			return False
	return True
```



