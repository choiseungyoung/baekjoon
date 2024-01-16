import sys
input=sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))
arr2=set(arr)
arr3=list(sorted(arr2))
print(arr3)
dic={}
for i in range(len(arr3)):
     dic[arr3[i]]=i

for i in arr:
     print(dic[i],end=" ")
