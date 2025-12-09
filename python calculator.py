Calculator
class CalculatorWithHistory:
    def __init__(self):
        self.history = []
    def calculate(self, a, b, operator):
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                print("Error: Cannot divide by zero")
                return None
            result = a / b
        else:
            print("Error: Invalid operator")
            return None
        self.history.append(f"{a} {operator} {b} = {result}")
        return result

    def get_history(self):
        return self.history
calc = CalculatorWithHistory()
while True:
    print("\nEnter calculation (or type 'history' to view, 'exit' to quit):")
    user_input = input(">>> ").strip()
    if user_input.lower() == 'exit':
        print("Exiting calculator.")
        break
    elif user_input.lower() == 'history':
        print("\nCalculation History:")
        for entry in calc.get_history():
            print(entry)
        continue
    try:
        a, operator, b = user_input.split()
        a = float(a)
        b = float(b)
        result = calc.calculate(a, b, operator)
        if result is not None:
            print("Result:", result)
    except ValueError:
        print("Invalid input. Format: number operator number (e.g., 5 + 3)")
    except Exception as e:
        print("Error:", e)


How to run code?
Save code as calculator.py.
Open terminal in that folder.
Run:
python calculator.py


LOgical explanation

The calculator with history is designed to perform basic arithmetic operations (+, -, *, /) while keeping a record of all calculations. It is implemented using a class CalculatorWithHistory that contains two main components: a calculate method and a history list. The calculate method takes two numbers and an operator as input, performs the corresponding arithmetic operation, and stores a string of the calculation (e.g., 5 + 3 = 8) in the history list. Division by zero and invalid operators are handled to prevent errors. The get_history method returns all previous calculations, allowing users to review past results. The program can run interactively, prompting the user to enter calculations, view history, or exit. This structure separates computation from history management, making it modular and easy to extend. Overall, it provides a simple yet effective way to perform calculations and track all results for reference.

