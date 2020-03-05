#Matthew Zhang
#CS 102 Spring 2020
#March 3rd
#Program: heading toward nothing
#Calculates how many rounds of subtractions it takes for a randomly generated list of ints to calculate its way down to zero, if possible.

import random

#Function to populate the list with random integers.
def initial(storeNum):
    #The number of ints to put into the list
    startNum = 0
    keepGoing = True
    #While loop to ensure input is a valid positive whole integer.
    while keepGoing:
        startNum = float(input("Welcome to Heading toward nothing, please enter the amount of #s you want calculated: "))
        #Rounds user's response to nearest whole number.
        startNum = int(round(startNum))
        if(startNum <= 0):
            print("Error: must be greater than 0. Try again. ")
        else:
            keepGoing = False
    
    #While loop to populate list with the amount of integers the user wants to use for calculation.
    i = 0
    while(i < startNum):
        storeNum.append(random.randint(0, 50))
        i += 1
    
    print("Initial list of integers: ", storeNum)
    return storeNum

#Function for subtraction calculation in the integer list.
def update(storeNum):
    i = 0
    #Creates a new list to temporarily store values from storeNum list for calculation purposes
    rvalue = []
    rvalue = storeNum.copy()
    #Performs calculation on all the numbers in the list
    while(i < len(rvalue)):
        rvalue[i] = abs(rvalue[i-1] - rvalue[i])
        i += 1
    print("Current list:", rvalue)
    #returns result to main function, where the storeNum values will be replaced with rvalue calculations.
    return rvalue

#Determines how the program prints the appropriate final message.
def finished(storeNum):
    count = 0
    #Counts through list to make sure all values are 0.
    while(count < len(storeNum)):
        #If not all values are 0, return false.
        if(count >= 0):
            return False
        #Continues the while loop until all values are read through, ensuring everything in the list is 0.
        else:
            continue
        count += 1
    #Flips the fvalue bool to True, allowing the attempt to reach 0 message be printed.
    return True

def main():
    #For the list of ints undergoing calculation.
    storeNum = []
    #Retains the original list of ints before calculation.
    archiveN = []
    #Fvalue will be set to false by default, ensuring that conditions of having the entire list full of zeroes has not been met yet.
    fvalue = False
    #Used to determine the final apporpriate message for the user, based on whether their list reached all zeroes or not.
    response = 0
    #Used for iteration in the amount of times to run update.
    j = 0
    #Used to determine whether the user wants to continue running update or not.
    k = True

    #Counts the number of rounds you run the program for.
    rounds = 1 

    #Calls initial to start the program, passes in an empty list and returns with a populated initial list.
    storeNum = initial(storeNum)
    #Saves original list for ending message purposes.
    archiveN.append(storeNum)
    #Run the update function once, passing in the current list of ints, and returning with a calculated list of ints.
    storeNum = update(storeNum)
    
    #Loop to regulate how many times you'd like to run the update function.
    while(k == True):
        response = float(input("How many rounds would you like to continue for: "))
        #Rounds the response to nearest whole number.
        response = int(round(response))
        #Ends the while loop and moves the user to the final part of the program
        if(response == 0):
            k = False
        #Continues running update for as long as the user specified.
        else:
            for j in range(response):
                storeNum = update(storeNum)
                j += 1
                rounds += 1

    #Final statments
    print("Original list: ", archiveN)
    print("Final list: ", storeNum)
    
    #Passes in the final list to the finished function for judgement on whether the list finished with all zeroes or not.
    fvalue = finished(storeNum)
    #List did not finish with all zeroes.
    if(fvalue == False):
        print(rounds, "rounds were attempted")
    #List finished with all zeroes
    else:
        print("Took this many rounds to get to 0: ", rounds)
    
main()