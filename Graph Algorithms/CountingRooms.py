import sys
sys.setrecursionlimit(10000000)
def dfs(mat,i,j,n,m):
    mat[i][j]="#"
    row=[-1,0,0,1]
    col=[0,-1,1,0]
    for k in range(4):
        ii=i+row[k]
        jj=j+col[k]
        if 0<=ii<n and 0<=jj<m and mat[ii][jj]==".":
            dfs(mat,ii,jj,n,m)
if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[]
    for _ in range(n):
        mat.append(list(input()))
    count=0
    for i in range(n):
        for j in range(m):
            if mat[i][j]==".":
                count+=1
                dfs(mat,i,j,n,m)
    print(count)
    
    