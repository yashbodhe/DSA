import sys
sys.setrecursionlimit(10000000)

def dfs(x,index,path,n):
    if x==n and index<res[0]:
        res[0]=index
        res_path[0]=path.copy()
        return 
    visit[x]=1
    if x in adj:
        for i in adj[x]:
            if not visit[i]:
                path.append(i)
                dfs(i,index+1,path,n)
                path.pop()
    visit[x]=0
        
if __name__=="__main__":
    n,m=map(int,input().split())
    adj=dict()
    for _ in range(m):
        u,v=map(int,input().split())
        if u not in adj:
            adj[u]=[]
        adj[u].append(v)
        if v not in adj:
            adj[v]=[]
        adj[v].append(u)
    res=[9999999]
    res_path=[[0]]
    visit=[0 for i in range(n+1)]
    dfs(1,1,[1],n)
    if res_path[0][-1]==n:
        print(res[0])
        print(*res_path[0])
    else:
        print("IMPOSSIBLE")
        
        