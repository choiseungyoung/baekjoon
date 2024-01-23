N,K=map(int,input().split())

arr=list(map(int,input().split()))

acc=[0]*(N-K+1)
sum=sum(arr[:K])
acc[0]=sum

for i in range(1,N-K+1):
    sum=sum-arr[i-1]+arr[i+K-1]
    acc[i]=sum
print(acc)
print(max(acc))