# Enter your code here. Read input from STDIN. Print output to STDOUT

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

T = input()
num = []

for i in range(T):
    num.append(input())
for j in num:
    count = 0
    f = factors(j)
    for k in f:
        if k%2==0:
            count+=1
    print count
