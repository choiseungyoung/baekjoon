N=int(input())

key=list(map(int,input().split()))

new=[0]*N

for i in range(N):
    count=0 
    for j in range(N):
        if( key[i]== count and new[j]== 0):
            new[j]= i+1
            break
        elif(new[j]==0):
            count+=1
    
for i in range(N):    
    print(new[i],end=" ")
    