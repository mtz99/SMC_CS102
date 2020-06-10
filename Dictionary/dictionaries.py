#CS 102 Spring 2020
# Dictionary code
# Adapted from the text 


class Dictionary:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def keys(self):
        thekeys = []
        for x in self.slots:
            if x != None:
                thekeys.append(x)
        return thekeys

    def values(self):
        thevalues = []
        for x in self.data:
            if x != None:
                thevalues.append(x)
        return thevalues

    def items(self):
        theitems = []
        for i in range(self.size):
            if self.slots[i] != None:
                theitems.append( (self.slots[i], self.data[i] ) )
        return theitems

    def hashfunction(self,key,size):
        return key%size
    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def put(self,key,data):
        # Either 'key' is not yet in our dictionary or it is.
        # How to tell? Look through the hashtable starting at 'slot'
        # Eventually will either find 'key' or will find None
        # If find 'key' first (so "yes"), then update self.data[] with given data
        # If find None first (so "no"), then put given data in self.data[]
        
        # Minor worry -- what if the table is full? If we had two more days, we'd
        # take care of this. For today, to prevent infinite loops, we 'cheat' by
        # using slow methods
        if not None in self.slots and not key in self.slots:
            print("Table is Full! Cannot add to it")
            return None
        
        slot = self.hashfunction(key,self.size)
        # hope that most of the either slots[slot] is open (= None) or contains 'key'
        # Test to see if we are unlucky. If so, start linear probing. 
        while self.slots[slot] != None and self.slots[slot] != key: #bad luck
            slot = self.rehash(slot,len(self.slots))

        if self.slots[slot] == None:  #Did find an empty slot!
            self.slots[slot] = key   #store key
            self.data[slot] = data    #store data
        else: # self.slots[slot] == key:  #OR found where our key is stored
            self.data[slot] = data     # update the data


    def get(self,key):
        # Similar to put. Either 'key' is in self.slots or not
        # Search for it. Either will find it, and then can return its data
        # Or will instead find a None, in which case return None
        
        # Again Minor worry - if our table is full, the tests just explained fail
        # take care of this kinda ugly slow way today
        if not None in self.slots and not key in self.slots:
            print("Looked for", key,"but not present and table full")
            return None
        
        slot = self.hashfunction(key,self.size)
        while self.slots[slot] != None and self.slots[slot]!= key:
            slot=self.rehash(slot,len(self.slots))
        # loop very similar to put. Probably should combine into one auxiliary function
        # Again, should worry about full table that doesn't have our key, but won't 

        if self.slots[slot] == None:
            return None     #Did not find our key, so there is no data for it
        elif self.slots[slot] == key:   
            return self.data[slot]   #Did find our key! return its data

    def __getitem__(self,key):   # to use []
        return self.get(key)

    def __setitem__(self,key,data): # to use []
        self.put(key,data)



def main():
    animals = Dictionary()
    animals[54]="cat"
    animals[26]="dog"
    animals[93]="lion"
    animals[17]="tiger"
    animals[77]="bird"
    animals[31]="cow"
    animals[44]="goat"
    animals[55]="pig"
    animals[20]="chicken"
    animals[32] ="frog"
    animals[42]= "sloth"
    print("lion?", animals[93] )
    print("frog?", animals[32])
    animals[32] = "toad"
    print("new frog?", animals[32])
    print(animals.keys() )
    print(animals.values() )
    print(animals.items() )
    animals[50] = "human"
    a = animals[50]
main()
