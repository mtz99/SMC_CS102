#Matthew Zhang
#CS 102 Spring 2020
#February 13th
#Program: weights
#Asks the user to input two people's weights in pounds. Translates them to kg and 'stone'

def main():
    print("Welcome to the weight converter!")

    #saves name
    name1 = input("Name of person 1: ")

    #saves pounds of person
    pounds1 = int(input("Enter weight in pounds: "))
    
    #convert to stone
    stone1, stone2 = int(pounds1 / 14), int(pounds1 % 14)
    
    #convert to kg
    kg1 = pounds1/2.20462262185

    #print results
    print(name1, "weight is", stone1, "stone", stone2, "and", kg1, "kg")

    #Do the same for person 2
    name2 = input("Name of person 2: ")
    pounds2 = int(input("Enter weight in pounds: "))
    stone3, stone4 = int(pounds2 / 14), int(pounds2 % 14)
    kg2 = pounds2/2.20462262185
    print(name2, "weight is", stone3, "stone", stone4, "and", kg2, "kg")

    #Avg every value
    tpounds = (pounds1 + pounds2)/2
    tstone1, tstone2 = (int(stone1 + stone3)/2), int((stone2 + stone4)/2)
    tkg = (kg1 + kg2)/2
    print("Avg. weight in pounds:", tpounds)
    print("Avg. weight in stone:", tstone1, "stone", tstone2)
    print("Avg. weight in kg:", tkg)

    print("Thanks for playing!")

main()
    
