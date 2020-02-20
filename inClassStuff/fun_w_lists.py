## CS 102 Spring 2020
## Fun with Functions

# GOAL: Build out most of these functions, which includes both their code
#  and the full function comments.

## It is not necessarily clear which of the functions work for which of
## strings, tuples and lists. Some maybe for all, some maybe only for
## one or two. Figuring out which, and the clearly indicating this, is
## part of the work. 

import random

## make_list function
##     makes a list of integers
## INPUT: size = the desired length of the list
##        limit = integers will be in range [1, limit]
## PRINTS: nothing
## RETURNS: a list of length 'size' containing integers chosen
##        randomly in the range [1, limit]
def make_list(size, limit):
    mylist=[]
    for i in range(size):
        mylist.append(random.randint(1, limit+1))
    return mylist

## make_list_alpha function
##     makes a list of lower case letters
## INPUT: size = the desired length of the list
## PRINTS: nothing
## RETURNS: a list of length 'size' containing lower case letters
##        that is, chosen randomly from 'a' to 'z'
def make_alpha_list(size):
    mylist = []
    for i in range(size):
        num = random.randint(1, 100)%26
        char = chr(97+num)
        mylist.append(char)
    return mylist

#INPUT: thelist = A list of integers
#PRINTS: nothing
#RETURN: the sum of the numbers in the list
# takes a collection of objects and returns the sum of
# the objects in that collection
def summer(thelist):
    total = 0   #ACCUMULATION LOOP
    for i in range(len(thelist)):
        total += thelist[i]
    return total

# takes a linear collection of objects and returns the product
# the objects in that collection
def producter(thelist):
    total = 0
    for i in range(len(thelist)):
        total * thelist[i]
    return total

# takes a linear collection of objects and returns the largest of
# the objects in that collection
# Do with a loop, not with 'max' function

def maxxy(thelist):
    largest = 0
    for i in range(len(thelist)):
        if(thelist[i] > thelist[i-1]):
            largest = thelist[i]
    return largest
# takes a linear collection of objects and returns the 2nd largest of
# the objects in that collection
# Do with a loop, not with 'max' function
def second_max(thelist):
    secondL = 0
    largest = maxxy(thelist)
    thelist[largest].remove()
    for i in range(len(thelist)):
        if(thelist[i] > thelist[i-1]):
            secondL = thelist[i]
    return secondL
        

# takes a linear collection of o and removes from it all the even
# numbers in the collection
def remove_evens(thelist):
    for i in range(len(thelist)):
        if(i % 2 == 0):
            thelist.remove(thelist[i])
    return thelist

# takes a linear collection of objects and integer and returns a new 
# collection composed of all elements of the original collection that
# at least as large as the given object
def large():
    pass

# takes a linear collection of objects, and one object, and prints the number
# times that object occurs in the collection 
# do via a loop, not with the count function    
def counter():
    pass

# takes a linear collection of objects modifies it so that the first
# and last elements have been swapped. So 1-3-5-7 becomes 7-3-5-1
def swapper():
    pass

# takes a linear collection of objects and two other objects obj1 and obj2
# replaces all the obj1 by obj2 (if any) and then prints the result
# do via a loop
def exchanger():
    pass
    
def main():
    ###### START OF CODE ##############
    size = 11    # length of the lists we are dealing with
    height  = 12     # our numbers will be in the range [1,height]
    list1  = make_list(size, height)
    list2 = make_alpha_list(size)
    print(list1)
    print(list2)
    input() #is like a 'pause'

    #### SUMMER   
    summer(list1)
    print("hi")
    print("The sum of the elements of", list1, "is", summer(list1) )
    print("lo")
    ans = summer(list1)   
    print(ans)


#   productor()
#   maxxy()
#   second_max()
#   remove_evens()
#   large()
#   counter()
#   swapper()
#   exchanger()


main()
