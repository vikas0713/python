#!/usr/bin/py
# solution of https://www.hackerrank.com/challenges/lonely-integer
def lonelyinteger(a):
    answer=0
    for i in a:
        if a.count(i)==1:
                answer = i
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)