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