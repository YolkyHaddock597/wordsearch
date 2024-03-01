words = ["children","careless","replace","numberless","selective","evasive","loaf","morning","year","defeated","general","reduce"]

x = 12
y = 8

for i in range(len(words)):
    # Capitalize each element (string) in the array
    words[i] = words[i].upper()


bank = ["M", "O", "R", "N", "I", "N", "G", "Y", "E", "A", "R", "G",
        "C", "N", "U", "M", "B", "E", "R", "L", "E", "S", "S", "E",
        "T", "K", "D", "E", "F", "E", "A", "T", "E", "D", "K", "N",
        "L", "M", "H", "Q", "R", "E", "P", "L", "A", "C", "E", "E",
        "O", "C", "A", "R", "E", "L", "E", "S", "S", "Z", "J", "R",
        "A", "U", "C", "H", "I", "L", "D", "R", "E", "N", "H", "A",
        "F", "E", "V", "A", "S", "I", "V", "E", "R", "J", "V", "L",
        "Y", "X", "S", "E", "L", "E", "C", "T", "I", "V", "E", "S"]

locs = []


str1 = ""


for i in bank:
    str1 = str1 + i

str1 = "".join(bank)
print(str1)

for i in words: 
    sub = str1.find(i)
    if sub != -1:
        loc = [i, sub]
        locs.append(loc)
        words.remove(i)


print(locs)

print(words)



def calculate_coordinates(index):
    row = index // x
    col = index % x
    if col == 0:
        col = x  # Adjust column index to array width if it's currently 0
        row -= 1  # Adjust row index accordingly
    return col, row

def calculate_index(row, col):
    return (col + ((row-1)*x))

def calc_combos(word, index):
    nume = 1
    adder = 0
    if (index - (12*len(word) > -1)):
        if (word[1] == index-12):
            print("hit")
    
    for index, letter in enumerate(bank):
        if index + (12 * len(word)) < x * y:
            adder = index
            for char in word:
                try:
                    adder += 12
                    #print(adder)
                    if bank[adder] == word[nume]:
                        print(True)
                        print(calculate_coordinates(index+1))
                    else:
                        break
                except IndexError:
                    pass
        else:
            pass  # Handle the case when index + (12 * len(word)) >= x * y

    
        


for word in words:
    first_letter = word[0]
    for indx1, letter in enumerate(bank):
        if letter == first_letter:
            #print("Found", first_letter, "at index", indx1)
            calc_combos(word, indx1)