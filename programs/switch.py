# program to make switches in python



def yes():
    print 'yes'
    
def no():
    print 'no'
    
def cancel():
    print 'cancel'
 
a={'yes':yes,'no':no,'cancel':cancel}

for i in a:
    function= a[i]
    function()
