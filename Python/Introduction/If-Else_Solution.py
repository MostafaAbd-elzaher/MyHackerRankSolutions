# Problem: If-Else
# Platform: HackerRank
# Description: print "Weird" if the number is odd or even and in the range of 6 to 20, otherwise print "Not Weird".


if __name__=='__main__':

        n = int(input())

        #sample1=3
        if n >=1 and n <=100:
            if n % 2 !=0 :
                print("Weird")
            elif n % 2 ==0 and n in range(2,6) :
                print("Not Weird")

            elif n % 2 ==0 and n in range(6,21) :
                print("Weird")
            elif n % 2 ==0 and 20 < n  :
                print("Not Weird")
        else :print ("out of the range")


     
