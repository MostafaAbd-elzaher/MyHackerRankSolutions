# Problem: Write a Function
# Platform: HackerRank
# Description: Determine if a year is a leap year.
# The function is_leap takes an integer year as input and returns True if the year is a leap year, otherwise returns False.
# The year is a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400.


def is_leap(year):
    # Write your logic here
    if 1900 < year < 10**5:
        if year % 4 == 0 :
            if year % 100 != 0 or year % 400 == 0 :return True
            else:return False
        else:return False
    else:return False

year = int(input())
print(is_leap(year))