if __name__=="__main__":
    a=list(map(int,input().split()))
    p=0
    d=0
    while p<a[4]:
        d+=1
        if d>=a[0]:
            p+=a[1]
        if d>=a[2]:
            p+=a[3]
    print(d)