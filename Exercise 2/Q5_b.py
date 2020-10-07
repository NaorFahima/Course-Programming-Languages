class mutableInt:

  def __init__(self, num):
    self.num = num

  def changeNum(self,newNum):
      self.num = newNum

num = mutableInt(1)
print("num = 1")
print("num id:", id(num))
num.changeNum(2)
print("num = 2")
print("num id:", id(num))
print("num id stay the same if we change the number")
print("we created class immutable int")

