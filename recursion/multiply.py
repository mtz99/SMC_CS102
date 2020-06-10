#CS 102 Spring 2020
# recursive multiplication

def r_mult(n, k):
    #since n*k is "n copies of k, all added"
    if n == 0:
        return 0
    else:
        return k + r_mult(n-1, k)

def main():
    print("We multiple, the recursive way!")
    first = int(input("Please give the first integer: "))
    second = int(input("Please give the second integer: "))

    ans = r_mult(first, second)
    print(first,"*",second, "=", ans)
main()
