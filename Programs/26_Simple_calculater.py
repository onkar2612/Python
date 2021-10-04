try:
    n1 = int(input("Enter a first number: "))
    op = input("Enter a operation: ")
    n2 = int(input("Enter a second number: "))

    if op == '+':
        print("Sum of numbers is ",n1+n2)
    elif op == '-':
        print("Substraction of numbers is ",n1-n2)
    elif op == '*':
        print("Multiplication of numbers is ",n1*n2)
    elif op == '/':
        print("Dividation of numbers is ",n1//n2)
    else:
        print("Invalid input")
except:
    print("Please enter floating numbers")

