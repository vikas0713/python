#!/bin/python

# solution of https://www.hackerrank.com/challenges/maximizing-xor


def  maxXor( l,  r):
    result=0
    max=result
    for i in range(l,r+1):
        for j in range(l,r+1):
            result=i^j
            if result>max:
                max=result
    return max

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
print(res)
