# # def say_hello(name):
# #     '''
# #     this is a multi line comment and
# #     name is parameter
# #     '''
# #     print("hello",name)

# # # person = "jack"
# # # '''
# # # a comment for p
# # # '''


# # # say_hello(person) #person is argument.


# # # def add(num1,num2):
# # #     result = num1 + num2
# # #     return result
# # # sum = add(88,2)
# # # print(sum)

# # def fizzbuzz_game(start,end):
# #     result = ""
# #     for inte in range(start,end):
# #         if (inte % 3 == 0 and inte % 5 == 0):
# #             result += "fizzBuzz"
# #         elif inte %5 == 0:
# #             result += "Buzz"
# #         elif inte %3 == 0:
# #             result += "Fizz"
# #         else:
# #             result += f"{inte}"
# #         result += ", "

# #     return result
# # final = fizzbuzz_game(5,33)    #make dynomic the code
# # print(final)

# # # print(fizzbuzz_game(32,76))

# # newstr = say_hello(final)
# # print("newstr: ",newstr)
# # print("newstr: ",type(newstr))
# # hello my love
# # def multiply(num1, num2=5, num3=4):
# #     return num1*num2*num3


# # res = multiply(3, 4)
# # print(res)


# # def get_even_list(item):
# #     even_list = []
# #     for num in item:
# #         if (num % 2 == 0):
# #             even_list.append(num)
# #     return even_list


# # even = get_even_list([1, 2, 3, 4, 5, 6])
# # print(even)


# # list_of_employee = [("jack",3),("michael",8),("walter",0)]
# # def find_lowest_off(list_of_employee):
# #     check_hours = 30
# #     lowest_hour_employee = ""
# #     for name,hours in list_of_employee:
# #         if(check_hours > hours):
# #             check_hours = hours
# #             lowest_hour_employee = name

# #     return (lowest_hour_employee,check_hours)
# # lowest_off = find_lowest_off(list_of_employee)
# # print(lowest_off)

# from random import shuffle

# def shuffle_list(list): # list = new list
#     shuffle(list)
#     return list
# new_list = [1,2,3,4,5]
# test = shuffle_list(new_list)
# print("test: ", test)
# print("new_list: ",new_list)


# # def shuffle_list(my_list):
# #     temp = list(my_list)
# #     shuffle(temp)
# #     return temp
# # new_list = [1,2,3,4,5]
# # test = shuffle_list(new_list)
# # print("test: ", test)
# # print("new_list: ",new_list)


# # def shuffle_list(my_list):
# #     temp = list(my_list)
# #     shuffle(temp)
# #     return temp

# # def player_guess():
# #     guess = ""
# #     while not(guess in ["0","1","2"]):
# #         guess = input("pick a number between 0 , 1 , or 2 :")
# #     return int(guess)

# # def check_guess(list_param,input_guess):
# #     if(list_param[input_guess] == 'o'):
# #         print("correct answer!!!")
# #     else:
# #         print("wrong answer!!!")
# #         print(list_param)

# # my_list = [' ','o',' ']

# # mixed_list = shuffle_list(my_list)
# # given_guess = player_guess()
# # check_guess(mixed_list,given_guess)


# # def odd_num(list_item):
# #     new_list_item = []
# #     for num in list_item:
# #         if num % 2 != 0 :
# #             new_list_item.append(num)
# #         else:
# #             new_list_item.append("even")

# #     return new_list_item
# # nums = odd_num([1,2,3,4,5,6])
# # print(nums)


# # define a function and pass any number of args
# # and pass a key value pair of opertion that can be + or -

# def my_func(test,*args, **kwargs):
#     print(test)
#     print(kwargs)
#     if ("operation" in kwargs):
#         if (kwargs["operation"] == "+"):
#             return sum(args)
#         elif (kwargs["operation"] == "-"):
#             result = args[0]
#             for index, num in enumerate(args):
#                 if (index == 0):
#                     continue
#                 result -= num
#             return result
#         else:
#             return "operation is not allowed"
#     else:
#         return "operation not found"


# result = my_func("malfhqefhoqiehfqhef", 2, 4, 5, 6, 1, 7, 2, operation="-")
# print(result)

# write a function that return the lesser of two nums if both number are even
# #but the greater if one or both of nums are odd.

# def lesser_even(num1, num2):
#     if (not (num1 % 2) and not (num2 % 2)):
#         return min(num1,num2)
#     else:
#         return max(num1,num2)
# even_nums = lesser_even(4,2)
# print(even_nums)

# def same_first_letter(letter):
#     word_list = letter.split(" ")
#     # if (word_list[0].startswith(word_list[1][0])):
#     #     return True
#     # else:
#     #     return False
#     return word_list[0].startswith(word_list[1][0])
# same = same_first_letter("apple orange")
# print(same)

# def capitalize_letter(string):
#     new_string = ""
#     for index,name in enumerate(string.capitalize()): # for --> tuple unpaking
#         if index == 3:
#             new_string += name.capitalize()
#         else:
#             new_string += name
#     return new_string
# lett = capitalize_letter('jhjgjgkhl')
# print(lett)

# def master_yoda(sentence):
#     new_sentence = ""
#     splitted_sentence = sentence.split(" ")
#     count = len(splitted_sentence) - 1
#     while count >= 0 : # 2
#         new_sentence += splitted_sentence[count]
#         new_sentence += " "
#         count -= 1 #1

#     return new_sentence
# my_sentence = master_yoda("love is everything")
# print(my_sentence)

# print(abs(-7))

# def almost_there(num):
#     # if (num in range(90,111) or num in range(190,211)):
#     #     return True
#     # return False
#     return num in range(90,111) or num in range(190,211)
# print(almost_there(45))
# print(almost_there(90))

# print("hahahah".count("hah"))  # not including overlap


# def laughter(pattern, text): # including overlap
#     repitition = 0
#     for index, _ in enumerate(text): # 4
#         for p_index, _ in enumerate(pattern): # 0
#             next_chr_index = index + p_index # 3+0
#             if ((next_chr_index >= len(text)) or #7
#                     (text[next_chr_index] != pattern[p_index])):
#                 break
#             if (p_index == len(pattern)-1): # 2
#                 repitition += 1
#     return repitition
# smile = laughter("hah", "hahahah")
# print(smile)

# ch_li = [1,2,3,4]
# def change(num): # pass by reference
#     num[0] = 2
# change(ch_li)
# print(ch_li)

# ch_li = 5
# def change(num): # pass by value (copy)
#     num = 3
# change(ch_li)
# print(ch_li)

# ch_li = {"a":True}
# def change(num): # pass by reference
#     num["a"] = False
# change(ch_li)
# print(ch_li)

# ch_li = "abc"
# def change(num): # pass by value
#     num[1] = "f" # strings are immutable
# change(ch_li)
# print(ch_li)

# ch_li = "abc"
# def change(num): # pass by value
#     num = "jkl"
#     # str1 = num[1:2]

#     # print(str1)
# change(ch_li)
# print(ch_li)

# ch_li = True
# def change(num): # pass by value
#     num = False
# change(ch_li)
# print(ch_li)

# int, str, bool => primitive data type => pass by value
# dict, list, tuple => compund data type => pass by reference

# str_text = "hello hello"


# def paper_doll(text):
#     result = ""
#     for chr in text:

#         # result += f"{chr}{chr}{chr}"
#         result += "{}{}{}".format(chr,chr,chr)

#     return result


# pap = paper_doll(str_text)
# print(pap)

# def blackjack(a, b, c):
#     if not((type(a) is int) and (type(b) is int) and (type(c) is int)):
#         return "please enter integer as arguments"
#     elif (not(a in range(1,12)) or not(b in range(1,12)) or not(c in range(1,12))):
#         return "please enter enteger between 1,11"
#     sum_num = a+b+c
#     if (sum_num <= 21):
#         return sum_num
#     elif (sum_num > 21):  # or else is true
#         if (a == 11 or b == 11 or c == 11):
#             sum_num = sum_num - 10
#             if (sum_num > 21):
#                 return "BUST"
#             else:
#                 return sum_num
#         else:
#             return "BUST"
            
# check = blackjack(5,11,7)
# print(check)

# def summer_69(array):
#     return sum(array)
# my_list = summer_69([1,3,5])
# print(my_list)

# def summer_69(array):
#     sum_list = 0
#     seen_6 = False
#     for num in array:
#         if(num == 6):
#             seen_6 = True
#         if (not(seen_6)):
#             sum_list += num
#         if(num == 9):
#             seen_6 = False
#     return sum_list
# my_list = summer_69([4,5,6,7,8,9]) #desighn pattern flag usage
# print(my_list)