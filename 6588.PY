sosu=[True]*1000001

for i in range(2,int(1000001**0.5)+1):
    if sosu[i]:
        for j in range(i**2,1000001,i):
            sosu[j]=False
            
            
                    
while(True):
    sum=0
    N=int(input())
    if(N==0):
        break
    
    for i in range(3,N):
        if(sosu[i]==True and sosu[N-i]==True):
            print("%d = %d + %d" %(N,i,N-i))
            break
    else:
        print("Goldbach's conjecture is wrong.")