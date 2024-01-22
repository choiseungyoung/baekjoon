import sys
input=sys.stdin.readline
N=int(input())

arr=[]
for i in range(N):
    a=int(input())
    arr.append(a)
    
average=sum(arr)/len(arr)

arrsort=sorted(arr)
centerindex=len(arr)//2
centerdata=arrsort[centerindex]

dict={}
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

minvalue=max(dict.values())
arr2=[]
for i in arr:
    if(dict[i]==minvalue):
       arr2.append(i)   
a=sorted(set(arr2))
rangedata=max(arr)-min(arr)

print(round(average))
print(centerdata)
if(len(a)==1):
    print(a[0])
else:
    print(a[1])

print(rangedata)