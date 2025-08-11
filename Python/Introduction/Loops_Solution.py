# Problem: Loops
# Platform: HackerRank
# Description: Print the square of each number in the range from 0 to n-1.

if __name__=='__main__':
    n=int(input())
    if n in range(1,21):
        for i in range(n):
            print(i**2)
        
# The first line contains the square of each number in the range from 0 to n-1.
# The second line contains the square of each number in the range from 0 to n-
