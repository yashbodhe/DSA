from math import inf
 
def bellman_ford_path(edge_list, n):
    distance = [inf] * n
 
    distance[0] = 0
    for k in range(n - 1):
        for (f, t, w) in edge_list:
            distance[t] = min(distance[t], distance[f] + w)
 
    # chech for negative cycle
    for k in range(n - 1):
        for (f, t, w) in edge_list:
            if distance[f] + w < distance[t]:
                distance[t] = -inf
 
    return distance[n - 1] * -1
 
 
def main():
    n, m = map(int, input().split())
    edges = []
 
    for _ in range(m):
        f, t, w = map(int, input().split())
        edges.append((f - 1, t - 1, -w))
 
    max_dist = bellman_ford_path(edges, n)
    print(max_dist if max_dist != inf else -1)
 
if __name__ == "__main__":
    main()