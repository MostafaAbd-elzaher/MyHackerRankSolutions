# Problem: Find the Runner-Up Score
# Platform: HackerRank
# Description: Find the second largest score in a list of integers.
#  takes a list of integers as input and returns the second largest score.

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) 
    unique_scores = list(set(arr))
    
    unique_scores.sort(reverse=True)

    print(unique_scores[1])
