words = ["Activism","Activist","Bigotry","Boycott","Courage","Creed","Desolate","Dignity","Dream","Equality","Freedom","Holiday","Intolerance","January","Legacy","March","Memorial","Minister","Oasis","Reagan","Reverend"]


x = 15
y = 16

for i in range(len(words)):
    # Capitalize each element in the array
    words[i] = words[i].upper()

#reverses all words
backwords = []
for i in words:
    backwords.append(i[::-1])


bank = [["O","M","D","U","E","C","N","A","R","E","L","O","T","N","I"],
        ["M","S","R","R","L","I","E","V","C","D","E","E","R","C","E"],
        ["O","I","E","S","B","B","I","G","O","T","R","Y","Y","E","E"],
        ["D","V","A","G","L","I","E","R","A","T","I","C","N","T","T"],
        ["E","I","M","O","E","A","E","Q","T","R","A","V","A","N","D"],
        ["E","T","T","H","E","V","I","O","U","G","U","L","I","D","A"],
        ["R","C","Y","W","E","R","C","R","E","A","O","O","E","S","B"],
        ["F","A","E","R","E","Y","J","L","O","S","L","C","C","D","T"],
        ["O","M","E","A","O","E","A","S","E","M","I","I","I","L","H"],
        ["E","N","G","B","N","T","N","D","A","B","E","G","T","O","O"],
        ["D","A","U","T","S","T","U","H","I","N","N","M","H","Y","L"],
        ["N","G","S","I","T","H","A","A","T","I","M","A","C","T","I"],
        ["T","E","S","R","F","T","R","Z","T","Q","C","M","R","H","D"],
        ["Q","A","N","R","J","L","Y","Y","H","H","Y","T","A","P","A"],
        ["O","D","M","I","N","I","S","T","E","R","W","N","M","F","Y"]]

#simple = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
simple = bank
transposed = []

for iter1 in range(len(bank[0])):
    col = []
    for iter2 in range(len(bank)):
        col.append(bank[iter2][iter1])
    transposed.append(col)

#print(transposed)
    
diagonalized = []
diagonalized2 = []
rows = len(simple)
cols = len(simple[0])

for i in range(rows + cols - 1):
    temp = []
    for j in range(max(0, i - rows + 1), min(cols, i + 1)):
        temp.append(simple[i - j][j])
    diagonalized.append(temp)

#print(diagonalized)

for i in range(rows + cols - 1):
    temp = []
    for j in range(max(0, i - rows + 1), min(cols, i + 1)):
        temp.append(simple[i - j][cols - j - 1])  # Traverse columns in reverse order
    diagonalized2.append(temp)

print(diagonalized2)

locs = []



str1 = ""
str2 = ""
str3 = ""
str4 = ""


for arr in bank:
    for i in arr:
        str1 = str1 + i

print(str1)

for arr in transposed:
    for i in arr:
        str2 = str2 + i

for arr in diagonalized:
    for i in arr:
        str3 = str3 + i

for arr in diagonalized2:
    for i in arr:
        str4 = str4 + i

#str1 = "".join(bank)
print(str2)
for letters in "hi":
    for word in words[:]:  # Iterate over a copy of the list
        sub = str1.find(word)
        if sub != -1:
            loc = [word, sub, "a"]
            locs.append(loc)
            words.remove(word)

    #print(locs)
    #print(words)


    for word in words[:]:  # Iterate over a copy of the list
        sub = str2.find(word)
        if sub != -1:
            loc = [word, sub, "d"]
            locs.append(loc)
            words.remove(word)
    

    #diagnalized
    for word in words[:]:  # Iterate over a copy of the list
        sub = str3.find(word)
        if sub != -1:
            loc = [word, sub, "lr"]
            locs.append(loc)
            words.remove(word)

    for word in words[:]:  # Iterate over a copy of the list
        sub = str4.find(word)
        if sub != -1:
            loc = [word, sub, "rl"]
            locs.append(loc)
            words.remove(word)
    #print(locs)
    #print(words)
    words = backwords


print(locs)
print(len(locs))