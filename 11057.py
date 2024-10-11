N=int(input())
arr=[0,1,2,3,4,5,6,7,8,9,10]
for i in range(N-1):
    for j in range(1,11):
        arr[j]=arr[j]+arr[j-1]
    
print(arr[-1]%10007)
        