print("this is a program to count the uppercase and lower case letters in a given string")
def lettercount(s):                                   #Defining funtion
    uppernos = 0
    lowernos = 0
    
    for char in s:
        if char.isupper():  
            uppernos=uppernos+1
        elif char.islower():
            lowernos=lowernos+1
    
    print("Number of uppercase letters:", uppernos)
    print("Number of lowercase letters:", lowernos)

s =input("enter your string ")
lettercount(s)                                        #invoking funtion
print("CODED BY AMAL BENNY")

