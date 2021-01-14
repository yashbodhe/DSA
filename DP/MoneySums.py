if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    dp=[[False for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,s+1):
            if a[i-1]<=j:
                dp[i][j]=dp[i-1][j-a[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    res=[]
    count=0
    for i in range(1,s+1):
        if dp[n][i]:
            count+=1
            res.append(i)
    print(count)
    print(*res)
    