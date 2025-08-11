# Problem: List Comprehensions
# Platform: HackerRank
# Description: Create a list of all possible coordinates in a 3D space defined by the ranges of x, y, and z, excluding those where the sum of the coordinates equals n.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    final_lis=[[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
    print(final_lis)
