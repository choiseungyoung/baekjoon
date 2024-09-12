T=int(input())
for i in range(T):
    c0=[1,0]
    c1=[0,1]
    N=int(input())   
    if(N>1):
        for i in range(N-1):
            c0.append(c1[-1])
            c1.append(c0[-2]+c1[-1]) 
    print(c0[N],c1[N])
    
