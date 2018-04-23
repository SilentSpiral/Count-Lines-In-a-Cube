import os,time
#x,y,z三个坐标都在0到16的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？
#科学边界
def gcd(x,y,z,N):
	for i in range(2,N):
		if not any((x%i,y%i,z%i)):
			return False
	return True

def incube(x,y,z,n):
	if all((n>=x,n>=y,n>=z)):
		return True
	return False

def address(x,y,z,N):
	return ((x*N+y)*N+z)

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
	points=[True]*((n+1)**3)
	K=n/max(x,y,z)
	K=int(K)+1 #此处向下取整即可,+1是为了方便后面的range()
	for X in range(n+1-x):
		for Y in range(n+1-y):
			for Z in range(n+1-z):
				if(points[address(X,Y,Z,n+1)]):
					flag=False
					for k in range(1,K):
						if incube(X+x*k,Y+y*k,Z+z*k,n):
							points[address(X+x*k,Y+y*k,Z+z*k,n+1)]=False
							flag=True
						#else:
						#	print(X,Y,Z,x,y,z,K,k)
					if(flag):
						sum+=1
	return sum
	
def pgcd(x,y,N):
	for i in range(2,N):
		if not any((x%i,y%i)):
			return False
	return True

def inplane(x,y,n):
	if all((n>=x,n>=y)):
		return True
	return False

def paddress(x,y,N):
	return (x*N+y)

def pvector(n):#此处的n已是n+1
	A=[]
	for x in range(1,n):
		for y in range(1,n):
			if(pgcd(x,y,n)):
				A.append((x,y))
	print("共",len(A),"个二维非平凡向量")
	return A
	
def pgenlines(x,y,n):
	sum=0
	points=[True]*((n+1)**2)
	K=n/max(x,y)
	K=int(K)+1
	for X in range(n+1-x):
		for Y in range(n+1-y):
			if(points[paddress(X,Y,n+1)]):
				flag=False
				for k in range(1,K):
					if inplane(X+x*k,Y+y*k,n):
						points[paddress(X+x*k,Y+y*k,n+1)]=False
						flag=True
					#else:
					#	print(X,Y,x,y,K,k)
				if(flag):
					sum+=1
	return sum
	
def ans(sum1,sum2,n):
	return(3*((n+1)**2)+sum2*2*3*(n+1)+sum1*4)
	
def solve(n):#此处为边长值
	start = time.clock()
	a=vector(n+1)
	sum1=0
	for (x,y,z) in a:
		sum1+=genlines(x,y,z,n)
	print("sum1=",sum1)
	
	b=pvector(n+1)
	sum2=0
	for (x,y) in b:
		sum2+=pgenlines(x,y,n)
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

os.system("PAUSE")