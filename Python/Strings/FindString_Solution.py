# Problem: Find String Occurrences
# Platform: HackerRank
# Description: Count the number of occurrences of a substring in a given string.

def count_substring(string, sub_string): #ABCDCD , CDC
    N=len(string)
    n=len(sub_string)
    if 1<= N <= 200 and n < N :
        count=0
        for i in range(N-n+1):
            if string[i:i+n] == sub_string:
                count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)