#Matthew Zhang
#CS 102 Spring 2020
#February 20th
#Program: Dice Solitare
#Plays a single player dice game in which the user must reach 50 points through rolling dice. Each turn includes an infinite number of rolls which increases their score
#until they choose to hold or their dice roll equals 2, 7, or 12. Should the happen, all points for that round will be forfeited.


import random

def roll(dice1, dice2, turnScore):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    turnScore = dice1 + dice2 #User's score for this turn
    return dice1, dice2, turnScore

def main():
    dice1 = 0
    dice2 = 0
    overallScore = 0
    turnScore = 0
    turnScoreHolder = 0  #Holder for your score, as the current score will have it's conditions checked and reset for the next turn.
    turns = 0 #Counts the number of turns you take to win the game
    choice = ''
    
    print("Welcome to Dice Solitaire! We play to 50. You know the rules - let’s begin!")
    print("Your total score is", overallScore)

    #Count until the score reaches 50, then end the game.
    while(overallScore < 50):
        turns += 1
        dice1, dice2, turnScore = roll(dice1, dice2, turnScore) #Call the function which "rolls your dice"
        turnScoreHolder += turnScore
        print("Your first roll this turn is", dice1, "&", dice2)
        #2nd while loop for the additional turns after the first one:
        while True:
            #First 3 if statements check if the dice will make the user lose.
            if(turnScore == 2):
                print("Your next roll is a", dice1, "&", dice2, "Busted! You lost all turn-points.")
                print("After", turns, "turns you have a total score of", overallScore)
                turnScoreHolder = 0
                break
            
            elif(turnScore == 7):
                print("Your next roll is a", dice1, "&", dice2, "Busted! You lost all turn-points.")
                print("After", turns, "turns you have a total score of", overallScore)
                turnScoreHolder = 0
                break
            
            elif(turnScore == 12):
                print("Your next roll is a", dice1, "&", dice2, "Busted! You lost all turn-points.")
                print("After", turns, "turns you have a total score of", overallScore)
                turnScoreHolder = 0
                break
            
            #If the dice passes all conditions:
            else:
                print("Your next roll is a", dice1, "&", dice2, "You now have", turnScoreHolder, "turn-points.")
                choice = input("Would you like to Roll or Hold? (R/H): ")
                #Answer must be capitalized to be accepted
                if(choice == 'R'): #Rolls the dice again and runs through the condition checks again.
                    dice1, dice2, turnScore = roll(dice1, dice2, turnScore)
                    turnScoreHolder += turnScore
                    continue
                
                elif(choice == 'H'): #Breaks the secondary while loop and starts a new round for the user
                    print("You held.")
                    overallScore += turnScoreHolder
                    turnScoreHolder = 0
                    print("After", turns, "turns you have a total score of", overallScore)
                    break
                
                else:
                    print("Sorry, that is not a permissible choice.")
    
    #Final statment
    print("Congratulations! You Won! It took you", turns, "turns.")  
    
main()