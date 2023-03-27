
def lettercount(s):    #Defining funtion
    a = 0
    b = 0
    
    for letter in s:
        if letter.isupper():  
            a += 1
        elif letter.islower():
            b += 1
    
    print("Number of uppercase letters:", a)
    print("Number of lowercase letters:", b)

s =input("enter your string ")
lettercount(s)    #invoking funtion
