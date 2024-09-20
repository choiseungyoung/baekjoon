N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,list(input().rstrip()))))
               
len=min(N,M)
size=1
for i in range(N):
    for j in range(M):
        for k in range(1,len):
            number=arr[i][j]
            if((i+k)>N-1):
                break
            if(j+k>M-1):
                break
            if(arr[i+k][j] == number and arr[i][j+k]==number and arr[i+k][j+k]==number):
                if(size< (k+1)**2):
                    size=(k+1)**2
                    
print(size)