import sys
input=sys.stdin.readline
arr=list(map(int,input().split()))

arr2=list(map(int,input().split()))

def pointing(arr,arr2):
    point=[]
    point2=[]
    count=0
    for i in range(4):
        if(i%2==0):
            for j in range(4):
                if(j%2==1):
                    point.append((arr[i],arr[j]))
    for i in range(4):
        if(i%2==0):
            for j in range(4):
                if(j%2==1):
                    point2.append((arr2[i],arr2[j]))

    for i in point2:
        for j in point:
            if(i==j):
                count+=1
    if(count==1):
        if(arr[3]==arr2[1]):
            if(arr[0]!=arr2[0] and arr[2]!=arr2[2]):
                return 1
        if(arr[1]==arr2[3]):
            if(arr[0]!=arr2[0] and arr[2]!=arr2[2]):
                return 1
def lineing(arr,arr2):
    if(arr[2]==arr2[0]):
        return 1
    if(arr[0]==arr2[2]):
        return 1
    if(arr[3]==arr2[1]):
        return 1
    if(arr[1]==arr2[3]):
        return 1
                
    
def nulling(arr,arr2):
    if(arr[2]<arr2[0]):
        return 1
    if(arr[0]>arr2[2]):
        return 1
    if(arr[3]<arr2[1]):
        return 1
    if(arr[1]>arr2[3]):
        return 1

if(nulling(arr,arr2)==1):
    print('NULL')
elif(pointing(arr,arr2)==1):
    print('POINT')
elif(lineing(arr,arr2)==1):
    print('LINE')
else:
    print('FACE')