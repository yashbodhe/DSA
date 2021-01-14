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
                queue=[(i,j,0,"")]
                while queue:
                    x,y,index,path=queue.pop(0)
                    if mat[x][y]=="B":
                        if index<res[0]:
                            res[0]=index
                            res_path[0]=path
                    else:
                        mat[x][y]="#"
                        for k in range(4):
                            ii=x+row[k]
                            jj=y+col[k]
                            if 0<=ii<n and 0<=jj<m and (mat[ii][jj]=="." or mat[ii][jj]=="B") :
                                queue.append((ii,jj,path+p[k],index+1))
                        mat[x][y]="."
                mat[i][j]="A"

    if res[0]!=999999:
        print("YES")
        print(res[0])
        print(res_path[0])
    else:
        print("NO")


    