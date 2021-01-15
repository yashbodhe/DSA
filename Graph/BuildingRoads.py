import sys
sys.setrecursionlimit(10000000)

def dfs(x):
    visit[x]=1
    if x in adj:
        for i in adj[x]:
            if not visit[i]:
                dfs(i)
        
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
    res=[]
    visit=[0 for i in range(n+1)]
    for u in range(1,n+1):
        if not visit[u]:
            res.append(u)
            dfs(u)
    print(len(res)-1)
    for i in range(1,len(res)):
        print(res[0],res[i])
        