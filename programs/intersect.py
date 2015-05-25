# program to find intersection between two dictionaries only key values are matched not he values
a={'a':1, 'b':2,'c':3,'j':4}
b={'a':1, 'n':6, 'j':3}
print "intersects:", [k for k in a if k in b]