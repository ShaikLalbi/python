a=raw_input().split()
k=" "
for i in range(0,len(a)):
	a[i]=a[i].capitalize()
c=a[0]
for i in range(1,len(a)):
	c=c+k+a[i]
print c
