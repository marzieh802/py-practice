import re
text = "the trees need caring and we need trees."
pattern = "need"
m = re.search(pattern, text)

print(m.span())
print(m.start())
print(m.end())


# print(re.search(pattern,text).span())

print(re.findall(pattern, text))

for x in re.finditer(pattern, text):
    print("in for: ", x.span(), x.group())
print("*****************")
text2 = "I am the boss, we are in 2024-10-05 but I need the date of 2024-11-05"
date = re.findall(r"\d{4}-\d{2}-\d{2}", text2)
print(date)

iterator = re.finditer(r"[^\d,\s]{3,}", text2)
for x in iterator:
    print("3 or more: ", x.span(), x.group())
print("*****************")
text3 = "let's find this word 'Cat-87' In this sentence"

# print(re.findall(r"[a-a,A-Z]+", text3))
# print(re.findall(r"[a-z,1-9]+", text3))
print(re.findall(r"['a-zA-Z]+-[1-9']+", text3))

print("*****************")
text4 = "let's find this word 'weHaveToProtectPlanet-1' In this sentence and I'm a developer"
pattern = re.compile(r"(['a-zA-Z]+)-([1-9']+)")
result = re.search(pattern, text4)
print(result.group())
print(result.group(1), result.span(1))
print(result.group(2), result.span(2))

print(re.findall(r"[A-Za-z]+'[A-Za-z]", text4))

text5 = "00981111111111"
# [1-90]{9}

print(re.findall(r"^(09|0098)[0-9]{9}$", text5))

# truthy or falsy of list
print(True if re.findall(r"^(09|0098)[0-9]{9}$", text5) else False)

# match = re.match(r"^(09|0098)[0-9]{9}$", text5)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match found.")
