import sys
input=sys.stdin.readline 

N=int(input())
arr=set(list(map(int,input().split())))

M=int(input())
arr2=list(map(int,input().split()))


for i in arr2:
    if i in arr:
        sys.stdout.write("1 ")
    else:
        sys.stdout.write("0 ") 
