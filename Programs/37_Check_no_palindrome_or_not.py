

if __name__=="__main__":
    n=123321
    re=0
    n1=n
    while(n1!=0):
        rem = n1%10

        re=re*10+rem

        n1//=10
    if(re == n):
        print(f" {n} is palindrome numer")
    else:
        print(f" {n} is not-palindrome numer")
    