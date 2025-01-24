i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

total = 0
number = int(input('Enter a number: '))

while number != 0:
    total += number  # total = total + number

    # take integer input again
    number = int(input('Enter a number: '))

print('total =', total)
