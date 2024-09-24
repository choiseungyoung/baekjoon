import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    N=int(input())
    arr=[list(map(int,input().split())) for j in range(N)]
    arrsort=sorted(arr)
    count=1
    top=0        
    for k in range(1,len(arrsort)):
        if(arrsort[k][1] < arrsort[top][1]):
            top=k
            count+=1
                        
    print(count)            
        