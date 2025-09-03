
def dfs(v):
    visited[v]=True

    for i in range(1,n+1):
        if not visited[i] and graph[v][i]==1:
           dfs(i)
           
n=int(input())
m=int(input())

visited=[False]*(n+1)
graph=[[False]*(n+1) for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1
dfs(1)
count=0
for i in range(n+1):
     if(visited[i] == True):
         count+=1

print(count-1)         