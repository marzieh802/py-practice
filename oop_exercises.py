import math
# class Line():
    
#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
    
#     def distance(self):
#         return math.sqrt((self.coor2[0]-self.coor1[0])**2 + (self.coor2[1]-self.coor1[1])**2)

#     def slope(self):
#         return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

# coordinate1 = (3,2)
# coordinate2 = (8,10)
# li = Line(coordinate1,coordinate2)
# print(li.distance())
# print(li.slope())


# class Cylinder():

#     def __init__(self,height = 1, radius = 1):
#         self.height = height
#         self.radius = radius

#     def volume(self):
#         return math.pi*(self.radius**2)*self.height 
    
#     def surface_area(self):
#         return (2*math.pi*self.radius*self.height)+(2*math.pi*(self.radius**2))
    
# height = 5
# radius = 12
# cylinder = Cylinder(height,radius)
# print(cylinder.volume())
# print(cylinder.surface_area())

class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,cashe):
        self.balance += cashe
        return "Deposit Accepted"
        

    def withdraw(self,cashe):
        if (cashe <= self.balance):
            self.balance -= cashe
            return "withdraw Accepted"
        else:
            return "funds unavailable"
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"
    
    def __len__(self):
        return self.balance

owner = "jack"
balance = 100
acc1 = Account(owner,balance)
print(acc1)
print(acc1.owner)
print(acc1.balance)
print(acc1.deposit(50))
print(acc1)
print(acc1.withdraw(150))
print(acc1)
print(len(acc1))



