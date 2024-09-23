N=int(input())
arr=[]

sum=0
for i in range(N):
    arrset=set()
    count=0
    word=list(input().rstrip())
    arr.append(word)
    for j in range(0,len(word)):
        if(j+1==len(word)):
            break
     
        if(arr[i][j]==arr[i][j+1]):
            continue
        elif(arr[i][j]!=arr[i][j+1]):
            if(arr[i][j] in arrset):
                count=1
            arrset.add(arr[i][j])
    if(arr[i][-1] in arrset):
        count=1    
                            
    if(count==0):
        sum+=1
print(sum)