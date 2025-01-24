# Create an empty list to hold the student marks
student_marks = []

# Get input from the user for each student mark
for i in range(5):
    mark = float(input("Enter student mark: "))
    student_marks.append(mark)

# Calculate the average student mark
average_mark = sum(student_marks) / len(student_marks)

# Check if the student passed or failed
if average_mark >= 50:
    print('Your Average mark is', average_mark)
    print('PASS')
else:
    print('Your Average mark is', average_mark)
    print("Fail")
