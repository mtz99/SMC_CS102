#CS 102 Spring 2020
# direct and recursive factorial

def direct_factorial(n):
    ans = 1
    while n>1:
        ans *= n
        n -= 1
    return ans

def rec_factorial (n):
    if n==1: 
        return 1
    else:
        return n * rec_factorial(n-1)

def main():
    n = int(input("Integer please: "))
    print(direct_factorial(n))
    print(rec_factorial(n))
main()
