#solution of https://www.hackerrank.com/challenges/utopian-tree on hackerrank
t=int(input())
n=[]
for i in range(0,t):
    n.append(int(input()))
for j in n:
    k=1
    for m in range(0,j+1):
        if m==0 :
            k=1
        elif m%2==0:
            k+=1
        else:
            k<<=1
    print k
    