
average = (0,0)

def trig_decorator(f):
    def wrapper(*args, **kwargs):
        global average
        temp = (args[0],f(args[0]))
        newTuple = ((temp[0]+average[0])/2,(temp[1]+average[1])/2)
        average = newTuple
        print(f"Average input: {average[0]} \nAverage output: {average[1]}")

    return wrapper

@trig_decorator
def addOne(num):
    return num+1

@trig_decorator
def subOne(num):
    return num-1


addOne(100)
addOne(50)
subOne(8)
subOne(5)