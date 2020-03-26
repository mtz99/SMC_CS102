#Matthew Zhang
#CS 102 Spring 2020
#March 24th
#Program: under
#A function that puts the elements of some stack r 'under' 
#those in another stack s. So if r=[2 3 4 5) and s=[7 8 9) 
#at the start, then r=[2 3 4 5) and s=[2 3 4 5 7 8 9) at the end.

from stackprint import Stack


## under goes here
def under(st2, st1):
    x = 0
    y = 0
    z = 0
    z2 = 0
    t = Stack()
    t2 = Stack()
    while(st1.size() != 0):
        x = st1.peek()
        st1.pop()
        t.push(x)
    while(st2.size() != 0):
        y = st2.peek()
        st2.pop()
        t2.push(y)
    while(t2.size() != 0):
        z = t2.peek()
        t2.pop()
        st1.push(z)
        st2.push(z)
    while(t.size() != 0):
        z2 = t.peek()
        t.pop()
        st1.push(z2)
    #I added these print statements as the first stack is not displaying properly.
    print(st1)
    print(st2)
    return(st2, st1)


   
def main():
    letters = "ABCDEFG"
    st1 = Stack()
    for c in letters:
        st1.push(c)

    moreletters = "RSTUVW"
    st2 = Stack()
    for c in moreletters:
        st2.push(c)

    st1 = under(st2, st1)
    print(st1, " =RSTUVWABCDEFG")

    print(st2, " = RSTUVW")


main()
