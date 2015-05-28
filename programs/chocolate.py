from __future__ import division
t=int(input())
a=[]
for i in range(t):
    a.append(raw_input())
for i in a:
    money,price,wrap=i.split()
    money,price,wrap=int(money),int(price),int(wrap)
    n=money/price
    remaining_wrapper=n/wrap
    if remaining_wrapper==0:
        print n+1
    else:
        n+=1
        wrap+=remaining_wrapper
        n/=n
        

