# if/elif(related to pervious if)/else
# they have to align in the same indentation
# # nature = "mountains"

# # if nature == "jungle":
# #     print("Let's go to the jungle")
# # elif(nature == "mountains"):
# #     print("Let's go to the mountains")
# # else:
# #     print("where should we go?")

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 'for' is for navigating the lists or sth we can navigate until the end
# the difference between 'for' and 'while' is while works until the condition is true
# for num in my_list:
#     if not (num % 2):

#         print(num)

# message = "earth: please protect me"
# message[0]
# for _ in message:  # '_' mean is we don't want to name that
#     print("hello")

# message = "earth: please protect me"
# message[0]
# for _ in message:  # '_' mean is we don't want to name that
#     print(message)

# plus = 0
# for num in my_list:
#     plus = num + plus
# print(plus)

# cords = (1, 2)
# for cord in cords:
#     print(f"cord: {cord}") # this 'f"...:{...}"' is dot formatting

# list_cords = [(1, 2, 3), (3, 4, 7), (5, 6, 9), (7, 8, 0)]
# for x, y, z in list_cords:
#     print(f"cords:{z} , {x} , {y}")

# cars = {"name1": "benz", "name2": "pride"}
# for k, v in cars.items(): #this is tuple unpacking
#     print(f"car:{k} , {v}")

# people = {
#     1: {
#         "name": "jack",
#         "age": 3
#     },
#     2: {
#         "name": "david",
#         "age": 2
#     }
# }
# for a, b in people.items():
#     print(f"key:{a},value:{b}")
#     for key, value in b.items():
#         print(f"inner key: {key} , inner value: {value}")

# people_1 = [
#     {
#         "job": "engineer",
#         "education": "bachelor"
#     },
#     {
#         "job": "teacher",
#         "education": "master"
#     }
# ]
# print("\n")
# line = ""
# for item in people_1:
#     # for key,value in item.items():
#     #     print(f"{key}:{value}")

#     for key, value in item.items():
#         line += f"'{key}': '{value}',"
#     line += "\n"
# print(line)

# x = 0
# while x < 5:
#     print(f"the value of x is {x}")
#     x += 2
# else:
#     print(f"{x}")

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in numbers_list:
#     # pass
#     if num == 3:
#         continue
#     if num == 6:
#         break
#     print(num)


# x = 0
# while x <= 5:

#     if x == 2:
#         x += 1
#         continue
#     if x == 4:
#         break

#     print(f"x: {x}")
#     x += 1
# print("while done.")

# for num in range(1, 101):
#   if (not(num % 5)):
#     print(num)

# print(list(range(1,101,10)))

# index_count =0
# for letter in "abcde":
#   print("at index {} the letter is {}".format(index_count,letter))

#   index_count +=1

# index_count =0
# word ="dfghj"
# for letter in word :
#     print(word[index_count])
#     index_count +=1    this is counting the index of the word

# for index,letter in enumerate("ertyu"):
# print(index,letter,"\n")   this is counting the index of the word

# indentation iterate


# li1 = [1,2,3,4,5]
# li2 = ['a','b','c']
# li3 = list(zip(li1,li2))
# print(li3)

# if (1 in [1,2,3]):
#     print("in if")

# from random import shuffle #import a library like math or shuffle
# list_of_num = [1,2,3,4,5,6]
# shuffle(list_of_num)
# print(list_of_num)

# returns a number between 1 and 45333 (both included)
# from random import randint
# print(randint(1,45333))

# random_num = []
# x = 1
# while (x <= 100): # this works until 100 times
#     random_num.append(randint(1, 1000))
#     x += 1 # if this line dose'nt exist, we face to infinite loop
# print(random_num)


# result= input("what's your favorite color? ")
# print(type(result))

# age = int(input("how old are you?")) #explicit casting
# print(type(age))

# print("program is ending")

# my_list = [num for num in range(30,81)]
# print(my_list)

# my_list = [num for num in range(50,101) if not(num%2)]
# print(my_list)

# my_list = [number if number%2 else "even" for number in range(1,11)] # else just return srt.
# print(my_list)

# my_list = [f"{h} hour: {m} minute" for h in [1,2] for m in range(0,61)]
# print(my_list)

# my_list = []
# for h in [1,2]:
#     for m in range(0,5):
#         my_list.append(f"{h} hour: {m} minute")
# print(my_list)

# st = "print only the words that start with s in this sentence"
# words = st.split(" ")
# for word in words:
#     if word.startswith("s"):
#         print(word)

# my_list = [num for num in range(1,51) if not(num%3)]
# print(my_list)

# st = "print every word in this sentence that has an even number of letters"
# words = st.split(" ")
# for word in words:
#     if len(word) %2==0:
#         print(f"{word} : even")


# for inte in range(1,101):
#     if (inte % 3 == 0 and inte % 5 == 0):
#         print("FizzBuzz")
#     elif inte %5 == 0:
#         print("Buzz")
#     elif inte %3 == 0:
#         print("Fizz")
#     else:
#         print(inte)

# list2 = [1,2,3,4]
# print(list2[0])

# st = "create a list of the first letters of every word in this string"
# my_list = [word[0] for word in st.split(" ")]
# print(my_list)
