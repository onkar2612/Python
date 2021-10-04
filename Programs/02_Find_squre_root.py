# First Method

'''num = float(input("Enter a number: "))
squre_root=num**0.5
print(squre_root)'''



# Second Method By creating function

'''def sqrt(num):
    result=num**0.5
    return result

num = float(input("Enter a number: "))
print(sqrt(num))'''



# Third method Using library

import math
num = float(input("Enter a number: "))
print(math.sqrt(num))


