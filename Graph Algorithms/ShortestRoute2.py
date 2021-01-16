import sys
from math import inf

def floyd_warshall_path(adj_matrix, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])
    return adj_matrix

def main_warshall():
    n, m, q = map(int, input().split())
    adj_matrix = [[inf] * n for _ in range(n)]
    
    for _ in range(m):
        f, t, w = map(int, input().split())
        if w < adj_matrix[f - 1][t -1]: 
            adj_matrix[f - 1][t - 1] = w
            adj_matrix[t - 1][f - 1] = w

    floyd_warshall_path(adj_matrix, n)   

    for _ in range(q):
        f, t = map(int, input().split())

        if f == t:
            adj_matrix[f - 1][t - 1] = 0
        if adj_matrix[f - 1][t - 1] == inf:
            adj_matrix[f - 1][t - 1] = -1
        print(adj_matrix[f - 1][t - 1])

if __name__ == "__main__":
    main_warshall()