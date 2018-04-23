import math,os,time
#x,y,z三个坐标都在0到16的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？
#最初的版本-航迹
def gcd(x,y,z,n):
	for i in range(2,n):
		if not any((x%i,y%i,z%i)):
			return False
	return True

def incube(x,y,z,n):
	if all((n>=x>=0,n>=y>=0,n>=z>=0)):
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
	
def pgcd(x,y,n):
	for i in range(2,n):
		if not any((x%i,y%i)):
			return False
	return True

def inplane(x,y,n):
	if all((n>=x>=0,n>=y>=0)):
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

def solve(n):#此处为边长值
	start = time.clock()
	a=vector(n+1)
	sum1=0
	#cnt=0
	for (x,y,z) in a:
		points=[0]*((n+1)**3)
		K=math.sqrt((3*n*n)/(x*x+y*y+z*z))
		K=int(K)+1 #此处向下取整即可,+1是为了方便后面的range()
		for X in range(n+1):
			for Y in range(n+1):
				for Z in range(n+1):
					if(points[address(X,Y,Z,n+1)]==0):
						flag=0
						for k in range(1,K):
							for i in (-1,1):
								if incube(X+x*i*k,Y+y*i*k,Z+z*i*k,n):
									points[address(X+x*i*k,Y+y*i*k,Z+z*i*k,n+1)]=-1
									flag+=1
						if(flag):
							points[address(X,Y,Z,n+1)]=1
		sum1+=points.count(1)
		#cnt+=1
		#print(cnt)
	print("sum1=",sum1)
	
	b=pvector(n+1)
	sum2=0
	for (x,y) in b:
		points=[0]*((n+1)**2)
		K=math.sqrt((2*n*n)/(x*x+y*y))
		K=int(K)+1 
		for X in range(n+1):
			for Y in range(n+1):
				if(points[paddress(X,Y,n+1)]==0):
					flag=0
					for k in range(1,K):
						for i in (-1,1):#此处可以删去
							if inplane(X+x*i*k,Y+y*i*k,n):
								points[paddress(X+x*i*k,Y+y*i*k,n+1)]=-1
								flag+=1
					if(flag):
						points[paddress(X,Y,n+1)]=1
		sum2+=points.count(1)
	print("sum2=",sum2)
	print("final answer=",3*((n+1)**2)+sum2*2*3*(n+1)+sum1*4)
	
	end = time.clock()
	print("运算耗时 %f秒\n" % (end - start))

for n in range(1,17):
	print("n =",n)
	solve(n)

os.system("PAUSE")