N=int(input())

name=input()
count=0
lenname=len(name)
arr=[]
step=1
for i in range(N):
    a=0
    oldname=input()
    for start in range(100):
        for step in range(1,100):
            if name in oldname[start:100:step]:
                count+=1
                arr.append(oldname)
                a=1
                break
        if(a==1):
            break
print(count)