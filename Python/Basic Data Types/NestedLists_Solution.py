# Problem: Nested Lists
# Platform: HackerRank
# Description: Given the names and grades of students, find the students with the second lowest grade.
# takes a list of student records (name, grade) and returns a list of names with the second lowest grade.
if __name__ == '__main__':
    N=int(input())
    if 2 <= N <=5 :
        lis=[[input(),float(input())] for i in range(N)]
        grades=list(set([i[1] for i in lis]))
        grades.sort()
        sec_low=[i[0] for i in lis if i[1] == grades[1]]
        sec_low.sort()
        for i in sec_low:
            print(i)
