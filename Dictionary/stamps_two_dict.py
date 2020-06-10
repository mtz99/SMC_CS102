
#CS 102: Memoization for two stamps. 

def d_stamper(k, stamps):

    if k < 0:  
      return False
    elif k in stamps:   ## CHANGE ONLY THIS LINE !! :)
       return stamps[k]
    else:
       ans =  d_stamper(k-7, stamps) or d_stamper(k-5,stamps)
       stamps[k] = ans
       return ans


def main():

    n = int(input("How much does your letter cost? "))

    stamps = {}   ## CHANGE ONLY THiS LINE !! :)
    stamps[0] = True

    print("That amount is .... ")
    if d_stamper(n, stamps):
        print("Possible!")
    else:
        print("Impossible")
    print(stamps)
    
    print("% of spots used is", len(stamps))
main()
