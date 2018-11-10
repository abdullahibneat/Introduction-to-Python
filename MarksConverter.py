Exam = int(input('Exam marks: '))
Assignment = int(input('Assignment marks: '))
while (Exam > 100):
    Exam = int(input('Error: Exam marks can\'t exceed 100 marks. Please enter correct marks: '))
while (Assignment > 100):
    Assignment = int(input('Error: Assignment marks can\'t exceed 100 marks. Please enter correct marks: '))
ExamMarks = Exam * 0.6
AssignmentMarks = Assignment * 0.4
Grade = int(ExamMarks + AssignmentMarks)
print(Grade)
if (Grade >= 80):
    print('A grade')
elif (60 <= Grade < 80):
    print('B grade')
elif (40 <= Grade < 60):
    print('C grade')
else:
    print('Retake')