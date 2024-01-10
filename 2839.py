N=int(input())
a=3
b=5

countc=0
mincount=10000
for i in range(2000):
    for j in range(1100):
        if(i*a+b*j>N):
            break
        if(i*a+b*j==N):
            countc+=1
            if(i+j<mincount):
                mincount=i+j
if(countc==0):
    print(-1)
else:    
    print(mincount)