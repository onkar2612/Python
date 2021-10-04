def Dec_to_binary(n):
    if n>1:
        Dec_to_binary(n//2)
    print(n % 2,end='')

if __name__=="__main__":
    Dec_to_binary(34)