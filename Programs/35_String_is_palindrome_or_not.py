str1 = input("Enter a string: ")
str1 = str1.casefold()

str2 = "".join(reversed(str1))


if(str1==str2):
    print(f"{str1} is Palindrome string")
else:
    print(f"{str1} is not-Palindrome string")
