N=int(input())

sum=0
count=0
for i in range(1,N+1):
    sum=i
    if(sum==N):
        count+=1
    for j in range(i+1,N+1):
        sum+=j 
        if(sum>N):
            break
        if(sum==N):
            count+=1
            break

            
print(count)