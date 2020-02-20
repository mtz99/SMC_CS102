#range(n) goes from 0 to n-1 [0,n), #=n
#rangme(m,n) is m to n-1 [m,n), # =n-m
#range(m,n,s) starts at m, s = "steps", n = first we don't want m+s+s...


'''FOR LOOPS
for <variable> in <sequence>:
    <body>

    -Assigns initial element of the sequence to the variable
    -executes <body>
    -repeats with next element of the sequence
    -continues until sequence is used up
'''


def main():
    n = int(input("Tell me a number: "))
    for i in range(3, n, 2):
        if n % i == 0:
            print(i, "divides", n)
            break

main()