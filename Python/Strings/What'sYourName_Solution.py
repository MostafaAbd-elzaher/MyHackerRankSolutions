# Problem: What's Your Name?
# Platform: HackerRank
# Description: Print a greeting message using the first and last name provided by the user.


def print_full_name(first, last):
    if 1 <= len(first) <= 10 and 1 <= len(last) <= 10:
        print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)