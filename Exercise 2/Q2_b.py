class hailstone:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n % 2 == 0:
            self.n = int(self.n / 2)
            return self.n

        else:
            self.n = int((self.n * 3) + 1)
            return self.n

x = int(input("please enter a number "))
hailstone_sequence = hailstone(x)
print(x)
while x != 1:
    x = hailstone_sequence.__next__()
    print(x)