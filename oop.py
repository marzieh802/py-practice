# class Person(): #class
# # self is refering to the object that created with the class
#     def __init__ (self,name,age): #initializing method(constructor)
#         print('init is working')
#         self.name = name # attribute or property
#         self.age = age

#     def say_my_name(self): # method
#         print(self.name) # with self.name we access its attribute named name

#     def say_my_age(self):
#         return self.age
    
# person1 = Person(age= 3, name= 'sami') # object/instance creation
# person2 = Person('jack',2)
# # print(person1.name)
# # print(person1.age)

# person1.say_my_name() #call the method that related to their object
# person2.say_my_name()

# # age1 = person1.say_my_age()
# # print(age1)

# print(person2.say_my_age())

# person1.age = 10
# print(person1.say_my_age())



# class Rectangle():

#     number_of_angles = 4 # class attribute
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def calc_area(self):
#         return self.length*self.width
    
#     def calc_perimeter(self):
#         return (self.width + self.length)* 2
    
#     def get_info(self,name):
#         return f"I'm so {name}\nrectangles have {Rectangle.number_of_angles} angles\nlength = {self.length} width = {self.width}\narea and perimeter = {self.calc_area(),self.calc_perimeter()} "
        
# r1 = Rectangle(length= 4 , width= 2)
# print(r1.get_info("curious"))

# print(Rectangle.number_of_angles)


# def func(num1):
#     return num1.capitalize() *5
# my_map = list(map(func,"hello"))
# print(my_map)

# class Animal():
    
#     def __init__(self,name):
#         print("animal created")
#         self.name = name

#     def who_am_i(self):
#         print("i am animal")

#     def eat(self):
#         print("i am eating")

# # animal1 = Animal()  # make an object --> x = classname(init method parameters)
# # animal1.eat()     # call method

# class Cat(Animal):
#     # def __init__(self):
#     #     # Animal.__init__(self) calling parent is optional, in some situation that we want share child's init parameter to the parent
#     #     print("cat created")

    
#     def meow(self):
#         print("meow meow")

#     def eat(self):
#         print(f"the cat {self.name} is eating")
# cat1 = Cat("felix")
# cat1.eat()
# cat1.meow()
# cat1.who_am_i()

# class Dog():
#     def __init__(self,name):
#         print("dog created")
#         self.name = name

    
#     def eat(self):
#         print(f"the dog {self.name} is eating")

# dog1 = Dog("niko")

# # pets = [cat1,dog1] #polymorphism
# # for pet in pets:
# #     print(type(pet))
# #     pet.eat()

# # def call_eat(pet): #polymorphism
# #     print(type(pet))
# #     pet.eat()
# # call_eat(cat1)
# # call_eat(dog1)

class Car():
    def __init__(self,brand_name,number_of_wheels,maximum_speed):
        self.brand_name = brand_name
        self.number_of_wheels = number_of_wheels
        self.maximum_speed = maximum_speed

    def __str__(self): #string representation of object
        return f"this car is from {self.brand_name} and has {self.number_of_wheels} and maximum speed is {self.maximum_speed}"
    
    def __len__(self):
        return self.number_of_wheels
    
    def __del__(self):
        print(f"the car object with brand name {self.brand_name} has been deleted")
car1 = Car('benz',4,300)
# print(car1)
print(str(car1))
print(len(car1))
del car1
# print(car1)