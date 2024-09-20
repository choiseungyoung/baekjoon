X=int(input())


count=0
for i in range(1,7):
    if(2**i<=X and X<2**(i+1)):
        count=i

number=0
for j in range(count,-1,-1):
    if(X-2**j>=0):
        number+=1
        X=X-2**j
        
print(number)