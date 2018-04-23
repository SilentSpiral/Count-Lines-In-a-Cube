import os
#x,y,z三个坐标都在0到16的范围内(包含边界) 这其中所有的整点每两个点确定一条直线,一共有多少条不同的直线？
#雪地工程,根本跑不出来,弃

def judge(a,b):
	if all(((a>=0),(a<=16),(b>=0),(b<=16))):
		return (a,b)
	else:
		return None

def snow(x,y,z,a,b,c):
	if a==0:
		return(None,None)
	k1=0-x/a
	k2=(16-x)/a
	return(judge(k1*b+y,k1*c+z),judge(k2*b+y,k2*c+z))

def snowfield(X,Y,Z,x,y,z):
	line=[]
	a=X-x
	b=Y-y
	c=Z-z
	A=snow(x,y,z,a,b,c)
	B=snow(y,z,x,b,c,a)
	C=snow(z,x,y,c,a,b)
	
	line.append(A[0])
	line.append(A[1])
	line.append(B[0])
	line.append(B[1])
	line.append(C[0])
	line.append(C[1])
	
	return(tuple(line))

def solve(n):	
	lines=set()
	for X in range(n):
		for Y in range(n):
			for Z in range(n):
					
				for x in range(n):
					for y in range(n):
						for z in range(n):
							if not all((X==x,Y==y,Z==z)):
								#print(snowfield(X,Y,Z,x,y,z))
								lines.add(snowfield(X,Y,Z,x,y,z))
							
							
	print(len(lines))
	return 0
	
for n in range(1,10):
	print("边长=",n)
	solve(n+1)

os.system("PAUSE")