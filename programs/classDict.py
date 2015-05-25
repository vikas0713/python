# collecting data in class as a dictionary

class Data:
    def __init__(self, **kwargs):
        return self.__dict__.update(kwargs)

obj=Data(eng=60,maths=80, science=78)

if obj.maths>=70 and obj.eng>=70 and obj.science>=70:
    print " A grade "
else:
    print "B grade"