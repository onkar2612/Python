def Check_num(num):
    if(num>0):
        print(num,"Positive number")    
    elif(num<0):
        print(num,"Negative number")    
    elif(num==0):
        print(num,"is zero")    
    else:
        print("Enter valid number")
    
if __name__=="__main__":
    Check_num(10)
    Check_num(-10)
    Check_num(0)
