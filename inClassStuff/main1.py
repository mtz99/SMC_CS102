from fraction import Fraction

def main():
    a = Fraction(2, 3)    
    print("a is the fraction ", a)
    
    b = Fraction(4,8)
    print("b is the fraction ", b)
    
    c = a.add(b)
    print("c is the fraction ", c)

##    print("c-a=",c.subtract(a))
    d = c.subtract(a)
    print("d is the fraction ", d)
##     
##    print("c*b=",c.multiply(b))
    e = c.mul(b)
    print("c * b is the result", e)
##
##    print("c/a=", c.divide(a))
    f = c.divide(a)
    print("c/a is the result", f)
## 
##    print("a<b is ", a.lessthan(b))
##    
##    d = Fraction(8, 10)
##    print("c=d is", c.equals(d))


main()
