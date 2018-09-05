N,K=map(int,raw_input().split( ))
N=list(map(int,raw_input().split()))
sum=0
for i in range(0,(K+1)):
	sum=sum+i
	N.append(sum)
print(sum)
