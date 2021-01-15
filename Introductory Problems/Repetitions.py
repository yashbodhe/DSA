if __name__=="__main__":
    s=input()
    s1=s[0]
    count=0
    res=0
    for x in s+"J":
        if x!=s1:
            res=max(res,count)
            count=1
            s1=x
        else:
            count+=1
    print(res)
