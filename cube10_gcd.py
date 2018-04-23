import os,time
import numpy as np
#x,y,z三个坐标都在0到16的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？

def _gcd(a,b):
    if (np[a][b])>0:
        return np[a][b]
    if a%b == 0:  
        return b  
    else :  
        np[a][b]=_gcd(b,a%b) 
        return np[a][b]
        #return _gcd(b,a%b) 
def gcd(a,b):
    if a%b == 0:  
        return b  
    else :  
        return gcd(b,a%b) 
    
def ans(cnt,pcnt,n):
    #return(3*(n**2)+pcnt*6*n+cnt*4)
    return(27*(n**2)+12*(pcnt*n+cnt)-54*n+28)
    
def solve(n):#此处为边长值+1
    cnt=0
    pcnt=0
    start = time.clock()
    for x in range(1,n//2+1):
        for y in range(1,x):
            t0=(n-x)*(n-y)
            t1=(n-2*x)*(n-2*y)
            g=gcd(x,y)
            if(g<2):
                pcnt+=t0-t1
            for z in range(1,x+1):
                if(gcd(g,z)<2):
                    cnt+=t0*(n-z)-t1*(n-2*z)
                    
    for x in range(n//2+1,n):
        for y in range(1,x):
            tmp=(n-x)*(n-y)
            g=gcd(x,y)
            if(g<2):
                pcnt+=tmp
            for z in range(1,x+1):
                if(gcd(g,z)<2):
                    cnt+=tmp*(n-z)

    print("cnt=",cnt)
    print("pcnt=",pcnt)
    print("final answer=",ans(cnt,pcnt,n))
    print("运算耗时 %f秒\n" % (time.clock()  - start))
    return 0
'''
n=90
n+=1
np=[[-1]*n]*n
for i in range(1,n):
    print("n =",i)
    solve(i+1)'''
solve(17)
solve(100+1)
solve(400+1)
os.system("PAUSE")