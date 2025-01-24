def total(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum

student_a = total(60, 70, 65)
print(student_a)