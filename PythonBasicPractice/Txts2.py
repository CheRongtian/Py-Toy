'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
'''
print("Give my two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("The second number cannot be zero!")
    else:
        print(answer)