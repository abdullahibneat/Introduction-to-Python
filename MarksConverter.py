# Input exam marks
Exam = int(input('Exam marks: '))

# Input assignment marks
Assignment = int(input('Assignment marks: '))

# If exam mark > 100
while (Exam > 100):
    # Keep asking for correct mark.
    Exam = int(input('Error: Exam marks can\'t exceed 100 marks. Please enter correct marks: '))

# If assignment mark > 100
while (Assignment > 100):
    # Keep asking for correct mark
    Assignment = int(input('Error: Assignment marks can\'t exceed 100 marks. Please enter correct marks: '))

# Multiply marks by weight percentage
ExamMarks = Exam * 0.6
AssignmentMarks = Assignment * 0.4

# Calculate overall marks
Grade = int(ExamMarks + AssignmentMarks)

# Marks >= 90
if (Grade >= 80):

    # Grade A
    print(Grade, 'marks. A grade')

# Marks between 60 and 80
elif (60 <= Grade < 80):

    # Grade B
    print(Grade, 'marks. B grade')

# Marks between 40 and 60
elif (40 <= Grade < 60):

    # Grade C
    print(Grade, 'marks. C grade')

# Grade less than 40
else:

    # Retake exam
    print(Grade, 'marks. Retake')