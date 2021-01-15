if __name__=="__main__":
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[[999999999 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]<=j:
                dp[i][j]=min(dp[i-1][j],dp[i][j-a[i-1]]+1)
            else:
                dp[i][j]=dp[i-1][j]
    if dp[n][m]<999999999:
        print(dp[n][m])
    else:
        print(-1)