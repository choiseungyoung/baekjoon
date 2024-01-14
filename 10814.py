N=int(input())
arr2=[]
for i in range(N):
    age,name=map(str,input().split())
    age=int(age)
    arr2.append((age,name))

arr2.sort(key=lambda x:x[0])
for i in arr2:
    print(i[0],i[1])