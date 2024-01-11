import sys
input=sys.stdin.readline
T=int(input())

count=1
while(count<=T):
    arr=[]
    N,M=map(int,input().split())
    for i in range(M):
        a=list(map(int,input().split()))
        arr.append(a)
    
    count+=1
    print(N-1)