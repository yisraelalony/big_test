def multiply(x, y):
    result = x * y
    return result


def is_palidrome(string):
    for char in string.casefold():
        if char not in "abcdefghijklmnopqrstuvwxyz":
            neww_string = string.replace(char, "")


    backwards = neww_string[::-1]
    return backwards.casefold() == neww_string.casefold()

word = input("give me a word:  ")
if is_palidrome(word):
    print("{} is a paladrom".format(word))
else:
    print("{} is not a paladrom".format(word))

answer = multiply(33, 10)
print(answer)

blue = multiply(1.223, 45)
print(blue)

for ting in range(1, 10):
    leads = multiply(ting, 3)
    print(leads)




