N=int(input())

arr=list(map(int,input().split()))

arrsort=sorted(arr)
arrcount=[0]*N
for i in range(N):
    for j in range(N):
        if(arrsort[i]==arr[j]):
           arrcount[j]=i
           arr[j]='x'
           break

for i in arrcount:
    print(i,end=" ")