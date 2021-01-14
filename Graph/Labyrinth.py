import sys
sys.setrecursionlimit(10000000)

def dfs(mat,i,j,n,m,res,res_path,path,index):
    if mat[i][j]=="B":
        if index<res[0]:
            res[0]=index
            res_path[0]=path
    else:
        mat[i][j]="#"
        for k in range(4):
            ii=i+row[k]
            jj=j+col[k]
            if 0<=ii<n and 0<=jj<m and (mat[ii][jj]=="." or mat[ii][jj]=="B") :
                dfs(mat,ii,jj,n,m,res,res_path,path+p[k],index+1)
        mat[i][j]="."
    
if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[]
    for _ in range(n):
        mat.append(list(input()))
    res=[999999]
    res_path=[""]
    row=[-1,0,0,1]
    col=[0,-1,1,0]
    p=["U","L","R","D"]
    for i in range(n):
        for j in range(m):
            if mat[i][j]=="A":
                dfs(mat,i,j,n,m,res,res_path,"",0)
                mat[i][j]="A"
    if res[0]!=999999:
        print("YES")
        print(res[0])
        print(res_path[0])
    else:
        print("NO")


    