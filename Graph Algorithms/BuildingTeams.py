import sys
from collections import deque


# Node - color1, all neigs - color2 and so on
def bipartite_check(adj, n):
    visited = [False] * n
    colors = [None] * n

    def _bfs_coloring(source):
        queue = deque([source])
        visited[source] = True
        colors[source] = True

        while queue:
            node = queue.pop()

            for neig in adj[node]:
                if colors[neig] == colors[node]:
                    return False
                if visited[neig]:
                    continue

                visited[neig] = True
                colors[neig] = not colors[node]
                queue.appendleft(neig)
        return True

    possible = True
    for node in range(n):
        if visited[node]:
            continue
        if possible:
            possible = _bfs_coloring(node)

    return colors if possible else []


def main():
    n, m = map(int, sys.stdin.readline().split())
    adjency = [[] for _ in range(n)]

    for _ in range(m):
        a, b = [int(i) - 1 for i in sys.stdin.readline().split()]
        adjency[a].append(b)
        adjency[b].append(a)

    colors = bipartite_check(adjency, n)
    if colors:
        print(*[[1, 2][color] for color in colors])
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()