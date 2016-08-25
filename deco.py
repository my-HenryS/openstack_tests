def deco1(func):

    def temp(a,b):
        print "before myfunc() called."
        func(a,b)
        print "after myfunc() called."


    return temp


@deco1
def myfunc(a,b):
    print 'sum is : '+(str)(a+b)
    print "myfunc() called"

#myfunc = deco1(myfunc)

myfunc(1,2) 
myfunc(3,4)   
