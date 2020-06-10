#Matthew Zhang
#CS 102 Spring 2020
#March 31st
#Program: Cdeques
#This program lets the user runs cdeques in which the cdeque will march forth the letters, march them back,
#and remove them at the end.

#Note: I could not find out how to prevent the infinite empty list from printing at the end, so once you see
#the infinite empty lists, stop the program immediately or you will not see the end results.


#### YOUR CDEQUE GOES HERE
class CDeque:

    def __init__ (self, maxsize = 10): #so a CQueue has 10 spots by default (so we can see them all)
        self.maxsize = maxsize
        self.items = [None]*maxsize #all the entrties start life as None = empty
        self.front = maxsize - 1 #point tot the 'right hand end' as the front of the cqueue
        self.rear = maxsize - 1
        self.size = 0 #Let's keep track ourselves

    def isEmpty(self):
        return self.size == 0
    

#So far so good! Now the 'circular' part.
#Eventually our front and/or rear pointer will become 0.
#i.e. be at the very front of our sotrage list. What to do when they back up?
#Then we wrap around so that the previous spot is [-1], i.e. maxsize - 1!
    def addRear(self, item): #Version last
        if self.size == self.maxsize:
            print("Queue is full! Item was not enqueued!")
        else:
            if not self.isEmpty():
                if self.rear == 0:
                    self.rear = self.maxsize - 1
                else:
                    self.rear -= 1
            self.items[self.rear] = item
            self.size += 1

    def addFront(self, item):
        if self.size == self.maxsize:
            print("Queue is full! Item was not enqueued!")
        else:
            if not self.isEmpty():
                if self.front == self.maxsize - 1:
                    self.front = 0
                else:
                    self.front += 1
            self.items[self.front] = item
            self.size += 1
    
    def removeFront(self):
        if self.isEmpty():
            print("Queue is empty! None was returned")
            return None
        else:
            val = self.items[self.front]
            self.items[self.front] = None
            if self.front != self.rear:
                if self.front == item:
                    self.front = self.size - 1  
                    
            return val
    
    def removeRear(self): #Version last
        if self.isEmpty():
            print("Queue is empty! None was returned")
            return None
        else:
            val = self.items[self.rear]
            self.items[self.rear] = None
            if self.rear != self.front:
                if self.rear == self.maxsize - 1:
                    self.rear = 0
                else:   
                    self.rear += 1
            self.size -= 1
            return val
    

    #### KEEP THIS
    def __str__(self):
    ## we don't print queues but to see how we did in our design
    ## this let's us see the queue. 
        temp = CDeque()
        stringy = "["
        for a in self.items:
            if a == None:
                stringy += "_"
            else:
                stringy += str(a)
        #return stringy+")" + " size =" + str(self.size) + ", f=" + str(self.front) +", r=" + str(self.rear)
        return stringy+")" 



def main():
    print("A main for testing your Circular Deque")
    print("It likely requires a couple changes from you in order for it to work.")
    print("1) You should have 'pointers' variabls telling you where the 'front' and 'rear' of your CDeque is")
    print("In the __str__ function above adjust the final return statement to use your variables.")
    print("2) Your CDeque should have a default size. For the code below to test it, that size should be 10")
    print()

    d = CDeque()

    print("Start by filling the CD")
    letters = "ABCDEFGHIJ"
    i=0    
    while i<10:
        d.addRear(letters[i])
        d.addFront(letters[i+1])
        i+=2
    print(d)

    print("\nTry another letter - should get error messages")
    d.addRear("Z")
    d.addFront("Z")

    print("\nMake some room")
    d.removeFront()
    d.removeRear()
    d.removeFront()
    d.removeRear()
    print(d)

    print("\nWalk the letters 'forward'")
    for i in range(5):
        d.addFront(d.removeRear())
        print(d)
    
    print("\nWalk the letters 'backward'")
    for i in range(5):
        d.addRear(d.removeFront())
        print(d)

    print("\nMake it go away")
    while not d.isEmpty(): 
        d.removeFront()
        print(d)
    print("Try final remove - should get error messages")
    d.removeRear()
    d.removeFront()
    

main()

    
