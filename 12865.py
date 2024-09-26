N,K=map(int,input().split())
arr=[[0,0]]
arr2=[[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(N):
    arr.append(list(map(int,input().split())))

value=0
for i in range(1,N+1):
    for j in range(1,K+1):
        ori0=arr[i][0]
        ori1=arr[i][1]
        if( j<ori0):
            arr2[i][j]=arr2[i-1][j]
        else:
            arr2[i][j]=max(ori1 + arr2[i - 1][j - ori0],arr2[i - 1][j])


print(arr2[N][K])


