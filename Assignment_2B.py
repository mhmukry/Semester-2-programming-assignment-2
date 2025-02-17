##Write a program that uses a list called scores initialized with 10 values. The program iterates over the list and 
# determines student’s grade for the given score, as done in week3 lesson. Student must use elif construct to determine 
# the grades based on the following criteria: score>80 is grade A, score between 70 and 80 is grade B, score between 60 
# and 70 is grade C, score between 50 and 60 is grade D and score less than 50 is grade D. Use any loop of your choice. 
# Student must provide a flowchart for this program

#Providing a list of scores of each student
score_list = [50, 76, 98, 21, 54, 87, 66, 45, 78, 96]
#For loop to go through the entire score list
for student_score in score_list:
    #Grade A if score is greater than 80
    if student_score >80:
        print(f'score: {student_score}  grade A')

    #Grade B if score is between 70 and 80
    elif student_score >= 70 and student_score <= 80:
        print(f'score: {student_score}  grade B')

    #Grade C if score is between 60 and 69
    elif student_score >= 60 and student_score < 70:
        print(f'score: {student_score}  grade C')

    #Grade D if score is between 50 and 59
    elif student_score >= 50 and student_score < 60:
        print(f'score: {student_score}  grade D')

    #Grade D if less than 50
    else:
        print(f'score: {student_score}  grade D')


    