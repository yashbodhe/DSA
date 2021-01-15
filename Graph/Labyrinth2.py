if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[]
    for _ in range(n):
        mat.append(list(input()))
    visit=[[False]*m]*n
    res=[999999]
    res_path=[""]
    row=[-1,0,0,1]
    col=[0,-1,1,0]
    p=["U","L","R","D"]
    for i in range(n):
        for j in range(m):
            if mat[i][j]=="A":
                queue=[(i,j,0,"")]
                visit[i][j]=True
                while queue:
                    #print(1)
                    x,y,index,path=queue.pop(0)
                    if mat[x][y]=="B":
                        res[0]=index
                        res_path[0]=path
                        break
                    else:
                        for k in range(4):
                            ii=x+row[k]
                            jj=y+col[k]
                            #print(2)
                            if 0<=ii<n and 0<=jj<m and (mat[ii][jj]=="." or mat[ii][jj]=="B") :
                                #print(p[k])
                                visit[ii][jj]=True
                                queue.append((ii,jj,index+1,path+p[k]))

    if res[0]!=999999:
        print("YES")
        print(res[0])
        print(res_path[0])
    else:
        print("NO")
