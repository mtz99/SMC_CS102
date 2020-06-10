#CS 102 Spring 2020
# Dictionary code & main for HW
# Adapted from the text 

'''CS 102 Dictionary Methods
Python Dictionaries have a number of methods that we did not implement in our code. Below we
write methods that do some (and mimic others).
Note: This is meant to be a pretty straightforward review of lists (hidden inside work on
dictionaries). There should be <50 lines of code total in your functions.

1) Write .haskey() and hasvalues() methods
('in' is a keyword in Python, so we don't try to rewrite it, but mimic its purpose)
Given a dictionary 'mydict' and a key 'akey', if akey is a key in mydict, then "mydict.haskey(akey)"
will return True, otherwise will return False.
Given a dictionary 'mydict' and a key 'avalue', if avalue is a value in mydict, then
"mydict.hasvalue(avalue)" will return True, otherwise will return False.
Note: This can be done multiple ways. One way is to iterate through the list(s) underlying our
Dictionary class. Do this. Another way is to use the list method 'in'. Do this also.'''


'''2) Write a .pop() method.
Given a dictionary 'mydict' and a key 'akey':
If akey is a key in mydict, then "mydict.pop(akey)" will cause the associated value to be removed.
If akey is not a key, nothing occurs.
Note: This can be done multiple ways. One way is to iterate through the list(s) underlying our
Dictionary class. Do this. Another way is to use the list method 'index'. Do this also. Finally, the
list method .pop() is not useful here - why?'''

'''3) Write a len() method.
First write it as "def len(self):" which you can test as "mydict.len()"
Then convert it to a magic method - "def __len__(self):" allowing us
to do "len(mydict)"'''

'''4) Write a .setdefault() method
Given a dictionary 'mydict' and a key/value pair 'akey:avalue'
"mydict.setdefault(key, value)" will do the following
a) if akey is in mydict, the current associated value is returned
b) if akey not in mydict, then the pair 'akey:avalue' is added to mydict.'''


'''5) Write an .update() method
Given two dictionaries 'dict1' and 'dict2', "dict1.update(dict2)" will add all the key:value pairs of
dict2 into dict1, except that it will not overwrite any existing pairs. That is, if key2:value2 is in
dict2,
a) if key2 is not in dict1, then key2:value2 added to dict1
b) if key2 is in dict1, then nothing happens '''


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
        return key*key%size
    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def put(self,key,data):

        if not None in self.slots and not key in self.slots:
            print("Table is Full! Cannot add to it")
            return None
        
        slot = self.hashfunction(key,self.size)

        while self.slots[slot] != None and self.slots[slot] != key: #bad luck
            slot = self.rehash(slot,len(self.slots))

        if self.slots[slot] == None:  #Did find an empty slot!
            self.slots[slot] = key   #store key
            self.data[slot] = data    #store data

            self.data[slot] = data     # update the data


    def get(self,key):
        if not None in self.slots and not key in self.slots:
            print("Looked for", key,"but not present and table full")
            return None
        
        slot = self.hashfunction(key,self.size)
        while self.slots[slot] != None and self.slots[slot]!= key:
            slot=self.rehash(slot,len(self.slots))

        if self.slots[slot] == None:
            return None     #Did not find our key, so there is no data for it
        elif self.slots[slot] == key:   
            return self.data[slot]   #Did find our key! return its data

    def __getitem__(self,key):   # to use []
        return self.get(key)

    def __setitem__(self,key,data): # to use []
        self.put(key,data)

###############################
    def len(self):
        count = 0
        for i in range(self):
            count += 1
        return count
    def __len__(self):
        count = 0
        for i in range(self):
            count += 1
        return count
    def pop(self, mydict, akey):
        for i in mydict.keys():
            if mydict[i] == akey:
                mydict
            else:
                return False
    def haskey(self, mydict, akey):
        for i in mydict.keys():
            if mydict[i] == akey:
                return True
            else:
                return False
    def hasvalue(self, mydict, avalue):
        for i in mydict.values():
            if (mydict[i] == avalue):
                return True
            else:
                return False
    def setdefault(self, mydict, akey):
        pass
    def update(self, dict1, dict2):
        pass


def main():
    animals = Dictionary()
    animals[93]="lion"
    animals[44]="goat"
    animals[20]="chicken"
    print("lion?", animals[93])
    print("frog?", animals[32])
    animals[32] = "toad"
    print("new frog?", animals[32])
    input()
    
    animals[42]= "sloth"
    animals[17]="tiger"
    print(len(animals), "animals: ", animals.values())
    print("tigers too scary")
    animals.pop(17)
    print(len(animals), "animals: ", animals.values())
    print(len(animals), "keys: ", animals.keys())
    input()
    
    animals[32]="cow"
    animals.setdefault(40, "robin")
    print(len(animals), "animals: ", animals.values())
    input()
    
    print(animals.setdefault(40, "blue jay"))
    print(len(animals), "animals (no blue jay):", animals.values())
    input()

    print("dog is no:", animals.hasvalue("dog"))
    print("lion is yes:", animals.hasvalue("lion"))
    print("93 is yes:", animals.haskey(93))
    print("94 is no:", animals.haskey(94))

    animals[44]="pig"  #change goats into pigs
    print(animals.values())
    input()

    pets = Dictionary()
    pets[20] = "cat"
    pets[26] = "dog"
    pets[77] = "bird"
    print("pets are:", pets.values())
    input()
    print("Before animals are:", animals.values())
    animals.update(pets)
    print("After animals are:", animals.values())

main()
