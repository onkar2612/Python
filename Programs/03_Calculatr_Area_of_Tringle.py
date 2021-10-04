# Formula of calculating area of triangle is A=(1/2) X base X Height Or A = (Base X Height)/ 2
# Another formula is Area = √[s(s-a)(s-b)(s-c)]


#First method
'''
Base = float(input("Enter a base of tringle: "))
Height = float(input("Enter Height of Triangle: "))
Area = (1/2) * Base * Height
print(Area)'''


#Second Method Creating a function
'''
def Area(base,height):
    result = (1/2)*base*height
    return result

Base = float(input("Enter a base of tringle: "))
Height = float(input("Enter Height of Triangle: "))

print("Area of tringle is",Area(Base,Height))'''

#Third method
import math
a = float(input("Enter First side: "))
b = float(input("Enter Second side: "))
c = float(input("Enter Third side: "))

s = (a+b+c)/2

Area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(Area)