# solution of https://www.hackerrank.com/challenges/angry-professor



t=int(input())
student=[]
timing=[]
for i in range(t):
    student.append(raw_input())
    timing.append(raw_input())

for i,j in zip(student,timing):
    a=[x for x in i.split()]
    total ,present = int(a[0]),int(a[1])
    b=[int(y) for y in j.split()]
    yes,no=0,0
    for i in b:
        if i<=0:
            no+=1
        else:
            yes+=1
    if no>=present:
        print "NO"
    else:
        print "YES"
    