N,L=map(int,input().split())

arr=list(range(0,N))
index=0
print(arr)
for i in range(1,len(arr)):
    for j in range(2,100):    
        arr[i]=arr[i]+arr[i-1]
        
        if((arr[i]==N) and j>=L):
            index=i
            break
        elif(arr[i]!=N):
            break
        print(arr)