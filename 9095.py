T=int(input())

for i in range(T):
    count=0
    number=int(input())
    arr=[1,2,4]
    for j in range(number-3):
        arr.append(arr[j]+arr[j+1]+arr[j+2])
    print(arr[number-1])
                                                