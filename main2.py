words = ["children","careless","replace","numberless","selective","evasive","loaf","morning","year","defeated","general","reduce"]

x = 12
y = 8

for i in range(len(words)):
    # Capitalize each element in the array
    words[i] = words[i].upper()


bank = [["M", "O", "R", "N", "I", "N", "G", "Y", "E", "A", "R", "G"],
        ["C", "N", "U", "M", "B", "E", "R", "L", "E", "S", "S", "E"],
        ["T", "K", "D", "E", "F", "E", "A", "T", "E", "D", "K", "N"],
        ["L", "M", "H", "Q", "R", "E", "P", "L", "A", "C", "E", "E"],
        ["O", "C", "A", "R", "E", "L", "E", "S", "S", "Z", "J", "R"],
        ["A", "U", "C", "H", "I", "L", "D", "R", "E", "N", "H", "A"],
        ["F", "E", "V", "A", "S", "I", "V", "E", "R", "J", "V", "L"],
        ["Y", "X", "S", "E", "L", "E", "C", "T", "I", "V", "E", "S"]]

transposed = []

for iter1 in range(len(bank[0])):
    col = []
    for iter2 in range(len(bank)):
        col.append(bank[iter2][iter1])
    transposed.append(col)

#print(transposed)

shearR = []
fo

locs = []


str1 = ""
str2 = ""



for arr in bank:
    for i in arr:
        str1 = str1 + i

print(str1)

for arr in transposed:
    for i in arr:
        str2 = str2 + i

#str1 = "".join(bank)
#print(str1)

for i in words: 
    sub = str1.find(i)
    if sub != -1:
        loc = [i, sub]
        locs.append(loc)
        words.remove(i)

print(locs)
print(words)


for i in words: 
    sub = str2.find(i)
    if sub != -1:
        loc = [i, sub]
        locs.append(loc)
        words.remove(i)

print(locs)
print(words)