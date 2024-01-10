N=int(input())
count=0
for i in range(1,N+1):
    if(i//10==0):
        count+=1
    elif(i//100==0):
        count+=1
    else:
        a=i//100
        b=i//10%10
        c=i%10
        if(a==b and b==c):
            count+=1
        elif(a>b and b>c):
            if(abs(c-b) == abs(b-a)):
                count+=1
                
        elif(a<b and b<c):
            if(abs(c-b) == abs(b-a)):
                count+=1            
            
print(count)

