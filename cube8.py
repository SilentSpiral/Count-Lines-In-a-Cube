import os,time
#x,y,z三个坐标都在0到16的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？
#合并循环
def gcd(x,y,z,N):#如果xyz能同时被一个数整除,就返回false
	for i in range(2,N):
		if not any((x%i,y%i,z%i)):
			return False
	return True
	
def pgcd(x,y,N):
	for i in range(2,N):
		if not any((x%i,y%i)):
			return False
	return True
	
def ans(sum1,sum2,n):
	return(3*(n**2)+sum2*2*3*n+sum1*4)
	
def solve(n):#此处为边长值+1
	start = time.clock()
	sum1=0
	sum2=0
	for x in range(1,n):
		for y in range(1,n):
			if(pgcd(x,y,n)):
				K=n/max(x,y)
				if K>=2:
					sum2+=(x+y)*n-3*x*y
				else:
					sum2+=(n-x)*(n-y)
			for z in range(1,n):
				if(gcd(x,y,z,n)):
					#if not (pgcd(x+y-z,z,n)):
					#	print(x,y,z)
					K=min(K,n/z)
					if K>=2:
						sum1+=(n-x)*(n-y)*(n-z)-(n-2*x)*(n-2*y)*(n-2*z)
					else:
						sum1+=(n-x)*(n-y)*(n-z)
	print("sum1=",sum1)
	print("sum2=",sum2)
	print("final answer=",ans(sum1,sum2,n))

	end = time.clock()
	print("运算耗时 %f秒\n" % (end  - start))
	return 0
'''
n=16
for i in range(1,n+1):
	print("n =",i)
	solve(i+1)'''
	
solve(17)
solve(101)

os.system("PAUSE")