#Matthew Zhang
#CS 102 Spring 2020
#March 24th
#Program: remove
#a function that has a stack and an item as parameters, 
#and removes one copy of 'target' from a stack, returning 
#the possibly revised stack that has the other entries still in order.

from stackprint import Stack

## remove goes here
def remove(st, target):
    t = Stack()
    x = 0
    y = 0
    while(st.size() != 0 and x != target):
        x = st.peek()
        st.pop()
        t.push(x)
    while(t.size() != 0):
        y = t.peek()
        t.pop()
        if(y == target):
            continue
        else:
            st.push(y)
    return st


def main():
    letters = "ABCDEFG"
    st = Stack()
    for c in letters:
        st.push(c)

    first = "D"
    st = remove(st, first)   #now st should be [ABCEFG)
    print("after first", st)  #cheating a bit - the stack is a list so we print it

    second = "H"
    st = remove(st, second)  #st should still be [ABCEFG)
    print("after second", st)

    third = "A"
    st = remove(st, third)
    print("after third", st)
main()
