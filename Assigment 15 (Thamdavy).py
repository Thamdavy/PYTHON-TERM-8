def total(a, b, c):
    sum = a + b + c
    return sum

math = int(input("Please input mark for math:"))
eng = int(input("Please input mark for english:")) # Corrected input prompt
physic = int(input("Please input mark for physics:")) # Corrected input prompt

all_mark = total(math, eng, physic)

print(all_mark)