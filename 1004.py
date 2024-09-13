T=int(input())

for i in range(T):
    count=0
    arr=list(map(int,input().split()))
    n=int(input())
    for j in range(n):
        a,b,c=map(int,input().split())
        dis1=(a-arr[0])**2 + (b-arr[1])**2
        dis2 =(a-arr[2])**2 + (b-arr[3])**2
        if(dis1<c**2 and dis2<c**2):
            pass
        elif(dis1<c**2):
            count+=1
        elif(dis2<c**2):
            count+=1        
    print("count",count)