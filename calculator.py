history = []  # storing history
filename = "history.txt"  # file to store history

# Load previous history from file when program starts
try:
    with open(filename, "r") as file:
        history = file.read().splitlines()
except FileNotFoundError:
    history = []  # if file doesn’t exist yet, start fresh

def save_history():
    with open(filename, "w") as file:
        for record in history:
            file.write(record + "\n")

def calculator():
    try:
        num1 = float(input("Enter Number 1: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return
    
    op = input("Select your operator : + , - , * , / or history: ")

    if op.lower() == "history":
        if history:
            print("\nCalculation History:")
            for record in history:
                print(record)
        else:
            print("No calculations yet")
        return
    
    try:
        num2 = float(input("Enter Number 2: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return
    
    result = None

    if op == "+":
        result = num1 + num2
        print("Sum is", result)
    elif op == "-":
        result = num1 - num2
        print("Subtraction is", result)
    elif op == "*":
        result = num1 * num2
        print("Product is", result)
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
            print("Division is", result)
        else:
            print("Division with 0 is not possible")
    else:
        print("❌ Select a correct operator")

    # ✅ Only create record if we actually got a result
    if result is not None:
        record = f"{num1} {op} {num2} = {result}"
        history.append(record)
        save_history()

while True:
    calculator()
    choice = input("Do you want to calculate again? (y/n): ").lower()
    if choice != "y":
        print("Goodbye 👋")
        break
