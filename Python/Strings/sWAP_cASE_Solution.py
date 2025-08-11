# Problem: sWAP cASE
# Platform: HackerRank
# Description: Convert all lowercase letters to uppercase and vice versa in a given string.

def swap_case(s):
    result = ""
    if  0 < len(s) <= 1000: 
        for i in s: 
            if i.islower()  :result+=i.upper() 
            elif i.isupper() :result+=i.lower()
            else: result+=i
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)