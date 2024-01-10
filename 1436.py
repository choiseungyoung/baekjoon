N=int(input())
count=0
arr2=[666]
for i in range(1000,3000000): 
    arr=list(str(i))
    for j in range(len(str(i))): 
        if(j+2 > len(str(i))-1): 
            break
        
        if arr[j] == '6' :
            if arr[j+1] == '6' :
                if arr[j+2] == '6' :
                    arr2.append(i)
                    count+=1
                    
                    if(count==N):
                        print(arr2[count-1]) 
                        exit()
                        
                    break