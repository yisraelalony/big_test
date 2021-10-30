def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    new_string = string
    for char in string.casefold():
        if char not in "abcdefghijklmnopqrstuvwxyz":
            new_string = string.replace(char, "")


    backwards = new_string[::-1]
    return backwards.casefold() == new_string.casefold()

is_palindrome("")
word = input("give me a word:  ")
if is_palindrome(word):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))

answer = multiply(33, 10)
print(answer)

blue = multiply(1.223, 45)
print(blue)

for ting in range(1, 10):
    leads = multiply(ting, 3)
    print(leads)



