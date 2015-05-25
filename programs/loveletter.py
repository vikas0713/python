# solution of https://www.hackerrank.com/challenges/the-love-letter-mystery 

t=int(input())
a=[]
for i in range(t):
    a.append(raw_input())

for j in a:
    operation=0
    for m in range(len(j)/2):
        if j[m]==j[len(j)-m-1]:
            operation+=0
        elif ord(j[m])<ord(j[len(j)-m-1]):
            operation+=ord(j[len(j)-m-1])-ord(j[m])
        else:
            operation+=ord(j[m])-ord(j[len(j)-m-1])
    print operation
