# CS 102 Spring 2020
# timing binary search of ordered lists

from random import randrange
import time

#Book's solution
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1   #item should be in positions 0 <= pos <= last
    found = False
    while first<=last and not found: #more places to look and didn't find it
        midpoint = (first + last)//2   # middle position

        if alist[midpoint] == item:    #win!
            found = True
        else:
            if item < alist[midpoint]:    #that positions number was "too big"
                last = midpoint-1 
            else:                        #that position's number was too small
                first = midpoint+1
    return found


def main():
    # Starter sizes: Lists length 10. 
    size = 10
    maxx = 10**6
    repetitions = 1000
    rounds = 12

    masterlist = []

    for i in range(size*10*rounds):
        masterlist.append(randrange(1, maxx))
    masterlist.sort()

    print("Masterlist:", masterlist)


    for i in range(rounds):
        #make a list to search through        
        mylist = masterlist[:size]

        #see how long 'repetitions' searches take       
        start = time.time()
        for j in range(repetitions): 
            ans = randrange(1, maxx)
            binarySearch(mylist, ans)
        end = time.time()
        
        print("For size=", size, "this took", end-start)
        size = size*10
main()

    
    







        
