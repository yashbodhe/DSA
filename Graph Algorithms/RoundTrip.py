import sys
sys.setrecursionlimit(10000000)
def roundtrip(adj, n):
    visit = [False] * (n+1)
    res = [[]]
    def dfs(src,l,path,des):
        if src==des and l>=4:
            res[0]=path
            return True
        elif src==des and l!=1:
            return False
        for x in adj[src]:
            if not visit[x]:
                visit[x]=True
                if dfs(x,l+1,path+[x],node):return True
                visit[x]=False
        return False

    for node in range(1,n+1):
        visit = [False] * (n+1)
        if dfs(node,1,[node],node):
            return res
    return []


def main():
    n, m = map(int, sys.stdin.readline().split())
    adjency = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = [int(i) for i in sys.stdin.readline().split()]
        adjency[a].append(b)
        adjency[b].append(a)

    res = roundtrip(adjency, n)
    if res:
        print(len(res[0]))
        print(*res[0])
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()