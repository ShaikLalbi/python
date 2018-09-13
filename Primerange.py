a,b=map(int,raw_input().split())
for k in range(a+1,b):
		for i in range(2,k):
			if(k%i==0):
				break
		else:
			print(k),
