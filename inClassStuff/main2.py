from fraction import Fraction

def main():
    a = Fraction(2, 3)    
    print("a is the fraction ", a)
    
    b = Fraction(4,8)
    print("b is the fraction ", b)
    
    c = a+b
    print("c is the fraction ", c)

    print("c-a=",c-a) 

    print("c*b=",c*b) 

    print("c/a=", c/a)
 
    print("a<b is ", a<b)
    
    d = Fraction(8, 10)
    print("c==d is", c==d)


main()
