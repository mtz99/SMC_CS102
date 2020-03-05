## Sauerberg, Spring 2020, CS 102
## Checked and works

from fullfraction import Fraction

def main():
    a = Fraction(2, 3)
    b = Fraction(4) #be able to make a fraction from an integer
    print("a is the fraction =", a)
    print("b is the fraction =", b)
    c = Fraction(4, 5)
  
    print("a+b =",a+b) #fraction + fraction  __add__
    print("a+4 =", a+4)# fraction + int __add__
    print("3+a =", 3+a) #int+fraction __radd_ cause self is on the right
    a+=b    #__iadd__   #add it 'I', to me
    print("a+=b = ", a)
    print()
    
    print("c-a =",c-a) #fraction - fraction __sub__
    print("b-2 =", b-2)     #fraction - int  __sub__
    print("3-b =",3-b)# int - fraction  __rsub__ cause self is on the right
    b -= c # __isub__   #sub from "I", from me
    print("b-=c = ", b) 
    print()
    
    print("a*b =", a*b) #fraction * fraction  __mul__
    print("b*6 =", b*6) #fraction * int  __mul__
    print("5*a = ", 5*a) #int * fraction   __rmul__
    a *= c   #__imul__ 
    print()
    
    print("c/a =", c/a) #fraction / fraction __truediv__
    print("b/2 =", b/2) #fraction/int  __trudiv__
    print("3/a =", 3/a) #int/ fraction  __rtruediv__
    b /= c  #__idiv__

    print()
    
    print("a<b is", a<b) #less than  __lt__
    print("a <= 4/6", a<=Fraction(4,6)) #  __le__
    print("a>b is", a>b) # __gt__
    print("a>=4/6", a>=Fraction(6, 9)) #__ ge__

    d = Fraction (8, 10)
    print("c==d is", c==d) # __eq__
    print("c != d is", c!=d) #__ne__

    ############## ADDITION ###############
    #Again have frac+frac, frac+int, int+frac cases
    def __add__ (self, other):
        if isinstance(other, int): ##if doing fract + int
            other = Fraction(other)
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __radd__(self, other): ##for doing int+fract
        newnum = other * self.den + self.num
        newden = self.den
        return Fraction(newnum, newden)
    
    def __iadd__(self, other): ##a += b
        return self + other
    ############## ADDITION ###############



main()
