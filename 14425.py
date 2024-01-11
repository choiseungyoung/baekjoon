import sys
input=sys.stdin.readline
N,M=map(int,input().split())
arr =[]
arr2 = []
for i in range(N):
    arr.append(input())
for j in range(M):
    arr2.append(input())

count=0

for index in arr:
    for index1 in arr2:
        if(index==index1):
            count+=1
            break
            
print(count)

