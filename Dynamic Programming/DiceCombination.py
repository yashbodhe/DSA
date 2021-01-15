if __name__=="__main__":
    n=int(input())
    k=6
    dp=[0 for i in range(n+1)]
    dp[0]=dp[1]=1
    for i in range(2,7):
    	if i<=n:
        	dp[i]=2*dp[i-1]
    for i in range(7,n+1):
        dp[i]=2*dp[i-1]-dp[i-7]
    print(dp[n]%1000000007)