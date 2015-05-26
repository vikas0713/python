# solution of https://www.hackerrank.com/challenges/cut-the-sticks
def cut(a):
    mini=min(a)
    for i in range(len(a)):
        a[i]-=mini
    c=a.count(0)
    while(c):
        a.remove(0)
        c-=1
    return a,len(a)

n=int(input())
a=raw_input()
a=[int(i) for i in a.split()]
while(n):
    print n
    a,n=cut(a)
