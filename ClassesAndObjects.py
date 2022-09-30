class Dog:
    def __init__(self):
        self.name = "rover"
        self.legs = 4

    def speak(self):
        print(self.name+"bark")


my_dog = Dog()
another_dog = Dog()

my_dog.speak()
another_dog.speak()



class Dog1:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name+"bark")


my_dog = Dog1("rover1")
another_dog = Dog1("rover1")

my_dog.speak()
another_dog.speak()



######class with private variables, This case is also static
class Dog2:
    ##static variables
    _legs = 6
    def __init__(self, name):
        self.name = name
    
    def getLegs(self):
        return self._legs

    def speak(self):
        print(self.name+"bark")

my_dog = Dog2("rover2")
print(my_dog.name, my_dog.getLegs())




#ineheritance for custom classes
#to extend the class pass the name of the class to be extended as parameter

class chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: yap yap') 
    def wagtail(self):
        print('vigorous wagging')


#nheritance for built-in class ex1
myList = list()


class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)


uniqueList = UniqueList()
uniqueList.append(2)
uniqueList.append(2)
uniqueList.append(4)

print(uniqueList)


#nheritance for built-in class ex2
myList = list()
class UniqueList1(list):
    def __init__(self):
        super().__init__() 
        self.someProperty = 'Get UNIQUE LIST'

    def append(self, item):
        if item in self:
            return
        super().append(item)
uniqueList = UniqueList1()
uniqueList.append(2)
uniqueList.append(2)
uniqueList.append(4)
print(uniqueList.someProperty)