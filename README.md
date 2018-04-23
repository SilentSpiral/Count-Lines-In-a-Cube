# Count Lines In a Cube

大佬提出的问题, 来源又双叒叕是[oeis:](http://oeis.org/A222267)   
> x,y,z三个坐标都在0到 n(原题是16)的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？  

---
<p style="font-size:em;text-align:center"> "我要向锤雷世界通话"</p>

## 雪地工程 ( Version 1 )  
寒假的时候试着写了一下, 期望以python的集合来搞定这个问题, 于是有了代码的第一个版本  

于我来说问题的瓶颈在于直线查重是困难的, 需要一种方式把每一个直线唯一的标示出来以供查重,
我的想法是这个直线一定会在最外层的六个平面中的两个或者更多平面上有交点, 不妨以这些交点来唯一的标示每一个直线,(比较像三体里的雪地工程) 即每个直线由一个六个交点坐标的六元组来表示   

- 若不存在交点或直线在某一平面上(无数个交点), 则计为None   
- 若交点在正方体棱或顶点, 则此交点算入相关的每一个平面上  

譬如n=4的时候, (1,1,1)和(2,2,2)所确定的直线可表示为((0,0),(0,0),(0,0),(1,1),(1,1),(1,1))  

结果并不如愿, n=1~3时答案都对, n=4时算得ans=6025, 多了, 我猜也许是浮点数精度问题  
n=16时,数据太大跑不出来, 内存没炸也真是神奇

## 航迹 ( Version 2 )   
这个灵感是返校后想到的, 为了这个还特地去复习直线在空间中的表示方法.  
一个空间直线可以由直线上某一点及方向向量确定, 但不是唯一确定, 因为点只要在直线上即符合要求, 方向向量也可以倍增或者倍减   
想要唯一确定直线, 需要怎么做呢  

对于方向向量而言, 由于直线都是由整点两两连线确定, 所有每个方向向量都可以化为一组互质的正整数, 我们可以通过一个三重循环生成(0,0,0)出发终点且在正方体内(及其表面,下同)所有互质的向量, 之后遍历这些向量, 对每一个向量遍历一遍所有的点  

既然直线是由立方体内及其表面上的整点确定的, 那么直线一定经过正方体内或其表面的整点, 这样一来, 我们可以对于每个向量维护一个对应此正方体且初值皆为0的数组, 对于每一个为0的点, 若通过当前向量可达正方体内别的点, 则该点置1, 经此点达到的其他点置-1, (在想象中的正方体里, 每一个点生成直线的染色过程就像三体舰队留下航迹一样, 因而得名), 点的遍历完成后统计数组里1的个数即可  

因为互质求起来遇到0比较麻烦,故将向量分类如下(名字乱起的, 勿深究):  

- 原则: 不互质则平凡, 有0则降维  
- 三维非平凡向量: xyz皆不为0, 且xyz没有公因子(这里并不是两两互质)  
- 二维非平凡向量: xyz有且只有一个为0, 且其余二者互质  
- 一维向量: (0,0,1) or (0,1,0) or (1,0,0)  
- 平凡向量: 在其所在维度下不满足互质要求   

其中一维向量可生成直线3(n+1)<sup>2</sup>个  

**三维非平凡向量** 所生成直线的总数 (记作sum1,后改为cnt) 需要乘**4**  
因为一个顶点生成的所有向量都可以被其体被对角线连接的另一顶点对应表示, 譬如(0,0,0)指向(x,y,z)的向量与(n,n,n)指向(n-x,n-y,n-z)的向量   
立方体共有4对顶点, 分为4组, 每一个顶点生成的三维向量不可被组外的顶点生成(而生成的二维向量可以,这也是为什么把二维三维的分开考虑)   

**二维非平凡向量** 在平面上生成的直线总数 (记作sum2,后改为pcnt) 要乘 **6(n+1)**  
正方形内顶点可分为 **两组**  
而后正方体内可以找到平行于xoy,yoz,zox的平面各 **(n+1)** 个  

answer=3(n+1)<sup>2</sup>+4\*sum1+2\*3\*(n+1)\*sum2  

在写代码的时候,由于觉得三个数调用好多遍求公因子的函数太麻烦, 所以写了个o(n)的四不像来判断是否互质  
``` python
def gcd(x,y,z,n):
    for i in range(2,n):
        if not any((x%i,y%i,z%i)):
            return False
    return True
```
具体在每一个点通过向量对其他点染色时, 我会事先计算向量的模长, 再用体对角线长度除以该值, 记作k, 每一个点生成的通过-k到k个向量,都可以遍历这条直线在立方体里面的所有整点  

时间复杂度O(n<sup>6</sup>),空间复杂度O(n<sup>3</sup>)  
**跑n=16时耗费40秒左右, 事实上的第一个可行版本, 能够做出来已经是0的突破了**

## version 3  
做完versoin2后, 入睡前猛然想到-k到k的遍历是不必要的, 并将此作为一个猜想向北锤世界留言  
第二天尝试了一下, 确实猜想是对的  

> 解释:  
> 向量(X,Y,Z), 点(a2,b2,c2)若可通过该向量被点(a1,b1,c1)染色, 则必有a2＞a1,b2＞b1,c2＞c1  
> 否则一定会先遍历到(a2,b2,c2),此时已经将(a1,b1,c1)染色, 不会再遍历该点  
> 所以-k到k的遍历是没有必要的  

代码只减少了一行, 时间空间复杂度仍是O(n<sup>6</sup>)和O(n<sup>3</sup>)  
**跑n=16时耗费20秒左右**

## version 4&5  
乏善可陈  
第四版把之前的染色后统计改为了在循环中cnt+1, 以及把列表改成了bool型, 并未有显著加速  
第五版仅仅做了些模块化的工作, 把主过程拆成了一个个函数, 事实证明这个工作开始的过早了, 后面的代码改进还需要再把这些模块重新rua到一起  

## 科学边界 (version 6)  
鉴于我们在第三版里染色全改成了单向的  
那么对于向量(X,Y,Z)而言, 并不需要遍历到x＞n-X, y＞n-Y, z＞n-Z的这些点  
每一个向量的遍历范围都有其自己的边界  
故得名**科学边界**  
``` python
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
```
循环结构更改如下:   
``` python
for x in range(n+1-X):
    for y in range(n+1-Y):
        for z in range(n+1-Z):
```

时间空间复杂度仍是O(n<sup>6</sup>)和O(n<sup>3</sup>)  
**跑n=16时耗费4秒左右**  

## 降维打击 (version 7)  
算是一个历史性进展了, 时间复杂度由O(n<sup>6</sup>)降到O(n<sup>3</sup>)  
空间复杂度仍是O(n<sup>3</sup>), 因为仍需保存非平凡向量  

受到科学边界的启发, 我发现有些点在遍历时是无用的, 能不能进一步削减遍历范围呢?  
三维不好想, 不妨先想明白二维的形式  
![](https://github.com/SilentSpiral/Count-Lines-In-a-Cube/blob/master/scienceEdge.png?raw=true)  
此图是为n=12的情形, 图中向量为(5,3), 黑色方框为其科学边界  
观察可知蓝色方框内的点必定可达黑色框内其他点  
故黑色方框减去蓝色方框剩下的格点,可以唯一的表示出该向量在正方体内生成的所有直线  
统计其个数便可得该向量生成直线的个数  
**cnt = (n-x)(n-y) - (n-2x)(n-2y)**  
应该注意到, 这其实是在隐性要求 **(n-2x)(n-2y)** 都大于0   
如果 **2x＞n** 则会有蓝色方框被挤出正方形以外, 不再被统计  
此时有**cnt = (n-x)(n-y)**  

而后猜想三维的形式, 对于其是否奏效并无绝地的把握  
n＞2\*max(x,y,z)时:  
cnt = (n-x)(n-y)(n-z) - (n-2x)(n-2y)(n-2z)   
else:  
cnt = (n-x)(n-y)(n-z)  

幸运的是跑通了, 答案无误, 心有余悸  
炼丹,炼丹......  
时间复杂度**O(n<sup>3</sup>)**, 空间复杂度O(n<sup>3</sup>)  
**n=16时耗时约0.02秒**  
**n=100时耗时约17秒**  

## version 8  
这个版本主要是把直线计数写进生成向量的循环里了,也就不必保存向量了,空间复杂度跳楼大甩卖  
以及把二维时的二重循环合并进三维时的三重循环中  

发现传入n(正方体边长)时, 主过程里面几乎全是n+1参与运算  
经锤雷大神指点, 改为传入n+1(正方体边上点的个数), 后面的版本都沿袭了这个     

时间复杂度O(n<sup>3</sup>), 空间复杂度**O(1)**  
**n=16时耗时约0.016秒**  
**n=100时耗时约17秒 (你个不争气的玩仍)**  

## version 9  
我们考虑到了正方体四对顶点的对称性, 所以生成向量时实际上减小了3/4的工作量  
但对称性仍然没有用尽    

这个版本里又将工作量降低了2/3, 希望不靠几何的前提下说清楚吧, 毕竟画图废  
三维可以模糊的分成三类分别是  
{A: x最大; B: y最大; C: z最大}  

进一步处理  

- A：x最大，y≤x，z<x  
- B：y最大，z≤y，x<y  
- C：z最大，x≤z，y<z  
- D：x=y=z  
(这里添等号的方式一共只有两种,都可以)  
ABC只用算其中一类即可, 结果乘3再加上D的结果就可以了  

时间复杂度O(n<sup>3</sup>), 空间复杂度O(1)  
**n=16时耗时约0.005秒**  
**n=100时耗时约5.5秒**       

## version 10 & 10_gcd  
循环中需要判断 if n＞2\*max(x,y,z)  
因为在第九版中改成了x最大, 所以有max(x,y,z)=x  
但并不需要再做比较, 可以直接将最外层x的循环拆开  
``` python
for x in range(1,n//2+1):  
    ......
for x in range(n//2+1,n):  
    ......
```


时间复杂度O(n<sup>3</sup>), 空间复杂度O(1)  
**n=16时耗时约0.005秒**  
**n=100时耗时约5.2秒**  

gcd版本是用O(logn)的gcd函数代替了O(n)的原有遍历判断是否公因子的函数  
没想到居然可以快这么多  
**n=16时耗时约0.0011秒**  
**n=100时耗时约0.18秒**  
**n=400时耗时约12秒**  

## version Xplus   
第九版虽改进了生成向量的遍历过程  
但仍有对称未用尽, 事实上剩余的对称性是难以利用的, 当初也考虑过, 但并未实现  
后来发现可以把第九版的遍历范围当作跳板, 即仅需考虑由对称生成第九版代码中的范围即可  

- A：x最大，y≤x，z<x  => { x≥y＞z;   x＞z＞y;   x＞z=y}    
- B：y最大，z≤y，x<y  => { y≥z＞x;   y＞x＞z;   y＞x=z}    
- C：z最大，x≤z，y<z  => { z≥x＞y;   z＞y＞x;   z＞y=x}    
- D：x=y=z  

至此我自以为对称性被压榨到极致了, 仅需遍历所有向量的1/24即可  
除此之外也用了几个临时变量减少重复运算  
**从此算法再无可读性**
---

**n=16时耗时约0.0007秒**  
**n=100时耗时约0.11秒**  
**n=400时耗时约7.2秒**   

## version Xplusplus   
在循环中提取公因式, 显著减少乘法的运行次数  
**n=400时耗时约6秒**   

## version Xplusplusplus   
若r=1, 则必有gcd(r,z)=1  
这里不必对于每个z都调用gcd  
在r=1的时候cnt的增量可由等差数列求和得到  
原本不觉得这个会有多少优化, 仅仅试着改了一下  
没想到效果拔群  
**n=400时耗时约2.8秒**

## version Xplusplusplusplus   
当r不为1时, 按照等差数列求和失败
具体来说因为r可能是合数, 所以要先分解再容斥原理才能够求和

后来想到了利用周期性的解决方案
z的遍历范围以r为周期划分
周期内遍历, 周期间根据周期个数等差求和
最后不足一周期者再单独求和即可
**n=400时耗时约0.43秒**


























