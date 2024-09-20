N,M=map(int,input().split())
arr=[]
for i in range(M):
    c=list(map(int,input().split()))
    arr.append(c)

cost=0
mincost=100000000000
for i in range(0,M):
    for j in range(0,M):
        if(N%6!=0):
            cost=((N//6)+1)*arr[i][0]
            for k in range(0,(N//6)+1):  
                if(cost > k*arr[i][0]+ arr[j][1]*(N-(6*k)) ):
                    cost=k*arr[i][0]+ arr[j][1]*(N-(6*k))
                print(cost)    
            if(mincost> cost):
                mincost=cost
            
        
        if(N%6==0):
            cost=(N//6)*arr[i][0]
            for k in range(0,(N//6)+1):
                if(cost > k*arr[i][0]+ arr[j][1]*(N-(6*k)) ):
                    cost=k*arr[i][0]+ arr[j][1]*(N-(6*k))
                print(cost)
                if(mincost> cost):
                    mincost=cost
            
               
            
print(mincost)