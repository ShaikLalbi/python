num=int(raw_input())
temp=num
sum=0
while (temp>0):
	rem=temp%10
	sum=sum+rem**3
	temp//=10
if(num==sum):
	print("yes")
else:
	print("no")
