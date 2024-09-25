N=int(input())
count=0
arr=[0,0,1,1]

for i in range(4,N+1):
    if(i%2!=0 and i%3!=0):
        arr.append(arr[i-1]+1)
    elif(i%2==0 and i%3!=0):
        arr.append(min(arr[i//2]+1,arr[i-1]+1))
    elif(i%3==0 and i%2!=0):
        arr.append(min(arr[i//3]+1,arr[i-1]+1))
    elif(i%3==0 and i%2==0):
        arr.append(min(arr[i//3]+1, arr[i//2]+1))
print(arr[N])   