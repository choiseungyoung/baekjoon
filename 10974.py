N=int(input())
fac=1
for i in range(1,N+1):
    fac=fac*i

arr=[]
for i in range(1,N+1):
    arr.append(i)

print(arr)
for i in range(fac):
    for j in range(N):
        print(arr[j])
        