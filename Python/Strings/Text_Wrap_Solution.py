#problem: Text Wrap Solution
#Platform: HackerRank
#Description: Wrap a string to a specified width.

import textwrap

def wrap(string, max_width):
    if 0< len(string) < 1000 and 0< max_width < len(string):
        s= textwrap.fill(string, max_width)
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)