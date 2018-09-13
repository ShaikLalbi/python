N=int(raw_input())
count=0
for i in range (2,N):
	if(N%i==0):
		count = count+1
if(count==0):
	print("yes")
else:
	print("no")
