def hailstone(startNum):
    startNum
    yield startNum
    while startNum!=1:
        startNum = startNum/2 if startNum%2==0 else startNum*3+1
        yield int(startNum)

for i in hailstone(5):
    print(i)
