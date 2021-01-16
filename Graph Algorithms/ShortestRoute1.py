import sys
import heapq

from math import inf


def dijkstra_shortest_path(adj, n, source):
    visited = [False] * n
    distance = [inf] * n

    distance[source] = 0

    heap = [(0, source)]
    heapq.heapify(heap)
    
    while heap:
        weight, node = heapq.heappop(heap)

        if visited[node] or weight > distance[node]:
            continue
        visited[node] = True

        for neig, w in adj[node]:
            if distance[node] + w < distance[neig]:
                distance[neig] = distance[node] + w

                heapq.heappush(heap, (distance[neig], neig))
    return distance


def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]

    for _ in range(m):
        f, t, w = [int(x) for x in input().split()]
        
        adj[f - 1].append((t - 1, w))
        # adj[t - 1].append((f - 1, w))
    
    print(*dijkstra_shortest_path(adj, n, 0))

    # print(adj)


if __name__ == "__main__":
    main()