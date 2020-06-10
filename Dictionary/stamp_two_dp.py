
#CS 102: Dynamic Programming for two stamps. 

def d_stamper(k, stamps):
    print("trying ", k)
    if k < 0:  
      return False
    elif stamps[k] != None:
       return stamps[k]
    else:
       ans =  d_stamper(k-7, stamps) or d_stamper(k-5,stamps)
       stamps[k] = ans
       return ans


def main():

    n = int(input("How much does your letter cost? "))

    stamps = [None]*(n+1)
    stamps[0] = True

    print("That amount is .... ")
    if d_stamper(n, stamps):
        print("Possible!")
    else:
        print("Impossible")
    print(stamps)
    perc= round(100* (1- stamps.count(None)/len(stamps)),2)
    
    print(n, "% of spots actually used is", perc)
main()
