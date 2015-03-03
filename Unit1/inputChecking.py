#This file's purpose is to practice checking inputs and using operators such
#as loops and if statements. 

def main():
    #Print out welcome
    print("Hello there! \n This program will take a number and run it through")
    print(" a series of tests.")

    #Use getValidInput to get a number
    number = getValidInput("Please enter your number.")

    #This boolean will be false until the user decides to end the program
    done = False
 
    #This loop will keep going until the user indicates the program should end
    while not done:
        
        #Print out menu
        print("\nPlease pick a choice:\n1. Is Even?\n2. Is positive?")
        print("3. Is a factor of 3?\n4.Is a perfect square?\n5. Quit")
      
        #Get input from the user
        choice = getValidInput("")
        
        print("")
 
        #These if statements will check the input from the user and run the
        #correct tests
        if(choice == 5):
            #If the user typed 5, they want to quit, so we make our loop end
            #by making done true
            done = True;
        
        elif(choice == 4):
            perfectSquare(number)
       
        elif(choice == 3):
            factorOfThree(number)

        elif(choice == 2):
            isPositive(number)
        
        elif(choice == 1):
            isEven(number)
   
        else:
            #If the number given was not between one and 5, it will hit this
            #else and print the error.
            print("Invalid number. Please try again.")

#This function checks if a given input is a number. It will keep asking
#until the user types in a number.
def getValidInput(message):
    
    good = False
    #This is very similiar to the while loop above. It will keep going until
    #the boolean good is proven true. This hap[pens when a valid input is 
    #entered
    while not good:
        #Get input from user. Check if it is a number. 
        number = input(message)

        if(number.isdigit() == True):
            #If it is, end the loop
            good = True;
        
        else:
            #if it is not a number, tell the user
            print("That is not a number. Please try again.")
    #return the number
    return int(number)



#This function checks if the number is even
def isEven (number):

    #What makes a number even? Fill in the contents of this if statement
    if(number % 2 == 0):
        print("It is even")
    else:
        print("It is odd")
    return

#This function checks if the number is positive
def isPositive(number):
   
    #What nmakes a number positive? Fill in the if statement
    if(number>0):
        print("It is positive")
    else:
        print("It is negative")
    return

#This function checks if the number is a multiple of three
def factorOfThree(number):
   
    #This if statement should look a lot like the one in isEven
    if(number % 3 == 0):
        print("It is divisible by three")
    else:
        print("It is not divisible by three")

#This function checks if the number is a perfect square
def perfectSquare(number):

    #This variable keeps track of the root we are checking
    root = 1

    #How would we check if a number is a perfect square? Use root to fill
    #in the condition for the while loop and if statement
    while(root<number):

        
        if(root*root == number):
            print("It is a perfect square")
            return
        
        root+=1

    print("It is not a perfect square")
    return 

main() 
    
