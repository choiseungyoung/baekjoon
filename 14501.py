N=int(input())
arrT=[]
arrP=[]
arrsum=[]

index=0

arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

sum=[0 for i in range(N+1)]
for i in range(N):
    for j in range(i+arr[i][0] ,N+1):
        if sum[j]<sum[i]+arr[i][1]:
            sum[j]=sum[i]+arr[i][1]

print(sum[-1]) 