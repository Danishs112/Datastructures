def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + " + " + str(b) + " = " + str(answer))


def mul(a, b):
    answer = a * b
    print(str(a) + " + " + str(b) + " = " + str(answer))


def div(a, b):
    if b != 0:
        answer = a // b
    elif b == 0:
        answer = 0
    print(str(a) + " + " + str(b) + " = " + str(answer))


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Enter your choice: ")
    if choice == 'e':
        print("stop execution")
        quit()
    else:
        first_number = int(input("Enter your first number"))
        second_number = int(input("Enter your second number"))

    match choice:
        case "a":
            add(first_number, second_number)
        case "b":
            sub(first_number, second_number)

        case "c":
            mul(first_number,second_number)

        case "d":
            div(first_number,second_number)

