E,S,M=map(int,input().split()) # 1<E<15 1<S<28 1<M<19
a=0
b=0
c=0
year=0
while True:
    a+=1
    b+=1
    c+=1   
    if(a>15):
        a=1
    if(b>28):
        b=1
    if(c>19):
        c=1       
    year+=1
    if(a==E and b==S and c==M):
        print(year)
        exit()
