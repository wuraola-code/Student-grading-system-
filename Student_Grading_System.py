# Step 1: Welcome interphase
print('Welcome to the Student Grading System')
#Step 2:Define Variables
student_name = input("Enter your student's name: ")
num_subjects = int(input('How many subjects: '))
#Step 3:Collect subject names and scores using loops
subjects = {}
for i in range (num_subjects):
    subject = input(f'Enter name of subject {i+1}: ')
    score = int(input(f'Enter score for {subject}: '))
    subjects[subject]= score
#Step 4:Calculate total and average score
total_score = sum(subjects.values())
average_score = total_score/num_subjects
#Step 5:Assign grade based on average
if average_score >=70:
    grade = 'A'
elif (average_score >=60) and (average_score <70):
    grade = 'B'
elif (average_score >=50) and (average_score <60):
    grade = 'C'
elif (average_score >=40) and(average_score <50 ):
    grade = 'D'
else:
    grade = 'F'
#Step 6:Print full result
print('\n--- Report Card ---')
print('Student Name:', student_name)
for subject, score in subjects.items():
    print(f'{subject}:{score}')
print(f'Total Score: {total_score}')
print(f'Average Score: {average_score:.2f}')
print(f'Grade: {grade}')  