# program tocheck either a dict contains a list

a={'a':2, 'b':'3','c':[4,5,6],'d':'ten','e':[3,6,1,23,45]}
m=0
for i,j in a.items():
    if isinstance(j,list):
        m+=1
    else:
        pass
print 'there is '+str(m)+' list(s) in the dictionary'