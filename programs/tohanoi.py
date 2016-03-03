a=[]
for i in range(3):
   a.append(input())
b=[]
c=[]
b.append(a.pop())
print a
print b
print c
print "-----------------------------------"
c.append(a.pop())
print a
print b
print c
print "-----------------------------------"
c.append(b.pop())
print a
print b
print c
print "-----------------------------------"
b.append(a.pop())
print a
print b
print c
print "-----------------------------------"
a.append(c.pop())
print a
print b
print c
print "-----------------------------------"
b.append(c.pop())
print a
print b
print c
print "-----------------------------------"
b.append(a.pop())
print a
print b
print c
print "-----------------------------------"
