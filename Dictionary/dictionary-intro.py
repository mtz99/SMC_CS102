#CS 102
#Concrete introduction to Dictionaries

# Dictionaries consist of pairs = two objects.
# The first is called the "key", and must be immutable,
# The second is the "value" and can be anything. 
#
# d = {key1:value1, key2:value2, key3:value3}  {}
# Notice the colon to connect the key/value pairs,
# and the comma to separate pairs from each other.



def main():
## Example: a simple English to French color dictionary
    etf = {}   #empty dictionary. Use {} for dictionaries, [] for lists, () for tuples.
    etf = dict() # same
    
    etf['red'] = 'rouge'    #add the pair 'red':'rouge' to the dictionary

    etf['green'] = 'veurt'  #add a third pair. Oops!! Typo!
    etf['green'] = 'vert'   #update pair to "green":"vert"
    etf['blue'] = 'bleu'
    print(etf)
    input()


#How to access? by 'indexing' like lists
    print("red is ", etf['red']) 
    len(etf)
    print("keys = ", etf.keys())   #print keys directly?? 
    print("values = ", etf.values())
    print("items = pairs = ", etf.items()) 
    input()

###  Can also create dictionaries by { pairs } 
    other = {'brown':'marron', 'black':'noir', 'white':'blanc', 'pink':'rose'}

### Then can add all of 'others' pairs into etf
    etf.update(other)
#adds all the pairs from numbers into etf, except that it won't over write any pairs whose key exists in etf
    print("updated dictionary: ", etf)
    input()

#Can also access and save any of this information, if we want to use it from some reason. 
    r = etf['red']  
    list_of_keys = list(etf.keys())
    list_of_values = list(etf.values()) 
    print("saved value of eft[red] = ", r)
    print("list of keys = ", list_of_keys)
    print(type(etf.keys()))
    print("list of values = ", list_of_values)
    print(type(etf.values() ) )
    input()

# Dictionaries are mutable, and can easily add and delete
    del etf['green']     # removes pair, forgetting it entirely
    r_word = etf.pop('red')  # deletes (key,value) from eft saves the value 
    print('revised dictionary = ', etf)
    input()

## Common operations with dictionaries    
    print("Black is in our dictionary:", 'black' in etf)
    print("Orange is in our dictionary:", 'orange' in etf)
    print(etf.get('pink'))
    print(etf.get('grey'))
    # doing  >>> etf['grey'] would lead to an error, since 'grey' is not a key
    input()

## can do loops!    
    for w in etf:  # print all values
       print(etf[w]) 
#    or
    for v in etf.values():
       print(v)
    input()

## How to copy and delete dictionaries

#Dictionaries are mutable (like lists). So need to be careful when assigning. 
    eng_to_french = etf   #now have two names for the same data structure.
    #just like mylist2 = mylist does
    
    #If want a seperate copy of lists to mylist2 = mylist[:]. For dictionaries
    eng_to_french = etf.copy() #or 
    eng_to_french = dict( etf )
    
    etf.clear()  #Empty the dictionary (but it still exists)
    print("eft after clear() = ", etf)
    input()
    
    del eng_to_french   #Make the dictionary go away completely 
    print(eng_to_french)  # will lead to error

main()

"""
of course there are other methods.
One not mentioned above is
>>> setdefault(key, value1)
Doing
a = mydictionary.setdefault(key, value1)
       is the same as
if key in mydictionary:
    a = mydictionary[key]
else
    mydictionary[key] = value1
    a = value1
#ie
if not key in mydictionary:
    mydictionary[key] = value1
a = d[key]
"""













