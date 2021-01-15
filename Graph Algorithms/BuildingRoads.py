import sys

from collections import deque

# idea: just check were new component appear and connect them on the fly
def build_roads(adj, n):
    visited = [False] * n

    def _bfs(source, comp):
        queue = deque([source])
        visited[source] = True

        while queue:
            node = queue.pop()

            for neig in adj[node]:
                if visited[neig]:
                    continue

                visited[neig] = True
                queue.appendleft(neig)
    
    comp, add_edges = 0, []
    for node in range(n):
        if visited[node]:
            continue
        
        if comp > 0:
            add_edges.append(f"{node - 1 + 1} {node + 1}")
    
        _bfs(node, comp)
        comp = comp + 1

    print(len(add_edges))
    print("\n".join(add_edges))


def main():
    n, m = map(int, sys.stdin.readline().split())
    adjency = [[] for _ in range(n)]

    for _ in range(m):
        a, b = [int(i) - 1 for i in sys.stdin.readline().split()]
        adjency[a].append(b)
        adjency[b].append(a)

    # print(adjency)
    build_roads(adjency, n)
    

if __name__ == "__main__":
    main()