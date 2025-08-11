# Problem:  Arithmatic Operators
# Platform: HackerRank
# Description: Perform basic arithmetic operations on two integers.


if __name__ == '__main__':
    a=int(input())  #provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
    b=int(input())
    
    if  1 <= a <= (10**10)  and 1 <= b <= (10**10):
#The first line contains the sum of the two numbers.
        print(a+b)
#The second line contains the difference of the two numbers (first - second).
        print(a-b)
#The third line contains the product of the two numbers.
        print(a*b)
