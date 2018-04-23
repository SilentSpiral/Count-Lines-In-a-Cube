import os,time
#x,y,z三个坐标都在0到16的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？
#定积分换限
def gcd(a,b):
    if a%b == 0:  
        return b  
    else :  
        return gcd(b,a%b) 
	
def ans(cnt,pcnt,n):
	return((27*n-54)*n+12*(pcnt*n+cnt)+28)
	
def solve(n):#此处为边长值+1
	start = time.clock()
	cnt=0
	pcnt=0
	for x in range(1,n//2+1):
		for y in range(1,x):
			r=gcd(x%y,y)
			tmp0=(n-x)*(n-y)
			tmp1=(n-2*x)*(n-2*y)
			if(r==1):
				pcnt+=tmp0-tmp1
				cnt+=tmp0*((2*n-y)*y-x)-2*tmp1*((n-y)*y-x)#c1=(2*n-y)*(y-1)//2   c2=(n-y)*(y-1)
			else:
				c1=(n-1)
				c2=(n-2)
				for z in range(2,y):
					if(gcd(r,z)==1):
						c1+=(n-z)
						c2+=(n-2*z)
				cnt+=2*(tmp0*c1-tmp1*c2)
			
	for x in range(n//2+1,n):
		for y in range(1,x):
			r=gcd(x%y,y)
			tmp=(n-x)*(n-y)
			if(r==1):
				pcnt+=tmp
				cnt+=tmp*((2*n-y)*y-x)				#cnt+=tmp*(2*n-x-y)	c=(2*n-y)*(y-1)//2
			else:
				c=(n-1)                           #z=1单独提出来了
				for z in range(2,y):
					if(gcd(r,z)==1):  #q=n//r 进一步优化失败, 我知道为什么了, 太可惜
						c+=(n-z)   #c=((2*n-y)*(y-1)-(2*n-r-q*r)*q)//2
				cnt+=2*tmp*c

	print("cnt=",cnt)
	print("pcnt=",pcnt)
	print("final answer =",ans(cnt,pcnt,n))

	end = time.clock()
	print("运算耗时 %f秒\n"%(end - start))
	return 0
'''
n=400
for i in range(1,n+1):
	print("n =",i)
	solve(i+1)'''
#solve(17)
solve(400+1)

os.system("PAUSE")