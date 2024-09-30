# def spy_game(array):
#     target = [0,0,7]
#     active_index = 0
#     for num in array:
#         if (num == target[active_index]):
#             if (target[active_index] == 7):
#                 return True
#             else:
#                 active_index += 1
#     return False
# print(spy_game([1,2,4,0,3,0,7,5]))

# def count_primes(top):
#     primes_num = 0
#     for num in range(2,top+1): # 2-11 num = 11
#         for digit in range(2,num+1): # 2-11 digit = 11
#             if(num % digit == 0 ): # t  if (not(num % digit))
#                 if(num != digit): # f 
#                     break
#                 primes_num += 1 # 5
#     return primes_num
# print(count_primes(100))


# my_list = [[1,2,3,4],[5,6,7,8]]
# print(my_list[1][2])
# my_list[0][3] = 9
# print(my_list[0][3])
# print(my_list)
# for num in my_list:
#     print(num)
#     for num1 in num:
#         print(num1)

# def print_big(letter):
#     patterns = {
#         'a':[[0,0,1,0,0],[0,1,0,1,0],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]],
#         'h':[[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]],
#         'm':[[1,0,0,0,1],[1,1,0,1,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1]],
#         'heart':[[0,1,0,1,0],[1,0,1,0,1],[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0]]
#     }
#     if (letter in patterns):
#         result = ''
#         for row in patterns[letter]:
#             for value in row:
#                 if(value):
#                     result += '*'
#                 else:
#                     result += ' '
#             result += '\n'
#         return result

# star = f"{print_big('h')} \n{print_big('heart')}\n{print_big('m')}"
# print(star)

# list_3d = [[1,2,3],[4,5,6]],[[7,8,9],[10,11]]
# print(list_3d[1][0][0])
# for layer1 in list_3d:
#     for layer2 in layer1:
#         for value in layer2:
#             print(value)
