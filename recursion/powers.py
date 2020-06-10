#CS 102 Spring 2020
# recursive powers

#Compute a^n using recursion

#Idea:
# If n = 0 or n = 1 this is easy!
# If n is big, then a^n = a * a^(n-1)

#Pseudo-code: 
# if n == 0:
#     then ans = 1
#else: 
#    ans = a * (previous answer, with n-1)

#  Code: #assume a>0, and n>= 0 is an integer.
def power(a,n):
    if n == 0 : 
        return 1
    else:
        return a * power(a, n-1)


#
def main():
    a = int(input("Base please: "))
    n = int(input("Power power:" ))

    print(a, "to the power of ", n, "is", power(a,n))

#Modify to handle the case that n<0: 2^(-3) = 1/8.
