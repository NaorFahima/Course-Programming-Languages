def hailstone(startNum):
    yield startNum
    while startNum!=1:
        if startNum%2 == 0:
            startNum = startNum/2
        else:
             startNum= startNum*3+1
        yield int(startNum)


for i in hailstone(5):
    print(i)
