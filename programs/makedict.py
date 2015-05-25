# program to make dictionary without using qoutes

def makedict(**kwargs):
    return kwargs


value1=str(raw_input('enter value1:'))
value2=str(raw_input('enter value2:'))
value3=str(raw_input('enter value3:'))
value4=str(raw_input('enter value4:'))
m=makedict(a=value1,b=value2,c=value3,d=value4)
print "the resultant dictionary is "+str(m)
    