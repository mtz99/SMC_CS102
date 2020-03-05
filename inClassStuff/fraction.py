class Fraction:

     #constructor -- create a fraction
     def __init__(self, top = 0, bottom = 1):
          g = Fraction.gcd(top, bottom) #the gcd fxn from Fraction
          self.num = top//g
          self.den = bottom//g
     ## used as >>> myfrac = Fraction(3, 8)

     def gcd(m, n):
          while m % n != 0:
               m, n = n, m % n
          return n

     ## num and den are "instance variables". Each example of
     ## of a Fraction will have these two pieces of data in it .

    ## would like to see what a fraction looks like
    ## our first example of a "method"
     def show(self):
          print(self.num, "/", self.den)
        ## used as >>> myfrac.show()
     
    ## 'show' is fine, but we'd expect >>>print(myfrac) to work
    ## need a special method to do that.
     def __str__(self):
          return str(self.num) + "/" + str(self.den)
    ## now can use >>> print(frac)
    
     ## add two fractions. 
     def add(self, other):
          newnum = self.num * other.den + self.den * other.num
          newden = self.den * other.den
          return Fraction(newnum, newden)
     
     def __add__(self, other):
          newnum = self.num * other.den + self.den * other.num
          newden = self.den * other.den
          return Fraction(newnum, newden)
     ## used >>> myfrac.add(otherfrac)
     ## or, if a, b, c, are fractions, a = b.add(c)

     ## .mul(),
     def mul(self, other):
          newnum = self.num * other.num
          newden = self.den * other.den
          return Fraction(newnum, newden)

     ##  .subtract(),
     def subtract(self, other):
          newnum = (self.num * other.den) - self.den * other.num
          newden = self.den * other.den
          return Fraction(newnum, newden)

     ##  .divide()
     def divide(self, other):
          newnum = self.num * other.den
          newden = self.den * other.num
          return Fraction(newnum, newden)
     
     ## .equals(),
     def equals(self, other):
          if(self.num * other.den == self.den * other.num):
               return(True)
          
     ## .lessthan(),
     def lessthan(self, other):
          return(self.num * other.den < self.den * other.num)

     ## .greaterthan()
     ##  .lessequal(
     ##, .greaterequal()
     def greatereq(self, other):
          return not self.lessthan(other)
