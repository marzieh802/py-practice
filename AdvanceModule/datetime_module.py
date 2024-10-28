from datetime import date, datetime
from time import time
from timeit import timeit
# first = datetime.now()
first = time()

my_date = date(2024, 7, 1)
print(my_date)

print(my_date.year)
print(my_date.month)

my_date2 = date(2023, 7, 1)

dif = my_date - my_date2
print(dif)

today = date.today()
print(today)

dt1 = datetime(2020, 4, 30, 18, 20)
print(dt1)

dt2 = datetime(2023, 4, 1, 18, 21)

dif_dt = dt2 - dt1
print(dif_dt.total_seconds())

print(datetime.now())


def test(n):

    a = 1
    b = []
    while (a < n):
        b.append(a + 2)
        with open("./test.txt", "w") as file1:
            file1.write(f"{a}")
            print("created!", a)
        a += 1


# test(1_000)

# last = datetime.now()
last = time()
program_diff = last - first
# print("Program execution length: ", program_diff.total_seconds())
# print("Program execution length: ", program_diff)

statement = '''
test(1_000)

'''
setup = '''
def test(n):

    a = 1
    b = []
    while (a < n):
        b.append(a + 2)
        with open("./test.txt", "w") as file1:
            file1.write(f"{a}")
            print("created!", a)
        a += 1


'''
time_elapsed = timeit(statement, setup, number=30)
print(time_elapsed)
