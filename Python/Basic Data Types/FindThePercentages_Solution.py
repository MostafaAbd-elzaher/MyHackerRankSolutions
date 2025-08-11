# Problem: Find the Percentages
# Platform: HackerRank
# Description: Given a list of student names and their scores, calculate the average score for a specific student.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    if 2 <= n <= 10 :
        for _ in range(n):
            name, *line = input().split() #put the first element in name and the rest in line list 
            scores = list(map(float, line))
            if len(scores) == 3 and all(0 <= i <=100 for i in scores) :
                student_marks[name.capitalize()] = scores
        query_name = input().capitalize()                
        if query_name in student_marks :
            avg=sum(student_marks[query_name]) / len(student_marks[query_name])
            
        print(f"{avg:.2f}") # Format the output to 2 decimal places
        