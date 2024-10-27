import math
import random
lo = math.log(1000,3)
print(lo)

print(math.floor(3.4),math.ceil(8.1))
print(round(5.5))  # round to even nums

print(math.sin(90),math.cos(90))

# random.seed(78)
# print(random.randint(1,11))
# print(random.randint(1,11))
# print(random.randint(1,11))
# print(random.randint(1,11))
# print(random.randint(1,11))
# print(random.randint(1,11))
# print(random.randint(1,11))


my_list = [1,2,3,4,5,6,7,8,9]
print(random.choice(my_list)) 
print(random.choices(population=my_list,k=5))
print(random.sample(population=my_list,k=5))
random.shuffle(my_list) # in place doesn't have return and it just changes the argument --> shuffle is in place func
print(my_list)