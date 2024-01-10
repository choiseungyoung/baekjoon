a,b=map(int,input().split())

arr=[]
for i in range(a):
    string=input()
    arra=list(string)
    arr.append(arra)


mincount=100000

def counting(a,b,c,d):
    count=0
    counta=0
    n=a
    m=b
    p=c
    q=d
    
    if((n+q)%2==0):
        start=arr[n][p]
        for i in range(n,m):
            for j in range(p,q):
                if((i+j)%2==0):
                    if(arr[i][j]!=start):
                        count+=1
                elif((i+j)%2==1):
                    if(arr[i][j]==start):
                        count+=1
    elif((n+q)%2==1):
        start=arr[n][p]
        for i in range(n,m):
            for j in range(p,q):
                if((i+j)%2==0):
                    if(arr[i][j]==start):
                        count+=1
                elif((i+j)%2==1):
                    if(arr[i][j]!=start):
                        count+=1
    
    if((n+q)%2==0):
        start=arr[n][p]
        for i in range(n,m):
            for j in range(p,q):
                if((i+j)%2==0):
                    if(arr[i][j]==start):
                        counta+=1
                elif((i+j)%2==1):
                    if(arr[i][j]!=start):
                        counta+=1
    elif((n+q)%2==1):
        start=arr[n][p]
        for i in range(n,m):
            for j in range(p,q):
                if((i+j)%2==0):
                    if(arr[i][j]!=start):
                        counta+=1
                elif((i+j)%2==1):
                    if(arr[i][j]==start):
                        counta+=1      
    if(count<counta):
        return count
    else:
        return counta

for i in range(0,50):
    for j in range(0,50):
        if(i+8>a or j+8>b):
            break
        num=counting(i,i+8,j,j+8)
        if(num<mincount):
            mincount=num
    
    
print(mincount)
