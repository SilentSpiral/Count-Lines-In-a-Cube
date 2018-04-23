import os,time
#x,y,z三个坐标都在0到16的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？
#定积分换限
def gcd(a,b):
    if a%b == 0:  
        return b  
    else :  
        return gcd(b,a%b) 
	
def ans(cnt,pcnt,n):
	return(27*(n**2)+12*(pcnt*n+cnt)-54*n+28)
	
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
				cnt+=tmp0*(2*n-y-x)-2*tmp1*(n-y-x)
			for z in range(1,y):
				if(gcd(r,z)==1):
					cnt+=2*(tmp0*(n-z)-tmp1*(n-2*z))
						
	for x in range(n//2+1,n):
		for y in range(1,x):
			r=gcd(x%y,y)
			tmp=(n-x)*(n-y)
			if(r==1):
				pcnt+=tmp
				cnt+=tmp*(2*n-x-y)
			for z in range(1,y):
				if(gcd(r,z)==1):
					cnt+=2*tmp*(n-z)

	print("cnt=",cnt)
	print("pcnt=",pcnt)
	print("final answer =",ans(cnt,pcnt,n))

	end = time.clock()
	print("运算耗时 %f秒\n"%(end - start))
	return 0
'''
n=210
for i in range(1,n+1):
	print("n =",i)'''
#solve(16+1)
solve(17)
solve(100+1)
solve(400+1)

os.system("PAUSE")