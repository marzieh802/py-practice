# def say_hello(name):
#     '''
#     this is a multi line comment and
#     name is parameter
#     '''
#     print("hello",name)

# # person = "jack"
# # '''
# # a comment for p
# # '''


# # say_hello(person) #person is argument.


# # def add(num1,num2):
# #     result = num1 + num2
# #     return result
# # sum = add(88,2)
# # print(sum)

# def fizzbuzz_game(start,end):
#     result = ""
#     for inte in range(start,end):
#         if (inte % 3 == 0 and inte % 5 == 0):
#             result += "fizzBuzz"
#         elif inte %5 == 0:
#             result += "Buzz"
#         elif inte %3 == 0:
#             result += "Fizz"
#         else:
#             result += f"{inte}"
#         result += ", "

#     return result
# final = fizzbuzz_game(5,33)    #make dynomic the code
# print(final)

# # print(fizzbuzz_game(32,76))

# newstr = say_hello(final)
# print("newstr: ",newstr)
# print("newstr: ",type(newstr))
# hello my love
# def multiply(num1, num2=5, num3=4):
#     return num1*num2*num3


# res = multiply(3, 4)
# print(res)


# def get_even_list(item):
#     even_list = []
#     for num in item:
#         if (num % 2 == 0):
#             even_list.append(num)
#     return even_list


# even = get_even_list([1, 2, 3, 4, 5, 6])
# print(even)


# list_of_employee = [("jack",3),("michael",8),("walter",0)] 
# def find_lowest_off(list_of_employee):
#     check_hours = 30
#     lowest_hour_employee = ""
#     for name,hours in list_of_employee:
#         if(check_hours > hours):
#             check_hours = hours
#             lowest_hour_employee = name

#     return (lowest_hour_employee,check_hours)
# lowest_off = find_lowest_off(list_of_employee)
# print(lowest_off)

from random import shuffle

# def shuffle_list(list): # list = new list
#     shuffle(list)
#     return list
# new_list = [1,2,3,4,5]
# test = shuffle_list(new_list)
# print("test: ", test)
# print("new_list: ",new_list)


# def shuffle_list(my_list):
#     temp = list(my_list) 
#     shuffle(temp)
#     return temp
# new_list = [1,2,3,4,5]
# test = shuffle_list(new_list)
# print("test: ", test)
# print("new_list: ",new_list)


def shuffle_list(my_list):
    temp = list(my_list) 
    shuffle(temp)
    return temp

def player_guess():
    guess = ""
    while not(guess in ["0","1","2"]):
        guess = input("pick a number between 0 , 1 , or 2 :")
    return int(guess)

def check_guess(list_param,input_guess):
    if(list_param[input_guess] == 'o'):
        print("correct answer!!!")
    else:
        print("wrong answer!!!")
        print(list_param)

my_list = [' ','o',' ']

mixed_list = shuffle_list(my_list)
given_guess = player_guess()
check_guess(mixed_list,given_guess)




