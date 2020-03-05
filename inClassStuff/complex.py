class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b
    def __str__(self):
        return str(self.real) + "__+__"+str(self.imag)+"i"
        #if self.imag == 0: return 
        #elif self.imag < 0: return

class Circle:
    def __init__(self, r, x, y, c):
        self.rad = r
        self.x = x
        self.y = y
        self.color = c
    def area(self):
        return 3.141 * self.rad * self.rad

    def circum(self):
        return 2 * 3.141 *self.rad

def __add__(self, them):
    newreal = self.real + them.real
    newimag = self.imag + them.imag
    return Complex(newreal, newimag)

def __mul__(self, them):
    newreal = self.real * them.real - self.imag * them.imag
    newimag = self.imag * them.imag + self.real * them.real
    return Complex(newreal, newimag)



def main():
    m = Complex(3, 5)
    n = Complex(13, -7)
    print(n)

    me = Circle(12, 2, 7, "red")
    print(me.area())
    print(me.circum())

main()