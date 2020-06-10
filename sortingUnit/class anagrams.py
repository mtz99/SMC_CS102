# CS 102 Spring 2020
# Code based on Chapter 3 from text
import time
import random
from math import sqrt

## BOOKS Method 1.
## Use 'stillOK' as boolean to mean "T/F: They appear equal so far"
## Go through string1 letter by letter, see if each is in string2.
## If the letter is not, then stillOK becomes False
## If the letter is in string2, then mark it as 'used', and go onto next letter in string1.
## If get to end of string1, then all matched
def anagramSolution1(string1,string2):

    if len(string1) != len(string2):
        return False
 
    alist = list(string2)  #turn string2 into list, to make 'used' marks easier
    pos1 = 0   #index of string1
    stillOK = True
    
    while pos1 < len(string1) and stillOK:
        pos2 = 0  #start at front of string2
        found = False # did we find this letter in string2?
        while pos2 < len(alist) and not found: #go through string2
            if string1[pos1] == alist[pos2]:
                found = True  #found it!
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None #found it, so mark it as used
        else:
            stillOK = False  #didn't find it. string1 != string2  

        pos1 = pos1 + 1

    return stillOK




## BOOKS Method 2
## Turn each string into a list of letters
## Sort each list of letters
## Then compare entry-by-entry. If ever not equal we know the answer is False. 

def anagramSolution2(string1,string2):
    if len(string1) != len(string2):
        return False

    #turn the strings into lists, then sort in alphabetic order
    alist1 = list(string1)
    alist2 = list(string2)
    alist1.sort()
    alist2.sort()

    ## march through the lists
    pos = 0 # index of strings
    matches = True  #do they match so far? 

    while pos < len(string1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


# METHOD 3 - list all anagrams, way too long








## BOOK code for solution 4
## Count how many times each letter appears in each string
## If these counts are identical then the strings are anagrams
## If they are not, they are not

def anagramSolution4(string1,string2):
    if len(string1) != len(string2):
        return False
    stillOK = True

    # lists to hold the counts
    count1 = [0]*26
    count2 = [0]*26

    ## Go through string1 & string2 and count how many of each letter
    for i in range(len(string1)):
        pos = ord(string1[i])-ord('a')
        count1[pos] += 1

    for i in range(len(string2)):
        pos = ord(string2[i])-ord('a')
        count2[pos] += 1

    ## Testing is here. Go through counts to see if they are equal.
    j = 0
    while j<26 and stillOK:
        if count1[j] == count2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK










## random_strings function
##      Makes two strings that are anagrams.
##      
## INPUT: n = length of the output strings. Positive integer
## PRINTS: nothing
## RETURNS: two strings
def random_strings(n):
    mystring = ""
    for i in range(n):
        mystring += chr(97 + random.randint(0,25) )

    newstring = list(mystring)
    random.shuffle(newstring)
    mystring2 = "".join(newstring)
        
    return mystring, mystring2
                        
## anagram_list
##      makes m pairs of anagrams each consisting of n letters
## INPUT: m = how many pairs we wish
## PRINT: nothing
## RETURNS: the paris of anagrams
def anagram_list(m, n):
    mylist = []
    for j in range(m):
        mylist.append(random_strings(n) )
    return mylist
    







def main():
    #Change these at will.
    # 3, 2, 8
    length = 2 ## how long the strings are
    growth = 10  ##how quickly they grow in length
    top = 6 ## len * (gr^top) is max
    howmany = 1000 ## how many in a comparison
    
    for i in range(1,top+1):
        print("\nLength is", length)
        myanagrams = anagram_list(howmany, length) 
        print("Done making anagrams")
        
##        start = time.time()
##        for (string1, string2) in myanagrams: 
##            anagramSolution1(string1, string2)
##        end = time.time()
##        print ("Method 1: " ,end-start)

        start = time.time()
        for (string1, string2) in myanagrams: 
            anagramSolution2(string1, string2)
        end = time.time()
        print ("Method 2: ", end-start)

        start = time.time()
        for (string1, string2) in myanagrams: 
            anagramSolution4(string1, string2)
        end = time.time()
        print ("Method 4: ", end-start)
        
        
        length *= growth

main()
    


## SOLUTION #1 Jim
## Same idea as Solution 1, but Jim doesn't like floating booleans
## Instead, if/when we find evidence that string1!=string2 we should immediate
## return False
    
def anagramSolution1Jim(string1, string2):
    if len(string1) != len(string2):
        return False

    alist = list(string2) 
    pos1 = 0

    while pos1 < len(string1) : #go through string1
        pos2 = 0    #go through string2

        #continue through string2 as long as didn't get to end of string2
        # and didnt find a match
        while pos2 < len(alist) and string1[pos1] != alist[pos2]:
                pos2 = pos2 + 1

        ## case that did find a match. Then mark as 'used'
        if string1[pos1] == alist[pos2]:
            alist[pos2] = None
        ## case that didn't find a match. NOT THE SAME, so return False
        else:
            return False

        ##go onto next spot in string1
        pos1 += 1

    return True




## Jim's version of solution 2
## Make 2 changes. (1) Return False as soon as find a mis-match
## Do as for loop
def anagramSolution2Jim(string1, string2):
    if len(string1) != len(string2):
        return False

    #turn the strings into lists, then sort in alphabetic order
    alist1 = list(string1)
    alist2 = list(string2)
    alist1.sort()
    alist2.sort()

    for pos in range(len(string1)):
        if alist1[pos] != alist2[pos]:
            return False
    return True   #if didn't find difference, then equal    



## JIM's #3 via
# RECURSION
#think of "abc" as the big case. The smaller case is "bc". 
#Its rearrangements are bc and cb. 
#Notice the more general case has Abc, bAc, and bcA. And Acb, cAb and cbA. 
#Hmmm.   pluck off first letter --a 
#make all the anagrams of the rest -- bc, cb <--- reduction
#put first letter into all spots -- Abc, bAc, bcA and Acb, cAb, cbA <--- combining

#Rewrite
#  ans = []//save our answers
#  x = mystring[0]
#  for word in anagram(mystring[1:]):
#      for i in range(0: len(word)-1):
#            insert x into the i'th spot of word
#            newword = word[:i] + x + word[i:]

#mystring is a string
#anagram returns the list consisting of all possible arrangements of the letters in mysting
def anagrams_r(mystring):
    if mystring == "":
        return [mystring]
    else: 
        ans = []
        for word in anagrams_r( mystring[1:] ): 
            for i in range( len(word) + 1 ):
                ans.append( word[:i] + mystring[0] + word[i:] )
    return ans


## Jim's version of method 4
## Setup is the same.
## Use for loop to compare the counting lists
def anagramSolution4Jim(string1,string2):
    if len(string1) != len(string2):
        return False

    # lists to hold the counts
    count1 = [0]*26
    count2 = [0]*26

    ## Go through string1 & string2 and count how many of each letter
    for i in range(len(string1)):
        pos = ord(string1[i])-ord('a')
        count1[pos] += 1
    for i in range(len(string2)):
        pos = ord(string2[i])-ord('a')
        count2[pos] += 1

    ## Compare count1 & count2. If they are ever equal, answer is False
    for j in range(26):
        if count1[j] != count2[j]:
            return False
    return True  #if made it to the end, answer is True

