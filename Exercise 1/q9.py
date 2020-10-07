class Animal:
    def __init__(self, name, birthDate, kind, numOfLegs):
        self.name = name
        self.birthDate = birthDate
        self.kind = kind
        self.numOfLegs = numOfLegs

    def __str__(self):
        print(f"Name: {self.name}, birthDate: {self.birthDate}, kind: {self.kind}, numOfLegs: {self.numOfLegs}")


class Domesticated(Animal):
    def __init__(self, lastCheck, name, birthDate, kind, numOfLegs):
        Animal.__init__(self, name, birthDate, kind, numOfLegs)
        self.lastCheck = lastCheck

    def __str__(self):
        Animal.__str__(self)
        print(f"lastCheck: {self.lastCheck}")


class Cat(Animal):
    def __init__(self, mustacheLength, name, birthDate, numOfLegs):
        Animal.__init__(self, name, birthDate, "Mammal", numOfLegs)
        self.mustacheLength = mustacheLength

    def __str__(self):
        Animal.__str__(self)
        print(f"mustacheLength: {self.mustacheLength}")


class Tiger(Cat):
    def __init__(self, mustacheLength, name, birthDate, numOfLegs):
        Cat.__init__(self, mustacheLength, name, birthDate, numOfLegs)

    def __str__(self):
        Cat.__str__(self)


class HomeCat(Cat, Domesticated):
    def __init__(self, mustacheLength, lastCheck, name, birthDate, kind, numOfLegs):
        Cat.__init__(self, mustacheLength, name, birthDate, numOfLegs)
        Domesticated.__init__(self, lastCheck, name, birthDate, kind, numOfLegs)

    def __str__(self):
        Cat.__str__(self)
        Domesticated.__str__(self)


def countAnimals(listOfAnimals):
    tigerList = []
    homeCatList = []
    for animal in listOfAnimals:
        if isinstance(animal, Tiger):
            tigerList.append(animal)
        elif isinstance(animal, HomeCat):
            homeCatList.append(animal)

    if len(tigerList) > 0:
        print(f"Number of Tigers: {len(tigerList)}\n")
        print("Tiger LIST:")
        for tiger in tigerList:
            tiger.__str__()
        print("\n")

    if len(homeCatList) > 0:
        print(f"Number of HomeCats: {len(homeCatList)}\n")
        print("HomeCats LIST:")
        for homeCat in homeCatList:
            homeCat.__str__()
        print("\n")


check = 0
listOfAnimals = []
while True:
    print("Please Choose which Animal to add: \n"
          "1) Tiger \n"
          "2) HomeCat \n"
          "3) Other")
    check = int(input("Answer: "))
    if check == 1:
        name = input("Name: ")
        birth = input("BirthDate: ")
        numOfLegs = input("Number of Legs: ")
        mustacheLength = input("Mustache Length: ")
        animal = Tiger(mustacheLength, name, birth, numOfLegs)
    elif check == 2:
        name = input("Name: ")
        birth = input("BirthDate: ")
        animalType = "Mammal"
        numOfLegs = input("Number of Legs: ")
        mustacheLength = input("Mustache Length: ")
        lastCheck = input("When was last checked at vet?: ")
        animal = HomeCat(mustacheLength, lastCheck, name, birth, animalType, numOfLegs)
    elif check == 3:
        name = input("Name: ")
        birth = input("BirthDate: ")
        animalType = input("Animal Type (Mammal , Bird, Reptile): ")
        numOfLegs = input("Number of Legs: ")
        animal = Animal(name, birth, animalType, numOfLegs)
    else:
        break
    print(f"{animal.name} has been added !")
    listOfAnimals.append(animal)

print("\n")
countAnimals(listOfAnimals)
