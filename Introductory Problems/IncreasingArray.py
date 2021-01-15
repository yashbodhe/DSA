if __name__=="__main__":
    n=input()
    a=list(map(int,input().split()))
    prev=a[0]
    res=0
    for x in a:
        if x<prev:
            res+=prev-x
        else:
            prev=x
    print(res)
