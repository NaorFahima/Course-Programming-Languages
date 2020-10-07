def funcs(my_list):
    return [func for func in my_list if func.__code__.co_argcount <= 1]

def f1(d):
    pass

def f2(n,d):
    pass

def f3(n,d,s):
    pass

my_list = [f1,f2,f3]
print(funcs(my_list))