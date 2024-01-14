
N=int(input())
arr=[]
for i in range(N):
    a=input()
    arr.append(a)

arr2=list(set(arr))

arr2.sort()
arr2.sort(key=len)
for i in arr2:
    print(i)