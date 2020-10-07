logList = []
def logged(f):
    global logList
    def wrapper(*args, **kwargs):
        logList.append(f"{f.__name__}")
        if len(logList)>2:
            print(logList[-3:])
    return wrapper

@logged
def add(num):
    return num+1

@logged
def sub(num):
    return num-1

@logged
def pow(num):
    return num**2

@logged
def mod(num):
    return num%2 == 0

add(2)
sub(4)
pow(5)
mod(5)
sub(6)
