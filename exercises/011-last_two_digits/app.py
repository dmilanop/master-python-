#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):
    if num > 9:
        num = int(str(num)[2:])
    else:
        print("intentalo otra vez")
    return num 

#Invoke the function with any interger greater than 9.
print(last_two_digits(1234))
