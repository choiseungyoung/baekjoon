N=int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

maxmax=0    
arr.sort()
arr2=[]
for i in range(N):
    arr2.append(arr[i]*N)
    N-=1
print(max(arr2))