S=list(input())
zerocount=0
onecount=0
if(S[0]=='0'):
    zerocount=1
else:
    onecount=1
for i in range(1,len(S)):
    if( S[i-1]=='0' and S[i] =='0'):
        continue
    elif(S[i-1]=='0'  and S[i] =='1'):
        onecount+=1
    elif(S[i-1]=='1' and S[i]== '0'):
        zerocount+=1
    elif(S[i-1]=='1' and S[i]=='1'):
        continue


if(onecount>zerocount):
    print(zerocount)
else:
    print(onecount)