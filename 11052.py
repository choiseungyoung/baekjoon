N=int(input())

arr=list(map(int,input().split()))

for i in range(1,N):
    for j in range(N):
        if(j==i):
            break
        arr[i]=max(arr[i], arr[i-j-1]+arr[j] )
    
print(arr[-1])

