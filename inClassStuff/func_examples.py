#Spring 2020     #CS 102: Function Examples
#J Sauerberg

##### EXAMPLE 0: WarmUp ######
def f(a):
    return 2*a-1
def g(b):
    print( b + f(b) )
def main():
    print( f(4) )
    g(5) 
    
#### Example 1a: Illustrates data passing #######
def fxn1a(n):
    print(n+1)
def main1a():
    m = int(input("Number please: "))
    fxn1a(m)
    print("bye")

#### Example 1b :Illustrates data passing & return ######
def square(n):
    n *= n
    return n
def main1b():
    m = int(input("Number please: "))
    k = square(m)
    print("k = ", k)

##### EXAMPLE 2: Illustrates scope. ##############
def fxn2(n):
    m=2
    print("Inside fxn n=", n, ", m=", m, " and k=", k)
def main2():
    n = 16
    m = "baseball"
    k = 3.14
    fxn2(n)
    print("Outside n=", n, ", m=", m, ", k=", k)
    
###### EXAMPLE 3: naming #####
def fxn3(a,b):
    a += 1
    b = b*a
    print(b)
def main3():
    A = 3
    B = "bee"
    fxn3(A,B)

#A VARIABLE IS ONLY VISIBLE IN THE SMALLEST SCOPE BOXING
######EXAMPLE 4: Scope and Order #######
def fxn4(first, second):
    print("FXN: first is ", first, "and second is", second)
    first += 11
    second = second**2	
    print("FXN:Now first is",first,"and second is",second)

def main4():
    first = 4
    second = 3.3
    print("MAIN:first is", first, "and second is", second)
    fxn4(second, first)	
    print("MAIN:first is",first,"and second is",second)	
    
    
##### EXAMPLE 6: Catch or Print #####  
def double(n):
    return 2*n

def main6():
    m=6
    double(m)
    print(m)  
    k=10
    print(double(k))
    print(k)   
    r=1.4
    r=double(r)
    print(r)

####### EXAMPLE 7: Immutable and mutable
def change1(mystring):  #meant to be on strings
    mystring = (mystring+"! ")*2
    print(mystring)

def change2(mylist): #meant to be on a list
    mylist.append("Retirement")
    print(mylist)

def main7():
    string1 = "SMC"
    change1(string1)
    print(string1)
    
    list1 = ["Union College", "Saint Mary's College"]
    change2(list1)
    print(list1)
