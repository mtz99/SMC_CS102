##Sums of sum program Solution
##CS 102 Spring 2020
##Main supplied by Sauerberg

## SUBSET
# can target be build with a subset of myset??
#### INPUTS
# myset = set of numbers can use to build target with
# target = target number
# ans = solution set
## OUTPUT
# returns True = target can be a sum of a subset of myset
# return False = target cannot be a sum of a subset of myset
## SIDE EFFECT
# lists are mutable. So if an element from myset is useful, add it total
# the list ans. This will (eventually) allow us to see how target is built
def subset(myset, target, ans):
    if(len(myset) == 0):
        return False
    elif(len(myset) == 1):
        if(myset[0] == 1):
            ans.append(myset[0])
            return True
        else:
            return False
    else:
        return(subset(myset[:-1], target - myset[-1], ans) + subset(myset[:-1], target, ans))

    
    
    
    '''if(len(myset) == 0):
        return False
    elif(target < myset[0]):
        return False
    elif(target in myset):
        ans.append(target)
        return True
    else:
        if(target >= myset[-1]):
            ans.append(myset[-1])
            if(subset(myset[:-1], target - myset[-1], ans)):
                return True
            else:
                for a in myset:
                    if(a in ans):
                        ans.remove(a)
                return subset(myset[:-1], target, ans)
            
        else:
            return subset(myset[:-1], target, ans)'''
            

## NSUBSET
# how many ways can target be built as a subset of myset??
## INPUTS
# myset = list of weights to use
# target = value trying to build using subsets of mylist
## RETURNS
# the number of ways.
def nsubset(myset, target):
    if(len(myset) == 0):
        return 0
    if(len(myset) == 1):
        return 1
    else:
        return (nsubset(myset[:-1], target - myset[-1]) + nsubset(myset[:-1], target)) #Find ways to use the last number and find ways NOT to use the last number
        

'''def nsubset(myset, target):
    ans = []
    anscheck = []
    totaln = 0
    if(len(myset) == 0):
        return 0
    elif(target < myset[0]):
        return 0
    if(subset(myset, target, ans)):
        anscheck.append(ans)
        totaln += 1
    anscopy = ans[:]
    for i in anscopy:
        ans = []
        myset.remove(i)   
        if(subset(myset, target, ans)):
            if not ans in anscheck:
                printer(ans, target)
                anscheck.append(ans) 
                totaln += 1
            anscopy.remove(i)
            for a in anscopy:
                ans = []
                myset.remove(a)
                if(subset(myset, target, ans)):
                    if not ans in anscheck:
                        anscheck.append(ans)
                        printer(ans, target)
                        totaln += 1
                myset.append(a)
                myset.sort()
                for b in ans:
                    if not b in anscopy:
                        anscopy.append(b)
            anscopy.append(i)
       
        myset.append(i)
        myset.sort()
        for a in ans:
            if not a in anscopy:
                anscopy.append(a)
    return totaln'''


## MISSING
# function producing 'first weight that can't be weighed'
## Input: myset = list of weights
def missing(myset):
    target = 1
    ans = []
    for i in myset:
        if not -i in myset:
            myset.insert(0,-i)
    myset.sort()
    while subset(myset,target,ans):
        printer(ans,target)
        ans = []
        target += 1
    return target

    
    for i in range (0, n ): 
        if arr[i] <= res: 
            res = res + arr[i] 
        else: 
            break
    return res 


#Printer
#nicely prints a list.
# [3,5,7] --> "3 + 5 + 7"
def printer(ans, target):
    for i in ans[:-1]:
        print(i, "+", end=" ")
    print(ans[-1], "=", target)


def test():
    ans = []
    myset = [1,2,3,4,5,6,7]
    subset(myset, 10, ans)
    print(ans)

from random import randrange
def main():
    print("Fun with weights! Give me the size of the set. (probably <=10)")
    size = int(input("How large is our set? "))
    #s = set of positive integers
    s = []
    #maxx is the largest integer possible in our set
    maxx = 100

    #now create a list of size-many integers from 1 to maxx
    #Use a for loop with a test to the entries are unique
    #sort it at end, for pretty
    while len(s)<size: 
        newint = randrange(1, maxx)
        if not newint in s:
            s.append(newint)
    s.sort()

    #target1 = use about half of the elements of s
    target = randrange(size*maxx)//4 #REACTIVATE WHEN DONE
    #target = 10
    ans = [] #the answer set
    print("The set s is", s)
    ssum = subset(s, target, ans)
    if ssum: 
        answer = "possible"
    else:
        answer = "impossible"
    print("It is", answer, "to make", target, "as a subset sum of s.")
    
    if ssum:
        printer(ans, target)
    print("The integer", target, "is possible in", nsubset(s, target), "ways.")

    print("The smallest weight not measurable with s is", missing(s))
main()
#test()


    


