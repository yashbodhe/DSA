if __name__=="__main__":
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    mod=1000000007
    dp=[[0 for i in range(m+1)]for j in range(n)]
    if a[0]==0:
        for i in range(m+1):
            dp[0][i]=1
    else:
        dp[0][a[0]]=1
            
    for i in range(1,n):
        x=a[i]
        if x==0:
            for j in range(1,m+1):
                for k in range(j-1,j+2):
                    if 1<=k<=m:
                        dp[i][j]+=(dp[i-1][k])%mod
        else:
            for k in range(x-1,x+2):
                if 1<=k<=m:
                    dp[i][x]+=(dp[i-1][k])%mod
    res=0
    for i in range(1,m+1):
        res+=dp[n-1][i]
    print(res%mod)
        