import calendar
try:
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    print(calendar.month(year,month))
            
except:
    print("Please enter write value")