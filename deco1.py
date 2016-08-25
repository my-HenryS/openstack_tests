def deco1(arg):
    def _deco(func):
        def temp(*args, **kwargs):
            print arg
            print "before myfunc() called."
            func(*args, **kwargs)
            print "after myfunc() called."
            
        return temp
    return _deco


@deco1('module begin')
def myfunc(*args, **kwargs):
    sum = 0
    
    for arg in args:
        sum = sum + arg
    print 'sum :'+ str(sum)

    for kwarg in kwargs:
        print "kwargs: %s->%s" %(kwarg,kwargs[kwarg])

#myfunc = deco1(myfunc)

myfunc(1, 2, 3,  a='1', b='2', c='3') 
myfunc(3, 4, c='3', d='4')  
 
