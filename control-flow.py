# nature = "mountains"

# if nature == "jungle":
#     print("Let's go to the jungle")
# elif(nature == "mountains"):
#     print("Let's go to the mountains")
# else:
#     print("where should we go?")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    if not (num % 2):

        print(num)

message = "earth: please protect me"

for _ in message:
    print("hello")

plus = 0
for num in my_list:
    plus = num + plus
print(plus)

cords = (1, 2)
for cord in cords:
    print(f"cord: {cord}")

list_cords = [(1, 2, 3), (3, 4, 7), (5, 6, 9), (7, 8, 0)]
for x, y, z in list_cords:
    print(f"cords:{z} , {x} , {y}")

cars = {"name1": "benz", "name2": "pride"}
for k, v in cars.items():
    print(f"car:{k} , {v}")

people = {
    1: {
        "name": "jack",
        "age": 3
    },
    2: {
        "name": "david",
        "age": 2
    }
}
for a, b in people.items():
    print(f"key:{a},value:{b}")
    for key, value in b.items():
        print(f"inner key: {key} , inner value: {value}")

people_1 = [
    {
        "job": "engineer",
        "education": "bachelor"
    },
    {
        "job": "teacher",
        "education": "master"
    }
]
print("\n")
line = ""
for item in people_1:
    # for key,value in item.items():
    #     print(f"{key}:{value}")

    for key, value in item.items():
        line += f"'{key}': '{value}',"
    line+= "\n"
print(line)
