class Vehicle:

    def __init__(self, name, max_speed, mileage,):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

    
    def defination(self,colour):
        return f"The colour of this {self.name} is {colour} and its max speed is {self.max_speed} together with its milage which is {self.mileage}"
    
class Bus(Vehicle):
     def defination(self,colour="white"):
          return super().defination(colour="white")

class Car(Vehicle):
     def defination(self,colour="white"):
          return super().defination(colour="white")
     

road=Car("Mercedes","300","50")
print(road.defination())    
big=Bus("Volvo","180","8000")
print(big.defination())