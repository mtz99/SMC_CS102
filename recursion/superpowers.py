#CS 102 Spring 2020
# recursive powers

#Compute a^n %  m using recursion
#
# In modern cryptography -- the type used by your phone everytime you open it --
# it is essential to be able to compute the remainder when a^n is divided 
# by m instantly. And do so when a, n and m are all huge numbers
# (e.g. m is 400 digits long!)
# Fortunately, that is possible. 

#Idea:
# If n = 0 or n = 1 this is easy!
# If n is big, then
#   if n is even e have a^n = (a^(n//2) )^2. 
#    if n is odd, then a^n = a*a^(n-1)a^n = a * a^(n-1)

# This is called 'binary exponentiation' because we are actually
# (implicitly) writing n in binary and using the 0's and 1's!

# Code
def bpower(a,n, m):
#assume a>0, and n>= 0 is an integer.
    if n == 0 : 
        return 1
    elif n%2 == 0: 
         return (bpower(a, n//2, m)**2) % m
    else:
         return a*bpower(a, n-1, m) % m


#
def main():
    a = int(input("Base please: "))
    n = int(input("Power please:" ))
    m = int(input("Modulus please:" ))

    print(a, "to the power of", n, "module", m, "is", bpower(a,n,m))
main()
#Modify to handle the case that n<0: 2^(-3) = 1/8.
