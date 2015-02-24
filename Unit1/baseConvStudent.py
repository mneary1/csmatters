#CSMatters File for Unit 1.6
#Creator: Caroline Kery 2/16/2015
#This is the answer file





#This program will take a number in one base and convert it into a different 
#base.

#This function controls the flow of the program.
def main ():

    #Welcome the user
    print("Welcome to the base converter!")
    print("Remember, the values for a base should never equal or exceed that number!")
    print("ex: for base 3, only use 0,1,2. For base 16, only use 1-9 and A-G")

    #Take user input for the basees and number
    base = getInput("What is your base? Must be between 2 and 25: ",2,25,10);
    
    num = getInput("What is your number? Must be less than 25^25 and greater than 0: ",0,25**25,int(base));
    
    newBase = getInput("What is the new base? Must be between 2 and 25: ",2,25,10);
    #Print out the new number using the baseConverter function
    print("Your new number in base ",newBase," is ",baseConverter(num,int(base),int(newBase)))



#This function will read in input from the user and checks that it is valid
#It will keep asking until a valid input is given
#Input: A message to read out to the user. 
#The minimum and maximum allowed for the number as a whole. 
#The charMax is the maximum value for a single character. For the bases, it
#is ten, as the base numbers themselves are written in base ten. The number
#given must have induvidual values less then the original base.
def getInput(message,minimum,maximum,charMax):
    answer = input(message)
    ok = False
    while not ok:
        good = True 
        #check if the whole number is less then the max. First make sure it
        #is in base ten
        answer10 = int(anythingToTen(charMax,answer))
        if (answer10<minimum or answer10>maximum):
            good = False
        else:
            for i in answer:
                if(not isdigit(i)):
                    #change to its corrosponding number
                    i = powerOrLetter(i)
                i = int(i)
                #check if it is less then the character max
                if(i>=charMax):
                    #If good is False, some digit in answer is not valid
                    good = False
        if not good:
            #answer is invalid, so ask again
            answer = input("Input invalid. Please try again: ")
        else:
            #if answer was never proven invalid, it is good so you can return it
            ok = True
    return answer

#This function simply puts the two steps together
def baseConverter(num,base1,base2):

    return tenToAnything(anythingToTen(base1,num),base2)    



#This function receives either a number or a letter. It then figures out
#which one it is given, and returns its corrosponding letter or number
def powerOrLetter(numOrChar):

        if(isdigit(numOrChar)):
            num = int(numOrChar)
            #Create your new ASCII value. The ASCII of A = 65 and
            #corrosponds with 10
            ascii = 65+(num-10)
            numOrChar = chr(ascii)
            #convert back to character
        else:
            #Bases only use uppercasd letters, so make sure to make everything
            #uppercase
            numOrChar = numOrChar.upper()
            #convert from letter to number A = 10, Z = 35
            character = ord(numOrChar)
            #The ASCII value of A is 65, so by subtracting 55 from the 
            #letters ASCII, one will get their equivalent value.
            numOrChar = character-55

        return numOrChar


#This function takes a number in any base and converts it to base ten
def anythingToTen(base1,number):
        #Change the number into a string in order to examine induvidual 
        #characters.
        charNum = str(number)

        total = 0

        #Start from the last character (length-1) which corrosponds to the
        #zeroth power
        i = len(charNum)-1
        power = 0

        #This while loop iterates over every digit in the number from right
        #to left.
        while(i>=0):
            aI = charNum[i]
            
            #if the digit is a letter, turn it into a number
            if(not isdigit(aI)):
                aI = powerOrLetter(aI)
            
            aI = int(aI)
            
            #Multiply digit times that base^power to get its base 10 value
            #Add this to the total
            add =  aI*(base1**power)
            total+=add
            
            i-=1
            power+=1
        #return the base ten value
        return int(total)


#This function is the other half of the equation. It takes a base ten value
#and turns it into a different base
def tenToAnything(number, base2):
        
        #i keeps track of the highest power of the base the number given goes to
        #For example: i of 20 for binary is 4 because 16 is the highest
        #power of two that is less then 20
 
        #x is the base^i, or the value of that highest slot (16 for the previous
        #example).
        i = 0
        x = 0
        answer = ""

        #This loop keeps testing powers until it finds the right x and i
        while x<number:
            i+=1
            x = base2**i

        #firstSlot is the actual value to be placed in the left-most slot
        firstSlot = number//x
 
        #Subtract x*firstSlot from number to avoid repeats
        number-=(firstSlot*x)

        #No number starts with a zero, so only bother if it is >0
        #If firstSlot is greater then 9, it needs to be represented by a letter
        if(firstSlot>0):
            if(firstSlot>9):
                firstSlot = powerOrLetter(firstSlot)
            #Add firstSlot to the string so that "" + "#" = "#"
            answer+=str(firstSlot)

        #Repeat the above steps on the rest of the digits, decreasing the power
        #until it becomes zero. (rightmost slot)
        i-=1
        while(i>=0):

            x = base2**i
            nSlot = number//x

            number-=(nSlot*x)

            if(nSlot>9):
                nSlot = powerOrLetter(nSlot)

            answer+=str(nSlot)
            i-=1
        #Return final solution in the form of a String
        return answer
#This function merely returns True if the given character is a number, and 
#False otherwise
def isdigit(number):
    #Basically, try to typecast the character. If it causes an error, it is
    #not a number
    try:
        int(number)
        return True
    except ValueError:
        return False

#Always put main() at the bottom so the program will run
main() 
 
