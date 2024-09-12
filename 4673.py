N=10000

for i in range(1,N):
    number=i
    for k in range(1,N):
        count=0
        if(k>number):
            break
        sum=k
        b=str(k)
        for j in range(len(b)):
            sum+=int(b[j])
            if(sum>i):
                break
        if(number==sum):
            count=1
            break
    if(count==0):
        print(number)
    