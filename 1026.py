import sys
input=sys.stdin.readline
N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

Asort=sorted(A)
Asort.sort(reverse=True)
Bsort=sorted(B)

sum=0
for i in range(N):
    sum+=Asort[i]*Bsort[i]

print(sum)