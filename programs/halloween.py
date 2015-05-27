t=int(input())
a=[]
for i in range(t):
    a.append(int(input()))
    
for i in a:
    x=int(i/2)
    y=i-x
    res=x*y
    print res
    