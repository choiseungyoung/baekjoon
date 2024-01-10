a=int(input())
sum=0
num=0
for i in range(1,4294967295):
    sum=sum+i
    if(sum==a):
        num=i
        break
    elif(sum>a):
        num=i-1
        break    
    
    
print(num)
    