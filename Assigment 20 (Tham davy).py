mid_term = int(input("Add Score Mid-term: "))
final_exam = int(input("Add Score Final Exam: "))
assignment = int(input("Add Score Assignment: "))
total_mark = mid_term + final_exam + assignment

if total_mark >= 50:
    result = "Pass"
else:
    result = "Fail"

print(f"Result {result}")
