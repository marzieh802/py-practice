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

def count_primes(top):
    primes_num = 0
    for num in range(2,top+1): # 2-11 num = 11
        for digit in range(2,num+1): # 2-11 digit = 11
            if(num % digit == 0 ): # t  if (not(num % digit))
                if(num != digit): # f 
                    break
                primes_num += 1 # 5
    return primes_num
print(count_primes(201000))