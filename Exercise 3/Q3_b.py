logList = []
def logged(f):
    global logList
    def wrapper(*args, **kwargs):
        str = f"{f.__name__}("
        for i in args:
            str += f"{i},"
        str = str[:len(str)-1]
        str += ")"
        logList.append(f"you called {str} it returned {f(*args)}")
        for i in logList:
            print(i)
        print()
    return wrapper

@logged
def func(*args):
    return 3+len(args)


func(2,3,4)
func(10,20)
func(5)
func(1,2,3,4,5,6,7)