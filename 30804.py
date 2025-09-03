from collections import deque
import sys
input=sys.stdin.readline

N=int(input())

arr=list(map(int,input().split()))
arr=deque(arr)

count=0
for i in range(len(arr)):
    tang=set(arr)
    if( len(tang) <=2 ):
        print(len(arr))
        break
    elif(len(tang)>2 and count==0):
        arr.popleft()
        count=1
    elif(len(tang)>2 and count==1):
        arr.pop()
        count=0
        