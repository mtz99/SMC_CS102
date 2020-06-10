'''2) Write a short program that requests an integer and prints the dictionary whose keys are the
integers less equal that integer, and the associated values are the cubes of those integers.
e.g. for input 7 it would print
{1:1, 2:8, 3:27, 4:64, 5:125, 6:216}
(remember that order of the pairs doesn't matter, so
{1:1, 2:8, 3:27, 4:64, 5:125, 6:216} = {2:8, 3:27, 1:1, 4:64, 5:125, 6:216}'''
def dict1():
    sample = {}
    limit = int(input("Please enter an int: "))
    for i in range(limit):
        sample[i] = i*i*i
    print(sample)


'''3) Write a short program that takes two given dictionaries d1 and d2 and produces a third
dictionary as follows.
a) The value in d3 associated to a key is the sum of the values that is associated to key in d1 &
d2. (count the value as 0 if that key doesn't appear).
Example:
d1 = {'A': 10, 'B': 30, 'F':9}
d2 = {'A': 9, 'C': 50, 'F':1}
d3 = {'A': 19, 'C': 50, 'F':10, 'B':30}
b) The (key,value) pair appears in d3 only when key appears in exactly one of d1 & d2.
Example:
d1 = {'A': 10, 'B': 30, 'F':9}
d2 = {'A': 9, 'C': 50, 'F':1}
d3 = {'C': 50, 'B':30}'''
def dict3a():
    d1 = {'A': 10, 'B': 30, 'F':9}
    d2 = {'A': 9, 'C': 50, 'F':1}
    d3 = {}
    for i in d1.keys():
        d3[i] = d1[i]
    for i in d2.keys():
        if(i in d1.keys()):
            d3[i] += d2[i]
        else:    
            d3[i] = d2[i]
    print(d3)

def dict3b():
    d1 = {'A': 10, 'B': 30, 'F':9}
    d2 = {'A': 9, 'C': 50, 'F':1}
    d3 = {}
    for i in d1.keys():
        d3[i] = d1[i]
    for i in d2.keys():
        if(i in d1.keys()):
            d3.pop(i)
        else:
            d3[i] = d2[i]
            
    print(d3)


'''4) Write a short program that asks the user for a string of letters, and produces the dictionary
that consists of (key, value) pairs where the keys are the lower case versions of the letters in the
string, and the value is the ASCII value of that letter. (Look up ord() and chr() ).'''
def dict4():
    words = {}
    add = str(input("Please enter a string of letters: "))
    add = add.lower()
    for i in add:
        words[i] = ord(i)
    print(words)
    


'''5a) Write a short program that asks the user for a string, and produces the dictionary that
consists of (key, value) pairs where the keys are the lower case versions of the letters in the
string, and the value is the number of times that letter appears in the string.
Hint: Read through the string once, making the values of each of the letters 0, then read through
the string again, doing +=1 to each letter.
b) Revise your program to read through the string exactly once. Hint: the associated value is 1 if
the key=letter is not yet in the dictionary, and get +=1 if it is already in the dictionary.'''

def dict5a():
    words = {}
    add = str(input("Please enter a string of letters: "))
    add = add.lower()   
    for i in add:
        words[i] = 0
    for i in add:
        words[i] += 1
    print(words)

def dict5b():
    words = {}
    add = str(input("Please enter a string of letters: "))
    add = add.lower()   
    for i in add:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    print(words)

def test():
    numlist = []
    for i in range(99):
        numlist.append(i * i)
    print(numlist)

test()