student_mark = []
i = 1

while i <= 5:
    mark = float(input("Enter the score: "))
    student_mark.append(mark)
    i += 1  # You can use i += 1 for simplicity

avg_mark = sum(student_mark) / len(student_mark)  # Correct the variable name

if avg_mark >= 50:
    print(f'Congratulations! Your average mark is {avg_mark:.2f}')  # f-string with formatting for two decimals
else:
    print(f'Try again later! Your average mark is {avg_mark:.2f}')
