# Problem: Tuples
# Platform: HackerRank
# Description: Given a list of integers, convert it into a tuple and print the hash value of the tuple.

if __name__ == '__main__':
    n = int(input())
    integer_list=input().split()
    integer_list =map(int,integer_list) 
    t=tuple(integer_list)
    print(hash(t))
