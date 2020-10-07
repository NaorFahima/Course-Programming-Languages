import functools
def highestRes(myDic):
    newList = list(map(lambda kv: kv[1], myDic.items()))
    newlist = list(map(lambda x:x[1],newList))
    return functools.reduce(lambda x, y: x if x > y else y,newlist)

cameras = {'LEQ2B':('Nikon',3.68,4995),
           'CAE5D4242105':('Cannon',3.40,3899),
           'DC52':('Apple',2.5,5894)}

print("Cameras: " ,cameras)

print("Highest res:",highestRes(cameras))
