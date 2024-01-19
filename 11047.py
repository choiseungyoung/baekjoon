import sys
input=sys.stdin.readline
N,K=map(int,input().split())

arr=[]
for i in range(N):
    a=int(input())
    arr.append(a)
    
sum=0
while(True):
    for i in range(N-1,-1,-1):
        count=K//arr[i]
        sum+=count
        K=K%arr[i]
    break
print(sum)
