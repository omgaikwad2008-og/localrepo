#Calculator
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Simple Python Calculator")
    print("Supported operations: +  -  *  /")

    first = get_number("First number: ")
    operator = input("Operation: ")
    second = get_number("Second number: ")

    if operator == "+":
        print("Result:", first + second)
    elif operator == "-":
        print("Result:", first - second)
    elif operator == "*":
        print("Result:", first * second)
    elif operator == "/":
        if second == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", first / second)
    else:
        print("Invalid operation.")


main()