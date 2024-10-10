n=int(input())
arr=[]
arr.append([int(input())])
for i in range(n-1):
    arr.append(list(map(int,input().split())))
print(arr)
for i in range(n-2,-1,-1):
    for j in range(i+1):
        arr[i][j]+=max(arr[i+1][j] , arr[i+1][j+1])
        
print(arr[0][0])