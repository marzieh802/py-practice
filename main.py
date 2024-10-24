# open function is for opening files
content = open("/media/h3m/New Volume/Learning/py_practice/test.txt")

print("first: ", content.read())
content.seek(1)
print("again:", content.read())

content.seek(0)

print("readLine: ", content.readline())
print("readLine: ", content.readline())
print("readLine: ", content.readlines())
print("readLine: ", content.read())

content.close()  # we have to 'close' the file if we write open function like that

path_to_file = "/media/h3m/New Volume/Learning/py_practice/test.txt"

with open(path_to_file, mode="w") as content1:  # this address is absolute --> start from '/'
    content1.write("test1\ntest2\ntest3\ntest4\n")


value_in_file = ""
with open(path_to_file, mode="w") as c1:  # mode'w' is for writing
    # every write, writes from first line and deletes the pervious tests
    c1.write("inside write")


# mode'r' is for reading the test from every seek() that we want
with open(path_to_file, mode="r") as content1:
    print("first in with: ", content1.read())
    content1.seek(0)
    value_in_file = content1.read()
    print("second in with: ", value_in_file)


print("outside of with: ", value_in_file)
# print("outside of with: ",content1.read())

# mode'a' is for appending the file without deleting the pervious text
with open(path_to_file, mode="a") as c:
    c.write("\ntest9")  # \n is for entering line to the next
# we do not need to close the file if we write open function with "with as"
