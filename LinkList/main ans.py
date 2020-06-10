class Node:
    def __init__(self,initdata=""):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    
class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    
    def remove(self, item):
        if self.size > 0:   #can only remove from a list with items
            if self.head.getData() == item: #if is in the first Node
                self.head = self.head.getNext()
            else:   
                current = self.head  #where we are looking. The person we are looking at
                previous = self.tail    #the 'person' just behind them

                #use same finder-method as .search(), but also update 'previous'
                while current.getData() != item and self.tail() != None:
                    previous = current
                    current = current.getNext()

                if current.getData() == item:
                    previous.setNext( current.getNext() )  

    def pop(self):
        if self == 0:   #could do self.head == None
            return None
        if self == 1:
            item = self.head.getData()
            self.head = None
            return item
        
        previous = self.tail     #like remove, we need know who is behind us
        current = self.head
    
        for current < previous:   #work our way to the end
            previous = current
            current = current.getNext()
        #current is now 'tail', and previous is 2nd-to-last (and will be new last)
            
        item = current.getData()    #save last 'data' 
        previous.setNext( None)   #make previous the new end = new tail
        return item

def main():
    n = Node("two")
    print("n's data = ", n.getData())
    print("n's pointer =", n.getNext() )
    input()

    nl = LinkList()
    print(nl)

    nl.remove(13)
    print("removed the 13 (old head)")
    print(nl)
    input()

    nl.remove(7)
    print("removed the 7")
    print(nl)
    input()

    nl.remove(22)
    print("removed the first 22")
    print(nl)
    input()

    nl.pop()
    print("popped off the end")
    print(nl)
    input()

    nl.append(1)
    print("appended a 1")
    print(nl)

    nl.reverse()
    print("reversed list")
    print(nl)
main()
