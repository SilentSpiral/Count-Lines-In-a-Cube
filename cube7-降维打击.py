import os,time
#x,y,z三个坐标都在0到16的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？
#降维打击
def gcd(x,y,z,N):
	for i in range(2,N):
		if not any((x%i,y%i,z%i)):
			return False
	return True

def vector(n):#此处的n已是n+1
	A=[]
	for x in range(1,n):
		for y in range(1,n):
			for z in range(1,n):
				if(gcd(x,y,z,n)):
					A.append((x,y,z))
	print("共",len(A),"个三维非平凡向量")
	return A

def genlines(x,y,z,n):
	sum=0
	K=n/max(x,y,z)
	if K>=2:
		sum+=(n-x)*(n-y)*(n-z)-(n-2*x)*(n-2*y)*(n-2*z)
	else:
		sum+=(n-x)*(n-y)*(n-z)
	return sum
	
def pgcd(x,y,N):
	for i in range(2,N):
		if not any((x%i,y%i)):
			return False
	return True

def pvector(n):#此处的n已是n+1
	A=[(x,y) for x in range(1, n) for y in range(1, n) if pgcd(x,y,n)]
	return A
	
def pgenlines(x,y,n):
	sum=0
	K=n/max(x,y)
	if K>=2:
		sum+=(x+y)*n-3*x*y
	else:
		sum+=(n-x)*(n-y)
	return sum
	
def ans(sum1,sum2,n):
	return(3*((n+1)**2)+sum2*2*3*(n+1)+sum1*4)
	
def solve(n):#此处为边长值
	start = time.clock()
	a=vector(n+1)
	sum1=0
	for (x,y,z) in a:
		sum1+=genlines(x,y,z,n+1)
	print("sum1=",sum1)
	
	b=pvector(n+1)
	sum2=0
	for (x,y) in b:
		sum2+=pgenlines(x,y,n+1)
	print("sum2=",sum2)
	print("final answer=",ans(sum1,sum2,n))
	
	end = time.clock()
	print("运算耗时 %f秒\n" % (end  - start))
	return 0
'''
n=16
for i in range(1,n+1):
	print("n =",i)
	solve(i)'''
solve(16)
solve(100)

os.system("PAUSE")