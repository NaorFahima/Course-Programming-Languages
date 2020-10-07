import functools

def sumArrays(arrs):
    return functools.reduce(lambda x,y:x+y,functools.reduce(lambda x,y:x+y,arrs))

arrs = [[12,4],[1],[2,3]]
print(sumArrays(arrs))
