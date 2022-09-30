import math
from ClassesAndObjects import Dog

class Orientation:
        def __init__(self, x_pos,  y_pos, degrees):
            self.x = x_pos
            self.y = y_pos
            #self.x_dir, self.y_dir = self.getUnitVectorFromDegree(degrees)
            #this is how can use the static method, otherwise you will get an error at runtime
            #that is use the name of the class
            self.x_dir, self.y_dir = Orientation.getUnitVectorFromDegree(degrees)
        
        #this is static method
        def getUnitVectorFromDegree(degrees):
            radians = (degrees/180)*math.pi
            return math.sin(radians), -math.cos(radians)

        def getNextPos(self):
            return self.x + self.x_dir, self.y + self.y_dir


#testing code for the class

myOrientation = Orientation(5,5,75)
print(myOrientation.getNextPos())


class Orientation1:
        pi = 3.14
        def __init__(self, x_pos,  y_pos, degrees):
            self.x = x_pos
            self.y = y_pos

            self.x_dir, self.y_dir = self.getUnitVectorFromDegree(degrees)
        
        @staticmethod #this is a decorator indicatiting to Python interpreter that the following method must not contain
        #self parameter. This way of coding is a matter of style
        def getUnitVectorFromDegree(degrees):
            radians = (degrees/180)*Orientation1.pi
            return math.sin(radians), -math.cos(radians)

        def getNextPos(self):
            return self.x + self.x_dir, self.y + self.y_dir

myOrientation = Orientation1(5,5,75)
print(myOrientation.getNextPos())



