if __name__=="__main__":
    n,m=map(int,input().split())
    w=list(map(int,input().split()))
    p=list(map(int,input().split()))
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if w[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],p[i-1]+dp[i-1][j-w[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    print(dp[n][m])
    