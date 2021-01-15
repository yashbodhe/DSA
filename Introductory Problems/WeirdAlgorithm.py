if __name__=="__main__":
    n=int(input())
    res=[n]
    while n!=1:
        if n%2==0:
            n//=2
        else:
            n=3*n+1
        res.append(n)
    print(*res)
