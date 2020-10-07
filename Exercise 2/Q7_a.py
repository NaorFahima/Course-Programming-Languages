import functools
def listPow(mylist):
    return functools.reduce(lambda x,y:x+y,map(lambda y:2**y,list(filter(lambda x:x<12,mylist))))

mylist = [1,4,6,8,20]
print(listPow(mylist))
