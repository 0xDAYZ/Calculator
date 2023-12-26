from art import logo
from os import system, name

def clear_screen():
    if name == 'nt':
        system("cls")
    else:
        system("clear")


exit_calculator = False

def addition(first_number, second_number):
    return first_number + second_number
def subtraction(first_number, second_number):
    return first_number - second_number
def multiplication(first_number, second_number):
    return first_number * second_number
def division(first_number, second_number):
    return first_number / second_number

operations_available = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

def ask_operator():
    for operators in operations_available.keys():
        print(operators)
    operation = input("Pick an operation: ")
    return operation

try:
    while not exit_calculator:
        clear_screen()
        print(logo)
        first_number = float(input("What's the first number?: "))
        continue_calculation = True

        while continue_calculation:
            operation = ask_operator()
            second_number = float(input("What's the second number?: "))
            result = operations_available[operation](first_number, second_number)
            print(f"{"{:.2f}".format(first_number)} {operation} {"{:.2f}".format(second_number)} = {"{:.2f}".format(result)}\n")
            
            should_continue_calculation = input(f"Type 'y' to continue calculating with {"{:.2f}".format(result)}, or type 'n' to start a new calculation: ").lower()
            if should_continue_calculation == 'y':
                first_number = result
            else:
                continue_calculation = False
except KeyboardInterrupt:
    clear_screen()
    print("\nExited\n")
    exit(0)
        