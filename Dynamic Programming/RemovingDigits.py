if __name__=="__main__":
    n=int(input())
    dp=[999999999 for i in range(n+1)]
    dp[0]=0
    for i in range(1,n+1):
        res = [int(x) for x in str(i)] 
        for j in res:
            dp[i]=min(dp[i-j]+1,dp[i])
    print(dp[n])
    