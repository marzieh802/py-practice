# def ten_muliply(num):
#     return num * 10


# num_list = [1, 2, 3, 4, 5]
# result_list = []
# for num in num_list:
#     result_list.append(ten_muliply(num))
# print(result_list)


# def ten_muliply(num):
#     return num * 10


# num_list = [1, 2, 3, 4, 5]
# new_list = list(map(ten_muliply,num_list))
# print(new_list)

# def check_ten(num):
#     return not(num % 10)
# num_list = [20,10,4,3,5]
# res = []
# for num in num_list:
#     if (check_ten(num)):
#         res.append(num)
# print(res)

# def check_ten(num):
#     return not(num % 10)
# num_list = [20,10,4,3,5]
# res = list(filter(check_ten,num_list)) # filter works for bolean's func
# print(res)


# temp = lambda num: num * 10
# print(temp(34))

# var = list(map(lambda st : st + "*",["h","i"]))
# print(var)


# num_list = [20,10,4,30,5]
# check = list(filter(lambda num : not(num % 10),num_list))
# print(check)

var = 50
def func(var):
    print(f"var in func is {var}") #50
    var = 'hi' # assignment occurs / local
    print(f"var after change in func is {var}")
    temp = lambda var : var +10
    return temp
assignment = func(var)
print(assignment(var))
print(var)






# def add(num1, num2):
#     return num1 + num2
# res = add(1,2)

# def greeting():
#     number = 10
#     def hello(name):
#         return f"hello {name}"
#     return hello

# say_hello = greeting() # def hello(name) : 
# print(say_hello("hosein"))

