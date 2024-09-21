import sys
input=sys.stdin.readline
N,M=map(int,input().split())
s=set()
arr2 = [0]*M

for i in range(N):
    s.add(input())
for j in range(M):
    arr2[j]=input()    


count=0

for index in arr2:
    if index in s:
        count+=1

            
print(count)

