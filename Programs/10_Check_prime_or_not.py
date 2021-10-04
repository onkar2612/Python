def Is_prime(n):
    flag = True
    if n==0 or n==1:
        flag = False   
    else:
        for i in range(2,int((n/2))):
            if(n%i==0):
                flag = False                
                break
    return flag


if __name__=="__main__":
    print(Is_prime(9))
    print(Is_prime(5))
    print(Is_prime(13))
    print(Is_prime(98))