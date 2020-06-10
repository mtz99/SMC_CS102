
#CS 102 Spring 2020
# Binary search through ordered list

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
            if item < alist[midpoint]:    #that positions entry was "too big"
                last = midpoint-1 
            else:                        #that position's entry was too small
                first = midpoint+1

    return found


#Jim's version. Same idea, but return True when/if found, and return False if never found. 
def binarySearchJim(alist, item):
    first = 0
    last = len(alist)-1   #item should be in positions first <= pos <= last

    while first<=last: 
        midpoint = (first + last)//2.   # middle position
        if alist[midpoint] == item:    #win!
            return True
        elif item < alist[midpoint]:    #alist[midpoint] was "too big"
            last = midpoint-1        #look in first <= pos <= midpoint-1
        else:                        #alist[midpoint]  "too small"
            first = midpoint+1        #look in midpoint+1 <= pos <= last

    return False



#Recursive version
def recBinarySearch(alist, item):
    if len(alist) == 0: #when list is empty, :(
        return False
    elif len(alist) == 1:
        return alist[1] == item  #when list is one entry, test 
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:    #found it!
            return True
        elif item < alist[midpoint]:    #alist[midpoint] was "too big"
            return recBinarySearch( alist[:midpoint], item)
        else:                        #alist[midpoint]  "too small"
            return recBinarySearch(alist[midpoint+1:], item)


def main():
    