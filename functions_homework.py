import math


# def vol(rad):

#     return ((4/3)*math.pi*(rad**3))


# volume = vol(2)
# print(volume)

# vol = lambda rad : ((4/3)*math.pi*(rad**3))
# volume = vol(2)
# print(volume)

# def ran_check(num,low,high):
#     if(num in range(low,high + 1)):
#         return f"{num} is in the range between {low} and {high}"
#     else:
#         return f"{num} is not in the range between {low} and {high}"
# result_string = ran_check(5,2,7)
# print(result_string)


# def ran_check(num, low, high):
#   return (num in range(low,high + 1)) # return (low <= num <= high)
# result_string = ran_check(11,1,10)
# print(result_string)

# def up_low(s):
#     upper_count = 0
#     lower_count = 0
#     for letter in s:
#         if (letter.isupper()):
#             upper_count += 1
#         elif (letter.islower()):
#             lower_count += 1
#     return f"Original String :{s} \nNo. upper case characters : {upper_count} \nNo. lower case characters : {lower_count}"
# string = up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
# print(string)


# def unique_list(lst):
#     return list(set(lst))
# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# def multiply(nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
# print(multiply([1,2,3,-4]))

# def palindrome(s):
#     text = s.replace(' ','')
#     return (text == text[::-1])
    
# # print(palindrome('ma d am'))

# import string
# def ispangram(str1 , alphabet = string.ascii_lowercase):
#     txt = str1.replace(' ','')
#     txt= txt.lower()
#     for letter in txt:
#         alphabet = alphabet.replace(letter,'')
#     print(alphabet) #debugging print
#     return alphabet == ''
        
# print(ispangram("The quick brown fox jumps over the lazy dog"))


