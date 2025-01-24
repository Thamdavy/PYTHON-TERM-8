# First dictionary
a = {1: "First Name", 2: "Last name", 'age': 33}
print(a['age'])  # Prints the value associated with the key 'age'

# Second dictionary for marks
my_marks = {
    'homework': 15,
    'assignment': 22,
    'attendance': 8,
    'exam': 55
}

# Calculate total marks
total_mark = sum(my_marks.values())

# Print specific marks and total
print('My assignment mark is', my_marks['assignment'])
print('My exam mark is', my_marks['exam'])
print(f'My Total is {total_mark} and My homework is {my_marks["homework"]}')
