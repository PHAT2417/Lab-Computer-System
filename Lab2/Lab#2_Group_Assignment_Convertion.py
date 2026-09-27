# This program aims to converts a signed integer between signed magnitude and 2's complement. The input could be signed magnitude or 2's complement
#Kristine Nguyen
#Question 2

#ask user for their input and if it returns false 
def checkingInput(answer, answerType):
    if ((answerType != "2C") and (answerType != "SM")): 
        print("Please input either 2C or SM for the type!")
        return False
    if (len(answer) != 8): # making sure its 8 characters
        print("Your answer needs 8 characters!")
        return False
    if not all(bit in "01" for bit in answer): # making sure it's binary only
        print("Your answer must contain only 0s and 1s!")
        return False
    return True


#the first bit stays the same while the rest inverts
def invert(answer):
    return answer[0] + ''.join('1' if bit == '0' else '0' for bit in answer[1:])


def functionConvertion(answer):
    if (answer.startswith("0")): #the answer will be positive for both SM and 2's Complement
        return answer
    
    invertedanswer = invert(answer)
    
    carryOver = 1
    resultantString = ""
    for i in range(len(invertedanswer) - 1, -1, -1): # will loop through  every character except for the first 
        bit = int(invertedanswer[i]) + carryOver # adding one to the integer value of the bit 
        #carry over if there is any
        if bit == 1: 
            carryOver = 0
        elif bit == 2: 
            bit = bit % 2
            carryOver = 1

        resultantString = str(bit) + resultantString
    
    return resultantString


def askInput():
    #ask the user for their input if it returns true 
    while (True):
        answer = input("Input an 8-bit binary string!: ")
        answerType = input("Is this [2C] 2's complement or [SM] Signed magnitude?:").strip().upper()
        isValid = checkingInput(answer, answerType)
        if (isValid == True):
            break 
    convertedValue = functionConvertion(answer)
    print(convertedValue)
    
askInput()
    


