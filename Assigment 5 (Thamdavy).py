# Prompt user for their name
last_name = input("What is your last name? ")
first_name = input("What is your first name? ")

# Welcome message
print("Welcome, " + last_name + " " + first_name + ", nice to meet you!")

# Input midterm and final exam marks
midterm_exam = int(input("What is your midterm mark? "))
final_exam = int(input("What is your final mark? "))

# Calculate total marks
total_mark = midterm_exam + final_exam

# Display total marks
print("Your total mark is:", total_mark)
