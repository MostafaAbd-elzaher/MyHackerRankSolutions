# Problem: String Split and Join
# Platform: HackerRank
# Description: Split a string by spaces and join it with hyphens.

def split_and_join(line):
    n=line.split()
    return "-".join(n)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)