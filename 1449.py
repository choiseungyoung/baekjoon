N,L=map(int,input().split())

arr=list(map(int,input().split()))
arr.sort()
count=0
start=arr[0]
for i in arr[1:]:
    if i in range(start,start+L):
        continue
    else:
        count+=1
        start=i
       
print(count+1)