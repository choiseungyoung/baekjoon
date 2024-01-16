import sys
input=sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))
arr.sort()
sum=0
arr2=[]
for i in arr:
    sum+=i
    arr2.append(sum)

sum2=0
for j in arr2:
    sum2+=j

print(sum2)