punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str1= input("Enter a string: ")
new_str=''
for char in str1:
    if char not in punctuations:
        new_str+=char

print(new_str)
