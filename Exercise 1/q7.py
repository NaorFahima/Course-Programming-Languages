class Base(object):
    pass

##changed the classes inhertiance from object to an another class which inherit object
#this way there aren't any duplicates in the classes bases

class A(Base):
    def __init__(self, name):
        self.name = name


class AMixin(Base):
    def mixinExample(self):
        return ("in AMixin.mixinExample " + self.name)


def MixIn(TargetClass, MixInClass):
    if MixInClass not in TargetClass.__bases__:
        ##Adding the bases in a different way
        TargetClass.__bases__ = (MixInClass,)+TargetClass.__bases__


if __name__ == "__main__":
    a_instance = A("Question7")
    MixIn(A, AMixin)
    print(a_instance.mixinExample())