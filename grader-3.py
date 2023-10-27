
score = int(input("What is your score:")) #promts the user to type in a value, tha value has to be an integer otherwise it will not compute

if score >= 90: #value must be more than/ equal to 90 to get the result "A"
    print("You got an A!") 
elif score >= 75 and score < 90: #value must be more than/ equal to 75 and less than 90 to get the result "B"
    print("You got a B!")
elif score >= 65 and score < 75: #value must be more than/ equal to 65 and less than 75 to get the result "C"
    print("You got a C!")
elif score >= 50 and score < 65: #value must be more than/ equal to 50 and less than 65 to get the result "D"
    print("You got a D!")
else:
    print("You got an F!") #and other value less than 50 would get the result "F"