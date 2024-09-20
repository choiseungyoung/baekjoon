M,N=map(int,input().split())
arr=[]
for i in range(M,N+1):
    count=0
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            count=1
            break
    if(count==0):
        print(i)   
        