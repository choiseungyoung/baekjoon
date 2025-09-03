import sys
input=sys.stdin.readline
T=int(input())
arr=[0]*1000001
arr[0]=1
arr[1]=2
arr[2]=4


for j in range(3,1000001):
    arr[j]=(arr[j-1] %1000000009+ arr[j-2]%1000000009+ arr[j-3]%1000000009)
    
    
for i in range(T):       
    N=int(input())
    print(arr[N-1]%1000000009)
