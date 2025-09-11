from abc import ABC,abstractmethod
class shape(ABC):
        
    @abstractmethod
    def area(self):
        pass    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("area of the circle:",3.14*self.radius*self.radius)
class reactangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area of rectangle:",self.length*self.breadth)
c=circle(10)
r=reactangle(2,3)
c.area()
r.area()