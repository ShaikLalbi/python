a,b=map(int,raw_input().split())
for i in range(a,b):
	sum=0
	temp=i
	while temp>0:
		rem=temp%10
		sum=sum+rem**3
		temp//=10
	if i==sum:
		print i,
