T=int(input())

for i in range(T):
    ecount=1
    wcount=1
    ewcount=1
    count=0
    west,east=map(int,input().split())
    for j in range(east,0,-1):
        ecount*=j
    for k in range(west,0,-1):
        wcount*=k
    for p in range(east-west,0,-1):
        ewcount*=p    
    count=ecount/(wcount*ewcount)
    print(int(count))        