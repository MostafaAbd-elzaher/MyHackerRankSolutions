# Problem: Print Function
# Platform: HackerRank
# Description: Print the numbers from 1 to n in a single line without spaces.
# The function fun takes an integer n as input and returns a string of numbers from 1 to n concatenated together.

if __name__ == '__main__':
    def fun(n):
        if 1 <= n <= 150:  
            string=""
            for i in range(n):
                string += str(i+1)
        return string
    
n = int(input())
print(fun(n))