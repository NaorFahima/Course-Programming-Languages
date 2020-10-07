class A:
    def __init__(self):
        print("A.__init__")

    def m(self):
        print("m of A called")


class B(A):
    def __init__(self):
        print(super())

    def m(self):
        print("m of B called")
        A.m(self)


class C(A):
    def m(self):
        print("m of C called")
        b = B()
        b.m()
        A.m(self)
        super().__init__()


class D(B,C):
    def m(self):
        print("m of D called")
        b = B()
        b.m()
        C.m(self)
        super().m()
        A.__init__(self)


d = D()
d.m()

'''
After removing number 1 :
A.__init__
m of D called
A.__init__
m of B called
m of A called
m of C called
A.__init__
m of B called
m of A called
m of A called
'''

'''
After removing number 2 :
<super: <class 'B'>, <D object>>
m of D called
<super: <class 'B'>, <B object>>
m of B called
m of A called
m of C called
<super: <class 'B'>, <B object>>
m of B called
m of A called
m of A called
'''

'''
After removing number 3:
<super: <class 'B'>, <D object>>
m of D called
<super: <class 'B'>, <B object>>
m of B called
m of A called
m of C called
<super: <class 'B'>, <B object>>
m of B called
m of A called
m of A called
A.__init__
'''

'''
After removing number 4:
<super: <class 'B'>, <D object>>
m of D called
<super: <class 'B'>, <B object>>
m of B called
m of A called
m of C called
<super: <class 'B'>, <B object>>
m of B called
m of A called
m of A called
A.__init__
m of B called
m of A called
'''

'''
After removing number 5:
<super: <class 'B'>, <D object>>
m of D called
<super: <class 'B'>, <B object>>
m of B called
m of A called
m of C called
<super: <class 'B'>, <B object>>
m of B called
m of A called
m of A called
A.__init__
m of B called
m of A called
A.__init__
'''