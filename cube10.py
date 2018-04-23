import os,time
#x,y,z三个坐标都在0到16的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？

def gcd(x,y,z,N):#如果xyz能同时被一个不为1的数整除,就返回false
	for i in range(2,N):
		if not any((x%i,y%i,z%i)):
			return False
	return True
	
def pgcd(x,y,N):
	for i in range(2,N):
		if not any((x%i,y%i)):
			return False
	return True
	
def ans(cnt,pcnt,n):
	#return(3*(n**2)+pcnt*6*n+cnt*4)
	return(27*(n**2)+12*(pcnt*n+cnt)-54*n+28)
	
def solve(n):#此处为边长值
	start = time.clock()
	cnt=0
	pcnt=0
	for x in range(1,n//2+1):
		for y in range(1,x):
			t0=(n-x)*(n-y)
			t1=(n-2*x)*(n-2*y)
			if(pgcd(x,y,n)):
				pcnt+=t0-t1
			for z in range(1,x+1):
				if(gcd(x,y,z,n)):
					cnt+=t0*(n-z)-t1*(n-2*z)
					
	for x in range(n//2+1,n):
		for y in range(1,x):
			tmp=(n-x)*(n-y)
			if(pgcd(x,y,n)):
				pcnt+=tmp
			for z in range(1,x+1):
				if(gcd(x,y,z,n)):
					cnt+=tmp*(n-z)
	#pcnt=2*pcnt+2*n-3
	#cnt=3*cnt+3*n*n-9*n+7
	print("cnt=",cnt)
	print("pcnt=",pcnt)
	print("final answer=",ans(cnt,pcnt,n))

	end = time.clock()
	print("运算耗时 %f秒\n" % (end  - start))
	return 0
'''
n=90
for i in range(1,n+1):
	print("n =",i)
	solve(i+1)'''
solve(17)
solve(100+1)
os.system("PAUSE")