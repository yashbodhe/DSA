import sys
if __name__=="__main__":
    n,m=map(int,input().split())
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==j:dp[i][j]=0
            else:
                dp[i][j]=sys.maxsize
                for k in range(1,i//2+1):
                    dp[i][j]=min(dp[i][j],dp[k][j]+dp[i-k][j]+1)
                for k in range(1,j//2+1):
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[i][j-k]+1)
    print(dp[n][m])
                
    