N=int(input())

M=int(input())
breakarr=list(map(int,input().split()))

count=abs(100-N)

for i in range(1000001):
    i=str(i)
    for j in range(len(i)):
        if(int(i[j]) in breakarr):
            break
        elif( j == len(i)-1 ):
            count=min(count, abs(N-int(i))+len(i))    
print(count)