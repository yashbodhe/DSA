if __name__=="__main__":
    for _ in range(int(input())):
        x,y=map(int,input().split())
        if x<y:
            i,j=y,x
            minn,maxx=(i-1)**2+1,i**2
            if i%2==0:
                print(minn+j-1)
            else:
                print(maxx-j+1)
        else:
            i,j=x,y
            minn,maxx=(i-1)**2+1,i**2
            if i%2==0:
                print(maxx-j+1)
            else:
                print(minn+j-1)