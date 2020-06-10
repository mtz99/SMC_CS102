## CS 102 Spring 2020
# Daniel Rascon, Kevin Eddy, Matthew Zhang, Oscar Lopez
#skipHW: a version of linear search in which we take big steps
#until we are close to our value, and then small steps until we find it. So we
#start at the beginning of the list, but we don’t go item by item. Instead we
#‘skip’ our way forward through the list, as long as the numbers we are seeing
#are too small. Once we find one one that is too big, then we step backwards
#linearly until we find our target

from random import randrange
import time

#Part A:
def skipSearch(mylist, target, skip):
    found = None
    current = 0
    stop = False
    while found == None: #more places to look and didn't find it
        #print(mylist[current])
        if target > mylist[len(mylist)-1] or target < mylist[0]: #If the target is greater or less than the edge numbers of the list.
            found = False
        if mylist[current] == target:    #when target is found/exists in the list
            found = True
        else:
            if stop == True and mylist[current] < target: #the current position is less than the target, so keep going until you can or cannot find target.
                found = False
            elif target < mylist[current]:    #the current position is greater than the target, so step down by 1 till you find the target
                current -= 1
                stop = True
            else: #keep skipping until you pass the range where the target should be.
                current += skip
    return found


#Part B:
# f(m) = (n / m) + (m-1)
#The n divided by m represents the amount of big skips which can be performed before the full skip amount cannot be added. Afterwards, the remaining amount
#which is less than the skip rate will be added to the (n/m) value to find the target.

#Part C:
#Find the derivative of f(m):
# f'(m) = -(n)/(m^2) + 1

#Solving for f'(m) = 0
# -(n)/(m^2) + 1 = 0
# 1 = (n/m^2)
# m^2 = n
# m = sqrt(n)

#Part D:
# f(sqrt(n)) = (n/sqrt(n)) + (sqrt(n) - 1)
# (2^2^n) - 1 (This is our O-notation equantion).


#Part E:
def randSort():
    # Starter sizes: Lists length 10. 
    size = 10
    maxx = 1000
    repetitions = 1000
    rounds = 12

    skip = 5 
    target = randrange(1, maxx)

    masterlist = []

    for i in range(size*10*rounds):
        masterlist.append(randrange(1, maxx))
    masterlist.sort()



    for i in range(rounds):
        #make a list to search through        
        mylist = masterlist[:size]

        #see how long 'repetitions' searches take       
        start = time.time()
        for j in range(repetitions):
            ans = target
            skipSearch(mylist, ans, skip)
        end = time.time()
        
        print("For size=", size, "this took", end-start)
        size = size*10
    

#randSort()

#Part F:
def leapSearch(mylist, target, leap, skip):
    # leap forward until too far
    print(mylist)
    print(target)

    for i in range(0, len(mylist), leap):
        print("leap", i)
        
        if target == mylist[i]: return True

        elif(target > mylist[len(mylist)-1] or target < mylist[0]):
            return False

        # skip backward until too far
        elif target < mylist[i]:
            max = i
            for j in range(i, -1, -skip):
                print("skip", j)
                if target == mylist[j]: return True
                
                # step forward until found (or not)
                elif target > mylist[j]:
                    for k in range(j, i, 1):
                        print("step", k)
                        if target == mylist[k]: return True
                    return False
                
            return False
                
    return False

#Part G:
def TleapSearch(mylist, target, leap, skip):
    # leap forward until too far
    print(mylist)
    print(target)

    for i in range(0, len(mylist), leap):
        print("leap", i)
        
        if target == mylist[i]: return True

        elif(target > mylist[len(mylist)-1] or target < mylist[0]):
            return False

        # skip backward until too far
        elif target < mylist[i]:
            Tskipsearch(mylist, target, skip, i)
                
    return False
def Tskipsearch(mylist, target, skip, i):
    for j in range(i, -1, -skip):
        print("skip", j)
        Tstep(mylist, target, i, j)    
    return False

def Tstep(mylist, target, i, j):
    if target == mylist[j]: return True
                
    # step forward until found (or not)
    elif target > mylist[j]:
        for k in range(j, i, 1):
            print("step", k)
        if target == mylist[k]: return True
    return False

#Main for testing purposes:
def main():
    mylist = []
    
    #make a list to search through        
    for i in range(0, 100, 3):
        mylist.append(i)

    #mylist = [1, 3, 4, 5, 8, 11, 19, 28, 33, 47, 51, 63, 66, 71, 78, 88, 89, 93, 95, 99]
    leap = 10
    skip = 5
    target = 64
    found = TleapSearch(mylist, target, leap, skip)
    print(found)



main()
