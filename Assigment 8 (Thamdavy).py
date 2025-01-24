student_mark = []
i = 1

while i <= 5:
    mark = float (input("Enter the score"))
    student_mark.append(mark)
    i = i + 1

avg_mark = sum(student_mark) / len(Student_mark)
if (avg_mark >= 50):
    print ('congratulations is {avg_mark} ')
else: 
    print ('Try again later ! your mark is {avg_mark}')