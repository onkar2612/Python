def Check_leap(num):
    if (num % 4) == 0:
        if (num % 100) == 0:
            if (num % 400) == 0:
                print(f"{num} is a leap Year")
            else:
                print(f"{num} is not a leap Year")
        else:
            print(f"{num} is a leap Year")
    else:
        print(f"{num} is not a leap Year")

if __name__=="__main__":
    Check_leap(2004)
    Check_leap(2000)
    Check_leap(2021)
    Check_leap(2050)