print("this is a program to count the uppercase and lower case letters in a given string")
def lettercount(s):                                   #Defining funtion
    a = 0
    b = 0
    
    for char in s:
        if char.isupper():  
            a=a+1
        elif char.islower():
            b=b+1
    
    print("Number of uppercase letters:", a)
    print("Number of lowercase letters:", b)

s =input("enter your string ")
lettercount(s)                                        #invoking funtion
print("CODED BY AMAL BENNY")

