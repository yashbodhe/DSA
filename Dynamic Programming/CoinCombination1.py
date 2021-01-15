if __name__=="__main__":
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[0 for i in range(m+1)]
    dp[0]=1
    for i in range(1,m+1):
        for j in range(n):
            if a[j]<=i:
                dp[i]+=dp[i-a[j]]
                dp[i]=dp[i]%1000000007
    print(dp[m])
    