t=int(input())
a=[]
for i in range(t):
    a.append(int(input()))
    
for i in a:
    n,count=i,0
    while(n):
        x=n%10
        if x!=0 and i%x==0:
            count+=1
        else:
            pass
        n/=10
    print count