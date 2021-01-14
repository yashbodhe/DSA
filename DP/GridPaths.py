if __name__=="__main__":
    n=int(input())
    mat=[]
    for _ in range(n):
        mat.append(list(input()))
    dp=[[0 for i in range(n)] for j in range(n)]
    dp[0][0]=1
    for i in range(n):
        for j in range(n):
            if mat[i][j]==".":
                if i>0:
                    dp[i][j]+=dp[i-1][j]
                if j>0:
                    dp[i][j]+=dp[i][j-1]
            else:
                dp[i][j]=0
    print(dp[n-1][n-1]%1000000007)
    