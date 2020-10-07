def average(x,y):
    return (x+y)/2

def improve(update,close,guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x,y,tolerance = 1e-3):
    return  abs(x-y)< tolerance

def sqrt(a):

    def sqrt_update(x):
        b = a/x
        return average(b,x)

    def sqrt_close(x):
        return approx_eq(a,x*x)


    return round(improve(sqrt_update,sqrt_close),3)

print(sqrt(2))