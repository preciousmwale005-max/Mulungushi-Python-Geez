# Make a calculator that gets 2 inputs from the user 
# the calculator that can multiply, add and find the modulas of the numbers 


import math

# Global history list and memory
history = []
memory = 0.0

# Arithmetic functions
def Addition(a, c): 
    return a + c
def Subtraction(a, c): 
    return a - c
def Multiplication(a, c): 
    return a * c

def Divide(a, c):
    if c == 0:
        print ("~----------------------------------------------------------------------------------~")
        print("Error: I'm sure you are smarter an rat, Division by zero is not allowed.")
        print ("~----------------------------------------------------------------------------------~")
        return None
    return a / c

def Modulus(a, c):
    if c == 0:
        print ("~----------------------------------------------------------------------------------~")
        print("Error: Take a chill pill and try kabili, Modulus by zero is not allowed.")
        print ("~----------------------------------------------------------------------------------~")
        return None
    return a % c

def power(a, c): 
    return a ** c

def square_root(a):
    if a < 0:
        print ("~----------------------------------------------------------------------------------~")
        print("Error: Are you being serious with me, Cannot take square root of a negative number.")
        print ("~----------------------------------------------------------------------------------~")
        return None
    return math.sqrt(a)

# Input handling
def get_number_input(adon):
    while True:
        try:
            return float(input(adon))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# History functions
def update_history(expression, result):
    if result is not None:
        history.append(f"{expression} = {result}")

def display_history():
    if not history:
        print ("(----------------------------------------)")
        print("No calculations yet.")
        print ("(+--------------------------------------+)")
    else:
        print("\n--- Calculation History ---")
        for record in history:
            print(record)
        print("-----------------------------")

def clear_history():
    history.clear()
    print("History cleared.")

# Memory functions
def memory_add(value):
    global memory
    memory += value
    print(f"Memory updated: {memory}")

def memory_subtract(value):
    global memory
    memory -= value
    print(f"Memory updated: {memory}")

def memory_recall():
    print(f"Memory recall: {memory}")
    return memory

def memory_clear():
    global memory
    memory = 0.0
    print("Memory cleared.")

# Calculator menu
def calculator():
    while True:
        print("\n--- WELCOME TO PYTHON INTELLECTUAL'S CALCULATOR -------NO LIMITS TO TRYING-------------")
        print("1- Addition")
        print("2- Subtraction")
        print("3- Multiplication")
        print("4- Divide")
        print("5- Modulus")
        print("6- Power")
        print("7- Square Root")
        print("8- Show History")
        print("9- Clear History")
        print("10- Memory Add (M+)")
        print("11- Memory Subtraction (M-)")
        print("12- Memory Recall (MR)")
        print("13- Memory Clear (MC)")
        print("14- Exit")

        try:
            option = int(input("Choose an option (1-14): "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if option in [1, 2, 3, 4, 5, 6,]:
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")

            if option == 1:
                result = Addition(num1, num2)
                update_history(f"{num1} + {num2}", result)
            elif option == 2:
                result = Subtraction(num1, num2)
                update_history(f"{num1} - {num2}", result)
            elif option == 3:
                result = Multiplication(num1, num2)
                update_history(f"{num1} * {num2}", result)
            elif option == 4:
                result = Divide(num1, num2)
                update_history(f"{num1} / {num2}", result)
            elif option == 5:
                result = Modulus(num1, num2)
                update_history(f"{num1} % {num2}", result)
            elif option == 6:
                result = power(num1, num2)
                update_history(f"{num1} ^ {num2}", result)

            if result is not None:
                print("Result:", result)

        elif option == 7:
            num = get_number_input("Enter a number: ")
            result = square_root(num)
            update_history(f"√{num}", result)
            if result is not None:
                print("Result:", result)

        elif option == 8:
            display_history()

        elif option == 9:
            clear_history()

        elif option == 10:
            val = get_number_input("Enter value to add to memory: ")
            memory_add(val)

        elif option == 11:
            val = get_number_input("Enter value to subtract from memory: ")
            memory_subtract(val)

        elif option == 12:
            memory_recall()

        elif option == 13:
            memory_clear()

        elif option == 14:
            print("Thats it for now Exiting the iconic PYTHON INTERLECT calculator. Goodbye!")
            break

        else:
            print ("+----------------------------------------------------------------------------------------------------+")
            print("Are you being serious with me, the number you chose isn't even on those options. Please try again.")
            print ("==---------------------------------------------------------------------------------------------------==")

# Run the calculator
if __name__ == "__main__":
    calculator()