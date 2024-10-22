from collections import Counter,defaultdict,namedtuple #these are advance datatypes
my_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
c = Counter(my_list)
c1 = Counter("hello world")
c2 = Counter("hello hello world".split(" "))
print(c)

for i,x in c2.items():
  print(i,x)

d = {"a":1,"m":2}
# print(d["jack"])
d1 = defaultdict(lambda : "is not")
d1["k1"] = 9
print(d1["k1"])
print(d1["jack"])
print(d1)

t = (1,2)
print(t[0])
Cat = namedtuple("cat",["name","age"])
cat1 = Cat(name="jack",age=2)
print(cat1.name,cat1.age)