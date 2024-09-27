N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
               
arr.sort(key=lambda x:(x[1],x[0]))

ori=arr[0][1]
count=1
for i  in range(1,N):
    if(ori<=arr[i][0]):
        count+=1
        ori=arr[i][1]
        
print(count)