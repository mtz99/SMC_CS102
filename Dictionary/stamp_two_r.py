
#CS 102: Recursion for two stamps. 

def r_stamper(k ):
    print("Working on k=", k)
    if k < 0:  
      return False
    elif k==0:
        return True
    else:
       return r_stamper(k-7) or r_stamper(k-5)

def main():

    n = int(input("How much does your letter cost?: "))
    ## Try 50, then 52, then ....., 51
    
    print("That amount is .... ")
    if r_stamper(n):
        print("Possible!")
    else:
        print("Impossible")


main()
